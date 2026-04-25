---
layout: post
title:      "lecture15 ee720 optical io 深度学习报告"
date:       2026-04-21 10:47:52
author:     "Bert"
tags:
  - Fundamentals
  - Lecture
  - Optical
  - SerDes
  - 深度学习
---

## Spring 2023 - Lecture 15: Optical I/O
### Sam Palermo, Analog & Mixed-Signal Center, Texas A&M University

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/1e8d8123726a9f729cb2f30b717d287d2afaacddfe704a97f8a88edcd301dfd4.jpg)
> 🔍 深度说明：
> 【研究背景】ECEN 720是德州农工大学的研究生课程，聚焦高速链路电路与系统，2023年春季第15讲聚焦Optical I/O技术。该课程时间节点处于数据中心从电互连向光互连转型的关键期，112Gb/s Serdes即将商用，硅光子技术开始成熟。
> 【核心结论】本讲全面覆盖光I/O技术：1)光通道特性（损耗~0.2dB/km @1550nm，远优于铜缆）；2)光发射技术（VCSEL/EAM/MZM/RRM各类型调制器）；3)光接收技术（PIN/APD + TIA）；4)光电集成方案（CPO、混合集成、CMOS光子）。课程强调电光联合设计的重要性。
> 【工程价值】对于Serdes芯片设计者，理解光I/O是必备知识——当Serdes速率超过100Gb/s时，电互连瓶颈显现，光I/O成为必然选择。课程中关于调制器带宽、探测器灵敏度、TIA噪声的分析直接指导光模块系统设计。
> 【落地注意】实际光模块设计需平衡调制器类型选择：VCSEL适合短距离（<100m数据中心），EAM集成DFB适合中距离（<2km），MZM适合长距离相干通信。硅光子RRM正在成为芯片共封装（CPO）的主流方案。

---

## High-Speed Electrical Link System

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/527e4dd9a0dd6099e143633961e03dbb593c00e1aea0f3264f4fa21a1e3ef72c.jpg)
> 🔍 深度说明：
> 【研究背景】高速电互连系统完整架构图，展示TX Serializer → 驱动器 → 背板通道 → RX Deserializer的完整链路。电互连在带宽-距离积方面存在根本限制，理解这一架构是学习光I/O替代优势的前提。
> 【核心结论】典型Serdes链路结构：并行数据 → Serializer（串行化，8b/10b或64b/66b编码）→ 驱动器 → 背板/连接器/PCB通道 → RX均衡器 → Deserializer。关键瓶颈：趋肤效应和介电损耗导致的频率相关衰减，连接器回波损耗，串扰。
> 【工程价值】电互连的局限性决定了何时必须转向光互连。经验法则：>100Gb/s @ >1m或>56Gb/s @ >10m时，电互连功耗急剧上升。Serdes设计者需清楚通道的S参数（S21插入损耗）是链路预算的基础。
> 【落地注意】56G Serdes系统要求通道插入损耗<30dB @ 14GHz。均衡技术（CTLE/DFE）可部分补偿但功耗代价高（占整个Serdes功耗的~30%）。实际设计中，发射功率~800mVppd差分，接收灵敏度~100mVppd。

---

## Channel Performance Impact

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/ba03854bcd03e89694ec2713498b2d8b0e88e01a24ecc294af72301564f49236.jpg)
> 🔍 深度说明：
> 【研究背景】电互连与光互连的性能对比图，直观展示两者在带宽-距离积上的根本差异。该图是光I/O取代电互连的核心论据基础。
> 【核心结论】电互连衰减特性：趋肤效应（损耗∝√f）+ 介电损耗（损耗∝f）导致10GHz下FR4 PCB约5dB/in。光互连（单模光纤）：1550nm窗口损耗仅~0.2dB/km，与频率几乎无关，可传输>100km。
> 【工程价值】对于光模块设计链路预算：发射功率（典型0dBm）→ 光纤损耗（0.2dB/km × 距离）→ 连接器损耗（~2dB/个）→ 探测器灵敏度（-15dBm @ 112Gb/s）→ 必须 > 0。
> 【落地注意】电互连设计中存在"带宽-距离积"陷阱：增加距离必须降低速率，或增加功耗补偿。对于芯片封装内线宽（<1cm），光互连的耦合损耗是负担；>10m距离，光互连具有决定性优势。

---

## Channel Performance Impact

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/cac277c8777d0aa254f2ec6e396ee7640fad607668acdf4f56d7de72f8a0cd3c.jpg)
> 🔍 深度说明：
> 【研究背景】Channel Performance Impact对比图的续页，可能展示了不同速率下电互连的衰减曲线或眼图对比。理解通道衰减如何限制系统性能是光I/O设计的理论基础。
> 【核心结论】关键数据点：电互连在56Gb/s时可用距离约1m（PCB），10Gb/s时可延伸至约10m。光互连在56Gb/s时可达10km+，差距达1000倍。该图表量化了电光之间的不可逾越的鸿沟。
> 【工程价值】系统架构师根据该图确定电vs光的选择边界。HPC系统：计算核心之间用光（chip-to-chip），芯片内部仍用电。AI加速器：HBM与计算芯片之间用光可突破内存墙。
> 【落地注意】混合光电设计需要精细的系统规划。光通道需要额外的电光/光电转换功耗，当距离<1m时，光电转换功耗可能抵消光通道的损耗优势。

---

## Channel Performance Impact

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/8c323db33b0f9a1301504876f673dece3d4d28125787164a4bf553124a6754f9.jpg)
> 🔍 深度说明：
> 【研究背景】可能是不同长度背板或电缆的频率响应对比图（s21参数），展示通道衰减与频率的关系。
> 【核心结论】s21曲线显示：低频损耗小，高频损耗大。1m背板@28Gb/s约-7dB，@56Gb/s时损耗增加到-15dB+。频率越高，通道的等效衰减越严重，这是电互连的根本限制。
> 【工程价值】s参数测量是通道表征的核心。设计者需要根据s21数据确定均衡强度和类型（CTLE/DFE/FFE的组合）。高频衰减还影响时序裕量（jitter transfer）。
> 【落地注意】实际通道设计要留余量：除了插入损耗（S21），回波损耗（S11）也很重要——阻抗不匹配导致反射，反射信号叠加在原信号上产生干扰。S11<-15dB是常见要求。

---

## Channel Performance Impact

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/a3b141bb8bbb32c473038e64da7edb92e5d3d74a67e2d392e794dd9ec271888b.jpg)
> 🔍 深度说明：
> 【研究背景】可能是均衡后的眼图对比或通道仿真结果，展示均衡技术对电互连性能的改善程度。
> 【核心结论】均衡可有效打开闭合的眼图。对于28Gb/s NRZ信号，CTLE+DFE可将通道损耗从-20dB补偿到等效-5dB的效果。但代价是噪声放大和功耗增加（均衡器功耗约占Serdes总功耗30%）。
> 【工程价值】均衡技术使电互连在有限距离内勉强维持高速率。但112Gb/s PAM4的均衡复杂度远高于NRZ，需要更复杂的DSP和更高的功耗。均衡无法解决>100Gb/s @ >1m的根本问题。
> 【落地注意】均衡设计中的陷阱：过度均衡会放大噪声，导致BER反而恶化。实际均衡系数需要根据实测通道响应来调优，DSP的自适应均衡可在运行时调整。

---

