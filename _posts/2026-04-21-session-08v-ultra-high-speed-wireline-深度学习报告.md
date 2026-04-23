---
layout: post
title:      "Session 08V ULTRA HIGH SPEED WIRELINE 深度学习报告"
date:       2026-04-21 10:53:13
author:     "Bert"
tags:
  - Fundamentals
  - Lecture
  - SerDes
  - 深度学习
---

ISSCC 2021


      SESSION 8
Ultra-High-Speed Wireline


> 🔍 深度说明：
> 【研究背景】本专题面向224G/448G Serdes前沿技术，探讨超高速有线传输的技术路径与挑战，是当前链接电路研究的核心前沿。224G系统的Nyquist频率约56GHz，相比112G的28GHz提升了1倍，高频传输的物理挑战急剧增加。
> 【核心结论】超高速传输的核心挑战：1) 插入损耗剧增——28GHz时约3~5dB/in，56GHz时可达8~12dB/in，传统PCB材料难以支撑；2) 抖动预算减半——UI从8.9ps（112G）缩小到4.5ps（224G），对时钟和CDR的噪声要求更严苛；3) 功耗墙——高速Serdes功耗已达3~5W/通道，224G预计翻倍到6~8W/通道，散热成为瓶颈；4) 封装极限——BGA封装的引脚电感在高频下等效阻抗已不容忽视，封装从BGA向HBM/SiP演进。技术路径：1) PAM4→PAM6/PAM8多电平调制；2) 先进均衡（ML均衡、概率整形）；3) CPO共封装光学；4) 新型低损耗材料。
> 【工程价值】224G Serdes已经开始在超算和数据中心试用，是下一代800G/1.6T光模块的电接口基础；理解这些挑战有助于在当前112G系统设计中预留足够的余量（通常要求30%以上）。
> 【落地注意】224G系统的板材必须使用Ultra-low loss材料（如Isola Astra MT77），走线长度要严格控制；连接器必须使用专门为224G设计的低损耗连接器（如Samtec FireFly）；目前224G系统的主要瓶颈是成本（材料+测试成本约为112G的2倍）和长期可靠性数据不足。

---

A 224Gb/s DAC-Based PAM-4 Transmitter
               with 8-Tap FFE in 10nm CMOS
                     Jihwan Kim*1, Sandipan Kundu*1, Ajay Balankutty1, Matthew Beach2, Bong Chan Kim1, Stephen Kim1,
                        Yutao Liu1, Savyassachi K. Murthy1, Priya Wali1, Kai Yu1, Hyung Seok Kim1, Chuan-Chang Liu1,
                                       Dongseok Shin1, Ariel Cohen3, Yongping Fan1, Frank O’Mahony1

                                                1Intel, Hillsboro, OR, 2Foundation Devices, Boston, MA, 3Intel, Jerusalem, Israel




© 2021 IEEE
                                                                 8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS   Page 1 of 68
International Solid-State Circuits Conference


> 🔍 深度说明：
> 【研究背景】本专题面向224G/448G Serdes前沿技术，探讨超高速有线传输的技术路径与挑战，是当前链接电路研究的核心前沿。224G系统的Nyquist频率约56GHz，相比112G的28GHz提升了1倍，高频传输的物理挑战急剧增加。
> 【核心结论】超高速传输的核心挑战：1) 插入损耗剧增——28GHz时约3~5dB/in，56GHz时可达8~12dB/in，传统PCB材料难以支撑；2) 抖动预算减半——UI从8.9ps（112G）缩小到4.5ps（224G），对时钟和CDR的噪声要求更严苛；3) 功耗墙——高速Serdes功耗已达3~5W/通道，224G预计翻倍到6~8W/通道，散热成为瓶颈；4) 封装极限——BGA封装的引脚电感在高频下等效阻抗已不容忽视，封装从BGA向HBM/SiP演进。技术路径：1) PAM4→PAM6/PAM8多电平调制；2) 先进均衡（ML均衡、概率整形）；3) CPO共封装光学；4) 新型低损耗材料。
> 【工程价值】224G Serdes已经开始在超算和数据中心试用，是下一代800G/1.6T光模块的电接口基础；理解这些挑战有助于在当前112G系统设计中预留足够的余量（通常要求30%以上）。
> 【落地注意】224G系统的板材必须使用Ultra-low loss材料（如Isola Astra MT77），走线长度要严格控制；连接器必须使用专门为224G设计的低损耗连接器（如Samtec FireFly）；目前224G系统的主要瓶颈是成本（材料+测试成本约为112G的2倍）和长期可靠性数据不足。

---

Self Introduction

                                                 B.S. degree from Hanyang University, Seoul, Korea in 2005
                                                 M.S. degree from Georgia Institute of Technology, GA, USA in 2007
                                                 Ph.D. degree from Georgia Institute of Technology, GA, USA in 2011
                                                 Have been with Advanced Design, Intel Corporation, OR, USA since 2011
                                                 My interests are in designing CMOS IC’s for high-speed IO applications




© 2021 IEEE
                                                          8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS   Page 2 of 68
International Solid-State Circuits Conference


> 🔍 深度说明：
> 【研究背景】超高速系统的信号完整性分析，高频下的传输线效应、阻抗失配、串扰等比低速率系统严重得多，是系统设计的关键制约因素。
> 【核心结论】高频SI问题：1) 插入损耗——趋肤效应使电流只在导体表面流动，等效截面积减小；介质损耗随频率线性增加；2) 反射——阻抗不连续点的反射系数与频率成正比，高频反射更严重；3) 串扰——相邻走线耦合电容和互感在高频下增强，NEXT和FEXT都增加；4) 模式转换——差分对不平衡（长度差、耦合差）导致共模转换，产生EMI和降低共模抑制；5) 趋肤效应深度——铜在28GHz时趋肤深度约0.4μm，在56GHz时仅0.28μm，导线等效厚度需超过2倍趋肤深度才能避免电阻剧增。传输线选择：微带线加工容易但EMI大，带状线EMI小但层压对齐要求高；先进封装内走线用RDL（重分布层）更合适。
> 【工程价值】在224G系统背板设计中，最大走线长度要限制在15in以内，否则即使均衡也无法补偿这么深的损耗；眼图闭合程度直接反映通道质量，眼图margin<20%的通道必须重新设计或选用更低损耗的材料。
> 【落地注意】仿真必须用3D full-wave EM工具（HFSS），2D提取在28GHz以上不再准确；差分对的skew要求<1ps，走线长度差<5mil；保护地（coplanar waveguide shielding）的间距要<2倍线宽才能有效屏蔽；板材的Dk（介电常数）和Df（损耗角正切）随频率变化，厂家给出的28GHz数据更接近真实应用。

---

Outline

             Backgrounds
             TX architecture
             Circuit implementation
                              Clock distribution
                              Data-path
                              DAC
                              Output pad

             Measurement results
             Summary
© 2021 IEEE
                                                    8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS   Page 3 of 68
International Solid-State Circuits Conference


> 🔍 深度说明：
> 【研究背景】先进均衡技术是超高速Serdes的核心使能技术，通过在TX和RX两端联合均衡来补偿通道的高频衰减。
> 【核心结论】先进均衡方案：1) 高精度ADC（10bit @ 56GSa/s）——替代8bit，动态范围提升~6dB，可以处理更大范围的输入信号和更深通道；2) 数字预加重（TX FFE）——在TX侧用DSP实现去加重，补偿通道损耗，可以减少RX侧均衡的压力；3) ML均衡——用神经网络学习通道的非线性特性（PLL相位噪声的非高斯、ADC量化噪声的分布），比传统线性均衡提升1~2dB；4) 混合判决反馈均衡（Hybrid DFE）——在判决前加入ML滤波器，补偿DFE的错误传播；5) 概率整形（Probabilistic Shaping）——调整QAM/PAM星座点的概率分布，使信道容量更接近香农极限，在长距离传输中可获得1~2dB的增益。DSP工艺从16nm向5nm演进，单位功耗性能提升约3倍，5nm下224G DSP功耗约3~4W。
> 【工程价值】ML均衡在长距离背板（>30dB @ Nyquist）中比传统均衡提升1~2dB链路余量，相当于将可传输距离延长20%；概率整形在相干检测系统中已经是标配，在直接检测（IMDD）系统中也开始应用。
> 【落地注意】ML均衡需要额外的功耗和延迟（推理时间约1~2ns），要权衡是否值得；概率整形需要链路两端都支持，需要完整的协议栈支持；混合均衡的复杂度增加约30%，功耗增加约15%，只有在对性能要求极高（>30dB通道）的场景才值得。

---

Wireline Data-Rate Trend




                                                   Source: ISSCC Wireline Trends 2020
© 2021 IEEE
                                                     8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS   Page 4 of 68
International Solid-State Circuits Conference

![](_images/img-004.jpg)
> 🔍 深度说明：
> 【研究背景】超高速Serdes的时钟架构演进，高速率和低抖动要求推动时钟电路从模拟向数字化方向发展。
> 【核心结论】时钟架构演进路径：1) 传统模拟PLL——参考时钟的相位噪声经PLL环路过滤后输出，环路带宽受限，无法跟踪高频参考噪声，但能抑制VCO内部噪声；2) 亚采样PLL（SS-PLL）——用分频器将VCO输出分频到参考时钟频率附近工作，鉴相器工作在低频，噪声性能更好，适合低噪声应用；3) 数字PLL（DPLL）——用数字滤波器替代模拟滤波器，时间数字转换器（TDC）测量相位误差，数字控制器调整DCO/LC VCO；数字实现的 PLL在先进工艺下的一致性和可重复性更好，温度漂移更小。DPLL的关键模块：TDC（时间-数字转换器，分辨率<100fs）、数字环路滤波器、NCO（数控振荡器）。CDR架构：Bang-bang CDR在高抖动输入下有模式切换问题，导致周期性错误；高速系统倾向使用线性CDR或混合架构，在不同抖动水平下自适应调整环路参数。
> 【工程价值】DPLL的锁定时间比模拟PLL快10~100倍（<1μs vs >10μs），这对需要快速链路建立的系统非常重要，比如热插拔场景；DPLL的相噪性能已经可以媲美甚至超越模拟PLL，在5nm工艺下，DPLL的带内相位噪声可以做到<-100dBc/Hz。
> 【落地注意】DPLL的TDC是设计的瓶颈，分辨率直接决定参考环路的噪声地板；TDC功耗约占DPLL总功耗的30%~40%，要权衡分辨率和功耗；在224G Serdes中，时钟抖动要求<50fs rms，比112G的100fs严格1倍，对VCO的相位噪声要求更高（带内噪声<-110dBc/Hz @ 1MHz偏移）。

---

100+Gb/s TX Trend
                                                                 Published in ISSCC in last 3 years
              112Gb/s PAM-4                                                  106, 128Gb/s PAM-4                             112Gb/s PAM-4
              Analog FFE, DSP/8b-DAC                                         Analog FFE, DSP/7b-DAC                         Analog FFE, DSP/7b-DAC
              4:1 serialization                                              4:1, 2:1 serialization                         4:1, 2:1 serialization
              SST, CML                                                       CML                                            CML, SST, H-bridge
              1.7 ~ 2.1pJ/bit [2,3]                                          1.3 ~ 1.8pJ/bit [4,5]                          1.1 ~ 1.3pJ/bit [6,7,8]
                           Per-Lane Transfer Rate (Gb/s)




                                                           256


                                                           128


                                                           64


                                                           32
                                                                      2018     2019            2020                2021
                                                                                      Year
© 2021 IEEE
                                                                                  8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS   Page 5 of 68
International Solid-State Circuits Conference

![](_images/img-005.jpg)
> 🔍 深度说明：
> 【研究背景】超高速Serdes的功耗管理和散热设计，功耗是制约系统部署和扩展的核心因素，尤其在数据中心场景。
> 【核心结论】功耗来源分解（以112G PAM4 Serdes为例）：TX驱动器约30%~35%（~1W/通道）、ADC/DSP约25%~30%（~0.8W/通道）、时钟和CDR约15%~20%（~0.5W/通道）、I/O封装损耗约10%~15%（~0.4W/通道）、静态泄漏功耗约10%~15%（~0.3W/通道，先进工艺占比更高）。224G系统的功耗预计比112G增加约60%~80%，主要来自ADC/DSP和时钟。功耗优化技术：1) 功率门控——空闲通道关闭电源或降低时钟频率，数据中心Idle功耗可降低70%；2) 动态电压频率调节（DVFS）——根据链路长度和噪声水平动态调整，在短通道/低噪声时降低功耗；3) 模拟/数字混合均衡——低速率场景用模拟CTLE替代部分DSP，节省数字功耗；4) 先进封装（CPO）——Serdes和光引擎共封装，Serdes输出从PCB走线（10~30cm）变为封装内走线（<5mm），驱动功耗降低30%~50%，但封装的散热设计是主要挑战。散热方案：先进节点（5nm）芯片功率密度>100W/cm²，传统空冷已无法满足，需要液冷（直接接触芯片背面，热阻<0.1°C/W）或浸没式冷却。
> 【工程价值】数据中心的电费和散热成本占TCO的20%~30%，Serdes功耗降低50%意味着整体TCO降低10%~15%；对于超大规模数据中心（百万量级服务器），即使每通道节省1W，总节省的电费也非常可观。
> 【落地注意】CPO方案的散热需要光模块厂商和芯片厂商紧密协作，光模块的散热和Serdes的散热要统一设计；液冷系统的漏水检测和可靠性是部署的主要顾虑；224G系统的功耗预留30%~40%的增长余量，因为新产品功能往往会在开发过程中增加功耗。

---

100+Gb/s TX Trend
                                                                 Published in ISSCC in last 3 years
              112Gb/s PAM-4                                                  106, 128Gb/s PAM-4                             112Gb/s PAM-4
              Analog FFE, DSP/8b-DAC                                         Analog FFE, DSP/7b-DAC                         Analog FFE, DSP/7b-DAC
              4:1 serialization                                              4:1, 2:1 serialization                         4:1, 2:1 serialization
              SST, CML                                                       CML                                            CML, SST, H-bridge
              1.7 ~ 2.1pJ/bit [2,3]                                          1.3 ~ 1.8pJ/bit [4,5]                          1.1 ~ 1.3pJ/bit [6,7,8]
                                                                                                                                                                  This Work!!!
                           Per-Lane Transfer Rate (Gb/s)




                                                           256
                                                                                                      2x!!                                                 224Gb/s PAM-4
                                                           128                                                                                             DSP/7b-DAC
                                                                                                                                                           4:1 serialization
                                                           64                                                                                              CML
                                                                                                                                                           1.7pJ/bit
                                                           32
                                                                      2018     2019            2020                2021
                                                                                      Year
© 2021 IEEE
                                                                                  8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS                         Page 6 of 68
International Solid-State Circuits Conference

---

TX Architecture Consideration
                                                    Used for 112Gb/s

                                                      14G                        28G
              Clocking                             [2,3,4,6,7]                   [5,8]

                                                       4:1                        2:1
              Multiplexing                         [2,3,4,6,7]                   [5,8]

                                                   Analog FIR               DSP/DAC
              FFE                                   [2,4,6]                 [3,5,7,8]

                                                    SST      CML                   Hybrid
             Driver                                [3,7]   [2,4,5,6]                [8]

                                                  T-coil (2L+3C) Pi-coil (3L+4C)
             Output Pad
                                                     [3,4,5,7]       [2,6,8]

© 2021 IEEE
                                                                 8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS   Page 7 of 68
International Solid-State Circuits Conference

---

TX Architecture Consideration
                                                    Used for 112Gb/s                                                   Options for 224Gb/s

                                                      14G                        28G
              Clocking                             [2,3,4,6,7]                   [5,8]
                                                                                                                       14G                 28G            56G

                                                       4:1                        2:1
              Multiplexing                         [2,3,4,6,7]                   [5,8]
                                                                                                                       8:1                  4:1           2:1

                                                   Analog FIR               DSP/DAC
              FFE                                                                                                 Analog FIR               DSP/DAC
                                                    [2,4,6]                 [3,5,7,8]

                                                    SST      CML                   Hybrid
             Driver                                [3,7]   [2,4,5,6]                [8]
                                                                                                                    SST             CML        Hybrid

                                                  T-coil (2L+3C) Pi-coil (3L+4C)                                    T-coil                 Pi-coil      LC Filter
             Output Pad
                                                     [3,4,5,7]       [2,6,8]                                       (2L+3C)                (3L+4C)       (4L+5C)

© 2021 IEEE
                                                                 8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS                             Page 8 of 68
International Solid-State Circuits Conference

---

TX Architecture Consideration
                                                    Used for 112Gb/s                                                   Chosen for 224Gb/s

                                                      14G                        28G                                                                                 Jitter,
              Clocking                             [2,3,4,6,7]                   [5,8]
                                                                                                                       14G                 28G            56G        power

                                                       4:1                        2:1                                                                               BW,
              Multiplexing                         [2,3,4,6,7]                   [5,8]
                                                                                                                       8:1                  4:1           2:1
                                                                                                                                                                    power

                                                   Analog FIR               DSP/DAC                                                                       Channel
              FFE                                                                                                 Analog FIR               DSP/DAC
                                                    [2,4,6]                 [3,5,7,8]                                                                     adaptability

                                                    SST      CML                   Hybrid                                                                 Swing, linearity,
             Driver                                [3,7]   [2,4,5,6]                [8]
                                                                                                                    SST             CML        Hybrid
                                                                                                                                                          BW, power

                                                  T-coil (2L+3C) Pi-coil (3L+4C)                                    T-coil                 Pi-coil      LC filter   BW,
             Output Pad                                                                                                                                             group delay,
                                                     [3,4,5,7]       [2,6,8]                                       (2L+3C)                (3L+4C)       (4L+5C)
                                                                                                                                                                    return loss,
                                                                                                                                                                    ESD
© 2021 IEEE
                                                                 8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS                                        Page 9 of 68
International Solid-State Circuits Conference

---

Outline

             Backgrounds
             TX architecture
             Circuit implementation
                              Clock distribution
                              Data-path
                              DAC
                              Output pad

             Measurement results
             Summary
© 2021 IEEE
                                                    8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS   Page 10 of 68
International Solid-State Circuits Conference

---

224Gb/s TX Architecture
                                                                                                                      Clock Distribution
                                                    2                                          4                                                              Output Pad
                    2x                                        HF CK Path
       LC          4-UI          De-                                                                                 4           CK                                           28GHz on-chip LC PLL [1]
                                                                                                              MUX
       PLL                       MUX
                                                    2                                          4
                                                                                                                                Buff
                                                              LF CK Path
                                                                                                                                                 4
                                                                                                                                                                              Dual-path inductively-
                              QEC/DCC ctrl                                                          Sampler ctrl                                                               peaked CMOS clock




                                                                                                                                                                 ESD
                                                                                                                                       4
                                                                                                                            CK
                                                                                                                                                                               distribution for BW extension




                                                                                                                                             4 x 4-UI
       CK Cal                                                                                                             Sampler
        FSM
                                                                                                                                                                               and jitter filtering




                                                                                                                                                                 ESD
                             Data-Path                                                              Replica 8:4 &                      4
                                                                                                                                                     1.5V
                                                                                                                                                                              8-tap FFE in DSP
                                                                                                   Phase Detector
       Phase
      Rotator
                                                                                                                           /2
                                                                                                                                                                              7-bit DAC
        FSM                                                                                             8x          8x                 4
                                                Phase rotator ctrl                                      8UI         8UI                                                       2-stage CML driver w/ active
                                                                                                                                             4
                                                                                                                                                                               peaking
                                                                                                                                                                              4L-5C output pad network
      Pattern
       Gen
                                                                                                                                                                               for BW/group-delay
                                                              Therm decoder




         &                                                                                                                                                                     optimization
                                                                                     Retimer




        FFE
                                                                  3-to-7




                            64x7
                                       64:8                                                                         8:4         Ret        4:1          Drv                   64:4 data-path w/ phase
                                                        8x7                   8x11                   8x11
                                                                                                                                                                               detector for timing
      TXDIG                                                                                                                                                       7b-DAC       optimization
© 2021 IEEE
                                                                                                    8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS                             Page 11 of 68
International Solid-State Circuits Conference

---

Outline

             Backgrounds
             TX architecture
             Circuit implementation
                              Clock distribution
                              Data-path
                              DAC
                              Output pad

             Measurement results
             Summary
© 2021 IEEE
                                                    8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS   Page 12 of 68
International Solid-State Circuits Conference

---

CMOS Buffers w/ Inductive Peaking
              Inductor-less                     Shunt-series peaked                                                      Series-shunt peaked




© 2021 IEEE
                                                8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS                         Page 13 of 68
International Solid-State Circuits Conference

---

CMOS Buffers w/ Inductive Peaking
              Inductor-less                         Shunt-series peaked                                                      Series-shunt peaked




                                                    Inductor-less                                    Shunt-series                       Series-shunt

                             Jitter Amplification
                                  (Iso-fanout)                                                                                            
                              Swing & self-noise
                                 (Iso-fanout)                                                                                             
                                  Overall Power                                                                                          
                                  Inductor Area
                                    (Iso-load)                                                                                            
© 2021 IEEE
                                                    8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS                             Page 14 of 68
International Solid-State Circuits Conference

---

CMOS Buffers w/ Inductive Peaking
              Inductor-less                           Shunt-series peaked                                                       Series-shunt peaked




                                                       Inductor-less                                    Shunt-series                       Series-shunt
                                          Used in 3 early/mid stages in CK
                             Jitter Amplification
                                  (Iso-fanout)                 
                                                     distribution                                                                             
                              Swing & self-noise
                                 (Iso-fanout)                                                                                                
                                  Overall Power                                                                                             
                                  Inductor Area
                                    (Iso-load)                                                                                               
© 2021 IEEE
                                                       8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS                             Page 15 of 68
International Solid-State Circuits Conference

---

CMOS Buffers w/ Inductive Peaking
              Inductor-less                         Shunt-series peaked                                                      Series-shunt peaked




                                                    Inductor-less                                    Shunt-series                       Series-shunt
                                                                Used in the last stage where
                             Jitter Amplification
                                  (Iso-fanout)               CL is the largest and power
                                                                                     is the                                                
                                                                            highest
                              Swing & self-noise
                                 (Iso-fanout)                                                                                             
                                  Overall Power                                                                                          
                                  Inductor Area
                                    (Iso-load)                                                                                            
© 2021 IEEE
                                                    8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS                             Page 16 of 68
International Solid-State Circuits Conference

---

Clock Buffers Comparison
           Jitter amplification of CMOS clock buffers




                                                             0.55x




            Series-shunt & shunt-series  45% lower jitter amplification than inductor-less


© 2021 IEEE
                                                     8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS   Page 17 of 68
International Solid-State Circuits Conference

---

Clock Buffers Comparison
           Jitter amplification of CMOS clock buffers                                               Power of CMOS clock buffers

                                                                                                                  Inductor-less
                                                                                                                                  Shunt-series
                                                                                                                                                          0.72x
                                                                                                                                                 Series-shunt
                                                             0.55x




            Series-shunt & shunt-series  45% lower jitter amplification than inductor-less
            Series-shunt  28% less power consumption than inductor-less
© 2021 IEEE
                                                     8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS                                       Page 18 of 68
International Solid-State Circuits Conference

---

Overall Clock Distribution
                                                     S2

                                                                                              Asym. MUX
                           S1                                                       HF DCC
                                                                                                                                                   CK
                                                2                            4                                                                   Sampler
                                                    HF Quad Gen & QEC                DAC
                                                                                                               Rfb                                     TX DAC

            LC                                                                                                                         S3        4
                           2           De-                                          enb                        en
            PLL                        MUX                                                                                        4
                                                                                                                                            S4
                                                    Quad Div 2/4/8/16,               en
                                                2     LF DCC & QEC            4




        Dual-path (HF & LF) clock distribution to support multi-data-rate
        Inductive peaking technique enables higher FO distribution w/ lower jitter
        3 shunt-series and 1 series-shunt peaked buffers  Located to optimize
         jitter/power/area
© 2021 IEEE
                                                              8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS                      Page 19 of 68
International Solid-State Circuits Conference

---

Clock DeMUX and MUX
                                                DeMUX                                                                               Asymmetric MUX

                                                S1         A

            Ckin                                      LB        SW          Out1
                                                                               (HF)                                                                         SW
                                                                                                                            SW                SW   CK_out
                                                           A’                                HF_CK_in                                                       LF_CK_in
                                                     LA
                                                                                                                            SW                SW
                                                           B                                                                                                SW

                                                      SW                    Out2
                                                                                (LF)

                                                           B’

       SW=1  HF with shunt-series peaking                                                                    SW=1  HF path, SW=0  HF high-Z
       B-B’  virtual ground and shields LF                                                                   Avoids series SW in HF path
                                                                                                               Superior HF swing/jitter to conventional
© 2021 IEEE
                                                                     8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS                   Page 20 of 68
International Solid-State Circuits Conference

---

Quadrature Clock Generation & Control
                                            Shown single-ended
                                                                                                      I Clk


                                                               Cap ctrl
                                                Res ctrl
                                                               Coarse                                                        Cap ctrl
                              Cap ctrl
                               Fine
                                                                                                                            not shown                          Res ctrl
                                                                                                      Q Clk



                                                               Res ctrl              Cap ctrl
                                  Cap ctrl
                                Fine+Coarse
                                                    Cap ctrl
                                                     Fine
                                                                                     Coarse                                     Res ctrl provides extra range at low
                                                                                                                                         frequency (<24GHz)


        16-32GHz quad clock generation using controlled delay line
        Coarse/fine IQ skew control using capacitance loading modulation
        Extra range control (<24GHz) using resistive loading modulation
        Cap loading is distributed for optimal jitter amplification
© 2021 IEEE
                                                                    8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS                                Page 21 of 68
International Solid-State Circuits Conference

---

Outline

             Backgrounds
             TX architecture
             Circuit implementation
                              Clock distribution
                              Data-path
                              DAC
                              Output pad

             Measurement results
             Summary
© 2021 IEEE
                                                    8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS   Page 22 of 68
International Solid-State Circuits Conference

---

Data-Path                                                                    x33

                                                                                                          8x4                                    P4




                                                                                                                                 8x11
                                    64x7




                                                                         16x7
                                                                                                                                                                 4




                                                          32x7




                                                                                             Retimer




                                                                                                                                                       Retimer
                                                                                                                      Retimer
                                                                                       8x7




                                                                                                                                                                           Output
                                                                                                                                                                                          OutP


                                                64 : 32




                                                                                                                                                                            Stage
                                                                 32:16
                     TX DIG




                                                                                16:8




                                                                                                                                           8:4




                                                                                                                                                                     4:1
                                                                                                          3-to-7




                                                                                                   8x3




                                                                                                                   8x7
                                                                                                                                                   4             4
                      PRBS                                                                                Therm                                                                           OutN
                      Gen                                                                                Decoder                                 N
                                                          /2             /2            /2
                                                                                                                                                                           DAC
                                                                                                                                                            4          4


                                                                                                                                                  /2
                                                                                                                                                 CK4_I/Q




            TX Dig sends 64x7b data with 64UI clock (1.75GHz)


© 2021 IEEE
                                                                                       8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS                                    Page 23 of 68
International Solid-State Circuits Conference

---

Data-Path                                                                    x33

                                                                                                          8x4                                    P4




                                                                                                                                 8x11
                                    64x7




                                                                         16x7
                                                                                                                                                                 4




                                                          32x7




                                                                                             Retimer




                                                                                                                                                       Retimer
                                                                                                                      Retimer
                                                                                       8x7




                                                                                                                                                                           Output
                                                                                                                                                                                          OutP


                                                64 : 32




                                                                                                                                                                            Stage
                                                                 32:16
                     TX DIG




                                                                                16:8




                                                                                                                                           8:4




                                                                                                                                                                     4:1
                                                                                                          3-to-7




                                                                                                   8x3




                                                                                                                   8x7
                                                                                                                                                   4             4
                      PRBS                                                                                Therm                                                                           OutN
                      Gen                                                                                Decoder                                 N
                                                          /2             /2            /2
                                                                                                                                                                           DAC
                                                                                                                                                            4          4


                                                                                                                                                  /2
                                                                                                                                                 CK4_I/Q




            3b-to-7b binary-to-thermometer decoding after 16:8 serialization
            Location of this decoder  power-timing trade-off

© 2021 IEEE
                                                                                       8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS                                    Page 24 of 68
International Solid-State Circuits Conference

---

Data-Path                                                                    x33

                                                                                                          8x4                                    P4




                                                                                                                                 8x11
                                    64x7




                                                                         16x7
                                                                                                                                                                 4




                                                          32x7




                                                                                             Retimer




                                                                                                                                                       Retimer
                                                                                                                      Retimer
                                                                                       8x7




                                                                                                                                                                           Output
                                                                                                                                                                                          OutP


                                                64 : 32




                                                                                                                                                                            Stage
                                                                 32:16
                     TX DIG




                                                                                16:8




                                                                                                                                           8:4




                                                                                                                                                                     4:1
                                                                                                          3-to-7




                                                                                                   8x3




                                                                                                                   8x7
                                                                                                                                                   4             4
                      PRBS                                                                                Therm                                                                           OutN
                      Gen                                                                                Decoder                                 N
                                                          /2             /2            /2
                                                                                                                                                                           DAC
                                                                                                                                                            4          4


                                                                                                                                                  /2
                                                                                                                                                 CK4_I/Q




            8x11b data (8UI) sent to DAC (4b binary + 7b thermometer)


© 2021 IEEE
                                                                                       8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS                                    Page 25 of 68
International Solid-State Circuits Conference

---

Data-Path                                                                    x33

                                                                                                          8x4                                    P4




                                                                                                                                 8x11
                                    64x7




                                                                         16x7
                                                                                                                                                                 4




                                                          32x7




                                                                                             Retimer




                                                                                                                                                       Retimer
                                                                                                                      Retimer
                                                                                       8x7




                                                                                                                                                                           Output
                                                                                                                                                                                          OutP


                                                64 : 32




                                                                                                                                                                            Stage
                                                                 32:16
                     TX DIG




                                                                                16:8




                                                                                                                                           8:4




                                                                                                                                                                     4:1
                                                                                                          3-to-7




                                                                                                   8x3




                                                                                                                   8x7
                                                                                                                                                   4             4
                      PRBS                                                                                Therm                                                                           OutN
                      Gen                                                                                Decoder                                 N
                                                          /2             /2            /2
                                                                                                                                                                           DAC
                                                                                                                                              T1            4          4


                                                                                                                                                  /2
                                                                                                                                                 CK4_I/Q




            8x11b data (8UI) sent to DAC (4b binary + 7b thermometer)
            T1 = Tdiv + Tbuff + TMUX(ck-q) + Twire + Tsetup < 4UI (35.7ps)  Tough to meet !!!
© 2021 IEEE
                                                                                       8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS                                    Page 26 of 68
International Solid-State Circuits Conference

---

Data-Path                                                                        x33

                                                                                                          8x4                                      P4




                                                                                                                                 8x11
                                   64x7




                                                                         16x7
                                                                                                                                                                  4




                                                          32x7




                                                                                             Retimer




                                                                                                                                                        Retimer
                                                                                                                      Retimer
                                                                                       8x7




                                                                                                                                                                              Output
                                                                                                                                                                                              OutP


                                                64 : 32




                                                                                                                                                                               Stage
                                                                 32:16
                     TX DIG




                                                                                16:8




                                                                                                                                           8:4




                                                                                                                                                                      4:1
                                                                                                          3-to-7




                                                                                                   8x3




                                                                                                                   8x7
                                                                                                                                                    4             4
                      PRBS                                                                                Therm                                                                               OutN
                      Gen                                                                                Decoder                                   N
                                                          /2             /2            /2
                                                                                                                                                                                  DAC
                                                                                                                                                             4          4


                                                                                                                           8                   8
                                                                             /2
                                          4                      4                     8                    8              8
                   CK4_I/Q                                                 Quad-
                                                                          to-Octa               PI/PR
                                                                                                                                4
                                                                                                                                                             4

                                                                                                                                                   P4             4




                                                                                                                                                                       Detector
                                                                                                                                                        Retimer
                                                                                                                         CK64




                                                                                                                                                                        Logic
                                                                                                                                           8:4
                                                                                                                                                    4             4
      Optimal phase selection for                                                                                                            N
       robust timing                                                                                                                     Replica DAC slice



© 2021 IEEE
                                                                                       8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS                                        Page 27 of 68
International Solid-State Circuits Conference

---

Data-Path                                                                        x33

                                                                                                          8x4                                      P4




                                                                                                                                 8x11
                                   64x7




                                                                         16x7
                                                                                                                                                                  4




                                                          32x7




                                                                                             Retimer




                                                                                                                                                        Retimer
                                                                                                                      Retimer
                                                                                       8x7




                                                                                                                                                                              Output
                                                                                                                                                                                              OutP


                                                64 : 32




                                                                                                                                                                               Stage
                                                                 32:16
                     TX DIG




                                                                                16:8




                                                                                                                                           8:4




                                                                                                                                                                      4:1
                                                                                                          3-to-7




                                                                                                   8x3




                                                                                                                   8x7
                                                                                                                                                    4             4
                      PRBS                                                                                Therm                                                                               OutN
                      Gen                                                                                Decoder                                   N
                                                          /2             /2            /2
                                                                                                                                                                                  DAC
                                                                                                                                              T1             4          4



                                                                             /2
                                                                                                                           8                   8
                                                                                                                                                                  Timing match is important
                                          4                      4                     8                    8              8
                   CK4_I/Q                                                 Quad-
                                                                          to-Octa               PI/PR                                         T1’
                                                                                                                                4
                                                                                                                                                             4

                                                                                                                                                   P4             4




                                                                                                                                                                       Detector
                                                                                                                                                        Retimer
                                                                                                                         CK64




                                                                                                                                                                        Logic
                                                                                                                                           8:4
                                                                                                                                                    4             4
      Optimal phase selection for                                                                                                            N
       robust timing                                                                                                                     Replica DAC slice

                   T1 = T1’ = Tdiv – TPI + Tbuff + TMUX(ck-q) + Twire + Tsetup < 4UI (35.7ps)
© 2021 IEEE
                                                                                       8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS                                        Page 28 of 68
International Solid-State Circuits Conference

---

Phase Interpolator & Rotator
                                                 4     /2    8                            8                            8           8
                                       CK4_I/Q                             PI                          PR
                                                     Quad to                                                                           CK8_Octa_Phase
                                                                         0.5UI                         3UI
                                                      Octa




© 2021 IEEE
                                                          8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS                        Page 29 of 68
International Solid-State Circuits Conference

---

Phase Interpolator & Rotator
                                                 4     /2    8                            8                            8           8
                                       CK4_I/Q                             PI                          PR
                                                     Quad to                                                                           CK8_Octa_Phase
                                                                         0.5UI                         3UI
                                                      Octa




            CK8_(N)UI                                    x8
                                                                                      CK8_A_7UI
                                                                                 CK8_A_1UI
                                                                               CK8_A_0UI
           CK8_(N+1)UI
                                          Sel




         Generates 0.5UI stepped CK8
© 2021 IEEE
                                                          8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS                        Page 30 of 68
International Solid-State Circuits Conference

---

Phase Interpolator & Rotator
                                                 4     /2    8                            8                            8                  8
                                       CK4_I/Q                             PI                          PR
                                                     Quad to                                                                                  CK8_Octa_Phase
                                                                         0.5UI                         3UI
                                                      Octa
                                                                                                                             CK8_A_0UI
                                                                                                                                                         CK8_B_0UI

                                                                                                                             CK8_A_1UI

                                                         x8
                                                                                                                                                         CK8_B_1UI
            CK8_(N)UI
                                                                                                                             CK8_A_2UI
                                                                                      CK8_A_7UI                                                          CK8_B_2UI

                                                                                 CK8_A_1UI                                   CK8_A_3UI
                                                                               CK8_A_0UI                                                                 CK8_B_3UI
                                                                                                                             CK8_A_4UI
           CK8_(N+1)UI                                                                                                                                   CK8_B_4UI
                                          Sel                                                                                CK8_A_5UI
                                                                                                                                                         CK8_B_5UI

                                                                                                                             CK8_A_6UI
                                                                                                                                                         CK8_B_6UI
         Simple and power efficient                                                                                          CK8_A_7UI
                                                                                                                                                         CK8_B_7UI
         Phase selection step/range: 0.5UI/4UI
© 2021 IEEE                                                                                                                                      SEL
                                                          8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS                                     Page 31 of 68
International Solid-State Circuits Conference

---

Phase Detector
                                        Replica DAC slice
                                            P4                4




                                                                  Detector
                                                    Retimer
       CK64




                                                                   Logic
                                                                                       FSM
                                  8:4
                                                4             4

                                            N

                                        8                4
                                  CK8               CK4




© 2021 IEEE
                                                                             8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS   Page 32 of 68
International Solid-State Circuits Conference

---

Phase Detector
                                          Replica DAC slice
                                              P4              4




                                                                    Detector
                                                    Retimer
       CK64




                                                                     Logic
                                                                                          FSM
                                  8:4
                                                4             4

                                              N

                                          8              4
                                  CK8               CK4


       D3N
       D3P         Replica Retimer                                Phase Detect Slice
       D2N
       D2P
       D1N                           L              L         L        L       FF
       D1P
       D0N                      CK4_180         CK4_0 CK4_180                CK64
       D0P
                                                                                                   Lock
  CK4_0                               L             L                  L       FF
  CK4_90
  CK4_180                         CK4_0         CK4_180                      CK64
  CK4_270


© 2021 IEEE
                                                                                8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS   Page 33 of 68
International Solid-State Circuits Conference

---

Phase Detector
                                          Replica DAC slice                                                   Good phase                                  Bad phase
                                                                                                        Data                                             Data
                                              P4              4




                                                                    Detector
                                                    Retimer
       CK64




                                                                     Logic
                                                                                          FSM                                                            CK0
                                  8:4
                                                4             4                                         CK0

                                              N                                                        CK180                                             CK180

                                          8              4
                                                                                                        Lock                                             Lock
                                  CK8               CK4                                                                        Lock=1                             Lock=0


       D3N
       D3P
       D2N
                   Replica Retimer                                Phase Detect Slice                                         Ensures data transitions at hold
       D2P
       D1N
       D1P
                                     L              L         L        L       FF                                             window in retimer latch
       D0N
       D0P
                                CK4_180         CK4_0 CK4_180                CK64
                                                                                                   Lock
                                                                                                                             Count of lock = 8 for optimal phase
  CK4_0                               L             L                  L       FF
  CK4_90
  CK4_180                         CK4_0         CK4_180                      CK64
  CK4_270


© 2021 IEEE
                                                                                8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS                     Page 34 of 68
International Solid-State Circuits Conference

---

Outline

             Backgrounds
             TX architecture
             Circuit implementation
                              Clock distribution
                              Data-path
                              DAC
                              Output pad

             Measurement results
             Summary
© 2021 IEEE
                                                    8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS   Page 35 of 68
International Solid-State Circuits Conference

---

DAC: High-Level Overview

     7b DAC (4B + 3T)                                                                                                                                     To RT/Pad

     8:4 MUX and S-to-D in DAC slice
         (matched timing across DAC)                                                                                          1V
     4x slice is unit for larger array                                                                         4                  4
                                                                        8-way                8        8:4
         (clock loading/power reduction)                                 Data                         S2D 4
                                                                                                                       Ret 4           4:1           Drv

     1UI pulse based 4:1 MUX




                                                                                                                                             VSSHI
     VSSHI for 1UI pulse enhancement                                                             8                             4
     CML driver                                                                                   CK8                        CK4_I/Q




© 2021 IEEE
                                                     8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS                                     Page 36 of 68
International Solid-State Circuits Conference

---

DAC Unit Slice
          DAC Slice                                                                                                             To RT/Pad
                                                                                                                      VCC
                                                                                                       Q4
                                                                                                      Q3
                                                                                                    Q2
                                                                                                   Q1            M4        M3
              8:4 MUX                      Retimer                         Pulse Gen
   Deven                                                             VCC
                                                                                                                                     M5
                                                        D                                                              Y
   Dodd             2:1                           L
                                                                                                                                          M6
                                                                                      X             M2
                                                                                                                                          M7
                                                                                          M1

                                                                                                                4:1 MUX              Driver
                                                                             VSSHI

                    CK8                         CK4_0       CK4_90


           Dedicated CML driver  minimal output cap for high pad BW
           1UI pulse generator based 4:1 MUX w/ VSSHI
           Active peaking (M3-M4) at 4:1 MUX output (node Y) to improve BW
© 2021 IEEE
                                                                            8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS   Page 37 of 68
International Solid-State Circuits Conference

---

DAC Unit Slice
                                                            Inductive load (active peaking)
          DAC Slice                                                                                                             To RT/Pad                Node X (for Q1-Q4)
                                                                                                                      VCC                            Q1 Q2 Q3 Q4 Q1 Q2 Q3 Q4 Q1 Q2
                                                                                                       Q4
                                                                                                      Q3
                                                                                                    Q2
                                                                                                   Q1            M4        M3                        1   1   0   1   0   0   1   0   1    1
              8:4 MUX                      Retimer                         Pulse Gen
   Deven                                                             VCC
                                                                                                                                     M5
                                                        D                                                              Y
   Dodd             2:1                           L
                                                                                                                                          M6
                                                                                      X             M2                                                           Node Y
                                                                                                                                          M7
                                                                                          M1

                                                                                                                4:1 MUX              Driver          0   0   1   0   1   1   0   1   0     0
                                                                             VSSHI

                    CK8                         CK4_0       CK4_90


           Dedicated CML driver  minimal output cap for high pad BW
           1UI pulse generator based 4:1 MUX w/ VSSHI
           Active peaking (M3-M4) at 4:1 MUX output (node Y) to improve BW
© 2021 IEEE
                                                                            8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS                                   Page 38 of 68
International Solid-State Circuits Conference

---

Pulse Generator VSSHI
                                                VCC
                                                                            IMUX
                    D

                                                         X
                                                                            M2
                 CK1
                 CK2                                         M1

                                                         VSSHI



               Gm stage (4:1 MUX) performance degrades at slow corner
               VSSHI improves pulse height (at node X) for better IMUX
               Coarse tuning based on process corner
© 2021 IEEE
                                                          8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS   Page 39 of 68
International Solid-State Circuits Conference

---

Pulse Generator VSSHI
                                                                                                                                       D=0
                                                VCC
                                                                            IMUX                                    VCC VT
                                                                                                                               P
                                                                                                                                                         CK1
                                                                                                                                                         CK2
                    D                                                                             VSSHI             VSS                          VTN

                                                                                                   =0               VCC
                                                         X                                                                                   X
                                                                                                                    VSS
                                                                            M2
                 CK1
                 CK2                                         M1                                                     VCC VT
                                                                                                                                   P
                                                                                                                                                         CK1
                                                                                                  VSSHI                                      VTN+VSSHI   CK2
                                                                                                                   VSS
                                                         VSSHI                                     >0              VCC
                                                                                                                                             X
                                                                                                                               VSSHI
                                                                                                                    VSS

               Gm stage (4:1 MUX) performance degrades at slow corner
               VSSHI improves pulse height (at node X) for better IMUX
               Coarse tuning based on process corner
© 2021 IEEE
                                                          8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS                               Page 40 of 68
International Solid-State Circuits Conference

---

Pulse Generator Topology
      Falling-Rising                                                               Falling-Falling
                                        D                                                                                            CK1
      Edge                                                                         Edge
      Chosen design                                                                Alternative                   D
                                                    A          B                                                                      A     B
                                     CK1                                                                         CK2
                                     CK2                                                                                                   CK1



                             D                  1              0                                            D                    1               0

                           CK1                                                                             CK1
                           CK2                                                                             CK2
                             A                                                                              A
                             B                                                                               B


               1UI pulse can be generated with either
                 Rising and falling edges (or falling and rising edges) of I/Q clocks
                 Rising and rising edges (or falling and falling edges) of I/Q clocks
© 2021 IEEE
                                                        8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS                       Page 41 of 68
International Solid-State Circuits Conference

---

Pulse Generator RJ Filtering
                                                Chosen                                                                            Alternative
                       Falling(CK2)-Risng(CK1) edge-based                                                    Falling(CK2)-Falling(CK1) edge-based
                           CK0                                                                                    CK0
                           CK90                                                                                  CK90

                          CK180                                                                                 CK180
                          CK270                                                                                 CK270




         TX Output_P                                                                                 TX Output_P
         TX Output_N                                                                                 TX Output_N

      TX Output_Diff                                                                              TX Output_Diff



© 2021 IEEE
                                                         8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS                     Page 42 of 68
International Solid-State Circuits Conference

---

Pulse Generator RJ Filtering
                                                Chosen                                                                            Alternative
                       Falling(CK2)-Risng(CK1) edge-based                                                    Falling(CK2)-Falling(CK1) edge-based
                           CK0                                                                                    CK0
                           CK90                                                                                  CK90

                          CK180                                                                                 CK180
                          CK270                                                                                 CK270




         TX Output_P                                                                                 TX Output_P
         TX Output_N                                                                                 TX Output_N

      TX Output_Diff                                                                              TX Output_Diff                                𝜎

                                                          3dB RJ attenuation
© 2021 IEEE
                                                         8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS                     Page 43 of 68
International Solid-State Circuits Conference

---

Pulse Generator RJ Filtering
                               Jitter Impulse                 Jitter Impulse Response                                             Jitter Transfer Function
                                                                                                             Inverse
                                                    PG
                                                                                                           Z-transform
                                                   4:1
                                                   MUX
                                                   Drv




© 2021 IEEE
                                                         8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS                              Page 44 of 68
International Solid-State Circuits Conference

---

Pulse Generator RJ Filtering
                               Jitter Impulse                  Jitter Impulse Response                                             Jitter Transfer Function
                                                                                                              Inverse
                                                     PG
                                                                                                            Z-transform
                                                    4:1
                                                    MUX
                                                    Drv



                                      Alternative             Falling-Rising
                                                              Falling-Falling


                                                                                                                                                   Alternative

                                                     Chosen
                                                                                                                                     ~3dB
                                                                                                                                                    Chosen

                                                                                                                                                         Falling-Rising
                                                                                                                                                         Falling-Falling




© 2021 IEEE
                                                          8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS                                           Page 45 of 68
International Solid-State Circuits Conference

---

Outline

             Backgrounds
             TX architecture
             Circuit implementation
                              Clock distribution
                              Data-path
                              DAC
                              Output pad

             Measurement results
             Summary
© 2021 IEEE
                                                    8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS   Page 46 of 68
International Solid-State Circuits Conference

---

Output Pad Network for CML Driver
                                                        Zo                                 Driving current splits into TX/RX termination
                                                                                           Big capacitance sources : driver, Rterm,
             RT                                                           RT                ESD, C4 bump, or any circuits connected to
                                                                                            pad




© 2021 IEEE
                                                8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS               Page 47 of 68
International Solid-State Circuits Conference

---

Output Pad Network for CML Driver
                                                                        Zo                                 Driving current splits into TX/RX termination
                                                                                                           Big capacitance sources : driver, Rterm,
             RT                                                                           RT                ESD, C4 bump, or any circuits connected to
                                                                                                            pad

                                                Output pad matching network
                                                                        Zo                                 Inductors + distributed cap form multi-
                                                                                                            segment cascaded LC filter
             RT                                                                           RT               Signal BW should be extended maintaining
                                                                                                            good return loss




© 2021 IEEE
                                                                8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS               Page 48 of 68
International Solid-State Circuits Conference

---

Output Pad Network for CML Driver
                                                                             Zo                                 Driving current splits into TX/RX termination
                                                                                                                Big capacitance sources : driver, Rterm,
             RT                                                                                RT                ESD, C4 bump, or any circuits connected to
                                                                                                                 pad

                                                     Output pad matching network
                                                                             Zo                                 Inductors + distributed cap form multi-
                                                                                                                 segment cascaded LC filter
             RT                                                                                RT               Signal BW should be extended maintaining
                                                                                                                 good return loss

                              Z1                Z2      Z3   Z4     Zout Z
                                                                           o
                                                                                                                Need small Z (~Zo) change at each section
           RT                                                                                 RT                Cdrv is the biggest source for Z deviation
                                 CT             Cdrv
                                                                                                                CT (termination cap) can’t be tuned with L
                                                                                                                Can’t design ideal LC filter  Bessel-like
© 2021 IEEE
                                                                     8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS               Page 49 of 68
International Solid-State Circuits Conference

---

112Gbaud Output Pad Network
                                                                                                           Distributed ESD (CDM-150V)
                     Idrv                                                                                  4 L’s and 5 C’s
                                L1              L2    L3     L4                 Zo                         9th order Bessel-like filter (BW, group-delay,
                                                                                                            return loss optimized)
          RT                Ct            Cdrv       ESD2   ESD1      Cbump                      RT        Full 3D EM modeling of pad network and
                                                                                                            interface to package




© 2021 IEEE
                                                                   8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS                Page 50 of 68
International Solid-State Circuits Conference

---

112Gbaud Output Pad Network
                                                                                                           Distributed ESD (CDM-150V)
                     Idrv                                                                                  4 L’s and 5 C’s
                                L1              L2    L3     L4                 Zo                         9th order Bessel-like filter (BW, group-delay,
                                                                                                            return loss optimized)
          RT                Ct            Cdrv       ESD2   ESD1      Cbump                      RT        Full 3D EM modeling of pad network and
                                                                                                            interface to package

                                                                                                                                                                               Rt
   C4 bumps to                                                                                                                                                 DAC
   package                                                                                                                  GND shield
                                                                                                                                                                               L1
   interface
                                                                                                                               125um
                                                                                                                                                                               L1

                                                                                                                                                                               Rt
                                                                                                                  TX outp (C4)           L2          L2         TX outn (C4)




                                                                                                                                              ESD2
                                                                                                                       L4           L3                    L3          L4
                                                                                                                      ESD1                                           ESD1


© 2021 IEEE
                                                                   8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS                                           Page 51 of 68
International Solid-State Circuits Conference

---

112Gbaud Output Pad Network
                                                                                                                                             BW and group-delay at C4
                Simulated pad performance (Full EM model)




                                                                                                                           Amplitude (dB)
                                                112Gb/s NRZ eye diagram at C4
                                                                                                                                                 <2ps




                                                                                                                                               Return loss at PKG pin


                                        <100fs




                                                                                                                          Return Loss (dB)
                                                                                                                                                        IEEE spec scaled
                                                                                                                                                        from 56GBaud TX

© 2021 IEEE
                                                                   8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS
                                                                                                                                                        Frequency (GHz)
International Solid-State Circuits Conference                                                                                                                              Page 52 of 68

---

Outline

             Backgrounds
             TX architecture
             Circuit implementation
                              Clock distribution
                              Data-path
                              DAC
                              Output pad

             Measurement results
             Summary
© 2021 IEEE
                                                    8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS   Page 53 of 68
International Solid-State Circuits Conference

---

Measurement Setup

                                                                                                 RT           On-package TR connector
                                                   Die                   TR conn               Scope
                                                                                                              100GHz BW RT scope
                                                 PKG
                                                                                                              Measured channel loss ~4dB @56GHz
                                                           PCB




© 2021 IEEE
                                                       8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS               Page 54 of 68
International Solid-State Circuits Conference

---

Measurement Setup
                                                LC-PLL
                                                                                                          RT           On-package TR connector
                                                            Die                   TR conn               Scope
                                                                                                                       100GHz BW RT scope
                                                          PKG
                                                                                                                       Measured channel loss ~4dB @56GHz
                                                TX AFE              PCB




© 2021 IEEE
                                                                8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS               Page 55 of 68
International Solid-State Circuits Conference

---

Measurement Setup
                                                LC-PLL
                                                                                                          RT           On-package TR connector
                                                            Die                   TR conn               Scope
                                                                                                                       100GHz BW RT scope
                                                          PKG
                                                                                                                       Measured channel loss ~4dB @56GHz
                                                TX AFE              PCB


                                                                                                                           Measured PKG Insertion Loss




                                  DUT


© 2021 IEEE
                                                                8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS                   Page 56 of 68
International Solid-State Circuits Conference

---

Measurement Result
             At room temperature
             56Gbaud w/ 4MHz 1st order CDR
             LF clock distribution, TX-FFE OFF
             RJ=154fs at 56Gbaud CLK, EW=7.2ps at 112Gb/s PAM-4

               28GHz Clock Pattern                      56Gb/s NRZ (PRBS-13)                                               112Gb/s PAM-4 (QPRBS-13)




                         RJ=154fs, DJ=376fs                    RJ=165fs, DJ-ISI=158fs                                       EW=7.3/9.2/7.2ps
                                                                                                                            EH=141/165/148mV @BER=1e-4

© 2021 IEEE
                                                  8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS                           Page 57 of 68
International Solid-State Circuits Conference

---

Measurement Result
             At room temperature
             112Gbaud w/ 4MHz 1st order CDR
             HF clock distribution, TX-FFE ON
             RJ=65fs at 112Gbaud CLK, EW=2.4ps at 224Gb/s PAM-4

               56GHz Clock Pattern                      112Gb/s NRZ (PRBS-13)                                              224Gb/s PAM-4 (QPRBS-13)




                                                                    C-1/C0/C+1=-0.01/0.92/-0.07                              C-1/C0/C+1/C+2/C+3=-0.01/0.86/-0.1/-0.02/0.01




                          RJ=65fs, DJ=247fs                     RJ=90fs, DJ-ISI=183fs                                       EW=2.4/2.8/2.4ps
                                                                                                                            EH=90/110/90mV @BER=1e-4

© 2021 IEEE
                                                  8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS                                                     Page 58 of 68
International Solid-State Circuits Conference

---

Measurement Result
             Temp=100C
             112Gbaud w/ 4MHz 1st order CDR
             HF clock distribution, TX-FFE ON
             RJ=66fs at 112Gbaud CLK, EW= >1.85ps at 224Gb/s PAM-4

               56GHz Clock Pattern                      112Gb/s NRZ (PRBS-13)                                              224Gb/s PAM-4 (QPRBS-13)




                          RJ=66fs, DJ=384fs                    RJ=133fs, DJ-ISI=203fs                                       EW=2.1/2.6/2ps
                                                                                                                            EH=64/86/63mV @BER=1e-4

© 2021 IEEE
                                                  8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS                              Page 59 of 68
International Solid-State Circuits Conference

---

Measurement Result
             At room temperature
             116Gbaud w/ 4MHz 1st order CDR
             HF clock distribution, TX-FFE ON
             RJ=69fs at 116Gbaud CLK, EW= >1.8ps at 232Gb/s PAM-4                                                         W/ max frequency of LC PLL

               58GHz Clock Pattern                      116Gb/s NRZ (PRBS-13)                                              232Gb/s PAM-4 (QPRBS-13)




                          RJ=69fs, DJ=276fs                    RJ=111fs, DJ-ISI=137fs                                       EW=1.9/2.3/1.8ps
                                                                                                                            EH=75/92/75mV @BER=1e-4

© 2021 IEEE
                                                  8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS                                Page 60 of 68
International Solid-State Circuits Conference

---

28GHz Clock (HF path)                   Measurement Result
                                          QEC Coarse Control                                                QEC Fine Control
                                     Range: 3.3ps
                                     Step: <300fs

                                                                                                                                  Range: 1.6-2ps
                                                                                                                                  Step: <60fs




                               QGen Res Control (Extra Range)                                                     DCC Control

                                     Range: 7ps                                                      Range: 1.5-2.8ps
                                     Step: <700fs                                                    Step: <30fs




                          Lowest R                                Highest R
© 2021 IEEE
                                                         8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS              Page 61 of 68
International Solid-State Circuits Conference

---

Measurement Result
                  112Gbuad clock pattern RJ w/ 4MHz 1st order CDR
                  Clock distribution supply is swept




© 2021 IEEE
                                                  8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS   Page 62 of 68
International Solid-State Circuits Conference

---

TX Comparison and Power Break-down
           Reference          ISSCC '18 [2] ISSCC '18 [3] ISSCC '19 [4] ISSCC '19 [5] ISSCC '20 [6] ISSCC '20 [7] ISSCC '20 [8]                This work

       Data-rate (Gb/s)           112             112           128          106              112            112          112                     224

          Technology             10nm            14nm          14nm         16nm              7nm           7nm           7nm                    10nm

          Modulation             PAM-4          PAM-4         PAM-4         PAM-4            PAM-4         PAM-4         PAM-4                   PAM-4

            FFE taps                4              8             3            3                 4             6             7                       8

          Architecture         Analog FFE       8b DAC      Analog FFE      7b DAC        Analog FFE       7b DAC       7b DAC                  7b DAC

         Multiplexing              4:1            4:1           4:1           2:1              4:1           4:1           2:1                     4:1

          Clock source          On-chip         External     External       On-chip         On-chip        On-chip      On-chip                 On-chip

             Driver               CML             SST          CML           CML              CML            SST        H-bridge                  CML
                                                                                          1.78 (w/ PLL)*              1.56 (w/ PLL)           1.88 (w/ PLL)
     Analog power (pJ/b) 1.72 (w/o PLL) 2.05 (w/o PLL)      1.3 (w/o PLL)      -                              -
                                                                                          1.34 (w/o PLL)              1.05 (w/o PLL)          1.74 (w/o PLL)

      Digital power (pJ/b)        N/A           0.5 (FFE)       N/A            -              N/A             -        0.13 (FFE)              0.37 (FFE)
                                                                                                                                                   65
           RJ (fs_rms)            150            185**            -          197              140             -           171
                                                                                                                                       4MHz (1st order CDR) - 90GHz

         Swing (Vppd)             0.75            0.92          1.0           1.1              1.0            -            1.2                     1.0

              RLM                 0.99              -          0.99          0.95               -           0.99          0.94                    0.99
                                                                                                                                            37.5 (112Gb/s)
           SNDR (dB)               31               -             -          34.6               -            36             -
                                                                                                                                            33.3 (224Gb/s)
       Analog supply (V)            1             0.95       0.95/1.2       1.1/1.2      0.88/1.2/1.5      0.85/1.2     0.9/1.2               0.85/1/1.5

          Area (mm2)              0.03           0.095         0.048           -             0.136            -          0.193                   0.088

     * Combined clock distribution power for both TX and RX
     ** For 56Gb/s NRZ PRBS7. All other RJ numbers reported are from clock pattern.



© 2021 IEEE
                                                                                      8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS          Page 63 of 68
International Solid-State Circuits Conference

---

TX Comparison and Power Break-down
           Reference          ISSCC '18 [2] ISSCC '18 [3] ISSCC '19 [4] ISSCC '19 [5] ISSCC '20 [6] ISSCC '20 [7] ISSCC '20 [8]                This work

       Data-rate (Gb/s)           112             112           128          106              112            112          112                     224

          Technology             10nm            14nm          14nm         16nm              7nm           7nm           7nm                    10nm

          Modulation             PAM-4          PAM-4         PAM-4         PAM-4            PAM-4         PAM-4         PAM-4                   PAM-4

            FFE taps                4              8             3            3                 4             6             7                       8                          PLL
          Architecture         Analog FFE       8b DAC      Analog FFE      7b DAC        Analog FFE       7b DAC       7b DAC                  7b DAC                       (8.7%)
         Multiplexing              4:1            4:1           4:1           2:1              4:1           4:1           2:1                     4:1
                                                                                                                                                                                      CK Distribution
          Clock source          On-chip         External     External       On-chip         On-chip        On-chip      On-chip                 On-chip
                                                                                                                                                                      DAC + Bias         (24.9%)
             Driver               CML             SST          CML           CML              CML            SST        H-bridge                  CML
                                                                                          1.78 (w/ PLL)*              1.56 (w/ PLL)           1.88 (w/ PLL)
                                                                                                                                                                       (22.3%)
     Analog power (pJ/b) 1.72 (w/o PLL) 2.05 (w/o PLL)      1.3 (w/o PLL)      -                              -
                                                                                          1.34 (w/o PLL)              1.05 (w/o PLL)          1.74 (w/o PLL)

      Digital power (pJ/b)        N/A           0.5 (FFE)       N/A            -              N/A             -        0.13 (FFE)              0.37 (FFE)
                                                                                                                                                   65
                                                                                                                                                                               Serializer +
           RJ (fs_rms)            150            185**            -          197              140             -           171
                                                                                                                                       4MHz (1st order CDR) - 90GHz            CK Sampler
         Swing (Vppd)             0.75            0.92          1.0           1.1              1.0            -            1.2                     1.0
                                                                                                                                                                                (44.1%)
              RLM                 0.99              -          0.99          0.95               -           0.99          0.94                    0.99
                                                                                                                                            37.5 (112Gb/s)
           SNDR (dB)               31               -             -          34.6               -            36             -
                                                                                                                                            33.3 (224Gb/s)
       Analog supply (V)            1             0.95       0.95/1.2       1.1/1.2      0.88/1.2/1.5      0.85/1.2     0.9/1.2               0.85/1/1.5
                                                                                                                                                                          1.88pJ/bit (w/ PLL)
          Area (mm2)              0.03           0.095         0.048           -             0.136            -          0.193                   0.088
                                                                                                                                                                          1.74pJ/bit (w/o PLL)
     * Combined clock distribution power for both TX and RX
     ** For 56Gb/s NRZ PRBS7. All other RJ numbers reported are from clock pattern.



© 2021 IEEE
                                                                                      8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS                                      Page 64 of 68
International Solid-State Circuits Conference

---

Outline

             Backgrounds
             TX architecture
             Circuit implementation
                              Clock distribution
                              Data-path
                              DAC
                              Output pad

             Measurement results
             Summary
© 2021 IEEE
                                                    8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS   Page 65 of 68
International Solid-State Circuits Conference

---

Summary

            We presented the first 224Gb/s CMOS TX fabricated in Intel 10nm FinFET
             technology.
            In measurement, TX achieved 65fs_rms RJ at 112Gbaud clock pattern.
            The TX demonstrated open eye at 224Gb/s PAM-4 with 1.88pJ/bit.
            The TX occupies 0.088mm2 silicon area.
            The TX shows robust jitter/BW performance across voltage/temperature.
            This result proves the effectiveness of proposed design techniques to
             improve overall jitter and BW of TX for next generation 224Gb/s TX.


© 2021 IEEE
                                                8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS   Page 66 of 68
International Solid-State Circuits Conference

---

References
        [1] D. Shin et al. “A 23.9-29.4GHz Digital LC-PLL with a Coupled Frequency Doubler for Wireline
         Applications in 10nm FinFET,” ISSCC, Feb. 2021. Intel
        [2] J. Kim et al. "A 112Gb/s PAM-4 Transmitter with 3-Tap FFE in 10nm CMOS,” ISSCC, pp. 102-103, Feb.
         2018. Intel
        [3] C. Menolfi et al. "A 112Gb/s 2.6pJ/b 8-Tap FFE PAM-4 SST TX in 14nm CMOS," ISSCC, pp. 104-105,
         Feb. 2018. IBM
        [4] Z. Toprak-Deniz et al. "A 128Gb/s 1.3pJ/b PAM-4 Transmitter with Reconfigurable 3-Tap FFE in 14nm
         CMOS," ISSCC, pp. 122-123, Feb. 2019. IBM
        [5] C. Loi et al. "A 400Gb/s Transceiver for PAM-4 Optical Direct-Detect Application in 16nm FinFET,"
         ISSCC, pp. 120-121, Feb. 2019. Inphi
        [6] J. Lim et al. "A 112Gb/s PAM-4 Long-Reach Wireline Transceiver Using a 36-Way Time-Interleaved SAR-
         ADC and Inverter-Based RX Analog Front-End in 7nm FinFET," ISSCC, pp. 116-117, Feb. 2020. Xilinx
        [7] T. Ali et al. "A 460mW 112Gb/s DSP-Based Transceiver with 38dB Loss Compensation for Next-
         Generation Data Centers in 7nm FinFET Technology," ISSCC, pp. 118-119, Feb. 2020. MediaTek
        [8] E. Groen et al. "A 10-to-112Gb/s DSP-DAC-Based Transmitter with 1.2Vppd Output Swing in 7nm
         FinFET," ISSCC, pp. 120-121, Feb. 2020. RAMBUS
© 2021 IEEE
                                                8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS   Page 67 of 68
International Solid-State Circuits Conference

---

Thank You


© 2021 IEEE
                                                8.1: A 224Gb/s DAC-Based PAM-4 Transmitter with 8-Tap FFE in 10nm CMOS   Page 68 of 68
International Solid-State Circuits Conference

---

An Output Bandwidth Optimized
           200Gb/s PAM-4 100Gb/s NRZ Transmitter
               with 5-Tap FFE in 28nm CMOS
                           Minsoo Choi1, Zhongkai Wang1, Kyoungtae Lee1, Kwanseo Park1,
                              Zhaokai Liu1, Ayan Biswas1, Jaeduk Han2, and Elad Alon1

                                                1University of California, Berkeley, CA,

                                                  2Hanyang University, Seoul, Korea



© 2021 IEEE                                           8.2: An Output Bandwidth Optimized 200Gb/s PAM-4 100Gb/s NRZ Transmitter with 5-Tap FFE in 28nm CMOS
International Solid-State Circuits Conference                                                                                                                1 of 44

---

Self Introduction
                                                 Education
                                                   Ph.D. in EE from POSTECH, Korea, in 2018
                                                   M.S. in EE from POSTECH, Korea, in 2014
                                                   B.S. in EE from Soongsil University, Korea in 2012
                                                 Experience
    Minsoo Choi                                    Postdoc at UC Berkeley, CA, since 2018
                                                 Research Interests
                                                   High-speed SerDes and interfaces
                                                   Analog/mixed-signal circuit design & automation
                                                   Interconnect modeling and characterization
© 2021 IEEE                                          8.2: An Output Bandwidth Optimized 200Gb/s PAM-4 100Gb/s NRZ Transmitter with 5-Tap FFE in 28nm CMOS
International Solid-State Circuits Conference                                                                                                               2 of 44

---

Outline
                  Motivation

                  TX Architecture

                  Circuit Implementation

                  Design and Measurement Results

                  Conclusion


© 2021 IEEE                                     8.2: An Output Bandwidth Optimized 200Gb/s PAM-4 100Gb/s NRZ Transmitter with 5-Tap FFE in 28nm CMOS
International Solid-State Circuits Conference                                                                                                          3 of 44

---

Recently Published High-Speed TXs
                                                                                                                                Src: [ISSCC, VLSI Circuits]
                                                  This work!                                                                                  This work!
                Data rate [Gb/s]




                                                                                           Data rate [Gb/s]
                                                                                                                                            ~3x faster
                                                   2x/3~4yrs




                                                Year                                                                        Technology [nm]
                   A 200Gb/s PAM-4 TX in a 28nm CMOS
                   The highest data rate in a standard planar CMOS technology
© 2021 IEEE                                            8.2: An Output Bandwidth Optimized 200Gb/s PAM-4 100Gb/s NRZ Transmitter with 5-Tap FFE in 28nm CMOS
International Solid-State Circuits Conference                                                                                                                 4 of 44

---

TX Architecture Considerations
                           Data                 4:1                                                     Data                 2:1
                           Path                 MUX       DRV                                           Path                 MUX                       DRV
                                                      25GHz
                                                      4-phase clock
                                             Quad.
                                            CLK Gen.

                                                      25GHz                                                                                50GHz
                                                      differential clock                                                                   differential clock

               Quarter-rate & 25GHz clock
                       Easy clock distribution
                                                                                                           Half-rate & 50GHz clock
                                                                                                   Hard clock distribution
                       Enough timing margin for MUX                                               Poor timing margin for MUX
                       Quadrature clock generator                                                 No multi-phase clock generator

© 2021 IEEE                                                 8.2: An Output Bandwidth Optimized 200Gb/s PAM-4 100Gb/s NRZ Transmitter with 5-Tap FFE in 28nm CMOS
International Solid-State Circuits Conference                                                                                                                      5 of 44

---

TX Architecture Considerations
                  LSB                           Gm
                                                                               LSB0                   Gm                                                            Pre
                                                     xM                                                                                                           Post
                                                                               LSB1                   Gm
                                                                                                                                                                 Main
                  MSB                           Gm
                                                             N




                                                                                  ...

                                                                                                       ...
                                                                                                                                          MSB                    Gm
                                                     xM                                                                                                               x2
                                                                               MSBk-1                 Gm
                  MSB                           Gm                                                                                        LSB                    Gm
                                                                               MSBk                   Gm
                                                     xM

      Segmented FFE TX DAC-based FFE TX
              Reconfigurable taps                            Flexible taps
                                                                                                                                         Analog FFE TX
                                                                                                                                 Fixed number of taps
              High output BW                                 High output BW                                                    Low output BW
              Complex circuit imp.                           Complex circuit imp.                                              Simple circuit imp.

© 2021 IEEE                                               8.2: An Output Bandwidth Optimized 200Gb/s PAM-4 100Gb/s NRZ Transmitter with 5-Tap FFE in 28nm CMOS
International Solid-State Circuits Conference                                                                                                                              6 of 44

---

The Proposed TX Architecture
                                                                     Re-      Driver w/                                      VDDRV
                                                                                                                                                            Quadrate architecture
                       128:8 Serializer


                                                Thermometer
                                                               8           8
                                                                    timer D8A 5-tap FFE x6                                                                
  Pattern Gen.




                 128                      8                   T8A                                                      IU    RTX
                                                  Encoder

                                                                              Driver w/                                                                    Segmented structure
                                          MSB



                                                               8     Re-   8                                                   T-coil
                                                              T8B   timer D8B 5-tap FFE x6               D1P                                TXP
                 128                      8
                                                               8     Re-   8  Driver w/
                                                                                                         D1N
                                                                                                                       ESD
                                                                                                                                            TXN
                                                                                                                                                           Reconfigurable FFE
                                                                    timer D8C 5-tap FFE x6
                                          LSB




                                                              T8C
        C128                    C16                                   C8'I/Q     C8I/Q C4I/Q                                                               Coarse/fine FFE tuning
                                2                                     4          4
             ⁄8                            ⁄2                 PI
                                                                                                                                                           Flexible clock timing
                                                        C8
                                                       Buffer                                                                                               control
                                                                      4          4

                                                                     PI/
                                                                    DCDL
                                                                                PI/
                                                                               DCDL
                                                                                                                                                           T-coil for BW extension
                                                                                           C4
                                                                      4

                                                                     ⁄2
                                                                                 4

                                                                                ⁄2
                                                                                          Buffer                                                           Output BW optimized
                                                                                                                                            C4
                                                                                      4              4    DCC/
                                                                                                          QEC
                                                                                                                        4   Quad. C4P
                                                                                                                            Gen.    N                       merged 4:1 MUX/driver

© 2021 IEEE                                                                           8.2: An Output Bandwidth Optimized 200Gb/s PAM-4 100Gb/s NRZ Transmitter with 5-Tap FFE in 28nm CMOS
International Solid-State Circuits Conference                                                                                                                                                7 of 44

---

Outline
                  Motivation

                  TX Architecture

                  Circuit Implementation

                  Design and Measurement Results

                  Conclusion


© 2021 IEEE                                     8.2: An Output Bandwidth Optimized 200Gb/s PAM-4 100Gb/s NRZ Transmitter with 5-Tap FFE in 28nm CMOS
International Solid-State Circuits Conference                                                                                                          8 of 44

---

A Driver Segment with 5-Tap FFE
                                                4UI Wide Pulse Gen.                                    8:4 MUX (half circuit)
                                   D8S<0>
                                                C8S<0>                                                        VDD      VDD
                   D8A<0>          D8S<2>                                    D4U<0> D4U<0:7>
                                   D8S<4>       Sgn<0>                                                 D4U<0>   D4U<1>
                   D8A<1>                                                                                                D4<0>
                                   D8S<6>       D8S<0>
                             4:1



                   D8A<2>                                                    D4D<0> D4D<0:7>           D4D<0>   D4D<1>
                                                C8S<2>
                   D8A<3>          x4
                                   D8S<1>                                                                                                    x4
                   D8A<4>          D8S<3>       C8S<2>                       D4U<1>                            D4<0:3>                                    4:1 MUX/Driver (half circuit)
                                   D8S<5>       Sgn<0>                                  1UI
   From Re-Timer




                   D8A<5>
                                   D8S<7>       D8S<1>                                            VDD    VDD                               VDD
                                                                                      Wide
                             4:1




                   D8A<6>                                                    D4D<1>          C4Q                                                   D1A                                             D1P
                                                C8S<0>                               Pulse                                                         D1B     VFFE<0>                                 D1N
                   D8A<7>          x4                                                  Gen. D4<0>                                                  D1C
                                                                                 x4    (half         C4I                                    D1A    D1D          D1A         D1B        D1C   D1D
                               D8 Data                                              circuit) C4
                               Selector           C8S<0:3>                                                Q

                                                                         x4     C8 Phase
                                                           4:1                  Selector                                                     x4
                                                                      C8QB




                                                                                                                                    C4QB
                                                                                                                                                           VFFE<0>
                                                               C8IB




                                                                                                                             C4IB
                                                         C8Q




                                                                                                                       C4Q
                                                   C8I




                                                                                                                 C4I
                                                                                                                                                                                             x6 segments
                                                  C8 Buffer                                                     C4 Buffer                             Bias Circuit                           x3 bundles
© 2021 IEEE                                                                     8.2: An Output Bandwidth Optimized 200Gb/s PAM-4 100Gb/s NRZ Transmitter with 5-Tap FFE in 28nm CMOS
International Solid-State Circuits Conference                                                                                                                                                            9 of 44

---

A Driver Segment with 5-Tap FFE
                                                4UI Wide Pulse Gen.                                    8:4 MUX (half circuit)
                                   D8S<0>
                                                C8S<0>                                                        VDD      VDD
                   D8A<0>          D8S<2>                                    D4U<0> D4U<0:7>
                                   D8S<4>       Sgn<0>                                                 D4U<0>   D4U<1>
                   D8A<1>                                                                                                D4<0>
                                   D8S<6>       D8S<0>
                             4:1



                   D8A<2>                                                    D4D<0> D4D<0:7>           D4D<0>   D4D<1>
                                                C8S<2>
                   D8A<3>          x4                                                                                                                      4:1 MUX/Driver
                   D8A<4>
                                   D8S<1>
                                   D8S<3>       C8S<2>                       D4U<1>                            D4<0:3>
                                                                                                                                             x4
                                                                                                                                                           (half circuit)
                                                                                                                                                          4:1 MUX/Driver (half circuit)
                                   D8S<5>       Sgn<0>                                  1UI
   From Re-Timer




                   D8A<5>
                                   D8S<7>       D8S<1>                                            VDD    VDD                               VDD
                                                                                      Wide
                             4:1




                   D8A<6>                                                    D4D<1>          C4Q                                                   D1A                                             D1P
                                                C8S<0>                               Pulse                                                         D1B     VFFE<0>                                 D1N
                   D8A<7>          x4                                                  Gen. D4<0>                                                  D1C
                                                                                 x4    (half         C4I                                    D1A    D1D          D1A         D1B        D1C   D1D
                               D8 Data                                              circuit) C4
                               Selector           C8S<0:3>                                                Q

                                                                         x4     C8 Phase
                                                           4:1                  Selector                                                     x4
                                                                      C8QB




                                                                                                                                    C4QB
                                                                                                                                                           VFFE<0>
                                                               C8IB




                                                                                                                             C4IB
                                                         C8Q




                                                                                                                       C4Q
                                                   C8I




                                                                                                                 C4I
                                                                                                                                                                                             x6 segments
                                                  C8 Buffer                                                     C4 Buffer                             Bias Circuit                           x3 bundles
© 2021 IEEE                                                                     8.2: An Output Bandwidth Optimized 200Gb/s PAM-4 100Gb/s NRZ Transmitter with 5-Tap FFE in 28nm CMOS
International Solid-State Circuits Conference                                                                                                                                                            10 of 44

---

Design Options of 4:1 MUX
     Stacked 4:1 MUX
                 D0
                       D1
                                                                              Low output BW
                                                4:1
                                                      D0 D1 D2 D3
                              D2
                                    D3
                                                  C4I/Q BW!

   
    Unstacked 4:1 MUX + 1UI wide pulse generator
                 D0                               1UI             D0
                       D1                        Wide                   D1
                                                                                                                                           Improved output BW


                                                                                                   4:1
                                                                                                                 D0 D1 D2 D3
                              D2                 Pulse                        D2
                                    D3           Gen.
                                                                                    D3
                                                      C4I/Q
                                                                                                              Details: [Z. Toprak-Deniz, JSSC 2019]
© 2021 IEEE                                                   8.2: An Output Bandwidth Optimized 200Gb/s PAM-4 100Gb/s NRZ Transmitter with 5-Tap FFE in 28nm CMOS
International Solid-State Circuits Conference                                                                                                                        11 of 44

---

Prior Arts: 4:1 MUX in Pre-Driver
     [Z. Toprak-Deniz, ISSCC 2019], [Y. Frans, ISSCC 2016]

                                                                                                                        An internal full-rate node
                                                                                                                        Area limitation for a
                      D0                             Gm
                                                                                                                         passive inductor
                                 D1                  Gm                                                                 Insufficient BW extension
                                                     Gm                                                                  with an active inductor
                                           D2
                                                                BW! Driver
                                                D3   Gm
                                                                                                                                   Insufficient BW in
                                                     4:1 MUX                                                                        28nm technology…

© 2021 IEEE                                               8.2: An Output Bandwidth Optimized 200Gb/s PAM-4 100Gb/s NRZ Transmitter with 5-Tap FFE in 28nm CMOS
International Solid-State Circuits Conference                                                                                                                    12 of 44

---

Prior Arts: Merged 4:1 MUX/Driver
   
    [J. Kim, ISSCC 2018]



                      D0                             Gm
                                                                                                                        4:1 output serialization
                                 D1                  Gm                                                                 Only one full-rate node
                                                     Gm
                                                                                                                        No area limitation for a
                                           D2
                                                                                                                         passive inductor
                                                D3   Gm
                                                                                                                                   Improved BW
                                                     Merged
                                                     4:1 MUX/Driver
© 2021 IEEE                                               8.2: An Output Bandwidth Optimized 200Gb/s PAM-4 100Gb/s NRZ Transmitter with 5-Tap FFE in 28nm CMOS
International Solid-State Circuits Conference                                                                                                                    13 of 44

---

Prior Arts: Driver Type
     A conventional CML driver                                                                     
                                                                                                     A tailless CML driver



                                                               Fine tuning of the
                                                                  tap weight
                            OutP                OutN                                                                           OutP                           OutN
                      InN                             InP                                                            Vbias
                                                BW!    Lower BW due to
                         Vbias                                                                                           InN                                       InP
                                                       a larger parasitic
                                                       at the tail node                                                         [G. Steffan, ISSCC 2017]
© 2021 IEEE                                                 8.2: An Output Bandwidth Optimized 200Gb/s PAM-4 100Gb/s NRZ Transmitter with 5-Tap FFE in 28nm CMOS
International Solid-State Circuits Conference                                                                                                                            14 of 44

---

The Final Design Choice for High BW
                       Output Network
                                                VDDRV                  RRX             RRX

                                                  RTX                                                            Merged 4:1 MUX/driver
                                  CESD                                       Z0 Z0                               Tailless CML driver
                                                  T-coil          CPAD
                           ESD
                                                                  TXP
                                                                  TXN
                                                                                                                 Output BW is only consideration
                                                                  CPAD                                           1KV HBM ESD protection diode
                                         D1P            D1N
                                     CDRV               CDRV                                                     T-coil for BW extension
                              BW!
                       VFFE<0>
                                                        x4                                                             Still insufficient BW in
                     D1A(B,C,D)N
                                                                                                                        28nm technology…
                                                               D1A(B,C,D)P


                    4:1 MUX/Driver                                       x6
                                                                          x3
© 2021 IEEE                                                              8.2: An Output Bandwidth Optimized 200Gb/s PAM-4 100Gb/s NRZ Transmitter with 5-Tap FFE in 28nm CMOS
International Solid-State Circuits Conference                                                                                                                                   15 of 44

---

The Proposed Merged 4:1MUX/Driver
                                                                                                                                      4            ROUTD
                       Output Network                                                                                               10
                                                VDDRV                 RRX           RRX




                                                                                                                   Resistance [Ω]
                                                  RTX                                                                               103
                                                                            Z0 Z0
                                                  T-coil
                           ESD
                                                                TXP                                                                 102
                                                                TXN
                                                                                                                                                     ~51Ω @ VLOW=0.55V
                                         D1P             CNDRV
                                                        D1                                                                          101
            ROUTD                    CDRV               CDRV                                                                              VLOW         VMID                  VHIGH
                                                                                                                                            TXP or TXN [V]

         VFFE<0>
             VFFE<0>
                                                        x4
                                                             WM1                         Minimize CDRV by increasing VOV of
                     D1A(B,C,D)N                             D1A(B,C,D)P
                                                                                          M1 (reducing the widths of M1/M2)
                                                             WM2                                 Too small output resistance or limited
                    4:1 MUX/Driver                                    x6                                 output swing in 28nm technology…
                                                                       x3
© 2021 IEEE                                                           8.2: An Output Bandwidth Optimized 200Gb/s PAM-4 100Gb/s NRZ Transmitter with 5-Tap FFE in 28nm CMOS
International Solid-State Circuits Conference                                                                                                                                        16 of 44

---

The Proposed Merged 4:1MUX/Driver
                                                                                                          VDDRV
                       Output Network                                                                                                                             104
                            VDDH                VDDRV                   RRX           RRX                                         VHIGH                                        ROUTD w/o IU
                                                                                                                                                                               ROUTD w/ IU




                                                                                                                                                 Resistance [Ω]
                                                                                                                                                                               ROUTU
     ROUTU
                                      IU          RTX                                                                             VMID                            103
                          CU                                                  Z0 Z0
                                                  T-coil
                           ESD
                                                                  TXP                      VLOW                                                                   102
                                                                  TXN
                                                                                                              ∆VMID=RTXIU
                                                                        ROUT                                                                                        1
                                                                                                                                                                         ~94Ω @ VLOW=0.7V
            ROUTD
                                           D1P          D1N                                                                                                       10
                                     CDRV               CDRV                                                                                                            VLOW      VMID        VHIGH
                                                                                                             VSS                                                         TXP or TXN [V]
                       VFFE<0>
                                                        x4                                 Pull-up current source IU with ROUTU
                     D1A(B,C,D)N                               D1A(B,C,D)P
                                                                                                   Increasing ROUTD by boosting VMID
                                                                                                   Stabilizing ROUT in combination with ROUTD
                    4:1 MUX/Driver                                      x6                         CU<<CDRV and isolated CU due to T-coils
                                                                         x3
© 2021 IEEE                                                             8.2: An Output Bandwidth Optimized 200Gb/s PAM-4 100Gb/s NRZ Transmitter with 5-Tap FFE in 28nm CMOS
International Solid-State Circuits Conference                                                                                                                                                     17 of 44

---

The Proposed Merged 4:1MUX/Driver
                                                                                                                                                    ROUT
                       Output Network                                                                                              100
   VDDH=~1.4V
          VDDH VDD
               VDDRV RV=1.3V RRX                                                   RRX
                                                                                                                                    80




                                                                                                                  Resistance [Ω]
                                      IU         RR
                                                  TX
                                                    TX=90Ω
                                                                                                                                    60
                          CU                                              Z0 Z0
                                                 T-coil
                                                               TXP
                                                                                                                                    40
                           ESD                                 TXN
                                                                                                                                    20
                                           D1P       D1N             ROUT                                                            0
                                     CDRV            CDRV                                                                             VLOW            VMID                  VHIGH
                                                                                                                                         TXP or TXN [V]
                       VFFE<0>
                                                     x4
                                                                                        ROUT = ~50Ω (within ±20% error)
                     D1A(B,C,D)N                            D1A(B,C,D)P                 BW of output stage = ~33GHz
                    4:1 MUX/Driver
                                                                                        BW of overall TX = ~17GHz
                                                                     x6
                                                                      x3
                                                                                                  (Including 1UI wide pulse gen.)
© 2021 IEEE                                                          8.2: An Output Bandwidth Optimized 200Gb/s PAM-4 100Gb/s NRZ Transmitter with 5-Tap FFE in 28nm CMOS
International Solid-State Circuits Conference                                                                                                                                       18 of 44

---

A Driver Segment with 5-Tap FFE
                                                4UI Wide Pulse Gen.                                       8:4 MUX (half circuit)
                                   D8S<0>
                                                C8S<0>                                                           VDD      VDD
                   D8A<0>          D8S<2>                                    D4U<0> D4U<0:7>




                                                                                                                                                                                                       To Output
                                   D8S<4>       Sgn<0>                                                    D4U<0>   D4U<1>
                   D8A<1>




                                                                                                                                                                                                       Network
                                   D8S<6>       D8S<0>                                                                      D4<0>
                             4:1



                   D8A<2>                                                    D4D<0> D4D<0:7>              D4D<0>   D4D<1>
                                                C8S<2>
                   D8A<3>          x4
                                   D8S<1>                                                                                                       x4
                   D8A<4>          D8S<3>       C8S<2>                       D4U<1>                               D4<0:3>                                    4:1 MUX/Driver (half circuit)
                                   D8S<5>       Sgn<0>
                                                                                   1UI1UI
   From Re-Timer




                   D8A<5>
                                   D8S<7>       D8S<1>                                          VDD   VDD                                     VDD
                                                                                    Wide
                             4:1




                   D8A<6>                                                 D4 <1>Wide       C4                                                         D1A                                             D1P
                                                C8S<0>                         D
                                                                                   Pulse                     Q
                                                                                                                                                      D1B     VFFE<0>                                 D1N
                   D8A<7>          x4
                                                                               Pulse
                                                                              x4
                                                                                     Gen. D4<0>
                                                                                     (half
                                                                                                                                                      D1C
                               D8 Data                                           Gen.
                                                                                  circuit) C4
                                                                                                   C4                       I                  D1A    D1D          D1A         D1B        D1C   D1D
                               Selector
                                                                                 (half
                                                                                                             Q
                                                  C8S<0:3>
                                                                         x4 C8 Phase
                                                           4:1                circuit)
                                                                             Selector                                                           x4
                                                                      C8QB




                                                                                                                                       C4QB
                                                                                                                                                              VFFE<0>
                                                               C8IB




                                                                                                                                C4IB
                                                         C8Q




                                                                                                                          C4Q
                                                   C8I




                                                                                                                    C4I
                                                                                                                                                                                                x6 segments
                                                  C8 Buffer                                                        C4 Buffer                             Bias Circuit                           x3 bundles
© 2021 IEEE                                                                        8.2: An Output Bandwidth Optimized 200Gb/s PAM-4 100Gb/s NRZ Transmitter with 5-Tap FFE in 28nm CMOS
International Solid-State Circuits Conference                                                                                                                                                               19 of 44

---

1UI Wide Pulse Generator
       From                                                                                          To 4:1                                                                2UI window
       8:4 MUX                                                                                       MUX/                         D4<0>                       D0                       D4
                                                                                                     Driver                          C4I
                                                VDD         VDD              VDD
                                C4Q                                                           D1A
                                                                                                                                    C4Q
                                                      X                                       D1B
       D4<0:3>                  D4<0>                                                         D1C                                      X                D0                        D4
                                                  C4I              Y              D1A         D1D
                                C4Q                                                                                                    Y
                                                                                                                                    D1A                    D0                         D4
                                                                                     x4
                                                                                                                                    D1B                           D1                       D5
                                                                   C4QB
                                                            C4IB
                                                      C4Q
                                                C4I




                                                                                                                                    D1C                                  D2                     D6

                                    Matched delay                                                                                   D1D             D-1                          D3



© 2021 IEEE                                                               8.2: An Output Bandwidth Optimized 200Gb/s PAM-4 100Gb/s NRZ Transmitter with 5-Tap FFE in 28nm CMOS
International Solid-State Circuits Conference                                                                                                                                                        20 of 44

---

A Driver Segment with 5-Tap FFE
                                                4UI Wide Pulse Gen.                                    8:4 MUX (half circuit)
                                   D8S<0>
                                                C8S<0>                                                        VDD      VDD
                   D8A<0>          D8S<2>                                    D4U<0> D4U<0:7>




                                                                                                                                                                                                    To Output
                                   D8S<4>       Sgn<0>                                                 D4U<0>   D4U<1>
                   D8A<1>




                                                                                                                                                                                                    Network
                                   D8S<6>       D8S<0>                                                                   D4<0>
                             4:1



                   D8A<2>                                                    D4D<0> D4D<0:7>           D4D<0>   D4D<1>
                                                C8S<2>
                   D8A<3>          x4
                                   D8S<1>                                                                                                    x4
                   D8A<4>          D8S<3>       C8S<2>                       D4U<1>                            D4<0:3>                                    4:1 MUX/Driver (half circuit)
                                   D8S<5>       Sgn<0>                                  1UI
   From Re-Timer




                   D8A<5>
                                   D8S<7>       D8S<1>                                            VDD    VDD                               VDD
                                                                                      Wide
                             4:1




                   D8A<6>                                                    D4D<1>          C4Q                                                   D1A                                             D1P
                                                C8S<0>                               Pulse                                                         D1B     VFFE<0>                                 D1N
                   D8A<7>          x4                                                  Gen. D4<0>                                                  D1C
                                                                                 x4    (half
                   D8 Data
                       D8 Data                                                      circuit) C4
                                                                                                     C4I                                    D1A    D1D          D1A         D1B        D1C   D1D
                       Selector
                                                                               C8   Phase
                                                                                                          Q

                   Selector                       C8S<0:3>
                                                                         x4    C8 Phase
                                                           4:1                 Selector
                                                                               Selector                                                      x4
                                                                      C8QB




                                                                                                                                    C4QB
                                                                                                                                                           VFFE<0>
                                                               C8IB




                                                                                                                             C4IB
                                                                                                   Coarse FFE configuration by D8 data
                                                         C8Q




                                                                                                                       C4Q
                                                   C8I




                                                                                                                 C4I
                                                                                                    selector and C8 phase selector
                                                  C8 Buffer                                        Fully reconfigurable
                                                                                                     C4 Buffer           5-tap FFE
                                                                                                                   Bias Circuit
© 2021 IEEE                                                                     8.2: An Output Bandwidth Optimized 200Gb/s PAM-4 100Gb/s NRZ Transmitter with 5-Tap FFE in 28nm CMOS
International Solid-State Circuits Conference                                                                                                                                                            21 of 44

---

Coarse FFE Config.: E.g. Main Cursor
                                                4UI Wide Pulse Gen.                                                                                               8UI
                                D8S<0>
           D8A<0>               D8S<2>          C8S<0>                       D4U<0> D4U<0:7>                          D8A<0>                                         D0
                                D8S<4>          Sgn<0>
           D8A<1>                                                                                                     D8A<1>                                         D1
                                D8S<6>          D8S<0>
                         4:1



           D8A<2>                                                            D4D<0> D4D<0:7>
                                                C8S<2>
           D8A<3>               x4                                                                                    D8A<2>                 D-6                               D2
                                D8S<1>
           D8A<4>               D8S<3>          C8S<2>                                                                D8A<3>                 D-5                               D3
                                                                             D4U<1>
                                D8S<5>          Sgn<0>
           D8A<5>
                                D8S<7>          D8S<1>
                                                                                              To                      D8A<4>                        D-4                         D4
                         4:1




           D8A<6>
                                                C8S<0>                       D4D<1>           8:4                     D8A<5>                        D-3                         D5
           D8A<7>               x4
                                                                                              MUX
                                                                                    x4                                D8A<6>                               D-2                       D6
                            D8 Data
                            Selector              C8S<0:3>                                                            D8A<7>                               D-1                       D7
                                                                         x4      C8 Phase
         From                                              4:1                   Selector
                                                                                                                  Input data from re-timer
         Re-Timer
                                                                      C8QB
                                                               C8IB
                                                         C8Q
                                                   C8I




                                                                                                                          2UI-staggered octa-rate data
© 2021 IEEE                                                             8.2: An Output Bandwidth Optimized 200Gb/s PAM-4 100Gb/s NRZ Transmitter with 5-Tap FFE in 28nm CMOS
International Solid-State Circuits Conference                                                                                                                                             22 of 44

---

Coarse FFE Config.: E.g. Main Cursor
                                                4UI Wide Pulse Gen.
                                D8S<0>
           D8A<0>               D8S<2>          C8S<0>                       D4U<0> D4U<0:7>                          D8S<0>                                         D0
                                D8S<4>          Sgn<0>
           D8A<1>                                                                                                     D8S<1>
                                D8S<6>          D8S<0>                                                                                              D-4                         D4
                         4:1



           D8A<2>                                                            D4D<0> D4D<0:7>
                                                C8S<2>
           D8A<3>               x4                                                                                    D8S<2>                                         D1
                                D8S<1>
           D8A<4>               D8S<3>          C8S<2>                                                                D8S<3>                        D-3                         D5
                                                                             D4U<1>
                                D8S<5>          Sgn<0>
           D8A<5>
                                D8S<7>          D8S<1>
                                                                                              To                      D8S<4>                 D-6                               D2
                         4:1




           D8A<6>
                                                C8S<0>                       D4D<1>           8:4                     D8S<5>                               D-2                       D6
           D8A<7>               x4
                                                                                              MUX
                                                                                    x4                                D8S<6>                 D-5                               D3
                            D8 Data
                            Selector              C8S<0:3>                                                            D8S<7>                               D-1                       D7
                                                                         x4      C8 Phase
         From                                              4:1                   Selector
                                                                                                                  Selected data by D8 data
         Re-Timer
                                                                      C8QB
                                                               C8IB
                                                         C8Q




                                                                                                                   selector for main cursor config.
                                                   C8I




© 2021 IEEE                                                             8.2: An Output Bandwidth Optimized 200Gb/s PAM-4 100Gb/s NRZ Transmitter with 5-Tap FFE in 28nm CMOS
International Solid-State Circuits Conference                                                                                                                                             23 of 44

---

Coarse FFE Config.: E.g. Main Cursor
                                                4UI Wide Pulse Gen.
                                 D8S<0>
           D8A<0>                D8S<2>         C8S<0>                       D4U<0> D4U<0:7>                          D8S<0>                                         D0
                                 D8S<4>         Sgn<0>
           D8A<1>                                                                                                     D8S<1>
                                 D8S<6>         D8S<0>                                                                                              D-4                         D4
                          4:1



           D8A<2>                                                            D4D<0> D4D<0:7>
                                                C8S<2>
           D8A<3>               x4                                                                                    C8S<0>
                                D8S<1>
           D8A<4>               D8S<3>          C8S<2>                                                                C8S<2>
                                                                             D4U<1>
                                D8S<5>          Sgn<0>
           D8A<5>
                                D8S<7>          D8S<1>
                                                                                              To                      D4U<0>                           D0
                          4:1




           D8A<6>
                                                C8S<0>                       D4D<1>           8:4                     D4D<0>                           D0
           D8A<7>               x4
                                                                                              MUX
                                                                                    x4                                D4U<1>                                                   D4
                                                C8S<0>
                                                C8S<1>
                                                C8S<2>
                                                C8S<3>




                            D8 Data
                            Selector              C8S<0:3>                                                            D4D<1>                                                   D4
                                                                         x4      C8 Phase
         From                                              4:1                   Selector
                                                                                                              8:4 MUX output
         Re-Timer
                                                                      C8QB
                                                               C8IB
                                                         C8Q
                                                   C8I




                                                                                                                       D4<0>                           D0                      D4

© 2021 IEEE                                                             8.2: An Output Bandwidth Optimized 200Gb/s PAM-4 100Gb/s NRZ Transmitter with 5-Tap FFE in 28nm CMOS
International Solid-State Circuits Conference                                                                                                                                        24 of 44

---

Coarse FFE Config.: E.g. 1 Post Cursor
                                                4UI Wide Pulse Gen.
                                D8S<0>
           D8A<0>               D8S<2>          C8S<0>                       D4U<0> D4U<0:7>                          D8S<0>                 D-5                               D3
                                D8S<4>          Sgn<0>
           D8A<1>                                                                                                     D8S<1>
                                D8S<6>          D8S<0>                                                                                                     D-1                       D7
                         4:1



           D8A<2>                                                            D4D<0> D4D<0:7>
                                                C8S<2>
           D8A<3>               x4                                                                                    D8S<2>                                         D0
                                D8S<1>
           D8A<4>               D8S<3>          C8S<2>                                                                D8S<3>                        D-4                         D4
                                                                             D4U<1>
                                D8S<5>          Sgn<0>
           D8A<5>
                                D8S<7>          D8S<1>
                                                                                              To                      D8S<4>                                         D1
                         4:1




           D8A<6>
                                                C8S<0>                       D4D<1>           8:4                     D8S<5>                        D-3                         D5
           D8A<7>               x4
                                                                                              MUX
                                                                                    x4                                D8S<6>                 D-6                               D2
                            D8 Data
                            Selector              C8S<0:3>                                                            D8S<7>                               D-2                       D6
                                                                         x4      C8 Phase
         From                                              4:1                   Selector
                                                                                                                  Selected data by D8 data
         Re-Timer
                                                                      C8QB
                                                               C8IB
                                                         C8Q




                                                                                                                   selector for 1 post cursor config.
                                                   C8I




© 2021 IEEE                                                             8.2: An Output Bandwidth Optimized 200Gb/s PAM-4 100Gb/s NRZ Transmitter with 5-Tap FFE in 28nm CMOS
International Solid-State Circuits Conference                                                                                                                                             25 of 44

---

Coarse FFE Config.: E.g. 1 Post Cursor
                                                4UI Wide Pulse Gen.
                                 D8S<0>
           D8A<0>                D8S<2>         C8S<0>                       D4U<0> D4U<0:7>                          D8S<0>                 D-5                               D3
                                 D8S<4>         Sgn<0>
           D8A<1>                                                                                                     D8S<1>
                                 D8S<6>         D8S<0>                                                                                                     D-1                      D7
                          4:1



           D8A<2>                                                            D4D<0> D4D<0:7>
                                                C8S<2>
           D8A<3>               x4                                                                                    C8S<0>
                                D8S<1>
           D8A<4>               D8S<3>          C8S<2>                                                                C8S<2>
                                                                             D4U<1>
                                D8S<5>          Sgn<0>
           D8A<5>
                                D8S<7>          D8S<1>
                                                                                              To                      D4U<0>                                                   D3
                          4:1




           D8A<6>
                                                C8S<0>                       D4D<1>           8:4                     D4D<0>                                                   D3
           D8A<7>               x4
                                                                                              MUX
                                                                                    x4                                D4U<1>                           D-1
                                                C8S<0>
                                                C8S<1>
                                                C8S<2>
                                                C8S<3>




                            D8 Data
                            Selector              C8S<0:3>                                                            D4D<1>                           D-1
                                                                         x4      C8 Phase
         From                                              4:1                   Selector
                                                                                                              8:4 MUX output
         Re-Timer
                                                                      C8QB
                                                               C8IB
                                                         C8Q
                                                   C8I




                                                                                                                       D4<0>                           D-1                     D3

© 2021 IEEE                                                             8.2: An Output Bandwidth Optimized 200Gb/s PAM-4 100Gb/s NRZ Transmitter with 5-Tap FFE in 28nm CMOS
International Solid-State Circuits Conference                                                                                                                                            26 of 44

---

Coarse FFE Config.: E.g. Main/1 Post
      8:4 MUX output
                4UI Wide Pulse Gen.                                                                          8:4 MUX (half circuit)
                                     D8S<0>
                                                                                                                    VDD      VDD
                     D8 Main
                         <0>  cursor  config. D4 <0> D4 <0:7> D4 <0>
                                  C8 <0>
                                     D8S<2>




                                                                                                                                                                                                          To Output
                        A                         S
                                                                                  U             U
                                     D8S<4>
                                  Sgn<0>                                                                       U      D4U<1>
                      D8A<1>




                                                                                                                                                                                                          Network
                                     D8S<6>     D8S<0>                                                                         D4<0>
             D4<0>                       D0                        D4
                               4:1



                D8A<2>                                                          D4D<0> D4D<0:7>              D4D<0>   D4D<1>
                                                C8S<2>
                        x4
                      D8A<3>
             D4<1>           D1
                         D8S<1>                                    D5                                                                              x4
                D8A<4>   D8S<3>                 C8S<2>                          D4U<1>                               D4<0:3>                                    4:1 MUX/Driver (half circuit)
             D4<2>     D-2D8S<5>                   D2
                                                Sgn<0>                          D6
   From a Re-Timer




                D8A<5>
                         D8S<7>
                                                                                           1UI       VDD    VDD                                  VDD
                                                D8S<1>                                   Wide
                               4:1




                D8A<6>                                                                                                                                                                                   D1P
             D4<3>             D-1              C8SD
                                                   <0>
                                                     3                          DD7<1> Pulse C4Q
                                                                                D4                                                                       D1A
                                                                                                                                                                                                         D1N
                      D8A<7>       x4                                                                                                                    D1B     VFFE<0>
                                                                                          Gen. D4<0>                                                     D1C
                                                                                          (half
                      1 post  cursor config.
                                                                                    x4                  C4I                                       D1A    D1D          D1A         D1B        D1C   D1D
                          D8 Data                                                      circuit) C4
                               Selector           C8S<0:3>                                                      Q


             D4<0>                       D-1                       D        x4        C8 Phase
                                                              4:1 3                   Selector                                                     x4

             D4<1>                       D0                        D4
                                                                         C8QB




                                                                                                                                          C4QB
                                                                                                                                                                 VFFE<0>
                                                                  C8IB




                                                                                                                                   C4IB
                                                            C8Q




                                                                                                                             C4Q
                                                      C8I




                                                                                                                       C4I
             D4<2>             D-3                D1                            D5
             D4<3>             D-2                D2                            D6
                                                                                                                                                                                                   x6 segments
                                                  C8 Buffer                                                           C4 Buffer                             Bias Circuit                           x3 bundles
© 2021 IEEE                                                                           8.2: An Output Bandwidth Optimized 200Gb/s PAM-4 100Gb/s NRZ Transmitter with 5-Tap FFE in 28nm CMOS
International Solid-State Circuits Conference                                                                                                                                                                  27 of 44

---

Coarse FFE Config.: E.g. Main/1 Post
                                                4UI Wide Pulse Gen.                                          8:4 MUX (half circuit)
      4:1   MUX/driver
        D8 <0>    C8 <0> output      D8S<0>
                                     D8S<2>
                            D4 <0> D4 <0:7>
                                                                                                                    VDD      VDD




                                                                                                                                                                                                          To Output
                        A                         S
                                                                                  U             U
                                     D8S<4>                                                                  D4U<0>   D4U<1>
                     D8 Main cursor  config.
                         <1>                    Sgn<0>




                                                                                                                                                                                                          Network
                        A
                                     D8S<6>
                                  D8 <0>                                                                                       D4<0>
                               4:1


                                                  S
                      D8A<2>                                                    D4D<0> D4D<0:7>              D4D<0>   D4D<1>
                                                C8S<2>
                      D8A<3>   x4
                               D8S<1>                                                                                                              x4
       D1P                D-1 DD80S<3>
                      D8A<4>        D1 D    D3 D4
                                       C82S<2>                           D5 D4DU<1>
                                                                                6                                    D4<0:3>                                    4:1 MUX/Driver (half circuit)
                               D8S<5> Sgn<0>
   From a Re-Timer




                      D8A<5>
                               D8S<7> D8S<1>
                                                                                           1UI       VDD    VDD                                  VDD
                                                                                         Wide                                                          VFFE
                                                                                                                                                        D1 <0>
                               4:1




                      D8A<6>                                                    D4D<1>          C4Q                                                                                                      D1P
                                       C8S<0>                                           Pulse                                                            D1B
                                                                                                                                                            A
                                                                                                                                                                 VFFE<0>                                 D1N
                      D8A<7>   x4                                                         Gen. D4<0>
                      1 post cursor config.                                        x4    (half         C4I                                       D1A
                                                                                                                                                         D1C
                                                                                                                                                         D1D          D1A         D1B        D1C   D1D
                               D8 Data                                                 circuit) C4
                               Selector           C8S<0:3>                                                      Q

                                                                           x4 C8 Phase
       D1P                  D-2 D-1 D0 D1 D2                 D4:1 D
                                                                  3        4 D5
                                                                              Selector                                                             x4
                                                                         C8QB




                                                                                                                                          C4QB
                                                                                                                                                                 VFFE<0>
                                                                  C8IB




                                                                                                                                   C4IB
                                                            C8Q




                                                                                                                             C4Q
                                                      C8I




                                                                                                                       C4I
                       1UI shifted data stream                                                                                                                                                     x6 segments
                                                  C8 Buffer                                                           C4 Buffer                             Bias Circuit                           x3 bundles
© 2021 IEEE                                                                           8.2: An Output Bandwidth Optimized 200Gb/s PAM-4 100Gb/s NRZ Transmitter with 5-Tap FFE in 28nm CMOS
International Solid-State Circuits Conference                                                                                                                                                                  28 of 44

---

Fine FFE Control and Bias Circuit
     [G. Steffan, ISSCC 2017], [Z. Toprak-Deniz, ISSCC 2019]
             VDD                                  VDDRV                                                                          Tolerance to VDDRV drift
                                                                                To 4:1
                                                                                                                                   Main cursor




                                                                                                                                                              |Tap coefficient|
                         IDAC                          RMID                     MUX/Driver                                                                                        Main cursor
                                                VMID




                                                                                                                VFFE [V]
                                                                                                                                1 post cursor
                                                       IMID                                                                                                                       1 post cursor
                                                          5                  VFFE<0:17>



                                                                   5:1
                              VDD                                         x18                                                      VDDRV [V]                                       VDDRV [V]

                              Driver                                                                           7-bit current DACs
                              Replica                                                                          0.6mVppd resolution
                                     x5
                                                                                                               Tracking PVT variations
© 2021 IEEE                                            8.2: An Output Bandwidth Optimized 200Gb/s PAM-4 100Gb/s NRZ Transmitter with 5-Tap FFE in 28nm CMOS
International Solid-State Circuits Conference                                                                                                                                                29 of 44

---

TX Architecture: Clock Path
                                                                                                         Re-      Driver w/                                                               VDDRV




                                                         128:8 Serializer
                                                                                                 8             8




                                                                                  Thermometer
                                                                                                        timer D8A 5-tap FFE x6
                                    Pattern Gen.
                                                   128                      8                   T8A                                                                                IU     RTX




                                                                                    Encoder
                                                                                                                  Driver w/


                                                                            MSB
                                                                                                 8       Re-   8                                                                            T-coil
                                                                                                T8B     timer D8B 5-tap FFE x6                                    D1P                                   TXP
                                                   128                      8
                                                                                                                                                                  D1N                                   TXN
                                                                                                 8       Re-   8  Driver w/                                                        ESD
                                                                            LSB                 T8C     timer D8C 5-tap FFE x6
                                          C128            4-phase C16
                                                                  2
                                                                                                               C8'I/Q
                                                                                                               4
                                                                                                                                    C8I/Q C4I/Q 4-phase
                                                                                                                                    4
                                               ⁄ 8 12.5GHz
                                                       ⁄2      PI
                                                             clock                                                                                         25GHz clock
                                                                                          C8
                                                                                         Buffer
                                                                                                               4                   4

                                                                                                        PI/                  PI/                                                                              Differential
                                                                                                       DCDL                 DCDL                                                                              25GHz
                                                                                                                                                  C4
                                                                                                               4                   4
                                                                                                                                                 Buffer                                                       clock
                                                                                                            ⁄2                  ⁄2                                                                      C4
                                                                                                                                            4                 4    DCC/            4    Quad. C4P
                                                                                                                                                                   QEC                  Gen.    N


© 2021 IEEE                                                                                      8.2: An Output Bandwidth Optimized 200Gb/s PAM-4 100Gb/s NRZ Transmitter with 5-Tap FFE in 28nm CMOS
International Solid-State Circuits Conference                                                                                                                                                                          30 of 44

---

Clock Path: C4 Clock Distribution
                    C8 Phase Selector
                                                                                                                           Quadrature clock generator
            Re-Timer                                 1UI Wide Pulse Gen.                                                    [J. Kim, ISSCC 2018]

                           C8'I/Q                C8I/Q C4I/Q
                          4                      4
     C8                                                        CKOUT                                       CKIN
    Buffer
                          4                      4                                                                                          CKBOUT                        CKOUT
                   PI/                    PI/                                                                     x4
                  DCDL                   DCDL
                           4                     4        C4
                       ⁄2                       ⁄2       Buffer                                                                         VCM0                                  VCM1
                                                                                                          C4P
                                                     4         4   DCC/           4    Quad.              C4N
                                                                   QEC                 Gen.
                                                                                                                                                    CKIN                  CKBIN


© 2021 IEEE                                                        8.2: An Output Bandwidth Optimized 200Gb/s PAM-4 100Gb/s NRZ Transmitter with 5-Tap FFE in 28nm CMOS
International Solid-State Circuits Conference                                                                                                                                        31 of 44

---

Clock Path: C8 Clock Distribution
                    C8 Phase Selector
                                                                                                                            PI: 2.5ps resolution
            Re-Timer                                 1UI Wide Pulse Gen.
                                                                                                                            DCDL: 4.6ps tuning range
                           C8'I/Q                C8I/Q C4I/Q
                                                                                                                                     175fs resolution
                          4                      4
     C8
    Buffer                                                     Flexible clock timing                                                 CKIIN
                          4                      4
                                                               control by PI/DCDL
                   PI/                    PI/
                  DCDL                   DCDL                                                                                        CKQIN
                           4                     4        C4                                                                                                               CKIOUT
                       ⁄2                       ⁄2       Buffer                                                                      CKIBIN
                                                                                                           C4P
                                                     4          4   DCC/           4    Quad.              C4N
                                                                    QEC                 Gen.                                         CKQBIN
                                                                                                                                                                               x4

© 2021 IEEE                                                         8.2: An Output Bandwidth Optimized 200Gb/s PAM-4 100Gb/s NRZ Transmitter with 5-Tap FFE in 28nm CMOS
International Solid-State Circuits Conference                                                                                                                                       32 of 44

---

Outline
                  Motivation

                  TX Architecture

                  Circuit Implementation

                  Design and Measurement Results

                  Conclusion


© 2021 IEEE                                     8.2: An Output Bandwidth Optimized 200Gb/s PAM-4 100Gb/s NRZ Transmitter with 5-Tap FFE in 28nm CMOS
International Solid-State Circuits Conference                                                                                                          33 of 44

---

Generator-Based Design Flow
          Target specification
          & input parameters
             128:8 serializer                                                   Berkeley analog generator (BAG)
             Driver w/ 5-tap FFE                Data                             [E. Chang, CICC 2018]
                                                path
             T-coil                                                                     Open-source hierarchical python
                                                                                         framework
                                    ...




             C8 clock generation                                                        Parametrized design procedures
                                                Clock
             C4 clock generation                generation                              Process portable schematics,
                                                                                         layouts, verification testbenches
                                    ...




             VDAC
                                                Peripheral
             IDAC
                                     ...




© 2021 IEEE                                     8.2: An Output Bandwidth Optimized 200Gb/s PAM-4 100Gb/s NRZ Transmitter with 5-Tap FFE in 28nm CMOS
International Solid-State Circuits Conference                                                                                                          34 of 44

---

Generator-Based Design Flow
          Target specification                      Subblock
          & input parameters                     specification &
             128:8 serializer                   input parameters
             Driver w/ 5-tap FFE                Main driver
                                                      Resistor termination
             T-coil
                                                      4:1 MUX
                                    ...




             C8 clock generation                      Current source

             C4 clock generation                Pre driver
                                                     1UI pulse generator
                                    ...




             VDAC                                    8:4 MUX

             IDAC                                    4UI pulse generator
                                                                     ...
                                     ...




© 2021 IEEE                                      8.2: An Output Bandwidth Optimized 200Gb/s PAM-4 100Gb/s NRZ Transmitter with 5-Tap FFE in 28nm CMOS
International Solid-State Circuits Conference                                                                                                           35 of 44

---

Generator-Based Design Flow
          Target specification                      Subblock                                                                Generator
          & input parameters                     specification &
             128:8 serializer                   input parameters                                                               Run script

             Driver w/ 5-tap FFE                Main driver
                                                                                                                     Schematic generation
                                                      Resistor termination
             T-coil
                                                      4:1 MUX                                                          Layout generation
                                    ...




             C8 clock generation                      Current source
                                                                                                                               Extraction
             C4 clock generation                Pre driver




                                                                                                     Re-sizing
                                                     1UI pulse generator                                             Post layout simulation
                                    ...




             VDAC                                    8:4 MUX
                                                                                                                 N            Spec met?                 Y
             IDAC                                    4UI pulse generator                                                       (BW, ROUT)
                                                                                                                                                        Generated
                                                                     ...
                                     ...




                                                                                                                                                         4:1 MUX
© 2021 IEEE                                      8.2: An Output Bandwidth Optimized 200Gb/s PAM-4 100Gb/s NRZ Transmitter with 5-Tap FFE in 28nm CMOS
International Solid-State Circuits Conference                                                                                                                  36 of 44

---

Generator-Based Design Flow
                                                                                                                                  Customized &                    Top integration
          Target specification                                          Generator                                                  synthesized                     & verification
          & input parameters
                                                                Design or run script                                                                                        Data
             128:8 serializer                                                                                                                     ESD                       path
                                                                                                                                                                  Clock generation
             Driver w/ 5-tap FFE                                Schematic generation                                                Digital Wires
             T-coil
                                                                   Layout generation                                                  Generated instances
                                    ...




             C8 clock generation
                                                                           Extraction
             C4 clock generation                                                                                                                                         VDAC
                                                                                                                                                                T-coil
                                                Re-sizing


                                                                Post layout simulation
                                    ...




                                                                                                                                                                   C8 clk
             VDAC                                                                                                                                              IDAC Gen.
                                                            N                                                   Y
             IDAC                                                         Spec met?
                                                                                                                                   128:8 Driver
                                                                                                                                    Ser.                         C4 clk Gen.
                                     ...




© 2021 IEEE                                             8.2: An Output Bandwidth Optimized 200Gb/s PAM-4 100Gb/s NRZ Transmitter with 5-Tap FFE in 28nm CMOS
International Solid-State Circuits Conference                                                                                                                                        37 of 44

---

Die Photo and Layout & Area Details
     28nm planar CMOS technology
                                                                                Block             Layout   Area (mm2)
                                                                      1 Pattern gen. + digital Synthesized   0.1357
                                                                      2     TX data path           BAG       0.0886
                                                             4        3    Output network          BAG       0.0406
                              1                 2    3                4      Bias circuit      Custom + BAG 0.0205
                                                                      5     Clock receiver         BAG       0.0034
                                                7                            Quad gen. +
                          8                                           6                            BAG       0.0320
                                                 6                      DCC/QEC + C4 buffer
                                                         8              Dividers + PI/DCDL +
                                                5                     7                            BAG       0.0152
                                                                              C8 buffers
                                                                      8    VDACs + IDAC            BAG       0.0963
                                        1mm                                      Top              Custom     0.4323
© 2021 IEEE                                                  8.2: An Output Bandwidth Optimized 200Gb/s PAM-4 100Gb/s NRZ Transmitter with 5-Tap FFE in 28nm CMOS
International Solid-State Circuits Conference                                                                                                                       38 of 44

---

Measurement Setup
                                                        FPGA                                          200Gb/s                                                    Keysight E8257D
                                                        Board                                         Data                                                       Signal Generator

                                                                                                      25GHz
                                                                                                      CLK
                                                           Remote
                                           200Gb/s         Header                                                       Probe
        Test Board                            Data                                  Balun                               Station
                                                          DC Block
                                                  Cable
                                                                                          Keysight N1000A
                                                Probe                                     DCA-X Oscilloscope
           DC &                                                                           Keysight 86118A
           Digital
                                                                                          Sampling Module
                                                    25GHz
                                                      CLK                            ~ 6dB loss @ 50GHz from probe setup
© 2021 IEEE                                                     8.2: An Output Bandwidth Optimized 200Gb/s PAM-4 100Gb/s NRZ Transmitter with 5-Tap FFE in 28nm CMOS
International Solid-State Circuits Conference                                                                                                                                       39 of 44

---

Pulse Response and Channel Loss
                                                                                                                       0
        Normalized voltage


                                                                                                                                                                       w/o ESD




                                                                                                  Channel loss [dB]
                             1                                w/o ESD
                                                              w/ ESD                                                   -5                                              w/ ESD

                         0.5                                                                                          -10                                            -13dB* @50GHz

                                                                                                                      -15
                             0                                                                                                      -15dB* @50GHz
                                                                                                                      -20
                                 0        0.05      0.1        0.15                 0.2                                     0            20                     40        60
                                                 Time [ns]                                                                              Frequency [GHz]
                                                                                                                                *Including internal loss and
                                                                                                                                ~6dB loss from probe setup

© 2021 IEEE                                                  8.2: An Output Bandwidth Optimized 200Gb/s PAM-4 100Gb/s NRZ Transmitter with 5-Tap FFE in 28nm CMOS
International Solid-State Circuits Conference                                                                                                                                    40 of 44

---

Output Eyes w/o ESD @200/100Gb/s
       PRBS7
       Total 926mW: 4.63pJ/b @200Gb/s

                                         200Gb/s PAM-4                                                                             100Gb/s NRZ


                                                         52.9mV                                                                                                   234.4mV


                    100mV                       0.36UI      RLM=99%                                           110mV                         0.76UI
             Coarse FFE (segments): [3/18, 9/18, 6/18]                                                  Coarse FFE (segments): [3/18, 9/18, 6/18]
             Fine FFE (DAC code): [58, 127, 48]                                                         Fine FFE (DAC code): [48, 127, 38]
             Polarity: [-1, +1, -1]                                                                     Polarity: [-1, +1, -1]
© 2021 IEEE                                                8.2: An Output Bandwidth Optimized 200Gb/s PAM-4 100Gb/s NRZ Transmitter with 5-Tap FFE in 28nm CMOS
International Solid-State Circuits Conference                                                                                                                               41 of 44

---

Output Eyes w/ ESD @180/90Gb/s
       PRBS7
       Total 826mW: 4.59pJ/b @180Gb/s

                                         180Gb/s PAM-4                                                                             90Gb/s NRZ


                                                        43mV                                                                                                 243.8mV


                     75mV                       0.4UI       RLM=99%                                          150mV                         0.77UI
             Coarse FFE (segments): [3/18, 9/18, 6/18]                                                  Coarse FFE (segments): [13/18, 4/18, 1/18]
             Fine FFE (DAC code): [58, 127, 63]                                                         Fine FFE (DAC code): [117, 127, 117]
             Polarity: [-1, +1, -1]                                                                     Polarity: [+1, -1, -1]
© 2021 IEEE                                                8.2: An Output Bandwidth Optimized 200Gb/s PAM-4 100Gb/s NRZ Transmitter with 5-Tap FFE in 28nm CMOS
International Solid-State Circuits Conference                                                                                                                          42 of 44

---

Comparison Table
                                                ISSCC’18 [1] ISSCC’19 [2] ISSCC’18 [3] ISSCC’20 [4]                                                                      This work
                                                    10nm         14nm         14nm        40nm                                                                             28nm
                    Technology
                                                   FinFET       FinFET       FinFET       CMOS                                                                            CMOS
                   Architecture                  Quarter-rate Quarter-rate Quarter-rate Quarter-rate                                                                    Quarter-rate
                  Clock source                  On-chip PLL              External                    External                    External                                External
                  Output swing
                                                  0.75Vppd                  1Vppd                    0.92Vppd                    0.56Vppd                                 0.8Vppd
                    w/o FFE
                      FFE                          3-tap                    3-tap                       8-tap                       8-tap                                  5-tap
                ESD protection                        Yes                    Yes                         Yes                          No                          No                 Yes
                      Signaling                 PAM-4 NRZ PAM-4 NRZ PAM-4 NRZ                                                        NRZ                PAM-4 NRZ PAM-4 NRZ
               Data rate (Gb/s)                 112         56        128            64           112            56                  100                  200           100    180         90
             Efficiency (pJ/bit)*               1.72    3.44           1.3           2.7           2.6           5.2                 6.19                 4.63          9.26   4.59    9.18
               Eye height (mV)                   30     260         100** 240**                   90**        170**                   73                   53           234     43     244
           Active area (mm2)       0.0302         0.048                                                0.095                       0.504                                   0.432
          *Excluding PLL, ** Estimated from eye diagram
© 2021 IEEE                                                      8.2: An Output Bandwidth Optimized 200Gb/s PAM-4 100Gb/s NRZ Transmitter with 5-Tap FFE in 28nm CMOS
International Solid-State Circuits Conference                                                                                                                                                   43 of 44

---

Conclusion
       A 200Gb/s PAM-4 transmitter with 5-tap FFE is designed
        and verified in a 28nm planar CMOS technology.
       Key features to improve output bandwidth and output swing
                Minimized driver capacitance with pull-up current sources
                Multiplexing with flexible clock timing control
                Employing a fully reconfigurable 5-tap FFE architecture

       The test chip achieves eye opening with 52.9mV eye height,
        0.36UI eye width, and 99% RLM under 6dB channel.
© 2021 IEEE                                     8.2: An Output Bandwidth Optimized 200Gb/s PAM-4 100Gb/s NRZ Transmitter with 5-Tap FFE in 28nm CMOS
International Solid-State Circuits Conference                                                                                                          44 of 44

---

An 8b DAC-based SST TX using metal gate
     resistors with 1.4pJ/b efficiency at 112Gb/s
         PAM4 and 8-taps FFE in 7nm CMOS
                         Marcel Kossel1, Vishal Khatri1,4, Matthias Braendli1,
            Pier Andrea Francese1, Thomas Morf1, Serdar Yonar1, Mridula Prathapan1, Eric
                                 Lukes2, Ray Richetta2, Carrie Cox3,
                                                  1IBM Research, Rüschlikon, Switzerland

                                                2IBM Systems and Technology, Rochester, MN

                                                 3IBM Systems and Technology, Durham, NC
                                         4Now with Samsung Semiconductor India Research, Bangalore

© 2021 IEEE                                          8.3: An 8b DAC-based SST TX using metal gate resistors with 1.4pJ/b efficiency at 112Gb/s PAM4 and 8-taps FFE in 7nm CMOS
International Solid-State Circuits Conference                                                                                                                                    1 of 37

---

Outline
               • Motivation
               • Transmitter Architecture
               • Circuit Implementation
                         – DSP Topology
                         – DAC Segmentation
                         – Metal Gate Poly Silicon Resistor
               • Measured Results
               • Comparison and Conclusions

© 2021 IEEE                                     8.3: An 8b DAC-based SST TX using metal gate resistors with 1.4pJ/b efficiency at 112Gb/s PAM4 and 8-taps FFE in 7nm CMOS
International Solid-State Circuits Conference                                                                                                                               2 of 37

---

Motivation
                                                FFE implementation                                              Tap length                               NRZ/PAM4 support


         Analog-based TX                        full-rate output stage                                           short (<4)                                      demanding


         DSP/DAC TX                              sub-rate DSP                                                    long (>4)                                   straightforward



                   This work chose a DAC TX architecture to address 112 Gb/s because of
                   the long FFE tap length and the different modulation format support.


© 2021 IEEE                                       8.3: An 8b DAC-based SST TX using metal gate resistors with 1.4pJ/b efficiency at 112Gb/s PAM4 and 8-taps FFE in 7nm CMOS
International Solid-State Circuits Conference                                                                                                                                  3 of 37

---

Concept drawing of DAC TX




© 2021 IEEE                                     8.3: An 8b DAC-based SST TX using metal gate resistors with 1.4pJ/b efficiency at 112Gb/s PAM4 and 8-taps FFE in 7nm CMOS
International Solid-State Circuits Conference                                                                                                                               4 of 37

---

FFE calculation in DSP




© 2021 IEEE                                     8.3: An 8b DAC-based SST TX using metal gate resistors with 1.4pJ/b efficiency at 112Gb/s PAM4 and 8-taps FFE in 7nm CMOS
International Solid-State Circuits Conference                                                                                                                               5 of 37

---

Lookup table (LUT) based FFE (1)




     [1] T. Toifl, et al., "A 0.3pJ/Bit 112GB/S PAM4 1+0.5D TX-DFE Precoder and 8-Tap FFE in 14nm CMOS," IEEE Symp. VLSI Circuits, pp. 53-54, Jun. 2018.
© 2021 IEEE                                     8.3: An 8b DAC-based SST TX using metal gate resistors with 1.4pJ/b efficiency at 112Gb/s PAM4 and 8-taps FFE in 7nm CMOS
International Solid-State Circuits Conference                                                                                                                               6 of 37

---

LUT based FFE (2)




© 2021 IEEE                                     8.3: An 8b DAC-based SST TX using metal gate resistors with 1.4pJ/b efficiency at 112Gb/s PAM4 and 8-taps FFE in 7nm CMOS
International Solid-State Circuits Conference                                                                                                                               7 of 37

---

FFE implemented in DSP

                                                                                                                                        • DSP synthesized netlist
                                                                                                                                           => runs at 1/32-rate
                                                                                                                                        • 4 LUT logic banks:
                                                                                                                                             -> NRZ 16 taps
                                                                                                                                             -> PAM4 8 taps
                                                                                                                                        • LUT performs 4b lookup
                                                                                                                                        • LUT logic is gatable
                                                                                                                                        • Correction adder is 4
                                                                                                                                                 (i.e., 4 x 0.5 for 50% 1s complement
                                                                                                                                                  look-up errors + 2 for round-half-up
                                                                                                                                                  when cutting off 2 LSBs)



© 2021 IEEE                                     8.3: An 8b DAC-based SST TX using metal gate resistors with 1.4pJ/b efficiency at 112Gb/s PAM4 and 8-taps FFE in 7nm CMOS
International Solid-State Circuits Conference                                                                                                                                     8 of 37

---

DAC segmentation




© 2021 IEEE                                     8.3: An 8b DAC-based SST TX using metal gate resistors with 1.4pJ/b efficiency at 112Gb/s PAM4 and 8-taps FFE in 7nm CMOS
International Solid-State Circuits Conference                                                                                                                               9 of 37

---

Parameter Space
       • Objective: Reduce the number of DAC segments
                                                                                                                                                                            Clock loading
         to save clocking power while maintaining linearity                                                                                                                 depends on
                                                                                                                                                                            segmentation
                                                                                                                                                                            option chosen
                                                                                                               32:4 Serializer




       DAC segmentation options: Parallel driver slices ↔ Scaling of Rout
© 2021 IEEE                                     8.3: An 8b DAC-based SST TX using metal gate resistors with 1.4pJ/b efficiency at 112Gb/s PAM4 and 8-taps FFE in 7nm CMOS
International Solid-State Circuits Conference                                                                                                                                        10 of 37

---

Binary to Linear Scaling
   a)

                                                                                                     Good linearity but large fanout spread
                                                                                                      between MSB and LSB DAC weights

                                                fanout w.r.t. serializer loading
   b)


                                                                                                 Converting 2b binary MSBs into 3b linear
                                                                                                  reduces fanout spread by 2x and
                                                                                                  improves linearity in unsigned mode
© 2021 IEEE                                                 8.3: An 8b DAC-based SST TX using metal gate resistors with 1.4pJ/b efficiency at 112Gb/s PAM4 and 8-taps FFE in 7nm CMOS
International Solid-State Circuits Conference                                                                                                                                           11 of 37

---

Further Segment Count Reduction
   c)




                                                 Moving up reference to weight w8 while
                                                 scaling smaller weights via driver resistor
   d)



                                                                                                 A/B-slice concept: Linearity depends
                                                                                                  on the matching of 2 resistors only

© 2021 IEEE                                       8.3: An 8b DAC-based SST TX using metal gate resistors with 1.4pJ/b efficiency at 112Gb/s PAM4 and 8-taps FFE in 7nm CMOS
International Solid-State Circuits Conference                                                                                                                                 12 of 37

---

Linearity Tuning
                                                                                     PVT tuning per
                                                                                      DAC-weight for
                                                                                      better linearity




© 2021 IEEE                                     8.3: An 8b DAC-based SST TX using metal gate resistors with 1.4pJ/b efficiency at 112Gb/s PAM4 and 8-taps FFE in 7nm CMOS
International Solid-State Circuits Conference                                                                                                                               13 of 37

---

32:4 Serializer and Skew Buffers




© 2021 IEEE                                     8.3: An 8b DAC-based SST TX using metal gate resistors with 1.4pJ/b efficiency at 112Gb/s PAM4 and 8-taps FFE in 7nm CMOS
International Solid-State Circuits Conference                                                                                                                               14 of 37

---

32:4 Serializer




                                                1.75GHz              3.5GHz                              7GHz                                14GHz




[2] C. Menolfi et al., "A 112Gb/S 2.6pJ/b 8-Tap FFE PAM-4 SST TX in 14nm CMOS," ISSCC, pp. 104-106, 3 Feb. 2018.
© 2021 IEEE                                        8.3: An 8b DAC-based SST TX using metal gate resistors with 1.4pJ/b efficiency at 112Gb/s PAM4 and 8-taps FFE in 7nm CMOS
International Solid-State Circuits Conference                                                                                                                                  15 of 37

---

Skew Buffers
       Skew buffers help mitigate MSB-to-LSB delay spread
        caused by the different loading of driver slices

                                                         τ1




                                                 τ2




© 2021 IEEE                                     8.3: An 8b DAC-based SST TX using metal gate resistors with 1.4pJ/b efficiency at 112Gb/s PAM4 and 8-taps FFE in 7nm CMOS
International Solid-State Circuits Conference                                                                                                                               16 of 37

---

4:1 MUX Timing
    De-skewing by skew buffers:                                                               Ideal 4:1 MUX timing:




© 2021 IEEE                                     8.3: An 8b DAC-based SST TX using metal gate resistors with 1.4pJ/b efficiency at 112Gb/s PAM4 and 8-taps FFE in 7nm CMOS
International Solid-State Circuits Conference                                                                                                                               17 of 37

---

Driver slices




© 2021 IEEE                                     8.3: An 8b DAC-based SST TX using metal gate resistors with 1.4pJ/b efficiency at 112Gb/s PAM4 and 8-taps FFE in 7nm CMOS
International Solid-State Circuits Conference                                                                                                                               18 of 37

---

Driver Slice
    Driver slice includes: 1-UI clock pulse generator, 4:1 mux, output driver




© 2021 IEEE                                     8.3: An 8b DAC-based SST TX using metal gate resistors with 1.4pJ/b efficiency at 112Gb/s PAM4 and 8-taps FFE in 7nm CMOS
International Solid-State Circuits Conference                                                                                                                               19 of 37

---

1-UI Clock Pulse Generators
    DPL implementation better suited for high speed because of symmetrical
     clock phase loading (at the cost of an increased capacitive load)




   Example shows 1-UI clock pulse generation for carving 1/4-rate data D4<0> with PSEL<0> and NSEL<0>
© 2021 IEEE                                     8.3: An 8b DAC-based SST TX using metal gate resistors with 1.4pJ/b efficiency at 112Gb/s PAM4 and 8-taps FFE in 7nm CMOS
International Solid-State Circuits Conference                                                                                                                               20 of 37

---

Metal Gate Poly Silicon (pc) Resistor
                      Exemplary pc res:
                                                    6 parallel poly stripes
                                                    IN                                                            1: FEOL part (poly res)
                                                        1                                                         2: BEOL part (Mx res)
                                                                2
                                                                                                                  - EM specs: #parallel pc stripes
                                                                2
                                                                                                                  - Res value: variation of pc length
                                                              1
                                                                                              OUT
                                                                                                                 (Diffusion and fins not shown)

o     PC resistor has 1.8x higher current carrying capability (Irms) than rmres of the same
      width at the chosen design point
o No special process layer used to build pc resistors
© 2021 IEEE                                     8.3: An 8b DAC-based SST TX using metal gate resistors with 1.4pJ/b efficiency at 112Gb/s PAM4 and 8-taps FFE in 7nm CMOS
International Solid-State Circuits Conference                                                                                                                               21 of 37

---

Application of PC Resistors
       PC resistors enable a seamless integration into regular CMOS style layouts




                                                                                                                                                    10%




© 2021 IEEE                                     8.3: An 8b DAC-based SST TX using metal gate resistors with 1.4pJ/b efficiency at 112Gb/s PAM4 and 8-taps FFE in 7nm CMOS
International Solid-State Circuits Conference                                                                                                                               22 of 37

---

Clock Path Design




© 2021 IEEE                                     8.3: An 8b DAC-based SST TX using metal gate resistors with 1.4pJ/b efficiency at 112Gb/s PAM4 and 8-taps FFE in 7nm CMOS
International Solid-State Circuits Conference                                                                                                                               23 of 37

---

Clock Path




                                                Synchronized divider                                               Clock receiver with quadrature
                                                                                                                   signal generation
© 2021 IEEE                                      8.3: An 8b DAC-based SST TX using metal gate resistors with 1.4pJ/b efficiency at 112Gb/s PAM4 and 8-taps FFE in 7nm CMOS
International Solid-State Circuits Conference                                                                                                                                24 of 37

---

Quadrature Error Correction (QEC)
        QEC performed in DIV2 via lead/lag delay in CML load:




© 2021 IEEE                                     8.3: An 8b DAC-based SST TX using metal gate resistors with 1.4pJ/b efficiency at 112Gb/s PAM4 and 8-taps FFE in 7nm CMOS
International Solid-State Circuits Conference                                                                                                                               25 of 37

---

Duty Cycle Correction (DCC)
     DCC: source/sink current into trip point of CML-to-CMOS inverter




    Blue: implemented on test chip
© 2021 IEEE                                     8.3: An 8b DAC-based SST TX using metal gate resistors with 1.4pJ/b efficiency at 112Gb/s PAM4 and 8-taps FFE in 7nm CMOS
International Solid-State Circuits Conference                                                                                                                               26 of 37

---

Schematic of implemented DAC TX




© 2021 IEEE                                     8.3: An 8b DAC-based SST TX using metal gate resistors with 1.4pJ/b efficiency at 112Gb/s PAM4 and 8-taps FFE in 7nm CMOS
International Solid-State Circuits Conference                                                                                                                               27 of 37

---

Layout of DAC TX in 7nm CMOS

                                                                                                                              A: DSP: 120 x 120 µm2
                                                                                                                              B: Data Path: 51 x 39 µm2
                                                                                                                              C: Clock Path: 50 x 16 µm2
                                                                                                                              D: T-coil/ESD: 215 x 72 µm2
                                                                                                                              Active area: A+B+C = 0.017 mm2

                                                                                                                              Total area: A+B+C+D = 0.032 mm2




© 2021 IEEE                                     8.3: An 8b DAC-based SST TX using metal gate resistors with 1.4pJ/b efficiency at 112Gb/s PAM4 and 8-taps FFE in 7nm CMOS
International Solid-State Circuits Conference                                                                                                                               28 of 37

---

Lab Characterization


© 2021 IEEE                                     8.3: An 8b DAC-based SST TX using metal gate resistors with 1.4pJ/b efficiency at 112Gb/s PAM4 and 8-taps FFE in 7nm CMOS
International Solid-State Circuits Conference                                                                                                                               29 of 37

---

Measurement Setup




© 2021 IEEE                                     8.3: An 8b DAC-based SST TX using metal gate resistors with 1.4pJ/b efficiency at 112Gb/s PAM4 and 8-taps FFE in 7nm CMOS
International Solid-State Circuits Conference                                                                                                                               30 of 37

---

FFE Optimization for NRZ/PAM4
     Exemplary                                                                                                                          PAM4 at 112 Gb/s (PRBS7)
     deconvolution                                                                                                                      6.02 dB pre-emphasis (8 FFE taps)

     at 56 GBd
                                                                                                                                                                       59 mV
                                                                                                                                                9ps
                                                                                                                                     RLM=96.5%                                              Level mismatch
    Sampled scope                                                                                                                            7.0 GHz x 8→ 56 GBd                            ratio (RLM): 96.5%
    data processed
    with Octave                                                     FFT impulse response                                                NRZ at 56 Gb/s (PRBS7)
                                                                                                                                        6.12 dB pre-emphasis


                                                                    Pre-emphasis at
                                                                    fNyquist: ~6dB
                                                                               freq.  28GHz
                                                                                                                                            TJ(1E-12)=6.09ps
  pink: unequalized,                                                  channel: 0.5m RF cable
  blue: equalized
                                                Normalized single bit response
                                                                       10 UI
© 2021 IEEE                                                     8.3: An 8b DAC-based SST TX using metal gate resistors with 1.4pJ/b efficiency at 112Gb/s PAM4 and 8-taps FFE in 7nm CMOS
International Solid-State Circuits Conference                                                                                                                                                            31 of 37

---

Efficiency and Jitter Measurements


                                                 ∅1.36pJ/b @ 0.9V




                                                                                             Wafer FF

                                                1.40pJ/b @ 112Gb/s



                                                                                           Oscilloscope (Agilent Infiniium DCA-J 86100C) allowed jitter measurements only in NRZ mode.


© 2021 IEEE                                            8.3: An 8b DAC-based SST TX using metal gate resistors with 1.4pJ/b efficiency at 112Gb/s PAM4 and 8-taps FFE in 7nm CMOS
International Solid-State Circuits Conference                                                                                                                                      32 of 37

---

Eye Diagram Sweeps and Linearity




                                                                                                                                                                      -0.82/+0.67b INL




                                                                                                                                                                      -0.21/+0.41b DNL

                                                                                                                                                                      Wafer SF



© 2021 IEEE                                     8.3: An 8b DAC-based SST TX using metal gate resistors with 1.4pJ/b efficiency at 112Gb/s PAM4 and 8-taps FFE in 7nm CMOS
International Solid-State Circuits Conference                                                                                                                                            33 of 37

---

Measurements with ISI-Board




© 2021 IEEE                                     8.3: An 8b DAC-based SST TX using metal gate resistors with 1.4pJ/b efficiency at 112Gb/s PAM4 and 8-taps FFE in 7nm CMOS
International Solid-State Circuits Conference                                                                                                                               34 of 37

---

Comparison and Power Breakdown




© 2021 IEEE                                     8.3: An 8b DAC-based SST TX using metal gate resistors with 1.4pJ/b efficiency at 112Gb/s PAM4 and 8-taps FFE in 7nm CMOS
International Solid-State Circuits Conference                                                                                                                               35 of 37

---

Conclusions
         DAC TX in 7nm for NRZ/PAM4 at up to 112 Gb/s

         Circuit design features:
          Table-based FFE with LUT logic gating
          DAC slice scaling optimized to reduce C4 clocking power
          PC resistors for seamless integration into CMOS style layout

         Performance highlights:
          1.4 pJ/b energy efficiency at 112 Gb/s PAM4 and VDD=0.96V
          Small area: 0.032mm2

© 2021 IEEE                                     8.3: An 8b DAC-based SST TX using metal gate resistors with 1.4pJ/b efficiency at 112Gb/s PAM4 and 8-taps FFE in 7nm CMOS
International Solid-State Circuits Conference                                                                                                                               36 of 37

---

A 116Gb/s DSP based Wireline Transceiver in
                7nm CMOS achieving 6pJ/bit at 45dB Loss in
                   PAM-4/Duo-PAM-4 and 52dB in PAM-2
    Marc-Andre LaCroix, Euhan Chong, Weilun Shen, Ehud Nir, Faisal Ahmed Musa, Haitao Mei,
    Mohammad-Mahdi Mohsenpour, Semyon Lebedev, Babak Zamanlooy, Carlos Carvalho, Qian
    Xin, Dmitry Petrov, Henry Wong, Huong Ho, Yang Xu, Sina Naderi Shahi, Peter Krotnev,
    Chris Feist, Howard Huang, Davide Tonietto
                                                Huawei Canada Research Center
                                                       Ottawa, Ontario
© 2021 IEEE                                      8.4 : A 116Gb/s DSP-Based Wireline Transceiver in 7nm CMOS Achieving 6pJ/b at 45dB Loss in PAM-4/Duo-PAM-4 and 52dB in PAM-2
International Solid-State Circuits Conference                                                                                                                                   1 of 44

---

Self Introduction




      •        Marc-Andre LaCroix
      •        B.Sc.Eng. from University of New-Brunswick, NB, Canada, in 2000
      •        M.A.Sc. from Carleton University, ON, Canada, in 2002
      •        Since 2011 has been with Huawei Technologies Canada
      •        Prior to joining Huawei he held positions at Gennum Corp,
               STMicroelectronics, and Nortel.
© 2021 IEEE                                     8.4 : A 116Gb/s DSP-Based Wireline Transceiver in 7nm CMOS Achieving 6pJ/b at 45dB Loss in PAM-4/Duo-PAM-4 and 52dB in PAM-2
International Solid-State Circuits Conference                                                                                                                                  2 of 44

---

Outline
         •        Introduction and background
         •        Goals and Architecture Overview
         •        Clocking Generation and Distribution
         •        TX
         •        RX
         •        Measurements
         •        Conclusions




© 2021 IEEE                                     8.4 : A 116Gb/s DSP-Based Wireline Transceiver in 7nm CMOS Achieving 6pJ/b at 45dB Loss in PAM-4/Duo-PAM-4 and 52dB in PAM-2
International Solid-State Circuits Conference                                                                                                                                  3 of 44

---

Outline
         •        Introduction and background
         •        Goals and Architecture Overview
         •        Clocking Generation and Distribution
         •        TX
         •        RX
         •        Measurements
         •        Conclusions




© 2021 IEEE                                     8.4 : A 116Gb/s DSP-Based Wireline Transceiver in 7nm CMOS Achieving 6pJ/b at 45dB Loss in PAM-4/Duo-PAM-4 and 52dB in PAM-2
International Solid-State Circuits Conference                                                                                                                                  4 of 44

---

Applications For This Work

                                                                                                                                                                                  
                                                  
                                                                                                                                                                                
                                                  

                                                                                                                                                                                  
© 2021 IEEE                                        8.4 : A 116Gb/s DSP-Based Wireline Transceiver in 7nm CMOS Achieving 6pJ/b at 45dB Loss in PAM-4/Duo-PAM-4 and 52dB in PAM-2
International Solid-State Circuits Conference                                                                                                                                         5 of 44

---

“Fun” Facts: Harsh Environments
                                                •   Exceed target performance in the harshest of environments
                                                •   Calibrate once, at any temperature or supply and work forever
                                                •   Don’t expect “clean” power supplies
                                                •   Lifetime 10yrs +

                                                                  Temperature
       Canadian Winter




                                                                                                                                                       1V/m                            DC
                                                                                                                     +5%                               s                                AC
                                                                                 Supply                    Calibrate                                                                        2
                                                                                                                                                                                            %
                                                                                                                     -5%

© 2021 IEEE                                             8.4 : A 116Gb/s DSP-Based Wireline Transceiver in 7nm CMOS Achieving 6pJ/b at 45dB Loss in PAM-4/Duo-PAM-4 and 52dB in PAM-2
International Solid-State Circuits Conference                                                                                                                                                   6 of 44

---

Passive Channel @ 112Gbps
                     0
                                                                                                                                0
                                                                                         Thru
                   -10                                                                                                                                                                              Thru
                                                                                         Xtalk PS                             -10                                                                   Xtalk PS
                   -20
                                                                                                                              -20
                                                                             IL=~40dB                                                                                                       IL=~26dB
  Amplitude (dB)




                   -30




                                                                                                             Amplitude (dB)
                                                                                                                              -30
                   -40           ICN~=1.9mV                                                                                                 ICN~=2.2mV
                                                                                                                              -40
                   -50                                                                                                        -50
                   -60
                                                                             28GHz                                            -60                                                           28GHz
                   -70                                                                                                        -70
                         0   5         10       15      20        25         30          35          40                             0   5         10     15          20         25          30    35           40
                                                Frequency (GHz)                                                                                          Frequency (GHz)



         • Backplane                                                                                        • Host Interface
                         − Very large total IL                                                                                  − ASIC PKG contributes for 50% IL
                         − ASIC PKG contributes for 30% IL                                                                      − high Xtalk NEXT and FEXT
                         − Significant Xtalk due mainly to NEXT                                                                 − ILD due to discontinuities
© 2021 IEEE                                                  8.4 : A 116Gb/s DSP-Based Wireline Transceiver in 7nm CMOS Achieving 6pJ/b at 45dB Loss in PAM-4/Duo-PAM-4 and 52dB in PAM-2
International Solid-State Circuits Conference                                                                                                                                                                       7 of 44

---

Latency
         • AI ASICs require relatively low latency serial links (~10-20ns)
         • Cannot rely on FEC or CDRs
                  − Conventional KP FEC latency ~100ns,
                  − CDRs at least doubles latency and power of a serial link
                  − Power, area or cost overhead for both options are prohibitive
         • Requirements:
                  − 50+Gbps
                  − BER<<1E-15
                  − No FEC, No CDRs

                                                                                       140-240ns                                                                        10-20ns

© 2021 IEEE                                     8.4 : A 116Gb/s DSP-Based Wireline Transceiver in 7nm CMOS Achieving 6pJ/b at 45dB Loss in PAM-4/Duo-PAM-4 and 52dB in PAM-2
International Solid-State Circuits Conference                                                                                                                                     8 of 44

---

Performance Margin and Cost
         • System performance much more sensitive than @ 50Gbps
         • More margin is required to cope with:
                  − Passive channel manufacturing variation and aging
                  − CMOS process spread & aging
                  − Channel discontinuities
                  − Higher crosstalk in package breakout & connectors
         • Higher cost of new materials, connectors, cables, CDRs
                  − Some products cannot afford to use best materials or CDRs on each link
                  − 10-20% materials performance improvement comes at 2X the cost



© 2021 IEEE                                         8.4 : A 116Gb/s DSP-Based Wireline Transceiver in 7nm CMOS Achieving 6pJ/b at 45dB Loss in PAM-4/Duo-PAM-4 and 52dB in PAM-2
International Solid-State Circuits Conference                                                                                                                                      9 of 44

---

Outline
         •        Introduction and background
         •        Goals and Architecture Overview
         •        Clocking Generation and Distribution
         •        TX
         •        RX
         •        Measurements
         •        Conclusions




© 2021 IEEE                                     8.4 : A 116Gb/s DSP-Based Wireline Transceiver in 7nm CMOS Achieving 6pJ/b at 45dB Loss in PAM-4/Duo-PAM-4 and 52dB in PAM-2
International Solid-State Circuits Conference                                                                                                                                  10 of 44

---

Overall Goals
         •          Goals in realistic, high volumes, long term conditions:
                  1.         112Gbps PAM4, BER <<1E-5 @ 40dB IL (<<1E-15 post-FEC)
                  2.         56Gbps NRZ, BER <1E-15 @ 40dB IL
                  3.         <6pJ/bit power efficiency on worst case channels
                  4.         ~25% power scaling from worst to best backplane or to module host link
                  5.         Negligible yield loss on largest lane count ASIC over all process spread




© 2021 IEEE                                     8.4 : A 116Gb/s DSP-Based Wireline Transceiver in 7nm CMOS Achieving 6pJ/b at 45dB Loss in PAM-4/Duo-PAM-4 and 52dB in PAM-2
International Solid-State Circuits Conference                                                                                                                                  11 of 44

---

Approach
         •          Key Strategies:
                  − High performance DSP based architecture with extensive power/performance
                    scaling capability
                  − Sensor network measuring P-V-T in the background
                  − Statistical Unit (SU) measures figures of merit and channel conditions
                  − Dynamic Performance Controller (DPC) adapts power/performance trade-off
                  − Calibration and adaptation algorithms developed using high volume, realistic
                    stress testing




© 2021 IEEE                                     8.4 : A 116Gb/s DSP-Based Wireline Transceiver in 7nm CMOS Achieving 6pJ/b at 45dB Loss in PAM-4/Duo-PAM-4 and 52dB in PAM-2
International Solid-State Circuits Conference                                                                                                                                  12 of 44

---

System Architecture
         •        8 Transceiver lanes
                  •         7b 58GS/s ADC
                  •         7b 58GS/s DAC
                  •         DSP
         •        Central clock generation
         •        Dynamic performance
                  controller
         •        Paired with 112G FEC

                                                Sense
                                                Control


© 2021 IEEE                                         8.4 : A 116Gb/s DSP-Based Wireline Transceiver in 7nm CMOS Achieving 6pJ/b at 45dB Loss in PAM-4/Duo-PAM-4 and 52dB in PAM-2
International Solid-State Circuits Conference                                                                                                                                      13 of 44

---

Analog
         • Sensing
                  • Per Lane P-V-T sensors
                  • ASAR conversion time
                  • Various voltage test points.


         • Control elements
                  •         ADC resolution (7b2b)
                  •         LDO Voltages(Rx,Tx, Clocking)
                  •         AFE + T&H sub-system bias
                  •         TX Swing


© 2021 IEEE                                     8.4 : A 116Gb/s DSP-Based Wireline Transceiver in 7nm CMOS Achieving 6pJ/b at 45dB Loss in PAM-4/Duo-PAM-4 and 52dB in PAM-2
International Solid-State Circuits Conference                                                                                                                                  14 of 44

---

DSP
         •        DSP can process PAM-4
                  or Duo-PAM-4
         •        Duo-PAM-4 can improve
                  link margin under right
                  conditions




                                                   Data Path
                                                   Sense
                                                   Control
© 2021 IEEE                                     8.4 : A 116Gb/s DSP-Based Wireline Transceiver in 7nm CMOS Achieving 6pJ/b at 45dB Loss in PAM-4/Duo-PAM-4 and 52dB in PAM-2
International Solid-State Circuits Conference                                                                                                                                  15 of 44

---

Duo-PAM4 – Reduce Channel BW
                      112.5Gb/s PAM-4
          1                                              2 Shape total channel response to 1+D.                                          3 Power Spectrum of signal
                  Transmitted down the line                                         Null at Nyquist.                                                contained in ~1/2 BW

                                                                                           1
                                                                                                  α=1


                                                                                                                                                               fNyq
                     fNyq                2xfNyq                                                                                                       fNyq/2
                                                                                                                                                   PAM4 * (1+D)  7-levels
               112Gb/s PAM-4 Power
             Power spectral density (PSD)
                       at TX.                                                                   fNyq
                                                            H(s)

                                                                                                                           3

                  Encoding
                                                                                     2                                                                             MOD4 recovers PAM-4
                                                           1                                                             6-slicers                                  from slicer outputs
© 2021 IEEE                                       8.4 : A 116Gb/s DSP-Based Wireline Transceiver in 7nm CMOS Achieving 6pJ/b at 45dB Loss in PAM-4/Duo-PAM-4 and 52dB in PAM-2
International Solid-State Circuits Conference                                                                                                                                       16 of 44

---

Outline
         •        Introduction and background
         •        Goals and Architecture Overview
         •        Clocking Generation and Distribution
         •        TX
         •        RX
         •        Measurements
         •        Conclusions




© 2021 IEEE                                     8.4 : A 116Gb/s DSP-Based Wireline Transceiver in 7nm CMOS Achieving 6pJ/b at 45dB Loss in PAM-4/Duo-PAM-4 and 52dB in PAM-2
International Solid-State Circuits Conference                                                                                                                                  17 of 44

---

Clock Generation



         •        Central generation with distribution to all TRX within the macro.
         •        Includes 2 LC-PLLs.
                  − Allows simultaneous operation at 2 independent data-rates
         •        Each PLL can generate any frequency between 14GHz - 29GHz.
         •        Wide frequency range, without holes, is achieved by:
                  − Two LC-VCO cores per PLL that achieve ~40% combined tuning range.
                  − Range is extended by using an optional fixed fractional divider
                  − Fractional synthesis
         •        Total solution supports data-rates between 8-116Gb/s
© 2021 IEEE                                     8.4 : A 116Gb/s DSP-Based Wireline Transceiver in 7nm CMOS Achieving 6pJ/b at 45dB Loss in PAM-4/Duo-PAM-4 and 52dB in PAM-2
International Solid-State Circuits Conference                                                                                                                                  18 of 44

---

Clock distribution
         •        Differential standing wave T-Lines
         •        14-29GHz pass band
         •        Open drain CML drivers
         •        Capacitor bank for Frequency tuning
                  − Provides extra coverage (Optional).
         •        Includes amplitude control
         •        Low overall power consumption
         •        Effective noise filtering
                  − <100fs-rms Rj at TX output




© 2021 IEEE                                     8.4 : A 116Gb/s DSP-Based Wireline Transceiver in 7nm CMOS Achieving 6pJ/b at 45dB Loss in PAM-4/Duo-PAM-4 and 52dB in PAM-2
International Solid-State Circuits Conference                                                                                                                                  19 of 44

---

Clock distribution (II)

                                                                                                                              Lane[n+1]                                         Lane[n]



                                                                                                                                  TX[n+1]                         Tap Point 2   TX[n]




                                                                                                                                  RX[n+1]                         Tap Point 1   RX[n]



                                                             Minimum requirement



© 2021 IEEE                                     8.4 : A 116Gb/s DSP-Based Wireline Transceiver in 7nm CMOS Achieving 6pJ/b at 45dB Loss in PAM-4/Duo-PAM-4 and 52dB in PAM-2
International Solid-State Circuits Conference                                                                                                                                     20 of 44

---

Outline
         •        Introduction and background
         •        Goals and Architecture Overview
         •        Clocking Generation and Distribution
         •        TX
         •        RX
         •        Measurements
         •        Conclusions




© 2021 IEEE                                     8.4 : A 116Gb/s DSP-Based Wireline Transceiver in 7nm CMOS Achieving 6pJ/b at 45dB Loss in PAM-4/Duo-PAM-4 and 52dB in PAM-2
International Solid-State Circuits Conference                                                                                                                                  21 of 44

---

Transmitter
           • Data Path
                    − 7b binary weighted 58Gs/s DAC
                    − 2:1 final mux
           • Clock Path
                    − Clock selector is resonant
                    − Large signal into CMOS chain at
                      29GHz.
                    − Duty cycle control on ½ rate clock.
                    − Delay control on ¼ rate clocks
                      used for alignment with ½ rate.
           • TX-FIR implemented in DSP



© 2021 IEEE                                     8.4 : A 116Gb/s DSP-Based Wireline Transceiver in 7nm CMOS Achieving 6pJ/b at 45dB Loss in PAM-4/Duo-PAM-4 and 52dB in PAM-2
International Solid-State Circuits Conference                                                                                                                                  22 of 44

---

DAC Driver
         •      Bit-3 cell is base unit
         •      Higher bits scale by replication
         •      Scaled down cells for bits 2-0
         •      Each cell is composed of
                  − SST driver
                  − Parallel pseudo-CML driver
         • High swing CML assist is optional
         • Output amplitude of 1.2Vppd




© 2021 IEEE                                     8.4 : A 116Gb/s DSP-Based Wireline Transceiver in 7nm CMOS Achieving 6pJ/b at 45dB Loss in PAM-4/Duo-PAM-4 and 52dB in PAM-2
International Solid-State Circuits Conference                                                                                                                                  23 of 44

---

Outline
         •        Introduction and background
         •        Goals and Architecture Overview
         •        Clocking Generation and Distribution
         •        TX
         •        RX
         •        Measurements
         •        Conclusions




© 2021 IEEE                                     8.4 : A 116Gb/s DSP-Based Wireline Transceiver in 7nm CMOS Achieving 6pJ/b at 45dB Loss in PAM-4/Duo-PAM-4 and 52dB in PAM-2
International Solid-State Circuits Conference                                                                                                                                  24 of 44

---

Receiver
         •        AFE
                  − CTLE with ~22dB boost
                  − VGA has ~10dB gain range
         •        T&H system
                  − 8-way interleaved
                  − Split into Even & Odd
         • 58GS/s 7-bit ADC
                  − x8 ASAR per T&H
                  − 875MS/s
         •        Clocking
                  − DIV2 generates Quad. 14.5GHz
                  − 29G DIV2’s are mutually excl.


© 2021 IEEE                                     8.4 : A 116Gb/s DSP-Based Wireline Transceiver in 7nm CMOS Achieving 6pJ/b at 45dB Loss in PAM-4/Duo-PAM-4 and 52dB in PAM-2
International Solid-State Circuits Conference                                                                                                                                  25 of 44

---

AFE
         •        Gm-TIA topology for CTLE & VGA
         •        R1/R2 have dual purpose
                  − They lower noise
                  − Create option for coupling signal to
                    source of MP0/1
                  − MP0/1 provide extra HF gain
         •        Techniques to achieve high BW
                  − Use N & P devices of Gm-stages
                  − Pole splitting with inductor L1
                  − Boost control voltage on switches; min.
                    their size.




© 2021 IEEE                                     8.4 : A 116Gb/s DSP-Based Wireline Transceiver in 7nm CMOS Achieving 6pJ/b at 45dB Loss in PAM-4/Duo-PAM-4 and 52dB in PAM-2
International Solid-State Circuits Conference                                                                                                                                  26 of 44

---

Track & Hold
      • 8-way interleaved acquisition
      • 7.25GHz clocks with 25% duty-cycle
      • Acquisition Cycle:
               − 2-UI Track, 4-UI Hold, 2-UI Reset
      • T&H are split into Even & Odd groups
               − In a group phases are 90° (2-UI) distant
                                                                                                                                                                               No bootstrapping
               − Even & Odd are 1-UI distant                                                                                                                                   No clock boosting

      • Two input buffers, one for each group,
        provide the necessary isolation.




© 2021 IEEE                                     8.4 : A 116Gb/s DSP-Based Wireline Transceiver in 7nm CMOS Achieving 6pJ/b at 45dB Loss in PAM-4/Duo-PAM-4 and 52dB in PAM-2
International Solid-State Circuits Conference                                                                                                                                                 27 of 44

---

Track & Hold (II)


     • CDACs have 4-6UI to capture sample
       from T&H                                                                                                                              ‘B’

     • Over PVT, less than optimal alignment                                                                                          ‘A’
       may occur                                                                                                                                                               ‘C’
               − Example: Orange window VS Blue window
               − Due to changes in insertion delay difference.
               − T1–T2 not constant over PVT
     • Aligner ensures proper CDAC clock
       position over PVT
               − Aligner values are determined by calibration
© 2021 IEEE                                     8.4 : A 116Gb/s DSP-Based Wireline Transceiver in 7nm CMOS Achieving 6pJ/b at 45dB Loss in PAM-4/Duo-PAM-4 and 52dB in PAM-2
International Solid-State Circuits Conference                                                                                                                                        28 of 44

---

Outline
         •        Introduction and background
         •        Goals and Architecture Overview
         •        Clocking Generation and Distribution
         •        TX
         •        RX
         •        Measurements
         •        Conclusions




© 2021 IEEE                                     8.4 : A 116Gb/s DSP-Based Wireline Transceiver in 7nm CMOS Achieving 6pJ/b at 45dB Loss in PAM-4/Duo-PAM-4 and 52dB in PAM-2
International Solid-State Circuits Conference                                                                                                                                  29 of 44

---

Jitter Generation
                            Setup
            Cables                  Huber Suhner
                                    Sucoflex 100                                                                 CDR BW = 10MHz
         Instrument                     RTO
                                       Keysight
                                      UXR1102A
                     Configurations
              Clock                    28.125-GHz
       Scope CDR BW                 4MHz & 10-MHz
               Measurement Summary
             Rj (4MHz)                    105 fs-rms
             Rj(10MHz)                    90 fs-rms




© 2021 IEEE                                            8.4 : A 116Gb/s DSP-Based Wireline Transceiver in 7nm CMOS Achieving 6pJ/b at 45dB Loss in PAM-4/Duo-PAM-4 and 52dB in PAM-2
International Solid-State Circuits Conference                                                                                                                                         30 of 44

---

TX Eye Diagram: Normal Mode
                              Setup
             Cables                     Huber Suhner
                                        Sucoflex 100
          Instrument                        RTO
                                           Keysight
                                          UXR1102A
         EVB Material                Thunderclad 933+
       EVB Trace loss                           ~4.6dB
         at Nyquist
                       Configurations
            Temp (C)                  Room (TJ=25C)       1.009Vppd
      Data Rate (Gbps)                          116.25
            DUT FIR                              ON
       De-embedding                              On
           Scope BW                   Brick Wall@50G
           Scope EQ                              OFF
       Scope CDR BW                             ~4MHz
             Pattern                        PRBS13
                 Measurement Summary
        Amplitude (Vppd)                          1.009
© 2021 IEEE                                               8.4 : A 116Gb/s DSP-Based Wireline Transceiver in 7nm CMOS Achieving 6pJ/b at 45dB Loss in PAM-4/Duo-PAM-4 and 52dB in PAM-2
International Solid-State Circuits Conference                                                                                                                                            31 of 44

---

TX Eye Diagram: High Swing Mode
                              Setup
             Cables                     Huber Suhner
                                        Sucoflex 100
          Instrument                        RTO
                                           Keysight
                                          UXR1102A
         EVB Material                Thunderclad 933+
       EVB Trace loss                           ~4.6dB
         at Nyquist
                       Configurations
            Temp (C)                  Room (TJ=25C)       1.219Vppd
      Data Rate (Gbps)                          116.25
            DUT FIR                              ON
       De-embedding                              On
           Scope BW                   Brick Wall@50G
           Scope EQ                              OFF
       Scope CDR BW                             ~4MHz
             Pattern                        PRBS13
                 Measurement Summary
        Amplitude (Vppd)                          1.219
© 2021 IEEE                                               8.4 : A 116Gb/s DSP-Based Wireline Transceiver in 7nm CMOS Achieving 6pJ/b at 45dB Loss in PAM-4/Duo-PAM-4 and 52dB in PAM-2
International Solid-State Circuits Conference                                                                                                                                            32 of 44

---

Receiver Transfer Function
         • CTLE @ MAX Boost
         • Data for 6-parts
         • Normalized to DC gain




© 2021 IEEE                                        8.4 : A 116Gb/s DSP-Based Wireline Transceiver in 7nm CMOS Achieving 6pJ/b at 45dB Loss in PAM-4/Duo-PAM-4 and 52dB in PAM-2
International Solid-State Circuits Conference                                                                                                                                     33 of 44

---

Measurement Setup (I)
                             Setup
                                                                                                                                                                                                Uncorrelated
             Cables                  Huber Suhner                                                                                        Board w/ ICN               Aggressor                   asynchronous
                                     Sucoflex 100                                                                                        coupling from
                                                                    Example                                                                                           Entry                     Aggressors
       Total Insertion                  29 – 45dB                                                                                        Aggressors
                                                        Time domain crosstalk measurement                                                                                                       (56Gb/s NRZ)
       loss at Nyquist
      (programmable)
       Programmable                   0 – 20mVrms
         crosstalk                                                                                                                                                 Variable IL Box
         Crest factor                           10
                      Configurations
           Temp (C)                 Room (TJ=25C)
           Data Rate               112 – 116.25Gb/s
            (Gbps)
          Line Code                PAM4, DuoPAM4
             Pattern                     PRBS31




                                                                                                                                                                                      DUT EVB




© 2021 IEEE                                            8.4 : A 116Gb/s DSP-Based Wireline Transceiver in 7nm CMOS Achieving 6pJ/b at 45dB Loss in PAM-4/Duo-PAM-4 and 52dB in PAM-2
International Solid-State Circuits Conference                                                                                                                                                          34 of 44

---

Measurement Setup (II)
                                                                                                                Signal trace layer
      •        Custom crosstalk coupling board                                                                    Coupler PCB
      •        Multiple aggressor channels                                                                                                                                        Modulated
                                                                                                                                                                                       Victim
               − 0 – 20mVrms                                                                                                                                                      power supply
      •        Single victim channel
                                                                                                                                        Xtalk                                                Aggressors
                                                                                                                                        board
                                                                                                       RF switchesMeasured S21 for three
                                                                                                                                     Temperature
                                                                                                                 loss settings (38, 40, 45dB)
           [~0-7GHz]          [~7-14GHz]        [~14-21GHz]   [~21-28GHz]      [~28-35GHz]
                                                                                                                                     control hose
          5.11mV-rms          7.62mV-rms        5.75mV-rms    2.94mV-rms       1.04mV-rms




                                 Example of crosstalk spectrum                                                                         Backplane
                                    ~11mV-rms (0-35GHz)
                                                                                                        IL board                       connectors &                           DUT board
                                                                                                                                       paddle cards

© 2021 IEEE                                                   8.4 : A 116Gb/s DSP-Based Wireline Transceiver in 7nm CMOS Achieving 6pJ/b at 45dB Loss in PAM-4/Duo-PAM-4 and 52dB in PAM-2
International Solid-State Circuits Conference                                                                                                                                                             35 of 44

---

Channel Performance
                                   Crosstalk tolerance VS                                                                        BER VS Crosstalk at
                               Insertion Loss for BER < 1E-05                                                                      38dB & 40dB IL
                                                                                                                                           PAM4
                                                                                                                                           PAM4
    Crosstalk Noise (mV-rms)




                                                                                                                                             Crosstalk Noise (mV-rms)
                                                                                 *3 part average
                                                                          ~equal to median of population
© 2021 IEEE                                     8.4 : A 116Gb/s DSP-Based Wireline Transceiver in 7nm CMOS Achieving 6pJ/b at 45dB Loss in PAM-4/Duo-PAM-4 and 52dB in PAM-2
International Solid-State Circuits Conference                                                                                                                                  36 of 44

---

112Gb/s PAM-4 Bathtub Curves
                                                              PRBS31 across 40dB Channel.
                                                    3 Parts                                                                                                 1 Part



                                                ~3E-09 to 8E-09




                                                                                                                                                                   ~3E-09



                               CDR                     frozen                                                                  CDR                           frozen
                               CDR - FFE               frozen                                                                  TR-FFE                        frozen
                               DP-FFE                  active                                                                  DP-FFE                        frozen
© 2021 IEEE                                                8.4 : A 116Gb/s DSP-Based Wireline Transceiver in 7nm CMOS Achieving 6pJ/b at 45dB Loss in PAM-4/Duo-PAM-4 and 52dB in PAM-2
International Solid-State Circuits Conference                                                                                                                                             37 of 44

---

58-Gb/s NRZ Over 52dB IL

                          Measured Channel Response                                                                                              PRBS31 Bathtub curve
            0                                                                                                                  1.E-05
                                                                                                                               1.E-06
          -10
                                                                                                                               1.E-07
                                                                                      29-GHz
          -20                                                                                                                  1.E-08




                                                                                                                     Raw BER
                                                                                                                               1.E-09
                                                                                                                               1.E-10
IL (dB)




          -30

                                                                                                                               1.E-11
          -40
                                                                                                52.8dB                         1.E-12
          -50                                                                                                                  1.E-13
                                                                                                                               1.E-14
          -60
                0        5            10          15        20           25           30           35           40
                                                                                                                               1.E-15
                                                       Freq (GHz)
                                                                                                                                        -0.6        -0.4          -0.2           0           0.2   0.4   0.6
                                                                                                                                                       Sampling Clock Phase (UI)



  © 2021 IEEE                                                       8.4 : A 116Gb/s DSP-Based Wireline Transceiver in 7nm CMOS Achieving 6pJ/b at 45dB Loss in PAM-4/Duo-PAM-4 and 52dB in PAM-2
  International Solid-State Circuits Conference                                                                                                                                                                38 of 44

---

High Volume System Level Testing
         System Level Test (SLT): large sample volume test over stressed channel
         Goal: improve RVS by fine tuning FW algorithms
         Method: use automatic test stations to test hundreds of samples/day
         1. Increase Repeatability (R)
                  − Minimize calibration & adaptation run-to-run
                    variations
         2. Reduce Variability (V)
                  − Minimize lane-to-lane, part-to-part, lot-to-lot
                    variations
         3. Optimize Stability (S)
                  − Minimize sensitivity to static & dynamic voltage
                    and temperature variations and aging drift

© 2021 IEEE                                     8.4 : A 116Gb/s DSP-Based Wireline Transceiver in 7nm CMOS Achieving 6pJ/b at 45dB Loss in PAM-4/Duo-PAM-4 and 52dB in PAM-2
International Solid-State Circuits Conference                                                                                                                                  39 of 44

---

Repeatability VS Total Variability
                     465-lanes across 31 parts; 4-lanes on single part x 180 repetitions
                               Setup                       Variation over the set
                                                                                                                LANE-0                        LANE-2                     LANE-4            LANE-6
        Total Insertion                         ~38dB      strongly related
        loss at Nyquist
                                                           to variation in initial                                 @ This stage ADAPT solutions yield good BER
            Crosstalk                           <1mV
                                                           CAL+ADAPT solutions                                     but still too variable across repetitions.
              Temp.                       Room Temp
        Single Sample                  180 repetitions x
           (1-part)                        4 Lanes         Will improve as
                                       (CAL + ADAPT)       ADAPT is tuned to
         Multi Sample                31-parts x 4 Lanes    yield better outcomes
          (31 parts)                  x 15 repetitions
                                                           more frequently
                        Configurations
      Data Rate (Gbps)                     112.5Gb/s
           Line Code                            PAM4
             Pattern                        PRBS31
           Adaptation                      Initial only




© 2021 IEEE                                                 8.4 : A 116Gb/s DSP-Based Wireline Transceiver in 7nm CMOS Achieving 6pJ/b at 45dB Loss in PAM-4/Duo-PAM-4 and 52dB in PAM-2
International Solid-State Circuits Conference                                                                                                                                                   40 of 44

---

Power Scaling vs. Channel IL
           • Example system channel                                                                                675
                                                                                                                   655




                                                                                               Total Lane Power (mW)
             distribution
                                                                                                                   635
           • Min/Max power ratio ~ 25%
                                                                                                                   615
           • Max power @45dB: 662mW                                                                                595                                        A
           • Minimum power @ 18dB: 490mW                                                                           575
           • Scaling Strategy: BER ≤ 1E-05                                                                         555
             Examples:                                                                                             535
              A. ADC  6-bit                                                                                       515
              B. FFE  1-tap                                                                                       495
                                                                                                                          B
                                                                                                                   475
                                                                                                                         18 29 31 33 35 37 39 41 43 45
         For an example on the process & methods used refer to:
                                                                                                                           Link Insertion Loss (bump-bump) at
           M.LaCroix et al.,” A 60Gb/s PAM-4 ADC-DSP Transceiver in 7nm                                                                fbaud/2 (dB)
           CMOS with SNR-Based Adaptive Power Scaling Achieving 6.9pJ/b at
           32dB Loss,” ISSCC, pp. 114-116, Feb. 2019
© 2021 IEEE                                         8.4 : A 116Gb/s DSP-Based Wireline Transceiver in 7nm CMOS Achieving 6pJ/b at 45dB Loss in PAM-4/Duo-PAM-4 and 52dB in PAM-2
International Solid-State Circuits Conference                                                                                                                                      41 of 44

---

Die Photo & Summary Table




© 2021 IEEE                                        8.4 : A 116Gb/s DSP-Based Wireline Transceiver in 7nm CMOS Achieving 6pJ/b at 45dB Loss in PAM-4/Duo-PAM-4 and 52dB in PAM-2
International Solid-State Circuits Conference                                                                                                                                     42 of 44

---

Summary

     1. We presented a 116-Gb/s Transceiver operating reliably beyond 40dB
     2. Built to achieve the highest margin in PAM4 at 40dB can achieve up to 45dB of IL
     3. Operates at extremely low BER, in NRZ (no FEC) over 50dB channels
     4. At maximum data rate and performance power efficiency meets 6pJ/bit targets
     5. Power scaling methods enable it to reduce by 25% power consumption on easier
        channels




© 2021 IEEE                                     8.4 : A 116Gb/s DSP-Based Wireline Transceiver in 7nm CMOS Achieving 6pJ/b at 45dB Loss in PAM-4/Duo-PAM-4 and 52dB in PAM-2
International Solid-State Circuits Conference                                                                                                                                  43 of 44

---

Acknowledgements

                                        We acknowledge and thank all HiLink
                                  contributors from our System, Digital, Verification
                                              & Physical design teams.

                                   Special thanks to the HiLink Applications Team
                                  for their contributions and measurement support!



© 2021 IEEE                                      8.4 : A 116Gb/s DSP-Based Wireline Transceiver in 7nm CMOS Achieving 6pJ/b at 45dB Loss in PAM-4/Duo-PAM-4 and 52dB in PAM-2
International Solid-State Circuits Conference                                                                                                                                   44 of 44

---

A Scalable Adaptive ADC/DSP-Based
             1.25-to-56Gbps/112Gbps High-Speed Transceiver Architecture
                Using Decision-Directed MMSE CDR in 16nm and 7nm
                   Danfeng Xu1, Yu Kou1, Paul Lai1, Zichuan Cheng1, Tze Yin Cheung2, Larry Moser1, Yang Zhang1,
                 Xiaolong Liu1, Man Pio Lam1, Haikun Jia3, Quan Pan4, Wing Hong Szeto2, Chi Fai Tang2, Ka Fai Mak2,
                  Khawar Sarfraz2, Tairan Zhu1, Ming Kwan1, Emily Yim Lee Au1, Cormac Conroy1, Kai Keung Chan1

                                                                           1eTopus Technology, San Jose, CA

                                                                       2eTopus Technology, Hong Kong, China

                                                                 3Now with Tsinghua University, Beijing, China

                                            4Now with Southern University of Science and Technology, Shenzhen, China




© 2021 IEEE
International Solid-State Circuits Conference     8.5: A Scalable Adaptive ADC/DSP-Based 1.25-to-56Gb/s/112Gb/s High-Speed Transceiver Architecture Using Decision-Directed MMSE CDR in 16nm and 7nm   1 of 34

---

Danfeng Xu
         Co-founder and VP of analog design in eTopus Technology Inc.


         Industrial Experience
           25 years experience in developing analog mixed-signal and RF integrated circuits for Storage
            and Communications applications/products in Silicon Valley
           Prior to eTopus, he served as a director of Analog Design for SK Hynix Memory Solutions and
            Link-A-Media Device and a principal engineer for LSI Logic and Datapath System Inc.


         Education Background
          MS in Electrical Engineering from University of Hawaii at Manoa, Hawaii
          MS in Applied Physics from Beijing University of Posts & Telecommunication, Beijing, China
          BS degree in Electronic Engineering from University of Electronic Science & Technology of
           China, Chengdu, China

© 2021 IEEE
International Solid-State Circuits Conference   8.5: A Scalable Adaptive ADC/DSP-Based 1.25-to-56Gb/s/112Gb/s High-Speed Transceiver Architecture Using Decision-Directed MMSE CDR in 16nm and 7nm   2 of 34

---

Outline
         Background and Motivation
         Transceiver Architecture and System Design
          System architecture and Decision-Directed Minimal Mean Square Error (DD-MMSE) approach
          Clock distribution
          Receiver blocks
          Transmitter block
         Testing and Performance
         Conclusions




© 2021 IEEE
International Solid-State Circuits Conference   8.5: A Scalable Adaptive ADC/DSP-Based 1.25-to-56Gb/s/112Gb/s High-Speed Transceiver Architecture Using Decision-Directed MMSE CDR in 16nm and 7nm   3 of 34

---

Hyperscale Data Center Traffic Drives
                                                SerDes Demands for Diverse Applications
         Hyperscale data center buildouts
          Reached 541 – Q2 2020 (2x from mid-2015); 176 in pipeline
          High speed SerDes demands continue to grow
         Drives IP traffic connected to:
          Enterprise, Edge and wireless infrastructure




         SerDes applications are diverse
          Data Rate: 1-28Gb/s NRZ; 1-56Gb/s PAM-4; 1-112Gb/s PAM-4; Future 224Gb/s PAM-N
          Insertion Loss: less than 10dB to over 35dB at Nyquist Frequency
          Media: Backplane, Direct Attached Cable, Optical modules, etc.
          Temperature Range: -40oC – 125oC
© 2021 IEEE
International Solid-State Circuits Conference     8.5: A Scalable Adaptive ADC/DSP-Based 1.25-to-56Gb/s/112Gb/s High-Speed Transceiver Architecture Using Decision-Directed MMSE CDR in 16nm and 7nm   4 of 34

---

Solution:
                                                     Move Complexity into DSP/Digital

               Advanced algorithms  better BER for given SNR


               Robust DSP System
                Less complex analog implementation needed
                Operates at wide range voltage and temperature variation
                Handles high insertion loss channel


               Technology Scaling
                Moving computation into digital takes more advantage of new CMOS technology nodes
                Easy to scale ADC time interleaves for higher data rates
                Results in lower power consumption and smaller area



© 2021 IEEE
International Solid-State Circuits Conference   8.5: A Scalable Adaptive ADC/DSP-Based 1.25-to-56Gb/s/112Gb/s High-Speed Transceiver Architecture Using Decision-Directed MMSE CDR in 16nm and 7nm   5 of 34

---

DD-MMSE Approach
                      RX AFE                                                                  RX DSP
                                                Control FSM
                                                                                                                  The MMSE principle is one of the most
                                                                                                                      used approaches in optimizing a
                          ADC                                                                                         communication link
                          ADC               DEMUX                FFE                  DFE
                                                                                                                        Joint CDR and FIR adaptation provides
                                                                                                                         optimal sampling phase and better BER for all
                            CSC                                                                                          ISI conditions
                                                                       MMSE
                                                                   Adaptation, Error                                    Decision driven TED (timing error detector)
                             /2
                                                                     Generation                                          has superb quality and overcomes the
                                                                                                                         relatively long latency
                                                Timing Loop
                                                     +                     TED
                                                Clock Skew
                             PI
                                                 Correction



         [5] Jan W. M. Bergmans, “Digital Baseband Transmission and Recording” Boston, MA; Kluwer Academic, 1996
© 2021 IEEE
International Solid-State Circuits Conference        8.5: A Scalable Adaptive ADC/DSP-Based 1.25-to-56Gb/s/112Gb/s High-Speed Transceiver Architecture Using Decision-Directed MMSE CDR in 16nm and 7nm   6 of 34

---

DD-MMSE Approach (Cont.)




                                                                                                               Δ Frequency (ppm)
                                                Blind adaptation, joint CDR and FIR adaptation                                     200
                        MSE
                                                                                                                                   100

                                                                                                                                      0
                                                                                                                                          2   4     6       8       10       12       14
                                                                                                                                                                                              5
                                                       Number of UIs                                                                               Number of UIs                         10

                                                                                                                                    0.5




                                                                                                               Timing Errors
                                                                                                                                                                             For ADC0d
                        FIR Taps




                                                                                                                                      0                                      For ADC1d
                                                                                                                                                                             For ADC2d
                                                                                                                                                                             For ADC3d
                                                                                                                                   -0.5
                                                                                                                                          2   4     6       8       10       12       14
                                                                                                                                                                                              5
                                                       Number of UIs                                                                              Number of UIs                          10
                        DFE Slicer Input




                                                                                                                                    0.1




                                                                                                              Δ Phases (UI)
                                                                                                                                                                                   1d-0d
                                                                                                                                      0                                            2d-0d
                                                                                                                                                                                   3d-0d

                                                                                                                                   -0.1
                                                                                                                                          2   4     6       8       10       12       14
                                                                                                                                                                                              5
                                                       Number of UIs                                                                              Number of UIs                          10


           To demonstrate robustness, a 42dB IL channel with 3.5mVrms noise pushes up BER to 2e-2
                  Fast convergence of FIR
                  Fast acquisition for timing, and the loop maintains lock
                  Fast acquisition for phase errors to guarantee an optimal sampling phase for TI-ADC
© 2021 IEEE
International Solid-State Circuits Conference         8.5: A Scalable Adaptive ADC/DSP-Based 1.25-to-56Gb/s/112Gb/s High-Speed Transceiver Architecture Using Decision-Directed MMSE CDR in 16nm and 7nm   7 of 34

---

System Architecture


                                                                                                                                                               Background clock skew
                                                                                                                                                                correction for TI ADC
                                                                                                                                                                from DSP
                                                                                                                                                               TXPI can accept RX
                                                                                                                                                                recovered phase codes
                                                                                                                                                               Support quad and octal
                                                                                                                                                                configs




© 2021 IEEE
International Solid-State Circuits Conference   8.5: A Scalable Adaptive ADC/DSP-Based 1.25-to-56Gb/s/112Gb/s High-Speed Transceiver Architecture Using Decision-Directed MMSE CDR in 16nm and 7nm   8 of 34

---

Transceiver Clock Distribution
                                                                                    2T I/Q CLOCKS TO RX


                                                Clock Path                              0
                                                                                                      1
                                                                                                                                              Two sets of half-rate I/Q clocks are
                                                                                    CML
                                                                                     CML                                                       generated by two LC PLLs in CU
                            PLL0




                                                                                                                                              Allow different lanes to run at
                                                   CML
                                                                                    0       1     0       1                                    different speeds
                                                    CML


                                                                                                                   PLL0 CML 2T I/Q CLOCKS
                                                                                                                                              Allow RX and TX in the same lane
                                                                                                                   PLL0 CMOS 2T I/Q CLOCKS     to run at different speeds
          Common Clock Unit
                                                                                                                   PLL1 CMOS 2T I/Q CLOCKS    High frequency clock is distributed
                                                                                                                                               by CML clock path
                                                   CML
                                                    CML




                                                                                                                   PLL1 CML 2T I/Q CLOCKS

                                                                                                                                              Low speed clock is distributed by
                                                                                    0       1     0       1


                                                                                                                                               CMOS clock path
                           PLL1




                                                                                     CML
                                                                                    CML


                                                                                        0             1


                                                                                     2T I/Q CLOCKS TO TX

© 2021 IEEE
International Solid-State Circuits Conference         8.5: A Scalable Adaptive ADC/DSP-Based 1.25-to-56Gb/s/112Gb/s High-Speed Transceiver Architecture Using Decision-Directed MMSE CDR in 16nm and 7nm   9 of 34

---

Receiver Block Diagram
                                                                                                                                                                                                      AFE OFFSET CODE




                                                                        ADC Bias Block
                                                                                                      Sub-ADC 0d                                               ADC_28D
                                                                                                                                           SAR ADC
                                                                                                                                 CLK_28D
                                                                                                           Sub-ADC 2d                                  ADC_24
                                                                                                                                                             ADC_30D
                                                                                                                                  CLK_24    SAR ADC
                                                                                                                                                  SAR ADCD
                                                                                                                                        CLK_30D
                                                                                                                 Sub-ADC 1d          D
                                                                                                                                                       ADC_20ADC_26
                                                                                                                                                                   ADC_29D
                                                                                                                                            SAR ADC
                                                                                                                                  CLK_20CLK_26    SAR ADC
                                                                                                                                                       SARD ADC D
                                                                                                                                             CLK_29D
                                                 Offset DAC
                                                                        TH_Buffer                     ADC_0D
                                                                                                                       Sub-ADC 3d    D    D
                                                                                                                                                       ADC_16ADC_22ADC_25
                                                                                                                                                                        ADC_31D
                                                                                                                                                                                                      ADC_00D<6:0>
                                                                                                                                                                                                      ADC_01D<6:0>
                                                                                                                                            SAR
                                                                                                                                  CLK_16CLK_22   ADC
                                                                                                                                                  SAR ADC
                                                                                                                                             CLK_25    SARD ADC
                                                                                                                                                             SARD ADCD
                                                                                                       INPUT                                       CLK_31D                                            ADC_02D<6:0>
                                                                                                                                     D    D     D
                                      Input                                                                                                            ADC_12ADC_18ADC_21
                                                                                                            ADC_2D
                                                                                                                                                                D ADCD ADC_27D                        ADC_03D<6:0>
                                                 CTLE/PGA
                                                                 ADC                                                                        SAR
                                                                                                                                  CLK_12CLK_18    SAR ADC
                                                                                                                                                 ADC   SARD ADC
                                                                                                                                                             SAR
                        RX INPUT   Termination                                                                                               CLK_21
                                                                INPUT                                        INPUT                                 CLK_27D
                                        &                                                                                            D    D     D
                                                                                                                                                       ADC_08ADC_14ADC_17
                                   AC coupling                                         TH_Buffer                 ADC_1D                                                 ADC_23D
                                                                                                                 CLK_TH_0                   SAR
                                                                                                                                  CLK_08CLK_14   ADC
                                                                                                                                             CLK_17    SAR
                                                                                                                                                  SAR ADC D ADC
                                                                                                                                                             SARD ADCD                    ADC Data
                                    Network                                                                        INPUT                           CLK_23D
                                                                                                                      D              D    D     D                                         Alignment
                                                                                                                                                       ADC_04ADC_10ADC_13
                                                                                                                        ADC_3D              SAR  ADC                    ADC_19D
                                                                                                                        CLK_TH_2 CLK_04CLK_10     SAR ADC
                                                                                                                                             CLK_13    SARD ADC
                                                                                                                                                             SARD ADCD
                                                                                                                         INPUT                     CLK_19D                                            ADC_28D<6:0>
                                                                                                                            D        D    D     D
                                                                                                                                                       ADC_00ADC_06ADC_09
                                                                                                                                            SAR  ADC
                                                                                                                                                  SAR ADC               ADC_15D                       ADC_29D<6:0>
                                                                                                                                  CLK_00CLK_06
                                                                                                                              CLK_TH_1       CLK_09    SARD ADC
                                                                                                                                                             SARD ADCD
                                                                                                                                     D             CLK_15D                                            ADC_30D<6:0>
                                                                                           ADCCK4T_0D     ADC Pulse Gen          D        D     D
                                                                                    Td                                                                       ADC_02ADC_05
                                                                                                                                        CLK_02    SARADCCK32T_
                                                                                                                                             CLK_05   ADC
                                                                                                                                                       SAR ADC
                                                                                                                                                             SARD ADCD ADC_11D                        ADC_31D<6:0>
                                                                                                                                   CLK_TH_3D             0D
                                                                                                                                                   CLK_11D
                                                                                           ADCCK4T_2D           ADC Pulse Gen             D     D
                   2T I/Q CLOCKS                  CML                               Td                                                                             ADC_01
                                     2T CML
                                                   2             /2                                                                          CLK_01    SARADCCK32T_
                                                                                                                                                            ADC
                                                                                                                                                             SAR ADCD
                                                                                                                                                                        ADC_07D
                                      RXPI                                                                                                         CLK_07D    2D
                                                 CMOS                                      ADCCK4T_1D                 ADC Pulse Gen             D
                                                                                    Td
                                                                                                                                                                        ADC_03D
                                                                                                                                                                ADCCK32T_
                                                                                                                                                             SAR  ADC
                                                                                                                                                   CLK_03D          1D                                ADCCK32T
                                                                                           ADCCK4T_3D
                                                                                    Td                                      ADC Pulse Gen




                                                                                                                                           REFERENCE VOLTAGE
                                                                             CSC                                                                                            ADCCK32T_3D




                                                                                                                                                                ...
                                                                                                                                                                      ADC Reference DAC
                                                                                                                                                                                                       GAIN CODE
                                                                                                                                                                                                       CKSKEW CODE
                                                                                                                                                                                                       PI PHASE CODE


© 2021 IEEE
International Solid-State Circuits Conference               8.5: A Scalable Adaptive ADC/DSP-Based 1.25-to-56Gb/s/112Gb/s High-Speed Transceiver Architecture Using Decision-Directed MMSE CDR in 16nm and 7nm          10 of 34

---

Receiver Block Diagram
                                                                                                                                                                                     AFE OFFSET CODE
                                                                                                                                                                                                        Analog Front End
                                                                                                                                                                                                          Input term. and AC coupling network
                                                                                    Sub-ADC 0d                                                ADC_28D
                                                                                                                                                                                                          CTLE/PGA
                                                      ADC Bias Block                                                     SAR ADC
                                                                                                               CLK_28D
                                                                                          Sub-ADC 2d                                  ADC_24
                                                                                                                                            ADC_30D
                                                                                                                 CLK_24    SAR ADC
                                                                                                                                 SAR ADCD
                                                                                                                       CLK_30D
                                                                                               Sub-ADC 1d          D
                                                                                                                                      ADC_20ADC_26
                                                                                                                                                  ADC_29D
                                                                                                                           SAR ADC
                                                                                                                 CLK_20CLK_26    SAR ADC
                                                                                                                                      SARD ADC D
                                                                                                                            CLK_29D
                                 Offset DAC
                                                      TH_Buffer                     ADC_0D
                                                                                                     Sub-ADC 3d    D     D
                                                                                                                                      ADC_16ADC_22ADC_25
                                                                                                                                                       ADC_31D
                                                                                                                                                                                     ADC_00D<6:0>
                                                                                                                                                                                     ADC_01D<6:0>
                                                                                                                           SAR
                                                                                                                 CLK_16CLK_22   ADC
                                                                                                                                 SAR ADC
                                                                                                                            CLK_25    SARD ADC
                                                                                                                                            SARD ADCD
                                                                                     INPUT                                        CLK_31D                                            ADC_02D<6:0>
                                                                                                                   D     D     D
                      Input                                                                                                           ADC_12ADC_18ADC_21
                                                                                          ADC_2D
                                                                                                                                               D ADCD ADC_27D                        ADC_03D<6:0>
                                 CTLE/PGA




                                               ADC                                                                         SAR
                                                                                                                 CLK_12CLK_18    SAR ADC
                                                                                                                                ADC   SARD ADC
                                                                                                                                            SAR
       RX INPUT    Termination                                                                                              CLK_21
                                              INPUT                                        INPUT                                  CLK_27D
                        &                                                                                          D     D     D
                                                                                                                                      ADC_08ADC_14ADC_17
                   AC coupling                                       TH_Buffer                 ADC_1D                                                  ADC_23D
                                                                                               CLK_TH_0                    SAR
                                                                                                                 CLK_08CLK_14   ADC
                                                                                                                            CLK_17    SAR
                                                                                                                                 SAR ADC D ADC
                                                                                                                                            SARD ADCD                    ADC Data
                    Network                                                                      INPUT                            CLK_23D
                                                                                                    D              D     D     D                                         Alignment
                                                                                                                                      ADC_04ADC_10ADC_13
                                                                                                      ADC_3D               SAR  ADC                    ADC_19D
                                                                                                      CLK_TH_2 CLK_04CLK_10      SAR ADC
                                                                                                                            CLK_13    SARD ADC
                                                                                                                                            SARD ADCD
                                                                                                       INPUT                      CLK_19D                                            ADC_28D<6:0>
                                                                                                          D        D     D     D
                                                                                                                                      ADC_00ADC_06ADC_09
                                                                                                                           SAR  ADC
                                                                                                                                 SAR ADC               ADC_15D                       ADC_29D<6:0>
                                                                                                                 CLK_00CLK_06
                                                                                                            CLK_TH_1        CLK_09    SARD ADC
                                                                                                                                            SARD ADCD
                                                                                                                   D              CLK_15D                                            ADC_30D<6:0>
                                                                         ADCCK4T_0D     ADC Pulse Gen           D        D     D
                                                                  Td                                                                        ADC_02ADC_05
                                                                                                                       CLK_02    SARADCCK32T_
                                                                                                                            CLK_05   ADC
                                                                                                                                      SAR ADC
                                                                                                                                            SARD ADCD ADC_11D                        ADC_31D<6:0>
                                                                                                                  CLK_TH_3D             0D
                                                                                                                                  CLK_11D
                                                                         ADCCK4T_2D           ADC Pulse Gen              D     D
   2T I/Q CLOCKS                  CML                             Td                                                                              ADC_01
                     2T CML
                                   2           /2                                                                           CLK_01    SARADCCK32T_
                                                                                                                                           ADC
                                                                                                                                            SAR ADCD
                                                                                                                                                       ADC_07D
                      RXPI                                                                                                        CLK_07D    2D
                                 CMOS                                    ADCCK4T_1D                 ADC  Pulse Gen             D
                                                                  Td
                                                                                                                                                       ADC_03D
                                                                                                                                               ADCCK32T_
                                                                                                                                            SAR  ADC
                                                                                                                                  CLK_03D          1D                                ADCCK32T
                                                                         ADCCK4T_3D
                                                                  Td                                      ADC Pulse Gen




                                                                                                                          REFERENCE VOLTAGE
                                                           CSC                                                                                             ADCCK32T_3D




                                                                                                                                               ...
                                                                                                                                                     ADC Reference DAC
                                                                                                                                                                                      GAIN CODE
                                                                                                                                                                                      CKSKEW CODE
                                                                                                                                                                                      PI PHASE CODE




© 2021 IEEE
International Solid-State Circuits Conference                         8.5: A Scalable Adaptive ADC/DSP-Based 1.25-to-56Gb/s/112Gb/s High-Speed Transceiver Architecture Using Decision-Directed MMSE CDR in 16nm and 7nm                   11 of 34

---

RX Analog Front End
                                                 Input Termination                       CTLE/PGA
                                                         &                                                                                                                        DAC
                                                                                                                                                                                                   AFE OFFSET CODE




                                                                                                                                                                  Gm
                                                AC coupling Network




                                                  Tcoil                      Cac
                  RX Input




                                                                                                                        TIA
                                                                                                Gm




                                                                                                                                                                         TIA
                                                                                                                                                  Gm
                                                      100Ohm                                                                                                                                       AFE Output
                                                                            Cac
                                                  Tcoil




                               Tcoil with ESD protection                                                                         CTLE/PGA
                               100 Ohm differential termination resistor                                                                 Two stage Gm TIA based CTLE/PGA
                                                                                                                                          Peaking, gain, and bandwidth control
                               AC coupling capacitor                                                                                     Background offset cancel
© 2021 IEEE
International Solid-State Circuits Conference             8.5: A Scalable Adaptive ADC/DSP-Based 1.25-to-56Gb/s/112Gb/s High-Speed Transceiver Architecture Using Decision-Directed MMSE CDR in 16nm and 7nm     12 of 34

---

Receiver Block Diagram
                                                                                                                                                                                   AFE OFFSET CODE
                                                                                                                                                                                                      Analog Front End
                                                                                                                                                                                                        Input term. and AC coupling network
                                                                                 Sub-ADC 0d                                                 ADC_28D
                                                                                                                                                                                                        CTLE/PGA
                                                       ADC Bias Block                                                   SAR ADC
                                                                                                             CLK_28D
                                                                                       Sub-ADC 2d                                    ADC_24
                                                                                                                                           ADC_30D
                                                                                                               CLK_24     SAR ADC
                                                                                                                                SAR ADCD
                                                                                                                      CLK_30D
                                                                                             Sub-ADC 1d            D
                                                                                                                                     ADC_20ADC_26
                                                                                                                                                 ADC_29D
                                                                                                                          SAR ADC
                                                                                                               CLK_20CLK_26     SAR ADC
                                                                                                                                     SARD ADC D
                                                                                                                           CLK_29D
                                  Offset DAC
                                                       TH_Buffer                   ADC_0D
                                                                                                   Sub-ADC 3d      D    D
                                                                                                                                     ADC_16ADC_22ADC_25
                                                                                                                                                      ADC_31D
                                                                                                                                                                                   ADC_00D<6:0>
                                                                                                                                                                                   ADC_01D<6:0>
                                                                                                                          SAR
                                                                                                               CLK_16CLK_22    ADC
                                                                                                                                SAR ADC
                                                                                                                           CLK_25    SARD ADC
                                                                                                                                           SARD ADCD
                                                                                    INPUT                                        CLK_31D                                           ADC_02D<6:0>
                                                                                                                   D    D     D
                       Input                                                                                                         ADC_12ADC_18ADC_21
                                                                                         ADC_2D
                                                                                                                                              D ADCD ADC_27D                       ADC_03D<6:0>
                                  CTLE/PGA




                                                ADC                                                                       SAR
                                                                                                               CLK_12CLK_18     SAR ADC
                                                                                                                               ADC   SARD ADC
                                                                                                                                           SAR
        RX INPUT    Termination                                                                                            CLK_21
                                               INPUT                                      INPUT                                  CLK_27D
                         &                                                                                         D    D     D
                                                                                                                                     ADC_08ADC_14ADC_17
                    AC coupling                                     TH_Buffer                  ADC_1D                                                 ADC_23D
                                                                                              CLK_TH_0                    SAR
                                                                                                               CLK_08CLK_14    ADC
                                                                                                                           CLK_17    SAR
                                                                                                                                SAR ADC D ADC
                                                                                                                                           SARD ADCD                   ADC Data
                     Network                                                                    INPUT                            CLK_23D
                                                                                                   D               D    D     D                                        Alignment
                                                                                                                                     ADC_04ADC_10ADC_13
                                                                                                     ADC_3D               SAR  ADC                    ADC_19D
                                                                                                     CLK_TH_2 CLK_04CLK_10      SAR ADC
                                                                                                                           CLK_13    SARD ADC
                                                                                                                                           SARD ADCD
                                                                                                      INPUT                      CLK_19D                                           ADC_28D<6:0>
                                                                                                         D         D    D     D
                                                                                                                                     ADC_00ADC_06ADC_09
                                                                                                                          SAR  ADC
                                                                                                                                SAR ADC               ADC_15D                      ADC_29D<6:0>
                                                                                                               CLK_00CLK_06
                                                                                                           CLK_TH_1        CLK_09    SARD ADC
                                                                                                                                           SARD ADCD
                                                                                                                   D             CLK_15D                                           ADC_30D<6:0>
                                                                        ADCCK4T_0D     ADC  Pulse Gen         D         D     D
                                                                 Td                                                                        ADC_02ADC_05
                                                                                                                      CLK_02    SARADCCK32T_
                                                                                                                           CLK_05   ADC
                                                                                                                                     SAR ADC
                                                                                                                                           SARD ADCD ADC_11D                       ADC_31D<6:0>
                                                                                                                 CLK_TH_3D             0D
                                                                                                                                 CLK_11D
                                                                        ADCCK4T_2D           ADC Pulse Gen              D     D
    2T I/Q CLOCKS                  CML                           Td                                                                              ADC_01
                      2T CML
                                    2           /2                                                                         CLK_01    SARADCCK32T_
                                                                                                                                          ADC
                                                                                                                                           SAR ADCD
                                                                                                                                                      ADC_07D
                       RXPI                                                                                                      CLK_07D    2D
                                  CMOS                                  ADCCK4T_1D                 ADC Pulse Gen              D
                                                                 Td
                                                                                                                                                      ADC_03D
                                                                                                                                              ADCCK32T_
                                                                                                                                           SAR  ADC
                                                                                                                                 CLK_03D          1D                               ADCCK32T
                                                                        ADCCK4T_3D
                                                                 Td                                      ADC  Pulse Gen




                                                                                                                        REFERENCE VOLTAGE
                                                            CSC                                                                                     ADCCK32T_3D




                                                                                                                                             ...
                                                                                                                                                   ADC Reference DAC
                                                                                                                                                                                    GAIN CODE
                                                                                                                                                                                    CKSKEW CODE
                                                                                                                                                                                    PI PHASE CODE




© 2021 IEEE
International Solid-State Circuits Conference                      8.5: A Scalable Adaptive ADC/DSP-Based 1.25-to-56Gb/s/112Gb/s High-Speed Transceiver Architecture Using Decision-Directed MMSE CDR in 16nm and 7nm                    13 of 34

---

Receiver Block Diagram
                                                                                                                                                                                    AFE OFFSET CODE
                                                                                                                                                                                                       Analog Front End
                                                                                                                                                                                                         Input term. and AC coupling network
                                                                                   Sub-ADC 0d                                                ADC_28D
                                                                                                                                                                                                         CTLE/PGA
                                                     ADC Bias Block                                                     SAR ADC
                                                                                                              CLK_28D
                                                                                         Sub-ADC 2d                                  ADC_24
                                                                                                                                           ADC_30D
                                                                                                                CLK_24    SAR ADC
                                                                                                                                SAR ADCD

                                                                                                                                                                                                       RXPI
                                                                                                                      CLK_30D
                                                                                              Sub-ADC 1d          D
                                                                                                                                     ADC_20ADC_26
                                                                                                                                                 ADC_29D
                                                                                                                          SAR ADC
                                                                                                                CLK_20CLK_26    SAR ADC
                                                                                                                                     SARD ADC D
                                                                                                                           CLK_29D
                                Offset DAC
                                                     TH_Buffer                     ADC_0D
                                                                                                    Sub-ADC 3d    D     D
                                                                                                                                     ADC_16ADC_22ADC_25
                                                                                                                                                      ADC_31D
                                                                                                                                                                                    ADC_00D<6:0>
                                                                                                                                                                                    ADC_01D<6:0>
                                                                                                                          SAR
                                                                                                                CLK_16CLK_22   ADC
                                                                                                                                SAR ADC
                                                                                                                           CLK_25    SARD ADC
                                                                                                                                           SARD ADCD
                                                                                    INPUT                                        CLK_31D                                            ADC_02D<6:0>
                                                                                                                  D     D     D
                     Input                                                                                                           ADC_12ADC_18ADC_21
                                                                                         ADC_2D
                                                                                                                                              D ADCD ADC_27D                        ADC_03D<6:0>
                                CTLE/PGA




                                              ADC                                                                         SAR
                                                                                                                CLK_12CLK_18    SAR ADC
                                                                                                                               ADC   SARD ADC
                                                                                                                                           SAR
      RX INPUT    Termination                                                                                              CLK_21
                                             INPUT                                        INPUT                                  CLK_27D
                       &                                                                                          D     D     D
                                                                                                                                     ADC_08ADC_14ADC_17
                  AC coupling                                       TH_Buffer                 ADC_1D                                                  ADC_23D
                                                                                              CLK_TH_0                    SAR
                                                                                                                CLK_08CLK_14   ADC
                                                                                                                           CLK_17    SAR
                                                                                                                                SAR ADC D ADC
                                                                                                                                           SARD ADCD                    ADC Data
                   Network                                                                      INPUT                            CLK_23D
                                                                                                   D              D     D     D                                         Alignment
                                                                                                                                     ADC_04ADC_10ADC_13
                                                                                                     ADC_3D               SAR  ADC                    ADC_19D
                                                                                                     CLK_TH_2 CLK_04CLK_10      SAR ADC
                                                                                                                           CLK_13    SARD ADC
                                                                                                                                           SARD ADCD
                                                                                                      INPUT                      CLK_19D                                            ADC_28D<6:0>
                                                                                                         D        D     D     D
                                                                                                                                     ADC_00ADC_06ADC_09
                                                                                                                          SAR  ADC
                                                                                                                                SAR ADC               ADC_15D                       ADC_29D<6:0>
                                                                                                                CLK_00CLK_06
                                                                                                           CLK_TH_1        CLK_09    SARD ADC
                                                                                                                                           SARD ADCD
                                                                                                                  D              CLK_15D                                            ADC_30D<6:0>
                                                                        ADCCK4T_0D     ADC Pulse Gen           D        D     D
                                                                 Td                                                                        ADC_02ADC_05
                                                                                                                      CLK_02    SARADCCK32T_
                                                                                                                           CLK_05   ADC
                                                                                                                                     SAR ADC
                                                                                                                                           SARD ADCD ADC_11D                        ADC_31D<6:0>
                                                                                                                 CLK_TH_3D             0D
                                                                                                                                 CLK_11D
                                                                        ADCCK4T_2D           ADC Pulse Gen              D     D
  2T I/Q CLOCKS                  CML                             Td                                                                              ADC_01
                    2T CML
                                  2           /2                                                                           CLK_01    SARADCCK32T_
                                                                                                                                          ADC
                                                                                                                                           SAR ADCD
                                                                                                                                                      ADC_07D
                     RXPI                                                                                                        CLK_07D    2D
                                CMOS                                    ADCCK4T_1D                 ADC  Pulse Gen             D
                                                                 Td
                                                                                                                                                      ADC_03D
                                                                                                                                              ADCCK32T_
                                                                                                                                           SAR  ADC
                                                                                                                                 CLK_03D          1D                                ADCCK32T
                                                                        ADCCK4T_3D
                                                                 Td                                      ADC Pulse Gen




                                                                                                                         REFERENCE VOLTAGE
                                                          CSC                                                                                             ADCCK32T_3D




                                                                                                                                              ...
                                                                                                                                                    ADC Reference DAC
                                                                                                                                                                                     GAIN CODE
                                                                                                                                                                                     CKSKEW CODE
                                                                                                                                                                                     PI PHASE CODE




© 2021 IEEE
International Solid-State Circuits Conference                           8.5: A Scalable Adaptive ADC/DSP-Based 1.25-to-56Gb/s/112Gb/s High-Speed Transceiver Architecture Using Decision-Directed MMSE CDR in 16nm and 7nm                14 of 34

---

Phase Interpolator

                                                                                                   Phase Interpolator
                                                                               sw.1                     sw.1=1, sw.2=0: high freq.
                                                                                                        sw.1=0, sw.2=1: mid freq.
                                                                               sw.2                     sw.1=0, sw.2=0: low freq.
                                                                                                                                                CML to CMOS



                                                                                                                                    PI Output                               CK to ADC




                                      CK000                                                                                                        CK090


                                      CK180                                                                                                        CK270




                CML based phase interpolator with configurable inductance to support wide range of operating frequency

© 2021 IEEE
International Solid-State Circuits Conference   8.5: A Scalable Adaptive ADC/DSP-Based 1.25-to-56Gb/s/112Gb/s High-Speed Transceiver Architecture Using Decision-Directed MMSE CDR in 16nm and 7nm   15 of 34

---

Receiver Block Diagram
                                                                                                                                                                                 AFE OFFSET CODE
                                                                                                                                                                                                    Analog Front End
                                                                                                                                                                                                      Input term. and AC coupling network
                                                                               Sub-ADC 0d                                                 ADC_28D
                                                                                                                                                                                                      CTLE/PGA
                                                     ADC Bias Block                                                   SAR ADC
                                                                                                           CLK_28D
                                                                                     Sub-ADC 2d                                    ADC_24
                                                                                                                                         ADC_30D
                                                                                                              CLK_24    SAR ADC
                                                                                                                              SAR ADCD

                                                                                                                                                                                                    RXPI
                                                                                                                    CLK_30D
                                                                                           Sub-ADC 1d            D
                                                                                                                                   ADC_20ADC_26
                                                                                                                                               ADC_29D
                                                                                                                        SAR ADC
                                                                                                              CLK_20CLK_26    SAR ADC
                                                                                                                                   SARD ADC D
                                                                                                                         CLK_29D
                                Offset DAC
                                                                                                 Sub-ADC 3d      D    D                                                          ADC_00D<6:0>

                                                                                                                                                                                                      CML with configurable inductance
                                                                                                                                   ADC_16ADC_22ADC_25
                                                     TH_Buffer                   ADC_0D                                                             ADC_31D                      ADC_01D<6:0>
                                                                                                                        SAR
                                                                                                              CLK_16CLK_22   ADC
                                                                                                                              SAR ADC
                                                                                                                         CLK_25    SARD ADC
                                                                                                                                         SARD ADCD
                                                                                  INPUT                                        CLK_31D                                           ADC_02D<6:0>
                                                                                                                 D    D     D
                     Input                                                                                                         ADC_12ADC_18ADC_21
                                                                                       ADC_2D
                                                                                                                                            D ADCD ADC_27D                       ADC_03D<6:0>
                                CTLE/PGA




                                              ADC                                                                       SAR
                                                                                                              CLK_12CLK_18    SAR ADC
                                                                                                                             ADC   SARD ADC
                                                                                                                                         SAR
      RX INPUT    Termination                                                                                            CLK_21
                                             INPUT                                      INPUT                                  CLK_27D
                       &                                                                                         D    D     D
                                                                                                                                   ADC_08ADC_14ADC_17
                  AC coupling                                     TH_Buffer                 ADC_1D                                                  ADC_23D
                                                                                            CLK_TH_0                    SAR
                                                                                                              CLK_08CLK_14   ADC
                                                                                                                         CLK_17    SAR
                                                                                                                              SAR ADC D ADC
                                                                                                                                         SARD ADCD                   ADC Data
                   Network                                                                    INPUT                            CLK_23D
                                                                                                 D               D    D     D                                        Alignment
                                                                                                                                   ADC_04ADC_10ADC_13
                                                                                                   ADC_3D               SAR  ADC                    ADC_19D
                                                                                                   CLK_TH_2 CLK_04CLK_10      SAR ADC
                                                                                                                         CLK_13    SARD ADC
                                                                                                                                         SARD ADCD
                                                                                                    INPUT                      CLK_19D                                           ADC_28D<6:0>
                                                                                                       D         D    D     D
                                                                                                                                   ADC_00ADC_06ADC_09
                                                                                                                        SAR  ADC
                                                                                                                              SAR ADC               ADC_15D                      ADC_29D<6:0>
                                                                                                              CLK_00CLK_06
                                                                                                         CLK_TH_1        CLK_09    SARD ADC
                                                                                                                                         SARD ADCD
                                                                                                                 D             CLK_15D                                           ADC_30D<6:0>
                                                                      ADCCK4T_0D     ADC Pulse Gen           D        D     D
                                                               Td                                                                        ADC_02ADC_05
                                                                                                                    CLK_02    SARADCCK32T_
                                                                                                                         CLK_05   ADC
                                                                                                                                   SAR ADC
                                                                                                                                         SARD ADCD ADC_11D                       ADC_31D<6:0>
                                                                                                               CLK_TH_3D             0D
                                                                                                                               CLK_11D
                                                                      ADCCK4T_2D           ADC Pulse Gen              D     D
  2T I/Q CLOCKS                  CML                           Td                                                                              ADC_01
                    2T CML
                                  2           /2                                                                         CLK_01    SARADCCK32T_
                                                                                                                                        ADC
                                                                                                                                         SAR ADCD
                                                                                                                                                    ADC_07D
                     RXPI                                                                                                      CLK_07D    2D
                                CMOS                                  ADCCK4T_1D                 ADC  Pulse Gen             D
                                                               Td
                                                                                                                                                    ADC_03D
                                                                                                                                            ADCCK32T_
                                                                                                                                         SAR  ADC
                                                                                                                               CLK_03D          1D                               ADCCK32T
                                                                      ADCCK4T_3D
                                                               Td                                      ADC  Pulse Gen




                                                                                                                      REFERENCE VOLTAGE
                                                          CSC                                                                                     ADCCK32T_3D




                                                                                                                                           ...
                                                                                                                                                 ADC Reference DAC
                                                                                                                                                                                  GAIN CODE
                                                                                                                                                                                  CKSKEW CODE
                                                                                                                                                                                  PI PHASE CODE




© 2021 IEEE
International Solid-State Circuits Conference                         8.5: A Scalable Adaptive ADC/DSP-Based 1.25-to-56Gb/s/112Gb/s High-Speed Transceiver Architecture Using Decision-Directed MMSE CDR in 16nm and 7nm                  16 of 34

---

Receiver Block Diagram
                                                                                                                                                                                    AFE OFFSET CODE
                                                                                                                                                                                                       Analog Front End
                                                                                                                                                                                                         Input term. and AC coupling network
                                                                                   Sub-ADC 0d                                                ADC_28D
                                                                                                                                                                                                         CTLE/PGA
                                                     ADC Bias Block                                                     SAR ADC
                                                                                                              CLK_28D
                                                                                         Sub-ADC 2d                                  ADC_24
                                                                                                                                           ADC_30D
                                                                                                                CLK_24    SAR ADC
                                                                                                                                SAR ADCD

                                                                                                                                                                                                       RXPI
                                                                                                                      CLK_30D
                                                                                              Sub-ADC 1d          D
                                                                                                                                     ADC_20ADC_26
                                                                                                                                                 ADC_29D
                                                                                                                          SAR ADC
                                                                                                                CLK_20CLK_26    SAR ADC
                                                                                                                                     SARD ADC D
                                                                                                                           CLK_29D
                                Offset DAC
                                                                                                    Sub-ADC 3d    D     D                                                           ADC_00D<6:0>

                                                                                                                                                                                                         CML with configurable inductance
                                                                                                                                     ADC_16ADC_22ADC_25
                                                     TH_Buffer                     ADC_0D                                                             ADC_31D                       ADC_01D<6:0>
                                                                                                                          SAR
                                                                                                                CLK_16CLK_22   ADC
                                                                                                                                SAR ADC
                                                                                                                           CLK_25    SARD ADC
                                                                                                                                           SARD ADCD
                                                                                    INPUT                                        CLK_31D                                            ADC_02D<6:0>
                                                                                                                  D     D     D
                     Input                                                                                                           ADC_12ADC_18ADC_21

                                                                                                                                                                                                       4-Way TI-ADC
                                                                                         ADC_2D
                                                                                                                                              D ADCD ADC_27D                        ADC_03D<6:0>
                                CTLE/PGA




                                              ADC                                                                         SAR
                                                                                                                CLK_12CLK_18    SAR ADC
                                                                                                                               ADC   SARD ADC
                                                                                                                                           SAR
      RX INPUT    Termination                                                                                              CLK_21
                                             INPUT                                        INPUT                                  CLK_27D
                       &                                                                                          D     D     D
                                                                                                                                     ADC_08ADC_14ADC_17
                  AC coupling                                       TH_Buffer                 ADC_1D                                                  ADC_23D
                                                                                              CLK_TH_0                    SAR
                                                                                                                CLK_08CLK_14   ADC
                                                                                                                           CLK_17    SAR
                                                                                                                                SAR ADC D ADC
                                                                                                                                           SARD ADCD                    ADC Data
                                                                                                                                                                                                         8 Async. SAR ADC in each Sub-ADC
                   Network                                                                      INPUT                            CLK_23D
                                                                                                   D              D     D     D                                         Alignment
                                                                                                                                     ADC_04ADC_10ADC_13
                                                                                                     ADC_3D               SAR  ADC                    ADC_19D
                                                                                                     CLK_TH_2 CLK_04CLK_10      SAR ADC
                                                                                                                           CLK_13    SARD ADC
                                                                                                                                           SARD ADCD
                                                                                                      INPUT                      CLK_19D

                                                                                                                                                                                                         TI-ADC configurable from 7bit to 3bit
                                                                                                         D        D     D     D                                                     ADC_28D<6:0>
                                                                                                                                     ADC_00ADC_06ADC_09
                                                                                                                          SAR  ADC
                                                                                                                                SAR ADC               ADC_15D                       ADC_29D<6:0>
                                                                                                                CLK_00CLK_06
                                                                                                           CLK_TH_1        CLK_09    SARD ADC
                                                                                                                                           SARD ADCD
                                                                                                                  D              CLK_15D                                            ADC_30D<6:0>
                                                                        ADCCK4T_0D     ADC Pulse Gen           D        D     D

                                                                                                                                                                                                         Background offset cancellation
                                                                 Td                                                                        ADC_02ADC_05
                                                                                                                      CLK_02    SARADCCK32T_
                                                                                                                           CLK_05   ADC
                                                                                                                                     SAR ADC
                                                                                                                                           SARD ADCD ADC_11D                        ADC_31D<6:0>
                                                                                                                 CLK_TH_3D             0D
                                                                                                                                 CLK_11D
                                                                        ADCCK4T_2D           ADC Pulse Gen              D     D
  2T I/Q CLOCKS                  CML                             Td                                                                              ADC_01
                    2T CML
                                  2           /2                                                                           CLK_01    SARADCCK32T_
                                                                                                                                          ADC
                                                                                                                                           SAR ADCD
                                                                                                                                                      ADC_07D
                     RXPI                                                                                                        CLK_07D    2D
                                CMOS                                    ADCCK4T_1D                 ADC  Pulse Gen             D
                                                                 Td
                                                                                                                                                      ADC_03D
                                                                                                                                              ADCCK32T_
                                                                                                                                           SAR  ADC
                                                                                                                                 CLK_03D          1D                                ADCCK32T
                                                                        ADCCK4T_3D
                                                                 Td                                      ADC Pulse Gen




                                                                                                                         REFERENCE VOLTAGE
                                                          CSC                                                                                             ADCCK32T_3D




                                                                                                                                              ...
                                                                                                                                                    ADC Reference DAC
                                                                                                                                                                                     GAIN CODE
                                                                                                                                                                                     CKSKEW CODE
                                                                                                                                                                                     PI PHASE CODE




© 2021 IEEE
International Solid-State Circuits Conference                          8.5: A Scalable Adaptive ADC/DSP-Based 1.25-to-56Gb/s/112Gb/s High-Speed Transceiver Architecture Using Decision-Directed MMSE CDR in 16nm and 7nm                    17 of 34

---

Receiver Block Diagram
                                                                                                                                                                                    AFE OFFSET CODE
                                                                                                                                                                                                       Analog Front End
                                                                                                                                                                                                         Input term. and AC coupling network
                                                                                   Sub-ADC 0d                                                ADC_28D
                                                                                                                                                                                                         CTLE/PGA
                                                     ADC Bias Block                                                     SAR ADC
                                                                                                              CLK_28D
                                                                                         Sub-ADC 2d                                  ADC_24
                                                                                                                                           ADC_30D
                                                                                                                CLK_24    SAR ADC
                                                                                                                                SAR ADCD

                                                                                                                                                                                                       RXPI
                                                                                                                      CLK_30D
                                                                                              Sub-ADC 1d          D
                                                                                                                                     ADC_20ADC_26
                                                                                                                                                 ADC_29D
                                                                                                                          SAR ADC
                                                                                                                CLK_20CLK_26    SAR ADC
                                                                                                                                     SARD ADC D
                                                                                                                           CLK_29D
                                Offset DAC
                                                                                                    Sub-ADC 3d    D     D                                                           ADC_00D<6:0>

                                                                                                                                                                                                         CML with configurable inductance
                                                                                                                                     ADC_16ADC_22ADC_25
                                                     TH_Buffer                     ADC_0D                                                             ADC_31D                       ADC_01D<6:0>
                                                                                                                          SAR
                                                                                                                CLK_16CLK_22   ADC
                                                                                                                                SAR ADC
                                                                                                                           CLK_25    SARD ADC
                                                                                                                                           SARD ADCD
                                                                                    INPUT                                        CLK_31D                                            ADC_02D<6:0>
                                                                                                                  D     D     D
                     Input                                                                                                           ADC_12ADC_18ADC_21

                                                                                                                                                                                                       4-Way TI-ADC
                                                                                         ADC_2D
                                                                                                                                              D ADCD ADC_27D                        ADC_03D<6:0>
                                CTLE/PGA




                                              ADC                                                                         SAR
                                                                                                                CLK_12CLK_18    SAR ADC
                                                                                                                               ADC   SARD ADC
                                                                                                                                           SAR
      RX INPUT    Termination                                                                                              CLK_21
                                             INPUT                                        INPUT                                  CLK_27D
                       &                                                                                          D     D     D
                                                                                                                                     ADC_08ADC_14ADC_17
                  AC coupling                                       TH_Buffer                 ADC_1D                                                  ADC_23D
                                                                                              CLK_TH_0                    SAR
                                                                                                                CLK_08CLK_14   ADC
                                                                                                                           CLK_17    SAR
                                                                                                                                SAR ADC D ADC
                                                                                                                                           SARD ADCD                    ADC Data
                                                                                                                                                                                                         8 Async. SAR ADC in each Sub-ADC
                   Network                                                                      INPUT                            CLK_23D
                                                                                                   D              D     D     D                                         Alignment
                                                                                                                                     ADC_04ADC_10ADC_13
                                                                                                     ADC_3D               SAR  ADC                    ADC_19D
                                                                                                     CLK_TH_2 CLK_04CLK_10      SAR ADC
                                                                                                                           CLK_13    SARD ADC
                                                                                                                                           SARD ADCD
                                                                                                      INPUT                      CLK_19D

                                                                                                                                                                                                         TI-ADC configurable from 7bit to 3bit
                                                                                                         D        D     D     D                                                     ADC_28D<6:0>
                                                                                                                                     ADC_00ADC_06ADC_09
                                                                                                                          SAR  ADC
                                                                                                                                SAR ADC               ADC_15D                       ADC_29D<6:0>
                                                                                                                CLK_00CLK_06
                                                                                                           CLK_TH_1        CLK_09    SARD ADC
                                                                                                                                           SARD ADCD
                                                                                                                  D              CLK_15D                                            ADC_30D<6:0>
                                                                        ADCCK4T_0D     ADC Pulse Gen           D        D     D

                                                                                                                                                                                                         Background offset cancellation
                                                                 Td                                                                        ADC_02ADC_05
                                                                                                                      CLK_02    SARADCCK32T_
                                                                                                                           CLK_05   ADC
                                                                                                                                     SAR ADC
                                                                                                                                           SARD ADCD ADC_11D                        ADC_31D<6:0>
                                                                                                                 CLK_TH_3D             0D
                                                                                                                                 CLK_11D
                                                                        ADCCK4T_2D           ADC Pulse Gen              D     D
  2T I/Q CLOCKS                  CML                             Td                                                                              ADC_01

                                                                                                                                                                                                         Common reference voltage (VREF)
                    2T CML
                                  2           /2                                                                           CLK_01    SARADCCK32T_
                                                                                                                                          ADC
                                                                                                                                           SAR ADCD
                                                                                                                                                      ADC_07D
                     RXPI                                                                                                        CLK_07D    2D
                                CMOS                                    ADCCK4T_1D                 ADC  Pulse Gen             D
                                                                 Td

                                                                                                                                                                                                          fed to 32 SAR ADCs
                                                                                                                                                      ADC_03D
                                                                                                                                              ADCCK32T_
                                                                                                                                           SAR  ADC
                                                                                                                                 CLK_03D          1D                                ADCCK32T
                                                                        ADCCK4T_3D
                                                                 Td                                      ADC Pulse Gen




                                                                                                                         REFERENCE VOLTAGE
                                                                                                                                                          ADCCK32T_3D
                                                                                                                                                                                                         VREF is adjusted by 6bit DAC with
                                                          CSC



                                                                                                                                                                                                          0.15dB/LSB to maximize ADC
                                                                                                                                                                                                          dynamic range

                                                                                                                                              ...
                                                                                                                                                    ADC Reference DAC
                                                                                                                                                                                                         Background gain adaptation
                                                                                                                                                                                     GAIN CODE
                                                                                                                                                                                     CKSKEW CODE
                                                                                                                                                                                     PI PHASE CODE




© 2021 IEEE
International Solid-State Circuits Conference                           8.5: A Scalable Adaptive ADC/DSP-Based 1.25-to-56Gb/s/112Gb/s High-Speed Transceiver Architecture Using Decision-Directed MMSE CDR in 16nm and 7nm                   18 of 34

---

Time-Interleaved ADC
                                                            TI-ADC        T/H
                                                                                                                                                Sub-ADC 0d                  S/H
                                                                                                                                                                     CLK_28D
                                                                       CLK_TH_3D          8 SAR ADCs

                                                ADC INPUT                                                                                                            CLK_24D


                                                                                                                                                    T/H              CLK_20D
                                                                       CLK_TH_1D          8 SAR ADCs
                                                                                                                                                 CLK_TH_0D
                                                                                                                                 ADC_0D INPUT                        CLK_16D


                                                                                                                                                                     CLK_12D

                                                                       CLK_TH_2D          8 SAR ADCs
                                                                                                                                                                     CLK_08D


                                                                                                                                                                     CLK_04D


                                                                       CLK_TH_0D          8 SAR ADCs                                                                 CLK_00D
                                                                                                                                  ADCCK4T_0D     ADC Pulse Gen
                                                                                                                                                                     ADCCK32T_0D



                                                                                        CKSKEW CODE
                                                                           CSC


                                                                            4T

                                     ADCCK4T_3D             CLK_TH_3D     T H
                                     ADCCK4T_2D             CLK_TH_2D      T H                                                                                     T: Track/Hold (T/H) in track
                                     ADCCK4T_1D
                                     ADCCK4T_0D
                                                            CLK_TH_1D
                                                            CLK_TH_0D
                                                                             T H
                                                                                 T H
                                                                                                                                                                    mode
                                                                                                                                                                   S: Sample/Hold (S/H) in
                                                            CLK_28D
                                                                                  2T
                                                                                  S H
                                                            CLK_24D
                                                            CLK_20D
                                                            CLK_16D
                                                                                                                                                                    Sample mode
                                                                                                                                                                   H: Track/Hold and
                                      Sub_ADC 0d
                                                            CLK_12D
                                        Clocks
                                                            CLK_08D
                                                            CLK_04D                                                                                                 Sample/Hold in hold mode
                                                            CLK_00D
                                                            ADCCK32T                       16T            16T




© 2021 IEEE
International Solid-State Circuits Conference                8.5: A Scalable Adaptive ADC/DSP-Based 1.25-to-56Gb/s/112Gb/s High-Speed Transceiver Architecture Using Decision-Directed MMSE CDR in 16nm and 7nm   19 of 34

---

Receiver Block Diagram
                                                                                                                                                                                   AFE OFFSET CODE
                                                                                                                                                                                                      Analog Front End
                                                                                  Sub-ADC 0d
                                                                                                                                                                                                        Input term. and AC coupling network
                                                    ADC Bias Block                                                                          ADC_28D

                                                                                                                                                                                                        CTLE/PGA
                                                                                                                       SAR ADC
                                                                                                             CLK_28D
                                                                                        Sub-ADC 2d                                  ADC_24
                                                                                                                                          ADC_30D
                                                                                                               CLK_24    SAR ADC
                                                                                                                               SAR ADCD

                                                                                                                                                                                                      RXPI
                                                                                                                     CLK_30D
                                                                                             Sub-ADC 1d          D
                                                                                                                                    ADC_20ADC_26
                                                                                                                                                ADC_29D
                                                                                                                         SAR ADC
                                                                                                               CLK_20CLK_26    SAR ADC
                                                                                                                                    SARD ADC D
                                                                                                                          CLK_29D
                               Offset DAC
                                                                                                   Sub-ADC 3d    D     D                                                           ADC_00D<6:0>

                                                                                                                                                                                                        CML with configurable inductance
                                                                                                                                    ADC_16ADC_22ADC_25
                                                    TH_Buffer                     ADC_0D                                                             ADC_31D                       ADC_01D<6:0>
                                                                                                                         SAR
                                                                                                               CLK_16CLK_22   ADC
                                                                                                                               SAR ADC
                                                                                                                          CLK_25    SARD ADC
                                                                                                                                          SARD ADCD
                                                                                   INPUT                                        CLK_31D                                            ADC_02D<6:0>
                                                                                                                 D     D     D
                    Input                                                                                                           ADC_12ADC_18ADC_21

                                                                                                                                                                                                      4-Way TI-ADC
                                                                                        ADC_2D
                                                                                                                                             D ADCD ADC_27D                        ADC_03D<6:0>
                               CTLE/PGA




                                             ADC                                                                         SAR
                                                                                                               CLK_12CLK_18    SAR ADC
                                                                                                                              ADC   SARD ADC
                                                                                                                                          SAR
     RX INPUT    Termination                                                                                              CLK_21
                                            INPUT                                        INPUT                                  CLK_27D
                      &                                                                                          D     D     D
                                                                                                                                    ADC_08ADC_14ADC_17
                 AC coupling                                       TH_Buffer                 ADC_1D                                                  ADC_23D
                                                                                             CLK_TH_0                    SAR
                                                                                                               CLK_08CLK_14   ADC
                                                                                                                          CLK_17    SAR
                                                                                                                               SAR ADC D ADC
                                                                                                                                          SARD ADCD                    ADC Data

                                                                                                                                                                                                        8 Async. SAR ADC in each Sub-ADC
                  Network                                                                      INPUT                            CLK_23D
                                                                                                  D              D     D     D                                         Alignment
                                                                                                                                    ADC_04ADC_10ADC_13
                                                                                                    ADC_3D               SAR  ADC                    ADC_19D
                                                                                                    CLK_TH_2 CLK_04CLK_10      SAR ADC
                                                                                                                          CLK_13    SARD ADC
                                                                                                                                          SARD ADCD
                                                                                                     INPUT                      CLK_19D                                            ADC_28D<6:0>
                                                                                                                                                                                                        TI-ADC configurable from 7bit to 3bit
                                                                                                        D        D     D     D
                                                                                                                                    ADC_00ADC_06ADC_09
                                                                                                                         SAR  ADC
                                                                                                                               SAR ADC               ADC_15D                       ADC_29D<6:0>
                                                                                                               CLK_00CLK_06
                                                                                                          CLK_TH_1        CLK_09    SARD ADC
                                                                                                                                          SARD ADCD
                                                                                                                 D              CLK_15D                                            ADC_30D<6:0>
                                                                       ADCCK4T_0D     ADC Pulse Gen           D        D     D

                                                                                                                                                                                                        Background offset cancellation
                                                                Td                                                                        ADC_02ADC_05
                                                                                                                     CLK_02    SARADCCK32T_
                                                                                                                          CLK_05   ADC
                                                                                                                                    SAR ADC
                                                                                                                                          SARD ADCD ADC_11D                        ADC_31D<6:0>
                                                                                                                CLK_TH_3D             0D
                                                                                                                                CLK_11D
                                                                       ADCCK4T_2D           ADC Pulse Gen              D     D
 2T I/Q CLOCKS                  CML                             Td                                                                              ADC_01
                   2T CML
                                                                                                                                                                                                        Common reference voltage (VREF)
                                 2           /2                                                                           CLK_01    SARADCCK32T_
                                                                                                                                         ADC
                                                                                                                                          SAR ADCD
                                                                                                                                                     ADC_07D
                    RXPI                                                                                                        CLK_07D    2D
                               CMOS                                    ADCCK4T_1D                 ADC  Pulse Gen             D
                                                                Td
                                                                                                                                                     ADC_03D
                                                                                                                                             ADCCK32T_

                                                                Td
                                                                       ADCCK4T_3D
                                                                                                        ADC Pulse Gen
                                                                                                                                CLK_03D
                                                                                                                                          SAR  ADC
                                                                                                                                                 1D                                ADCCK32T
                                                                                                                                                                                                         fed to 32 SAR ADCs


                                                                                                                        REFERENCE VOLTAGE
                                                                                                                                                         ADCCK32T_3D
                                                                                                                                                                                                        VREF is adjusted by 6bit DAC with
                                                         CSC



                                                                                                                                                                                                         0.15dB/LSB to maximize ADC
                                                                                                                                                                                                         dynamic range

                                                                                                                                             ...
                                                                                                                                                   ADC Reference DAC
                                                                                                                                                                                                        Background gain adaptation
                                                                                                                                                                                                      CTLE/PGA powered by1.2V supply
                                                                                                                                                                                    GAIN CODE
                                                                                                                                                                                    CKSKEW CODE
                                                                                                                                                                                    PI PHASE CODE




© 2021 IEEE
International Solid-State Circuits Conference                          8.5: A Scalable Adaptive ADC/DSP-Based 1.25-to-56Gb/s/112Gb/s High-Speed Transceiver Architecture Using Decision-Directed MMSE CDR in 16nm and 7nm                   20 of 34

---

Transmitter Block
                                       CK2T IQ CK from CU                               CML
                                                                  2T CML
                                                                                         2                 DCC            TX Clock Gen
                                                                   TXPI
                                                                                       CMOS

                                                                                                                                      DCC Engine


                                                                                                                                            DCD

                                                                                                                          2T CK

                                                TP




                                                                                                          SST Driver
                                                                        Tcoil                                                  2:1                                           TX Data
                                                                                                                                               32:2            TXFIR/
                                                                                                                               MUX             MUX              LUT
                                                TN                      Tcoil




                            Full 7bit source-series-terminated (SST) Driver
                            TX FIR/LUT provides non-linear pre-distortion and de-emphasis
                            SST driver and 2:1 mux powered by 0.9V supply
© 2021 IEEE
International Solid-State Circuits Conference        8.5: A Scalable Adaptive ADC/DSP-Based 1.25-to-56Gb/s/112Gb/s High-Speed Transceiver Architecture Using Decision-Directed MMSE CDR in 16nm and 7nm   21 of 34

---

Receiver Performance Measurement
                                                                                                                                     53.125Gb/s PAM-4 Jitter Tolerance
                                          Bit Error Rate vs Insertion Loss
                                                                                                                                           (35dB IL, BER<1e-6)




                                                                                                                   Silicon Thermal System
                                                                                                                                                              Amphenol
                                         eTopus 16nm EVB            TX                                                                                           FCI
                                                                                                                   eTopus 16nm EVB              TX
                                                                                                                                                                                          Keysight
                                         Platform with local                       Backplanes                                                                Backplane
                                                                                                                   Platform with local                                                     BERT
                                                                                                                                                                IEEE
                                          power supplies            RX                                              power supplies              RX                                        M8040B
                                                                                                                                                             compliance
                                                                                                                                                               Channel
© 2021 IEEE
International Solid-State Circuits Conference       8.5: A Scalable Adaptive ADC/DSP-Based 1.25-to-56Gb/s/112Gb/s High-Speed Transceiver Architecture Using Decision-Directed MMSE CDR in 16nm and 7nm   22 of 34

---

Continuous FIR Adaptation
                    RX DSP Temperature Tracking at
                      53.125Gb/s PAM-4(35dB IL)                                                                        FIR                                                     FIR Freq. Response
           1.00E-06
                                                                            120

                           BER                                   Temp.      100
           1.00E-07




                                                                                  Temperature ⁰C
                                                                            80

                                                                            60
    BER




           1.00E-08
                                                                            40

           1.00E-09                                                         20

                                                                            0

           1.00E-10                                                         -20
                       0     10     20     30   40   50     60    70
                                         Time (minutes)

                                                                                                                       -35.4dB at 13.28GHz
                                                                                                                                                             CDR and FFE/DFE can continuously
                                                                                                                                                              adapt to temperature variation for all
                                                                                                                                                              data rates
                                                                                                                                                             -15°C and 125°C with 10°C/minute
                                                                                                                                                              during the up-ramp and down-ramp


© 2021 IEEE
International Solid-State Circuits Conference             8.5: A Scalable Adaptive ADC/DSP-Based 1.25-to-56Gb/s/112Gb/s High-Speed Transceiver Architecture Using Decision-Directed MMSE CDR in 16nm and 7nm   23 of 34

---

CTLE/PGA Measurements
                      Peaking Control Examples                                    DC Gain Control Examples                                              Bandwidth Control Examples




                    Max 17dB peaking at 14GHz                                    8dB gain adjustment                                                  Bandwidth adjustment for
                    7dB peaking adjustment                                                                                                               different data rates
© 2021 IEEE
International Solid-State Circuits Conference   8.5: A Scalable Adaptive ADC/DSP-Based 1.25-to-56Gb/s/112Gb/s High-Speed Transceiver Architecture Using Decision-Directed MMSE CDR in 16nm and 7nm   24 of 34

---

53.125Gb/s Transceiver Eye Diagram




© 2021 IEEE
International Solid-State Circuits Conference   8.5: A Scalable Adaptive ADC/DSP-Based 1.25-to-56Gb/s/112Gb/s High-Speed Transceiver Architecture Using Decision-Directed MMSE CDR in 16nm and 7nm   25 of 34

---

ADC Performance Measurement
                              28Gsample/s TI-ADC low input frequency                                                 28Gsample/s TI-ADC Nyquist input frequency


                                                                                                                                                       Gain mismatch
                                                                                                                                                       and clock skew


                                                 Gain mismatch
             Amplitude (dB)




                                                                                                    Amplitude (dB)




© 2021 IEEE
International Solid-State Circuits Conference    8.5: A Scalable Adaptive ADC/DSP-Based 1.25-to-56Gb/s/112Gb/s High-Speed Transceiver Architecture Using Decision-Directed MMSE CDR in 16nm and 7nm   26 of 34

---

7nm 106.25Gb/s Transceiver Eye Diagram




© 2021 IEEE
International Solid-State Circuits Conference   8.5: A Scalable Adaptive ADC/DSP-Based 1.25-to-56Gb/s/112Gb/s High-Speed Transceiver Architecture Using Decision-Directed MMSE CDR in 16nm and 7nm   27 of 34

---

7nm 106.25 Gb/s Transceiver
                                                             Performance Measurement

                                      106.25Gb/s PAM-4 Jitter Tolerance
                                                                                                                         Silicon Thermal System


                                                                                                                          eTopus 7nm EVB                 TX
                                                                                                                                                                           ISI                       Keysight
                                                                                                                          Platform with local                           Backplane                     BERT
                                                                                                                           power supplies                RX              Channel                     M8040B




                                                                                                                                                                              -26dB at 26.56GHz




© 2021 IEEE
International Solid-State Circuits Conference   8.5: A Scalable Adaptive ADC/DSP-Based 1.25-to-56Gb/s/112Gb/s High-Speed Transceiver Architecture Using Decision-Directed MMSE CDR in 16nm and 7nm              28 of 34

---

Die Photos
                                                       1.6mm                                      0.5mm                                              0.46mm



                                     RX            RX             RX               RX
                                                                                                                                                          TX
                     1.35mm




                                                  Clock Path                                          CU
                                                                                                                                                           PLL




                                                                                                                                         1.78mm
                                                                                                                        2.05mm
                                     TX            TX             TX              TX
                     0.5mm




                                                                                                                                                           RX
                                                DSP for Quad



                                                16nm 56Gb/s PAM-4 SERDES                                                                    7nm 112Gb/s PAM-4 SERDES
                                                                                                                                                   (Analog Only)
© 2021 IEEE
International Solid-State Circuits Conference        8.5: A Scalable Adaptive ADC/DSP-Based 1.25-to-56Gb/s/112Gb/s High-Speed Transceiver Architecture Using Decision-Directed MMSE CDR in 16nm and 7nm   29 of 34

---

Performance Summary




© 2021 IEEE
International Solid-State Circuits Conference   8.5: A Scalable Adaptive ADC/DSP-Based 1.25-to-56Gb/s/112Gb/s High-Speed Transceiver Architecture Using Decision-Directed MMSE CDR in 16nm and 7nm   30 of 34

---

Conclusions
         Robust DD-MMSE design shows meaningful system benefit
          CDR remains locked at BER of 2E-2
         Combined timing loop and ADC clock skew correction lead to
          Direct and reliable timing error estimation
          Simplification of analog/mixed-signal implementation
         Scalable architecture with automated fast adaptation shows advantages
          A wide range of data rates
          Different insertion losses
          Temperature variation

         ☞ Sophisticated digital communications and signal processing algorithms
         combined with efficient analog/mixed-signal design, in advanced CMOS processes,
         has potential to address future and more demanding data link applications

© 2021 IEEE
International Solid-State Circuits Conference   8.5: A Scalable Adaptive ADC/DSP-Based 1.25-to-56Gb/s/112Gb/s High-Speed Transceiver Architecture Using Decision-Directed MMSE CDR in 16nm and 7nm   31 of 34

---

Acknowledgements
         The authors would like to thank the digital, layout, verification, firmware and
             test teams at eTopus for their support
               Steve Wan, Ming Fung Tse, Edwin Casey Arifin, Luyao Yan, Szu-Hsuan Wang, Cong Huei
                   Liou, Yu Ren Cai, Chu Chun Liu, Chien Chung Peng, Bingwei Jiang


         The authors would like to thank Kenichi Ushiyama, Toru Takaishi at Socionext
             Inc. for their support.

         The authors would like to thank Mike Sapozhnikov at Cisco Systems for his
             support.



© 2021 IEEE
International Solid-State Circuits Conference   8.5: A Scalable Adaptive ADC/DSP-Based 1.25-to-56Gb/s/112Gb/s High-Speed Transceiver Architecture Using Decision-Directed MMSE CDR in 16nm and 7nm   32 of 34

---

References
         [1] J. Im, et al., “A 112Gb/s PAM-4 Long-Reach Wireline Transceiver Using a 36-Way
         Time-Interleaved SAR-ADC and Inverter-Based RX Analog Front-End in 7nm FinFET”
         ISSCC Dig. Tech. Papers, pp.116-117, Feb, 2020
         [2] T. Ali, et al., “A 460mW 112Gb/s DSP-Based Transceiver with 38dB Loss
         Compensation for Next-Generation Data Centers in 7nm FinFET Technology” ISSCC Dig.
         Tech. Papers, pp.118-119, Feb, 2020
         [3] B-J Yoo, et al., “A 56Gb/s 7.7mW/Gb/s PAM-4 Wireline Transceiver in10nm FinFET
         Using MM-CDR-Based ADC Timing Skew Control and Low-Power DSP with Approximate
         Multiplier” ISSCC Dig. Tech. Papers, pp.122-123, Feb, 2020
         [4] H. Kimura, et al., “28Gb/s 560mW Multi-Standard SerDes with Single-Stage Analog
         Front-End and 14-Tap Decision-Feedback Equalizer in 28nm CMOS” ISSCC Dig. Tech.
         Papers, pp.38-39, Feb, 2014
         [5] Jan W. M. Bergmans, “Digital Baseband Transmission and Recording” Boston, MA;
         Kluwer Academic, 1996

© 2021 IEEE
International Solid-State Circuits Conference   8.5: A Scalable Adaptive ADC/DSP-Based 1.25-to-56Gb/s/112Gb/s High-Speed Transceiver Architecture Using Decision-Directed MMSE CDR in 16nm and 7nm   33 of 34

---

END


© 2021 IEEE
International Solid-State Circuits Conference   8.5: A Scalable Adaptive ADC/DSP-Based 1.25-to-56Gb/s/112Gb/s High-Speed Transceiver Architecture Using Decision-Directed MMSE CDR in 16nm and 7nm   34 of 34

---

A Highly Reconfigurable 40-97GS/s
                                 DAC and ADC with 40GHz AFE
                              Bandwidth and Sub-35fJ/conv-step for
                              400Gb/s Coherent Optical Applications
                                         in 7nm FinFET
                            R. L. Nguyen1, A. M. Castrillon2, A. Fan1, A. Mellati1, B. T. Reyes2, C. Abidin1,
                            E. Olsen1, F. Ahmad1, G. Hatcher1, J. Chana3, L. Biolato2, L. Tse4, L. Wang1,
                            L. Wang4, M. Azarmnia1, M. Davoodi1, N. Campos2, N. Fan1, P. Prabha1,
                            Q. Lu1, S. Cyrusian1, S. Dallaire5, S. Ho3, S. Jantzi1, T. Dusatko3, W. Elsharkasy1
                            1Inphi Corporation, Irvine, CA

                            2Inphi Corporation, Cordoba, ARG

                            3Inphi Corporation, Vancouver, CAN

                            4Inphi Corporation, San Jose, CA

                            5Inphi Corporation, Ottawa, CAN
© 2021 IEEE
International Solid-State Circuits Conference   8.6 A Highly Reconfigurable 40-97GS/s DAC and ADC with 40GHz AFE Bandwidth and Sub-35fJ/conv-step for 400Gb/s Coherent Optical Applications in 7nm FinFET   1 of 37

---

Outline
                  Motivation
                  Transceiver Overview
                  Transmitter Architecture
                  Receiver Architecture
                  Performance Summary
                  Conclusion



© 2021 IEEE
International Solid-State Circuits Conference   8.6 A Highly Reconfigurable 40-97GS/s DAC and ADC with 40GHz AFE Bandwidth and Sub-35fJ/conv-step for 400Gb/s Coherent Optical Applications in 7nm FinFET   2 of 37

---

Exponential Data and Traffic Growth




© 2021 IEEE
International Solid-State Circuits Conference   8.6 A Highly Reconfigurable 40-97GS/s DAC and ADC with 40GHz AFE Bandwidth and Sub-35fJ/conv-step for 400Gb/s Coherent Optical Applications in 7nm FinFET   3 of 37

---

Boost in Data and Traffic Growth




© 2021 IEEE
International Solid-State Circuits Conference   8.6 A Highly Reconfigurable 40-97GS/s DAC and ADC with 40GHz AFE Bandwidth and Sub-35fJ/conv-step for 400Gb/s Coherent Optical Applications in 7nm FinFET   4 of 37

---

Higher Throughput Demand
                                                         (2 bits/symbol)
                                                                                              PAM 4 DSP                                               •      Deployment flexibility for
                                                                                                                                                             different application needs
                                                                                                       2X
                                                    Inside DC                                                                                                  – Low power DSP
                                                       / 5G                                                                                                    – High-performance optical
               Analog NRZ                                                                                                                                        pluggable modules

               1X            Encoding
                                                                                                              Coherent DSP
                                                                                         2X, 8x, … for QPSK, 16QAM, …                                                   •     Pushing to 400Gb/s
                                                                                                                                                                              and beyond
                                                     DC-DC /                                                                                                                     – Various modulation
                                                    Long Haul-                                                                                                                     and oversampling
                                                      Metro                                                                                                                        requirements
                       1980…
                                                                                                                                                                                 – Various power vs.
                                                           (N bits/symbol,
                                                           dual polarization)                                        2008…                                                         reach tradeoffs


© 2021 IEEE
International Solid-State Circuits Conference   8.6 A Highly Reconfigurable 40-97GS/s DAC and ADC with 40GHz AFE Bandwidth and Sub-35fJ/conv-step for 400Gb/s Coherent Optical Applications in 7nm FinFET   5 of 37

---

Coherent Transceiver Challenges
                  High reconfigurability for various applications
                           Different modulation schemes (QPSK, QAM16, etc.)
                           Different oversampling and data rate requirements (over an
                                    octave of sampling frequency range)
                  High analog electrical performance requirements
                           Large analog bandwidth (> 35GHz)
                           Low clock jitter (< 150fs-rms)
                  Optical module power limit
                           Optimal transceiver energy efficiency (FOM)
© 2021 IEEE
International Solid-State Circuits Conference   8.6 A Highly Reconfigurable 40-97GS/s DAC and ADC with 40GHz AFE Bandwidth and Sub-35fJ/conv-step for 400Gb/s Coherent Optical Applications in 7nm FinFET   6 of 37

---

Optical Transceiver System Overview




© 2021 IEEE
International Solid-State Circuits Conference   8.6 A Highly Reconfigurable 40-97GS/s DAC and ADC with 40GHz AFE Bandwidth and Sub-35fJ/conv-step for 400Gb/s Coherent Optical Applications in 7nm FinFET   7 of 37

---

Optical Transceiver System Overview



                                                                                                                               Aligned Data




© 2021 IEEE
International Solid-State Circuits Conference   8.6 A Highly Reconfigurable 40-97GS/s DAC and ADC with 40GHz AFE Bandwidth and Sub-35fJ/conv-step for 400Gb/s Coherent Optical Applications in 7nm FinFET   8 of 37

---

Transceiver Clocking Strategy




    Central PLL core
    Global distribution of quadrature
     PLL clocks
    Dedicated channel-to-channel
     skew alignment
                                                                                                Aligned Data
© 2021 IEEE
International Solid-State Circuits Conference   8.6 A Highly Reconfigurable 40-97GS/s DAC and ADC with 40GHz AFE Bandwidth and Sub-35fJ/conv-step for 400Gb/s Coherent Optical Applications in 7nm FinFET   9 of 37

---

Transceiver Clocking Strategy (2)
    Within the central PLL

             Fractional N multiplication


             Third-order sigma delta


             Multi-modulus divider


             Series stacked LDOs for supply
                     rejection of critical blocks

© 2021 IEEE
International Solid-State Circuits Conference   8.6 A Highly Reconfigurable 40-97GS/s DAC and ADC with 40GHz AFE Bandwidth and Sub-35fJ/conv-step for 400Gb/s Coherent Optical Applications in 7nm FinFET   10 of 37

---

Transceiver Clocking Strategy (3)
    Wide operation range
     covered by quadrature
     LC VCOs



    Dedicated MUX and
     detector to eliminate
     I/Q phase uncertainty


© 2021 IEEE
International Solid-State Circuits Conference   8.6 A Highly Reconfigurable 40-97GS/s DAC and ADC with 40GHz AFE Bandwidth and Sub-35fJ/conv-step for 400Gb/s Coherent Optical Applications in 7nm FinFET   11 of 37

---

Transceiver I/Q Clock Alignment




© 2021 IEEE
International Solid-State Circuits Conference   8.6 A Highly Reconfigurable 40-97GS/s DAC and ADC with 40GHz AFE Bandwidth and Sub-35fJ/conv-step for 400Gb/s Coherent Optical Applications in 7nm FinFET   12 of 37

---

Transceiver Divider Alignment

                                                                                                                                                                                                 Using lowest
                                                                                                                                                                                                 divided clocks




© 2021 IEEE
International Solid-State Circuits Conference   8.6 A Highly Reconfigurable 40-97GS/s DAC and ADC with 40GHz AFE Bandwidth and Sub-35fJ/conv-step for 400Gb/s Coherent Optical Applications in 7nm FinFET     13 of 37

---

Transceiver Divider Alignment (2)

                                                                                                                                    Aligned                                                                 Aligned
                                                                                                                                    State                                                                   State




                          Aligned state has largest duty cycle
© 2021 IEEE
International Solid-State Circuits Conference   8.6 A Highly Reconfigurable 40-97GS/s DAC and ADC with 40GHz AFE Bandwidth and Sub-35fJ/conv-step for 400Gb/s Coherent Optical Applications in 7nm FinFET             14 of 37

---

Outline
                  Motivation
                  Transceiver Overview
                  Transmitter Architecture
                  Receiver Architecture
                  Performance Summary
                  Conclusion



© 2021 IEEE
International Solid-State Circuits Conference   8.6 A Highly Reconfigurable 40-97GS/s DAC and ADC with 40GHz AFE Bandwidth and Sub-35fJ/conv-step for 400Gb/s Coherent Optical Applications in 7nm FinFET   15 of 37

---

Transmitter Architecture
    Interleave-by-4 topology                                                                                     1.1Vpp-diff max swing




© 2021 IEEE
International Solid-State Circuits Conference   8.6 A Highly Reconfigurable 40-97GS/s DAC and ADC with 40GHz AFE Bandwidth and Sub-35fJ/conv-step for 400Gb/s Coherent Optical Applications in 7nm FinFET   16 of 37

---

Transmitter Driver
    Current steering DACs with a 2b
     binary, 6b thermometer topology
    T-coil output network for BW and
     return loss




© 2021 IEEE
International Solid-State Circuits Conference   8.6 A Highly Reconfigurable 40-97GS/s DAC and ADC with 40GHz AFE Bandwidth and Sub-35fJ/conv-step for 400Gb/s Coherent Optical Applications in 7nm FinFET   17 of 37

---

Transmitter Serializer
    32-to-1 serializer




    Separate LDOs
     for clock path


                                                                                                                                                                                         LDO
© 2021 IEEE
International Solid-State Circuits Conference   8.6 A Highly Reconfigurable 40-97GS/s DAC and ADC with 40GHz AFE Bandwidth and Sub-35fJ/conv-step for 400Gb/s Coherent Optical Applications in 7nm FinFET   18 of 37

---

Serializer Clocking
  Quadrature
   clocking from PLL
   at 25GHz

  Phase interpolators
   & trimmers for
   skew calibration
                                                                                                                                                                         Bkgnd Calibration


© 2021 IEEE
International Solid-State Circuits Conference   8.6 A Highly Reconfigurable 40-97GS/s DAC and ADC with 40GHz AFE Bandwidth and Sub-35fJ/conv-step for 400Gb/s Coherent Optical Applications in 7nm FinFET   19 of 37

---

Transmitter Duty Cycle Correction

            Individual
             analog
             calibration
             loops for
             duty cycle
             correction




© 2021 IEEE
International Solid-State Circuits Conference   8.6 A Highly Reconfigurable 40-97GS/s DAC and ADC with 40GHz AFE Bandwidth and Sub-35fJ/conv-step for 400Gb/s Coherent Optical Applications in 7nm FinFET   20 of 37

---

Transmitter Performance



                                                            HD2                                                                          HD3
                                                               HD3                           fs/4-fout                                                           fs/2-fout                                  fs/4-fout
                                                                                                                                                                                                    HD2
                                                                                                     fs/2-fout




       Linearity better than 40dB
       Post calibrated spurs < -55dBFS
© 2021 IEEE
International Solid-State Circuits Conference   8.6 A Highly Reconfigurable 40-97GS/s DAC and ADC with 40GHz AFE Bandwidth and Sub-35fJ/conv-step for 400Gb/s Coherent Optical Applications in 7nm FinFET         21 of 37

---

Transmitter Performance (2)




       WC bandwidth > 35GHz
       High frequency SNR/SNDR limited by jitter, WC < 150fs-rms
© 2021 IEEE
International Solid-State Circuits Conference   8.6 A Highly Reconfigurable 40-97GS/s DAC and ADC with 40GHz AFE Bandwidth and Sub-35fJ/conv-step for 400Gb/s Coherent Optical Applications in 7nm FinFET   22 of 37

---

Transmitter Performance (3)
                                                       (Meas. w/ Keysight DCAN1000A)

                                                                                                                                                                               66GBd PAM4

                                                                                                                                                                               RLM > 0.996

                                                                                                                                                                               RJ ~ 140fs




© 2021 IEEE
International Solid-State Circuits Conference   8.6 A Highly Reconfigurable 40-97GS/s DAC and ADC with 40GHz AFE Bandwidth and Sub-35fJ/conv-step for 400Gb/s Coherent Optical Applications in 7nm FinFET   23 of 37

---

Outline
                  Motivation
                  Transceiver Overview
                  Transmitter Architecture
                  Receiver Architecture
                  Performance Summary
                  Conclusion



© 2021 IEEE
International Solid-State Circuits Conference   8.6 A Highly Reconfigurable 40-97GS/s DAC and ADC with 40GHz AFE Bandwidth and Sub-35fJ/conv-step for 400Gb/s Coherent Optical Applications in 7nm FinFET   24 of 37

---

Receiver Architecture
     T-coil input network

     Two-tiered samplers and
      front-end buffers
               2 front-end buffers (BUF1)
               16 SAR buffers (BUF2)


     128 asynchronous SARs
© 2021 IEEE
International Solid-State Circuits Conference   8.6 A Highly Reconfigurable 40-97GS/s DAC and ADC with 40GHz AFE Bandwidth and Sub-35fJ/conv-step for 400Gb/s Coherent Optical Applications in 7nm FinFET   25 of 37

---

Receiver Front-End Buffers
     Buffer topologies:
               Class A/B BUF1 for large-signal
                       bandwidth

               Raised supply at 1.2V for
                       headroom improvement


               Stacked NMOS gm/gm BUF2 for
                       high gain and improved settling

© 2021 IEEE
International Solid-State Circuits Conference   8.6 A Highly Reconfigurable 40-97GS/s DAC and ADC with 40GHz AFE Bandwidth and Sub-35fJ/conv-step for 400Gb/s Coherent Optical Applications in 7nm FinFET   26 of 37

---

Receiver Clocking
     2UI TAH sampling
               12.5% TAH duty cycle


     12UI SAR re-sampling

     Approx ~ 1ns for SAR
      conversion
               BER ~ 1E-15

© 2021 IEEE
International Solid-State Circuits Conference   8.6 A Highly Reconfigurable 40-97GS/s DAC and ADC with 40GHz AFE Bandwidth and Sub-35fJ/conv-step for 400Gb/s Coherent Optical Applications in 7nm FinFET   27 of 37

---

Receiver Calibration
     Fine delay loop for
      background timing
      skew correction

     Resistive DACs at
      BUF2 output for gain
      correction


© 2021 IEEE
International Solid-State Circuits Conference   8.6 A Highly Reconfigurable 40-97GS/s DAC and ADC with 40GHz AFE Bandwidth and Sub-35fJ/conv-step for 400Gb/s Coherent Optical Applications in 7nm FinFET   28 of 37

---

Receiver Performance




       Linearity > 42dB
       Post calibrated spurs < -65dBFS
© 2021 IEEE
International Solid-State Circuits Conference   8.6 A Highly Reconfigurable 40-97GS/s DAC and ADC with 40GHz AFE Bandwidth and Sub-35fJ/conv-step for 400Gb/s Coherent Optical Applications in 7nm FinFET   29 of 37

---

Receiver Performance (2)




       Bandwidth > 40GHz
       High frequency SNR/SNDR limited by jitter
© 2021 IEEE
International Solid-State Circuits Conference   8.6 A Highly Reconfigurable 40-97GS/s DAC and ADC with 40GHz AFE Bandwidth and Sub-35fJ/conv-step for 400Gb/s Coherent Optical Applications in 7nm FinFET   30 of 37

---

Outline
                  Motivation
                  Transceiver Overview
                  Transmitter Architecture
                  Receiver Architecture
                  Performance Summary
                  Conclusion



© 2021 IEEE
International Solid-State Circuits Conference   8.6 A Highly Reconfigurable 40-97GS/s DAC and ADC with 40GHz AFE Bandwidth and Sub-35fJ/conv-step for 400Gb/s Coherent Optical Applications in 7nm FinFET   31 of 37

---

QAM16 PS 400Gb/s Constellation




© 2021 IEEE
International Solid-State Circuits Conference   8.6 A Highly Reconfigurable 40-97GS/s DAC and ADC with 40GHz AFE Bandwidth and Sub-35fJ/conv-step for 400Gb/s Coherent Optical Applications in 7nm FinFET   32 of 37

---

Optical Performance vs. Baud Rates
                                                     Electrical




                                                TX                                 RX




                                                                                      Km-Fibers
                                                      Optical




                                                                                                                                                                         [A. Castrillon et al., “First Real-Time
                                                                                                                                                                         Demonstration of Probabilistic Shaping 400G
                                                                                                                                                                         Transmission Enabling High-Performance
                                                                                                                                                                         Pluggable Module Applications,” IEEE Photonic
                                                                                                                                                                         Conference 2020, MG1.3, Sept. 2020]



© 2021 IEEE
International Solid-State Circuits Conference        8.6 A Highly Reconfigurable 40-97GS/s DAC and ADC with 40GHz AFE Bandwidth and Sub-35fJ/conv-step for 400Gb/s Coherent Optical Applications in 7nm FinFET   33 of 37

---

TX & RX Comparison to Prior Arts




            Adapted from B. Murmann, "ADC Performance Survey 1997-2020,"
            [Online]. Available: http://web.stanford.edu/~murmann/adcsurvey.html
© 2021 IEEE
International Solid-State Circuits Conference   8.6 A Highly Reconfigurable 40-97GS/s DAC and ADC with 40GHz AFE Bandwidth and Sub-35fJ/conv-step for 400Gb/s Coherent Optical Applications in 7nm FinFET   34 of 37

---

TX & RX Comparison to Prior Arts (2)
                                                                                      This                                                                                                                              This
                         Specification                         [3]       [4]       [5]       [6]                                           Specification                             [3]       [4]          [5]    [6]
                                                                                     Work                                                                                                                               Work
                         CMOS Technology [nm]                  28   32     20   14      7                                 Conversion TX FOM @ DC [fJ/c-s]                                                               18.2
                         Resolution [bits]                      8    8      8    8      8                                                  TX FOM @ 30GHz [fJ/c-s]                                                      90.2
          Specs
                         Sampling Speed [GHz]                 100 70-100 55-69 24-72 40-97                                                 RX FOM @ DC [fJ/c-s]                               186       188        43    34
                         TX Full Scale Output [mV]                        700        1100                                                  RX FOM @ HF [fJ/c-s] ˣ                             426       377ˣ        80   67
                         SNR at DC [dB]                                              48.76                                                 RX FOM @ 36GHz [fJ/c-s]                                                 121   96
                         SFDR at DC [dB]                      41           50        50.54                                    Area         TX Quad + PLL [mm²]                      1.5ᵀ                2.4             2.35
             TX          SNDR at DC [dB]                     33.67        43.9       46.65                                                 RX Quad + PLL [mm²]                                0.45ᵀ      8        0.15ᵀ 2.35
                         SNDR at 15G [dB]                     22         37.88         39                                                  ˣ Note on RX HF Freq                               20G       16G       20G 20G
                         SNDR at 30G [dB]                                            32.76                                                 ᵀ Single DAC or ADC Channel Area only
                         -3dB Bandwidth                       10                       40
                         SNR at DC [b]                                                44.5                               [3] H. Huang et al., "An 8-bit 100-GS/s Distributed DAC in 28-nm CMOS for Optical
                                                                                                                         Communications", IEEE TMTT, vol. 63, No. 4, pp. 1211-1218, Apr. 2015.
                         SFDR at DC [b]                                                44
                                                                                                                         [4] L. Kull et al., “A 90GS/s 8b 667mW 64× Interleaved SAR ADC in 32nm Digital SOI
             RX          SNDR at DC [dB]                            35     40  39.3 41.1                                 CMOS”, ISSCC, pp. 378–380, Feb. 2014.
                         SNDR at HF [dB] ˣ                          28     34   34    35.1                               [5] J. Cao et al., “A Transmitter and Receiver for 100Gb/s Coherent Networks with
                         SNDR at 36GHz [dB]                                    30.4    32                                Integrated 4×64GS/s 8b ADCs and DACs in 20nm CMOS”, ISSCC, pp. 484–486,
                         -3dB Bandwidth                             20     19   21     40                                Feb. 2017.
                                                                                                                         [6] L. Kull et al., “A 24-to-72GS/s 8b Time-Interleaved SAR ADC with 2.0-to-
                                                                                                                         3.3pJ/conversion and >30dB SNDR at Nyquist in 14nm CMOS FinFET”, ISSCC, pp.
                                                                                                                         358–360, Feb. 2018.

© 2021 IEEE
International Solid-State Circuits Conference   8.6 A Highly Reconfigurable 40-97GS/s DAC and ADC with 40GHz AFE Bandwidth and Sub-35fJ/conv-step for 400Gb/s Coherent Optical Applications in 7nm FinFET                35 of 37

---

Conclusion
             Highly reconfigurable transceiver with over an octave
              of sampling frequency (40-97GS/s)

             Lowest reported total FOM to-date (<35fJ/c-s) near
              100GS/s

             Highest reported 40GHz AFE bandwidth

             Low total jitter WC < 150fs-rms
© 2021 IEEE
International Solid-State Circuits Conference   8.6 A Highly Reconfigurable 40-97GS/s DAC and ADC with 40GHz AFE Bandwidth and Sub-35fJ/conv-step for 400Gb/s Coherent Optical Applications in 7nm FinFET   36 of 37

---

Acknowledgement


                  The authors would like to thank the entire
                   development team of this project, System,
                   Digital, Analog, Layout, PD, DFT, and CAD
                   for their dedication and valuable support


© 2021 IEEE
International Solid-State Circuits Conference   8.6 A Highly Reconfigurable 40-97GS/s DAC and ADC with 40GHz AFE Bandwidth and Sub-35fJ/conv-step for 400Gb/s Coherent Optical Applications in 7nm FinFET   37 of 37

---

A 112Gb/s ADC-DSP-Based PAM-4 Transceiver
                      for Long-Reach Applications with >40dB
                            Channel Loss in 7nm FinFET
                  P. Mishra1, A. Tan1, B. Helal1, C.R. Ho1, C. Loi1, J. Riani1, J. Sun2, K. Mistry3,
                  K. Raviprakash1, L. Tse1, M. Davoodi4, M. Takefman3, N. Fan4, P. Prabha4, Q.
                  Liu2, Q. Wang1, R. Nagulapalli5, S. Cyrusian4, S. Jantzi4, S. Scouten3, T.
                  Dusatko6, T. Setya3, V. Giridharan1, V. Gurumoorthy1, V. Karam3, W. Liew2, Y.
                  Liao1, Y. Ou1
                  1 Inphi, San Jose, CA, USA

                  2 Inphi, Singapore, Singapore

                  3 Inphi, Ottawa, Canada

                  4 Inphi, Irvine, CA, USA

                  5 Inphi, Northampton, UK

                  6 Inphi, Burnaby, Canada




© 2021 IEEE                                       8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                        1 of 48

---

Self Introduction
                  Senior Member of IEEE
                  Undergrad degree from Indian Institute of Technology
                   (IIT) Varanasi, India in Electronics Engineering
                  Masters degree from Walden University, USA in Electrical
                   Engineering
                  Two decades of experience in high-speed transceiver
                   designs and holds 18 US patents
                  Have been with Inphi Corporation since 2010. Most
                   recently have been leading high-speed PAM-4 based
                   transceiver development

© 2021 IEEE                                     8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                      2 of 48

---

Outline
                           Motivation
                           Transmitter Architecture
                           Receiver Architecture
                           Link Performance Summary




© 2021 IEEE                                     8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                      3 of 48

---

Data & Traffic Growth Post-COVID-19




© 2021 IEEE                                     8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                      4 of 48

---

Cloud Data Center Switch & Optics Transition
   Roadmap


                      Switch

                  Host Speed




                  Module
                 Bandwidth


                     Module
                     SerDes


                  Optical
                Components
                   BW

© 2021 IEEE                                     8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                      5 of 48

---

112Gb/s Transceiver Challenges

                   Baud rate up to 112Gb/s



                   Non-idealities in channel loss



                   Power limit due to thermal consideration


© 2021 IEEE                                     8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                      6 of 48

---

112Gb/s Transceiver Challenges
                    Baud rate up to 112Gb/s
                              Combined bump-to-bump loss > 40dB (including
                               package loss ~10dB)
                              Higher bandwidth and lower jitter requirements


                   Non-idealities in channel loss

                   Power limit due to thermal consideration

© 2021 IEEE                                     8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                      7 of 48

---

112Gb/s Transceiver Challenges

                   Baud rate up to 112Gb/s


                    Non-idealities in channel loss
                              Discontinuity in channel traces
                              Discontinuity in package traces



                   Power limit due to thermal consideration

© 2021 IEEE                                     8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                      8 of 48

---

112Gb/s Transceiver Challenges

                   Baud rate up to 112Gb/s

                   Non-idealities in channel loss


                    Power limit due to thermal consideration
                              Package thermal capacity
                              Low-power transceiver topology for pluggable modules


© 2021 IEEE                                     8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                      9 of 48

---

112Gb/s ADC-DSP Based Transceiver

                   Long reach support


                   Compensation for non-idealities



                   Low Power


© 2021 IEEE                                     8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                      10 of 48

---

112Gb/s ADC-DSP Based Transceiver

                   Long Reach Support
                             CTLE + FFE + DFE + MLSD architecture


                   Compensation for non-idealities

                   Low Power


© 2021 IEEE                                     8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                      11 of 48

---

112Gb/s ADC-DSP Based Transceiver

                   Long Reach Support

                   Compensation for non-idealities
                             Adaptive reflection canceller in receiver
                             Pre-distortion in transmitter

                   Low Power


© 2021 IEEE                                     8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                      12 of 48

---

112Gb/s ADC-DSP Based Transceiver

                   Long Reach Support

                   Compensation for non-idealities

                    Low Power
                              Optimization of analog design for lower power
                              7nm node for efficient digital computations


© 2021 IEEE                                     8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                      13 of 48

---

Outline
                           Motivation
                           Transmitter Architecture
                           Receiver Architecture
                           Link Performance Summary




© 2021 IEEE                                     8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                      14 of 48

---

Transmitter Overview
                      DSP/                         Digital                                                       64:1
                                                                                   FIR                                                            DAC
                      digital                   Pre-distortion                                                 Serializer



                                                                                                                 TX PLL



                      DSP/                         Digital                                                       64:1
                                                                                   FIR                                                            DAC
                                                                                                                                                  DAC
                      digital                   Pre-distortion                                                 Serializer




                  High speed transmitter with CMOS serializer and 7b DAC
                  Digitally-assisted predistortion and FIR equalization
© 2021 IEEE                                              8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                               15 of 48

---

Transmitter Analog Path




                  Separated data and clock power domains
© 2021 IEEE                                     8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                      16 of 48

---

Sub-UI Equalization                                                                                                                             With Feedback ®
                                                                                                                                                   Without Feedback ®



                           Sub-UI Equalizer
                                                ®   enb


                                                     en


                            IN                                              OUT




                  Sub-UI equalization is implemented in pre-driver and
                   clock path.
                           ISI in pre-driver degrades SNDR significantly.
                           BW limitation @ 28G leads to jitter amplification in the TX path
                  Transmission gate (instead of a resistor) is used for less
                   area occupation
© 2021 IEEE                                         8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                           17 of 48

---

Transmitter DAC
                                                                                                                      VDDH = 1.15V
             5-bit Binary
                                                                                                                     50 ohm termination
             3-bit Thermometric
                                                                        PMOS                                                                                                      PMOS
                                                                       bleeder                                                                                                   bleeder
                                                                                                                        TXP       TXN


                                                                                                                       Primary ESD




                                                Ref   P           N     P             N     P             N      P            N     P            N      P            N       P             N   P         N
                                                                                                                                                              2x                   2x              2x

                                                          d0                 d1                  d2                   d3                d4                  d5                    d6               d7
                                                                                                     Binary                                                              Thermometer

© 2021 IEEE                                               8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                                                           18 of 48

---

TX Measurement: 56Gb/s PAM4
                           56Gb/s PRBS13
                           4MHz 1st order CDR
                           De-embedded to package ball
                           3T FFE
                           0% pre-cursor
                           9% post-cursor                                                                                              Vamp = 710mV
                  RLM >0.95
                  SNDR >40dB




© 2021 IEEE                                     8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                      19 of 48

---

TX Measurement: 112Gb/s PAM4
                           112Gb/s PRBS13
                           4MHz 1st order CDR
                           De-embedded to package ball
                           3T FFE
                           4% pre-cursor
                           9% post-cursor                                                                                                Vamp = 610mV

                  RLM >0.95
                  SNDR >40dB




© 2021 IEEE                                     8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                      20 of 48

---

TX SNDR Over VT: 112Gb/s PAM4
                           112Gb/s PRBS13
                                                     45
                           4MHz 1st order CDR
                           De-embedded to package ball                                                                                      Measured Data

                           3T FFE                   40




                                                                                      SNDR [dB]
                           4% pre-cursor
                           9% post-cursor
                  RLM >0.95                                                                      35
                  SNDR                                                                                                                              Spec

                           Worst Case ~ 40dB
                                                                                                  30
                                                                                                            LV/LT TV/LT HV/LT LV/TT LV/TT HV/TT LV/HT TV/HT HV/HT

                                                                                                                                    Voltage/Temperature

© 2021 IEEE                                     8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                       21 of 48

---

TX Measurement: 56Gb/s NRZ
                           56.25Gb/s PRBS13
                           4MHz 1st order CDR
                           De-embedded to package ball
                           Jitter                                                                                                             Vamp = 650mV
                           RJ 178fsrms
                           DCD 40fsp-p
                           ISI 3.45psp-p
                  TJ(1e-12)
                           5.35psp-p




© 2021 IEEE                                     8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                      22 of 48

---

Outline
                           Motivation
                           Transmitter Architecture
                           Receiver Architecture
                           Link Performance Summary




© 2021 IEEE                                     8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                      23 of 48

---

Receiver Overview

                                                RX PLL                       CDR


                                                                                                                                                                     M
                                                 ADC                                             FFE +                       Refl.
                              ODT+CTLE          ADC
                                                ADC                                                                                                      MLSD        U
                                                                                                  DFE                        Canc.
                                                                                                                                                                     X




                  8-bit ADC-DSP based receiver
                  CDR and FFE/DFE/MLSD in the digital domain

© 2021 IEEE                                       8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                            24 of 48

---

Receiver Analog Path
                                                                                             16 Channels
                                                AFE
                 Input                                                                                                                        4x SAR                      Data from
                                         ODT                                                           T&H
                                                                                                       TAH                                 4x SAR
                                                                                                                                           4x
                                                                                                                                           4x  SAR
                                                                                                                                               SAR                        64 Lanes

                                                                             TAH
                                                CTLE1     CTLE2
                                                                            Buffer


                                      Analog
                                       data                                                                                                                              Quad. Phase
                                                                                                              Clock Generation
                                                                                                                                                                          14G Clock
                                      Analog
                                       clock



                  2-stage CTLE
                  VGA after TAH

© 2021 IEEE                                           8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                                          25 of 48

---

Receiver AFE: Termination
                                                Termination                                      RL,1                  RL,1        RL,2                   RL,2         RBuf                RBuf

                                                                                                 LP,1                  LP,1        LP,2                   LP,2
                                                                 CAC         LS
                  RX
                 Input               CBUMP
                                                                                                                           CC
                                                           cp1    cp2

                                     + CESD      LT        LT
                                                                                                                                                                                                   To
                                                                                                                                                                                                  T&H
                                                      k                 RT                                  CS,1                               CS,2
                                                                                                RS,1                   RS,1       RS,2                    RS,2

                                                      CB

                                                                                                         CTLE1                              CTLE2                             T&H Buffer




                  T-coil at the input for BW extension and better RL
                  AC-coupled CTLE stages

© 2021 IEEE                                                       8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                                                           26 of 48

---

Receiver AFE: CTLE
                                                Termination                                      RL,1                  RL,1        RL,2                   RL,2         RBuf                RBuf

                                                                                                 LP,1                  LP,1        LP,2                   LP,2
                                                                 CAC         LS
                  RX
                 Input               CBUMP
                                                                                                                           CC
                                                           cp1    cp2

                                     + CESD      LT        LT
                                                                                                                                                                                                   To
                                                                                                                                                                                                  T&H
                                                      k                 RT                                  CS,1                               CS,2
                                                                                                RS,1                   RS,1       RS,2                    RS,2

                                                      CB

                                                                                                         CTLE1                              CTLE2                             T&H Buffer




                  T-coil at the input for BW and RL
                  AC-Coupled CTLE Stages

© 2021 IEEE                                                       8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                                                           27 of 48

---

Receiver AFE: Buffer
                                                Termination                                      RL,1                  RL,1        RL,2                   RL,2         RBuf                RBuf

                                                                                                 LP,1                  LP,1        LP,2                   LP,2
                                                                 CAC         LS
                  RX
                 Input               CBUMP
                                                                                                                           CC
                                                           cp1    cp2

                                     + CESD      LT        LT
                                                                                                                                                                                                   To
                                                                                                                                                                                                  T&H
                                                      k                 RT                                  CS,1                               CS,2
                                                                                                RS,1                   RS,1       RS,2                    RS,2

                                                      CB

                                                                                                         CTLE1                              CTLE2                             T&H Buffer



                  T-coil at the input for BW and RL
                  AC-Coupled CTLE Stages

© 2021 IEEE                                                       8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                                                           28 of 48

---

Receiver ADC
                                           Global                                                                Quad Phase
                                          Ref Gen                                                                14GHz clock,
                                                                                                                    50%

                      RDAC for Gain
                                                                                                                                                                                                64 SAR
                                                    Bank   Bank   Bank   Bank   Bank     Bank      Bank   Bank      Bank     Bank    Bank       Bank   Bank   Bank   Bank   Bank   Bank
                          Cal                        0      4      8      12     15       3         7      11       DMY       14      2          6      10     13     1      5      9       
           Ref
           buf                                                                                                                                                                                 16 TAH
                   SAR SAR SAR SAR                                                                                                                                                             4-SAH/bank
                    00 16 32 48
                                                                                                                                                                                               Timing Cal
                                                                                       φS/H<0:63> 875MHz 12.5%
                                                                                                                                                                                               Gain Cal
          SAH
          SW                                                                                                                                                                                   Offset Cal
                                                                                                 SAH
                                                                                                                 TAH Divider
                                                                                                Divider
                                                                                                                                                                                               VGA after TAH
                                            SAH                                                                                       ph0trim
                                            BUF                                                    Trimmer                            ph1trim

                                                                                                      x16
                                            VGA                                                                                      ph15trim



                                            TAH                                                                            φT/H<0:15> 3.5GHz 25%
                                            SW




                                                                                                                    AFE


© 2021 IEEE                                                              8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                                                           29 of 48

---

Receiver ADC: VGA
                                           Global                                                                Quad Phase
                                          Ref Gen                                                                14GHz clock,
                                                                                                                    50%

                      RDAC for Gain
                                                                                                                                                                                                64 SAR
                                                    Bank   Bank   Bank   Bank   Bank     Bank      Bank   Bank      Bank     Bank    Bank       Bank   Bank   Bank   Bank   Bank   Bank
                          Cal                        0      4      8      12     15       3         7      11       DMY       14      2          6      10     13     1      5      9       
           Ref
           buf                                                                                                                                                                                 16 TAH
                   SAR SAR SAR SAR                                                                                                                                                             4-SAH/bank
                    00 16 32 48
                                                                                                                                                                                               Timing Cal
                                                                                       φS/H<0:63> 875MHz 12.5%
                                                                                                                                                                                               Gain Cal
          SAH
          SW                                                                                                                                                                                   Offset Cal
                                                                                                 SAH
                                                                                                                 TAH Divider
                                                                                                Divider
                                                                                                                                                                                               VGA after TAH
                                            SAH                                                                                       ph0trim
                                            BUF                                                    Trimmer                            ph1trim

                                                                                                      x16
                                            VGA                                                                                      ph15trim



                                            TAH                                                                            φT/H<0:15> 3.5GHz 25%
                                            SW




                                                                                                                    AFE


© 2021 IEEE                                                              8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                                                           30 of 48

---

Receiver ADC: VGA
                                                                                                              VGA
                                                                                                                                                             Single Gain Control
                                                                                                  RS                   RS                                    Dual Slope Gain Control
                                                                                                                                                  12
        9-bit                 Gain State Machine
      Gain Code                                                                                                                                   10
                                                   Dgcl
         (Di)                                                            LPF                           Mgcl         Weak
                                                          DSM                     vgcl                              PMOS
                                                                                                                                                  8
                   DAC Code




                                                          DAC
      Threshold




                                                                                                                                     Gain in dB
                                                   Dgch                                                             Strong
        (DTH)                          Dgch                                                            Mgch                                       6
                                                          DSM            LPF     vgch                               PMOS
                                 DTH                      DAC                                                                                     4
                                       Dgcl
                                                                                         vin+                                 vin-
                                  Gain Code (Di)                                                                                                  2

                                                                                           vo-                               vo+
                                                                                                                                                  0
                                                                                                  RL                   RL                              150      200      250       300      350   400        450
                                                                                                                                                  -2
                                                                                                                                                                                Gain Code




                   Dual-Slope Gain Controls for VGA
                   Better THD and smaller Gain Step size

© 2021 IEEE                                                     8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                                                           31 of 48

---

Receiver ADC: Clocking
                                           Global                                                                Quad Phase
                                          Ref Gen                                                                14GHz clock,
                                                                                                                    50%

                      RDAC for Gain
                                                                                                                                                                                                64 SAR
                                                    Bank   Bank   Bank   Bank   Bank     Bank      Bank   Bank      Bank     Bank    Bank       Bank   Bank   Bank   Bank   Bank   Bank
                          Cal                        0      4      8      12     15       3         7      11       DMY       14      2          6      10     13     1      5      9       
           Ref
           buf                                                                                                                                                                                 16 TAH
                   SAR SAR SAR SAR                                                                                                                                                             4-SAH/bank
                    00 16 32 48
                                                                                                                                                                                               Timing Cal
                                                                                       φS/H<0:63> 875MHz 12.5%
                                                                                                                                                                                               Gain Cal
          SAH
          SW                                                                                                                                                                                   Offset Cal
                                                                                                 SAH
                                                                                                                 TAH Divider
                                                                                                Divider
                                                                                                                                                                                               VGA after TAH
                                            SAH                                                                                       ph0trim
                                            BUF                                                    Trimmer                            ph1trim

                                                                                                      x16
                                            VGA                                                                                      ph15trim



                                            TAH                                                                            φT/H<0:15> 3.5GHz 25%
                                            SW




                                                                                                                    AFE


© 2021 IEEE                                                              8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                                                           32 of 48

---

Receiver ADC: Clocking
                                                                                                                                  16 Channels
                                 4UI

                        φT/H0   Track           Hold
                                                                                                                                                                             4x SAR
                        φT/H1
                                                                                                                                           T&H
                                                                                                                                           TAH                            4x SAR
                                                                                                                                                                          4x  SAR
           TAH CLK




                        φT/H2



                       φT/H15
                                        16UI

                                           Sample                ADC Conversion                                                                [15:0]                          [3:0]
                       φS/H00
                                             8UI                             56UI
        (T/H Lane 0)
         SAH CLK




                       φS/H16

                       φS/H32                                                                                                                                                          Quad. Phase
                       φS/H48
                                                                                                                                                 Clock Generation                       14G Clock



                        25% duty cycle on TAH clock 12.5% on SAH
                        4x TAH loading on the AFE buffer

© 2021 IEEE                                            8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                                               33 of 48

---

Receiver ADC: Asynchronous SAR
                                           Global                                                                Quad Phase
                                          Ref Gen                                                                14GHz clock,
                                                                                                                    50%

                      RDAC for Gain
                                                                                                                                                                                                64 SAR
                                                    Bank   Bank   Bank   Bank   Bank     Bank      Bank   Bank      Bank     Bank    Bank       Bank   Bank   Bank   Bank   Bank   Bank
                          Cal                        0      4      8      12     15       3         7      11       DMY       14      2          6      10     13     1      5      9       
           Ref
           buf                                                                                                                                                                                 16 TAH
                   SAR SAR SAR SAR                                                                                                                                                             4-SAH/bank
                    00 16 32 48
                                                                                                                                                                                               Timing Cal
                                                                                       φS/H<0:63> 875MHz 12.5%
                                                                                                                                                                                               Gain Cal
          SAH
          SW                                                                                                                                                                                   Offset Cal
                                                                                                 SAH
                                                                                                                 TAH Divider
                                                                                                Divider
                                                                                                                                                                                               VGA after TAH
                                            SAH                                                                                       ph0trim
                                            BUF                                                    Trimmer                            ph1trim

                                                                                                      x16
                                            VGA                                                                                      ph15trim



                                            TAH                                                                            φT/H<0:15> 3.5GHz 25%
                                            SW




                                                                                                                    AFE


© 2021 IEEE                                                              8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                                                           34 of 48

---

Receiver ADC: Asynchronous SAR
                                                                                                                                                                                                   vop

                                                                                                                                                                                                   vom


                               d<0>                 d<1>         d<2>            d<3>               d<4>              d<5>              d<6>              d<7>
                                                                                                                                                                                              Tc
                                  Dm                  Dm           Dm               Dm                Dm                 Dm                Dm                Dm
                                  Dp                  Dp           Dp               Dp                Dp                 Dp                Dp                Dp


                                   rst                 rst          rst              rst              rst                rst                rst               rst         rst
                         done start             done start   done start     done start       done start         done start        done start         done start                          CK
                                                                                                                                                                                                   Td

                                                                                                                                                                          done              Done
                                                                                                                                                                                          detection
                                                                                                                                                                          rstB              logic

                  8-bit 875MHz Asynchronous SAR ADC
                  CDAC: 5 LSB Binary, 3 MSB with radix 1.6
© 2021 IEEE                                                           8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                                                            35 of 48

---

Receiver: Analog Performance
                                  16


                                  12
              Peaking Magnitude [dB]




                                       8


                                       4



                                       0


                                       -4
                                         0.1    1                     10                        100
                                                    Frequency [GHz]




                            Measured AFE and receiver input return loss

© 2021 IEEE                                                    8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                                     36 of 48

---

Receiver: Analog Performance Cont’d
                                  0                                      FIN = 1GHZ                                             0        FIN = 25GHZ

                                 -20       HD3 = 40.24dB                                                                       -20                                 HD3 = 41.06dB
                Magnitude [dB]




                                                                                                              Magnitude [dB]
                                 -40                                                                                           -40

                                 -60                                                                                           -60

                                 -80                                                                                           -80

                           -100                                                                                         -100
                                       0    5         10        15             20               25                                   0          5       10        15              20   25
                                                     Frequency [GHz]                                                                                   Frequency [GHz]


                    SNDR of 35.12dB at 1GHz
                    SNDR of 30.04dB at 25GHz (~Nyquist)
© 2021 IEEE                                                    8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                                               37 of 48

---

Receiver: Analog Performance Cont’d
                                          65

                                          60

                                          55

                                          50
                                   [dB]




                                          45

                                          40

                                          35

                                          30
                                                5                  10           15                                 20                      25
                                                                   Frequency [GHz]

                  SNDR >30 dB from DC to 25GHz

© 2021 IEEE                                         8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                          38 of 48

---

Receiver: MLSD Performance
                                                       -4
                                                      10
                                                                          MLSD ON
                                                                          MLSD OFF

                                                       -6
                                                      10


                                                BER
                                                                                               >4dB
                                                           -8
                                                      10



                                                       -10
                                                      10
                                                            33             35       37      39                              41
                                                                           Insertion Loss [dB]
                                                                                                                                               [J.W.M. Bergmans, Linear Equalization, 1996]

                  MLSD achieving 4-5dB SNR gain or 2 orders of BER
                  MLSD better for high ISI channels
© 2021 IEEE                                                     8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                                                 39 of 48

---

Receiver: Jitter Tolerance
                                                                              101
                                                                                                                                          HV/LT




                                                Tolerated Pj Amplitude [UI]
                                                                                                                                          HV/HT
                                                                                                                                          LV/LT
                                                                                                                                          LV/HT
                                                                              100




                                                                          10-1




                                                                              10-2
                                                                                105                     106             107                                   108
                                                                                                               Frequency [Hz]

                  SJ+RJ modulates PRBS31 pattern
                  Channel loss of 35dB at Nyquist
© 2021 IEEE                                                                         8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                                                          40 of 48

---

Outline
                           Motivation
                           Transmitter Architecture
                           Receiver Architecture
                           Link Performance Summary




© 2021 IEEE                                     8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                      41 of 48

---

Testing Configuration in Smooth
   Channel                                      Tx (Source)

                                                                              ISI Loss
                                                                                                                           Rx (DUT)


                                                                                                      Noise
                                                                                                     Couplers




                                                                               ISI Traces
                                                                                                                                  Syrma
                                                                                             Balun



                                                                                                                      Rx


                                                 Test Signal Path
                                                 Added Noise                                         Noisewave

                                                                                                                                                                   Rx
                                                                                                      NW30G
                                                                                               (30GHz noise source)




                  This setup is tested with loss > 40dB w/ and w/o broadband
                   noise disturbance.
                  One board is used as the TX source while another board for
© 2021 IEEE
                   receiver.                    8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                           42 of 48

---

Measurement In Smooth Channel
   Setup Cont’d
                            Measured Channel Loss                         Bump to Bump Loss                                              Noise Tolerance Measurement
                                                                 Component USED                     Bump to Bump Loss
                                                                                                     @ Nyquist[dB]

                                                                      ISI Trace Loss                                              10-4
                                                                                                            32.15




                                                                                                                                 BER
                                                                    Tx and Rx Boards                         6.5
                                                                                                                                  10-5

                                                                Tx and Rx Package Loss                       2.5

                                                                       Total Loss
                                                                                                           ~41.15
                                                                     (Bump to Bump)                                               10-6

                                                                                                                                         0     0.2       0.4      0.6        0.8   1   1.2
                                                                                                                                                           Rms Noise (in mV)




                  PRBS31 pattern is used
                  Noise is swept for 106.25Gb/s

© 2021 IEEE                                         8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                                                43 of 48

---

Testing Configuration with 850G
   Direct attached passive cable
                                                                                                                                                                                 RX
                                                          800G direct                        800G
                                 800G           TX         attached                                                                                 TX
                                                                         RX                   Chip
                                 Chip                8   passive cable 8                     [DUT]                                                                                    DAC


                                     Pattern
                                                                         Pattern
                                    generator
                                                                         verifer


                  All 8 lanes enabled with 850Gb/s
                   data transition
                  5 meters OSFP DAC cable                                                                                               5 meters
                                                                                                                                           850G
                                                                                                                                           Cable

© 2021 IEEE                                                   8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                                           44 of 48

---

Measurement For Cable Setup
                                                                                                                                                         Bump to Bump Loss
                                                                                                           Component USED
                                                                                                                                                           @ Nyquist [dB]


                                                @26.56GHZ loss= -30.1 to                                          Cable Loss                                          >32
                                                       -32.7dB


                                                                                                   Tx and Rx boards (cable
                                                                                                    connectors)+ package                                              9.0
                                                                                                            loss

                                                                                                              Total Loss
                                                                                                                                                                    >41.0
                                                                                                            (Bump to Bump)


                  PRBS31 pattern is used
                  BER < 1.0e-6 and SNR > 19dB
© 2021 IEEE                                              8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                                45 of 48

---

State-of-the-art Comparison
                                                ISSCC 2020             ISSCC 2019                    ISSCC 2019                   ISSCC 2018                      This Work
                                                T. Ali                 C. Loi                        M. Pisati                    P. Upadhyaya
                 Technology                     7nm                    16nm                          7nm                          16nm                            7nm
                 Data Rate [Gb/s]               112                    106                           60                           56                              112
                 Architecture                   ADC/DSP                ADC/DSP                       ADC/DSP                      ADC/DSP                         ADC/DSP
                 Loss @ Nyquist [dB]            38.9                   -                             42.5                         32                              41.5
                 RX SNDR [dB]                   34.3                   33                            30                           -                               35
                 Power Supply [V]               0.85/1.2               -                             0.9/0.75                     0.85/0.9/1.2/1.8                0.65/0.94/1.15
                 TX Swing [mV]                  650                    1100                          900                          1000                            1000
                 TX SNDR [dB]                   36                     -                             -                            -                               40
                 Energy/bit [pJ/b]              4.02                   8.5                           4.36                         9.5                             6.51
                                                (analog)                                                                                                          (analog + digital)

                 Area/lane [mm2]                0.385                  1.54                          0.468                        2.2                             0.92
                                                (analog)                                                                                                          (analog + digital)


© 2021 IEEE                                            8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                                          46 of 48

---

Conclusion
                  We presented a transceiver architecture capable of
                   supporting 112Gb/s data rate and equalizing >40dB
                   channel loss.
                  The bandwidth-enhancement technique in the TX/RX
                   achieves >30GHz signal bandwidth.
                  This work demonstrates a long reach and low power 8-
                   lane retimer with 8x112Gb/s, enabling next generation of
                   data center line card applications.




© 2021 IEEE                                     8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                      47 of 48

---

Acknowledgment
                  The authors would like to thank validation, system
                   hardware and layout teams for their dedication and
                   support.




© 2021 IEEE                                     8.7: A 112Gb/s ADC-DSP based PAM-4 Transceiver for Long Reach Applications with >40dB Channel Loss in 7nm FinFET
International Solid-State Circuits Conference                                                                                                                      48 of 48

---

A 112Gb/s PAM-4 Low-Power 9-Tap Sliding-Block
    DFE in a 7nm FinFET Wireline Receiver

James Bailey1, Hossein Shakiba1, Ehud Nir2, Grigory Marderfeld2, Peter Krotnev2, Marc-
                            Andre LaCroix2, David Cassan1



                    Huawei Canada Research Center
                        1Toronto, Ontario, 2Ottawa, Ontario

---

Self Introduction
                                                                                 • James Bailey received B.A.Sc. and M.Eng
                                                                                   degrees in computer and electrical engineering
                                                                                   both from the University of Toronto, in 2009 and
                                                                                   2015 respectively.
                                                                                 • Senior Staff Engineer at Huawei Technologies
                                                                                   Canada in Toronto, since 2017 as a principal
                                                                                   architect of the digital control and signal
                                                                                   processing functions for high-speed chip-to-chip
                                                                                   circuits for wireline communication.
                                                                                 • Previously worked on high-speed interfaces at
                                                                                   Rambus/Semtech/Gennum from 2011-2017,
                    Imperial Palace East Gardens, Tokyo, 22 May 2019
                                                                                   and AMD from 2008-2011.

© 2021 IEEE                                                             8.8: A 112Gb/s PAM-4 Low-Power 9-Tap Sliding-Block DFE in a 7nm FinFET Wireline Receiver
International Solid-State Circuits Conference                                                                                                                      2 of 37

---

Outline
         •        Motivation and background
         •        Goals and System overview
         •        Sliding-Block DFE Architecture
         •        Simulated performance and logic synthesis
         •        Silicon and measurements
         •        Conclusions




© 2021 IEEE                                     8.8: A 112Gb/s PAM-4 Low-Power 9-Tap Sliding-Block DFE in a 7nm FinFET Wireline Receiver
International Solid-State Circuits Conference                                                                                              3 of 37

---

Outline
         •        Motivation and background
         •        Goals and System overview
         •        Sliding-Block DFE Architecture
         •        Simulated performance and logic synthesis
         •        Silicon and measurements
         •        Conclusions




© 2021 IEEE                                     8.8: A 112Gb/s PAM-4 Low-Power 9-Tap Sliding-Block DFE in a 7nm FinFET Wireline Receiver
International Solid-State Circuits Conference                                                                                              4 of 37

---

The Sliding Block DFE




                                                                                           SB-DFE!

         • A method for implementing very long DSP-DFEs at lower power
           and area than same-length conventional DFE/FFE DSP
         • Achieves same performance as traditional same-length DFE
         • An implemented 9-tap SB-DFE in 7nm FinFET
© 2021 IEEE                                         8.8: A 112Gb/s PAM-4 Low-Power 9-Tap Sliding-Block DFE in a 7nm FinFET Wireline Receiver
International Solid-State Circuits Conference                                                                                                  5 of 37

---

Current State of the Art
                            𝑣𝑣𝑅𝑅𝑅𝑅              𝑣𝑣𝐶𝐶𝐶𝐶𝐶𝐶𝐶𝐶                                                                                          𝑣𝑣𝐹𝐹𝐹𝐹𝐹𝐹         𝑣𝑣𝐷𝐷𝐷𝐷𝐷𝐷

                                         CTLE                 ADC                                           ⋯
       112Gb/s
            >36dB                    20-25dB                 7 bits                  FFE: 5 pre + 7 post taps                                                          DFE: 2 taps


                                                                      Work                      [1]           [2]          [3]         [4]
                                                                      FFE Length             15/25            31            7          16
                                                                      DFE Length                 2             1            1            1
                                                                 DSP configurations of recent 112Gb/s LR receivers

© 2021 IEEE                                                               8.8: A 112Gb/s PAM-4 Low-Power 9-Tap Sliding-Block DFE in a 7nm FinFET Wireline Receiver
International Solid-State Circuits Conference                                                                                                                                        6 of 37

---

FFE versus DFE
                                                     𝑣𝑣𝐹𝐹𝐹𝐹𝐹𝐹           𝑣𝑣𝐷𝐷𝐷𝐷𝐷𝐷                               FFE Pros and Cons

                                                ⋯                                                               Area & power grow
                                                                                                                 linearly with # of taps
                                                                                                               • Noise enhancement

               FFE Area & Power                      DFE Area & Power
                                                                                                               DFE Pros and Cons
                                                                                                                No noise enhancement
                                                                                                               • Timing Closure Issue
                                                                                                               • Area & power grow
                                                                                                                 exponentially w/ # of taps
                         # of taps                                    # of taps
© 2021 IEEE                                          8.8: A 112Gb/s PAM-4 Low-Power 9-Tap Sliding-Block DFE in a 7nm FinFET Wireline Receiver
International Solid-State Circuits Conference                                                                                                   7 of 37

---

FFE versus DFE
                                                     𝑣𝑣𝐹𝐹𝐹𝐹𝐹𝐹           𝑣𝑣𝐷𝐷𝐷𝐷𝐷𝐷                               FFE Pros and Cons

                                                ⋯                                                               Area & power grow
                                                                                                                 linearly with # of taps
                                                                                                               • Noise enhancement

               FFE Area & Power                      DFE Area & Power
                                                                                                               DFE Pros and Cons
                                                                                                                No noise enhancement
                                                                                                               • Timing Closure Issue
                                                                                                               • Area & power grow
                                                                                                                 exponentially w/ # of taps
                         # of taps                                    # of taps
© 2021 IEEE                                          8.8: A 112Gb/s PAM-4 Low-Power 9-Tap Sliding-Block DFE in a 7nm FinFET Wireline Receiver
International Solid-State Circuits Conference                                                                                                   8 of 37

---

Outline
         •        Motivation and background
         •        Goals and System overview
         •        Sliding-Block DFE Architecture
         •        Simulated performance and logic synthesis
         •        Silicon and measurements
         •        Conclusions




© 2021 IEEE                                     8.8: A 112Gb/s PAM-4 Low-Power 9-Tap Sliding-Block DFE in a 7nm FinFET Wireline Receiver
International Solid-State Circuits Conference                                                                                              9 of 37

---

Receiver System Architecture
                                                         RX
                                                                                 RX-DSP                Conventional
                                                                                                 5-Tap Pre       2-Tap
                                                                                                 7-Tap Post       DFE
                                                                                                    FFE




                                                                                                                                                   PRBS Check
                                                                                                              This work
                                                 Input    AFE   56GS/s                            5-Tap Pre                 9-Tap
                                                                 ADC                                 FFE                   SB-DFE


                                                                                                    LMS

                                                                                               2-Tap Pre                   Baud-Rate
                                                                                               2-Tap Post                    CDR
                                                                                                  FFE
                                                  Ref     PLL     PI




         • This work is an experimental DSP implemented in the Rx of 8.4 [1]
© 2021 IEEE                                                     8.8: A 112Gb/s PAM-4 Low-Power 9-Tap Sliding-Block DFE in a 7nm FinFET Wireline Receiver
International Solid-State Circuits Conference                                                                                                                   10 of 37

---

Overall Approach

         • Observation: Without timing challenges DFE is lower complexity
           and can be higher performance than FFE

         • Approach:
                  1. Break feedback loop without significant transformations to the canonical
                     DFE or overhead [6]
                  2. Pipeline to meet timing




© 2021 IEEE                                       8.8: A 112Gb/s PAM-4 Low-Power 9-Tap Sliding-Block DFE in a 7nm FinFET Wireline Receiver
International Solid-State Circuits Conference                                                                                                11 of 37

---

Outline
         •        Motivation and background
         •        Goals and system overview
         •        Sliding-Block DFE Architecture
         •        Simulated performance and logic synthesis
         •        Silicon and measurements
         •        Conclusions




© 2021 IEEE                                     8.8: A 112Gb/s PAM-4 Low-Power 9-Tap Sliding-Block DFE in a 7nm FinFET Wireline Receiver
International Solid-State Circuits Conference                                                                                              12 of 37

---

T-Tap DFE Decisor

                                           x[n]                                                                                                           𝑥𝑥𝑛𝑛
                                                                                                          𝑦𝑦𝑛𝑛−1                                                            𝑦𝑦𝑛𝑛
              y[n-1]                                  y[n]                                                                                                                𝑦𝑦𝑛𝑛−1
                                   x                 y[n-1]
                                                                                                          𝑦𝑦𝑛𝑛−2
                       Tap 1                                                                                 ⋮                                      T-Tap                    ⋮
                                                +                                                                                                                𝑌𝑌𝑛𝑛 =
             …




                                                      …                                          𝑌𝑌𝑛𝑛−1 =                                          Decisor                   ⋮
                                                                                                             ⋮
              y[n-T]                                y[n-T+1]
                                   x                                                                         �                                                               �
                                                                                                          𝑦𝑦𝑛𝑛−𝑇𝑇                                         𝑦𝑦𝑛𝑛          𝑦𝑦𝑛𝑛−𝑇𝑇+1
                       Tap T

                                            y[n]




© 2021 IEEE                                                    8.8: A 112Gb/s PAM-4 Low-Power 9-Tap Sliding-Block DFE in a 7nm FinFET Wireline Receiver
International Solid-State Circuits Conference                                                                                                                                   13 of 37

---

A Conventional DFE
                                                          4-symbol-parallel example


                                                  𝑥𝑥𝑛𝑛             𝑥𝑥𝑛𝑛+1                   𝑥𝑥𝑛𝑛+2                      𝑥𝑥𝑛𝑛+3
                                                                            Samples

                                                Decisor         Decisor                   Decisor                    Decisor


                                                                            Decisions




© 2021 IEEE                                                8.8: A 112Gb/s PAM-4 Low-Power 9-Tap Sliding-Block DFE in a 7nm FinFET Wireline Receiver
International Solid-State Circuits Conference                                                                                                         14 of 37

---

Transforming DFE to SB-DFE
                                                                4-symbol-parallel example
                                                               𝑥𝑥𝑛𝑛                      𝑥𝑥𝑛𝑛+1                   𝑥𝑥𝑛𝑛+2                      𝑥𝑥𝑛𝑛+3
                                                                                                  Samples

                                                             Decisor                  Decisor                   Decisor                    Decisor
                         DFE

                                                                                                  Decisions

                                                    𝑥𝑥𝑛𝑛−2    𝑥𝑥𝑛𝑛−1                 𝑥𝑥𝑛𝑛                      𝑥𝑥𝑛𝑛+1                  𝑥𝑥𝑛𝑛+2                    𝑥𝑥𝑛𝑛+3
                                                                                                   Samples


           SB-DFE                       0         Decisor    Decisor                 Decisor                    Decisor                   Decisor                Decisor

                                                                                                 Decisions
                                                Replace feedback with
                                                 a decisor “runway”
© 2021 IEEE                                                           8.8: A 112Gb/s PAM-4 Low-Power 9-Tap Sliding-Block DFE in a 7nm FinFET Wireline Receiver
International Solid-State Circuits Conference                                                                                                                              15 of 37

---

SB-DFE Architecture
                                                                                               Parallel Data BUS

                               h samples                   ...                               ...                                                                        ...
                             from previous                                                                                  ......
                                  cycle              1st k samples               2nd k samples                                                           Last k samples

                                            ...            ...
                                          History         Decode

                                                                    ...                      ...
                                                                   History                Decode
                                                                                                                          ...                ...                        ...
                                                                                                                                           History                 Decode




                                                    1st k Decisions             2nd k Decisions                                                         Last k Decisions

© 2021 IEEE                                                                  8.8: A 112Gb/s PAM-4 Low-Power 9-Tap Sliding-Block DFE in a 7nm FinFET Wireline Receiver
International Solid-State Circuits Conference                                                                                                                                 16 of 37

---

SB-DFE Architecture

                                                                                               b
                                                      h                                                                                       k
                                                                                               x[n]



           0
                           T-Tap
                          Decisor
                                                 T-Tap
                                                Decisor
                                                           …       T-Tap
                                                                  Decisor
                                                                                             T-Tap
                                                                                            Decisor
                                                                                                                      T-Tap
                                                                                                                     Decisor
                                                                                                                                             …             T-Tap
                                                                                                                                                          Decisor
                                                                                                                                                                     T-Tap
                                                                                                                                                                    Decisor




                                                                                               y[n]



© 2021 IEEE                                                    8.8: A 112Gb/s PAM-4 Low-Power 9-Tap Sliding-Block DFE in a 7nm FinFET Wireline Receiver
International Solid-State Circuits Conference                                                                                                                                 17 of 37

---

Block Performance Settling
                                                                                                           Samples

                                         BER    0
                                                     T-Tap
                                                    x[n]
                                                    Decisor
                                                               T-Tap
                                                              x[n]
                                                              Decisor
                                                                         T-Tap
                                                                        Decisor
                                                                                      …         T-Tap
                                                                                               Decisor
                                                                                                              T-Tap
                                                                                                             Decisor
                                                                                                                             T-Tap
                                                                                                                            Decisor
                                                                                                                                            T-Tap
                                                                                                                                           Decisor
                                                                                                                                                         …             T-Tap
                                                                                                                                                                      Decisor
                                                                                                                                                                                 T-Tap
                                                                                                                                                                                Decisor




                                                                                                                                                  Decisions
                        Unequalized
                          slicer BER




                      Traditional
             same-length DFE BER                                                      …                                                                  …

                                                                                        Symbol Position in Block

         •        BER improves consecutively through block until it reaches traditional DFE performance
                  •         Same behaviour as initially turning on a traditional DFE
         •        Use first ℎ decisions internally and then discard them
© 2021 IEEE                                                                8.8: A 112Gb/s PAM-4 Low-Power 9-Tap Sliding-Block DFE in a 7nm FinFET Wireline Receiver
International Solid-State Circuits Conference                                                                                                                                             18 of 37

---

Block Sizing

         • History size ℎ of block determined by performance settling
           characteristics of target channel(s)
         • Decode size 𝑘𝑘 of block sets balance between decode latency and
           computational overhead compared to canonical same-length DFE

                                                      𝐿𝐿𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎 ∝ ℎ + 𝑘𝑘 = 𝑏𝑏

                                                                               ℎ + 𝑘𝑘 𝑏𝑏
                                                𝑂𝑂𝑣𝑣𝑣𝑣𝑣𝑣ℎ𝑒𝑒𝑒𝑒𝑒𝑒 𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓 =       =
                                                                                 𝑘𝑘    𝑘𝑘


© 2021 IEEE                                           8.8: A 112Gb/s PAM-4 Low-Power 9-Tap Sliding-Block DFE in a 7nm FinFET Wireline Receiver
International Solid-State Circuits Conference                                                                                                    19 of 37

---

Block Seeding
                                                                                                         Samples
                                    Seed
                      Small
                       FFE
                                                 T-Tap
                                                x[n]
                                                Decisor
                                                           T-Tap
                                                          x[n]
                                                          Decisor
                                                                     T-Tap
                                                                    Decisor
                                                                                  …          T-Tap
                                                                                            Decisor
                                                                                                             T-Tap
                                                                                                            Decisor
                                                                                                                             T-Tap
                                                                                                                            Decisor
                                                                                                                                             T-Tap
                                                                                                                                            Decisor
                                                                                                                                                           …        T-Tap
                                                                                                                                                                   Decisor
                                                                                                                                                                              T-Tap
                                                                                                                                                                             Decisor



                                                                                                                                                   Decisions
                                    BER




             Unequalized BER

                       Seed BER


     Same-length DFE BER
                                                                                  …                                                                        …

                                                                                     Symbol Position in Block

         •        Block can be seeded with 𝑇𝑇 prior decision estimates to accelerate
                  performance settling
© 2021 IEEE                                                             8.8: A 112Gb/s PAM-4 Low-Power 9-Tap Sliding-Block DFE in a 7nm FinFET Wireline Receiver
International Solid-State Circuits Conference                                                                                                                                          20 of 37

---

Block Seeding

         • Seed does not need reliable BER to work well
         • Faster performance settling allows smaller history sizes
         • Variety of techniques can be used to generate the seed
                  •         Independent of SB-DFE
         • Implemented design can select seed from one of two already
           available FFEs
                  1. 5-tap pre/post-cursor CDR FFE
                  2. 5-tap precursor data path FFE



© 2021 IEEE                                     8.8: A 112Gb/s PAM-4 Low-Power 9-Tap Sliding-Block DFE in a 7nm FinFET Wireline Receiver
International Solid-State Circuits Conference                                                                                              21 of 37

---

Outline
         •        Motivation and background
         •        Goals and system overview
         •        Design details
         •        Simulated performance and logic synthesis
         •        Silicon and measurements
         •        Conclusions




© 2021 IEEE                                     8.8: A 112Gb/s PAM-4 Low-Power 9-Tap Sliding-Block DFE in a 7nm FinFET Wireline Receiver
International Solid-State Circuits Conference                                                                                              22 of 37

---

Simulated Performance
        10-0
                                                           SB-DFE Seed: Zero-Seeded                                                                                SB-DFE Seed: FFE-Equalized
        10-1

        10-2
BER




        10-3

        10-4                                                                                                 Seed BER Performance Level

        10-5
                                                     Traditional DFE Performance Level                                                                         Traditional DFE Performance Level
        10-6
                         0                      10                20                            30              0                             10                         20                 30
                                                                        Symbol Position in the Block

         • Ideal ISI channel
         • With and without FFE pre/post equalized seed
© 2021 IEEE                                                         8.8: A 112Gb/s PAM-4 Low-Power 9-Tap Sliding-Block DFE in a 7nm FinFET Wireline Receiver
International Solid-State Circuits Conference                                                                                                                                                   23 of 37

---

Logic Synthesis in 7nm FinFET

                                                    Synthesized SB-DFE, h = T+2, k = 64
                                                    Implemented SB-DFE
                                                    Implemented Reference DFE
                                                    Implemented Reference DFE + FFE
                                                    2-Tap DFE + Extrapolated FFE
                              Gate Area (µm2)




                                                                       Number of Postcursor Taps
© 2021 IEEE                                                      8.8: A 112Gb/s PAM-4 Low-Power 9-Tap Sliding-Block DFE in a 7nm FinFET Wireline Receiver
International Solid-State Circuits Conference                                                                                                               24 of 37

---

Logic Synthesis
         • All results are 112Gb/s DSPs at 1 GHz with suitable timing margin
         • Silicon SB-DFE implemented with ℎ = 16, 𝑘𝑘 = 64 and test features
         • Indicated area of reference DSP only includes FFE post taps
         • Synthesized SB-DFE is 50% to 60% smaller than extrapolated
           reference DSP
         • Silicon SB-DFE is 30% smaller than implemented reference DSP
         • Incremental cost of SB-DFE tap is about ⅔ of the FFE




© 2021 IEEE                                      8.8: A 112Gb/s PAM-4 Low-Power 9-Tap Sliding-Block DFE in a 7nm FinFET Wireline Receiver
International Solid-State Circuits Conference                                                                                               25 of 37

---

Pipelining
                                                                                             Input Samples




                                                 T-Tap        T-Tap                   T-Tap                       T-Tap                      T-Tap           T-Tap
                            Seed                             Decisor                 Decisor                     Decisor                    Decisor
                                                Decisor                                                                                                     Decisor


                                                  Example only
                                                                                                                     Output Decisions

         • Feed-forward cut-set pipelining
         • Implemented pipelining is sparser and cuts through decisor logic
© 2021 IEEE                                                      8.8: A 112Gb/s PAM-4 Low-Power 9-Tap Sliding-Block DFE in a 7nm FinFET Wireline Receiver
International Solid-State Circuits Conference                                                                                                                         26 of 37

---

Outline
         •        Motivation and background
         •        Goals and system overview
         •        Design details
         •        Simulated performance and logic synthesis
         •        Silicon and measurements
         •        Conclusions




© 2021 IEEE                                     8.8: A 112Gb/s PAM-4 Low-Power 9-Tap Sliding-Block DFE in a 7nm FinFET Wireline Receiver
International Solid-State Circuits Conference                                                                                              27 of 37

---

Implemented DSP
        64 x 7b samples                                                                                      9-Tap SB-DFE, h = 16, k = 64
          from ADCs                                                                                                                                                    64 x 2b
                                                  5-Tap Pre
                                                Data path FFE                                                 Input samples                                Output
                                                                 64 x 12b                                                                                  Error
                                                                                                                                           Seed


                                                                                          Seed Generation                                                    64 x 2b
                                                                            9 x 12b
                                                 2-Tap Pre                                                          D Q           9 x 2b                         LMS Tap
                                                                                                                  D Q
                                                 2-Tap Post                                                      D Q                                            Adaptation
                                                  CDR FFE                                                                                                         Engine




© 2021 IEEE                                                     8.8: A 112Gb/s PAM-4 Low-Power 9-Tap Sliding-Block DFE in a 7nm FinFET Wireline Receiver
International Solid-State Circuits Conference                                                                                                                                    28 of 37

---

Channel and DFE Taps
        1.2
                                                        Adapted DFE Taps
        1.0                                                                                                             0
                                                        Measured Pulse Response at ADC Output
        0.8
        0.6
        0.4
                                                    36 dB                                                              -10
        0.2                                                                                                            -20
        0.0
       -0.2                                                                                                            -30




                                                                                                             IL (dB)
       -0.4
        1.2
                                                                                                                       -40
        1.0
                                                                                                                       -50
        0.8                                                                                                                             36dB Channel
                                                    45 dB
        0.6
                                                                                                                       -60              45dB Channel
        0.4
        0.2                                                                                                            -70
        0.0
       -0.2                                                                                                            -80
       -0.4                                                                                                                  0                10            20         30     40
              -4              -2                0   2       4           6               8               10
                                                                                                                                                     Frequency (GHz)
       •           Measured pulse response matches adapted DFE taps
       •           Higher order taps (4+) accumulate to ~5% of cursor
       •           CTLE is not yet co-optimized to leave more post to SB-DFE
                   •      Existing algorithms designed for reference 2T DFE
© 2021 IEEE                                                      8.8: A 112Gb/s PAM-4 Low-Power 9-Tap Sliding-Block DFE in a 7nm FinFET Wireline Receiver
International Solid-State Circuits Conference                                                                                                                               29 of 37

---

112Gb/s PAM-4 Bathtub Curves
                          36dB Channel @ 112Gb/s




                                                                  BER
                          45dB Channel @ 112Gb/s




                                                                                                                      UI
© 2021 IEEE                                        8.8: A 112Gb/s PAM-4 Low-Power 9-Tap Sliding-Block DFE in a 7nm FinFET Wireline Receiver
International Solid-State Circuits Conference                                                                                                 30 of 37

---

Block Performance Settling
                                                                         Data Rate:                  112Gb/s
                                                                         Modulation:                 PAM-4
                                                                         FFE:                        5-Tap Precursor
                                                                         SB-DFE:                     9-Tap, Block Size = 80, History = 16, Decode = 64
                                                                         SB-DFE Seed:                5-Tap Precursor FFE
                                                                         Channel 1:                  36dB IL @ 28GHz
                                                                         Channel 2:                  45dB IL @ 28GHz
                  BER




                                                                    Symbol Position in the Block
© 2021 IEEE                                            8.8: A 112Gb/s PAM-4 Low-Power 9-Tap Sliding-Block DFE in a 7nm FinFET Wireline Receiver
International Solid-State Circuits Conference                                                                                                            31 of 37

---

Improved Noise Tolerance
                                                            0.35

                                                                0.3
                                        Noise Tolerance Delta
                                                            0.25
                                              ( mVrms)
                                                                0.2

                                                            0.15

                                                                0.1

                                                            0.05

                                                                 0
                                                                      32   34         36                38               40                42                44            46
                                                                                                   Insertion Loss (dB)

            •         LR wireline receivers challenged by crosstalk noise (ICN)
            •         Increased tolerance of 0.2mVrms over reference DSP at target BER 1E-5
                      •        Co-optimizing CTLE settings may yield more
© 2021 IEEE                                                                     8.8: A 112Gb/s PAM-4 Low-Power 9-Tap Sliding-Block DFE in a 7nm FinFET Wireline Receiver
International Solid-State Circuits Conference                                                                                                                                   32 of 37

---

Forward Error Correction
         • Measured error free on 36 dB channel for more than 48 hours
                  •         KP4 RS(544,514) code
                  •         No direct visibility into error burst behaviour but error-free performance
                            confirms SB-DFE functions well and does not break FEC
         • To stress SB-DFE error propagation Tx FIR configured to push
           first post-cursor as high as 0.43 before seeing post-FEC errors
                  •         Larger first post than on the 45 dB channel
                  •         0.5 tap value will substantially increase error propagation probability for
                            any DFE




© 2021 IEEE                                          8.8: A 112Gb/s PAM-4 Low-Power 9-Tap Sliding-Block DFE in a 7nm FinFET Wireline Receiver
International Solid-State Circuits Conference                                                                                                   33 of 37

---

Area & Power Consumption
                                                 DSP         Gate Area                  Digital Power
                                                 Variant       [µm2]                        [mW]

                                                 Reference     36372                              212
                                                 SB-DFE        23367                              175


       • Both power and area reduced
       • Gate area includes DFE and data path FFE including
         adaptation and test hooks
       • Digital power measured on 45 dB channel
       • Note: digital power includes significantly more logic
         than DSP
© 2021 IEEE                                                   8.8: A 112Gb/s PAM-4 Low-Power 9-Tap Sliding-Block DFE in a 7nm FinFET Wireline Receiver
International Solid-State Circuits Conference                                                                                                            34 of 37

---

Outline
         •        Motivation and background
         •        Goals and system overview
         •        Design details
         •        Simulated performance and logic synthesis
         •        Silicon and measurements
         •        Conclusions




© 2021 IEEE                                     8.8: A 112Gb/s PAM-4 Low-Power 9-Tap Sliding-Block DFE in a 7nm FinFET Wireline Receiver
International Solid-State Circuits Conference                                                                                              35 of 37

---

Summary Table
                                                                             [1]
                                                This Work                                                    [2] Xilinx                   [3] Rambus   [4] Intel
                                                                          Reference
                                                 SB-DFE                                                    ISSCC 2020                      VLSI 2020 JSSC 4/2020
                                                                            DSP
                Technology                       7nm FinFET               7nm FinFET                        7nm FinFET                     7nm FinFET     7nm FinFET
                Data rate [Gb/s]                    112                      112                               112                            112            112
                Modulation                         PAM-4                    PAM-4                             PAM-4                          PAM-4          PAM-4
                ADC Resolution [bit]                  7                        7                                7                             6+1             7
                Digital Supply Voltage              0.68                     0.68                                -                              -              -
                Number of FFE Pre Taps                5                        5
                                                                                                                     31                               7       16
                Number of FFE Post Taps               0                        7
                Number of DFE Taps                    9                        2                                1                                1              1
                                                     36                       36                               37.5                             36             35
                IL [dB] @ Nyquist
                                                     45                       45                                 -                               -              -
                                                2E-11 (36 dB)            2E-10 (36 dB)                    1E-8 (37.5 dB)                   2E-5 (36 dB)   1E-6 (35 dB)
                BER (IL)
                                                2E-6 (45 dB)              2E-6 (45 dB)                                 -                              -        -
                DSP Gate Area [µm2]                23367                        36372                                  -                              -        -
                Digital Power [mW]                  175                          212                                   -                              -        -

© 2021 IEEE                                                8.8: A 112Gb/s PAM-4 Low-Power 9-Tap Sliding-Block DFE in a 7nm FinFET Wireline Receiver
International Solid-State Circuits Conference                                                                                                                            36 of 37

---

Summary

     • We introduce a new DSP-DFE architecture: the SB-DFE
     • It can achieve the same performance as a traditional same-length
       DFE
     • Practical implementations are feasible at very long lengths, up to and
       exceeding 30 taps
     • A 9T SB-DFE is implemented in a 7nm FinFET receiver
     • The implemented SB-DFE is smaller than the reference DFE/FFE
       DSP and demonstrates lower power and higher performance



© 2021 IEEE                                     8.8: A 112Gb/s PAM-4 Low-Power 9-Tap Sliding-Block DFE in a 7nm FinFET Wireline Receiver
International Solid-State Circuits Conference                                                                                              37 of 37

---

