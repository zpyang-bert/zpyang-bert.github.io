---
layout: post
title:      "lecture2 ee720 channels 深度学习报告"
date:       2026-04-21 09:22:48
author:     "Bert"
tags:
  - Channel
  - Fundamentals
  - Lecture
  - SerDes
  - 深度学习
---

ECEN720: High-Speed Links
            Circuits and Systems
                Spring 2023

Lecture 2: Channel Components, Wires, & Transmission Lines




                       Sam Palermo
               Analog & Mixed-Signal Center
                   Texas A&M University

![课程封面](/img/serdes/fundamentals/lectures/lecture2_ee720_channels_深度学习报告/_images/img-000.jpg)
> 🔍 深度说明：
> 【研究背景】这是ECEN720课程第二讲的封面，主题是信道组件、传输线理论，是Serdes设计的核心基础内容，所有高速链路的性能上限都由信道特性决定，因此信道分析是Serdes设计的第一步。
> 【核心结论】本讲内容覆盖：传输线理论、趋肤效应与介质损耗、S参数分析、信道建模、阻抗匹配、串扰分析，是信号完整性设计的核心基础。
> 【工程价值】掌握信道特性是Serdes系统设计的前提，均衡器架构选择、链路预算计算、眼图余量估计都需要基于准确的信道模型，错误的信道分析会直接导致芯片流片失败。
> 【落地注意】实际信道建模需要考虑 worst-case 情况：最高工作温度、最大工艺偏差、最长传输距离、最差阻抗匹配，所有参数都需要留足够的余量，保证量产良率。


---

Announcements
• Homework 1 due today
• Lab
  • Prelab 1 due Jan 30
  • Lab 1 report and Prelab 2 due Feb 6
  • TA Tong Liu
     • liut@tamu.edu
     • Office Hours M 10AM-12PM, WEB 160

• Reference Material Posted on Website
  • TDR theory application note
  • S-parameter notes

                                           2

![典型链路信道组件](/img/serdes/fundamentals/lectures/lecture2_ee720_channels_深度学习报告/_images/img-001.jpg)
> 🔍 深度说明：
> 【研究背景】这是典型高速链路的信道组件构成图，展示了从发送端芯片到接收端芯片之间的所有信号路径组件，每个组件都会带来信号劣化。
> 【核心结论】信道组件包括：1) 芯片封装：BGA封装的过孔、引线，带来插入损耗和反射；2) PCB走线：传输线、过孔、连接器，带来损耗、反射、串扰；3) 背板/线缆：长距离传输线，是损耗的主要来源；4) 接收端封装：和发送端类似。总插入损耗一般在10dB到40dB之间，取决于传输距离。
> 【工程价值】链路预算计算需要把每个组件的损耗都考虑进去，任何一个组件的损耗超出预期都会导致链路余量不足，无法正常工作。
> 【落地注意】PCB过孔的stub是高频损耗的重要来源，112G PAM4链路中必须采用背钻工艺去掉过孔stub，否则会带来额外的5~10dB损耗，导致链路失效；连接器选择也非常重要，高频连接器的插入损耗必须控制在1dB以内@14GHz。


---

Agenda
• Channel Components
  • IC Packages, PCBs, connectors, vias, PCB Traces
• Wire Models
  • Resistance, capacitance, inductance
• Transmission Lines
  • Propagation constant
  • Characteristic impedance
  • Loss
  • Reflections
  • Termination examples
  • Differential transmission lines
                                                      3

![传输线特性](/img/serdes/fundamentals/lectures/lecture2_ee720_channels_深度学习报告/_images/img-002.jpg)
> 🔍 深度说明：
> 【研究背景】这是传输线的特性阻抗公式和传播速度公式，是信号完整性分析的基础理论，高速信号必须按照传输线理论来处理，否则会出现严重的反射和信号劣化。
> 【核心结论】1) 特性阻抗Z0 = √(L/C)，PCB上的微带线特性阻抗一般控制在50Ω，差分线100Ω；2) 信号传播速度v = c / √εr，FR4板材的相对介电常数εr≈4，所以传播速度约为1.5e8 m/s，即每英寸信号延迟约为170ps。
> 【工程价值】特性阻抗匹配是高速链路设计的基本要求，阻抗不匹配会带来信号反射，导致码间干扰，降低眼图余量，严重时会导致链路无法工作。
> 【落地注意】PCB设计时必须严格控制传输线的阻抗公差，一般要求±10%以内，差分线还要控制两根线的长度差（skew）在5ps以内，否则会引入差分转共模噪声，降低接收灵敏度；同时需要考虑板材的εr随频率和温度的变化，实际设计时要留余量。