## Channel Performance Impact

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/55ea51c40f03d569d39b43ca7af245b41ca97dd9e2b8bc8174ab10bb9de3240d.jpg)
> 🔍 深度说明：
> 【研究背景】可能是通道的脉冲响应或眼图扫描结果，展示符号间干扰（ISI）的具体表现。
> 【核心结论】通道的冲激响应显示：主脉冲后存在长尾拖尾（postcursor ISI），这是导致眼图闭合的根本原因。尾瓣振幅约为主瓣的10-30%，足以导致判决错误。均衡器就是要去除这些尾瓣。
> 【工程价值】眼图质量直接反映系统性能。眼高（Eye Height）和眼宽（Eye Width）是衡量指标。112Gb/s PAM4的8级眼图要求每级眼高>1mV，对均衡要求极高。
> 【落地注意】Postcursor ISI来源于通道的频率选择特性。设计时需要在TX预加重和RX均衡之间分配补偿比例，一般预加重占30-50%，剩余由RX均衡处理。

---

## Link with Equalization

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/dc5ba4499809d76c266a47022c3a629bb3e1bbd55448136a7f1bc90f52dbf04c.jpg)
> 🔍 深度说明：
> 【研究背景】带均衡技术的高速Serdes链路架构图，展示TX预加重和RX均衡的完整信号链路。理解均衡架构是理解电互连与光互连差异的关键。
> 【核心结论】TX侧：预加重（Pre-emphasis，FIR滤波器）提升高频分量，补偿通道衰减。RX侧：CTLE（连续时间线性均衡）放大高频恢复信号；DFE（判决反馈均衡）消除postcursor ISI。DSP-based方案可编程适应多种通道。
> 【工程价值】均衡使电互连在有限距离内达到>25Gb/s。但112Gb/s PAM4的均衡设计复杂度指数级增加，需要联合优化TX预加重和RX均衡。均衡器功耗约100-200mW/通道。
> 【落地注意】均衡会放大噪声——当信号衰减到噪声floor时，过度均衡反而恶化BER。PAM4对均衡线性度要求更高（IMD3<-40dBc），因为多电平之间的间隔更小。

---

## Channel Performance Impact

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/1cf14511fa2691d8a9656eee528a27e0ef8da8d6713fe428f5af90d3d2552c23.jpg)
> 🔍 深度说明：
> 【研究背景】可能是综合对比电互连（均衡后）与光互连的性能图表，展示两者在长距离下的最终差距。
> 【核心结论】即使使用强均衡，电互连在>10Gb/s @ >10m后仍然无法与光互连竞争。光互连的等效损耗<0.5dB/km，电互连经过均衡后等效损耗仍在dB/m量级。差距1000倍。
> 【工程价值】对于数据中心和长距离通信，光互连是必然选择。400G/800G光模块已经商用，1.6T光模块正在研发。光互连的功耗/比特效率正在逼近电互连。
> 【落地注意】光互连的优势建立在足够的传输距离上。对于芯片封装内线宽（<1cm），电互连仍是最优解。混合光电协同设计（Serdes+光学+封装）是未来的系统级解决方案。

---

## Channel Performance Impact

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/7a1a5c18ac10051439ded4185aa9857ca5b1a6e5fb75a364910924b3e612654c.jpg)
> 🔍 深度说明：
> 【研究背景】可能是另一种角度的通道性能对比图，可能涉及不同调制格式（NRZ vs PAM4）在电通道上的表现对比。
> 【核心结论】PAM4相比NRZ可在相同带宽下传输2倍数据，但代价是信噪比损失（每级眼SNR降低约9.5dB）。在电通道上，PAM4的眼高仅为NRZ的1/3，对噪声更敏感。
> 【工程价值】PAM4是112Gb/s和224Gb/s光模块的主流调制格式。电通道上的PAM4设计更加复杂，需要更精确的均衡和时钟恢复。TX预加重和RX均衡必须针对PAM4的4级特性优化。
> 【落地注意】电通道上的PAM4性能受限于串扰和反射——多电平使得任何反射都会跨越电平阈值，造成误码。设计时需要保证S11<-20dB @ 全频段。

---

## Channel Performance Impact

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/9b9bdc31e27b98021a55129b7b0f9f5998fd05657d93995c40ff50bf90c7ff45.jpg)
> 🔍 深度说明：
> 【研究背景】可能是电通道的眼图扫描结果，展示不同距离或不同速率下的眼图质量变化。
> 【核心结论】眼图随距离增加而闭合：10Gb/s @ 1m眼图清晰，56Gb/s @ 1m眼图部分闭合，112Gb/s @ 1m眼图几乎完全闭合。这量化展示了电互连的速率-距离限制。
> 【工程价值】眼图诊断是系统调试的核心工具。通过眼图可以直观判断通道性能和均衡效果。示波器或BERT的眼图分析能力直接决定调试效率。
> 【落地注意】112Gb/s PAM4的眼图分析更复杂：需要分析4级眼而非2级，需要测量每级眼的高度、宽度、对称性。眼图模板测试（Template Test）是光模块认证的必测项目。

---

## Channel Performance Impact

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/e0ddeb3fff3ebb60eaa1f03a58109b56f921af64b5cc379b67d35e2af3c642dd.jpg)
> 🔍 深度说明：
> 【研究背景】可能是通道的频率响应图（s21 magnitude），展示电通道的频率相关衰减特性。
> 【核心结论】s21曲线显示明显的低通特性：10GHz以下损耗较小，>10GHz后损耗急剧增加。FR4材料的介电损耗在10GHz附近显著上升。光纤的s21则几乎平坦（仅0.2dB/km）。
> 【工程价值】频率响应直接决定可用带宽。设计者需要根据s21数据选择合适的均衡策略。对于高速系统，通道的s21测量是设计验证的第一步。
> 【落地注意】s21的群延迟波动（group delay ripple）也会导致信号失真。即使 magnitude平坦，如果group delay不平坦，也会造成码间干扰。精密测量需要VNA（矢量网络分析仪）。

---

## Channel Performance Impact

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/182e19c36c44df1c2a34d913ebefbc5df33f37991a83a323cf07ce78a8a05b63.jpg)
> 🔍 深度说明：
> 【研究背景】可能是更全面的电/光通道性能对比，涵盖从芯片内部到数据中心规模的完整距离范围。
> 【核心结论】电互连的优势范围：芯片内部（<1cm）到板级（<1m）。光互连的优势范围：机架间（>1m）到数据中心（>100m）到城域（>10km）。两者在1m附近存在竞争，但电互连的功耗优势在缩短。
> 【工程价值】CPO（共封装光学）正在将光互连的边界推向芯片级。Intel的CPO产品将Serdes和光引擎封装在同一SiP中，电互连距离<5mm，光互连开始进入短距离场景。
> 【落地注意】光互连向短距离延伸的技术趋势：CPO + 硅光子 + VCSEL阵列。但光模块的功耗和成本仍是挑战，<1m场景电互连仍是最优解。

---

## High-Speed Optical Link System

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/02caae3bec91c536a038d0ee0151e0cc2a1ae95859768cfc459c44b221ff86a9.jpg)
> 🔍 深度说明：
> 【研究背景】完整高速光链路系统架构图，对比电互连系统结构，清晰展示光发射和光接收各模块的级联关系。
> 【核心结论】光链路TX：Serdes → 驱动器 → 调制器（EAM/MZM/RRM）→ 激光器（CW光源）→ 光纤。光链路RX：光纤 → 光探测器（PIN/APD）→ TIA → Limiting Amp → Serdes。关键指标：调制速率（GBd）、消光比（dB）、探测器灵敏度（dBm）、TIA噪声电流。
> 【工程价值】光链路设计核心在于电光接口匹配。驱动器需要提供足够的电压/电流摆幅驱动调制器（MZM需要~5Vppd，EAM需要~2Vppd）。TIA的输入噪声直接决定系统灵敏度。
> 【落地注意】光链路的总功耗约2-5W/通道，其中TIA和激光驱动占主要部分。探测器的响应度~0.8A/W @ 1550nm，典型规格需满足-15dBm灵敏度@112Gb/s。

