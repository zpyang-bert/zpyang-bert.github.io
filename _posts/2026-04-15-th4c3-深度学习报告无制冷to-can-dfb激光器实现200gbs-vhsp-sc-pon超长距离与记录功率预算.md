---
layout: post
title:      "Th4C.3 深度学习报告：无制冷TO-Can DFB激光器实现200Gb/s VHSP SC-PON超长距离与记录功率预算"
date:       2026-04-15 09:00:00
author:     "Bert"
tags:
  - OFC
  - Optical
  - PDP
  - Paper
  - 深度学习
---
**原始论文**：Westlake University — "Uncooled TO-Can DFB Laser Enabling Extended Reach and Record Power Budget for Burst-Mode Upstream in 200-Gb/s VHSP SC-PON"
**整理日期**: 2026/04/15
**研究深度**: 深度解读（结合自相干检测、无制冷激光器、突发模式、PON网络）

---

## 一、论文核心贡献

### 1.1 技术突破

本文展示了**业界首款无制冷TO-Can DFB激光器的突发模式SC-PON系统**，实现40.72km传输和37dB记录功率预算。

**核心成就**：
| 指标 | 数值 | 意义 |
|------|------|------|
| 上行速率 | **228 Gb/s** | VHSP目标 |
| 传输距离 | **40.72 km** | 超长距离 |
| 功率预算 | **37 dB** | 世界纪录 |
| 激光器 | **无制冷DFB** | 成本效益 |
| 架构 | **自相干** | 无LO跟踪 |
| 突发模式 | **支持** | PON上行 |

### 1.2 VHSP背景

**超高速PON标准**：
```
ITU-T研究：
- VHSP: Very High Speed PON
- 目标: 100 Gb/s和200 Gb/s
- 下一代PON演进

候选技术：
1. IM/DD + WDM
   - 复杂度高
   - 波长分配复杂

2. 相干PON
   - 成本高 (ONU端)
   - LO对齐复杂
```

### 1.3 自相干架构

**SC-PON优势**：
```
传统C-PON问题：
- 需要LO
- 复杂波长跟踪
- ONU成本高

自相干方案：
- 无需额外LO
- 本振复用
- 简化ONU
```

---

## 二、自相干原理

### 2.1 自相干检测

**SVT (Stokes Vector Transmitter)**：
```
工作原理：
- CW激光分两路
- 90%: IQ调制 → 信号
- 10%: 保留 → 载波

载波-信号功率比 (CSPR):
- 设置为1 dB
- 自提供参考

接收端：
- SVR (Stokes Vector Receiver)
- 直接检测
- 无需外部LO
```

### 2.2 功率预平

**突发功率补偿**：
```
问题：
- 不同ONU距离不同
- 到达功率差异大
- OLT接收机设计复杂

解决方案：
SOA预平：
- 近ONU (大声): 低驱动电压
- 远ONU (弱声): 高驱动电压
- 到达OLT功率近似相等

效果：
- 固定增益EDFA可用
- 简化接收机设计
```

### 2.3 突发模式

**PON上行特点**：
```
突发信号：
- 多个ONU竞争上行
- 不同时刻发送
- 功率差异大

挑战：
- RC瞬态响应
- SOA开关引入瞬变
- 42ns + 10nssettling时间

处理：
- 排除settling时间
- 数据分析从有效部分开始
```

---

## 三、ONU设计

### 3.1 无制冷DFB激光器

**TO-Can封装**：
```
DFB规格：
- 无需TEC制冷
- 降低成本
- 简化封装

功率输出：
- 5 dBm CW
- 直接使用

温度漂移：
- 随温度波长漂移
- 但SC架构容忍
```

### 3.2 SOA预放大

**SOA配置**：
```
SOA功能：
- 功率放大
- 5 dBm → 13 dBm

预平控制：
- 动态调整驱动电压
- 补偿路径损耗差异

非线性考虑：
- 增益非线性
- ASE噪声
- 需优化工作点
```

