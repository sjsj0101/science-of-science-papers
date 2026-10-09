<!-- Generated from data/papers.json by scripts/catalog.py; do not edit directly. -->
# 科学文献：形成、传播与失真

[返回主题目录](../README.md#scientific-literature) · [阅读路线](../docs/reading-routes.md) · [阅读方法](../docs/reading-guide.md)

哪些结果进入文献，AI 如何参与写作，学术注意力与科学主张又怎样在引用、摘要和综合中分配或失真？沿发表选择、证据报告、辅助写作、注意力分配和转述保真展开；语料层面的采用测量、机制模型与系统评测分别解释。

本主题 10 篇。以下保留每篇研究的定位、文章类型和证据边界；书目核验日期沿用各条目记录。

## 阅读顺序

1. [Identification of and Correction for Publication Bias](#andrews-2019-publication-bias)（2019）
2. [A Model of Scientific Communication](#andrews-2021-scientific-communication)（2021）
3. [Delving into LLM-assisted writing in biomedical publications through excess vocabulary](#kobak-2025-llm-excess-vocabulary)（2025）
4. [Quantifying large language model usage in scientific papers](#liang-2025-quantifying-llm-scientific-papers)（2025）
5. [Slowed canonical progress in large fields of science](#chu-2021-slowed-canonical-progress)（2021）
6. [The Noisy Path from Source to Citation: Measuring How Scholars Engage with Past Research](#chen-2025-noisy-path)（2025）
7. [Large Language Models Reflect Human Citation Patterns with a Heightened Citation Bias](#algaba-2025-heightened-citation-bias)（2025）
8. [Quantifying the prevalence and impact of overreaching causal claims in social science](#isch-2026-overreaching-causal-claims)（2026）
9. [Generalization bias in large language model summarization of scientific research](#peters-2025-generalization-bias)（2025）
10. [Synthesizing scientific literature with retrieval-augmented language models](#asai-2026-openscholar)（2026）

<a id="andrews-2019-publication-bias"></a>

## Identification of and Correction for Publication Bias

**2019 · American Economic Review · 期刊研究**

**研究定位：**SoS 核心 · 经典与科研制度

Isaiah Andrews; Maximilian Kasy

[论文](https://www.aeaweb.org/articles?id=10.1257/aer.20180310) · [正式来源](https://www.aeaweb.org/articles?id=10.1257/aer.20180310) · [代码](https://doi.org/10.3886/E116208V1)

研究结果被选择性发表后，读者如何从已发表文献进行统计推断。作者提出两条识别路径，分别利用系统性复现研究和元研究数据估计发表概率如何随研究结果变化，并在已知条件发表概率时构造偏差校正的估计与置信集合。正式摘要报告了实验经济学、心理学复现数据及最低工资元研究的应用，为评估文献证据受发表选择影响的程度提供方法。

**为什么读：**直接研究科学文献的选择机制和可信推断，是理解系统综述、AI 检索与文献综合所面对的证据偏差的基础方法论文。

**限制：**校正需要关于发表选择过程的假设及足够的复现或元研究数据；不是只凭已发表论文就能无条件恢复全部未发表结果。本文不能自动消除研究设计、测量或数据质量造成的偏差；本轮未复现估计，也未将旧稿应用或数值当作正式版结论。

标签：科学文献 / 科研可靠性 / 测量与识别 / 科研制度与资源

<details>
<summary>核验记录 · 2026-10-08 · 摘要</summary>

直接读取 AEA 官方摘要及书目信息，核验两位作者、AER 109(8):2766–2794、August 2019 与 DOI；官方 PDF 本轮403。读取 EDITH 保存的 NBER Working Paper 23298 首页、摘要与导言，确认是 March 2017、Revised November 2017 的旧稿；旧稿还讨论驱虫元研究，正式摘要的应用列表不含该项，因此短评依正式摘要且保留 abstract 证据级别。AEA 官方页链接的复现包可定位，但未下载或执行。

- [publication](https://www.aeaweb.org/articles?id=10.1257/aer.20180310)：直接读取 AEA 官方页，核验完整作者、正式题名、2019 年卷期页码和 DOI，并以正式摘要为短评主要内容依据；正式 PDF 本轮访问403。
- [content](https://www.nber.org/papers/w23298)：本轮读取 EDITH 保存的 NBER Working Paper 23298 首页、摘要及导言，确认 November 2017 修订旧稿；旧稿仅用于识别版本与方法背景，未替代正式版内容。NBER 网页直接访问失败。
- [metadata](https://doi.org/10.3886/E116208V1)：沿 AEA 官方 Replication Package 链接读取 openICPSR 项目元数据，确认两位作者、文章题名及 Code-and-Data-2019 文件夹；未下载或执行代码。

</details>

<a id="andrews-2021-scientific-communication"></a>

## A Model of Scientific Communication

**2021 · Econometrica · 期刊研究**

**研究定位：**SoS 核心 · 经典与科研制度

Isaiah Andrews; Jesse M. Shapiro

[论文](https://onlinelibrary.wiley.com/doi/abs/10.3982/ECTA18155) · [正式来源](https://onlinelibrary.wiley.com/doi/abs/10.3982/ECTA18155)

这项理论研究把科学报告建模为研究者向读者传递证据的过程：读者的先验信念和目标不同，收到同一报告后也可能形成不同判断或采取不同决策。作者将这一传播模型与报告直接决定损失的经典统计模型比较，指出两者在一些设定下会偏好不同的报告规则，为理解科学论文应保留哪些信息提供理论依据。

**为什么读：**将科学文献视为可供异质读者使用的证据载体，为研究摘要、引用与 AI 文献综合中的信息保留问题提供 SoS 理论背景。

**限制：**结论依赖读者信念、目标及信息结构的模型设定；不是对实际论文读者的行为实验，也不是 LLM 写作或文献综合效果的证据。本轮未审阅正式版的全部推导，不能把模型中的报告规则推广为所有科研传播情境的统一标准。

标签：科学文献 / 学术传播 / 测量与识别

<details>
<summary>核验记录 · 2026-10-08 · 摘要</summary>

直接读取 Wiley 官方页面，核验两位作者、Original Articles 类型、Econometrica 89(5):2117–2142、2021-09-27 及 DOI；全文入口转向摘要页。另读 EDITH 保存的 NBER Working Paper 26824 首页、摘要与导言，确认是 March 2020、Revised March 2021 的旧稿；未逐段比对正式版，短评以正式摘要为依据，证据级别仍为 abstract。未复核全部定理证明。

- [publication](https://onlinelibrary.wiley.com/doi/abs/10.3982/ECTA18155)：本轮直接可读的 Wiley 官方页面；核验完整作者、Original Articles、卷期页码、正式发表年份与 DOI，并读取正式摘要。
- [content](https://www.nber.org/papers/w26824)：NBER 页面直接访问403，官方搜索索引确认工作论文及修订时间；通过 EDITH 所存原文读取同一工作论文的首页、摘要和导言，仅用于版本识别及理论背景，不充当正式版全文阅读证据。

</details>

<a id="kobak-2025-llm-excess-vocabulary"></a>

## Delving into LLM-assisted writing in biomedical publications through excess vocabulary

**2025 · Science Advances · 期刊研究**

**研究定位：**SoS 核心 · AI 与科研

Dmitry Kobak; Rita González-Márquez; Emőke-Ágnes Horvát; Jan Lause

[论文](https://doi.org/10.1126/sciadv.adt3813) · [正式来源](https://www.science.org/doi/10.1126/sciadv.adt3813)

研究以历年生物医学摘要的词频趋势构造反事实基线，观察 ChatGPT 推出后突然增多的文体词，并据此估计群体层面的辅助写作下界。作者报告明显的语言变化及学科、国家和期刊差异，提供不依赖逐篇检测器的科研写作扩散测量方案。

**为什么读：**把 AI 进入科研传播过程转化为可检验的规模化测量问题。

**限制：**词汇变化只提供语料层面的使用下界，不能判定某篇论文是否用过模型；文体标记可能随时间变化，也不能据此推断科研质量或不当行为。

标签：AI 与科研 / 学术传播 / 测量与识别

<details>
<summary>核验记录 · 2026-10-07 · 部分正文 / 图表</summary>

出版商页面直接打开返回403；核对PMC所载最终文章的作者、DOI、Science Advances 11(27):eadt3813及2025年7月发表信息，读取摘要、结果和限制段落。正式标题与2024年预印本不同，按同一研究去重。

- [publication](https://pmc.ncbi.nlm.nih.gov/articles/PMC12219543/)：PMC刊载AAAS正式文章，标明卷期、作者、DOI、收稿/接收及发表日期。
- [content](https://pmc.ncbi.nlm.nih.gov/articles/PMC12219543/)：读取摘要、超额词汇分析、讨论与限制部分；检索返回正文，直接打开偶遇浏览器验证。
- [metadata](https://www.science.org/doi/10.1126/sciadv.adt3813)：对应出版商正式入口；本次直接访问受限，未将其称为可读全文。

</details>

<a id="liang-2025-quantifying-llm-scientific-papers"></a>

## Quantifying large language model usage in scientific papers

**2025 · Nature Human Behaviour · 期刊研究**

**研究定位：**SoS 核心 · AI 与科研

Weixin Liang; Yaohui Zhang; Zhengxuan Wu; Haley Lepp; Wenlong Ji; Xuandong Zhao; Hancheng Cao; Sheng Liu; Siyu He; Zhi Huang; Diyi Yang; Christopher Potts; Christopher D. Manning; James Zou

[论文](https://doi.org/10.1038/s41562-025-02273-8) · [正式来源](https://www.nature.com/articles/s41562-025-02273-8)

文章用词频混合分布估计 arXiv、bioRxiv 与 Nature 系列论文中经大模型修改的文本比例，比较不同学科和时间段。作者观察到辅助写作持续增长，并与更频繁的预印本发布、较短篇幅和更拥挤的研究主题相关，为讨论扩散与写作趋同提供群体证据。

**为什么读：**为 AI 科研采用研究提供核心测量方法，并连接写作扩散、产出频率和知识相似性。

**限制：**估计针对语料中的修改文本比例，不能直接识别个体作者采用行为；模型、提示和语言分布变化会影响校准，相关关系不能解释生产率变化的原因。

标签：AI 与科研 / 学术传播 / 测量与识别

<details>
<summary>核验记录 · 2026-10-07 · 部分正文 / 图表</summary>

Nature正式页面的检索结果核对全部14名作者、2025年8月在线发表及卷9页2599–2609；作者学校站点PDF用于读取定义、模型校准及相关性解释，未读取全部补充分析或复现。

- [publication](https://www.nature.com/articles/s41562-025-02273-8)：正式Article记录、完整作者表、DOI与卷期年；带查询参数的出版商检索页面可读取。
- [content](https://nlp.stanford.edu/~manning/papers/Liang_et_al-2025-Nature_Human_Behaviour.pdf)：作者大学站点提供排版论文PDF，读取方法定义、校准、采用相关性和局限讨论；日期以期刊正式记录为准。

</details>

<a id="chu-2021-slowed-canonical-progress"></a>

## Slowed canonical progress in large fields of science

**2021 · Proceedings of the National Academy of Sciences · 期刊研究**

**研究定位：**SoS 核心 · 经典与科研制度

Johan S. G. Chu; James A. Evans

[论文](https://doi.org/10.1073/pnas.2021636118) · [正式来源](https://www.pnas.org/doi/10.1073/pnas.2021636118)

研究提出，文献规模膨胀可能挤压读者识别新思想的注意力，并用引文变化检验相关预期。作者报告，大领域的引用更集中于既有高被引论文，经典地位更稳固，新论文更难进入核心，为理解知识积累与更新的张力提供证据。

**为什么读：**为分析 AI 带来的论文增产、推荐过滤和阅读辅助提供生态基线：应同时考察产出数量与新思想获得关注的机会。

**限制：**引文中的经典稳定不等于该领域停止取得实际进展，领域规模关联也不独立识别注意力机制。本次读取摘要及出版元数据，未审查正文模型或补充材料。

标签：知识演化 / 创新

<details>
<summary>核验记录 · 2026-10-07 · 摘要</summary>

已直接读取芝加哥大学作者机构库的摘要和 DOI；PMC 收录的 PNAS 原文检索文本显示正式卷期、完整作者及出版声明。PNAS 直接打开转入 cookieAbsent，PMC 直接打开遇到验证页，未读取正文。

- [publication](https://pmc.ncbi.nlm.nih.gov/articles/PMC8522281/)：检索呈现 PNAS 正式原文的作者、118(41):e2021636118、2021 年、DOI 及 Published by PNAS 声明；直接打开遇验证页。
- [content](https://knowledge.uchicago.edu/records/x681q-nn777)：已直接读取作者机构库的完整摘要、作者、期刊及 DOI；机构库页面自身更新日期不作为论文发表日期。
- [publication](https://www.pnas.org/doi/10.1073/pnas.2021636118)：期刊规范入口；本次直接打开重定向到 cookieAbsent，未取得正文。

</details>

<a id="chen-2025-noisy-path"></a>

## The Noisy Path from Source to Citation: Measuring How Scholars Engage with Past Research

**2025 · ACL 2025 · Volume 1: Long Papers · 会议论文**

**研究定位：**SoS 核心 · 经典与科研制度

Hong Chen; Misha Teplitskiy; David Jurgens

[论文](https://aclanthology.org/2025.acl-long.1534/) · [正式来源](https://aclanthology.org/2025.acl-long.1534/)

将施引句与被引论文中的主张匹配，用监督模型衡量引用保真度。作者发现，知识距离较近、较新和更易获取的来源通常被更忠实地转述；准实验还提供了失真沿中间引用传播的证据，提示引用次数不能完整表示知识传播质量。

**为什么读：**以科学文献及引用链本身为对象，提供知识传播失真的 SoS 基线，可与 LLM 摘要和引用推荐研究对照。

**限制：**单句匹配和筛选规则可能遗漏复杂转述并引入选择偏差；保真分数混合了主题、概括程度与事实对齐，不能直接视为逐条引用错误的人工裁决。准实验解释依赖识别假设，研究不估计 AI 采用效果。

标签：科学文献 / 学术传播 / 知识演化 / 测量与识别 / 科研可靠性

<details>
<summary>核验记录 · 2026-10-08 · 部分正文 / 图表</summary>

本轮直接读取 ACL Anthology 页面及正式 PDF，核验三位作者、2025 年、ACL 主会 Long Papers、页码 31786–31802 和 DOI；阅读摘要、引用保真测量与限制段落。未通读全文或复现实验。

- [publication](https://aclanthology.org/2025.acl-long.1534/)：官方论文页与 BibTeX 核对完整作者、主会 Long Papers、年份、页码和 DOI；直接访问成功。
- [content](https://aclanthology.org/2025.acl-long.1534.pdf)：正式会议 PDF；读取首页、引用保真测量及第 8 节限制，确认句子匹配与综合分数的适用边界。

</details>

<a id="algaba-2025-heightened-citation-bias"></a>

## Large Language Models Reflect Human Citation Patterns with a Heightened Citation Bias

**2025 · Findings of ACL: NAACL 2025 · 会议论文**

**研究定位：**SoS 核心 · AI 与科研

Andres Algaba; Carmen Mazijn; Vincent Holst; Floriano Tori; Sylvia Wenmackers; Vincent Ginis

[论文](https://aclanthology.org/2025.findings-naacl.381/) · [正式来源](https://aclanthology.org/2025.findings-naacl.381/)

隐去机器学习会议论文中的引文，让仅依靠参数知识的 LLM 补充参考文献，并与原作者引用比较。作者报告，受测模型延续了人类引用的若干模式，但更偏向高被引论文；控制年份、作者数等因素后，这种偏向仍然存在。

**为什么读：**直接研究 AI 如何选择和分配学术注意力，连接文献推荐、引用偏差与科学知识传播，归入 AI 与科研核心。

**限制：**实验限定于机器学习论文、受测模型及简单提示，没有搜索或 RAG。引用建议的偏差不能直接当作学者实际采纳后的引用分配变化，更不能证明长期科研不平等已经扩大。

标签：科学文献 / AI 与科研 / 学术传播 / 机会与不平等 / 科研可靠性

<details>
<summary>核验记录 · 2026-10-08 · 部分正文 / 图表</summary>

本轮直接读取 ACL 官方页面及正式 PDF，确认六位作者、NAACL 2025 Findings、2025 年 4 月、页码 6844–6879 和 DOI；阅读摘要及讨论中的提示和跨学科外推限制。未通读附录或复现实验。

- [publication](https://aclanthology.org/2025.findings-naacl.381/)：官方元数据确认完整作者、Findings track、年月、页码和 DOI；不将其写成 NAACL 主会论文。
- [content](https://aclanthology.org/2025.findings-naacl.381.pdf)：正式 PDF 首页与讨论部分；核对参数知识引用生成设定、热门论文偏向及提示和语料范围限制。

</details>

<a id="isch-2026-overreaching-causal-claims"></a>

## Quantifying the prevalence and impact of overreaching causal claims in social science

**2026 · Nature Human Behaviour · 期刊研究**

**研究定位：**元研究、理论与治理

Calvin Isch; Timothy Dörr; Neil Fasching; Grace Jennings; Duncan J. Watts

[论文](https://www.nature.com/articles/s41562-026-02553-x) · [正式来源](https://www.nature.com/articles/s41562-026-02553-x)

结合社会科学论文分类、读者实验和 LLM 摘要实验，研究横截面证据中的因果措辞及其传播。作者报告，因果越界表述较常见；相关性措辞或方法提示可减轻读者的因果解读，模型摘要有时会进一步强化因果含义，而谨慎提示能在部分设定下缓解。

**为什么读：**研究科学文本如何表达和传递证据，AI 同时用于测量和接受传播测试；作为科研可靠性的元研究，与文献摘要失真和引用保真研究相连。

**限制：**作者把无实验或准实验设计的横截面研究对自身新结果所作因果主张定义为越界；这不等于否定所有观察性因果推断。自动分类存在误差，读者实验未涵盖执业社会科学家，模型与提示有限且效果有差异。

标签：科学文献 / AI 与科研 / 学术传播 / 测量与识别 / 科研可靠性

<details>
<summary>核验记录 · 2026-10-08 · 部分正文 / 图表</summary>

本轮 Nature 原页直接打开返回 Internal Error；通过官方页面的可读检索索引核验五位作者、Article、2026-08-24 正式发表和 DOI，并读取摘要、分类方法、实验讨论及限制段落。未读取全部补充材料或复现实验。

- [publication](https://www.nature.com/articles/s41562-026-02553-x)：官方页面检索索引显示完整作者、Article、Published / Version of record 为 2026-08-24 及 DOI；直接打开未成功。
- [content](https://www.nature.com/articles/s41562-026-02553-x)：本轮读取官方索引返回的研究设计分类、因果措辞识别、读者及模型实验讨论和限制；未将索引访问写成全文阅读。

</details>

<a id="peters-2025-generalization-bias"></a>

## Generalization bias in large language model summarization of scientific research

**2025 · Royal Society Open Science · 期刊研究**

**研究定位：**元研究、理论与治理

Uwe Peters; Benjamin Chin-Yee

[论文](https://doi.org/10.1098/rsos.241776) · [正式来源](https://royalsocietypublishing.org/doi/10.1098/rsos.241776)

比较 LLM 科学摘要与原始文本，考察模型是否删去限定条件、扩大结论范围，并在部分任务中与人类摘要对照。作者发现，多数受测模型会产生过度概括，即使提示强调准确性也不能稳定消除；真实来源存在时，转述仍可能改变证据含义。

**为什么读：**将科学主张的限定条件作为评价对象，连接 LLM 文献摘要与元研究、科学传播可靠性。

**限制：**结论限于所测模型、科学文本和三类提示；人类对照的来源也有限，不能外推成全部模型或所有人类写作者的固定错误率。测量的是概括范围，不涵盖所有事实错误或完整阅读理解。

标签：科学文献 / AI 与科研 / 学术传播 / 科研可靠性

<details>
<summary>核验记录 · 2026-10-08 · 部分正文 / 图表</summary>

本轮 DOI 入口直接打开失败；官方出版页面检索索引可读，并直接读取 Utrecht 作者机构保存的 Publisher version PDF，核验两位作者、Research、2025 年 12(4):241776 和 DOI，阅读摘要、首页及限制段落。未通读全文或复现。

- [publication](https://doi.org/10.1098/rsos.241776)：Royal Society 正式文章的可读检索索引；DOI 入口本轮直接打开返回 Internal Error，未据此声称直接读取出版商正文。
- [publication](https://research-portal.uu.nl/ws/portalfiles/portal/263071618/peters-chin-yee-generalization-bias-in-large-language-model-summarization-of-scientific-research.pdf)：作者机构保存的正式排印版本，直接访问成功；封面明确标注 Publisher version、两位作者、2025 年及卷期 DOI，期刊首页标为 Research。
- [content](https://research-portal.uu.nl/ws/portalfiles/portal/263071618/peters-chin-yee-generalization-bias-in-large-language-model-summarization-of-scientific-research.pdf)：读取正式版本摘要和 Strengths and limitations，核对过度概括定义、提示范围及人类摘要对照的局限。

</details>

<a id="asai-2026-openscholar"></a>

## Synthesizing scientific literature with retrieval-augmented language models

**2026 · Nature · 期刊研究**

**研究定位：**技术背景与案例

Akari Asai; Jacqueline He; Rulin Shao; Weijia Shi; Amanpreet Singh; Joseph Chee Chang; Kyle Lo; Luca Soldaini; Sergey Feldman; Mike D’Arcy; David Wadden; Matt Latzke; Jenna Sparks; Jena D. Hwang; Varsha Kishore; Minyang Tian; Pan Ji; Shengyan Liu; Hao Tong; Bohao Wu; Yanyu Xiong; Luke Zettlemoyer; Graham Neubig; Daniel S. Weld; Doug Downey; Wen-tau Yih; Pang Wei Koh; Hannaneh Hajishirzi

[论文](https://www.nature.com/articles/s41586-025-10072-4) · [正式来源](https://www.nature.com/articles/s41586-025-10072-4)

提出 OpenScholar，将科学论文检索、重排序和反馈修订结合，生成带出处的文献综合回答，并构建跨学科 ScholarQABench。作者在特定任务的自动评分与专家比较中报告质量改善，展示检索增强如何支持文献理解。

**为什么读：**提供 AI 辅助文献综合的技术案例，用于理解检索与引用核验的能力边界。

**限制：**专家评价样本有限，回答长度、评分规则、语料可及性和时间边界会影响结果；检索仍可能遗漏代表性论文。任务表现不能证明真实科研中的长期效率或创新收益，也不能据此认为文献综合已能完全自动化。

标签：AI 与科研 / 学术传播 / 科研可靠性 / 科学文献

<details>
<summary>核验记录 · 2026-10-08 · 部分正文 / 图表</summary>

通过 Nature 原始出版页的可读索引核对完整 28 位作者、Article、2026 年 2 月 4 日、650:857–863 与 DOI，读取摘要、Main 和 Limitations。直接打开遇身份服务跳转；页面标注已更新，但更新明细未能核实，因此不采用存在口径差异的基准数量或具体提升幅度。未通读全文、附录或复现。

- [publication](https://www.nature.com/articles/s41586-025-10072-4)：Nature 官方页索引确认正式发表身份、卷期年及完整作者；DOI 含 2025 不代表正式发表年。
- [content](https://www.nature.com/articles/s41586-025-10072-4)：官方页索引中的 Main 和 Limitations 支持系统设计、评价任务及边界；更新明细未核实。

</details>