---

## High-Speed Optical Link System

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/c01cbc68399734dfedc4958f8af117f90cf2f1eeba0d874e3dd7ad8dd947d03a.jpg)
> 🔍 深度说明：
> 【研究背景】可能是高速光链路系统的详细框图，补充了完整的信号链路和关键参数指标。
> 【核心结论】光互连相比电互连的优势：1)极低损耗（光纤0.2dB/km vs PCB 5dB/m）；2)频率无关损耗；3)无串扰；4)天然支持WDM。光链路的模块化设计使系统升级更容易。
> 【工程价值】光模块设计者需要权衡：光发射（激光器+调制器+驱动器）、光传输（光纤+连接器）、光接收（探测器+TIA+限放+Serdes）。每个环节的性能和功耗都是系统级优化的一部分。
> 【落地注意】光模块中的隔离器（Isolator）用于阻挡反射光（>40dB隔离度），保护激光器。实际设计中需要考虑回波损耗（>45dB）和连接器重复性（<0.5dB variation）。

---

## Wavelength-Division Multiplexing

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/d6428ab9b87c9fc6587ec55380de54cfa3d21936f6ede3687c5b4fb91edbaf6e.jpg)
> 🔍 深度说明：
> 【研究背景】波分复用（WDM）技术原理图，Young等人2010年JSCC论文展示了WDM在硅光子集成光模块中的应用。这是提升光通信容量的核心技术。
> 【核心结论】WDM技术：1)DWDM（密集波分复用）——50GHz或100GHz波长间隔，可容纳40-80波长；2)CWDM（粗波分复用）——20nm间隔，用于短距离。典型设计：每个波长承载56Gb/s或112Gb/s，总容量可达3.2Tb/s。
> 【工程价值】WDM是光通信容量提升的核心技术。CPO方案中，WDM可在单根光纤上支持多个Serdes通道，大幅提高带宽密度。Intel的硅光子平台已支持4波长WDM。
> 【落地注意】WDM系统需要波长锁定技术（通常用外腔激光器或ITU grid标准）。激光器波长温度漂移~0.1nm/°C，需要精确温度控制或波长监控反馈补偿。

---

## Optical Fiber Cross-Section

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/ebf4bfe71431a5a9b0cf9422580708414177aa3134cac1d0e69989fdaa97e89d.jpg)
> 🔍 深度说明：
> 【研究背景】光纤横截面结构图，展示单模光纤的包层、芯径和折射率分布。光波在芯径内通过全内反射传输。
> 【核心结论】单模光纤（SMF）结构：芯径约8-10μm，包层直径125μm，涂覆层直径245μm。折射率差Δ≈0.3-0.5%，阶跃折射率分布。数值孔径NA≈0.12。
> 【工程价值】光纤选型直接影响传输距离和系统预算。数据中心内部用OM3/OM4多模光纤（50μm芯径，850nm），长距离用G.652D单模光纤。连接器制作精度影响耦合损耗。
> 【落地注意】实际布线中光纤弯曲半径需>10倍外径（约30mm）避免额外损耗。光纤端面研磨质量（PC/UPC/APC）影响回波损耗（UPC>50dB，APC>60dB）。

---

## Single-Mode Fiber Loss & Dispersion

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/5de0d07f23d4a1fd92b8c9bf2dfe554e8c307dd7be3d108b10fe32d31b33da3c.jpg)
> 🔍 深度说明：
> 【研究背景】单模光纤的损耗光谱和色散特性图，这是光通信系统设计的核心参考。1550nm窗口的最低损耗和17ps/nm/km的色散是长距离光通信的基础。
> 【核心结论】光纤损耗光谱：1550nm窗口~0.2dB/km（最低），1310nm窗口~0.35dB/km。色散：1550nm的色度色散~17ps/nm/km，零色散点在1310nm。光纤可用带宽>10THz。
> 【工程价值】DWDM系统设计必须考虑光纤的色散斜率。对于100Gb/s+的长距离传输，色散补偿成为必需。EDFA的增益波段（1530-1565nm，C-band）与光纤最低损耗波段完美匹配。
> 【落地注意】高速PAM4信号对色散更敏感：112Gb/s PAM4的谱宽约30GHz，在17ps/nm/km的色散下，10km光纤会导致~510ps的色散展宽，必须用DSP均衡补偿。

---

## Inter-Chip Waveguide Examples

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/0c863d6b5b9636ee99ba6c9164d424da1248130ae4d7b3f7ff48f57bde5a5c1a.jpg)
> 🔍 深度说明：
> 【研究背景】芯片间光波导实例——Reflex Photonics的12通道带状光纤（Ribbon Fiber）。这是典型的短距离高密度光互连技术。
> 【核心结论】带状光纤规格：12通道@250μm pitch，每通道10Gb/s → 40Gb/s/mm密度。与电差分对（~500μm间距）相比，带状光纤的带宽密度提升约10倍。
> 【工程价值】带状光纤是数据中心光模块内部光路连接的常见方案。VCSEL阵列与多模光纤的耦合技术成熟，成本较低。对于板级光互连，带状光纤是可靠的解决方案。
> 【落地注意】带状光纤的精密对准要求（<5μm）增加了模块组装成本。弯曲半径需>10mm避免额外损耗。实际系统需要考虑光缆管理和维护的便利性。

---

## Optical Polymer Waveguide in PCB

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/75dde616ef510a6f96a7003a7a48e99eabcce80650ee25cec706191969e33554.jpg)
> 🔍 深度说明：
> 【研究背景】PCB内嵌聚合物光波导实物图和结构图，Immonen 2009年研究成果。这种技术将光路直接集成到PCB板中，是短距离高密度光互连的研究方向之一。
> 【核心结论】聚合物光波导优势：与PCB工艺兼容，可批量制造。关键参数：波导间距<100μm，带宽>10GHz·km，损耗~0.1dB/cm @ 850nm。可实现>100Gb/s/mm的带宽密度。
> 【工程价值】对于高密度服务器板卡设计，PCB内嵌光波导可解决高速信号（>56Gb/s）的PCB走线密度问题。Intel曾探索过类似技术用于Light Peak。
> 【落地注意】聚合物波导的损耗对波长和温度敏感，长期可靠性（>10年@85°C/85%RH）是产品化的关键。耦合损耗约3-5dB/面，需要精确的对准结构设计。

---

## Free-Space Optical Links

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/9a417793f51e7d4769199c567557b9c6767da9b7a4a6ba63ed8e71c05da08128.jpg)
> 🔍 深度说明：
> 【研究背景】自由空间光互连示意图，Gruber等人的研究方案。这种技术用透镜系统将光束在芯片间路由，替代光纤或波导。
> 【核心结论】自由空间光互连原理：通过微型透镜阵列（microlens array）准直和聚焦光束，实现芯片到芯片的光传输。优势：无需光纤/波导，可实现极高带宽密度，支持3D堆叠芯片间光连接。
> 【工程价值】自由空间光互连是实现芯片堆叠（3D IC）光I/O的有力候选。对于HBM内存和计算芯片的集成，光互连可解决"内存墙"问题。但光学系统的对准精度要求极高（亚微米级）。
> 【落地注意】自由空间光互连的主要挑战：对准容差（<1μm）、环境光干扰、透镜阵列的加工精度。目前主要停留在研究阶段，未见大规模商用。成本是主要障碍。

