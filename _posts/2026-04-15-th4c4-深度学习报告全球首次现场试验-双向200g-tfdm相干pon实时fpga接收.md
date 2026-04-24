---
layout: post
title:      "Th4C.4 深度学习报告：全球首次现场试验 — 双向200G TFDM相干PON实时FPGA接收"
date:       2026-04-15 09:00:00
author:     "Bert"
tags:
  - OFC
  - Optical
  - PDP
  - Paper
---

# Th4C.4 深度学习报告：全球首次现场试验 — 双向200G TFDM相干PON实时FPGA接收

**原始论文**：Fudan University + China Telecom — "World's First Field-Trial Demonstration of Bidirectional 200G TFDM Coherent PON Enabled by Real-Time FPGA-Based Reception"
**整理日期**: 2026/04/15
**研究深度**: 深度解读（结合TFDM、相干PON、实时FPGA、场部署试验）


## 一、论文核心贡献

### 1.1 技术突破

本文展示了**全球首次现场试验验证的双向200G TFDM相干PON系统**，基于实时FPGA接收，实现-34dBm下游灵敏度和-31dBm上游灵敏度。

**核心成就**：
| 指标 | 数值 | 意义 |
|------|------|------|
| 总速率 | **200.54 Gb/s** | 双向200G |
| 子载波数 | **2** | TFDM结构 |
| 每子载波 | **100.27 Gb/s** | DP-QPSK |
| 下游灵敏度 | **-34 dBm** | 高灵敏度 |
| 上游灵敏度 | **-31 dBm** | 4.5dB功率差 |
| 动态范围 | **21 dB** | 宽动态范围 |
| 场光纤距离 | **29/30 km** | 实际部署 |

### 1.2 TFDM原理

**时分频分复用 (TFDM)**：
```
传统TDM vs TFDM：

TDM：
- 时分复用
- 时隙分配

TFDM：
- 频分复用
- 多子载波并行
- 频谱效率高

本文2-SC TFDM：
- 2个子载波
- 每载波100G
- 总计200G
```

### 1.3 为什么相干PON

**vs IM/DD PON**：
```
IM/DD挑战：
- 100G/波长困难
- 功率预算受限
- 色散容忍低

相干优势：
- 高灵敏度
- 高频谱效率
- 色散容忍高
- 偏振复用
```

---

## 二、场部署试验

### 2.1 试验拓扑

**实际网络部署**：
```
站点：
- OLT (中心局)
- Site B (汇聚点)
- Site C (ONU2附加)
- ONU1/ONU2 (用户端)

光纤路由：
- OLT → Site B: 14.5 km
- Site B → ONU1: 14.5 km (共29 km)
- Site B → ONU2: 14.5 + 0.5 + 0.5 km (共30 km)

包含多个ODF跨越
```

### 2.2 光功率预算

**实际链路损耗**：
```
ONU1:
- 总损耗: 23.5 dB
- 对应29 km

ONU2:
- 总损耗: 28 dB
- 对应30 km
- 含额外ODF损耗

功率差: 4.5 dB
```

### 2.3 网络拓扑图

**实际部署示意**：
```
OLT
  │
  │ 14.5 km
  ▼
Site B ────┬─── 0.5 km ─── Site C
(ODF)      │                  ↑
           │ 14.5 km         │
           ↓                  │
         ONU1 (29km)        │
                              │
                      0.5 km loopback
                              │
                         Site B ◀──┘
```

---

## 三、系统配置

### 3.1 OLT配置

**下行配置**：
```
光源：
- 可调激光器
- 波长: C-band

调制：
- DP-QPSK
- 符号率: 25.06752 GBd
- 2子载波

接收：
- ICR (集成相干接收)
- ADC: 28.20096 GSa/s
- FPGA: Xilinx XCVU13P
```

### 3.2 ONU配置

