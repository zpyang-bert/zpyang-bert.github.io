---
layout: post
title:      "lecture3 ee720 tdr spar 深度学习报告"
date:       2026-04-21 09:25:41
author:     "Bert"
tags:
  - Fundamentals
  - Lecture
  - SerDes
  - TDR
  - 深度学习
---

ECEN720: High-Speed Links
            Circuits and Systems
                Spring 2023
Lecture 3: Time-Domain Reflectometry & S-Parameter Channel Models




                        Sam Palermo
                Analog & Mixed-Signal Center
                    Texas A&M University

![课程封面](/img/serdes/fundamentals/lectures/lecture10_ee720_jitter_深度学习报告/_images/img-000.jpg)
> 🔍 深度说明：
> 【研究背景】这是ECEN720第三讲的封面，主题是TDR时域反射计和S参数测量，是高速信道特性测量的核心技术，准确的信道测量是Serdes设计和验证的基础。
> 【核心结论】本讲内容覆盖：TDR工作原理、阻抗不连续的TDR响应、S参数测量方法、VNA矢量网络分析仪使用、测量校准技术、去嵌方法，是信号完整性工程师必备的测量技能。
> 【工程价值】所有高速链路的信道特性都需要通过实际测量得到，仿真结果必须和测量结果对齐，才能保证Serdes芯片在实际系统中正常工作；测量不准确会导致设计余量不足，甚至流片失败。
> 【落地注意】高频S参数测量对校准要求非常高，SOLT校准、TRL校准都必须严格按照流程操作，测试夹具的去嵌必须准确，否则测量结果会有很大误差；同时要注意测量时的防静电和阻抗匹配，避免损坏仪表。


---

Announcements
• Lab 1 report and Prelab 2 due Feb 6

• Reference Material Posted on Website
  • TDR theory application note
  • S-parameter notes




                                         2

![TDR工作原理](/img/serdes/fundamentals/lectures/lecture1_ee720_intro_深度学习报告/_images/img-001.jpg)
> 🔍 深度说明：
> 【研究背景】TDR时域反射计的工作原理示意图，TDR是测量传输线阻抗分布的核心工具，可以定位传输线上的阻抗不连续点（比如过孔、连接器、stub等）。
> 【核心结论】TDR的工作原理是向传输线发送一个阶跃信号，然后测量反射回来的信号，根据反射信号的幅度和时间，可以计算出阻抗不连续点的位置和阻抗值；反射系数Γ = (Z - Z0)/(Z + Z0)，阻抗高于Z0时反射为正，低于Z0时反射为负。
> 【工程价值】TDR是PCB信号完整性测试的必备工具，可以用来验证PCB的阻抗控制是否符合要求，定位阻抗不连续的位置，分析过孔、连接器的阻抗特性。
> 【落地注意】TDR的上升时间决定了测量的分辨率，上升时间越快，分辨率越高，对于112G Serdes的信道测量，需要使用上升时间<20ps的TDR，才能分辨出毫米级的阻抗不连续点；测量时需要注意线缆的校准，消除测试线缆的影响。


---

Agenda
• Interconnect measurement techniques
  • Time-domain reflectometry (TDR)
  • Network analyzer
• S-parameters
• Cascading S-parameter models
• Full S-parameter channel model
• Transient simulations
  • Impulse response generation
  • Eye diagrams
  • Inter-symbol interference

                                        3

![TDR响应示例](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/img-002.jpg)
> 🔍 深度说明：
> 【研究背景】这是典型传输线结构的TDR响应示例，展示了不同阻抗不连续点的TDR波形特征，是TDR测量结果分析的基础。
> 【核心结论】1) 开路：反射系数为+1，TDR波形跳变到2倍输入阶跃幅度；2) 短路：反射系数为-1，TDR波形跳变到0；3) 电容性不连续（比如过孔stub）：TDR波形出现向下的凹陷；4) 电感性不连续（比如引线）：TDR波形出现向上的凸起。
> 【工程价值】通过分析TDR波形，可以定位传输线上的阻抗不连续点的位置和类型，指导PCB设计优化，降低信号反射。
> 【落地注意】过孔stub是TDR测量中最常见的阻抗不连续点，112G链路中背钻后的残留stub必须控制在8mil以内，否则TDR会出现明显的凹陷，导致反射过大，链路余量不足。


---

Lecture References
• Majority of TDR material from Dally
  Chapter 3.4, 3.6 - 3.7