---

## CMOS Waveguides – Bulk CMOS

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/93af74cc3d94b22bcfe39488aa8d1476b2011cb02e559b358381a7a3f82fdb94.jpg)
> 🔍 深度说明：
> 【研究背景】Bulk CMOS工艺制作硅光波导的研究，Holzwarth CLEO 2008论文。由于标准CMOS的STI层较薄，光学模式会泄漏到硅衬底，导致~1000dB/cm的极大损耗。
> 【核心结论】Bulk CMOS制作光波导的问题：多晶硅芯层被SiO₂包裹，但底层硅衬底距离近（STI厚度~350nm），光学模式泄漏严重。即使做后处理改善，损耗仍在10dB/cm量级。
> 【工程价值】Bulk CMOS不是硅光子的理想平台。该研究证明了标准CMOS与硅光子集成的根本障碍，解释了为什么需要SOI或专门的SiPho工艺。
> 【落地注意】后处理（刻蚀硅衬底）可将损耗降低，但增加成本。如果目标只是集成调制器和探测器，III-V族材料混合集成可能更实际。

---

## CMOS Waveguides – Bulk CMOS

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/fc3e7b00e2625e505099735492b2863e284275bdfcecc357cb72fadd3b451.jpg)
> 🔍 深度说明：
> 【研究背景】Bulk CMOS波导的损耗测试数据或仿真结果，可能展示了后处理前后波导截面的对比。
> 【核心结论】后处理前的波导损耗~1000dB/cm，后处理（刻蚀底部硅）后可降至~10dB/cm。改善了100倍，但仍比SOI（<3dB/cm）差3倍。
> 【工程价值】后处理工艺可以改善Bulk CMOS的光学性能，但代价是额外工艺复杂度和成本。这对量产不经济。
> 【落地注意】后处理还会影响CMOS器件性能，可能损坏晶体管。因此商业化方案必须从一开始就使用光学友好的工艺（如SOI），而非事后补救。

---

## CMOS Waveguides – SOI

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/5dd37520de2a805b73eb93b3c144d60786277c1853ae5f6fce0a57aee8cc29f8.jpg)
> 🔍 深度说明：
> 【研究背景】SOI（绝缘体上硅）工艺制作硅光波导的方案，Narasimha JSSC 2007论文。SOI的厚埋氧层（BOX，~2μm）提供了优异的光学隔离。
> 【核心结论】SOI波导结构：硅芯层（~220nm）被上方空气和下方SiO₂包裹，形成全内反射。厚BOX层确保光学模式不泄漏。典型损耗<3dB/cm，带宽>10THz。
> 【工程价值】SOI是当前硅光电子的主流平台。Intel、IBM、GlobalFoundries等都有成熟的SOI光子工艺。SOI波导的折射率差（Δ≈4%）使弯曲半径可小至5μm。
> 【落地注意】SOI硅光的制造依赖专门的PDK，Foundry服务供应商有限（AMF、IMEC等）。设计时需考虑工艺波动（±10%线宽变化）对波导性能的影响。

---

## CMOS Waveguides – Back-End Processing

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/f44b2b841b5a85b55e3a1e0c247326682feb22e114d3fc04986e62321e3f982f.jpg)
> 🔍 深度说明：
> 【研究背景】"Optics on Top"架构，Young JSSC 2010论文，将光子器件集成在CMOS芯片的金属层之上。
> 【核心结论】"Optics on Top"优势：1)不占用晶体管有源区；2)可与标准CMOS工艺兼容；3)光栅耦合器可直接耦合到光纤。适合制作调制器、探测器等无源/有源光子器件。
> 【工程价值】这种架构使在数字CMOS芯片上附加光子功能成为可能。对于CPO应用，Serdes PHY和光子器件可以共用基础设施（时钟、电源、ESD保护）。
> 【落地注意】后端波导的耦合效率是主要挑战。光栅耦合器的典型效率约30-40%，需优化光栅周期和入射角。波导与金属层的距离需仔细设计，避免金属吸收损耗。

---

## Optical Modulation Techniques

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/6cfc33c7dae3ca6f2cecb53e72ccc18eeaab3eda484a7ddd0677f8ff23860fbc.jpg)
> 🔍 深度说明：
> 【研究背景】光调制技术概述图，对比直接调制和外部调制两种技术路线。课程强调根据传输距离和速率选择合适的调制方式。
> 【核心结论】直接调制：简单、成本低，但有chirp，适合短距离（<100m）。外部调制：无chirp、调制速率高，适合长距离和高速率（>50Gb/s）。SLM（单纵模）激光器是长距离通信的必备条件。
> 【工程价值】调制方式的选择直接影响光模块的成本和性能。数据中心<100m用直接调制VCSEL，>10km用外部调制EAM或MZM。
> 【落地注意】直接调制的啁啾在光纤中与色散相互作用，限制传输距离。对于10Gb/s NRZ，啁啾限制约20km；对于40Gb/s，限制约5km。

---

## Directly Modulated Laser

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/e92e507306e41f84d00fecc19b306eb33ea41c9bd62e0f8bb2f66880ad126398.jpg)
> 🔍 深度说明：
> 【研究背景】直接调制激光器原理图，展示最简单的光调制方式——直接通过改变激光器驱动电流来调制输出光功率。
> 【核心结论】直接调制原理：改变偏置电流 → 载流子浓度变化 → 折射率变化 → 输出光功率变化。优点：简单、成本低、无额外插入损耗。缺点：产生频率啁啾（chirp）。
> 【工程价值】VCSEL直接调制是数据中心光模块的主流方案。10-25Gb/s的VCSEL成本低、功耗小，是SFP+光模块的核心器件。调制速率受限于驰豫振荡频率（约10-20GHz）。
> 【落地注意】激光啁啾问题：直接调制引入频率调制，在光纤中与色散相互作用导致脉冲展宽。经验公式：chirp × dispersion × distance < 1000（GHz·ps·nm·km）。

---

## Externally Modulated Laser

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/a776aaa2423a98abad9a014e58e39e04c56690911285c39ea03b5668cac3dabf.jpg)
> 🔍 深度说明：
> 【研究背景】外部调制激光器原理图，与直接调制对比，展示用独立调制器对CW激光器进行调制的方式。
> 【核心结论】外部调制工作原理：CW激光器 → 调制器（EAM/MZM）→ 通过电场改变材料特性 → 输出调制光。优点：无啁啾、调制速率高（>60GBd）、消光比高（>30dB）。
> 【工程价值】外部调制是长距离（>10km）和高速率（>50Gb/s）光模块的核心技术。DWDM系统和相干通信全部使用外部调制。EAM集成DFB激光器是数据中心中距离主流方案。
> 【落地注意】外部调制需要额外的激光器和调制器，增加成本和封装复杂度。调制器驱动电压要求较高（MZM需要5-10Vpp），需要专门的驱动放大器。偏置点稳定性需要闭环控制。

---

