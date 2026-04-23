---
layout: post
title:      "ISSCC 2021 Session 8: Ultra-High-Speed Wireline — 深度学习报告"
date:       2026-04-16 09:00:00
author:     "Bert"
tags:
  - Fundamentals
  - Lecture
  - SerDes
  - 深度学习
---
**会议**: ISSCC 2021 Session 8: Ultra-High-Speed Wireline
**论文**: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS
**作者**: Jihwan Kim et al., Intel Corporation
**整理日期**: 2026/04/16
**研究深度**: 深度解读（结合224Gb/s PAM-4发射机架构、DSP/7b-DAC、时钟分布、数据通路设计）

---

## 一、超高速有线发展趋势

### 1.1 数据率演进

```
有线数据率趋势:
2018: 32Gb/s
2019: 64Gb/s
2020: 128Gb/s
2021: 256Gb/s (峰值)

单通道数据率:
• 112Gb/s PAM-4 (2020-2021主流)
• 224Gb/s PAM-4 (本研究突破)
```

![](/img/serdes/fundamentals/lectures/lecture11_ee720_clocking_arch_plls_深度学习报告/_images/img-004.jpg)

> 🔍 深度说明：
> 【研究背景】有线数据率从2018年的32Gb/s快速增长到2021年的256Gb/s，年均增长率超过100%。这种高速增长得益于PAM-4调制、先进CMOS工艺和DSP增强均衡技术的结合。
> 【核心结论】PAM-4调制使单符号携带2比特信息，相比NRZ可实现两倍的数据率。112Gb/s PAM-4成为2020-2021年的主流，而224Gb/s PAM-4代表当前技术的突破。
> 【工程价值】理解数据率演进趋势有助于系统架构的选择。对于224Gb/s系统，需要解决更高带宽、更低抖动和更高效均衡的挑战。
> 【落地注意】数据率的提升对信道、 SerDes电路和系统设计都提出了更高要求，需要在架构层面进行优化。

### 1.2 100+Gb/s TX技术对比

```
112Gb/s PAM-4方案 (过去3年ISSCC):
• 模拟FFE, DSP/8b-DAC
• 4:1串行化
• SST/CML driver
• 功耗: 1.7~2.1pJ/bit

128Gb/s PAM-4方案:
• 模拟FFE, DSP/7b-DAC
• 4:1, 2:1串行化
• CML/SST/H-bridge driver
• 功耗: 1.3~1.8pJ/bit

224Gb/s PAM-4方案 (本研究):
• DSP/7b-DAC
• 4:1串行化
• CML driver
• 功耗: 1.7pJ/bit
• 数据率提升2倍!
```

---

## 二、TX架构考虑

### 2.1 112Gb/s vs 224Gb/s架构差异

**112Gb/s架构选项**:
```
时钟: 14GHz或28GHz
多路复用: 4:1或2:1
FFE: 模拟FIR或DSP/DAC
Driver: SST、CML或Hybrid
Output Pad: T-coil (2L+3C)或Pi-coil (3L+4C)
```

**224Gb/s架构挑战**:
```
• 更高的抖动要求
• 更高的带宽要求
• 更高的功耗预算
• 信道适应性需求

权衡因素:
• 抖动 vs 功耗
• 带宽 vs 功耗
• 摆幅/线性度 vs 带宽 vs 功耗
• 群延迟/回波损耗/ESD
```

---

## 三、224Gb/s TX架构

### 3.1 整体架构

```
关键模块:
1. 28GHz on-chip LC PLL
2. 双路径感应峰化CMOS时钟分布
3. DSP中8-tap FFE
4. 7-bit DAC
5. 2级CML driver w/主动峰化
6. 4L-5C输出pad网络
7. 64:4数据通路w/相位检测器

架构特点:
• 高集成度
• 多级优化
• 针对224Gb/s优化
```

![](/img/serdes/fundamentals/lectures/lecture1_ee720_intro_深度学习报告/_images/img-005.jpg)

