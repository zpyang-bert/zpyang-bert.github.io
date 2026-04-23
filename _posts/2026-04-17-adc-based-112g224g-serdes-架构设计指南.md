---
layout: post
title:      "ADC-Based 112G/224G SerDes 架构设计指南"
date:       2026-04-17 09:00:00
author:     "Bert"
tags:
  - 224G
  - SerDes
---
**文档版本**: v1.0  
**撰写日期**: 2026/04/17  
**研究基础**: 48篇SerDes/光通信论文深度学习报告 + 5份综合专题报告  
**目标读者**: 高速SerDes架构师、ADC设计工程师、系统工程师

---

## 执行摘要

随着单lane速率从56G PAM4向112G PAM4乃至200G PAM4演进，传统模拟CDR+CTLE+DFE架构正面临前所未有的挑战：DFE关键路径延迟逼近物理极限、CTLE噪声增强与均衡深度矛盾激化、PAM4的多电平判决对模拟精度要求呈指数级上升。**ADC-Based SerDes架构**通过在接收端前端引入高速ADC，将均衡、时钟恢复、判决等核心功能迁移到数字域实现，正在成为112G及以上速率的确定性技术路线。

本文档基于现有知识库中的Jiang (DMT ADC测试床)、Celik (PAM-16 TI-SAR ADC)、Zhang Hongyang (112Gb/s ADC配合型AFE)、LowPower PAM4 (纯模拟前端对比基准) 等核心论文，系统性地构建ADC-Based SerDes的架构设计指南。核心产出包括：

1. **四种ADC架构的量化选型矩阵**（Flash / SAR / Pipeline / TI-ADC）
2. **分辨率-功耗-速率的设计空间方程**
3. **ADC-Based vs 纯模拟架构的全面对比**
4. **112G与224G场景下的推荐架构及关键参数**

---

## 第一章 ADC-Based SerDes 的驱动力与市场定位

### 1.1 为什么必须走向ADC-Based

从现有论文和行业标准演进可以总结出三个不可逆转的驱动力：

**驱动力一：均衡复杂度超越模拟域处理能力**
- 802.3dj要求200G/lane电接口补偿28dB@53GHz的背板损耗
- 传统CTLE+DFE级联架构在112G时已需要4-tap TX FFE + 多级CTLE + 多tap DFE + Speculative结构
- 论文研究表明，DFE错误传播概率随PAM4电平数增加而恶化，而ADC-Based数字DFE可通过软判决、Turbo均衡等算法大幅降低误码平台

**驱动力二：工艺缩放有利于数字而非模拟**
- 7nm/5nm FinFET工艺中，晶体管本征增益(gm·ro)下降、电源电压降低(<0.8V)，模拟电路设计空间急剧收窄
- 相反，数字逻辑在先进工艺中速度提升、功耗降低、面积缩小，数字均衡器和DSP的能效比持续提升
- Zhang Hongyang论文明确指出：112Gb/s PAM-4前端在7nm FinFet中"需要ADC配合"，28nm的纯模拟方案已难以为继

**驱动力三：灵活性与PVT鲁棒性要求**
- ADC-Based架构可通过数字算法重新配置均衡器结构、抽头数量、CDR带宽
- 面对背板/线缆/芯片封装等多样化信道，同一套ADC+DSP硬件可通过固件适配不同场景
- Celik论文中的PAM-16系统正是利用"模拟域嵌入式均衡+ADC"的混合架构，实现了调制格式的灵活适配

### 1.2 ADC-Based 的市场定位

```
速率演进与架构选择:

25-56 Gb/s NRZ/PAM4  →  模拟CDR+CTLE+DFE  (主流，成熟)
     ↓
112 Gb/s PAM4        →  模拟AFE + 中等精度ADC + 数字DFE/CDR  (过渡/主流)
     ↓
200-224 Gb/s PAM4    →  高精度ADC + 全数字均衡/CDR  (未来确定性方向)
     ↓
400G+ / 相干光       →  高精度TI-ADC + 完整oDSP  (已成熟)
```

**关键判断**：
- **短距(XSR/VSR, <10dB损耗)**：112G仍可维持纯模拟或轻量ADC-Based架构
- **中距(MR, ~20dB)**：112G必须采用ADC-Based或强混合架构
- **长距(LR/背板, ~28-30dB)**：112G及以上只能依赖ADC-Based的数字均衡能力