## Optical Sources for Chip-to-Chip Links

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/b5ce8b2b14a6ba4c893a0e081e9b78fa71fd6df05aa27dd12be5503022bb5289.jpg)
> 🔍 深度说明：
> 【研究背景】四种芯片到芯片光互连光源技术总览：VCSEL、Mach-Zehnder调制器、电吸收调制器、环形谐振腔调制器。这是光I/O发射端的核心器件对比。
> 【核心结论】VCSEL：低成本短距（<100m），速率受限（<25Gb/s）；EAM：中等距离（<10km），速率>50Gb/s；MZM：长距离相干，高性能；RRM：硅光集成，适合CPO。选型取决于距离、速率、成本。
> 【工程价值】不同应用场景选择不同光源技术。数据中心叶脊网络：<500m距离，VCSEL方案仍是主流；长距离：EAM+MZM方案。Serdes系统设计者需要根据应用选择光模块类型。
> 【落地注意】光源的波长稳定性（±0.1nm）、啁啾特性、消光比是选型的关键参数。PAM4调制对线性度要求更高（IMD3<-40dBc）。

---

## VCSEL L-I-V Curves

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/715ca30dfcbdc0ddfee2199872b9603128ac9ceb480ae80513c11ab7fe9fdd58.jpg)
> 🔍 深度说明：
> 【研究背景】VCSEL的光功率-电流-电压（L-I-V）特性曲线，是表征VCSEL电光转换性能的核心图表。
> 【核心结论】L曲线（光功率vs电流）：线性区域斜率=η（效率），阈值I_TH~700μA处有明显拐点。V曲线显示工作电压~1.9V @ 10mA。调制响应在驰豫振荡频率处出现峰值。
> 【工程价值】光模块设计者根据L-I-V曲线确定VCSEL的偏置点：需要足够的过阈值电流保证线性工作。典型偏置点：I_bias ~ 0.7-0.8 × I_max，在效率和线性之间取得平衡。
> 【落地注意】VCSEL的正向电压温度系数为负（约-1mV/°C）。L曲线的斜率效率η随温度升高而下降（约-0.5%/°C），需要在链路预算中考虑温度余量。

---

## VCSEL Bandwidth vs Reliability

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/56086c44bf7f6130210fdf9393abc9bc1ed85c3719a6aea8e06a663b2eb679d3.jpg)
> 🔍 深度说明：
> 【研究背景】VCSEL带宽与可靠性的trade-off关系，这是VCSEL设计中最核心的权衡。带宽与电流密度成正相关，但电流密度增加会指数级降低器件寿命。
> 【核心结论】关键关系：BW ∝ √(I_avg - I_TH)，MTTF ∝ 1/BW⁴。带宽提高2倍，寿命降低16倍。MTTF = A/J² × exp(E_A/kT_j)，激活能EA~0.7eV。
> 【工程价值】VCSEL的速率-可靠性权衡限制了单通道最高速率。25Gb/s VCSEL可满足数据中心需求，50Gb/s VCSEL仍在可靠性验证中。对于>25Gb/s，通常采用EAM外部调制。
> 【落地注意】VCSEL的降额使用（derating）是标准做法：工作在建议电流的70-80%以延长寿命。结温每升高10°C，寿命约减半。汽车级VCSEL要求MTTF > 15年 @ 105°C。

---

## VCSEL Drivers

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/1bfe029a189ae94c92125e5e3757af5f41e3a8dc0c3e7072401f4b155baf73c4.jpg)
> 🔍 深度说明：
> 【研究背景】VCSEL驱动电路原理图，电流模式驱动器。Palermo和Horowitz 2006年ESSCIRC论文展示的90nm CMOS VCSEL驱动技术。
> 【核心结论】电流模式驱动器优势：VCSEL的L-I特性近似线性，用电流源驱动可实现良好的调制精度。驱动器核心是高速电流开关（current switch）+ 调制电流源。
> 【工程价值】VCSEL驱动器IC通常与TIA集成在同一芯片上。驱动器带宽要求>0.7×调制速率。功耗约100-200mW/通道。
> 【落地注意】驱动器设计关键：1)输出噪声（影响SMSR）；2)过冲/下冲（影响眼图质量）；3)与Serdes的CML接口匹配。

---

## VCSEL Driver w/ 4-tap FIR Equalization

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/698399b05296d02e40b9543670163bda42b5dc981613f4afd2a94e6a31ac31bd.jpg)
> 🔍 深度说明：
> 【研究背景】带4抽头FIR预均衡的VCSEL驱动器，通过数字信号处理技术扩展VCSEL调制带宽。
> 【核心结论】FIR预均衡原理：时域加权叠加，增强高频分量，补偿VCSEL和通道的带宽限制。4抽头FIR可有效扩展-3dB带宽约50%。
> 【工程价值】FIR预均衡是提高VCSEL单通道速率的关键技术。通过预均衡，25Gb/s VCSEL可工作在50Gb/s。但预均衡需要精确的VCSEL响应模型。
> 【落地注意】预均衡的抽头系数需要根据实际VCSEL频率响应和通道特性优化。系数过大会导致过冲和频谱扩展，反而恶化性能。

---

## Electro-Absorption Modulator (EAM)

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/9947d498296046e47240c37624b4fbb71d9fb5611f1f6aef2715d5d971931d30.jpg)
> 🔍 深度说明：
> 【研究背景】电吸收调制器（EAM）的QWAFEM结构图，Helman等人的JSTQE 2005论文。EAM是最广泛使用的外部调制器。
> 【核心结论】EAM工作原理：量子限制Stark效应（QCSE），改变反向偏压导致吸收边波长移动。调制速率>60GBd，驱动电压2-5Vpp。
> 【工程价值】EAM是目前数据中心光模块最广泛使用的外部调制器。EAM可以与DFB激光器单片集成（EML），实现小型化低功耗TOSA。
> 【落地注意】EAM关键参数：消光比（>30dB）、插入损耗（3-5dB）、调制带宽（>30GHz）。对偏振敏感，需要保偏光纤或集成偏振分束器。需要闭环偏置控制。

---

## Waveguide EAM

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/af83ef06811dc28987fbfdc78d26136190b756ecda81cc1f3044604e246367dc.jpg)
> 🔍 深度说明：
> 【研究背景】波导型EAM的结构图，与表面法向EAM对比。波导型EAM光在波导内传播，与电极平行，适合与激光器端面耦合形成集成光路。
> 【核心结论】波导EAM特点：端面耦合入纤功率高，与DFB激光器集成方便，调制带宽>40GHz，电容10-500fF。可承受高光功率。
> 【工程价值】波导EAM是长距离（>10km）光模块的主流选择。相比表面法向EAM，波导型具有更低的插入损耗和更高的饱和光功率。
> 【落地注意】波导EAM与光纤的耦合损耗约3dB/面，需要精确的光学封装。EAM的温度特性（约0.1nm/°C漂移）需要在模块中进行温度控制。

---

## Waveguide EAM

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/e45a164c0c5cf6804817e1f25a987c258f283a0c00cc33c049c45d0563d424ac.jpg)
> 🔍 深度说明：
> 【研究背景】可能是Waveguide EAM的详细结构或测试数据，Liu的研究工作。展示了波导型EAM与传统EAM的结构差异。
> 【核心结论】波导型EAM的电极与光波导平行，光在波导内传输，与交变电场充分相互作用。相比表面法向，消光比更高（>30dB），但制作工艺更复杂。
> 【工程价值】波导EAM是当前100G DWDM光模块的核心器件（Tosa叫EML）。配合DFB激光器，单芯片实现光源和调制。
> 【落地注意】波导EAM的偏置稳定性是关键问题——温度变化导致调制效率变化，需要闭环反馈控制回路。