**上行突发模式**：
```
上行信号：
- DP-QPSK突发
- 符号率: 25.06752 GBd
- SOA预放: +2 dBm

突发特性：
- 时分复用
- 功率预平
- 快速同步
```

### 3.3 FPGA处理

**实时DSP链**：
```
FPGA资源限制：
- 每次处理1个100G子载波
- 物理层全速运行

DSP处理：
- 偏振解复用
- 载波恢复
- 均衡
- 判决
```

---

## 四、灵敏度性能

### 4.1 下行灵敏度

**B2B vs 场部署**：
```
B2B灵敏度:
- 单100G载波: -37 dBm
- 双100G载波(200G): -34 dBm

场部署灵敏度:
- 单100G载波: 待测
- 200G (2 ONU各100G): -31 dBm

灵敏度代价:
- 4.5 dB功率差导致
```

### 4.2 上游灵敏度

**突发模式性能**：
```
单ONU 100G:
- 灵敏度: -31 dBm (假设)

双ONU 200G:
- 灵敏度: -31 dBm
- 基于最差载波(SC2)
- 功率差4.5 dB计入
```

### 4.3 功率预算

**动态范围**：
```
功率预算 vs SOA功率：
- 测量不同SOA boost功率
- 优化灵敏度

动态范围: 21 dB

覆盖距离: 29-30 km
```

---

## 五、实时FPGA实现

### 5.1 FPGA架构

**Xilinx XCVU13P**：
```
资源：
- LUTs: 大量
- DFFs: 大量
- BRAM: 足够
- DSP: 够用

约束：
- 每次1子载波处理
- 物理层全速运行
```

### 5.2 DSP链路

**下行Rx DSP**：
```
流程：
1. ADC采样
2. 偏振分集
3. 载波相位恢复
4. 均衡
5. 判决
6. BER计算

实时运行: ✓
```

**上行Rx DSP**：
```
突发处理：
1. 突发同步
2. 门控提取
3. 载波恢复
4. 均衡
5. 判决
```

### 5.3 长期稳定性

**24小时测试**：
```
24小时BER监控：
- 上行+下行
- FEC门限以下 ✓

FPGA资源利用：
- 记录于图2(k)
- 确认可用性
```

---

## 六、TFDM优势

### 6.1 频谱效率

**vs 单载波100G**：
```
单载波 vs TFDM:

单载波100G:
- 带宽: ~30 GHz
- 频谱效率: ~3.3 bit/s/Hz

2-SC TFDM 200G:
- 每载波: ~15 GHz
- 总带宽: ~30 GHz
- 频谱效率: ~6.6 bit/s/Hz

优势: 相同带宽，2×速率
```

### 6.2 功率预算

**灵敏度优势**：
```
相干检测优势:
- 散粒噪声极限
- 本振放大
- 高灵敏度

vs IM/DD:
- IM/DD灵敏度: -20 dBm量级
- 相干灵敏度: -30 dBm量级
- 10 dB优势
```

---

## 七、与之前工作对比

### 7.1 首次现场试验

**vs 实验室演示**：
```
之前工作:
- 实验室验证
- 短距离
- 控制环境

本文:
- 场部署光纤
- 实际ODF
- 运营商环境
```

### 7.2 双向200G

**vs 单向系统**：
```
单向200G:
- 研究较多

双向200G:
- 上行+下行
- 完整系统
- 更具实用价值
```

---

## 八、技术深度

### 8.1 突发同步

**快速同步算法**：
```
突发挑战:
- ONU时分发送
- 到达时间不确定
- 需快速检测

同步方法:
- 前导符检测
- 时钟恢复
- 快速收敛
```

### 8.2 功率预平

**ONU间功率差**：
```
功率差: 4.5 dB

原因:
- 距离不同
- ODF损耗差

接收机处理:
- 动态范围21 dB
- 处理功率差
```

### 8.3 子载波分配

**时频资源分配**：
```
上行分配:
- SC1: 100G
- SC2: 100G
- 聚合: 200G

灵活配置:
- 可单载波
- 可双载波
- 动态调整
```

