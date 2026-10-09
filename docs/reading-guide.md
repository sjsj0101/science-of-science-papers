# 如何研究 AI 对科学的影响

这份导读把 AI 与科研的问题分成工具、研究者、知识和制度四个层次。下面的组织方式是编辑框架；各论文的结论仍以其数据、研究设计及核验说明为边界。主题导航和简表见 [README](../README.md)，完整书目与核验记录位于各主题详情页。

目录按研究问题划分六个主主题，每篇有一个主展示位置。SoS 核心、元研究／理论与治理、技术背景与案例是独立的研究定位，在每个主题中逐条标注。阅读路线可以跨主题，但不能把系统表现、理论框架与现实科研效果视为同一种证据。具体顺序见 [建议阅读路线](reading-routes.md)。

## 先区分问题与分析单位

| 层次 | 核心问题 | 可观察结果 | 常见解释限制 |
| --- | --- | --- | --- |
| 工具与任务 | 模型能完成哪一步？ | 任务分数、实验成功、时间与成本 | 基准表现不能直接推出真实采用收益 |
| 研究者与团队 | 谁使用、谁受益、怎样分工？ | 采用信号、工时、产出、职业与合作 | 自选择、署名代理、学科及资源差异 |
| 知识与领域 | 科研探索了什么、遗漏了什么？ | 主题范围、知识组合、引用结构 | 代理指标与数据库变化不等于实际知识变化 |
| 制度与生态 | 如何资助、评审和验证？ | 资助方向、反馈质量、错误、资源可及性 | 短期局部干预不等于长期制度效果 |