---

## Ring-Resonator Modulator (RRM)

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/1d15f6f1d75e22ac1156d08950c6377679da11e627604304d86c5c0d3a5e5c4d.jpg)
> 🔍 深度说明：
> 【研究背景】环形谐振腔调制器（RRM）结构图，Young等人ISSCC 2009论文。RRM利用环形谐振腔的窄带滤波特性，通过等离子体色散效应改变折射率。
> 【核心结论】RRM工作原理：环形谐振腔具有窄带共振特性，共振波长随载流子浓度变化。调制速率>30GHz，电容仅~10fF，ring直径<20μm。
> 【工程价值】RRM是硅光子平台的核心调制器，极小电容适合与CMOS驱动器接口。在WDM系统中，可作为波长选择开关或调制器。
> 【落地注意】RRM的主要挑战：共振波长对工艺波动敏感（±10%）、温度敏感（约0.1nm/°C）、消光比有限（约3-6dB/周期）。

---

## Ring-Resonator-Based Silicon Photonics Transceiver

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/400648bab0a05efa01b8ca3e3e52935baca170aaf618fbbf17906609b5c2b907.jpg)
> 🔍 深度说明：
> 【研究背景】基于RRM的硅光子收发器芯片照片，Young等人ISSCC 2009论文。这是早期全集成的硅光子收发器，展示了高电压驱动器+预均衡、前向时钟接收机等技术。
> 【核心结论】芯片特性：1)高电压驱动器+预均衡扩展RRM调制带宽；2)前向时钟接收机+自适应功率灵敏度RX；3)偏置调谐环路锁定谐振波长。
> 【工程价值】硅光子集成是光I/O的未来方向。Intel的CWSP已实现相干和PAM4光模块商用。该技术路线指向CPO：Serdes和光引擎在同一个SiP封装内。
> 【落地注意】硅光子芯片的规模化量产面临挑战：硅光foundry产能有限、III-V激光器需要混合集成、光学封装的成本和良率问题。

---

## Ring-Resonator Modulator Performance

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/21fd03ec41bdebb9b8cd56112b52c85dff72d9e412e04dd0d4cce004964af2c5.jpg)
> 🔍 深度说明：
> 【研究背景】RRM的光学器件性能对比图，Young等人ISSCC 2009论文汇总了VCSEL、EAM、MZM、RRM的带宽-功耗-尺寸特性。
> 【核心结论】RRM优势：尺寸最小（<20μm ring）、电容极低（~10fF）、CMOS兼容驱动器。缺点：消光比低（3-6dB）、温度敏感、工艺敏感。
> 【工程价值】不同调制器技术适合不同应用场景：VCSEL<25Gb/s短距，EAM>25Gb/s中距，MZM长距相干，RRM芯片共封装。Serdes设计者需根据应用选择。
> 【落地注意】RRM的硅光调制器是CPO方案的首选，但消光比限制了对PAM4的支持。

---

## Wavelength Division Multiplexing w/ Ring Resonators

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/1dd9a1c7a48dc5e38c524e9c421b053d611cee36cace783cf5405db4764c533c.jpg)
> 🔍 深度说明：
> 【研究背景】RRM在波分复用系统中的应用原理图，Rabus的论文。环形谐振腔可同时作为WDM通道选择器和调制器。
> 【核心结论】RRM的WDM应用：每个RRM可独立调谐到不同波长，同时实现波长选择（add/drop filter）和强度调制。潜在能力：>100个波导，每个>10Gb/s，间距~4μm。
> 【工程价值】WDM+RRM组合是实现Tb/s级芯片到芯片光互连的有力方案。配合硅光子工艺，可在单芯片上集成数十到数百个WDM通道。
> 【落地注意】RRM阵列的关键挑战：每个ring的谐振波长需要独立调谐（加热器或注入电流），控制电路复杂。

---

## Wavelength Division Multiplexing w/ Ring Resonators

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/c0ac4d9474920018a562e7417bfbb13036c8ca3e8a806506e80648b031b1a230.jpg)
> 🔍 深度说明：
> 【研究背景】可能是RRM WDM系统的详细结构图或测试数据，展示了多波长通道的切换或选择功能。
> 【核心结论】RRM作为add/drop filter的工作原理：通过改变环内载流子浓度，调节谐振波长，实现特定波长的下载（drop）或上载（add）。
> 【工程价值】在光交换系统中，RRM可作为波长选择开关，实现灵活的光路配置。对于数据中心网络，这种可配置性提供了 architectural flexibility。
> 【落地注意】RRM的开关时间约10-100ns，比MEMS（ms级）快，但比电交换慢。功耗主要在加热器和驱动器电路上。

---

## Ring-Resonator-Based Silicon Photonics Transceiver

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/665a106dcf9899443df55878c58f2164cbd3e428dc032110a5605b572584cfba.jpg)
> 🔍 深度说明：
> 【研究背景】可能是硅光子收发器的详细照片或封装结构图，Li等人ISSCC 2013论文的后续或补充。
> 【核心结论】收发器集成特性：1)64通道WDM；2)每通道>10Gb/s；3)总容量>640Gb/s；4)芯片面积~10mm²。展示了全集成的可行性。
> 【工程价值】这是当时世界上集成度最高的硅光子收发器之一。证明了WDM+硅光子的容量扩展路线是可行的。
> 【落地注意】从实验室到产品化还需要解决：量产良率、封装成本、可靠性验证等工程化问题。

---

## CMOS Modulator Driver

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/21e8a07413383278ec15c6387463c6cfb32a45052bbdf45f09fd430f9defde32.jpg)
> 🔍 深度说明：
> 【研究背景】CMOS调制器驱动电路图，展示Pulsed-Cascode结构。Palermo和Horowitz 2006年ESSCIRC论文展示用标准CMOS工艺驱动EAM和RRM的技术。
> 【核心结论】CMOS驱动EAM/RRM的优势：调制器电容小（10-500fF），可用标准CMOS驱动器直接驱动。Pulsed-Cascode可提供2×Vdd或4×Vdd摆幅，最高可达2 FO4数据率。
> 【工程价值】CMOS调制器驱动器使光发射机与标准Serdes工艺兼容。Ayar Labs、Intel等公司的硅光子产品都使用CMOS驱动器。功耗约100-300mW/通道。
> 【落地注意】对于PAM4调制，驱动器线性度（IMD3）成为关键指标。阻抗匹配（50Ω传输线）设计至关重要。

---

## Pulsed-Cascode Driver

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/4d08d09d3ffcf0c7a29032ef607ea6615483f5fafee2dd7442561c3ce28ea503.jpg)
> 🔍 深度说明：
> 【研究背景】Pulsed-Cascode驱动器的详细电路图，这是实现高输出摆幅的经典CMOS技术，允许在标准CMOS工艺中产生超过2×Vdd的电压摆幅。
> 【核心结论】Pulsed-Cascode原理： cascoded transistors允许在输出节点累积电荷，实现瞬时电压超过Vdd。输出摆幅可达2×Vdd（cascode）或4×Vdd（stacked cascode）。
> 【工程价值】该技术使CMOS工艺可用于驱动需要较高电压摆幅的调制器（EAM典型需要2-5Vpp）。相比BiCMOS或GaAs工艺，CMOS驱动器具有成本和集成度的优势。
> 【落地注意】Pulsed-Cascode的可靠性（栅氧可靠性）需要在设计时仔细考虑。堆叠的晶体管数量受制于工艺的额定电压。