---

## 第二章 ADC 架构选型深度对比

### 2.1 四种架构的原理与特点

在SerDes接收机中，ADC架构的选择是系统设计的第一个关键决策。下表基于Celik (PAM-16, 8GS/s SAR)、Jiang (DMT测试床, DAC+ADC)、以及光通信oDSP的成熟经验进行综合对比。

| 架构 | 原理 | 速度 | 分辨率 | 功耗 | 面积 | 适用场景 |
|------|------|------|--------|------|------|----------|
| **Flash** | 2^N-1个并行比较器同时比较 | 极高 (>100GS/s) | 低 (4-6bit) | 极高 (指数增长) | 大 | 超高速、低精度、实验室验证 |
| **SAR** | 逐次逼近，二进制搜索 | 中 (1-10GS/s) | 中高 (6-10bit) | 低 | 小 | 能效优先、单通道中速 |
| **Pipeline** | 多级级联，每级处理1-2bit | 中高 (1-5GS/s) | 高 (8-14bit) | 中 | 中 | 高分辨率、中速应用 |
| **TI-ADC** | 多路SAR/Flash交错并行 | 极高 (10-100GS/s+) | 中 (6-8bit) | 中 (M×单通道) | 中 | **112G/224G SerDes主流选择** |

### 2.2 各架构在SerDes中的详细分析

#### Flash ADC

**优势**：
- 无需采样保持即可实现单次转换
- 延迟极低（单时钟周期出结果）
- 理论上可支持>100GS/s采样率

**劣势**：
- 功耗随分辨率指数增长：P ∝ 2^N，7bit Flash的功耗可能是6bit的2倍
- 输入电容巨大，对前级驱动能力要求苛刻
- 比较器失调导致INL/DNL恶化，6bit以上良率极具挑战
- **面积**：7bit Flash需要127个比较器，每个比较器还需要电阻梯和编码逻辑

**SerDes适用性**：
- 仅在实验室概念验证或超短距、极低损耗场景下使用
- 产业界112G/224G接收机**不采用纯Flash架构**

#### SAR ADC

**优势**：
- 能效极高（FoM可达1-10fJ/conv-step）
- 结构简单，面积小，与先进工艺兼容性好
- 单通道6-8bit分辨率下可达到1-5GS/s

**劣势**：
- 速度受限于DAC建立时间和逻辑延迟
- 单通道难以直接支持>10GS/s（对于PAM4 112G需要至少56GS/s）

**SerDes适用性**：
- **TI-SAR的核心构建单元**
- Celik论文中的PAM-16系统采用"8 GS/s TI-SAR ADC"，8路交织实现64GS/s总采样率
- Jiang论文的DMT系统也采用SAR作为子ADC
- 是**当前112G/224G SerDes ADC的主流选择**

#### Pipeline ADC

**优势**：
- 可在较高速度下实现高分辨率（10-14bit）
- 每级增益放大提供了级间噪声隔离
- 适合需要高精度信号处理的场景

**劣势**：
- 功耗和面积显著高于SAR
- 级间增益运算放大器在先进工艺中设计困难
- 延迟较大（通常需要多个时钟周期才能完成转换）

**SerDes适用性**：
- 主要用于相干光通信oDSP（需要10-12bit精度）
- 在电接口SerDes中因功耗/面积过大而**不适用**

#### Time-Interleaved ADC (TI-ADC)

**优势**：
- 通过M路低速子ADC时间交织，等效采样率提升M倍
- 可在保持SAR低功耗优势的同时实现超高采样率
- 架构灵活：子ADC可以是SAR、Flash或Pipeline

**劣势**：
- 通道间失配（offset/gain/timing skew）是核心挑战
- 需要精确的时钟分配网络
- 数字校准逻辑增加面积和功耗

**SerDes适用性**：
- **112G PAM4 SerDes的主流选择**：8×8GS/s TI-SAR = 64GS/s等效采样率（2×过采样）
- **224G PAM4 SerDes的趋势选择**：16×8GS/s TI-SAR = 128GS/s等效采样率

### 2.3 112G/224G 场景下的ADC架构推荐