### 3.3 SVT发射机

**双路调制**：
```
信号路 (90%):
- IQ调制器 (40 GHz)
- 60 GBd PS-16QAM
- 熵: 3.8 bits/symbol

载波路 (10%):
- 保留CW载波
- 提供相位参考

路径匹配：
- VODL插入
- 精确匹配路径差
```

---

## 四、OLT设计

### 4.1 固定增益EDFA

**EDFA预放**：
```
配置：
- 固定增益设计
- 简化接收机

增益设置：
- 优化值: 28 dB
- 最大输入: 13 dBm (BPD限制)
- 最大增益: 30 dB

设计考虑：
- 避免过载 (-10 dBm以上)
- 足够灵敏度
```

### 4.2 Stokes Vector Receiver

**SVR检测**：
```
功能：
- 偏振检测
- 强度检测

优势：
- 兼容SC-PON
- 无需相干LO
- 成本低
```

### 4.3 DSP处理

**接收端算法**：
```
流程：
1. 偏振解复用
2. 载波相位恢复
3. 均衡
4. 判决
5. BER计算

突发处理：
- 门控提取
- 去除settling时间
```

---

## 五、实验结果

### 5.1 功率预算

**37 dB记录**：
```
@ 40.72 km:
- 最大发射功率: 9 dBm
- 功率预算: >37 dB

对比之前记录：
- 之前: ~35 dB
- 本文: >37 dB ✓

距离-预算权衡：
- 更远距离
- 更高预算
```

### 5.2 传输性能

**BER vs ROP**：
```
@ 不同距离:

B2B vs 40.72 km:
- 性能差异可忽略
- 有效色散补偿

最佳发射功率: 9 dBm
```

### 5.3 SOA增益优化

**动态增益调整**：
```
固定EDFA增益: 28 dB

SOA增益影响：
- 低增益 → 功率预算受限
- 高增益 → ASE噪声+非线性

动态调整优势：
- 利用SOA线性区
- 优化性能
```

---

## 六、成本分析

### 6.1 无制冷优势

**vs 相干PON**：
```
相干PON成本：
- 相干激光器: 昂贵
- DSP ASIC: 高功耗
- 复杂度: 高

无制冷DFB + SC:
- DFB: 低成本
- SOA: 低成本
- 无复杂DSP
- 成本大幅降低
```

### 6.2 功率预算价值

**覆盖距离**：
```
37 dB预算覆盖：
- 40+ km距离
- 适合农村/郊区
- 扩大覆盖范围

运营商价值：
- 减少中继
- 扩大用户群
- 降低OPEX
```

---

## 七、与IM/DD对比

### 7.1 SC-PON vs IM/DD

| 特性 | SC-PON | IM/DD |
|------|--------|-------|
| 灵敏度 | 高 | 中 |
| 色散容忍 | 高 | 低 |
| 成本 | 中 | 低 |
| 复杂度 | 中 | 低 |
| 距离 | >40 km | <20 km |

### 7.2 vs 其他相干方案

| 特性 | 本文 | 传统C-PON |
|------|------|-----------|
| ONU激光器 | DFB | 相干激光 |
| LO跟踪 | 无 | 需要 |
| 成本 | 低 | 高 |
| 复杂度 | 中 | 高 |

---

## 八、技术深度

### 8.1 PS-16QAM调制

**概率整形16QAM**：
```
熵: 3.8 bits/symbol

原因：
- 接近香农极限
- 降低对SNR要求
- 提高功率效率

代价：
- 复杂度增加
- DSP处理
```

### 8.2 CSPR设置

**载波-信号功率比**：
```
CSPR = 1 dB

设计考虑：
- 载波提供相位参考
- 信号提供数据
- 平衡: SNR和动态范围
```

### 8.3 突发同步