• Majority of s-parameter material from Hall
  “Advanced Signal Integrity for High-Speed
  Digital Designs” Chapter 9




                                               4

![S参数测量](/img/serdes/fundamentals/lectures/lecture1_ee720_intro_深度学习报告/_images/img-003.jpg)
> 🔍 深度说明：
> 【研究背景】这是VNA矢量网络分析仪测量S参数的原理示意图，S参数是频域的信道特性描述，是Serdes链路仿真的标准输入格式。
> 【核心结论】VNA通过向被测件发送扫频的正弦信号，测量每个频率点的入射波、反射波、传输波的幅度和相位，计算得到S参数；可以测量的参数包括插入损耗（S21）、回波损耗（S11）、串扰（S31/S41）等。
> 【工程价值】S参数是Serdes链路仿真的核心输入，所有的眼图仿真、误码率仿真、均衡器参数优化都基于准确的S参数，测量得到的S参数还可以用来验证仿真模型的准确性。
> 【落地注意】测量S参数时，频率范围需要覆盖到Serdes的Nyquist频率的2~3倍，比如112G PAM4 Serdes的Nyquist频率是14GHz，测量频率范围需要到40GHz以上，才能准确描述信道的高频特性；同时要注意测量的动态范围，一般要求>80dB，保证弱信号的测量精度。


---

Interconnect Modeling



• Why do we need interconnect models?
  • Perform hand calculations and simulations (Spice, Matlab, etc…)
  • Locate performance bottlenecks and make design trade-offs
• Model generation methods
  • Electromagnetic CAD tools
  • Actual system measurements
• Measurement techniques
  • Time-Domain Reflectometer (TDR)
  • Network analyzer (frequency domain)
                                                                      5

![S参数校准](/img/serdes/fundamentals/lectures/lecture11_ee720_clocking_arch_plls_深度学习报告/_images/img-004.jpg)
> 🔍 深度说明：
> 【研究背景】这是S参数测量的校准技术示意图，校准是保证S参数测量准确性的关键步骤，没有校准的测量结果是没有意义的。
> 【核心结论】常用的校准方法包括：1) SOLT校准：使用短路（Short）、开路（Open）、负载（Load）、直通（Thru）四个校准件，是最常用的同轴校准方法；2) TRL校准：使用直通（Thru）、反射（Reflect）、延迟线（Line），适合非同轴的PCB测量，精度更高；3) SOLR校准：适用于未知负载的情况。
> 【工程价值】准确的校准是S参数测量准确的前提，校准误差是S参数测量的最大误差来源，因此必须严格按照校准流程操作，定期校准校准件，保证校准精度。
> 【落地注意】PCB上的S参数测量一般采用TRL校准，需要在测试板上设计专门的TRL校准图形，校准件的阻抗必须准确，延迟线的长度需要根据测量频率范围来设计，保证校准精度。


---

Time-Domain Reflectometer (TDR)
                                                            [Agilent]




[Dally]

• TDR consists of a fast step generator and a high-speed
  oscilloscope
• TDR operation
   • Outputs fast voltage step onto channel
   • Observe voltage at source, which includes reflections
   • Voltage magnitude can be converted to impedance
   • Impedance discontinuity location can be determined by delay
• Only input port access to characterize channel
                                                                        6

![去嵌技术](/img/serdes/fundamentals/lectures/lecture1_ee720_intro_深度学习报告/_images/img-005.jpg)
> 🔍 深度说明：
> 【研究背景】这是S参数测量的去嵌技术示意图，去嵌是去掉测试夹具对测量结果的影响，得到真实被测件的S参数的技术。
> 【核心结论】测试夹具包括测试端口到被测件之间的走线、过孔、连接器等，这些部分的特性会叠加到测量结果中，必须通过去嵌技术去掉；常用的去嵌方法包括：2xThru去嵌、SOLT去嵌、TRL去嵌等。
> 【工程价值】如果不去掉测试夹具的影响，测量得到的S参数会包含夹具的损耗和反射，导致信道特性被高估或者低估，影响Serdes设计的准确性。
> 【落地注意】去嵌模型必须准确，夹具的S参数需要预先测量或者仿真得到，去嵌后的S参数必须满足无源、互易、因果的条件，否则不能用于链路仿真；去嵌后的插入损耗在低频段应该接近0dB，保证去嵌的正确性。