---

Channel Components
                              Packaged SerDes

                  Backplane trace

            Line card trace

           Edge connector

           Via stub
                                                        [Meghelli (IBM) ISSCC 2006]


   Pkg         Line card       Line card      Edge    Backplane
                 trace            via       connector    via
   Tx IC                            The Channel                   Backplane
                                                                  16” trace

   Pkg         Line card       Line card      Edge    Backplane
                 trace            via       connector    via
   Rx IC

                                                                                  4

![趋肤效应](/img/serdes/fundamentals/lectures/lecture2_ee720_channels_深度学习报告/_images/img-003.jpg)
> 🔍 深度说明：
> 【研究背景】这是趋肤效应的原理示意图，是高速信号在传输线中传播时的核心损耗来源之一，频率越高，趋肤效应越明显，损耗越大。
> 【核心结论】趋肤效应：高频交流信号在导体中传播时，电流会集中在导体的表面薄层流动，导致导体的等效电阻增大，损耗与√f成正比；趋肤深度δ = √(2/(ωμσ))，频率10GHz时，铜的趋肤深度约为0.66μm，远小于普通PCB铜线的厚度（35μm）。
> 【工程价值】趋肤效应是高频传输线损耗的主要来源之一，112G Serdes的Nyquist频率是14GHz，趋肤效应带来的损耗占总损耗的40%以上，是链路预算的重要组成部分。
> 【落地注意】为了降低趋肤效应带来的损耗，高速PCB可以采用粗糙度更低的铜箔（比如HVLP铜箔），减少信号的散射损耗；同时可以采用更粗的传输线，降低等效电阻，但需要注意阻抗匹配。


---

IC Packages
• Package style depends                     Package Type                Pin Count
                                   Small Outline Package (SOP)              8 – 56
  on application and pin
                                   Quad Flat Package (QFP)                 64 - 304
  count
                                   Plastic Ball Grid Array (PBGA)          256 - 420
                                   Enhanced Ball Grid Array (EBGA)         352 - 896
• Packaging technology             Flip Chip Ball Grid Array (FC-BGA)   1089 - 2116
  hasn’t been able to                   SOP                          QFP
  increase pin count at
  same rate as on-chip
  aggregate bandwidth
  • Leads to I/O constrained
    designs and higher data            PBGA                         FC-BGA
    rate per pin


      [Package Images - Fujitsu]
                                                                                       5

![介质损耗](/img/serdes/fundamentals/lectures/lecture2_ee720_channels_深度学习报告/_images/img-004.jpg)
> 🔍 深度说明：
> 【研究背景】这是介质损耗的原理示意图，是高频传输线的另一个核心损耗来源，频率越高，介质损耗越大，在10GHz以上频段，介质损耗占总损耗的比例超过趋肤效应。
> 【核心结论】介质损耗是由于交变电场下介质分子极化滞后带来的能量损耗，损耗与频率f成正比，损耗角正切tanδ是衡量介质损耗的核心参数；普通FR4板材的tanδ≈0.02@10GHz，高速板材（比如Megtron6）的tanδ≈0.003@10GHz，损耗低一个数量级。
> 【工程价值】高速链路的板材选择非常重要，25G以下速率可以用普通FR4，56G以上速率必须采用低损耗高速板材，112G以上速率必须采用超低损耗板材，否则链路损耗会超过均衡器的补偿范围。
> 【落地注意】高速板材的成本比普通FR4高很多，设计时需要根据实际速率要求选择合适的板材，平衡性能和成本；同时需要注意介质损耗随温度升高而增大，高温下的损耗会比常温高20%以上，链路预算必须考虑温度影响。


---

