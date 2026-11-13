<!-- Generated from data/papers.json by scripts/catalog.py; do not edit directly. -->
# 同行评议、研究可靠性与监督

[返回主题目录](../README.md#peer-review-and-reliability) · [阅读路线](../docs/reading-routes.md) · [阅读方法](../docs/reading-guide.md)

AI 如何改变研究评价，科研流程中的错误又怎样被发现、约束和纠正？将真实评议中的采用测量与随机反馈实验对照，再考察数据泄漏和自动化科研监督；评语改善、模型表现与最终科学质量分别评价。

本主题 7 篇。以下保留每篇研究的定位、文章类型和证据边界；书目核验日期沿用各条目记录。

## 阅读顺序

1. [Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews](#liang-2024-monitoring-ai-peer-reviews)（2024）
2. [A large-scale randomized study of large language model feedback in peer review](#thakkar-2026-randomized-peer-review-feedback)（2026）
3. [Leakage and the reproducibility crisis in machine-learning-based science](#kapoor-2023-leakage)（2023）
4. [Risks of AI scientists: prioritizing safeguarding over autonomy](#tang-2025-risks-ai-scientists)（2025）
5. [Blinded versus Unblinded Review: A Field Study on the Equity of Peer-Review Processes](#pleskac-2026-blinded-review)（2026）
6. [Clubs and Networks in Economics Reviewing](#carrell-2024-clubs-networks)（2024）
7. [Unpacking P-hacking and Publication Bias](#brodeur-2023-unpacking-publication-bias)（2023）

<a id="liang-2024-monitoring-ai-peer-reviews"></a>

## Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews

**2024 · ICML · 会议论文**

**研究定位：**SoS 核心 · AI 与科研

Weixin Liang; Zachary Izzo; Yaohui Zhang; Haley Lepp; Hancheng Cao; Xuandong Zhao; Lingjiao Chen; Haotian Ye; Sheng Liu; Zhi Huang; Daniel Mcfarland; James Y. Zou

[论文](https://proceedings.mlr.press/v235/liang24b.html) · [正式来源](https://proceedings.mlr.press/v235/liang24b.html)

研究用人工与模型文本的参照分布估计整批评审中受到大语言模型显著改写的比例，并比较不同会议和评议行为。作者报告，估计的使用程度与临近截止提交、较少回应作者及文本趋同等现象相关，为研究评议制度变化提供语料级测量方法。

**为什么读：**研究AI进入真实同行评议制度后的采用及知识表达变化，而非只评价模型生成评语的能力。

**限制：**估计依赖参照模型、提示方式和语料分布，不能判断个别评审是否违规，也不能证明整篇评审由模型代写；行为关联不等于因果。

标签：AI 与科研 / 同行评议 / 学术传播 / 测量与识别

<details>
<summary>核验记录 · 2026-10-07 · 部分正文 / 图表</summary>

PMLR官方页核验ICML 2024、卷235、页29575–29620与完整作者；该页未列DOI。阅读官方摘要及作者arXiv v3的讨论和局限，未取得正式PDF，不把预印本单独计数。

- [publication](https://proceedings.mlr.press/v235/liang24b.html)：ICML 2024正式proceedings记录、作者列表与摘要。
- [content](https://arxiv.org/html/2403.07183v3)：阅读作者版本讨论及Limitations，辅助辨别语料估计和个体检测的边界；不是发表证明。

</details>

<a id="thakkar-2026-randomized-peer-review-feedback"></a>

## A large-scale randomized study of large language model feedback in peer review

**2026 · Nature Machine Intelligence · 期刊研究**

**研究定位：**SoS 核心 · AI 与科研

Nitya Thakkar; Mert Yuksekgonul; Jake Silberg; Animesh Garg; Nanyun Peng; Fei Sha; Rose Yu; Carl Vondrick; James Zou

[论文](https://www.nature.com/articles/s42256-026-01188-x) · [正式来源](https://www.nature.com/articles/s42256-026-01188-x)

研究在ICLR评议流程中随机分配模型反馈，针对含糊、误解与不专业的评语向评审人提出可选建议。作者报告反馈促进评语修订和作者评审互动，盲评认为纳入建议的修订更具体，展示在保留人工决定权下改进同行评议的路径。

**为什么读：**提供真实科研制度中的随机干预证据，可与评审文本中AI采用的观察性研究对照阅读。

**限制：**实验来自单次AI会议，反馈只覆盖选定问题；对修订样本的质量评价不能直接推广到全部评审，也没有证明最终论文科学质量提高。

标签：AI 与科研 / 同行评议 / 学术传播

<details>
<summary>核验记录 · 2026-10-07 · 部分正文 / 图表</summary>

Nature Machine Intelligence原页核验2026年正式文章、完整作者、卷8页326–336与DOI。正式正文订阅受限；阅读其官方链接预印本v1的方法、结果与讨论，保留版本差异限制，不引用精确效应数。

- [publication](https://www.nature.com/articles/s42256-026-01188-x)：2026-02-23正式发表，官方摘要与书目信息。
- [content](https://arxiv.org/html/2504.09737v1)：官方页面链接的作者预印本；阅读随机分配、可选反馈、质量评估样本和讨论。

</details>

<a id="kapoor-2023-leakage"></a>

## Leakage and the reproducibility crisis in machine-learning-based science

**2023 · Patterns · 期刊研究**

**研究定位：**元研究、理论与治理

Sayash Kapoor; Arvind Narayanan

[论文](https://doi.org/10.1016/j.patter.2023.100804) · [正式来源](https://www.cell.com/patterns/fulltext/S2666-3899(23)00159-9)

整理跨学科机器学习研究中的数据泄漏类型，并以战争预测复核展示评估流程如何夸大模型优势。作者提出模型信息表，要求把科学主张、目标人群与训练测试划分连在一起报告。

**为什么读：**评估 AI 是否促进科研时，需要检查证据是否可靠，而不仅比较论文数量或模型分数。

**限制：**所汇总案例不是全部机器学习科学研究的随机样本，不能据此估计总体错误比例；特定任务的复核也不意味着复杂模型普遍无效。

标签：AI 与科研 / 科研可靠性 / 测量与识别

<details>
<summary>核验记录 · 2026-10-07 · 部分正文 / 图表</summary>

出版商页面直接访问失败，但ScienceDirect及Cell DOI搜索索引返回正式卷期、摘要和泄漏分类正文；NSF存档索引返回非系统性元综述的限制。交叉核对作者机构记录，未运行原实验。

- [publication](https://www.sciencedirect.com/science/article/am/pii/S2666389923001599)：官方出版页面索引含Patterns 4(9),100804 (2023)、DOI、摘要与数据声明；直接访问失败。
- [content](https://doi.org/10.1016/j.patter.2023.100804)：出版商索引可读泄漏分类、评估人群及模型信息表正文片段。
- [content](https://par.nsf.gov/servlets/purl/10513990)：正式排印版索引说明检索不是来自一致样本的系统性元综述；直接打开502。
- [metadata](https://collaborate.princeton.edu/en/publications/leakage-and-the-reproducibility-crisis-in-machine-learning-based-/)：作者机构记录交叉核对姓名、正式题名和出版年。

</details>

<a id="tang-2025-risks-ai-scientists"></a>

## Risks of AI scientists: prioritizing safeguarding over autonomy

**2025 · Nature Communications · 观点 / 评论**

**研究定位：**元研究、理论与治理

Xiangru Tang; Qiao Jin; Kunlun Zhu; Tongxin Yuan; Yichi Zhang; Wangchunshu Zhou; Meng Qu; Yilun Zhao; Jian Tang; Zhuosheng Zhang; Arman Cohan; Dov Greenbaum; Zhiyong Lu; Mark Gerstein

[论文](https://www.nature.com/articles/s41467-025-63913-1) · [正式来源](https://www.nature.com/articles/s41467-025-63913-1)

文章从使用者、智能体与外部环境的关系梳理AI科研系统风险，结合范围综述提出人类监管、智能体对齐和环境反馈的三部分保障框架。重点是如何组织监督、工具权限和责任，而非只追求系统自主能力，为科研治理提供问题清单。

**为什么读：**为AI参与科研后的责任、监督与研究可靠性提供制度视角，可与自动化系统实证案例配对阅读。

**限制：**这是观点与框架论文，作者未开发或测试针对现有AI科研系统的具体攻击；提出的保障措施不能视为已验证有效的统一治理方案。

标签：AI 与科研 / 科研可靠性 / 科研生产

<details>
<summary>核验记录 · 2026-10-07 · 部分正文 / 图表</summary>

Nature Communications开放原文核验Perspective类型、完整作者、2025年卷16文章8317及DOI；阅读摘要、引言框架与结尾局限声明，未复现实验。

- [publication](https://www.nature.com/articles/s41467-025-63913-1)：2025-09-18正式Perspective；开放正文明确框架性质及未测试具体漏洞。

</details>

<a id="pleskac-2026-blinded-review"></a>

## Blinded versus Unblinded Review: A Field Study on the Equity of Peer-Review Processes

**2026 · Management Science · 期刊研究**

**研究定位：**SoS 核心 · 经典与科研制度

Timothy J. Pleskac; Ellie J. Kyung; Gretchen B. Chapman; Oleg Urminsky

[论文](https://pubsonline.informs.org/doi/10.1287/mnsc.2022.01646) · [正式来源](https://pubsonline.informs.org/doi/10.1287/mnsc.2022.01646)

通过学术会议评审的现场实验比较单盲与双盲制度，同时考察评分一致性、公平性和后续表现。作者报告，两种制度均有明显评审噪声，隐藏身份并不能消除所有群体差异；公开身份也未显示足以抵消偏向风险的评价优势。

**为什么读：**为讨论科学评价中的噪声、身份信号和机会差异提供制度基准，可与AI辅助评审研究对照。

**限制：**来自特定会议场景的制度比较，不能直接外推到所有期刊、学科或自动评审。短评基于正式摘要，未重新分析原始数据；这是评议制度的背景研究，不是AI采用效果证据。

标签：同行评议 / 机会与不平等 / 科研制度与资源 / 科研可靠性

<details>
<summary>核验记录 · 2026-11-10 · 摘要</summary>

从本轮文献库命中追踪至INFORMS官方文章页，直接核验四位作者、摘要、DOI、72(4):2702–2719及2025-08-06在线日期。按本库正式卷期年规则归档2026；出版商推荐引文中的2025在线年另保留说明。未通读正文或复现。

- [publication](https://pubsonline.informs.org/doi/10.1287/mnsc.2022.01646)：直接读取官方文章页的元数据与摘要；2025在线、2026卷期，非新近发表但属于本轮补接的既有缺口。

</details>

<a id="carrell-2024-clubs-networks"></a>

## Clubs and Networks in Economics Reviewing

**2024 · Journal of Political Economy · 期刊研究**

**研究定位：**SoS 核心 · 经典与科研制度

Scott Carrell; David Figlio; Lester Lusher

[论文](https://www.journals.uchicago.edu/doi/10.1086/730208) · [正式来源](https://www.journals.uchicago.edu/doi/10.1086/730208)

研究Journal of Human Resources投稿中的作者—编辑及作者—审稿人联系，考察同学、同事、合作网络和学术地位信号与送审及评价的关系。作者报告，多类联系与更有利的评审结果相关，为科学评价中的关系网络提供微观证据。

**为什么读：**提供同行评议中身份信号与关系网络的制度背景，可与双盲评审和AI辅助评价研究对照，但不是AI采用效果。

**限制：**来自单一期刊的投稿制度，不能直接外推到整个经济学或所有学科；关系网络与能力及稿件分配可能共同变化，短评不将摘要相关性升级为无条件因果。仅核验正式摘要和元数据，未审计识别策略或复现。

标签：同行评议 / 科研制度与资源 / 机会与不平等 / 团队组织

<details>
<summary>核验记录 · 2026-11-11 · 摘要</summary>

从本轮文献库命中追踪至UChicago官方文章页，直接核验三位作者、JPE132(9)、页2999–3024、DOI和2024-07-31在线日期；期刊卷期为2024。以正式版为单一条目，不重复收录2022工作论文。

- [publication](https://www.journals.uchicago.edu/doi/10.1086/730208)：官方出版社书目与摘要均直接读取；本轮未读付费全文。

</details>

<a id="brodeur-2023-unpacking-publication-bias"></a>

## Unpacking P-hacking and Publication Bias

**2023 · American Economic Review · 期刊研究**

**研究定位：**SoS 核心 · 经典与科研制度

Abel Brodeur; Scott Carrell; David Figlio; Lester Lusher

[论文](https://www.aeaweb.org/articles?id=10.1257/aer.20210795) · [正式来源](https://www.aeaweb.org/articles?id=10.1257/aer.20210795) · [代码](https://doi.org/10.3886/E192271V1)

利用期刊投稿稿件中的检验统计量，区分投稿时的显著性聚集与后续编辑、审稿环节的筛选。作者报告，初投稿已存在聚集，送审和直接退稿的分布不同，审稿建议与显著性正相关；评审流程对总体统计量分布的改变有限。

**为什么读：**为科学可靠性研究区分研究者端的分析选择与发表过程中的选择提供制度和测量基准，可与AI辅助评审研究对照。

**限制：**短评仅依据正式摘要，未审计统计量抽取、密度检验或重跑代码。特定投稿与追踪样本不代表所有学科，不应据此断言发表偏倚不存在，也不是AI评审效果证据。后续复现讨论与作者回应仍待配对细读。

标签：同行评议 / 科研可靠性 / 测量与识别 / 科研制度与资源

<details>
<summary>核验记录 · 2026-11-13 · 摘要</summary>

本轮文献库命中后直接核验AEA官方题名、四位作者、AER113(11):2974–3002、2023年11月与DOI；官方提供复现包入口，未下载或执行。补接旧缺口，不是新近发表或全覆盖核验。

- [publication](https://www.aeaweb.org/articles?id=10.1257/aer.20210795)：AEA正式文章页的书目信息与摘要，直接读取。
- [metadata](https://doi.org/10.3886/E192271V1)：AEA文章页直接链接的数据与代码复现包；核验入口，不声称执行。

</details>