```
                    112G PAM4 场景
                    
单lane符号率: 56 GBaud (PAM4)
奈奎斯特频率: 28 GHz
推荐过采样率: 1.5x - 2x
所需采样率: 84 - 112 GS/s

推荐架构: 8-12路 TI-SAR ADC
  - 子ADC采样率: 8-12 GS/s
  - 子ADC分辨率: 6-7 bit
  - 等效总采样率: 64-112 GS/s
  - 估算功耗: 80-200 mW (含校准)
```

```
                    224G PAM4 场景
                    
单lane符号率: 112 GBaud (PAM4) 或 56 GBaud (PAM6)
奈奎斯特频率: 56 GHz
推荐过采样率: 1.5x - 2x
所需采样率: 168 - 224 GS/s

推荐架构: 16-24路 TI-SAR ADC
  - 子ADC采样率: 8-12 GS/s
  - 子ADC分辨率: 6-8 bit
  - 等效总采样率: 128-256 GS/s
  - 估算功耗: 200-500 mW (含校准)
```

---

## 第三章 ADC分辨率与系统性能的定量关系

### 3.1 为什么分辨率是关键参数

ADC分辨率直接决定了接收机对PAM4多电平信号的分辨能力，以及数字均衡器的有效精度。分辨率不足会导致：

1. **量化噪声淹没信号**：等效于额外引入热噪声
2. **数字均衡器精度受限**：FFE/DFE系数无法精确收敛
3. **CDR鉴相器分辨率不足**：相位误差检测灵敏度下降

### 3.2 理论分析：ENOB与SNR的关系

ADC的量化噪声功率与分辨率N的关系为：

```
SQNR = 6.02·N + 1.76 (dB)  [理想情况]
ENOB = N - (Noise_Floor - Quantization_Noise)/6.02
```

对于PAM4信号，每个眼图的垂直开口为全幅度的1/3。若要求量化噪声不显著影响眼图质量，通常需要：

```
量化步长 ΔV = V_FullScale / 2^N
每个眼高 = V_FullScale / 3
每个眼内的量化级数 = (V_FullScale/3) / ΔV = 2^N / 3

工程经验：每个眼内至少需要 8-12 个量化级
→ 2^N / 3 ≥ 8  →  N ≥ 4.6 (最低理论值)
→ 2^N / 3 ≥ 16 →  N ≥ 5.6 (工程安全值)
```

### 3.3 不同速率下的分辨率需求

基于PAM4/oDSP报告、Jiang的DMT BER vs ENOB仿真、以及Celik论文的实测数据：

| 数据率 | 调制 | 推荐ENOB | 最低ENOB | 说明 |
|--------|------|----------|----------|------|
| 25-28 Gb/s | NRZ | 4-5 bit | 3.5 bit | 模拟方案仍为主流 |
| 56 Gb/s | PAM4 | 5-6 bit | 4.5 bit | ADC-Based开始显现优势 |
| 112 Gb/s | PAM4 | 6-7 bit | 5.5 bit | **主流需求，6bit为甜蜜点** |
| 224 Gb/s | PAM4 | 7-8 bit | 6.5 bit | 高损耗信道需要更高精度 |

**Jiang论文的关键发现**：
- DMT系统的BER对ADC/DAC的ENOB非常敏感
- 当ENOB < 5 bit时，BER迅速恶化（>10^-4）
- ENOB ≥ 6 bit时，BER进入"平坦区"，继续提高ENOB收益递减
- **6 bit是高速有线通信的一个关键拐点**

### 3.4 ADC功耗的Walden FoM框架

Walden定义的ADC品质因数（Figure of Merit）：

```
FoM_W = Power / (2^ENOB · Sample_Rate)  [pJ/conv-step]

或更常用的:
FoM_S = Power / (10^(SNDR/10) · Sample_Rate)  [fJ/conv-step]
```

基于公开文献的TI-SAR ADC数据：
- 7nm/5nm FinFET工艺中，TI-SAR的FoM可达 **5-20 fJ/conv-step**
- 以112G PAM4为例：
  - ENOB = 6, Sample_Rate = 100 GS/s
  - Power ≈ FoM × 2^6 × 100e9 ≈ 10fJ × 64 × 100e9 = **64 mW**
- 加上时钟树、数字校准、参考电压缓冲，总功耗通常在 **100-200 mW** 量级

