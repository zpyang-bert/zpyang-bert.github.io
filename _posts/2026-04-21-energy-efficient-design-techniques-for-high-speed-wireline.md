---
layout: post
title:      "Energy-Efficient Design Techniques for High-Speed Wireline Serial Links"
date:       2026-04-21 11:07:07
author:     "Bert"
tags:
  - SerDes
  - Thesis
  - 深度学习
---
## 深度学习报告 | Fırat ÇELİK | EPFL (École Polytechnique Fédérale de Lausanne), 2021

---

## 论文概述

本论文研究了高速有线串行链路的能效设计技术，包括：
1. 电流模式vs电压模式发射机能效对比
2. PAM调制阶数（PAM-2/PAM-4/PAM-8）对链路性能的影响
3. 高阻抗驱动器技术实现20%功耗降低
4. PAM-16兼容TX和ADC接收机模拟前端系统

**关键词**：Wireline SerDes、能效、PAM调制、FFE、CTLE、DFE、ADC-based RX

---

## 第一章 引言

### 论文目标

![](/img/serdes/fundamentals/lectures/lecture10_ee720_jitter_深度学习报告/_images/img-000.jpg)

> 🔍 深度说明：
> - **研究背景**：数据流量指数级增长推动I/O链路带宽需求持续攀升
> - **核心结论**：铜链带宽无法跟随技术 scaling 等比例提升，必须采用先进均衡和高阶调制
> - **工程价值**：系统性地分析了能效优化的多个维度
> - **落地注意**：高阶调制和均衡技术带来功耗增加，需权衡设计

### 全球移动数据流量预测

![](/img/serdes/fundamentals/lectures/lecture1_ee720_intro_深度学习报告/_images/img-001.jpg)

> 🔍 深度说明：
> - **研究背景**：Cisco预测2017-2022年移动数据流量将增长7倍
> - **核心结论**：到2022年月度移动数据流量将达77 EB
> - **工程价值**：量化了带宽需求增长压力
> - **落地注意**：有线链路需承接大量移动回程流量

### Google数据中心

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/img-002.jpg)

> 🔍 深度说明：
> - **研究背景**：数据中心是高速有线链路的核心应用场景
> - **核心结论**：Oklahoma数据中心展示大规模服务器互联需求
> - **工程价值**：揭示了高速SerDes的规模化部署场景
> - **落地注意**：能效直接影响数据中心运营成本和散热

### 有线标准数据率发展

![](/img/serdes/fundamentals/lectures/lecture1_ee720_intro_深度学习报告/_images/img-003.jpg)

> 🔍 深度说明：
> - **研究背景**：各标准组织定义的每引脚数据率持续提升
> - **核心结论**：PCIe、USB、以太网等标准速率不断提升
> - **工程价值**：为设计目标提供参考基准
> - **落地注意**：需关注标准演进路线以保证兼容性

### 有线收发器数据率趋势

![](/img/serdes/fundamentals/lectures/lecture11_ee720_clocking_arch_plls_深度学习报告/_images/img-004.jpg)

> 🔍 深度说明：
> - **研究背景**：学术论文中展示的收发器数据率不断提升
> - **核心结论**：论文发表的数据率呈指数上升趋势
> - **工程价值**：反映学术界和工业界的研究前沿
> - **落地注意**：论文结果需转化为产品才有实际价值

### 能效改进趋势

![](/img/serdes/fundamentals/lectures/lecture1_ee720_intro_深度学习报告/_images/img-005.jpg)

> 🔍 深度说明：
> - **研究背景**：收发器能效逐年提升
> - **核心结论**：先进工艺和电路技术推动pJ/bit持续降低
> - **工程价值**：设定了能效设计的目标方向
> - **落地注意**：能效提升往往伴随其他性能权衡

---

## 第二章 理论回顾

### 有线串行链路框图

![](/img/serdes/fundamentals/lectures/lecture13_ee720_fwd_clk_deskew_深度学习报告/_images/img-006.jpg)

> 🔍 深度说明：
> - **研究背景**：典型串行链路系统架构
> - **核心结论**：TX+Channel+RX构成完整链路
> - **工程价值**：为后续章节的详细分析奠定基础
> - **落地注意**：各模块需协同优化

### 4:1 DFF型Serializer

![](/img/serdes/fundamentals/lectures/lecture13_ee720_fwd_clk_deskew_深度学习报告/_images/img-007.jpg)