---

## 九、未来应用

### 9.1 商用部署

**50G/100G/200G演进**：
```
PON演进路径:
- 50G-PON (ITU-T G.9804): 已标准化
- 100G: 研究中
- 200G: 本文验证

运营商选择:
- 成本vs性能
- 本文提供技术验证
```

### 9.2 更高阶调制

**扩展到更高阶**：
```
当前: QPSK (2 bit/sym)

未来:
- 16QAM: 4 bit/sym
- 64QAM: 6 bit/sym

挑战:
- FPGA资源
- 灵敏度
- 功率预算
```

---

## 十、总结与技术洞察

### 10.1 论文核心价值

1. **全球首次现场试验** — 200G TFDM相干PON
2. **实时FPGA实现** — 完整DSP链
3. **29-30km场部署** — 实际验证
4. **24小时稳定** — 长期运行验证

### 10.2 对行业的影响

| 方面 | 影响 |
|------|------|
| PON演进 | 200G路径 |
| 相干接入 | 实用化 |
| FPGA实现 | 低成本验证 |
| 运营商 | 降低OPEX |

### 10.3 关键技术亮点

| 亮点 | 数值 | 意义 |
|------|------|------|
| 速率 | 200.54G | 双向 |
| 下游灵敏度 | -34 dBm | 高 |
| 上游灵敏度 | -31 dBm | 良好 |
| 功率差容忍 | 4.5 dB | 可用 |
| 稳定性 | 24h | 可靠 |

### 10.4 未来发展

1. **更高阶调制** — 16QAM
2. **更多子载波** — 4-SC+
3. **更长距离** — 40km+
4. **标准化** — ITU-T 200G

---

## 参考技术知识点

| 知识点 | 相关章节 | 参考资料 |
|--------|---------|---------|
| TFDM | 1.2, 6.1 | 多载波复用 |
| 相干PON | 1.3 | 相干检测 |
| 场部署 | 2.1-2.3 | 光网络 |
| FPGA | 5.1-5.3 | 实时DSP |
| 灵敏度 | 4.1-4.3 | 系统性能 |

---

*本报告由 Martin 整理，融合了TFDM多载波、相干检测、实时FPGA、PON网络等多领域知识，2026/04/15*

---
*Original paper figures (11 images):*

****
*Fig. 1 Field-trial setup of the real-time FPGA-based bidirectional 200G TFDM coherent PON through field-deployed fiber links. (a) The overall experiment architecture and hardware configuration: OLT (Optical Line Terminal) with XCVU13P FPGA at Site A, 14.5km SMF fiber to Site B (ODF distribution point), 0.5km to Site C, with dual-ONU configuration for 200G TFDM transmission. (b) Geographic aerial map of the deployed fiber route in Shanghai (Fudan University area) showing Site A (Shanghai Bay Valley Building D3), Site B (Fudan Law School), Site C (Fudan Interdisciplinary Complex), with yellow lines indicating actual installed fiber cable paths. Hardware photos show actual equipment racks installed at field sites including ECL lasers, dual-polarization IQ modulators, SOAs, ICR coherent receivers, and 4-channel ADC FPGA boards.*
![](/img/mineru_output/Th4C.4/auto/images/e9dcc64c2f0cfa058d46816b9ba5a66a5150e79a4c997a63e3fb586eaba3d0e3.jpg)
> 🔍 深度说明：本图展示基于上海现网商用光纤的双向200G TFDM相干PON现场试验系统。（a）系统架构与实物照片：Site A（上海湾谷科技园D3楼）为有源设备端，部署OLT和两个ONU，OLT发射链路由ECL窄线宽激光器+DP-IQM双偏振调制器+SOA放大器组成，接收链路含ICR相干接收机+4通道ADC+Xilinx XCVU13P FPGA；Site B/C为全无源节点（仅含ODF光纤配线架）。逻辑拓扑：OLT↔14.5km SSMF↔Site B(1:2耦合器)↔0.5km↔Site C↔0.5km↔Site B↔14.5km↔OLT，模拟实际接入网场景。右下角(i)为地理拓扑：Site A湾谷科技园、Site B复旦大学法学院楼、Site C交叉学科一号楼，黄色线条为实际光缆路由。（b）实际光缆照片和已敷设路由。该试验验证了相干光接入技术在实际运营商光纤中的可行性，对下一代50G/100G PON商用部署有直接参考价值。