### 3.5 分辨率-功耗-速率的系统级权衡

```
设计空间约束方程（经验公式）:

Power_ADC [mW] ≈ k × 2^ENOB × fs [GS/s]

其中 k 取决于工艺和架构:
- 28nm TI-SAR: k ≈ 0.8-1.5
- 7nm TI-SAR:  k ≈ 0.3-0.8
- 5nm TI-SAR:  k ≈ 0.2-0.5

示例计算 (7nm, k=0.5):
- 112G PAM4: ENOB=6, fs=100GS/s → Power ≈ 0.5 × 64 × 100 = 320 mW
  （实际经过优化后通常在150-250mW）
- 224G PAM4: ENOB=7, fs=200GS/s → Power ≈ 0.5 × 128 × 200 = 1.28 W
  （需要架构创新才能控制在500mW以下）
```

**核心结论**：
- 112G PAM4的ADC功耗是可接受的（通常占整个RX的20-40%）
- 224G PAM4若采用全速率高精度ADC，功耗将成为系统瓶颈
- 因此224G时代可能需要：
  1. **Baud-rate CDR** + 1.5x过采样（降低fs）
  2. **模拟预均衡增强**（降低ADC有效动态范围需求）
  3. **PAM6调制**（降低符号率，从而降低fs）

---

## 第四章 数字均衡 vs 模拟均衡的完整对比

### 4.1 两种架构的信号流对比

#### 纯模拟架构（传统方案）

```
Channel → CTLE → VGA → DFE → Slicer → CDR
            ↓     ↓     ↑
          (模拟域闭环，延迟在皮秒级)
```

**代表论文**：LowPower PAM4 (10mW CMOS反相器CTLE)、Loi (25Gb/s模拟FIR)、Zhang Hongyang (28nm CTLE)

#### ADC-Based 架构

```
Channel → CTLE(Optional) → VGA → ADC → RX FFE → DFE → Slicer → CDR
                                          ↑      ↑
                                       (数字域，延迟在纳秒级)
```

**代表论文**：Celik (PAM-16 TI-SAR ADC + 嵌入式模拟FFE)、Zhang Hongyang (112Gb/s ADC配合型)、Jiang (DMT DAC/ADC测试床)

### 4.2 核心性能维度对比

| 对比维度 | 纯模拟架构 | ADC-Based架构 | 胜出方 |
|----------|------------|---------------|--------|
| **功耗(112G)** | 低 (CTLE 10-50mW, DFE 20-80mW) | 中-高 (ADC 100-200mW, DSP 50-150mW) | 模拟 |
| **功耗(224G)** | 极高 (DFE关键路径失效) | 高但可控 (ADC 200-500mW, DSP 100-300mW) | ADC-Based |
| **均衡能力** | 有限 (CTLE峰值<20dB, DFE taps受限) | 极强 (数字FFE taps可达100+, DFE无延迟约束) | ADC-Based |
| **PVT鲁棒性** | 差 (模拟系数随温度漂移) | 优 (数字算法自动跟踪) | ADC-Based |
| **灵活性** | 差 (固定抽头/固定带宽) | 优 (软件定义均衡器) | ADC-Based |
| **延迟** | 低 (<1ns) | 高 (ADC+DSP通常2-10ns) | 模拟 |
| **面积(112G)** | 小 | 中 (ADC+DSP占面积) | 模拟 |
| **面积(224G,7nm)** | 大 (模拟电路难以缩小) | 小 (数字电路高度可缩) | ADC-Based |
| **设计复杂度** | 高 (模拟电路敏感，需大量SPICE迭代) | 中 (数字算法验证更标准化) | ADC-Based |
| **工艺可移植性** | 差 | 优 | ADC-Based |

### 4.3 延迟对比的深入分析

这是ADC-Based架构最受关注的劣势。延迟来源包括：

```
ADC-Based RX 延迟分解:
├── 模拟前端 (CTLE+VGA):     ~50-100 ps
├── ADC 转换 + 采样保持:      ~100-300 ps
├── 数字FFE处理:              ~1-3 UI (视taps和时钟频率)
├── 数字DFE处理:              ~1-2 UI
├── CDR环路延迟:              ~3-10 UI
└── FEC解码 (若需要):         ~50-200 ns
```