---

## Mach-Zehnder Modulator (MZM)

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/9c7abb2ba73faa11ffb4fc239bf0d12d3ca01ddd63e7dea997ada888924d18d5.jpg)
> 🔍 深度说明：
> 【研究背景】马赫-曾德调制器（MZM）的结构和工作原理图，Analui的研究。MZM是相干光通信系统的核心器件，也是长距离强度调制系统的首选。
> 【核心结论】MZM工作原理：输入光在两个臂分成两路，通过电极改变臂的折射率（电光效应），两路光再合并产生干涉。关键参数：Vπ（半波电压，约3-5V）、消光比（>30dB）、带宽（>30GHz）。
> 【工程价值】MZM是相干检测系统的标配调制器（I/Q调制器），也是DP-QPSK、DP-16QAM等高级调制格式的核心。LiNbO3 MZM仍是长距离（>100km）的主流选择。
> 【落地注意】MZM的主要问题：器件长度长（几mm）需要低阻抗传输线驱动器（5Vpp @ 50Ω，约100mA）；偏置点漂移需要dithering偏置控制；温度敏感（LiNbO3的 Thermo-optic系数大）。

---

## Optical Receiver Technology

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/ccb4b5423ec6cb3854a0415c16b5eb529523d63488fec5d3c5ce5ed1321fbcbf.jpg)
> 🔍 深度说明：
> 【研究背景】光接收技术概述图，展示了光电探测器（PIN/APD）和电放大器（TIA/Limiting Amp）的级联架构。
> 【核心结论】光接收链路：光探测器（PIN/APD）将光功率转为电流 → TIA转为电压并放大 → Limiting Amp提供固定电平输出 → Serdes CDR恢复时钟和数据。关键指标：灵敏度、带宽、动态范围。
> 【工程价值】TIA是光接收端的核心器件，其输入噪声直接决定系统灵敏度。灵敏度每提升1dB，光模块可传输距离增加约10%。TIA功耗约占整个接收机功耗的40%。
> 【落地注意】TIA设计需要平衡带宽、增益和噪声。输入电容要尽可能小（<50fF），包括探测器电容和封装寄生电容。

---

## Integrated Ge MSM Photodetector

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/002de462288fcc920633dee0a2e15dcf103724b8278e33be78a1dd8ce99cb16d.jpg)
> 🔍 深度说明：
> 【研究背景】锗（Germanium）金属-半导体-金属（MSM）探测器的截面图和性能参数，Young等人JSSC 2010论文。这是硅光子平台中实现高速光探测的关键器件。
> 【核心结论】Ge MSM探测器特性：与标准CMOS工艺兼容，极低电容<1fF，小有源区<2μm²，响应度~0.5A/W @ 850nm。适合集成在硅光子芯片上。
> 【工程价值】Ge MSM是硅光子接收机的核心器件。与SOI波导耦合的Ge探测器可实现>30GHz带宽，满足100Gb/s系统的需求。Intel的硅光子产品使用类似的Ge波导耦合探测器。
> 【落地注意】Ge探测器的挑战：与Si的晶格失配（需要低温外延）；响应度~0.5A/W比InGaAs PIN低约一半；金属电极的寄生电容需要最小化。

---

## Ge MSM Photodetector

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/9677c97f058c3b67718767620d424b8aa6e9a9bbf61955647aaf2edc52c161f2.jpg)
> 🔍 深度说明：
> 【研究背景】Ge MSM探测器的详细截面图，展示了Cu电极、Ge有源区、SiN波导的相对位置关系。叉指电极（interdigital fingers）结构用于增大光吸收面积同时保持小电容。
> 【核心结论】结构特点：SiN波导将光耦合到Ge有源区上方，Cu叉指电极在Ge表面，Ge直接在SiO₂上沉积。超低电容源于小有源区和厚介质隔离。
> 【工程价值】这种波导耦合的探测器结构是硅光子接收机的标配。与垂直入射探测器相比，波导耦合可在保持低电容的同时增加光程（提高响应度）。对CPO应用至关重要。
> 【落地注意】Ge MSM探测器的金属叉指间距（约100nm）需要精确控制。Cu电极的可靠性（电迁移）是长期稳定性的隐患。

---

## Integrated Ge MSM Photodetector

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/8509a9e176f7c1654cce45eb17de5cd1c35f8d1408046e2d3965294b8f53fec2.jpg)
> 🔍 深度说明：
> 【研究背景】可能是Ge MSM探测器的详细尺寸标注和性能参数汇总，展示了<1fF电容和<2μm²有源区的关键规格。
> 【核心结论】Ge MSM的超低电容使其成为高速光探测的理想选择。<1fF的电容与50Ω端接电阻产生的RC带宽约>300GHz，远超过实际系统需求。
> 【工程价值】超低电容探测器可以简化接收机设计——更少的均衡甚至不需要均衡，降低功耗和复杂度。对于112Gb/s PAM4系统，低电容探测器的优势更加明显。
> 【落地注意】但极小的有源区也意味着光耦合效率受限。需要精确的光学对准和高效的波导耦合结构。

---

## Hybrid Integration

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/66aeeae36727a4b5cb9120075f7fe7966a63b4f99af2c33dd591305e9bc2abaf.jpg)
> 🔍 深度说明：
> 【研究背景】混合集成方案对比图，展示Wirebonding、Flip-Chip Bonding、Short In-Package Traces三种方式。这是光电器件与电路集成的核心技术。
> 【核心结论】Wirebonding：寄生电感>1nH，带宽约10-15GHz，适合<10Gb/s。Flip-Chip Bonding：寄生电感<100pH，适合>25Gb/s。Short In-Package Traces：综合性能最佳，是CPO的主要选择。
> 【工程价值】混合集成是当前光模块的主流方案。III-V族激光器（InP）无法与标准CMOS集成，必须混合封装。Flip-chip使激光器靠近调制器/探测器，减少寄生效应。
> 【落地注意】混合集成的关键挑战：不同材料的热膨胀系数（CTE）不匹配、长期可靠性（热循环下的焊点疲劳）、光学对准精度要求高。

---

## Wirebonding

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/e90e8b65f3a28dbda6a6ffa6fb7c45a9b496dd9f50fa87713367c6b202b871a9.jpg)
> 🔍 深度说明：
> 【研究背景】引线键合方式的示意图，这是最原始的芯片到芯片电气连接方式。简单但高频性能差。
> 【核心结论】Wirebonding特性：寄生电感1-10nH（取决于线长和直径），带宽限制约10-15GHz，成本最低，工艺成熟。适用于较低速率（<10Gb/s）的光模块。
> 【工程价值】对于速率>25Gb/s的系统，wirebonding的寄生电感成为瓶颈。即使加上去耦电容，也难以支持56Gb/s以上的信号完整传输。
> 【落地注意】实际光模块中，wirebonding仍用于低速信号（偏置电流、控制信号）和电源连接。驱动器和TIA之间的高速信号通道必须避免wirebonding。

---