IC Package Examples
• Wirebonding is most          Standard Wirebond Package

  common die attach method
• Flip-chip packaging allows
  for more efficient heat      Flip-Chip/Wirebond Package
  removal
• 2D solder ball array on
  chip allows for more         Flip-Chip/Solder Ball Package
  signals and lower signal
  and supply impedance

                                [Package Images - Fujitsu]
                                                             6

![插入损耗曲线](/img/serdes/fundamentals/lectures/lecture2_ee720_channels_深度学习报告/_images/img-005.jpg)
> 🔍 深度说明：
> 【研究背景】这是不同长度的FR4传输线的插入损耗随频率变化的曲线，是Serdes设计时最常用的信道特性曲线，直接决定了均衡器需要的补偿范围。
> 【核心结论】插入损耗随频率升高而近似线性增大（dB/Hz），10英寸FR4传输线在10GHz下损耗约为15dB，20英寸约为30dB，30英寸约为45dB；损耗超过30dB时，普通的模拟均衡架构已经无法补偿，必须采用ADC+DSP架构。
> 【工程价值】插入损耗曲线是Serdes均衡器设计的核心输入，均衡器的带宽、增益范围、阶数都需要根据目标信道的损耗曲线来设计，才能保证补偿效果。
> 【落地注意】实际测量插入损耗时，必须采用SOLT校准去掉测试夹具的影响，得到真实的信道损耗；同时需要测量不同温度、不同板材批次的损耗曲线，覆盖所有worst-case情况。


---

IC Package Model

Bondwires             Package Trace
• L ~ 1nH/mm          • L ~ 0.7-1nH/mm
•Mutual L “K”         •Mutual L “K”
• Ccouple ~ 20fF/mm   • Clayer ~ 80-90fF/mm
                      •Ccouple ~ 40fF/mm




                                    [Dally]


                                              7

![串扰特性](/img/serdes/fundamentals/lectures/lecture2_ee720_channels_深度学习报告/_images/img-006.jpg)
> 🔍 深度说明：
> 【研究背景】这是传输线串扰的原理示意图，串扰是高速链路中除了损耗之外的另一个核心干扰来源，会导致接收端噪声增大，降低眼图余量。
> 【核心结论】串扰分为近端串扰（NEXT）和远端串扰（FEXT），是相邻传输线之间的电磁耦合导致的；串扰大小和线间距成反比，和耦合长度成正比，和频率成正比；高速链路中一般要求串扰控制在-30dB以下。
> 【工程价值】PCB设计时必须严格控制传输线的间距，避免串扰过大，导致链路余量不足；差分线的串扰比单端线小很多，因此高速链路都采用差分信号传输。
> 【落地注意】112G PAM4链路对串扰非常敏感，串扰超过-25dB就会导致误码率大幅上升，PCB设计时差分线之间的间距至少要达到3倍线宽（3W规则），同时要避免平行过长的走线，必要时可以加接地过孔隔离。


---

IC Package Model Comparisons

                     • FCB packaging allows
                       for much less chip
                       interface impedance

        [Intel]




                                              8

![S参数](/img/serdes/fundamentals/lectures/lecture2_ee720_channels_深度学习报告/_images/img-007.jpg)
> 🔍 深度说明：
> 【研究背景】S参数（散射参数）是描述线性网络端口特性的标准方法，是高速信道建模的标准格式，所有Serdes仿真都需要使用信道的S参数作为输入。
> 【核心结论】S参数是n×n的矩阵，对于差分对二端口网络，S11是回波损耗（反射），S21是插入损耗（传输），S12和S21相等（互易网络），S22是接收端回波损耗；一般要求S11<-15dB，保证阻抗匹配良好。
> 【工程价值】信道的S参数可以通过VNA（矢量网络分析仪）测量得到，也可以通过仿真软件计算得到，是Serdes链路仿真的核心输入，所有链路性能仿真（眼图、误码率）都基于S参数。
> 【落地注意】S参数测量时必须保证校准准确，测试夹具的影响必须去掉，否则得到的S参数不准确，会导致仿真结果和实际测试结果偏差很大；同时S参数必须是无源、互易、因果的，否则仿真会出现错误。