**对比**：纯模拟CDR的环路延迟通常<1 UI，整个RX延迟<1ns。

**对应用场景的影响**：
- **数据中心网络**：2-10ns延迟可接受
- **AI/ML GPU Fabric**：延迟敏感，但可通过移除FEC（如Linear Drive方案）或采用轻量DSP来缓解
- **存储互联**：延迟是关键指标，ADC-Based需要特别优化

### 4.4 均衡精度对比

这是ADC-Based的核心优势。以Celik论文中的PAM-16系统为例：

**模拟域均衡的局限**：
- CTLE的峰值增益受噪声和稳定性限制，通常<15-20dB
- 模拟DFE的抽头数量受限于反馈延迟，112G时通常只能实现3-5 tap
- 模拟FFE的系数精度受限于DAC/模拟乘法器，通常4-6bit系数精度

**数字域均衡的优势**：
- RX FFE可实现数十到上百个抽头（Jiang的DMT系统中每个子信道独立均衡）
- 数字DFE可实现10+ tap，且可采用Loop-Unrolled、Soft-Decision等高级结构
- 数字系数精度可达10bit以上，收敛精度远高于模拟
- 可集成高级算法：MLSE、Turbo Equalization、神经网络均衡

---

## 第五章 112G PAM4 场景下的架构推荐

### 5.1 场景分类与架构选择

基于OIF CEI-112G标准空间和现有论文数据，112G PAM4可分为三类场景：

#### 场景A：超短距/短距 (XSR/VSR, <2m, <16dB损耗)

**推荐架构**：**轻量ADC-Based** 或 **强混合架构**

```
TX: 4-tap FFE (模拟实现)
RX: 前端端接网络(Lt+Rt) → CMOS反相器CTLE → VGA → 
    6bit 8×TI-SAR ADC (64GS/s) → 
    数字5-tap FFE → 3-tap DFE → Mueller-Muller CDR
```

**依据**：
- LowPower PAM4论文证明：纯CMOS反相器CTLE可在30dB通道上实现10mW超低功耗
- 对于<16dB损耗，CTLE+VGA+轻量ADC是功耗与性能的最佳平衡点
- ADC仅需6bit，8路TI-SAR即可满足，功耗约80-150mW

**预计总RX功耗**：150-250 mW (含ADC+DSP)

#### 场景B：中距 (MR, ~20dB损耗)

**推荐架构**：**标准ADC-Based**

```
TX: 4-tap FFE
RX: 有源CTLE (gm-C, 可调峰值) → VGA → 
    7bit 8×TI-SAR ADC (64GS/s) → 
    数字15-tap FFE → 5-tap DFE → 数字CDR
```

**依据**：
- 20dB损耗需要更强的均衡能力，数字FFE的tap数优势开始凸显
- 7bit ADC提供足够的动态范围应对PVT变化和信道老化
- Zhang Hongyang论文中的64Gb/s PAM-4前端(2.8mW/Gb/s, 180mW)可视为此架构的降速版本

**预计总RX功耗**：250-400 mW

#### 场景C：长距/背板 (LR, ~28-30dB损耗)

**推荐架构**：**重数字ADC-Based**

```
TX: 4-tap FFE + 可选Pre-cursor增强
RX: 多级级联CTLE → VGA → 
    7-8bit 12×TI-SAR ADC (96GS/s) → 
    数字30-tap FFE → 8-tap DFE → 
    高级CDR + KP4 FEC
```

**依据**：
- 28dB@28GHz损耗下，模拟CTLE无法单独承担，需要长数字FFE补偿残余ISI
- 802.3ck/dj标准要求4-tap TX FFE + 强RX均衡
- 8bit ADC确保在长FFE抽头链中不引入显著量化误差

**预计总RX功耗**：400-600 mW

### 5.2 112G PAM4 ADC 关键参数推荐表