> 🔍 深度说明：
> 【研究背景】224Gb/s PAM-4发射机需要解决高数据率带来的带宽压力、抖动放大和功耗挑战。该架构采用模块化设计，每个模块都针对224Gb/s操作进行了优化。
> 【核心结论】28GHz LC PLL提供低抖动的时钟基准，双路径时钟分布提供带宽扩展和抖动过滤，DSP中的8-tap FFE提供灵活均衡，7-bit DAC提供64级量化精度。
> 【工程价值】该架构展示了先进CMOS工艺（10nm）下实现224Gb/s的能力，为下一代SerDes系统提供了参考设计流程。
> 【落地注意】高集成度带来了设计复杂度提升，需要进行系统级仿真以验证各模块的交互效应。

### 3.2 时钟分布

```
双路径架构:
• HF CK Path (高频时钟路径)
• LF CK Path (低频时钟路径)
• 提供带宽扩展和抖动过滤

关键设计:
• 感应峰化扩展带宽
• 抖动过滤降低输出抖动
```

![](/img/serdes/fundamentals/lectures/lecture11_ee720_clocking_arch_plls_深度学习报告/_images/img-029.jpg)

> 🔍 深度说明：
> 【研究背景】双路径时钟分布架构是解决高频率下带宽和抖动矛盾的有效方案。高频路径提供快速瞬态响应，低频路径提供低频抖动过滤。
> 【核心结论】双路径架构通过分离高低频成分，实现了带宽扩展和抖动过滤的平衡。感应峰化技术在时钟分布的早期和中级使用Series-shunt峰化，晚期使用Shunt-series峰化，以优化不同位置的抖动性能。
> 【工程价值】该设计展示了在28GHz时钟下实现低抖动的技术路径，为更高频率时钟分布网络提供了参考。
> 【落地注意】双路径架构需要精确的路径平衡设计，否则可能导致不期望的谐波分量。

### 3.3 数据通路

```
64:4数据通路:
• 64并行输入
• 4串行输出
• 相位检测器优化时序

组成:
• 64×7 Retimer
• 8×11 Serializer
• 7b-DAC
• 4:1 Driver
```

---

## 四、电路实现

### 4.1 CMOS缓冲器与感应峰化

**三种架构对比**:
```
无电感: 无峰化
Shunt-series峰化: 串联储能
Series-shunt峰化: 串-并联储能

性能对比:
┌──────────────────┬──────────┬──────────┬──────────┐
│ 指标              │ 无电感    │ Shunt-series│ Series-shunt│
├──────────────────┼──────────┼──────────┼──────────┤
│ 抖动放大          │ 最差      │ 最佳     │ 最佳      │
│ 摆幅/自噪声      │ 最差      │ 最佳     │ 最佳      │
│ 总体功耗         │ -        │ 中等     │ 最佳      │
│ 电感面积         │ 无       │ 中等     │ 最大      │
└──────────────────┴──────────┴──────────┴──────────┘

本设计:
• 在时钟分布早期/中级使用Series-shunt峰化
• 在时钟分布晚期使用Shunt-series峰化
```

![](/img/serdes/fundamentals/lectures/Session_08V-ULTRA-HIGH-SPEED_WIRELINE_深度学习报告/_images/img-037.jpg)

> 🔍 深度说明：
> 【研究背景】感应峰化是扩展缓冲器带宽的常用技术。Series-shunt和Shunt-series是两种基本的峰化架构，前者提供更大的带宽扩展，后者具有更好的抖动性能。
> 【核心结论】Series-shunt峰化通过串-并联电感实现带宽扩展，但引入更大的噪声。Shunt-series峰化提供更好的抖动性能，但带宽扩展有限。在时钟分配链的不同位置使用不同峰化架构可以实现整体优化。
> 【工程价值】该设计展示了如何通过混合使用不同峰化架构来平衡带宽、抖动和功耗。这为高速时钟分布网络设计提供了实用的指导。
> 【落地注意】电感占用较大的芯片面积，需要在布局中进行仔细规划。Series-shunt峰化的电感面积通常是Shunt-series的1.5-2倍。

