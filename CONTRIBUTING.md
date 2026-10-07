# 维护说明

本仓库研究 AI 如何改变科研生产、创新与学术生态。以直接讨论科研过程、科学知识或科研制度的研究为主，辅以少量 Science of Science 背景。它不是通用 AI for Science 应用大全或科研 Agent 排行榜。

## 收录与来源

1. 主目录 `ai-core` 与背景 `foundations` 仅收正式期刊或会议论文；综述、观点与研究论文分开标注。不限制固定 venue 清单，会议论文必须核对实际 track。
2. 必要的未发表研究放入 `supplement`，明确标为预印本；有重要身份或内容疑点的候选留在 `data/search-log.json`，不计入论文总数。
3. 以期刊页、proceedings 或官方 OpenReview 核实发表身份。出版商不可直接访问时，可使用原始出版页面的可读索引，或由作者机构、PMC、资助机构保留的正式排印版本交叉核验，逐条说明限制。仅有作者宣称、搜索标题或 arXiv 投稿记录不足以证明接收。
4. `sources` 必须说明实际读取的来源及用途。`official_url` 是规范出版入口，不表示本次一定直接访问成功。摘要、部分正文、全文阅读和实验复现不能互相替代；读取预印本内容配合正式书目信息时说明版本差异。
5. 中文短评用原创表述说明问题、方法、作者发现、关联与限制。数字结论须有对应正文证据；观察性关联不写成因果。观点框架不能写成已验证的制度效果。
6. 留意更正、撤回、方法批评及作者回复；不要把仍在争论的结论写成定论。批评和回复可以先作为关联来源，是否独立收录另作编辑决定。

## 唯一主数据

`data/papers.json` 是论文目录唯一主数据，`README.md` 由 `scripts/catalog.py` 生成，不能直接编辑。`docs/reading-guide.md` 是人工维护的研究问题导读。`data/search-log.json` 只记录检索与未收录候选，不是第二份论文主数据。

顶层字段：

| 字段 | 含义 |
| --- | --- |
| `schema_version` | 当前为 1 |
| `snapshot_date` | 本版实际检索截止日，ISO 日期 |
| `description_zh`、`scope` | 研究问题、纳入/排除、年份与来源口径、已知缺口 |
| `tags` | 标签到中文名称的映射；允许跨主题 |
| `reading_routes` | 以稳定论文 ID 引用的阅读顺序 |
| `experiments_reproduced` | 当前为 false；本地结构检查不改变它 |
| `papers` | 去重后的论文记录 |

每篇记录：

| 字段 | 含义与约束 |
| --- | --- |
| `id` | 稳定、唯一、英文小写及连字符；题名或链接变化尽量不换 ID |
| `collection` | `ai-core`、`foundations`、`supplement` |
| `title`、`authors`、`authors_complete` | 原文题名、已确认作者数组、名单是否完整 |
| `year`、`venue` | 正式卷期年和出版物；未分配卷期时用官方在线发表年；预印本用所读版本年 |
| `publication_type` | `journal-research`、`conference-paper`、`review`、`perspective`、`policy-analysis`、`preprint`；Letter/Article/Brief Report统一为研究，Policy Forum/评论映射为观点，Policy Article单列为政策分析（含实证），在记录中保留原始分类 |
| `publication_status` | 已发表 `published` 或补充预印本 `preprint` |
| `doi` | 确认的裸 DOI；未知为 null，不猜填 |
| `url`、`official_url` | 主入口与规范出版/预印本入口 |
| `tags` | 必须来自顶层标签表，无重复 |
| `summary_zh`、`limitations_zh`、`relevance_zh` | 原创概要、解释边界、与本仓库的关系 |
| `evidence_level` | `abstract`、`selected-full-text`、`full-text`，描述内容阅读深度 |
| `verified_on`、`verification_note_zh` | 实际核验日期与具体证据/访问/版本限制 |
| `sources` | 至少一个 `publication` 来源；另可用 `content`、`metadata`；每项有 URL 与说明 |
| `code_url` | 可选；仅在论文的代码声明等可信出处明确提供后添加 |

不要求所有论文有精确发表日；尚未核实就不添加。`verified_on` 不能替代发表日，也不表示已复现。按 DOI、规范化标题和链接查重，并人工确认预印本与正式版本的关系；不能仅因题名相似合并两项研究。

## 检索与候选

新增检索记录至少保存 `query`、`source`、`checked_on`、`scope_zh` 与 `limitations_zh`。当前 `coverage_claim` 为 `none`：记录的是关键词发现和定向核验，不是按 venue-year 全量筛查。

未收录候选使用 `pending`（待进一步核验或评估）、`out-of-scope`、`excluded`，写明理由。已收录正式版对应的旧版本可在排除台账中保留为版本线索。没有入选不意味着不存在或质量差。若将来宣称覆盖某些 venue-year 单元，应另外记录已筛查的 track、分页与缺口，不能由论文数推断覆盖完成。

## 更新顺序与验证

先读 README、主数据、本说明和本机 `HANDOFF.md`；确认 Git 分支与用户改动。然后检索、查重与核验，修改主数据和必要检索记录，更新导读，再执行：

```sh
python3 scripts/catalog.py --write
python3 scripts/catalog.py --check
git diff --check
git status --short
```

需要 Python 3.9 或以上，仅依赖标准库。`--write` 在验证数据后生成 README；`--check` 不修改文件，核对结构、必填字段、受控值、ID/DOI/标题/主链接重复、日期、阅读顺序、README统计与全文一致性、Markdown相对链接及显式锚点。日期检查使用执行机当前日期；快照日期按维护者实际研究日期记录。

脚本不访问网络、不核实论文科学结论；来源访问、发表身份及实验复现须分别记录。改生成逻辑时同时核对输出差异；修改数据后无须为了可逆文档变更新增镜像测试。提交前检查实际将发布的文件，不把临时检索全文、PDF、凭据和本机资料纳入。

阶段完成后更新本机 `HANDOFF.md` 的六个章节，保持 `/HANDOFF.md` 在 `.git/info/exclude` 中。公开文件使用相对路径；不放私人会话、本机绝对路径或原始下载。是否创建远端、推送及其可见性按用户当次要求决定。