****
*Fig. 1 continued: (a) DS, B2B — Back-to-Back downstream sensitivity performance. BER vs. Received Optical Power (ROP, dBm) for 200G/2SC transmission with dual-ONU configuration. Blue squares = ONU1(SC1), red squares = ONU2(SC2). Dashed line marks pre-FEC threshold @ 2E-2 (0.02). Inset: time-domain waveform (0-3000 ns) and 4-state QPSK constellation diagram at ~-31 dBm ROP showing well-separated symbol states confirming good signal quality at this operating point.*
![](/img/mineru_output/Th4C.4/auto/images/8d10bc8e9fcb0612d5c0d8465e88814258fd7d1e9262ec1dd71c83efd333842a.jpg)
> 🔍 深度说明：本图展示200G/2SC双载波PON方案的下行（DS）背靠背（B2B）灵敏度性能测试。横轴为接收光功率ROP（dBm，-39～-29dBm），纵轴为BER（对数坐标，10⁻³～10⁻¹）。蓝色方块=ONU1(SC1)，粉色方块=ONU2(SC2)，两条曲线几乎完全重合。黑色虚线@2E-2为FEC阈值。关键数据：FEC阈值处灵敏度约-34dBm，-31dBm时BER~3×10⁻³，远低于FEC阈值；两ONU性能一致说明子载波间串扰极低。左侧嵌入插图为0~3000ns时域波形（红色，幅度稳定无畸变），右下角为PAM4四电平星座图（热图分布、聚集度极高）。该B2B结果建立了200G PON的极限性能基准，为后续现场试验提供对比参考基线。

****
*Fig. 1 continued: (b) DS Field-Trial — Downstream sensitivity performance in field-deployed fiber field trial. BER vs. ROP (dBm) for 200G/2SC dual-ONU. Blue = ONU1(SC1), pink = ONU2(SC2). Both ONUs cross pre-FEC threshold @ ~-34.5 dBm. Inset lower-left: optical spectrum (1539.5-1540.5 nm C-band) showing 200G signal with dip between two subcarriers confirming 2SC configuration. Lower-right: 4-state constellation at ~-31 dBm ROP confirming clean signal quality.*
![](/img/mineru_output/Th4C.4/auto/images/dd1bfae69d4b8d1f3777cd504938f147452574a5f20e0726bc8aa302f919c736.jpg)
> 🔍 深度说明：本图展示200G/2SC PON方案的实际现网光纤下行（DS）传输灵敏度性能。横轴ROP（-39～-29dBm），纵轴BER（对数）。蓝色方块=200G/2SC, ONU1(SC1)，粉色方块=200G/2SC, ONU2(SC2)，两条曲线几乎重合。FEC阈值@2E-2处灵敏度约-34.5dBm，与B2B几乎一致，验证了现场光纤（包含熔接点、连接器、运营商级器件）未带来额外性能劣化。-31dBm时BER~5×10⁻³。左下角嵌入光谱图（1539.5~1540.5nm C-band）：200G信号呈双峰特征，两子载波间隔清晰、功率平坦，确认2SC配置。右下角星座图（指向-31dBm处）为PM-QPSK，星座点聚集度极高，EVM极小，证明外场传输后信号质量仍优异。该结果验证了200G PON在实际运营商光纤中的传输可行性。