> 🔍 深度说明：
> - **研究背景**：基于D触发器的并行转串行实现
> - **核心结论**：4:1 serializer利用时钟相位关系实现复用
> - **工程价值**：基本serializer架构
> - **落地注意**：时钟分配和偏斜需仔细控制

### 4:1 MUX型Serializer

![](/img/serdes/fundamentals/papers/PAM4 oDSP原理介绍_images/img-008.jpg)

> 🔍 深度说明：
> - **研究背景**：基于多路复用器的serializer实现
> - **核心结论**：全速率架构，3级2:1 MUX级联
> - **工程价值**：常用的高速serializer拓扑
> - **落地注意**：需生成2GHz选通信号

### LVDS驱动器

![](/img/serdes/fundamentals/lectures/lecture2_ee720_channels_深度学习报告/_images/img-009.jpg)

> 🔍 深度说明：
> - **研究背景**：低压差分信号发射机
> - **核心结论**：PMOS+NMOS推挽电流模式结构
> - **工程价值**：低噪声、抗共模干扰
> - **落地注意**：CMFB回路保证共模稳定

### CML驱动器

![](/img/serdes/fundamentals/lectures/lecture2_ee720_channels_深度学习报告/_images/img-010.jpg)

> 🔍 深度说明：
> - **研究背景**：电流模式逻辑驱动器
> - **核心结论**：恒定电流切换，速度快但功耗高
> - **工程价值**：适用于超高速应用
> - **落地注意**：版图匹配影响线性度

### 电压模式驱动器

![](/img/serdes/fundamentals/lectures/lecture2_ee720_channels_深度学习报告/_images/img-011.jpg)

> 🔍 深度说明：
> - **研究背景**：CMOS源极串联终止驱动器
> - **核心结论**：高摆幅、低功耗解决方案
> - **工程价值**：能效优于CML
> - **落地注意**：阈值电压依赖性是设计挑战

### Strong-Arm Latch

![](/img/serdes/fundamentals/lectures/lecture2_ee720_channels_深度学习报告/_images/img-012.jpg)

> 🔍 深度说明：
> - **研究背景**：高速比较器/判决电路
> - **核心结论**：动态锁存器实现快速决策
> - **工程价值**：SerDes接收机核心
> - **落地注意**：kickback噪声需抑制

### 信道频率响应

![](/img/serdes/fundamentals/lectures/lecture6_ee720_rx_circuits_深度学习报告/_images/img-013.jpg)

> 🔍 深度说明：
> - **研究背景**：FR4带状线的频率衰减特性
> - **核心结论**：趋肤效应和介质损耗导致高频衰减
> - **工程价值**：理解信道损伤的基础
> - **落地注意**：建模精度影响均衡效果

### 脉冲响应分析

![](/img/serdes/fundamentals/lectures/lecture3_ee720_tdr_spar_深度学习报告/_images/img-014.jpg)

> 🔍 深度说明：
> - **研究背景**：信道对单脉冲的响应
> - **核心结论**：脉冲展宽导致ISI
> - **工程价值**：指导均衡器设计
> - **落地注意**：符号间干扰是主要损伤源

### FFE实现

![](/img/serdes/fundamentals/lectures/lecture4_ee720_channel_pulse_model_深度学习报告/_images/img-015.jpg)

> 🔍 深度说明：
> - **研究背景**：前馈均衡器在发射端实现
> - **核心结论**：FIR滤波器预补偿信道损伤
> - **工程价值**：TX均衡降低接收机复杂度
> - **落地注意**：tap权重优化是关键

### CTLE电路

![](/img/serdes/fundamentals/lectures/lecture3_ee720_tdr_spar_深度学习报告/_images/img-016.jpg)

> 🔍 深度说明：
> - **研究背景**：连续时间线性均衡器
> - **核心结论**：有源网络实现高通特性
> - **工程价值**：接收机前端常用结构
> - **落地注意**：极点零点位置决定均衡特性

### CTLE传递函数

![](/img/serdes/fundamentals/lectures/lecture6_ee720_rx_circuits_深度学习报告/_images/img-017.jpg)

> 🔍 深度说明：
> - **研究背景**：CTLE的频率响应设计
> - **核心结论**：一个零点、两个极点实现带 peaking
> - **工程价值**：指导CTLE参数设计
> - **落地注意**：peaking过大会放大噪声

