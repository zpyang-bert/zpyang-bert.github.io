---
layout: post
title:      "lecture4 ee720 channel pulse model 深度学习报告"
date:       2026-04-21 09:28:02
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

Lecture 4: Channel Pulse Model & Modulation Schemes




                   Sam Palermo
           Analog & Mixed-Signal Center
               Texas A&M University

![课程封面](/img/serdes/fundamentals/lectures/lecture10_ee720_jitter_深度学习报告/_images/img-000.jpg)
> 🔍 深度说明：
> 【研究背景】这是ECEN720第四讲的封面，主题是信道脉冲响应和码间干扰（ISI）模型，是均衡器设计的核心理论基础，所有均衡算法都是为了消除码间干扰。
> 【核心结论】本讲内容覆盖：线性时不变系统理论、信道脉冲响应、阶跃响应、码间干扰产生原理、眼图的形成、链路预算分析，是Serdes系统设计的核心理论基础。
> 【工程价值】理解码间干扰的产生原理是设计均衡器的前提，均衡器的系数计算、阶数选择都基于信道的脉冲响应特性；眼图是评估链路性能最直观的方法，所有Serdes的性能验证都基于眼图测量。
> 【落地注意】实际信道不是理想的线性时不变系统，存在非线性、温度漂移、工艺偏差等影响，均衡器必须支持自适应调整功能，才能适配实际信道的变化；眼图测量时需要注意采样深度，一般需要采集1e6以上的比特才能得到准确的眼图和误码率估计。


---

Announcements
• Lab 2 report and Prelab 3 due Feb 13

• Reference material
  • Peak distortion analysis paper by Casper
  • Notes from H. Song, Arizona State
  • Papers posted on PAM-2/4 transceivers




                                               2

![信道脉冲响应](/img/serdes/fundamentals/lectures/lecture1_ee720_intro_深度学习报告/_images/img-001.jpg)
> 🔍 深度说明：
> 【研究背景】这是典型高速信道的脉冲响应示意图，脉冲响应是线性系统的时域描述，包含了信道的所有特性，是均衡器设计的核心依据。
> 【核心结论】信道的脉冲响应h(t)是系统输入一个冲激信号时的输出响应，经过信道传输后的信号是输入信号和脉冲响应的卷积；由于信道是低通特性，脉冲响应会被展宽，导致相邻符号之间产生重叠，即码间干扰（ISI）。
> 【工程价值】均衡器的作用就是对信道的脉冲响应进行逆滤波，把展宽的脉冲压缩回原来的宽度，消除码间干扰；FFE/DFE均衡器的系数就是根据信道的脉冲响应计算得到的。
> 【落地注意】实际测量信道的脉冲响应需要用高速采样示波器，采样率至少是符号速率的4倍以上，才能得到准确的脉冲响应；同时需要平均多次测量结果，降低噪声的影响。


---

Agenda
• ISI and channel pulse model

• Peak distortion analysis

• Compare NRZ (PAM-2) and PAM-4 modulation




                                        3

![码间干扰](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/img-002.jpg)
> 🔍 深度说明：
> 【研究背景】这是码间干扰产生原理的示意图，码间干扰是高速链路中误码的主要来源，均衡器的主要作用就是消除码间干扰。
> 【核心结论】由于脉冲响应被展宽，每个符号的能量会扩散到相邻的符号周期中，对相邻符号产生干扰，这就是码间干扰；干扰的大小取决于脉冲响应在相邻采样点的幅度，幅度越大，干扰越严重。
> 【工程价值】码间干扰的大小直接决定了链路的误码率，没有均衡的情况下，码间干扰会导致眼图完全闭合，无法正常接收数据；均衡器可以把码间干扰降低到噪声水平以下，让眼图重新张开。
> 【落地注意】对于PAM4调制，由于电平间距只有NRZ的1/3，对码间干扰更加敏感，相同的码间干扰对PAM4的影响是NRZ的3倍，因此PAM4 Serdes需要更复杂的均衡器，均衡器的阶数也更高。


---

Inter-Symbol Interference (ISI)
• Previous bits residual state can distort the current bit,
  resulting in inter-symbol interference (ISI)
• ISI is caused by
   • Reflections, Channel resonances, Channel loss (dispersion)
• Pulse Response
                   y   1
                             t   c t   ht 
                                      1


      c 1 t                   ht                  c 1 t 
                                                                     y 1 t 




                                                                                  4

![眼图](/img/serdes/fundamentals/lectures/lecture1_ee720_intro_深度学习报告/_images/img-003.jpg)
> 🔍 深度说明：
> 【研究背景】这是眼图的形成原理示意图，眼图是评估高速链路性能最直观的方法，把多个符号周期的波形叠加在一起，就形成了类似眼睛的图案，因此称为眼图。
> 【核心结论】眼图的参数包括：1) 眼高：垂直方向的张开度，反映了噪声和干扰的大小，眼高越大，灵敏度越高；2) 眼宽：水平方向的张开度，反映了抖动的大小，眼宽越大，时序余量越大；3) 眼图的交叉点：反映了信号的上升/下降时间和占空比。
> 【工程价值】眼图是Serdes芯片验证的核心指标，所有Serdes的性能验收都基于眼图测量，要求在最坏情况下眼高>100mV，眼宽>0.3UI，才能保证误码率<1e-12。
> 【落地注意】眼图测量时需要注意采样示波器的带宽，至少需要是信号速率的3倍以上，否则测量得到的眼高会偏低，眼宽会偏窄，不能反映真实的链路性能；同时需要注意示波器的本底噪声，避免噪声被高估。


---

NRZ Data Modeling
• An NRZ data stream can be modeled as a
  superposition of isolated “1”s and “0”s

    Data = “1000101”



 “1” Symbol            ck1 t   u t  kT   u t  k  1T 


 “0” Symbol            ck0  t   ck1 t 
                                                1 t  0
[Song]                           where u t   
                                                0 t  0
                                                                      5

![链路预算](/img/serdes/fundamentals/lectures/lecture11_ee720_clocking_arch_plls_深度学习报告/_images/img-004.jpg)
> 🔍 深度说明：
> 【研究背景】这是高速链路的链路预算分析示意图，链路预算是Serdes系统设计的第一步，用来计算链路的总余量，判断是否可以满足误码率要求。
> 【核心结论】链路余量 = 接收端灵敏度 - 总损耗 - 总噪声 - 抖动代价 - 串扰代价；一般要求链路余量>3dB，保证在最坏情况下仍然可以正常工作。各部分损耗包括：信道插入损耗、反射损耗、均衡器噪声、CDR抖动等。
> 【工程价值】链路预算可以在设计早期判断链路是否可行，避免设计完成后才发现性能不足，节省开发时间和成本；同时可以指导各个模块的性能指标分配，比如均衡器需要补偿的损耗、CDR的抖动容忍度等。
> 【落地注意】链路预算必须考虑所有最坏情况：最高温度、最大工艺偏差、最长传输距离、最大串扰、最差阻抗匹配，所有参数都要留足够的余量，一般要求总余量>3dB，对可靠性要求高的场景需要>6dB。