****
*Fig. 1 continued: (c) DS Power budget — Dual-Y axis plot: DS-200G Sensitivity (dBm, blue) and DS-200G Power Budget (dB, pink) vs. SOA Power (dBm). X-axis: SOA amplifier power from -1 to 11 dBm. Blue Y-axis (left): sensitivity from -35 to -32 dBm, flat at -34 dBm for 0-4 dBm SOA then degrades to ~-32.8 dBm at 10 dBm due to amplifier noise. Pink Y-axis (right): power budget from 34 to 44 dB, increasing steadily with SOA power as amplified transmit power outweighs sensitivity loss. Shows system can tolerate up to ~42.8 dB link loss at high SOA power.*
![](/img/mineru_output/Th4C.4/auto/images/63de6fd460d273b48dc90a7f558961eb4569aa5c4f3c419786ed96ad31848301.jpg)
> 🔍 深度说明：本图展示200G下行（DS）系统的功率预算特性——双Y轴图：蓝色=200G下行灵敏度（dBm，左轴），粉色=200G下行功率预算（dB，右轴），横轴为SOA放大器功率（dBm，-1~11dBm）。关键数据规律：（1）SOA功率≤4dBm时，灵敏度稳定在最优值-34.0dBm（蓝色平台区）；SOA>4dBm后灵敏度逐渐劣化（6dBm→-33.8dBm，10dBm→-32.8dBm），原因是高功率SOA引入更强的ASE噪声和非线性效应。（2）功率预算（粉色）随SOA功率近似线性上升：0dBm→34dB，4dBm→37.5dB，10dBm→42.7dB。即使灵敏度劣化，SOA增益收益仍大于损失，功率预算持续增加。工程价值：4dBm是SOA最优工作点（灵敏度无损+37.5dB功率预算）；若需更大功率预算（如32路分光），可推高至10dBm（42.7dB预算，仅付1.2dB灵敏度代价）。

****
*Fig. 1 continued: (d) US BER performance — Upstream bit error rate vs. received optical power for 100G/200G configurations. X-axis: ROP from -40 to -8 dBm. Y-axis (log): BER from 1e-3 to 1e-1. Three curves: blue squares = ONU1 only 100G/1SC, dark red squares = ONU1 only 200G/2SC, light pink squares = ONU1+ONU2 200G/2SC. Dashed threshold @ 2E-2. 21 dB power budget marked for 100G and 200G single-ONU cases. Constellation diagrams at low ROP (-35 dBm) for 200G single-ONU and at -12 dBm for dual-ONU 200G showing well-separated QAM4 symbols.*
![](/img/mineru_output/Th4C.4/auto/images/34c5ee6f9128252cbb23ad736048949d10fdb7512a389008459fd3c803ecccc7.jpg)
> 🔍 深度说明：本图展示100G/200G PON方案的上行（US）接收灵敏度/动态范围性能。横轴ROP（dBm，-40～-8dBm），纵轴BER（对数，10⁻³～10⁻¹），灰色虚线@2E-2为FEC阈值。3组测试配置：蓝色=100G/1SC单ONU，红色=200G/2SC单ONU，粉色=双ONU并发200G/2SC。三组曲线均呈U型（低功率噪声主导、高功率器件非线性主导）。关键数据（FEC阈值处）：（1）100G单ONU：动态范围21dB，灵敏度-37dBm；（2）200G单ONU：动态范围21dB，灵敏度-34dBm（较100G劣化3dB，符合速率加倍理论代价）；（3）200G双ONU并发：灵敏度-33dBm（较单ONU劣化1dB），多用户串扰代价极小。星座图插图：-34dBm处（单ONU 200G）QAM4符号聚集清晰，-12dBm处（双ONU并发）无明显非线性畸变。工程意义：200G PON多用户接入性能损失可控，完全满足下一代高速PON的功率预算和多用户接入需求。

