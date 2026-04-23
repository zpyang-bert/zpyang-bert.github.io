---
layout: post
title:      "lecture8 ee720 rx adaptive eq 深度学习报告"
date:       2026-04-21 10:04:53
author:     "Bert"
tags:
  - Fundamentals
  - Lecture
  - RX
  - SerDes
  - 深度学习
---

ECEN720: High-Speed Links
        Circuits and Systems
            Spring 2023

Lecture 8: RX FIR, CTLE, DFE, & Adaptive Eq.




                  Sam Palermo
          Analog & Mixed-Signal Center
              Texas A&M University

![课程封面](/img/serdes/fundamentals/lectures/lecture10_ee720_jitter_深度学习报告/_images/img-000.jpg)
> 🔍 深度说明：
> 【研究背景】这是ECEN720第八讲，主题是接收端自适应均衡与判决反馈均衡器（DFE），DFE是中长距Serdes的核心均衡技术，能够有效消除码间干扰，同时不会放大噪声。
> 【核心结论】内容覆盖DFE原理、DFE架构、自适应均衡算法（LMS/MMSE）、自适应环路设计、DFE时序收敛问题、噪声抑制特性，是Serdes均衡设计的核心内容。
> 【工程价值】DFE是中长距链路的必备均衡技术，相比线性均衡，DFE不会放大噪声，在高损耗信道下性能优势明显，可以提升链路余量2~3dB，是当前56G/112G Serdes的标配功能。
> 【落地注意】DFE的反馈环路延迟是设计的最大挑战，必须小于1个符号周期（UI），否则会引入额外的码间干扰，112G Serdes的UI仅为8.9ps，对DFE电路的速度要求非常高，需要采用前瞻（Look-Ahead）DFE结构或者2倍采样结构来解决时序问题。


---

Announcements
• Lab 5 Report and Prelab 6 due Mar 27

• Equalization overview and circuits papers
  are posted on the website




                                              2

![DFE原理](/img/serdes/fundamentals/lectures/lecture1_ee720_intro_深度学习报告/_images/img-001.jpg)
> 🔍 深度说明：
> 【研究背景】判决反馈均衡器（DFE）的原理示意图，DFE是一种非线性均衡技术，利用已经判决出来的符号来消除后续符号的码间干扰。
> 【核心结论】DFE由反馈抽头和加法器组成，对已经判决的符号进行加权，从当前输入信号中减去判决符号带来的残余码间干扰；由于是基于已经判决的符号，DFE不会放大噪声，这是相比线性均衡的最大优势。
> 【工程价值】在高损耗信道下，线性均衡会放大噪声导致眼图无法张开，而DFE可以在不放大噪声的情况下消除码间干扰，链路性能比仅用线性均衡提升2~3dB，是中长距链路的必备技术。
> 【落地注意】DFE只能消除后游标（post-cursor）码间干扰，无法消除前游标（pre-cursor）码间干扰，因此DFE一般需要和CTLE/FFE配合使用，CTLE/FFE消除前游标干扰，DFE消除后游标干扰，达到最优均衡效果。


---

Agenda
• RX FIR equalization
• RX CTLE equalization
• RX DFE equalization
• Equalization adaptation techniques
• Advanced modulation/other techniques




                                         3

![DFE架构](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/img-002.jpg)
> 🔍 深度说明：
> 【研究背景】典型的DFE架构示意图，包括模拟DFE和数字DFE两种实现方式，各有优缺点。
> 【核心结论】模拟DFE在采样之前进行均衡，速度快功耗低，但精度低，调整麻烦；数字DFE在采样之后进行数字域均衡，精度高，调整灵活，但需要高速ADC，功耗高；当前主流架构是1~2 tap模拟DFE+多tap数字DFE，平衡功耗和性能。
> 【工程价值】混合架构DFE结合了模拟和数字DFE的优点，1 tap模拟DFE消除第一个最大的后游标干扰，剩余的后游标干扰由数字DFE消除，性能好，功耗适中，是当前112G Serdes的主流DFE架构。
> 【落地注意】第一tap DFE的反馈延迟必须小于1个UI，否则会引入额外的码间干扰，112G Serdes的UI仅为8.9ps，需要采用全定制高速电路设计，或者采用前瞻DFE结构，提前计算所有可能的判决结果，在判决后直接选择对应的结果，解决时序问题。


---

Link with Equalization




                         Deserializer
   Serializer




                                        4

![自适应均衡算法](/img/serdes/fundamentals/lectures/lecture1_ee720_intro_深度学习报告/_images/img-003.jpg)
> 🔍 深度说明：
> 【研究背景】自适应均衡算法是均衡器自动调整系数的核心，不需要人工配置，自动适配不同的信道特性。
> 【核心结论】最常用的自适应算法是最小均方（LMS）算法，基于最小化误差信号的均方值来调整系数，算法简单，容易实现，收敛速度适中；另外还有MMSE、RLS等算法，收敛速度快，但复杂度高，功耗大。
> 【工程价值】自适应均衡可以让Serdes自动适配不同长度、不同特性的信道，不需要人工配置系数，大大降低了系统调试的复杂度，同时可以跟踪信道随温度、电压的变化，动态调整系数，保证链路始终工作在最优状态。
> 【落地注意】LMS算法的步长需要合适选择，步长太大收敛速度快，但收敛后系数抖动大，性能不稳定；步长太小收敛速度慢，需要权衡选择；实际应用中一般采用可变步长，初始大步长快速收敛，收敛后小步长稳定跟踪。


---

TX FIR Equalization
• TX FIR filter pre-distorts transmitted pulse in order to invert channel
  distortion at the cost of attenuated transmit signal (de-emphasis)




                                                                            5

![DFE性能对比](/img/serdes/fundamentals/lectures/lecture11_ee720_clocking_arch_plls_深度学习报告/_images/img-004.jpg)
> 🔍 深度说明：
> 【研究背景】不同均衡方案的性能对比示意图，展示了DFE相比线性均衡的性能优势。
> 【核心结论】在相同信道损耗下，DFE可以获得比线性均衡更高的眼高和更低的误码率；信道损耗越大，DFE的性能优势越明显，损耗30dB时，DFE比线性均衡的误码率低几个数量级。
> 【工程价值】DFE可以大幅提升高损耗链路的性能，延长传输距离，或者在相同传输距离下降低对信道的要求，降低PCB和连接器的成本。
> 【落地注意】DFE存在错误传播的问题，如果某个符号判决错误，会影响后续多个符号的判决，导致误码扩散，因此DFE的tap数不宜太多，一般控制在5~10 tap以内，同时可以加入错误检测和纠正机制，降低错误传播的影响。