### 4.2 DAC设计

```
7-bit DAC:
• 提供64级量化
• 支持PAM-4调制
• DSP/FFE联合优化

特点:
• 高分辨率
• 低功耗
• 匹配224Gb/s数据率需求
```

![](/img/serdes/fundamentals/lectures/Session_08V-ULTRA-HIGH-SPEED WIRELINE_images/img-038.jpg)

> 🔍 深度说明：
> 【研究背景】7-bit DAC提供64级量化精度，对于PAM-4调制足够。更高的位数（如8-bit）虽然提供更好的线性度，但会增加功耗和面积。DSP中的FFE预先补偿信道失真，与DAC联合优化。
> 【核心结论】7-bit分辨率在PAM-4系统中是性能和复杂度的良好平衡点。64级量化可以精确表示PAM-4的四个电平，DSP的FFE提供额外的均衡能力。
> 【工程价值】该DAC设计在10nm CMOS工艺下实现了1.7pJ/bit的能效，是当前最先进水平的代表。
> 【落地注意】DAC的静态线性度（INL/DNL）和动态性能（SFDR）需要仔细优化，以避免量化噪声和失真影响信号质量。

### 4.3 Output Pad网络

```
4L-5C输出网络:
• 4个电感 + 5个电容
• 针对带宽/群延迟优化
• 设计目标:
  - 最大化带宽
  - 优化群延迟
  - 改善回波损耗
```

![](/img/serdes/fundamentals/lectures/Session_08V-ULTRA-HIGH-SPEED WIRELINE_images/img-040.jpg)

> 🔍 深度说明：
> 【研究背景】Output pad网络是连接芯片内部电路和外部信道的重要界面。对于224Gb/s系统，pad网络的带宽特性直接影响输出信号质量。
> 【核心结论】4L-5C T-coil网络通过电感和电容的谐振实现带宽扩展，同时优化群延迟以减少信号失真。回波损耗优化确保最大限度地减少反射。
> 【工程价值】T-coil网络可以在保持低功耗的同时实现>40GHz的-3dB带宽，是高速输出网络的常用选择。
> 【落地注意】T-coil网络的敏感度较高，需要考虑工艺波动的影响。建议进行MC分析和角落验证。

---

## 五、设计权衡

### 5.1 关键设计决策

```
时钟选择: 28GHz (vs 14GHz/56GHz)
多路复用: 4:1 (vs 8:1/2:1)
FFE实现: DSP (vs 模拟FIR)
Driver类型: CML (vs SST/Hybrid)
Output Pad: T-coil (vs Pi-coil/LC filter)

功耗: 1.7pJ/bit @ 224Gb/s
```

### 5.2 技术亮点

```
1. 双路径感应峰化时钟分布
   • 同时优化带宽和抖动

2. 8-tap FFE in DSP
   • 灵活均衡
   • 适应不同信道

3. 7-bit DAC
   • 高精度
   • 平衡分辨率和功耗

4. 优化的输出pad网络
   • 最大化带宽
   • 改善信号完整性
```

---

## 六、总结

### 6.1 核心知识点

| 模块 | 关键点 |
|------|--------|
| 数据率趋势 | 32→256Gb/s, PAM-4主流 |
| 224Gb/s架构 | LC PLL + DSP/7b-DAC + CML |
| 时钟分布 | 双路径感应峰化、抖动过滤 |
| 电路实现 | Series-shunt峰化、4L-5C pad |
| 设计权衡 | 功耗1.7pJ/bit、数据率2x提升 |

### 6.2 学习路径

```
基础:
1. 理解超高速有线发展趋势
2. 掌握PAM-4调制优势
3. 学习TX架构选择

进阶:
4. 时钟分布设计
5. DAC/FFE联合优化
6. Output pad网络设计

实战:
7. 224Gb/s系统仿真
8. 功耗优化分析
9. 信号完整性验证
```

---

*本报告由 Martin 整理，融合了224Gb/s PAM-4发射机架构、时钟分布、数据通路设计等技术知识点，2026/04/16*