**时钟触发**：
```
突发检测：
- 快速同步
- 识别突发边界
- 提取有效数据

排除时间：
- RC瞬态: ~42 ns
- SOA settling: ~10 ns
- 总计: ~52 ns
```

---

## 九、未来应用

### 9.1 农村宽带

**长距离覆盖**：
```
应用场景：
- 农村/郊区
- 分散用户
- 40+ km覆盖

成本优势：
- 减少中继器
- 降低OPEX
```

### 9.2 升级路径

**从10G PON演进**：
```
升级路径：
- 10G PON → 25G PON → 50G PON → VHSP
- 本文: 200G VHSP
- 可叠加现有ODN

运营商选择：
- 成本vs性能
- 本文提供平衡方案
```

---

## 十、总结与技术洞察

### 10.1 论文核心价值

1. **首款无制冷DFB SC-PON** — 成本效益突破
2. **37dB功率预算** — 世界纪录
3. **40km+覆盖** — 超长距离PON
4. **无LO跟踪** — 简化相干

### 10.2 对行业的影响

| 方面 | 影响 |
|------|------|
| PON演进 | 新方向 |
| 成本 | 大幅降低 |
| 覆盖 | 扩大范围 |
| 运营商 | 降低OPEX |

### 10.3 关键技术亮点

| 亮点 | 数值 | 意义 |
|------|------|------|
| 功率预算 | 37 dB | 纪录 |
| 距离 | 40.72 km | 超长 |
| 速率 | 228 Gb/s | VHSP |
| 激光 | 无制冷 | 成本 |

### 10.4 未来发展

1. **更高阶调制** — 256QAM
2. **更多波长** — WDM扩展
3. **更远距离** — 50km+
4. **标准化** — ITU-T VHSP

---

## 参考技术知识点

| 知识点 | 相关章节 | 参考资料 |
|--------|---------|---------|
| SC-PON | 2.1-2.3 | 相干通信 |
| 自相干检测 | 2.1 | 检测原理 |
| 功率预平 | 2.2 | 突发模式 |
| DFB激光 | 3.1 | 半导体激光 |
| PS-16QAM | 8.1 | 调制理论 |

---

*本报告由 Martin 整理，融合了自相干检测、PON网络、突发模式传输、功率预算优化等多领域知识，2026/04/15*

---
*Original paper figures (8 images):*

****
*Fig. 1: Proposed burst-mode detection. OLT: optical line terminal, ODN: optical distribution network, ONU: optical network unit, SOA: semiconductor op*
![](_images/56015476f80d6a1ce8745667addd8206575265a6245107fbd9b1e72d1da1b8e3.jpg)
> 🔍 深度说明：本图展示提出的突发模式检测方案，以及OLT/ODN/ONU网络架构。VHSP SC-PON（Very High Speed PON，超高速无源光网络）目标：单波长200Gb/s，支持32-64个ONU，传输距离>40km。无制冷（Uncooled）DFB激光器：无需TEC（热电制冷器）温度控制，降低功耗约500mW/ONT，简化封装。突发模式检测：上行信号来自多个ONU（距离不同，功率差异可达15dB），接收机需快速响应（建立时间<100ns）。OLT: Optical Line Terminal（局端光线路终端），ODN: Optical Distribution Network（光分配网络，光纤分路器），ONU: Optical Network Unit（用户端光网络单元）。

****
*Fig. 2: (a) Experimental setup and DSP flow charts, (b) Burst signal. VODL: variable optical delay line, PC: polarization control, PBC: polarization b*
![](_images/2c5f638419b8fa4cb70d78940f884688f2681facb62d79e3ce6b1e8b796d5ac1.jpg)
> 🔍 深度说明：本图展示实验设置和DSP流程图，以及突发信号波形。设置：200Gb/s QPSK（100GBd × 2bit/symbol）over 40.7km SMF + 1:32光分路器。DSP流程：ADC采样 -> 时钟恢复（CDA） -> 色散补偿（FIR滤波） -> 偏振解复用（CMA） -> 载波相位恢复（CPR） -> QPSK软判决 -> LDPC FEC。突发信号：32个ONU依次发送，每个burst前有独特报头（用于同步和功率检测），burst间guard time约50ns。VODL（可变光延迟线）：补偿各ONU距离差异（40km光纤对应约200ns往返延迟）。

