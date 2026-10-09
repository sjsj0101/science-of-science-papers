#!/usr/bin/env python3
"""Validate the curated data and render the catalog; Python standard library only."""
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
GENERATED = "<!-- Generated from data/papers.json by scripts/catalog.py; do not edit directly. -->"
RESERVED_ANCHORS = {"scope", "at-a-glance", "how-to-use", "browse-by-topic", "paper-index", "evidence-and-scope", "known-gaps", "maintenance", "reading-routes"}


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
    require(not seen["id"] & RESERVED_ANCHORS, "Paper ID conflicts with navigation anchor")
    anchors = set(seen["id"]) | RESERVED_ANCHORS
    sections = data.get("topic_sections")
    require(isinstance(sections, list) and sections, "Missing topic sections")
    assigned = set()
    for section in sections:
        sid = section["id"]
        require(isinstance(sid, str) and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", sid), "Invalid topic section ID")
        require(sid not in anchors, f"Duplicate anchor: {sid}")
        anchors.add(sid)
        require(all(isinstance(section.get(k), str) and section[k].strip() for k in ("title", "description_zh")), f"Empty topic section: {sid}")
        refs = section["paper_ids"]
        require(isinstance(refs, list) and refs and all(isinstance(pid, str) for pid in refs) and len(refs) == len(set(refs)) and set(refs) <= seen["id"], f"Invalid topic section references: {sid}")
        require(not assigned.intersection(refs), f"Paper assigned to multiple topic sections: {sid}")
        assigned.update(refs)
    require(assigned == seen["id"], "Topic sections must cover every paper exactly once")
    require(log["snapshot_date"] == data["snapshot_date"], "Search log date mismatch")
    require(log["coverage_claim"] == "none", "Searches do not prove exhaustive coverage")
    for search in log["searches"]:
        require(all(search.get(k) for k in ("query", "source", "scope_zh", "limitations_zh")), "Incomplete search record")
        require(date.fromisoformat(search["checked_on"]) <= cutoff, "Future search date")
    for c in log["candidates"]:
        require(c["title"] and check_url(c["url"]) and c["reason_zh"], "Incomplete candidate")
        require(c["decision"] in {"pending", "out-of-scope", "excluded"}, "Invalid candidate decision")
    return papers


def markdown_cell(value):
    return str(value).replace("|", "&#124;").replace("\n", " ")


def paper_locations(data):
    return {pid: f"topics/{section['id']}.md#{pid}"
            for section in data["topic_sections"] for pid in section["paper_ids"]}


def render(data, log):
    papers = data["papers"]
    lookup = {p["id"]: p for p in papers}
    locations = paper_locations(data)
    counts = Counter(p["collection"] for p in papers)
    decisions = Counter(c["decision"] for c in log["candidates"])
    years = [p["year"] for p in papers]
    out = [GENERATED, "# Science of Science · AI 与科研", "", data["description_zh"], "",
           f"**{len(papers)} 篇论文 · {len(data['topic_sections'])} 个研究主题 · 中文导读**", "",
           f"文献检索与核验截止：**{data['snapshot_date']}**。收录年份：**{min(years)}–{max(years)}**。精选目录，不声称系统综述或完整 venue-year 覆盖。", "",
           '<a id="scope"></a>', "", "## 研究范围", ""]
    out.extend(f"- {s}" for s in data["scope"]["include_zh"])
    out += ["", "不纳入：" + "；".join(data["scope"]["exclude_zh"]) + "。", "", data["scope"]["year_policy_zh"], "", data["scope"]["source_policy_zh"], "",
            '<a id="at-a-glance"></a>', "", "## 目录概览", "", "| 项目 | 数量 |", "| --- | ---: |",
            f"| 收录论文 | {len(papers)} |",
            f"| SoS 核心（AI 与科研 / 经典与制度） | {counts['ai-core'] + counts['foundations']}（{counts['ai-core']} / {counts['foundations']}） |",
            f"| 交叉研究 / 技术背景 | {counts['cross-disciplinary']} / {counts['technical-background']} |",
            f"| 补充预印本 / 待核验候选 | {counts['supplement']} / {decisions['pending']} |", "",
            "主题回答“这篇研究在讨论什么”；研究定位说明它与 SoS 主线的关系。两者独立：同一主题可以包含核心研究、元研究和技术背景，后两者会逐条标明。", "",
            '<a id="how-to-use"></a>', "", "## 如何使用", "",
            "- 找研究问题：从下面的主题导航进入，每个主题使用相同的论文表格和详情格式。",
            "- 找阅读顺序：[建议阅读路线](docs/reading-routes.md) · [研究问题与阅读方法](docs/reading-guide.md)。",
            "- 查证据：表格题名直达论文，点击“解读与来源”查看作者、摘要、限制和核验记录。",
            "- 维护目录：[主数据](data/papers.json) · [检索与候选记录](data/search-log.json) · [维护说明](CONTRIBUTING.md)。", "",
            '<a id="browse-by-topic"></a>', "", "## 按研究主题浏览", "",
            "每篇按主要研究问题归入一个主题，以下数量可相加为目录总数；阅读路线和细分标签允许交叉。主题内顺序为编辑阅读建议，方法批评与被讨论论文尽量相邻。", "",
            "| 主题 | 篇数 | 完整条目 |", "| --- | ---: | --- |"]
    for section in data["topic_sections"]:
        out.append(f"| [{section['title']}](#{section['id']}) | {len(section['paper_ids'])} | [主题页](topics/{section['id']}.md) |")
    out += ["", '<a id="paper-index"></a>', "", "## 论文索引"]
    for section in data["topic_sections"]:
        out += ["", f'<a id="{section["id"]}"></a>', "", "### " + section["title"], "", section["description_zh"], "",
                "| 年份 / 来源 | 论文 | 为什么读 | 研究定位 |", "| --- | --- | --- | --- |"]
        for pid in section["paper_ids"]:
            p = lookup[pid]
            # Keep existing README links useful while full entries live on topic pages.
            title = f'<a id="{pid}"></a>[{markdown_cell(p["title"])}]({p["url"]})<br>[解读与来源]({locations[pid]})'
            out.append(f"| {p['year']} · {markdown_cell(p['venue'])}<br>{TYPES[p['publication_type']]} | {title} | {markdown_cell(p['relevance_zh'])} | {COLLECTIONS[p['collection']]} |")
    out += ["", '<a id="evidence-and-scope"></a>', "", "## 研究定位与证据口径", "",
            "| 研究定位 | 去重条目数 |", "| --- | ---: |"]
    out.extend(f"| {label} | {counts[key]} |" for key, label in COLLECTIONS.items())
    out += ["", "前两类合计为 SoS 核心；经典机制不直接证明 AI 效果，技术系统的任务表现不直接代表科学整体收益。研究定位是编辑判断，不是论文质量排名。", "",
            f"未收录候选：待核验 {decisions['pending']}、范围外 {decisions['out-of-scope']}、排除 {decisions['excluded']}；不计入论文总数。", "",
            "已发表条目类型：" + "、".join(f"{TYPES[k]} {v} 篇" for k, v in sorted(Counter(p["publication_type"] for p in papers if p["publication_status"] == "published").items())) + "。观点与综述分别标注。", "",
            "内容阅读层次：" + "、".join(f"{EVIDENCE[k]} {v} 篇" for k, v in sorted(Counter(p["evidence_level"] for p in papers).items())) + "。来源访问、发表身份和阅读深度逐篇说明；**未独立复现实验。**", "",
            '<a id="known-gaps"></a>', "", "## 已知缺口", ""]
    out.extend(f"- {gap}" for gap in data["scope"]["gaps_zh"])
    out += ["", '<a id="maintenance"></a>', "", "## 维护", "",
            "`data/papers.json` 是唯一论文主数据；README、主题页和阅读路线由同一脚本生成。参考 good_llm_stats_papers 的主题导航和中文表格，以及 good-quant-ai-papers 的首页与详情分离方式，按本仓库规模保留单脚本维护。", "",
            "```sh", "python3 scripts/catalog.py --write", "python3 scripts/catalog.py --check", "python3 -m unittest discover -s tests", "git diff --check", "```", "",
            "生成检查覆盖主题全量归属、字段与去重、所有生成页一致性及本地链接；不访问网络或核验科学结论。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。", "",
            "本仓库仅保存论文元数据、原创中文导读与来源链接；论文、图表、数据集和外部代码仍按各自权利与许可使用。"]
    return "\n".join(out).rstrip() + "\n"


def render_topic(data, section):
    lookup = {p["id"]: p for p in data["papers"]}
    out = [GENERATED, "# " + section["title"], "",
           f"[返回主题目录](../README.md#{section['id']}) · [阅读路线](../docs/reading-routes.md) · [阅读方法](../docs/reading-guide.md)", "",
           section["description_zh"], "",
           f"本主题 {len(section['paper_ids'])} 篇。以下保留每篇研究的定位、文章类型和证据边界；书目核验日期沿用各条目记录。", "", "## 阅读顺序", ""]
    out.extend(f"{i}. [{lookup[pid]['title']}](#{pid})（{lookup[pid]['year']}）" for i, pid in enumerate(section["paper_ids"], 1))
    for pid in section["paper_ids"]:
        p = lookup[pid]
        authors = "; ".join(p["authors"]) + ("（作者名单未完整核实）" if not p["authors_complete"] else "")
        out += ["", f'<a id="{pid}"></a>', "", f"## {p['title']}", "",
                f"**{p['year']} · {p['venue']} · {TYPES[p['publication_type']]}**", "",
                "**研究定位：**" + COLLECTIONS[p["collection"]], "", authors, "",
                f"[论文]({p['url']}) · [正式来源]({p['official_url']})" + (f" · [代码]({p['code_url']})" if p.get("code_url") else ""), "",
                p["summary_zh"], "", "**为什么读：**" + p["relevance_zh"], "", "**限制：**" + p["limitations_zh"], "",
                "标签：" + " / ".join(data["tags"][t] for t in p["tags"]), "", "<details>",
                f"<summary>核验记录 · {p['verified_on']} · {EVIDENCE[p['evidence_level']]}</summary>", "", p["verification_note_zh"], ""]
        out.extend(f"- [{s['role']}]({s['url']})：{s['note_zh']}" for s in p["sources"])
        out += ["", "</details>"]
    return "\n".join(out).rstrip() + "\n"


def render_reading_routes(data):
    lookup = {p["id"]: p for p in data["papers"]}
    locations = paper_locations(data)
    out = [GENERATED, '<a id="reading-routes"></a>', "", "# 建议阅读路线", "",
           "[返回主题目录](../README.md#browse-by-topic) · [研究问题与阅读方法](reading-guide.md)", "",
           "阅读路线可以跨主题，是编辑建议而非质量排名，也不承担全目录覆盖。完整分类见首页；以下题名直达对应论文的详细条目。"]
    for route in data["reading_routes"]:
        out += ["", "## " + route["title"], "", route["description_zh"], ""]
        out.extend(f"{i}. [{lookup[pid]['title']}](../{locations[pid]})（{lookup[pid]['year']}）" for i, pid in enumerate(route["paper_ids"], 1))
    out += ["", "科学文献的发表、写作、引用和摘要专题另有完整顺序，见 [科学文献主题页](../topics/scientific-literature.md)。"]
    return "\n".join(out).rstrip() + "\n"


def render_outputs(data, log):
    outputs = {"README.md": render(data, log), "docs/reading-routes.md": render_reading_routes(data)}
    outputs.update({f"topics/{section['id']}.md": render_topic(data, section) for section in data["topic_sections"]})
    return outputs


def check_local_links():
    for path in [ROOT / "README.md", ROOT / "CONTRIBUTING.md", *sorted((ROOT / "docs").glob("*.md")), *sorted((ROOT / "topics").glob("*.md"))]:
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
    mode.add_argument("--write", action="store_true", help="Validate data, then regenerate all catalog pages")
    mode.add_argument("--check", action="store_true", help="Validate without modifying files")
    args = parser.parse_args()
    data = json.loads((ROOT / "data/papers.json").read_text(encoding="utf-8"))
    log = json.loads((ROOT / "data/search-log.json").read_text(encoding="utf-8"))
    papers = validate(data, log)
    outputs = render_outputs(data, log)
    unexpected = set((ROOT / "topics").glob("*.md")) - {ROOT / name for name in outputs}
    require(not unexpected, "Unexpected topic files; migrate explicitly: " + ", ".join(sorted(p.name for p in unexpected)))
    for filename, expected in outputs.items():
        path = ROOT / filename
        if args.write:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(expected, encoding="utf-8")
        else:
            require(path.read_text(encoding="utf-8") == expected, f"{filename} differs: run --write")
    check_local_links()
    print(f"OK: {len(papers)} papers; {dict(Counter(p['collection'] for p in papers))}; {len(log['searches'])} search records; {len(log['candidates'])} candidates; all {len(outputs)} generated pages and local links consistent")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, TypeError, OSError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