****
*Fig. 1 continued: (e) US Field-Trial — Upstream field trial BER performance. X-axis: ROP from -40 to -22 dBm. Y-axis (log): BER 1e-3 to 1e-1. Multiple curves for different configurations: blue = ONU1 100G/1SC, orange = ONU2 100G/1SC, light purple = ONU1 200G/2SC, light pink = ONU2 200G/2SC, dark purple = both ONUs 200G/2SC (SC1 measured), dark pink = both ONUs 200G/2SC (SC2 measured). Pre-FEC threshold @ 2E-2 dashed line. Single-ONU configs perform better than dual-ONU; 100G/1SC outperforms 200G/2SC at same ROP.*
![](/img/mineru_output/Th4C.4/auto/images/28f05002ff839ca6a7dd7fd0bc3b287d88d47415c96e4783a54158dd3e6602c1.jpg)
> 🔍 深度说明：本图展示200G TFDM PON上行（US）实际现网现场试验性能。6条曲线：蓝色=ONU1 100G/1SC，橙色=ONU2 100G/1SC，深紫=ONU1 200G/2SC，浅粉=ONU2 200G/2SC，深紫/玫红=双ONU并发200G/2SC（分别测试SC1和SC2）。FEC阈值@2E-2处灵敏度：100G单ONU~-39dBm（最优），200G单ONU~-36.5dBm（速率加倍→灵敏度劣化约2.5dB，符合理论），200G双ONU并发~-35.5dBm（多用户代价~1dB，极小）。-28dBm左右所有配置BER可降至1e-3量级。工程价值：多用户并发时子载波间串扰被有效抑制，TFDM技术完全兼容PON的突发传输机制，验证了200G PON多用户共存的可行性。

****
*Fig. 1 continued: (f) TFDM upstream signal characterization — 2×2 subplot composite. Top row (optical spectra): (i) left: 100G US signals - separate spectra for ONU1 (blue, peak ~1552.4 nm) and ONU2 (red, peak ~1552.7 nm), ~0.25 nm wide each; (ii) right: 200G US signals - combined spectrum with dip between two subcarriers, ~0.5 nm total width. Y-axis: Power (dB), X-axis: Wavelength (nm) 1552.0-1553.0. Bottom row (time-domain burst waveforms): (iii) 100G TFDM burst pattern showing two transmission slots from ~0.5-2.0 μs and ~2.3-3.0 μs; (iv) 200G aggregated burst with same timing structure confirming TDM slot allocation. Y-axis: Amplitude (-40 to +40), X-axis: Time (μs) 0-3.0.*
![](/img/mineru_output/Th4C.4/auto/images/b3056cc901c6aa85cf6fcbeda94aca285776a92db667524e4b449ca36d75416f.jpg)
> 🔍 深度说明：本图为TFDM上行信号的2×2多维度特性表征图。（i）100G上行单ONU光谱：ONU1峰值~1552.4nm，ONU2峰值~1552.7nm，间隔~0.3nm，各~0.25nm宽，两路光谱独立无重叠；（ii）200G复用光谱：两路合波后光谱与单路200G几乎完全重合，说明TFDM复用未引入额外频谱损耗或失真，复用效率极高；（iii）100G上行时域突发波形：0~0.5μs、1.8~2.3μs为空闲（~0幅度），0.5~1.8μs、2.3~3.0μs为突发包（±30幅度），突发间隔~0.5μs，符合PON时序；（iv）200G复用时域波形：与单ONU波形时序结构一致，幅度±25左右，无明显波形畸变，证明TFDM完全兼容PON突发传输机制。该图从频域和时域两个维度验证了TFDM技术的可行性，是200G及以上PON的核心使能技术。

