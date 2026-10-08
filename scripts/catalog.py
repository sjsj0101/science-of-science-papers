#!/usr/bin/env python3
"""Validate the curated data and render README; Python standard library only."""
import argparse
from collections import Counter
from datetime import date
import json
from pathlib import Path
import re
import sys
import unicodedata
from urllib.parse import parse_qsl, unquote, urlencode, urlsplit

ROOT = Path(__file__).resolve().parents[1]
COLLECTIONS = {
    "ai-core": "SoS 核心 · AI 与科研",
    "foundations": "SoS 核心 · 经典与科研制度",
    "cross-disciplinary": "元研究、理论与治理",
    "technical-background": "技术背景与案例",
    "supplement": "补充预印本",
}
TYPES = {"journal-research": "期刊研究", "conference-paper": "会议论文", "review": "综述", "perspective": "观点 / 评论", "policy-analysis": "政策分析（含实证）", "preprint": "预印本"}
EVIDENCE = {"abstract": "摘要", "selected-full-text": "部分正文 / 图表", "full-text": "全文"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def norm(text):
    return "".join(c for c in unicodedata.normalize("NFKC", text).casefold() if c.isalnum())


def url_key(value):
    u = urlsplit(value)
    host = u.netloc.lower().removeprefix("www.")
    path = unquote(u.path).rstrip("/")
    if host == "doi.org":
        path = path.lower()
    # Keep document IDs and other meaningful query parameters; remove tracking only.
    query = [(k, v) for k, v in parse_qsl(u.query, keep_blank_values=True)
             if not k.lower().startswith("utm_") and k.lower() not in {"fbclid", "gclid"}]
    return (host, path, urlencode(sorted(query)))


def check_url(value):
    return isinstance(value, str) and urlsplit(value).scheme == "https" and bool(urlsplit(value).netloc)


def validate(data, log):
    require(data["schema_version"] == 1, "Unknown schema version")
    cutoff = date.fromisoformat(data["snapshot_date"])
    require(cutoff <= date.today(), "Snapshot is in the future")
    require(data["scope"]["coverage"] == "curated-not-exhaustive", "Coverage must remain explicit")
    require(data["experiments_reproduced"] is False, "Do not infer experiment reproduction from validation")
    papers = data["papers"]
    require(bool(papers), "Empty paper catalog")
    seen = {key: set() for key in ("id", "title", "doi", "url")}
    strings = ("id", "title", "venue", "url", "official_url", "summary_zh", "limitations_zh", "relevance_zh", "verification_note_zh")
    for p in papers:
        for key in strings:
            require(isinstance(p.get(key), str) and p[key].strip(), f"Missing {key}: {p.get('id')}")
        pid = p["id"]
        require(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", pid), f"Invalid ID: {pid}")
        require(p["collection"] in COLLECTIONS, f"Invalid collection: {pid}")
        require(p["publication_type"] in TYPES, f"Invalid type: {pid}")
        require(p["evidence_level"] in EVIDENCE, f"Invalid evidence: {pid}")
        require(type(p["year"]) is int and 1900 <= p["year"] <= cutoff.year, f"Invalid year: {pid}")
        require(type(p["authors_complete"]) is bool, f"Invalid author flag: {pid}")
        require(isinstance(p["authors"], list) and p["authors"] and all(isinstance(a, str) and a.strip() for a in p["authors"]), f"Missing authors: {pid}")
        require(len(p["authors"]) == len(set(p["authors"])), f"Duplicate author: {pid}")
        require(p["tags"] and len(p["tags"]) == len(set(p["tags"])) and set(p["tags"]) <= set(data["tags"]), f"Invalid tags: {pid}")
        require(date.fromisoformat(p["verified_on"]) <= cutoff, f"Verification after cutoff: {pid}")
        if p["collection"] == "supplement":
            require(p["publication_status"] == "preprint" and p["publication_type"] == "preprint", f"Supplement status mismatch: {pid}")
        else:
            require(p["publication_status"] == "published" and p["publication_type"] != "preprint", f"Main entry lacks publication: {pid}")
        for key in ("url", "official_url"):
            require(check_url(p[key]), f"Invalid {key}: {pid}")
        if p.get("code_url"):
            require(check_url(p["code_url"]), f"Invalid code URL: {pid}")
        doi = p.get("doi")
        require(doi is None or (isinstance(doi, str) and re.fullmatch(r"10\.\d{4,9}/\S+", doi)), f"Invalid DOI: {pid}")
        for key, value in (("id", pid), ("title", norm(p["title"])), ("doi", doi.casefold() if doi else None), ("url", url_key(p["url"]))):
            if value is not None:
                require(value not in seen[key], f"Duplicate {key}: {pid}")
                seen[key].add(value)
        require(p["sources"], f"No evidence source: {pid}")
        require(any(s["role"] == "publication" for s in p["sources"]), f"No publication evidence: {pid}")
        for s in p["sources"]:
            require(check_url(s["url"]) and s["role"] in {"publication", "content", "metadata"} and bool(s["note_zh"]), f"Invalid source: {pid}")
    for route in data["reading_routes"]:
        require(route["title"] and route["description_zh"], "Empty reading route")
        require(route["paper_ids"] and len(route["paper_ids"]) == len(set(route["paper_ids"])) and set(route["paper_ids"]) <= seen["id"], "Invalid reading route references")
    anchors = set(seen["id"])
    for section in data.get("topic_sections", []):
        sid = section["id"]
        require(isinstance(sid, str) and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", sid), "Invalid topic section ID")
        require(sid not in anchors, f"Duplicate anchor: {sid}")
        anchors.add(sid)
        require(all(isinstance(section.get(k), str) and section[k].strip() for k in ("title", "description_zh")), f"Empty topic section: {sid}")
        refs = section["paper_ids"]
        require(isinstance(refs, list) and refs and len(refs) == len(set(refs)) and set(refs) <= seen["id"], f"Invalid topic section references: {sid}")
    require(log["snapshot_date"] == data["snapshot_date"], "Search log date mismatch")
    require(log["coverage_claim"] == "none", "Searches do not prove exhaustive coverage")
    for search in log["searches"]:
        require(all(search.get(k) for k in ("query", "source", "scope_zh", "limitations_zh")), "Incomplete search record")
        require(date.fromisoformat(search["checked_on"]) <= cutoff, "Future search date")
    for c in log["candidates"]:
        require(c["title"] and check_url(c["url"]) and c["reason_zh"], "Incomplete candidate")
        require(c["decision"] in {"pending", "out-of-scope", "excluded"}, "Invalid candidate decision")
    return papers


def render(data, log):
    papers = data["papers"]
    lookup = {p["id"]: p for p in papers}
    counts = Counter(p["collection"] for p in papers)
    decisions = Counter(c["decision"] for c in log["candidates"])
    years = [p["year"] for p in papers]
    out = ["<!-- Generated from data/papers.json by scripts/catalog.py; do not edit directly. -->", "# Science of Science · AI 与科研", "", data["description_zh"], "", f"检索与核验截止：**{data['snapshot_date']}**。当前收录年份：**{min(years)}–{max(years)}**。这是按问题组织的精选目录，不是系统综述或完整 venue-year 覆盖。", "", "## 范围与入口", ""]
    out.extend(f"- {s}" for s in data["scope"]["include_zh"])
    entry_links = "入口：[研究问题与阅读方法](docs/reading-guide.md) · [主数据](data/papers.json) · [检索与候选记录](data/search-log.json) · [维护说明](CONTRIBUTING.md)"
    entry_links += "".join(f" · [{s['title']}](#{s['id']})" for s in data.get("topic_sections", []))
    out += ["", "不纳入：" + "；".join(data["scope"]["exclude_zh"]) + "。", "", data["scope"]["year_policy_zh"], "", data["scope"]["source_policy_zh"], "", entry_links, "", "## 数量与证据口径", "", "| 分层 | 去重条目数 |", "| --- | ---: |"]
    out.extend(f"| {label} | {counts[key]} |" for key, label in COLLECTIONS.items())
    out += [f"| 合计 | {len(papers)} |",
        "",
        f"SoS 核心合计 {counts['ai-core'] + counts['foundations']} 篇；交叉研究 {counts['cross-disciplinary']} 篇；技术背景与案例 {counts['technical-background']} 篇。分层是按研究对象与主要贡献作出的编辑判断，不是互斥的学科归属；经典文献仍属于 SoS，技术案例不计入核心。",
        "",
        f"未收录候选单列：待核验 {decisions['pending']} 条，范围外 {decisions['out-of-scope']} 条，排除 {decisions['excluded']} 条；不计入上表。",
        "",
        "已发表条目的类型：" + "、".join(f"{TYPES[k]} {v} 篇" for k,
        v in sorted(Counter(p["publication_type"] for p in papers if p["publication_status"] == "published").items())) + "。观点与综述单独标注，不能当作实证结论。",
        "",
        "内容阅读层次：" + "、".join(f"{EVIDENCE[k]} {v} 篇" for k,
        v in sorted(Counter(p["evidence_level"] for p in papers).items())) + "。阅读层次与发表身份核验是两个维度；搜索索引中的原文片段、访问失败与订阅限制逐条说明。**未独立复现实验。**",
        "",
        "主题标签允许交叉：" + "、".join(f"{data['tags'][k]} {v}" for k,
        v in Counter(t for p in papers for t in p["tags"]).most_common()) + "。标签数不能相加作为论文总数。",
        "",
        "## 建议阅读路线",
        "",
        "顺序是编辑建议，不是质量排名。"]
    for route in data["reading_routes"]:
        out += ["", "### " + route["title"], "", route["description_zh"], ""]
        out.extend(f"{i}. [{lookup[pid]['title']}](#{pid})（{lookup[pid]['year']}）" for i, pid in enumerate(route["paper_ids"], 1))
    for section in data.get("topic_sections", []):
        subset = [lookup[pid] for pid in section["paper_ids"]]
        out += ["", f'<a id="{section["id"]}"></a>', "", "## " + section["title"], "", section["description_zh"], "", f"本主题引用 {len(subset)} 篇已收录论文，沿用原分层，不重复计数；点击题名查看完整书目、来源与限制。", "", "| 论文 | 关注问题 | 分层 |", "| --- | --- | --- |"]
        out.extend(f"| [{p['title']}](#{p['id']})（{p['year']}） | {p['relevance_zh'].replace('|', '&#124;')} | {COLLECTIONS[p['collection']]} |" for p in subset)
    for collection, label in COLLECTIONS.items():
        subset = sorted((p for p in papers if p["collection"] == collection), key=lambda p: (-p["year"], p["id"]))
        out += ["", "## " + label, ""]
        if not subset:
            out.append("本版无条目；不代表不存在相关研究。")
        for p in subset:
            authors = "; ".join(p["authors"]) + ("（作者名单未完整核实）" if not p["authors_complete"] else "")
            out += [f'<a id="{p["id"]}"></a>', "", f"### {p['title']}", "", f"**{p['year']} · {p['venue']} · {TYPES[p['publication_type']]}**", "", authors, "", f"[论文]({p['url']}) · [正式来源]({p['official_url']})" + (f" · [代码]({p['code_url']})" if p.get("code_url") else ""), "", p["summary_zh"], "", "**为什么读：**" + p["relevance_zh"], "", "**限制：**" + p["limitations_zh"], "", "标签：" + " / ".join(data["tags"][t] for t in p["tags"]), "", "<details>", f"<summary>核验记录 · {p['verified_on']} · {EVIDENCE[p['evidence_level']]}</summary>", "", p["verification_note_zh"], ""]
            out.extend(f"- [{s['role']}]({s['url']})：{s['note_zh']}" for s in p["sources"])
            out += ["", "</details>", ""]
    out += ["## 已知缺口", ""]
    out.extend(f"- {gap}" for gap in data["scope"]["gaps_zh"])
    out += ["", "## 维护", "", "仅修改主数据及必要导读，再生成索引：", "", "```sh", "python3 scripts/catalog.py --write", "python3 scripts/catalog.py --check", "git diff --check", "```", "", "检查涵盖结构、受控值、稳定ID、规范化DOI/标题/主链接重复、阅读引用、日期、README一致性及本地Markdown链接；不会访问远程来源，也不能证明研究结论成立。详细约定见 [CONTRIBUTING.md](CONTRIBUTING.md)。", "", "本仓库仅保存论文元数据、原创中文导读与来源链接；论文、图表、数据集和外部代码仍按各自权利与许可使用。"]
    return "\n".join(out).rstrip() + "\n"


def check_local_links():
    for path in [ROOT / "README.md", ROOT / "CONTRIBUTING.md", *sorted((ROOT / "docs").glob("*.md"))]:
        contents = re.sub(r"```.*?```", "", path.read_text(encoding="utf-8"), flags=re.S)
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", contents):
            if urlsplit(target).scheme:
                continue
            filename, _, anchor = unquote(target).partition("#")
            resolved = (path.parent / filename).resolve() if filename else path
            require(resolved.is_relative_to(ROOT) and resolved.is_file(), f"Broken local link in {path.name}: {target}")
            if anchor:
                require(f'id="{anchor}"' in resolved.read_text(encoding="utf-8"), f"Missing explicit anchor: {target}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true", help="Validate data, then regenerate README")
    mode.add_argument("--check", action="store_true", help="Validate without modifying files")
    args = parser.parse_args()
    data = json.loads((ROOT / "data/papers.json").read_text(encoding="utf-8"))
    log = json.loads((ROOT / "data/search-log.json").read_text(encoding="utf-8"))
    papers = validate(data, log)
    expected = render(data, log)
    readme = ROOT / "README.md"
    if args.write:
        readme.write_text(expected, encoding="utf-8")
    else:
        require(readme.read_text(encoding="utf-8") == expected, "README differs: run --write")
    check_local_links()
    print(f"OK: {len(papers)} papers; {dict(Counter(p['collection'] for p in papers))}; {len(log['searches'])} search records; {len(log['candidates'])} candidates; README and local links consistent")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, TypeError, OSError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