| 参数 | XSR/VSR | MR | LR |
|------|---------|----|---- |
| 子ADC架构 | SAR | SAR | SAR |
| 交织路数 | 8 | 8-10 | 12-16 |
| 子ADC速率 | 8-12 GS/s | 8-12 GS/s | 8-12 GS/s |
| 等效总采样率 | 64-96 GS/s | 64-96 GS/s | 96-128 GS/s |
| ENOB目标 | 5.5-6 bit | 6-6.5 bit | 6.5-7.5 bit |
| 输入带宽 | >35 GHz | >35 GHz | >40 GHz |
| ADC功耗 | 60-120 mW | 100-180 mW | 180-300 mW |
| 模拟前端 | 轻量CTLE | 标准CTLE | 多级CTLE |
| 数字FFE taps | 5-15 | 15-30 | 30-50 |
| 数字DFE taps | 2-3 | 3-5 | 5-10 |

---

## 第六章 224G/200G 场景下的架构展望

### 6.1 224G PAM4 的核心挑战

224G对应802.3dj中的200GBASE-KR1/CR1/DR1。关键参数：
- **符号率**：112 GBaud (PAM4) → 奈奎斯特频率 **56 GHz**
- **典型信道损耗**：背板MR~25dB@40GHz, LR~35dB@40GHz, 甚至更高
- **ADC采样率需求**：按1.5x-2x过采样，需要 **170-225 GS/s**

### 6.2 224G ADC 架构演进路径

当前产业界对224G ADC的主流思考方向：

#### 路径一：扩展TI-SAR (保守方案)

```
24-32路 TI-SAR
- 子ADC: 8 GS/s, 7-8bit
- 等效速率: 192-256 GS/s
- 工艺: 3nm/2nm
- 预估功耗: 400-800 mW
```

**可行性**：
- 技术上可行，但功耗巨大
- 需要极其精确的skew校准（<100fs）
- 时钟分配网络的复杂度剧增

#### 路径二：降低过采样率 + Baud-rate处理 (激进方案)

```
Baud-rate ADC
- 采样率: 112 GS/s (1x)
- 架构: 14-16路 TI-SAR @ 8 GS/s
- 分辨率: 6-7bit
- 均衡: 数字FFE + Baud-rate CDR
```

**优势**：
- 大幅降低ADC功耗（约减半）
- 减轻时钟分配压力

**挑战**：
- Baud-rate采样对CDR和均衡算法要求极高
- 信息论上损失了过采样的冗余度
- 需要更精密的ADC抗混叠滤波器

#### 路径三：模拟预处理 + 中等精度ADC (混合方案) — **最可能的主流**

```
Channel → 前端无源均衡(Lt/Ct网络) → 
          有源CTLE/VGA (提供15-20dB boost) →
          6bit 16×TI-SAR ADC (128GS/s, ~1.1x过采样) →
          轻量数字FFE + DFE + FEC
```

**优势**：
- 模拟前端承担大部分均衡任务，降低ADC动态范围和数字复杂度
- 6bit ADC在128GS/s下功耗可控（约250-400mW）
- 与Linear Drive/CPO趋势兼容（主机侧承担更多处理）

### 6.3 PAM6调制作为224G的替代方案

若224G纯PAM4的ADC功耗难以接受，产业界可能转向：

```
224G数据率 = 56 GBaud × 4 bit/symbol (PAM-16) → 不现实
224G数据率 = 75 GBaud × 3 bit/symbol (PAM-8) → 困难
224G数据率 = 112 GBaud × 2 bit/symbol (PAM-4) → 当前路径

潜在折中:
224G数据率 ≈ 90 GBaud × 2.5 bit/symbol (PAM-6或PCS) 
```

**PAM-6/PCS的优势**：
- 符号率降低，从而ADC采样率需求降低
- SNR需求介于PAM4和PAM8之间
- 已有论文（如Celik的调制阶数分析）证明高阶调制在moderate-loss信道中可行

---

## 第七章 功耗、面积、延迟的系统级权衡

### 7.1 112G RX 功耗预算分解

基于Celik (PAM-16, 49.36mW RX AFE)、LowPower PAM4 (10mW CTLE)、以及产业数据：

```
112G PAM4 ADC-Based RX 功耗分配 (典型值, LR信道):

模拟前端 (CTLE + VGA):
  ├─ CTLE:           30-60 mW
  ├─ VGA:            10-20 mW
  └─ 小计:           40-80 mW  (10-20%)

ADC:
  ├─ 子ADC阵列:      120-200 mW
  ├─ 时钟树/PLL:     30-60 mW
  ├─ 参考缓冲:       10-20 mW
  └─ 小计:           160-280 mW  (40-55%)

数字DSP:
  ├─ FFE:            20-50 mW
  ├─ DFE:            15-40 mW
  ├─ CDR:            20-40 mW
  ├─ 校准/控制:       10-20 mW
  └─ 小计:           65-150 mW  (15-30%)

FEC (可选, 片内):
  └─ KP4 RS-FEC:     50-100 mW  (10-20%)

总RX功耗 (LR, 112G):  350-600 mW
能效:                  3.1-5.4 pJ/bit
```