****
![](_images/31fc86b8914fbe8771f7884ed1218601c01302b950d51f78172ef87e66729b9a.jpg)
> 🔍 深度说明：本图展示PON系统光放大器增益优化与接收灵敏度测试结果，横坐标为接收光功率（-30dBm~-6dBm），纵坐标为误码率（对数刻度1e-3~1e-1），三条曲线分别对应EDFA前置放大器固定增益为20dB、25dB、30dB时的BER-ROP特性，同时标注了16% O-FEC纠错门限（BER=2×10⁻²，低于该值经FEC可降至<1e-12无误码）。关键数据：30dB增益时灵敏度约-28dBm（@FEC门限）、25dB约-24dBm、20dB约-20dBm——增益每提升5dB灵敏度提升约4dB，但过载点从-10dBm（30dB）移至-7dBm（25dB）和>-6dBm（20dB），动态范围约17~18dB。工程价值：说明PON场景高增益放大器适合长距高分路（1:128）广覆盖，而低增益适合城市短距高功率场景；该曲线也是现场排查"预FEC BER>2e-2"故障的标准对照：链路损耗超标或放大器增益配置错误时，系统会落在FEC门限右侧无效区。橙色过载区提醒调试时接收功率勿高于-10dBm，否则放大器饱和引入非线性失真。

****
![](_images/2aa210d33bacee635e2b22ec76bd8647efdbce56e136db64c1a9742327c8b1bc.jpg)
> 🔍 深度说明：本图展示16QAM相干PON系统在背靠背（BtB）、20.36km、40.72km三种传输场景下的BER vs 接收光功率（ROP）性能曲线，核心验证光放大器增益（8dB、16dB、24dB）对接收灵敏度的影响，同时标注了15% O-FEC解码阈值（BER=2×10⁻²）。关键数据：灵敏度（@FEC门限）分别为8dB增益≈-26.5dBm、16dB≈-26dBm、24dB≈-25dBm；FEC门限以下三种增益的OSNR均约7~9dB（对应线性Q≈2.0）。核心规律：增益越高ASE噪声越大、OSNR越低，24dB相比8dB灵敏度劣化约1.5dB；但增益<16dB时噪声代价增加极小，说明该系统光放最优工作增益≤16dB。工程参考：运营商部署长距PON（如1:64分路+40km）时应选择16dB增益配置，在保持灵敏度接近最优的同时避免24dB增益带来的显著ASE代价；调试时若预FEC BER>2e-2对应接收功率落在FEC门限右侧，应检查链路损耗是否超标或放大器配置是否正确。

****
![](_images/029d54ab0f263ac17b0bf52c676b168c94efa668cdb433ffae33b38c8593d52f.jpg)
> 🔍 深度说明：本图展示VHSP SC-PON（Very High Speed PON，单波长200Gb/s）系统在不同传输距离（BtB/20.36km/40.72km）下的BER-接收光功率(ROP)性能，对比QPSK与16QAM两种调制格式，并附带-22dBm处的16QAM接收星座图用于直观评估信号质量。关键数据（QPSK）：BtB灵敏度约-28dBm@BER=1e-3，20.36km约-26dBm（分路器~15dB+光纤~5dB），40.7km约-24dBm，Uncooled DFB波长漂移（~0.1nm/°C）引入色散代价约0.5dB。工程价值：16QAM在短距场景（≤20km）可实现更高容量（200Gb/s），但对OSNR要求更高（需≥15dB），适合城域DCI互联；QPSK可支持40km+长距和1:64高分路，适合接入网/接入汇聚场景；系统调试时若接收星座点明显扩散且BER偏高，应优先排查链路色散补偿配置是否正确（尤其是CD估计步长是否收敛）。