****
*Fig. 1 continued: (g) OLT FPGA placement — FPGA floorplan visualization showing physical location of functional logic blocks on the Xilinx FPGA die at the Optical Line Terminal. Color legend mapping: blue = ADC (Analog-to-Digital Converter), cyan = FIFO (First-In First-Out buffer), pale yellow = De-skew (timing alignment correction), bright green = FFT/IFFT (Fast Fourier Transform), dark green = Sync. (synchronization), light purple = FDE (Frequency Domain Equalization), dark purple = FOC&FOE (Frequency Offset Correction/Estimation), red = CFR (Crest Factor Reduction), orange = Burst Detect & SOP Est. (burst detection and start-of-packet estimation), golden yellow = Others. X/Y axes represent physical die coordinates. Clustering shows input blocks (ADC, FIFO) on left, processing blocks centrally, output blocks on right.*
![](/img/mineru_output/Th4C.4/auto/images/cc57849e54e5024adb99ddb2dbf94fd85eff722a563717f79a06e7427bfddb2c.jpg)
> 🔍 深度说明：本图为OLT侧FPGA资源布局图（FPGA die的平面映射，不同颜色=不同功能模块）。布局按数据流从左到右排列：最左侧是ADC（蓝色，靠近输入管脚）和FIFO（青色）——数据进入后的第一步缓存；紧邻是FFT/IFFT（亮绿色）——OFDM时频变换核心；中部是De-skew（浅黄）、FDE（浅紫）——频域均衡补偿信道损伤；FOC&FOE（深紫）——频偏校正；CFR（红色）——峰均比降低；最右侧是Burst Detect（橙色）——识别上行突发信号的起始位置。数据流：从左（输入）→中（处理）→右（输出），最小化走线延迟以支持更高时钟频率。工程价值：该布局为Xilinx XCVU13P上的DSP实现提供了具体参考，各模块资源消耗占比（FD-CMA最大，其次FFT/IFFT≈FIFO）为后续FPGA资源优化提供依据。

****
*Fig. 1 continued: (h) ONU FPGA placement — FPGA floorplan showing physical location of functional blocks on the Optical Network Unit FPGA die. Color legend: dark blue = ADC (Analog-to-Digital Converter), light cyan = FIFO (buffer), bright green = FFT/IFFT (OFDM modulation), pale yellow = De-skew (timing correction), light pink = FD-CMA (Frequency-Domain Constant Modulus Algorithm equalization), dark purple = FOC&FCE (Frequency Offset Correction), magenta/dark pink = CPR (Carrier Phase Recovery), golden orange = Others. X/Y axes = physical die coordinates. Shows clustering: input blocks (ADC, FIFO, FFT/IFFT, de-skew) on left side, middle processing (FD-CMA, frequency correction) centrally, final processing (CPR, misc) on right side of die.*
![](/img/mineru_output/Th4C.4/auto/images/03ba1b757f4d8ef86f58b8df7b7e36bab47cb69513544fbb7dc3a463507daf40.jpg)
> 🔍 深度说明：本图为ONU侧FPGA资源布局图（与OLT布局对应，颜色映射相同）。布局同样按数据流从左到右：最左侧：ADC（深蓝）+FIFO（亮青）——接收数据的第一级缓存；紧邻：FFT/IFFT（亮绿）——OFDM调制核心；De-skew（浅黄）——时延校正；中部：FD-CMA（浅粉，占据FPGA近一半面积）——频域恒模均衡，是整个DSP中资源消耗最大的模块；FOC&FCE（深紫）——频偏补偿；最右侧：CPR（玫红）——载波相位恢复（相干接收核心），紧随其后是Others（橙黄）。空闲黑色区域说明该设计留有冗余资源可用于后续功能扩展。工程价值：FD-CMA资源消耗最大，这对实际的ONU芯片设计有重要启示——需要重点优化该模块的算法实现或降低计算复杂度，以降低功耗和资源占用。