### DFE实现

![](/img/serdes/fundamentals/lectures/lecture11_ee720_clocking_arch_plls_深度学习报告/_images/img-018.jpg)

> 🔍 深度说明：
> - **研究背景**：判决反馈均衡器
> - **核心结论**：利用历史判决结果抵消ISI
> - **工程价值**：非线性均衡，有效对抗ISI
> - **落地注意**：错误传播是主要风险

### PAM-4调制

![](/img/serdes/fundamentals/lectures/lecture11_ee720_clocking_arch_plls_深度学习报告/_images/img-019.jpg)

> 🔍 深度说明：
> - **研究背景**：四电平脉冲幅度调制
> - **核心结论**：相同带宽下数据率翻倍
> - **工程价值**：PAM-4是当前高速链路主流方案
> - **落地注意**：需更高SNR，对噪声更敏感

### PAM-4 vs NRZ波形

![](/img/serdes/fundamentals/lectures/lecture3_ee720_tdr_spar_深度学习报告/_images/img-020.jpg)

> 🔍 深度说明：
> - **研究背景**：PAM-4 vs NRZ信号波形对比
> - **核心结论**：PAM-4单位间隔是NRZ的2倍
> - **工程价值**：展示调制技术差异
> - **落地注意**：时序裕量增加但幅度裕量减少

---

## 第三章 JESD204B兼容LVDS和SST发射机

### LVDS vs SST对比

本章设计了两种12.5 Gb/s发射机原型，用于多通道ADC系统。

> 🔍 深度说明：
> - **研究背景**：JESD204B标准支持最高12.5 Gb/s
> - **核心结论**：SST在能效上优于LVDS
> - **工程价值**：为ADC接口设计提供参考
> - **落地注意**：28nm FD-SOI工艺验证

---

## 第四章 PAM调制比较研究

### PAM-2/PAM-4/PAM-8眼图对比

通过仿真比较了不同调制阶数在不同信道和数据率下的性能表现。

> 🔍 深度说明：
> - **研究背景**：高阶调制可提升带宽效率
> - **核心结论**：PAM-4是能效和性能的平衡点
> - **工程价值**：为调制阶数选择提供依据
> - **落地注意**：信道损耗限制了高阶调制性能

---

## 第五章 高阻抗驱动器技术

### 高阻抗PAM-4 SST TX

![](/img/serdes/fundamentals/papers/高速光通信接收机前端与时钟数据恢复电路研究与实现_images/img-021.jpg)

> 🔍 深度说明：
> - **研究背景**：传统SST TX的动态功耗问题
> - **核心结论**：高阻抗技术显著降低电容负载
> - **工程价值**：实现20%功耗降低
> - **工程成就**：32 Gb/s下达到2.4 pJ/bit能效

---

## 第六章 PAM-16系统

### PAM-16 TX+RX AFE

![](/img/serdes/fundamentals/lectures/lecture11_ee720_clocking_arch_plls_深度学习报告/_images/img-022.jpg)

> 🔍 深度说明：
> - **研究背景**：超高高阶调制的能效研究
> - **核心结论**：PAM-16在中等损耗信道下可行
> - **工程价值**：TX 26.85 mW + RX AFE 49.36 mW @ 8 Gbaud
> - **能效成就**：系统级2.38 pJ/bit @ 32 Gb/s

---

## 核心结论

1. **SST驱动器能效优于LVDS**：在相同数据率下，SST架构可降低功耗
2. **PAM-4是当前最优选择**：在能效和复杂度间取得最佳平衡
3. **高阻抗驱动器技术有效**：可降低20% TX功耗
4. **PAM-16在特定场景可行**：需配合模拟域均衡

---

## 能效性能对比

| 设计 | 工艺 | 数据率 | 能效 |
|------|------|--------|------|
| LVDS TX | 28nm FD-SOI | 12.5 Gb/s | - |
| SST TX | 28nm FD-SOI | 12.5 Gb/s | 优于LVDS |
| 高阻抗 PAM-4 TX | 28nm FD-SOI | 32 Gb/s | 2.4 pJ/bit |
| PAM-16系统 | 28nm FD-SOI | 32 Gb/s | 2.38 pJ/bit |

---

*报告生成时间：基于Energy_Efficient_HighSpeed_Wireline_Serial_Links_Celik_EPFL_131p.pdf深度分析*