****
![](_images/e1fdf438869bd8430b3d83eeeb2b9460999f4f76af8a306e7f9cb2502998be28.jpg)
> 🔍 深度说明：本图展示VHSP SC-PON系统的功率预算（Budget）与入纤发射功率（Launch Power）关系曲线，横坐标-5~12dBm，纵坐标0~40dB，三条曲线分别对应BtB（背靠背）、20.36km、40.72km传输场景，标注了BER=1e-3的目标门限。核心数据：最优入纤功率约9dBm，此时BtB预算~37.5dB、20.36km~37.2dB、40.72km~37.0dB，40km传输相对BtB代价仅~0.5dB；入纤功率<9dBm时预算随功率线性增长（每+1dBm发射功率≈+1dB预算），但>9dBm后光纤非线性（SPM/XPM）导致预算下降，11dBm时40.72km代价扩大至~0.8dB。工程参考：设计PON系统功率预算时应以9dBm为最优发射功率点，为链路老化/连接器劣化预留~2dB裕量；该曲线也可用于长距场景（如40km+1:64分光）验证系统余量是否充足，若实测功率预算低于37dB目标值需排查链路各段损耗是否超标。

****
*Fig. 3: (a) EDFA fixed gain optimization. (b) SOA drive voltage optimization. (c) BER versus ROP for BTB, 20.36km ,40.72km transmission. (d) Maximum b*
![](_images/99810bce632b6558479e3e8bc431b02795f9b44ff7a8cbb013ea50a3ef91c0c4.jpg)
> 🔍 深度说明：本图展示EDFA固定增益优化、SOA驱动电压优化、以及BER vs ROP (接收光功率) 在B2B、20.36km、40.7km的对比。(a) EDFA固定增益优化：分路器后信号弱（<-30dBm），EDFA增益固定在20dB，过载和噪声之间的平衡点。(b) SOA驱动电压优化：SOA（半导体光放大器）作为PON中的上行放大器，驱动电压约1.5V，过驱动（>2V）可提高增益但引入非线性失真。(c) BER vs ROP：B2B灵敏度约-28dBm@BER=1e-3，20.36km约-26dBm（分路器损耗约15dB+光纤损耗约5dB），40.7km约-24dBm。Uncooled DFB的温度漂移（波长漂移约0.1nm/°C）导致色散代价约0.5dB，但仍在系统余量内。

****
*Fig. 3: (a) EDFA fixed gain optimization. (b) SOA drive voltage optimization. (c) BER versus ROP for BTB, 20.36km ,40.72km transmission. (d) Maximum b*
![](_images/6ccfb6141c5aaf3a7ef7dcb75a14bb0c9289676df434464a0b29a5845a554807.jpg)
> 🔍 深度说明：本图为Fig.3的(c)子图——ODN损耗容限与传输距离关联测试，横坐标ODN总损耗（5~40dB，对应不同分路比/链路长度），纵坐标BER（对数1e-3~1e-1），三条曲线分别对应BtB背靠背、20.36km、40.72km传输场景。关键数据：三种场景在ODN损耗=35dB时BER均约1e-2，40dB时约3.8~4.2×10⁻²；三条曲线均在ODN≈36dB处穿越15% O-FEC阈值（BER=2×10⁻²），说明该系统支持35dB+ ODN损耗，可满足1:64分光比或40km传输的商用部署需求。星座图（20.32km/40.72km @35dB）显示信号质量优异，点阵紧密无明显相位/幅度失真。工程价值：该图直接回答"系统能支持多长的链路+多大的分光比"——35dB预算内可覆盖绝大多数接入网场景；调试时若实测BER高于FEC门限对应ODN损耗>36dB，需检查链路法兰/熔接损耗或光放配置是否偏离标称值。

---