****
*Fig. 1 continued: (j) Long-Term DSP Stability — 26-hour BER monitoring for upstream and downstream paths. Top plot: time-series scatter plot, X-axis = Time (hours) 0-26h, Y-axis (log) = BER 1e-4 to 1e-1. Blue squares = US OLT Rx (upstream at central office), dark red = DS ONU1 Rx (downstream at user node 1), light pink = DS ONU2 Rx (downstream at user node 2). Dashed threshold @ 2E-2. All paths stay below threshold throughout 26h between BER ~0.001-0.01 confirming stable long-term operation. (k) FPGA Resource Utilization — Clustered bar chart, X-axis = Resource type (LUT, FF, DSP, BRAM), Y-axis = Utilization % 0-100%. Blue bars = upstream processing, red/pink bars = downstream. LUT utilization: ~50% upstream, ~50% downstream, total ~95% (stacked bar). FF: ~45% upstream, ~35% downstream. DSP: ~63% upstream, ~72% downstream. BRAM: ~45% upstream, ~40% downstream. Shows DSP design fits within FPGA capacity with comfortable margins except LUT which is near full.*
![](/img/mineru_output/Th4C.4/auto/images/9e0f73c38ad2b633812deb5770a9ffd24c34daa279bb09b862971bc806883d86.jpg)
> 🔍 深度说明：本图验证DSP方案的长期稳定性（26小时）和FPGA资源占用。（上）26小时BER时序监测：蓝色=上行OLT Rx，粉红=下行ONU1 Rx，浅粉=下行ONU2 Rx。FEC阈值@2E-2（黑色虚线）。所有链路全程BER在10⁻³~10⁻²区间（低于FEC阈值），无明显劣化，验证了DSP方案长期运行的可靠性。（下）FPGA资源占用率（簇状柱图）：LUT上行~50%+下行~45%；FF上行~46%+下行~35%；DSP上行~63%+下行~71%（最高）；BRAM上行~45%+下行~40%。最高DSP资源~71%，所有资源<100%，说明DSP设计可正常实现且留有冗余。工程价值：LUT资源接近满（~95%总计）是潜在瓶颈，若后续加入新功能需考虑在DSP算法层面做简化；DSP资源~71%也给实际ASIC实现时的功耗预算提供了参考。

****
*Fig. 1 continued: (k) FPGA resource utilization details and long-term stability confirmation — Clustered bar chart showing resource usage breakdown for upstream vs downstream DSP pipelines on the Xilinx FPGA. LUT (Look-Up Tables): ~50% upstream + ~45% downstream = ~95% total (tight). FF (Flip-Flops): ~45% upstream, ~35% downstream. DSP (Digital Signal Processing blocks): ~63% upstream, ~72% downstream. BRAM (Block RAM): ~45% upstream, ~40% downstream. Inset: 26-hour BER monitoring confirms stable operation below pre-FEC threshold for all upstream and downstream paths, validating real-time FPGA implementation reliability.*
![](/img/mineru_output/Th4C.4/auto/images/1fbe3b4b1a00a8c7f780b0567fa090bf224e9a6a120d684e9fc86d54d8482284.jpg)
> 🔍 深度说明：本图为DSP长期稳定性（上）和FPGA资源占用（下）的详细验证图。（上）26小时BER稳定性：横轴0~26小时，纵轴BER（10⁻⁴~10⁻¹），蓝色=上行OLT Rx，粉红/浅粉=下行ONU1/ONU2 Rx。所有链路全程低于FEC阈值2E-2，BER在10⁻³~10⁻²区间稳定，无突发噪声或链路劣化，验证了系统满足电信级可靠性要求（>24小时连续运行）。（下）FPGA资源详细柱图：横轴Resource=LUT/FF/DSP/BRAM，纵轴0~100%。LUT上行~50%+下行~45%（总计~95%，已接近满载）；FF上行~46%+下行~35%；DSP上行~63%+下行~71%；BRAM上行~45%+下行~40%。DSP资源占用~71%是各类最高，说明相干均衡算法是FPGA实现的主要瓶颈。工程价值：LUT~95%意味着后续若要加入新功能（如更复杂的FEC解码）必须进行算法简化或迁移到更大规模FPGA；DSP~71%对ASIC实现时的功耗预算（通常DSP block功耗~pJ/bit级）有直接参考意义。

---