# 如何研究 AI 对科学的影响

这份导读把 AI 与科研的问题分成工具、研究者、知识和制度四个层次。下面的组织方式是编辑框架；各论文的结论仍以其数据、研究设计及核验说明为边界。完整书目和来源见 [README](../README.md)。

## 先区分问题与分析单位

| 层次 | 核心问题 | 可观察结果 | 常见解释限制 |
| --- | --- | --- | --- |
| 工具与任务 | 模型能完成哪一步？ | 任务分数、实验成功、时间与成本 | 基准表现不能直接推出真实采用收益 |
| 研究者与团队 | 谁使用、谁受益、怎样分工？ | 采用信号、工时、产出、职业与合作 | 自选择、署名代理、学科及资源差异 |
| 知识与领域 | 科研探索了什么、遗漏了什么？ | 主题范围、知识组合、引用结构 | 代理指标与数据库变化不等于实际知识变化 |
| 制度与生态 | 如何资助、评审和验证？ | 资助方向、反馈质量、错误、资源可及性 | 短期局部干预不等于长期制度效果 |

[Fortunato 等的领域综述](../README.md#fortunato-2018-science-of-science)提供整体框架；[Wang 等的技术综述](../README.md#wang-2023-scientific-discovery-ai)帮助定位工具所处环节。两者并读，可以避免把“模型能做科研任务”直接当作“科学整体进步更快”的证据。

## 采用测量与因果识别要分开

[Kobak 等](../README.md#kobak-2025-llm-excess-vocabulary)和[Liang 等](../README.md#liang-2025-quantifying-llm-scientific-papers)提供群体写作测量方法。文本中出现模型风格，既可能来自语言润色，也可能来自更深的写作参与；它不直接测量实验设计、思想贡献或真实节省的工作时间。这类估计也不适合据此判定某位作者的不当行为。

阅读 [Kusumegi 等的产量研究](../README.md#kusumegi-2025-scientific-production-llms)时，应同时阅读 [Renault 等的识别批评](../README.md#renault-2026-llm-production-timing-bias)：如果首次被检测到使用工具的时间本身取决于产量，就需要区分事件定义带来的变化和实际处理效果。批评识别设计并不等于证明 AI 没有收益。

[Qian 等的资助研究](../README.md#qian-2026-llm-us-research-funding)将分析前移到研究申请，展示了另一类观察窗口。比较论文前，需要核对分析单位、采用定义、未获资助样本、观察期与条件相关的解释范围。

## 创新不只有一个指标

[Uzzi 等](../README.md#uzzi-2013-atypical-combinations)的知识重组与 [Park 等](../README.md#park-2023-less-disruptive)的引文颠覆性回答不同问题。[Petersen 等](../README.md#petersen-2024-disruption-citation-inflation)说明，引用习惯的变化可能影响颠覆性指标。Park 条目的来源还关联了 2026 年正式评论与回复；本仓库不裁决这一争论。

因此，[Hao 等](../README.md#hao-2026-ai-impact-science-focus)讨论的主题范围、[Bianchini 等 2026 年研究](../README.md#bianchini-2026-ai-science-when-where)中的新颖性和引文表现，不能直接互相替代或合并成统一的“创新效应”。需要逐项比较时期、领域、采用定义和结果指标。

[Sourati 与 Evans](../README.md#sourati-2023-human-aware-ai)则从设计角度提出人机互补探索。阅读时应区分历史发现预测、候选的理论合理性与真正的前瞻实验验证。

## 评议与治理要看干预边界

[Liang 等的 ICML 研究](../README.md#liang-2024-monitoring-ai-peer-reviews)观察评审语料中的模型修改信号；[Thakkar 等的随机研究](../README.md#thakkar-2026-randomized-peer-review-feedback)测试向人类评审人提供可选反馈。它们分别回答“如何测量采用”和“某种具体干预是否有用”，都不能直接证明自动评审足以替代科学共同体判断。

[Lu 等的自动化科研案例](../README.md#lu-2026-end-to-end-ai-research)需要连同人工筛选、workshop评议和撤回安排一起阅读。系统论文正式发表于 Nature，与生成稿是否正式发表是两件独立的事。

[Kapoor 与 Narayanan](../README.md#kapoor-2023-leakage)提醒读者检查训练测试划分和科学主张是否匹配；[Messeri 与 Crockett](../README.md#messeri-2024-illusions-understanding)、[Tang 等的风险框架](../README.md#tang-2025-risks-ai-scientists)与 [Ahmed 等的政策讨论](../README.md#ahmed-2023-industry-ai)提供认知、责任和资源层面的提问方式。观点的价值在于形成可检查的问题，不能当作已验证的总体因果结论。

## 可以继续探索的问题

以下是基于目录形成的研究设想，尚未由本仓库验证，也不代表新颖性已完成查重。

| 研究设想 | 需要的数据或设计 | 关键区分 |
| --- | --- | --- |
| AI 是否减少写作时间，却把瓶颈转移到验证？ | 任务级工时、使用记录、验证错误与前瞻比较 | 时间节省与净科研产出 |
| 个体研究者的高产是否伴随领域选题集中？ | 研究者面板、主题空间、资源条件及独立采用测量 | 个体收益与集体外部影响 |
| 提供 AI 反馈是否改变评审共识和新颖研究的机会？ | 随机反馈、评审修订、分歧及后续研究质量 | 文本更具体与判断更可靠 |
| 公共算力或工具支持能否缩小科研机会差异？ | 资源开放的分期或随机分配、真实采用与长期结果 | 获取工具与能够有效使用工具 |

进一步工作宜从一个明确的分析单位和结果变量开始，并同时安排测量验证、混杂解释与时间窗口检查。尚未完成的候选核验和版本追踪见 [检索台账](../data/search-log.json)。