**对比纯模拟方案**：
- LowPower PAM4纯CTLE方案：10mW → **0.09 pJ/bit** (但仅限于30dB通道且可能需要片外/片内FEC)
- 模拟CDR+CTLE+DFE方案：150-300 mW → **1.3-2.7 pJ/bit**
- ADC-Based方案：350-600 mW → **3.1-5.4 pJ/bit**

**结论**：ADC-Based在112G时功耗比纯模拟高1.5-2倍，但均衡能力和灵活性显著增强。这是**性能与功耗的合理trade-off**。

### 7.2 面积权衡

在7nm/5nm工艺中：
- **模拟电路**：不易缩放，CTLE/VGA面积与28nm相比改善有限
- **数字电路**：高度可缩，FFE/DFE/CDR逻辑在7nm中面积很小
- **ADC**：中等缩放，电容和比较器受工艺限制

```
112G RX 面积分配 (7nm, 估算):
├── 模拟前端:     ~0.03-0.05 mm²
├── ADC阵列:      ~0.05-0.12 mm²  (含校准逻辑)
├── 数字DSP:      ~0.02-0.05 mm²
└── 总计:         ~0.1-0.22 mm²
```

### 7.3 延迟与系统兼容性

| 应用场景 | 可接受RX延迟 | 推荐架构 |
|----------|---------------|----------|
| 数据中心交换机 | <100 ns | 全ADC-Based + FEC |
| AI/ML集群(NVLink) | <10 ns | ADC-Based轻量DSP，或模拟+小ADC |
| 5G前传 | <100 μs | 任意ADC-Based |
| 存储互联 | <1 ns | 模拟优先，或Baud-rate ADC |
| CPO/LPO | <5 ns | 轻量ADC-Based，FEC卸载 |

---

## 第八章 与现有研究工作的关联分析

### 8.1 论文映射

| 论文来源 | 核心发现 | 在本指南中的角色 |
|----------|----------|------------------|
| **Jiang (DMT SERDES)** | >250Gb/s DAC/ADC测试床；ENOB≥6bit是BER拐点；TI-SAR是高速首选 | ADC架构选择的核心依据；分辨率-BER关系的定量支撑 |
| **Celik (EPFL)** | PAM-16系统：8GS/s TI-SAR ADC, 7bit, 嵌入式2-tap模拟FFE, RX AFE 49.36mW | ADC-Based混合架构的典范；模拟预处理+ADC的路径验证 |
| **Zhang Hongyang** | 112Gb/s PAM-4需要ADC配合；7nm FinFet中纯模拟难以为继 | 112G向ADC-Based迁移的转折点论证 |
| **LowPower PAM4** | 纯CMOS反相器CTLE 10mW@112G，30dB通道 | 纯模拟方案的性能边界参考；与ADC-Based的功耗对比基准 |
| **钧衡技术文档** | TX FFE/RX FFE/CTLE/DFE/MLSE完整分类 | 均衡器在模拟域vs数字域中的功能映射 |
| **PAM4/oDSP报告** | PAM4需要5-6bit ADC，NRZ需3-4bit | ADC分辨率需求的理论基础 |
| **IEEE 802.3dj解读** | 200G/lane电接口规范；28dB@53GHz损耗要求 | 224G场景下ADC-Based为确定性方向的产业依据 |
| **LPO报告** | Linear Drive去除DSP/CDR；主机侧承担更多处理 | 224G/CPO场景下"轻量ADC+模拟预处理"架构的产业趋势支撑 |

### 8.2 从研究到工程的Gap

现有论文已验证了以下关键技术点，但工程化仍面临挑战：