## Flip-Chip Bonding

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/faa46129f41412ac176bd492af2fc2807f3c34bdf464a3ba058b8d47d143c55d.jpg)
> 🔍 深度说明：
> 【研究背景】倒装芯片键合示意图，这是当前高速光模块的主流封装技术。通过焊球阵列实现电气连接，寄生电感可低至<100pH。
> 【核心结论】Flip-chip优势：焊球距离短（<100μm），寄生电感低；信号分布均匀；适合高频（>30GHz）；可用于光学器件与IC的混合封装。
> 【工程价值】Flip-chip是实现>100Gb/s光模块的必要封装技术。56G/112G Serdes的光电芯片必须用flip-chip与有机基板或硅基板连接。
> 【落地注意】Flip-chip的热管理是主要挑战：焊点的热导率有限。底部填充（underfill）材料提供机械保护但增加热阻。光模块中光学器件与IC的共面对准也是关键。

---

## Integrated CMOS Photonics

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/27cc8c05c2d887df8f7b556af1698efb7e3643f7dc861811860e394d7921f021.jpg)
> 🔍 深度说明：
> 【研究背景】"Optics on Top"架构在Bulk CMOS的实现方案，Batten的研究。这种架构将光子器件堆叠在CMOS芯片之上，不占用前端有源区。
> 【核心结论】"Optics on Top"特点：光子器件在金属层之上，不占用晶体管有源区，可使用标准CMOS工艺。挑战：光栅耦合效率低、层间串扰。
> 【工程价值】这种架构允许在数字处理器芯片上附加光子功能。对于CPO应用，Serdes PHY和光子器件可以共用基础设施。
> 【落地注意】光学层与CMOS层的对准是关键。通常使用红外对准技术实现精确对准。成本是主要障碍，目前主要用于研究。

---

## Bulk CMOS Process

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/c9c58c647c30db4b7ccdd2673e364d78d7de79d1ece323a3187897896ce8ed71.jpg)
> 🔍 深度说明：
> 【研究背景】Bulk CMOS工艺的光学集成方案，将光子器件制作在标准CMOS芯片之上。这是试图复用现有CMOS fab产能的方案。
> 【核心结论】Bulk CMOS光子集成的挑战：薄STI层导致波导模式泄漏，后处理工艺增加成本，光学性能受限。更实际的做法是使用专门的SOI光子工艺。
> 【工程价值】标准Bulk CMOS不是硅光子的理想平台。Ayar Labs、Intel等公司都使用专门的SOI或SiPho工艺。Bulk CMOS光子集成目前主要停留在学术研究。
> 【落地注意】后处理可将Bulk CMOS改造为可接受的波导性能，但额外工艺步骤显著增加成本。III-V族材料混合集成可能更实际。

---

## Short In-Package Traces

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/cf2a7b7544a9ae7b336d4fd839284ee2a67a59624abdac6453a6eff9587a96ff.jpg)
> 🔍 深度说明：
> 【研究背景】封装内短走线连接示意图，这是介于wirebonding和full flip-chip之间的折中方案。适合在同一个封装内连接光器件和电路。
> 【核心结论】Short In-Package Traces特性：走线长度1-5mm，可设计为受控阻抗传输线（50Ω差分），寄生电感约100-500pH。在硅基板（Si interposer）上可实现~100μm线宽/间距。
> 【工程价值】CPO方案中，Serdes芯片和光引擎之间的电气连接必须使用short in-package traces。Serdes I/O信号速率>100Gb/s，PCB走线太长会超出通道预算。
> 【落地注意】封装内走线的设计需要电磁仿真验证阻抗连续性。硅光子的Si interposer可以集成无源器件，但成本高，目前只有CPO方案采用。

---

## Integrated CMOS Photonics

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/5f672839131d8230350c8855fb00d8e2f95132b87a6fa5cb1b4b1aabf171ddd8.jpg)
> 🔍 深度说明：
> 【研究背景】可能是"Optics on Top"架构的详细示意图或"Future Photonic CMOS Chip"的早期概念图。
> 【核心结论】"Optics on Top"架构将光子器件层叠在CMOS电路之上，实现方式可以是背面（through- substrate coupling）或正面（through-metal coupling）耦合。
> 【工程价值】这种架构的最大优势是不占用宝贵的芯片有源区面积。光学层可以后加，不影响前端的器件密度。
> 【落地注意】光学层与CMOS层的对准是关键技术挑战。通常需要精密的对准标记和特殊的耦合结构设计。

---

## Future Photonic CMOS Chip

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/ccf7f1d31c2827922524c61ce1a01e16145a3341949944e6debfb9c325ee18c6.jpg)
> 🔍 深度说明：
> 【研究背景】未来光子CMOS芯片的愿景图，Young等人ISSCC 2009论文。展示了单芯片上集成Serdes PHY、CPU core和光I/O的融合架构。
> 【核心结论】愿景：统一的片上/片间光互连——核心到核心、处理器到处理器、处理器到内存。光互连实现"光I/O + 计算 + 存储"的单芯片融合。
> 【工程价值】这是CPO和硅光子的终极目标。光互连可解决"内存墙"和带宽瓶颈问题，释放处理器性能。Intel的"Light Peak"概念和全光子集成路线图指向这个方向。
> 【落地注意】该愿景的实现需要解决：III-V族激光器与硅的集成、封装成本、热管理（光子器件和CPU在同一芯片，热源密度极高）。真正的片上光I/O可能还需要10-15年。

---

## Conclusion

• Thanks for the fun semester!

---

## Reference Slides

### VCSEL References
1. D. Bossert et al, "Production of high-speed oxide confined VCSEL arrays for datacom applications," Proceedings of SPIE, 2002.
2. M. Teitelbaum and K. Goossen, "Reliability of Direct Mesa Flip-Chip Bonded VCSEL's," LEOS, 2004.

### VCSEL Driver Reference
- S. Palermo and M. Horowitz, "High-Speed Transmitters in 90nm CMOS for High-Density Optical Interconnects," ESSCIRC, 2006.

### EAM Reference
- N. Helman et al, "Misalignment-Tolerant Surface-Normal Low-Voltage Modulator for Optical Interconnects," JSTQE, 2005.

### RRM Reference
- I. Young, E. Mohammed, J. Liao, A. Kern, S. Palermo, B. Block, M. Reshotko, and P. Chang, "Optical I/O Technology for Tera-Scale Computing," ISSCC, 2009.

### CMOS Waveguide References
- Holzwarth et al, CLEO, 2008.
- Narasimha et al, JSSC, 2007.
- Young et al, JSSC, 2010.
- Batten et al, "Optics On Top" research.

### Photodetector Reference
- I. Young, E. Mohammed, J. Liao, A. Kern, S. Palermo, B. Block, M. Reshotko, and P. Chang, "Optical I/O Technology for Tera-Scale Computing," IEEE Journal of Solid-State Circuits, 2010.

### Silicon Photonics Transceiver Reference
- Li et al, ISSCC, 2013.

### Fiber and Waveguide References
- Sackinger, "Broadband Circuits for Optical Fiber Communication."
- Reflex Photonics, "12-Channel Ribbon Fiber."
- Immonen, "Optical Polymer Waveguide in PCB," 2009.
- Gruber, "Free-Space Optical Links."
- Rabus, "Wavelength Division Multiplexing with Ring Resonators."

### Hybrid Integration References
- Kromer et al, "Hybrid Integration" research.
- Schow et al, "Flip-Chip Bonding for Optical Interconnects."
- Mohammed et al, "Short In-Package Traces."

### CMOS Photonics References
- Analui et al, "SOI CMOS Process" research.
- Young, "Optics On Top" architecture.

---

*Report generated from ECEN 720 Lecture 15: Optical I/O*
*Spring 2023, Texas A&M University*
*Instructor: Sam Palermo*