[Fortunato 等的领域综述](../topics/workflow-and-human-ai-roles.md#fortunato-2018-science-of-science)提供整体框架；[Wang 等的技术综述](../topics/workflow-and-human-ai-roles.md#wang-2023-scientific-discovery-ai)帮助定位工具所处环节。两者并读，可以避免把“模型能做科研任务”直接当作“科学整体进步更快”的证据。

[Gopal 等的社论](../topics/workflow-and-human-ai-roles.md#gopal-2025-inventing-with-machines)讨论信息系统学科中的研究实践与责任；[De Freitas 等的构思框架](../topics/innovation-and-knowledge-evolution.md#de-freitas-2025-ideation-generative-ai)将 AI 放入问题重构与人机分工。这两篇属于交叉框架，均不能替代科研创新或生产率的实证检验。后者为受邀文章，原文明确说明未走常规同行评议。

## 采用测量与因果识别要分开

[Kobak 等](../topics/scientific-literature.md#kobak-2025-llm-excess-vocabulary)和[Liang 等](../topics/scientific-literature.md#liang-2025-quantifying-llm-scientific-papers)提供群体写作测量方法。文本中出现模型风格，既可能来自语言润色，也可能来自更深的写作参与；它不直接测量实验设计、思想贡献或真实节省的工作时间。这类估计也不适合据此判定某位作者的不当行为。

阅读 [Kusumegi 等的产量研究](../topics/productivity-and-opportunity.md#kusumegi-2025-scientific-production-llms)时，应同时阅读 [Renault 等的识别批评](../topics/productivity-and-opportunity.md#renault-2026-llm-production-timing-bias)：如果首次被检测到使用工具的时间本身取决于产量，就需要区分事件定义带来的变化和实际处理效果。批评识别设计并不等于证明 AI 没有收益。

[Qian 等的资助研究](../topics/organizations-resources-and-incentives.md#qian-2026-llm-us-research-funding)将分析前移到研究申请，展示了另一类观察窗口。比较论文前，需要核对分析单位、采用定义、未获资助样本、观察期与条件相关的解释范围。

## 创新不只有一个指标

[Uzzi 等](../topics/innovation-and-knowledge-evolution.md#uzzi-2013-atypical-combinations)的知识重组与 [Park 等](../topics/innovation-and-knowledge-evolution.md#park-2023-less-disruptive)的引文颠覆性回答不同问题。[Petersen 等](../topics/innovation-and-knowledge-evolution.md#petersen-2024-disruption-citation-inflation)说明，引用习惯的变化可能影响颠覆性指标。Park 条目的来源还关联了 2026 年正式评论与回复；本仓库不裁决这一争论。

因此，[Hao 等](../topics/innovation-and-knowledge-evolution.md#hao-2026-ai-impact-science-focus)讨论的主题范围、[Bianchini 等 2026 年研究](../topics/innovation-and-knowledge-evolution.md#bianchini-2026-ai-science-when-where)中的新颖性和引文表现，不能直接互相替代或合并成统一的“创新效应”。需要逐项比较时期、领域、采用定义和结果指标。

[Sourati 与 Evans](../topics/innovation-and-knowledge-evolution.md#sourati-2023-human-aware-ai)则从设计角度提出人机互补探索。阅读时应区分历史发现预测、候选的理论合理性与真正的前瞻实验验证。

## 评议与治理要看干预边界

[Liang 等的 ICML 研究](../topics/peer-review-and-reliability.md#liang-2024-monitoring-ai-peer-reviews)观察评审语料中的模型修改信号；[Thakkar 等的随机研究](../topics/peer-review-and-reliability.md#thakkar-2026-randomized-peer-review-feedback)测试向人类评审人提供可选反馈。它们分别回答“如何测量采用”和“某种具体干预是否有用”，都不能直接证明自动评审足以替代科学共同体判断。

[Lu 等的自动化科研案例](../topics/workflow-and-human-ai-roles.md#lu-2026-end-to-end-ai-research)需要连同人工筛选、workshop评议和撤回安排一起阅读。系统论文正式发表于 Nature，与生成稿是否正式发表是两件独立的事。

[Kapoor 与 Narayanan](../topics/peer-review-and-reliability.md#kapoor-2023-leakage)提醒读者检查训练测试划分和科学主张是否匹配；[Messeri 与 Crockett](../topics/workflow-and-human-ai-roles.md#messeri-2024-illusions-understanding)、[Tang 等的风险框架](../topics/peer-review-and-reliability.md#tang-2025-risks-ai-scientists)与 [Ahmed 等的政策讨论](../topics/organizations-resources-and-incentives.md#ahmed-2023-industry-ai)提供认知、责任和资源层面的提问方式。观点的价值在于形成可检查的问题，不能当作已验证的总体因果结论。

## 科研激励与技术变迁的历史参照

[Ding 等的信息技术研究](../topics/productivity-and-opportunity.md#ding-2010-it-scientists-productivity)将网络接入与科研产出、合作及机会差异相连，提供比较新技术扩散的历史参照。[Hager 等的评价指标研究](../topics/organizations-resources-and-incentives.md#hager-2024-measuring-science)则提醒我们，评价工具本身会改变人才匹配与资源分配。后者所存早期工作论文与正式摘要存在结论差异，阅读时以目录中的正式版为准。

[Scooped!](../topics/organizations-resources-and-incentives.md#hill-2025-scooped-priority)研究优先发现权带来的认可回报，[Race to the Bottom](../topics/organizations-resources-and-incentives.md#hill-2025-race-to-bottom)研究竞争与成果成熟度、质量之间的关系；同作者和相近数据不代表同一篇研究。它们可以帮助提出“AI 加速是否放大抢先激励”的问题，但没有检验 AI 的影响。

[Azoulay 等的研究](../topics/organizations-resources-and-incentives.md#azoulay-2019-funeral-science)进一步考察领域领导者退出后外部研究者的进入与知识变化，为学术权威和创新方向提供机制背景。这五篇都属于 SoS 核心，作为历史参照使用。

## 科学文献：形成、传播与失真

[主题页](../topics/scientific-literature.md)把论文作为研究对象，沿着“哪些结果进入文献—主张怎样表达—引用和摘要怎样传播”组织阅读。这里同时包含科研传播机制、元研究和 AI 系统研究，证据类型分别解释。

先读 [Andrews 与 Kasy](../topics/scientific-literature.md#andrews-2019-publication-bias)的发表偏差识别，再读 [Andrews 与 Shapiro](../topics/scientific-literature.md#andrews-2021-scientific-communication)的科学传播模型：前者研究文献为何是选择后的样本，后者讨论报告怎样向具有不同需求的读者传递信息。两篇都提供机制背景，没有估计 AI 采用的效果。

[Chen 等](../topics/scientific-literature.md#chen-2025-noisy-path)研究科学主张沿引用链的保真，[Isch 等](../topics/scientific-literature.md#isch-2026-overreaching-causal-claims)研究非实验横截面论文中过度因果表述及其理解后果。NLP 或 LLM 可以是测量工具；使用这些工具，并不意味着论文研究的就是 AI 对科研的影响。

[Chu 与 Evans](../topics/scientific-literature.md#chu-2021-slowed-canonical-progress)把文献规模与引用注意力联系起来；结合前文的 AI 写作测量，可将论文生成、证据选择和传播放在同一条研究链上。

再对照 [Algaba 等](../topics/scientific-literature.md#algaba-2025-heightened-citation-bias)的 LLM 引用偏差与 [Peters、Chin-Yee](../topics/scientific-literature.md#peters-2025-generalization-bias)的摘要过度概括：分别关注模型选择哪些文献，以及如何改写证据边界。[OpenScholar](../topics/scientific-literature.md#asai-2026-openscholar)提供检索增强文献综合的技术案例；任务评测不能直接推出科研人员的长期效率、创新或文献生态改善。

## 可以继续探索的问题

以下是基于目录形成的研究设想，尚未由本仓库验证，也不代表新颖性已完成查重。

| 研究设想 | 需要的数据或设计 | 关键区分 |
| --- | --- | --- |
| AI 是否减少写作时间，却把瓶颈转移到验证？ | 任务级工时、使用记录、验证错误与前瞻比较 | 时间节省与净科研产出 |
| 个体研究者的高产是否伴随领域选题集中？ | 研究者面板、主题空间、资源条件及独立采用测量 | 个体收益与集体外部影响 |
| 提供 AI 反馈是否改变评审共识和新颖研究的机会？ | 随机反馈、评审修订、分歧及后续研究质量 | 文本更具体与判断更可靠 |
| 公共算力或工具支持能否缩小科研机会差异？ | 资源开放的分期或随机分配、真实采用与长期结果 | 获取工具与能够有效使用工具 |

进一步工作宜从一个明确的分析单位和结果变量开始，并同时安排测量验证、混杂解释与时间窗口检查。尚未完成的候选核验和版本追踪见 [检索台账](../data/search-log.json)。