1. **TI-SAR的skew校准**：论文多为仿真或测试床，ASIC级别的生产校准良率尚未公开
2. **先进工艺ADC的PVT鲁棒性**：7nm以下工艺的电容匹配、比较器失调随工艺波动加剧
3. **224G的时钟抖动**：ADC采样时钟的抖动要求(fs jitter < 100fs RMS)对PLL是巨大挑战
4. **热噪声与量化噪声的联合优化**：如何在系统级分配噪声预算（thermal vs quantization vs DSP rounding）

---

## 第九章 设计检查清单与工程建议

### 9.1 ADC选型检查清单

```markdown
□ 确定符号率与调制格式
  └─ PAM4 112G → 56 GBaud → 推荐 fs = 84-112 GS/s
  └─ PAM4 224G → 112 GBaud → 推荐 fs = 150-225 GS/s

□ 选择ADC架构
  └─ 112G: 8-12路 TI-SAR (首选)
  └─ 224G: 16-24路 TI-SAR 或 Baud-rate TI-SAR
  └─ 避免纯Flash (功耗/面积过大) 和纯Pipeline (延迟/功耗不匹配)

□ 确定分辨率
  └─ 短距/VSR: 5.5-6 bit ENOB
  └─ 中距/MR: 6-6.5 bit ENOB
  └─ 长距/LR: 6.5-7.5 bit ENOB

□ 评估功耗预算
  └─ ADC功耗不应超过整个RX的50-60%
  └─ 使用 Walden FoM 进行初步估算

□ 时钟方案
  └─ 是否需要片上PLL？
  └─ 采样时钟 jitter 是否 < 150fs RMS？
  └─ 多路交织的 skew 校准精度是否 < 0.1 UI？
```

### 9.2 模拟前端设计建议

```markdown
□ 短距场景(XSR/VSR, <16dB)
  └─ 采用CMOS反相器CTLE或轻量gm-C CTLE
  └─ 前端端接网络可加入Lt实现被动均衡
  └─ ADC前VGA增益范围：0-20 dB

□ 长距场景(LR, >25dB)
  └─ 采用多级级联CTLE (2-3级)
  └─ 每级CTLE峰值限制在8-12dB以避免噪声恶化
  └─ VGA需具备快速AGC能力
```

### 9.3 数字DSP设计建议

```markdown
□ FFE抽头数
  └─ 模拟CTLE较强时: 5-15 taps
  └─ 模拟CTLE较弱时: 30-50 taps
  └─ 224G长距: 可达100+ taps

□ DFE抽头数
  └─ 112G: 3-5 taps (数字DFE无关键路径约束)
  └─ 224G: 5-10 taps
  └─ 考虑Loop-Unrolled结构降低延迟

□ CDR架构
  └─ 112G: 数字Bang-bang CDR 或 Mueller-Muller CDR
  └─ 224G: 考虑Baud-rate CDR降低功耗

□ 自适应算法
  └─ 收敛阶段: CMA (盲均衡)
  └─ 跟踪阶段: DD-LMS (判决导向)
  └─ 步长μ: 0.01-0.1 (收敛) → 0.001-0.01 (跟踪)
```

### 9.4 224G 前瞻建议

```markdown
□ 优先考虑"强模拟预处理 + 轻量ADC"的混合架构
□ 若功耗预算紧张(<3pJ/bit)，研究PAM6/PCS调制降低符号率
□ Baud-rate ADC是值得探索的方向，但需配套先进的Baud-rate CDR算法
□ 考虑将FEC卸载到系统级芯片的其他部分，降低SerDes RX面积/功耗
```

---

## 附录：核心公式速查

### ADC SQNR
```
SQNR_dB = 6.02·N + 1.76
```

### Walden ADC FoM
```
FoM = Power / (2^ENOB · fs)
```

### PAM4 SNR损失 (相对NRZ)
```
SNR_PAM4 = SNR_NRZ - 9.5 dB
```

### 奈奎斯特采样定理
```
fs ≥ 2 × f_Nyquist
(工程建议: fs = 1.5x ~ 2x 符号率)
```

### TI-ADC等效采样率
```
fs_total = M × fs_sub
(M = 交织路数, fs_sub = 单个子ADC采样率)
```

### 能效换算
```
Energy Efficiency [pJ/bit] = Power_RX [mW] / Data_Rate [Gb/s]
```

---

*本文档基于 /mnt/wisewave/research/ 下48篇论文深度学习报告及综合研究成果撰写。*
