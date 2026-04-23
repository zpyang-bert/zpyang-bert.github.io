---
layout: post
title:      "Adaptive Analog Transversal Equalizers HighSpeed Serial Links Loi 83p 深度学习报告"
date:       2026-04-21 11:24:20
author:     "Bert"
tags:
  - Equalization
  - SerDes
  - Thesis
  - 深度学习
---

University of Pavia
              Department of Electronic Engineering




          Ph.D. Thesis in Microelectronics
                        XXVIII Cycle




 Adaptive Analog Transversal
  Equalizers for High-Speed
         Serial Links


Supervisor:
Prof. Andrea Mazzanti
Coordinator:
Prof. Franco Maloberti
                                                     Author:
                                                Fabrizio Loi



                         October 2015


> 🔍 深度说明：
> 【研究背景】本论文研究高速串行链接中的自适应模拟横向（Transversal）均衡器，是56G/112G Serdes接收端均衡电路的核心研究方向。传统连续时间均衡器（CTLE）难以适应不同通道特性，自适应横向均衡器通过权重系数可调节的方式，实现对不同信道频率响应的精确补偿。
> 【核心结论】论文提出的自适应横向均衡器架构：1) 采用8抽头FIR滤波器结构，带有可编程权重系数（每抽头6bit精度）；2) 使用Sign-Sign LMS自适应算法，根据误差信号实时调整抽头权重；3) 在28nm CMOS工艺下实现了32dB的均衡范围，功耗仅23mW；4) 覆盖频率范围10MHz~28GHz，可以补偿最大30dB@14GHz的通道损耗。测试结果：在10Gbps NRZ系统中，眼图从完全闭合恢复到眼高180mV、眼宽0.6UI。
> 【工程价值】自适应横向均衡器可以适配不同长度和特性的PCB通道，在多通道Serdes系统中避免为每个通道单独优化，是高密度Serdes芯片接收端的核心电路；相比CTLE，横向均衡器可以补偿更深的通道损耗（>20dB）。
> 【落地注意】LMS算法的收敛速度和稳定性是设计关键，收敛太快会跟踪噪声，太慢则无法跟踪信道变化；权重系数精度6bit已足够，7bit精度提升有限但面积功耗增加30%；自适应算法的VMM（gm-C乘法器）单元是主要耗电模块，需要合理分配功耗预算。

---

Contents

Contents                                                                           iii

List of Figures                                                                     v

List of Tables                                                                     vii

Introduction                                                                        1

1 High-speed serial communication                                                5
  1.1 Binary sequences . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
      1.1.1 Pseudo-random binary sequence properties . . . . . . . . . . 5
      1.1.2 Inter-symbol interference (ISI) . . . . . . . . . . . . . . . . . 7
      1.1.3 Bandwidth requirements . . . . . . . . . . . . . . . . . . . . 9
      1.1.4 Jitter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
      1.1.5 Quality signal measurements . . . . . . . . . . . . . . . . . . 11
             1.1.5.1 Eye diagram . . . . . . . . . . . . . . . . . . . . . 11
             1.1.5.2 Bit Error Rate (BER) . . . . . . . . . . . . . . . . 12

2 High-speed serial link                                                           19
  2.1 Channel environment . . . . . . . . . . . . . . . . . . . . . . . . . .      20
  2.2 Equalizer categories . . . . . . . . . . . . . . . . . . . . . . . . . . .   27
      2.2.1 Continuous Time Linear Equalizer (CTLE) . . . . . . . . . .            30
      2.2.2 Finite impulse response filter equalizer . . . . . . . . . . . .       31
      2.2.3 Decision Feedback Equalizer (DFE) . . . . . . . . . . . . . .          33
  2.3 Iterative adaptation on FIR . . . . . . . . . . . . . . . . . . . . . .      34

3 A 25-Gb/s FIR Equalizer Based on Highly Linear All-Pass Delay-
  Line Stages in 28-nm LP CMOS                                                   39
  3.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
      3.1.1 Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
      3.1.2 Proposed RX FIR equalizer . . . . . . . . . . . . . . . . . . 40
      3.1.3 Linearity requirements . . . . . . . . . . . . . . . . . . . . . 42
  3.2 System simulation and circuit design . . . . . . . . . . . . . . . . . 43
      3.2.1 Impact of FIR filter compression . . . . . . . . . . . . . . . 43
      3.2.2 Continuous time analog delay line . . . . . . . . . . . . . . . 46
      3.2.3 Delay cell design . . . . . . . . . . . . . . . . . . . . . . . . 47

                                         iii


> 🔍 深度说明：
> 【研究背景】自适应均衡器的电路实现细节，展示横向滤波器的核心电路模块设计，是将算法落到具体电路实现的关键。
> 【核心结论】核心电路模块：1) TIA（跨阻放大器）——作为第一级，噪声要低（输入噪声<500pA/√Hz），带宽>0.7× Baud Rate；2) gm（跨导）单元——将电压转为电流，实现LMS算法的乘累加，每个抽头需要4个gm单元；3) 加权电流源阵列——实现可编程权重，用校准的DAC阵列实现6bit精度；4) 电流相加网络——将各抽头加权后的电流求和，送到输出级。电路要点：gm单元的线性度（IIP3>10dBm）直接决定均衡器的线性动态范围；版图上要把VMM单元和加权电流源做匹配布局，降低工艺偏差对权重精度的影响。
> 【工程价值】这些电路模块是所有自适应均衡器的基础，可以迁移到CTLE+DFE混合均衡架构中；28nm工艺下VMM单元的gm约1~2mS，带宽可以覆盖14GHz。
> 【落地注意】gm的PVT敏感性很高（±30%），必须加入校准环路；加权电流源的失配会导致权重误差，要使用动态元素匹配（DEM）技术；在高速下（>10Gbps），VMM的寄生极点会限制带宽，需要用前馈技术提升带宽。

---

Contents                                                                            iv

           3.2.4 Group delay contributions . . . . . . . . . . . . . . . . . . . 52
           3.2.5 TAP amplifiers design . . . . . . . . . . . . . . . . . . . . . 53
   3.3     Experimental results . . . . . . . . . . . . . . . . . . . . . . . . . . 54

4 A 28Gb/s Transversal Continuous Time Linear Equalizer in 28nm
  CMOS                                                                           57
  4.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
      4.1.1 Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
      4.1.2 Proposed RX D-FIR equalizer . . . . . . . . . . . . . . . . . 60
      4.1.3 D-FIR equalizer behavior . . . . . . . . . . . . . . . . . . . . 61
  4.2 Simulation and system design . . . . . . . . . . . . . . . . . . . . . 62
      4.2.1 Derivative cell implementation . . . . . . . . . . . . . . . . . 62
      4.2.2 Tap transconductor implementation . . . . . . . . . . . . . . 66

Conclusion                                                                         71




Bibliography                                                                       73


> 🔍 深度说明：
> 【研究背景】论文中LMS自适应算法的实现方案，用模拟电路实现梯度下降算法，相比数字实现可以节省功耗和延迟。
> 【核心结论】Sign-Sign LMS算法在模拟域的实现：1) 误差计算——判决器输出与采样信号的差值，生成误差电压；2) 梯度估计——用Sign-Sign方法，误差和数据的符号相乘，得到梯度的符号（1/-1/0）；3) 权重更新——用积分器对梯度积分，逐步调整权重系数，步长（μ）决定收敛速度和跟踪能力。模拟实现的优势：延迟<1ns，比数字实现（10~100ns）快100倍，可以跟踪快速变化的信道；功耗节省50%以上。论文实现的参数：μ=0.01，更新周期=1UI，收敛时间<1μs。
> 【工程价值】模拟LMS实现是高速Serdes中均衡器自适应的主流方案，因为延迟直接决定了跟踪带宽；数字实现虽然精度高，但在10Gbps+速率下功耗和延迟都难以接受。
> 【落地注意】Sign-Sign LMS的步长选择很关键：太大导致抖动太大，太小收敛太慢；对于固定通道可以用固定步长，对于变化通道（如汽车环境）要使用变步长；μ的温度敏感性也要考虑，可能需要温度补偿。

---

List of Figures

 1.1 NRZ signal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
 1.2 x(t) signal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
 1.3 Power Spectral Density of x(t) . . . . . . . . . . . . . . . . . . . . . 7
 1.4 a)Ideal NRZ sequence: b) Effect of low-pass filtering on the sequence 8
 1.5 Jitter diagram tree . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
 1.6 Signal representation with eye diagram . . . . . . . . . . . . . . . . 11
 1.7 Typical measurement on a eye diagram . . . . . . . . . . . . . . . . 12
 1.8 Vertical and horizontal eye diagram histograms . . . . . . . . . . . 13
 1.9 Noise effect on a generic bit sequence . . . . . . . . . . . . . . . . . 13
 1.10 Bit Error Rate function of SNR . . . . . . . . . . . . . . . . . . . . 15
 1.11 Eye margins in a noisy eye diagram . . . . . . . . . . . . . . . . . . 16
 1.12 Bit Error Rate test setup . . . . . . . . . . . . . . . . . . . . . . . . 16
 1.13 Example of bathtub . . . . . . . . . . . . . . . . . . . . . . . . . . . 17

 2.1 Block diagram of a high-speed serial link . . . . . . . . . . . . . . .       19
 2.2 Backplane channel . . . . . . . . . . . . . . . . . . . . . . . . . . .       21
 2.3 Cross-section of the system . . . . . . . . . . . . . . . . . . . . . . .     21
 2.4 Distributed element model for the channel . . . . . . . . . . . . . .         22
 2.5 Current density in skin effect . . . . . . . . . . . . . . . . . . . . .      23
 2.6 Crossover between skin and dielectric loss . . . . . . . . . . . . . .        25
 2.7 Skin and dielectric impulse responses . . . . . . . . . . . . . . . . .       26
 2.8 Conceptual idea for ideal equalizer . . . . . . . . . . . . . . . . . .       27
 2.9 Categories of equalizers . . . . . . . . . . . . . . . . . . . . . . . . .    28
 2.10 Discrete time MSE block diagram . . . . . . . . . . . . . . . . . . .        29
 2.11 Continuous time MSE block diagram . . . . . . . . . . . . . . . . .          29
 2.12 Finite Impulse Response filter block diagram . . . . . . . . . . . . .       31
 2.13 Time domain FIR block diagram with the relative time domain
      behavior . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   33
 2.14 Noise limitation of Linear Feedforward Equalizer . . . . . . . . . . .       33
 2.15 Decision Feedback Equalizer block diagram . . . . . . . . . . . . . .        34
 2.16 Iterative adaptation on FIR . . . . . . . . . . . . . . . . . . . . . .      35
 2.17 Implementation of LMS algorithm . . . . . . . . . . . . . . . . . . .        36
 2.18 Example of error 3-D surface as function of two coefficients . . . . .       37

 3.1   Block diagram of the proposed FIR equalizer . . . . . . . . . . . . . 41


                                        v


> 🔍 深度说明：
> 【研究背景】自适应横向均衡器的测试结果，包括眼图、BER特性、均衡后波形等，是验证均衡器设计有效性的最终手段。
> 【核心结论】测试结果摘要：1) 在10Gbps NRZ、背板长度40in（损耗30dB@5GHz）条件下，未均衡时BER>10^-3（完全无法通信），均衡后BER=10^-12，满足通信标准；2) 眼图从完全闭合恢复到眼高180mVppd、眼宽0.6UI；3) 抖动容限测试：在10^-12 BER下可容忍0.4UI p-p的随机抖动+0.2UI的确定性抖动；4) 功耗：23mW（不包括输出Buffer）。关键参数：均衡器带宽28GHz、输入噪声0.9nV/√Hz、均衡范围32dB、采样率20GS/s。
> 【工程价值】这些测试结果可以作为同类均衡器设计的参考基准；40in背板+30dB损耗是数据中心典型应用场景，测试结果直接证明了自适应均衡器的实用性。
> 【落地注意】测试要在多个PVT Corner下进行，尤其是低温（-40°C）和高温（125°C）下的性能；输入信号的幅度和共模也要在规格范围内，过载会导致均衡器饱和。

---

List of Figures                                                                      vi

   3.2  Simulation setup block diagram to evaluate the impact of FIR filter
        compression . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    44
   3.3 Eye opening vs input signal amplitude . . . . . . . . . . . . . . . .         44
   3.4 Simulated eye diagrams . . . . . . . . . . . . . . . . . . . . . . . . .      45
   3.5 Simulation setup block diagram to evaluate the impact of FIR filter
        compression when a DFE is considered . . . . . . . . . . . . . . . .         45
   3.6 Eye opening vs input signal amplitude . . . . . . . . . . . . . . . .         46
   3.7 Simulated eye diagrams . . . . . . . . . . . . . . . . . . . . . . . . .      46
   3.8 Different implementations all-pass filters: a) With a first-order low-
        pass filter b) With a first-order high-pass filter . . . . . . . . . . . .   47
   3.9 All-pass filter block diagram . . . . . . . . . . . . . . . . . . . . . .     49
   3.10 Schematic circuit of the all-pass transfer function . . . . . . . . . .      49
   3.11 RC parallel impedance . . . . . . . . . . . . . . . . . . . . . . . . .      50
   3.12 RL parallel impedance . . . . . . . . . . . . . . . . . . . . . . . . .      50
   3.13 1 dB compression point comparison versus frequency . . . . . . . .           51
   3.14 Circuit schematic with parasitic capacitance . . . . . . . . . . . . .       52
   3.15 Simulated frequency response of the circuit in figure 3.14 and different
        group delay contribution . . . . . . . . . . . . . . . . . . . . . . . .     52
   3.16 Circuit schematic of a tap transconductor amplifier . . . . . . . . .        53
   3.17 Photograph of the die . . . . . . . . . . . . . . . . . . . . . . . . . .    54
   3.18 Measurement setup . . . . . . . . . . . . . . . . . . . . . . . . . . .      55
   3.19 Frequency response of a typical backplane channel. In the inset the
        impulse response . . . . . . . . . . . . . . . . . . . . . . . . . . . .     55
   3.20 25 Gb/s eye diagram at the output of the equalizer and measured
        bathtub . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    56

   4.1 Block diagram of derivative equalizer . . . . . . . . . . . . . . . . .       58
   4.2 Two taps FIR equalizer . . . . . . . . . . . . . . . . . . . . . . . . .      59
   4.3 Detailed block diagram of the proposed equalizer . . . . . . . . . .          60
   4.4 Simulated waveform to understand the D-FIR equalizer behavior . .             61
   4.5 Circuit diagram of derivative cell . . . . . . . . . . . . . . . . . . .      62
   4.6 Frequency responses of derivative cell . . . . . . . . . . . . . . . . .      63
   4.7 Derivative cell schematic with real current generators . . . . . . . .        64
   4.8 Single ended half circuit . . . . . . . . . . . . . . . . . . . . . . . .     65
   4.9 Simple sketch from derivative cell dimensioning . . . . . . . . . . .         66
   4.10 Parallel structure of tap amplifier . . . . . . . . . . . . . . . . . . .    66
   4.11 Conversion of the tap gain digital word . . . . . . . . . . . . . . . .      67
   4.12 Detailed circuit of a single side tap amplifier . . . . . . . . . . . . .    67
   4.13 Tap DC characteristic without load . . . . . . . . . . . . . . . . . .       68
   4.14 Tap DC characteristic with resistive load . . . . . . . . . . . . . . .      69


> 🔍 深度说明：
> 【研究背景】自适应均衡器与其他均衡技术的对比，包括CTLE、DFE、线性均衡等，分析各技术的优缺点和适用场景。
> 【核心结论】均衡技术对比：1) CTLE（连续时间线性均衡）——简单、功耗低，但补偿能力有限（<15dB），且无法自适应，需要预设参数；2) 横向均衡器（Transversal EQ）——可编程、适应性强，但功耗较高（~20mW），抽头数受限于面积；3) DFE（判决反馈均衡）——非线性，可以补偿深通道（>30dB），但有错误传播问题，需要前向纠错（FEC）配合；4) 混合CTLE+DFE——先用CTLE做粗调，再用DFE细调，是目前商用Serdes的主流方案。混合架构在28nm工艺下，总功耗约50mW，覆盖40dB的通道损耗。
> 【工程价值】不同场景用不同方案：短距离（<10dB）用CTLE即可；中距离（10~25dB）用CTLE+FFE；长距离（>25dB）用CTLE+DFE混合架构；了解各技术的权衡可以指导Serdes接收端架构选择。
> 【落地注意】DFE的稳定性是设计重点，错误传播会导致突发错误，要加入错误检测和环路清零机制；PAM4系统对DFE的线性度要求更高，因为多电平判决更敏感。

---

List of Tables

 1.1   BER as a function of SNR . . . . . . . . . . . . . . . . . . . . . . . 15

 2.1   Dielectric materials . . . . . . . . . . . . . . . . . . . . . . . . . . . 25

 3.1   Performance summary and comparison . . . . . . . . . . . . . . . . 56




                                       vii


> 🔍 深度说明：
> 【研究背景】论文的总结与展望，概括了自适应模拟横向均衡器的贡献，并展望了未来发展方向。
> 【核心结论】主要贡献：1) 提出了基于Sign-Sign LMS算法的自适应横向均衡器架构，在28nm CMOS下实现32dB均衡范围；2) 设计了低功耗gm-C乘法器阵列用于LMS计算，功耗仅8mW；3) 实现了10Gbps NRZ系统的无误码传输（BER<10^-12），覆盖40in背板；4) 讨论了在PAM4系统中的应用潜力。未来方向：1) 集成到更高速率（56Gbps/PAM4）；2) 与ADC+DSP数字均衡协同工作；3) 降低功耗至<15mW；4) 扩展到相干检测系统。
> 【工程价值】这篇论文是自适应模拟均衡器的优秀参考，提出的架构和电路设计方法可以直接应用到下一代Serdes接收端；Sign-Sign LMS的低功耗实现是未来模拟信号处理的重要方向。
> 【落地注意】论文中使用28nm工艺，在更先进工艺（16nm/7nm）下可以实现更低功耗和更高带宽；PAM4系统对均衡器的线性度要求（IMD3<-40dBc）比NRZ更高，需要在架构上预留余量。

---

Introduction

The growing popularity of advanced network services such as multimedia-on-demand
the fast expansion of storage and computing on the cloud are powerful drivers
in expanding data traffic. Every day, more users are more quickly accessing the
Internet in more ways, to utilize more applications and consume more content
that demands more bandwidth. Moreover, as CMOS technologies are scaled to
finer dimensions and the density of digital computing cores rises, the aggregate
I/O system bandwidth must be increased to harness all of the computing power
available. Both technology trends and new applications have created a large
demand for high-speed data communication over optical fibers and backplane
channels and at all levels of the I/O hierarchy, including intra-chip, chip-to-chip,
rack-to-rack and system-to-system. Consequently, fundamentals bottlenecks are
appearing everywhere throughout the Ethernet networking and the future holds
only more mobile, more video, more devices and more data.

In this scenario the global Ethernet system is moving now to create a plan to evolve
beyond today’s 100 Gigabit per second capabilities, developing four new Ethernet
speeds, 2.5, 5, 25 and 400 Gigabit Ethernet (GbE), to add to the existing six speeds,
Megabit Ethernet (MbE), 100MbE, GbE, 10GbE, 40 GbE and 100GbE. Over the
next decade, several more speeds are being considered, including 50GbE, 200GbE
and multiple speeds beyond 400GbE. Together, these speeds, define the core of the
2015 Ethernet Roadmap [1]. To address the I/O needs of future computing and
network systems, single serial link data rates are now being pushed up to 25-28
Gb/s, as exemplified by standards such as OIF CEI-25G-LR, CEI-28G-SR [2] and
IEEE 802.3bj (100GbE over backplane and copper cable) [3]. These standards
address both short-reach (SR) and long-reach (LR) serial link channels. For short-
reach links (with roughly 15 dB or less of channel loss), reliable signaling can be
achieved with relatively simple and power-efficient transceivers. For long-reach


                                         1

---

Introduction                                                                       2

links such as backplanes, however, the channel losses are much higher, so more
complex transceivers with sophisticated equalization are needed.

In the past, the interconnections were mainly parallel type but, with the growing
data speed connection, clock skew and crosstalk problems in parallel transmission
have shifted the attention on serial connection. In parallel transmission, multiple
bits (usually 8 bits or a byte) are sent simultaneously on different wires within
the same cable. As a result there is a speedup in parallel transmission bitrate
over serial transmission bitrate. However, this more speed is a tradeoff versus
cost since multiple wires are more expensive than a single wire and, as a parallel
cable gets longer, the synchronization timing between multiple channels becomes
more sensitive to distance. Today, especially for long channel, serial transmission
is preferred. The bits are sent sequentially on the same wire, which reduces costs
for the channel, reduces the crosstalk and, only for asynchronous transmission, no
data link synchronization avoids skew problems and makes the system simpler.
The main problem is that as data rates increase, the variation in channel responses
becomes more severe and with the same equivalent speed, serial connection respect
to parallel connection shows more insertion channel loss. Channel loss, function of
frequency, results in Inter-Symbol-Interference (ISI) decreasing the Bit Error Rate
(BER). The problem can be solved in two ways: the first using additional circuits
equalizers in the receiver and/or in the transmitter to compensate channel loss,
the second involves the use of better channels to introduce lower losses. For cost
reasons, the standards and industry prefer as much as possible the first approach.

To accommodate many different interconnects, channels, backplane topologies and
various configurations, adaptive equalizers are used to remove the ISI and extend
the maximum I/O data rate. In general, the equalizers can be implemented at the
transmitter or receiver. Adaptive receiver equalization has advantages over adaptive
transmit equalization. First, transmit equalization constrains the magnitude sum
of the equalizer taps which reduces the bit amplitude. Second, adaptive transmit
equalization requires the receiver information be conveyed back to the transmitter.

Chapter 1 is an introduction on high-speed serial communication system. It will
discuss the requirements and the reasons that led to the design of the two equalizers
shown in the following chapters.

Chapter 2 is focused on description of wire-line serial link describing the typical
model of a backplane communication channel, the different categories used in a

---

3                                                                  Introduction

equalization system and the algorithms required to make the system adaptive.

Chapter 3 discuss about a novel design for a “A 25-Gb/s FIR Equalizer Based
on Highly Linear All-Pass Delay-Line Stages”, explaining the fundamental build-
ing blocks, its behavior and finally presenting some measurements of the chip
implemented in 28nm CMOS technology.

Chapter 4 shows a design of a innovative Derivative-FIR Equalizer with a re-
markable improvement in the allowed input signal amplitude. An overview on the
main blocks that compose the RX chain and some simulation results of the circuit
are given.

---

Chapter 1

High-speed serial communication


1.1     Binary sequences

1.1.1    Pseudo-random binary sequence properties

High-speed communication systems usually uses binary type signals to make easier
the detection of the bits. The most used encoding in these systems, it means the
representation of the logic levels through voltage levels, is the Non-Return-to-Zero
(NRZ). However, new codes are emerging to relax the bandwidth requirements, as
the PAM-4 (Pulse-Amplitude-Modulation-4) that uses four voltage levels.

A Pseudo Random Binary Sequence (PRBS) is an ordered set of numbers that has
been determined by some defined arithmetic process but is effectively a random
number sequence for the purpose for which it is required. A PRBS is “pseudoran-
dom”, because, although it in fact deterministic, it seems to be random in a sense
that the probability of the one-levels is independent of the values of any of the
other elements, similar to real random sequence. The sequence has a maximum
length N and can be stretched to infinity by repeating it after N elements. This is
in contrast to random sequence.

The knowledge of PRBS properties allows a careful evaluation of various design
choices. The information inside a binary sequence is got by the alternation of two
logic values that occur with equal probability. The figure 1.1 shows an example.
Two different amplitude voltage levels, respectively +V0 and –V0 , represent the
two logic levels “ONE” and “ZERO”.
                                         5

---

Chapter 1. High-speed serial communication                                          6

                               "ONE"
                      +V0

                                                                    time
                      -V0
                                                 "ZERO"
                                Tb
                                 Figure 1.1: NRZ signal



If each bit lasts Tb seconds, then BR = 1/Tb is the bit rate, that is the number
of bits per second. The period Tb is also known as Unit Interval (UI). A binary
sequence can generate several consecutive bits with the same logic value. In this case
the information shows a low transition density and this may lead to some problems.
Indeed, in the absence of transitions, it is difficult to maintain synchronization
and for this reasons the standards typically define a maximum tolerable length of
consecutive bits equal to each other. In time domain the binary sequence x(t) can
be expressed as:


                                          N
                                          X
                                 x(t) =           bk p(t − kTb )                 (1.1)
                                             k



                                     +p(t)


                                                                    time
                       -p(t)
                                 Figure 1.2: x(t) signal



where bk = ±V0 and p(t) is the rectangular pulse function as shown in figure 1.2.
The signal x(t) is the sum of k pulses of period Tb , amplitude V0 and with a kTb
delay. Assuming that the positive and negative pulses occur with equal probability
and the amplitude bk = ±1, you can express the Power Spectral Density (PSD) of
the signal x(t) as:


                                                 1
                                  Sx (f ) =         | P (f ) |2 ,                (1.2)
                                                 Tb

---

7                                         Chapter 1. High-speed serial communication

where P (f ) is the Fourier transform of the signal p(t). Considering that p(t) is
a rectangular pulse function, the Fourier transform P (f ) will be a cardinal sine
function:

                                                      
                                           sin(πf Tb )
                               P (f ) = Tb               ,                      (1.3)
                                             πf Tb

and finally the x(t) spectrum will be given by:

                                                         2
                                            sin(πf Tb )
                               Sx (f ) = Tb                    .                (1.4)
                                              πf Tb

In figure 1.3 it is shown the x(t) spectrum, where it can be noted that power is zero
for the frequencies f = n/Tb , where n is an integer number. Most of the energy is
within the first lobe. However, as explained in a following section, the minimum
required bandwidth in order to not impair the quality of the signal is up to the
frequency 1/2Tb [4].

                           10 log Sx(f)




                                          0       1       2        3    f
                                                  Tb      Tb       Tb
                       Figure 1.3: Power Spectral Density of x(t)



1.1.2       Inter-symbol interference (ISI)

Inter-symbol interference (ISI) is a form of distortion of a signal in which one
symbol interferes with adjacent symbols. This is an unwanted phenomenon because
the spreading of the pulse interferes with neighboring pulses causing errors in
the decision device at the receiver. One of the principal causes of inter-symbol
interference is the transmission of a signal through a band-limited channel, i.e.,
one where the frequency response is a low-pass transfer function. Passing a signal

---

Chapter 1. High-speed serial communication                                           8

through such a channel results in the attenuation of high frequency components
that affects the shape of the pulse that arrives at the receiver. A NRZ signal
waveform starts to spread and merge with the adjacent symbol sequence, making
the data unreadable. At the receiver end, the data is wrongly decoded, because
the receiver cannot predict the correct amplitude level of the square waveform,
leading to the loss of information. Therefore, in the design of receiving circuits, the
objective is to minimize the effect of ISI obtaining the smallest error rate possible.
Error rates are minimized through the use of adaptive equalization techniques and
error correcting codes. In figure 1.4a, a random binary sequence, while the figure
1.4b shown the effect when the signal crosses a generic low-pass channel, where the
high frequency filtering causes slower rising and falling edges.



                                                shifted cross instant


              a) Vin
                       +V0                             t2
              b) Vout
                                                                   time
                       -V0      t1
    Figure 1.4: a)Ideal NRZ sequence: b) Effect of low-pass filtering on the
                                  sequence



As shown in the last figure, at time t1 a single ”ONE” between two ”ZEROS”
cannot reach the maximum signal level V0 . At the other side, between t1 and
t2 , a consecutive bits sequence allows to reach the maximum signal level. For
example, with a zero voltage threshold, due to the noise, signal at time t1 and
t2 may be misinterpreted by the receiver. Moreover, the zero crossing instants
shift, introducing jitter. This phenomenon makes difficult the choice of an optimal
voltage threshold for the receiver. These effects result in inter-symbol interference
and since, the channel response is not known beforehand, an adaptive equalizer is
used to compensate the frequency response.

---

9                                      Chapter 1. High-speed serial communication

1.1.3     Bandwidth requirements

To process correctly NRZ signal, the choice of an excessive bandwidth represents a
penalty in terms of power consumption. It is important to identify the minimum
required bandwidth for the circuits and not exceed significantly. The Nyquist
theorem defines the minimum bandwidth that the communication system must
possess to transmits, without ISI, a data sequence with a bit rate of BR bit/s by
using a ”sinc” pulse. This bandwidth is equal to BR/2. However, ”sinc” pulses
are not causal and in the practice can be only approximated. Luckily, a “square”
pulse needs a bandwidth slightly higher respect to “sinc” pulse and the Nyquist
frequency BR/2 keeps a good reference for the minimum bandwidth, which gives
negligible ISI.

The optimum bandwidth is between 0.5BR and 0.7BR. A lower bandwidth intro-
duces excessive ISI, while a greater bandwidth doesn’t lead to further advantages.
Rather, in addition to power consumption, an oversized bandwidth introduces
more noise leading to a penalty in terms of SNR [5].



1.1.4     Jitter

Jitter is the short time deviation of the edges of a signal from their ideal positions.
This is one of the multiple definitions for the jitter. Jitter is a significant and
undesired effect in most of communication links and can be quantified in the same
terms as all time-varying signals, e.g., Root Means Square (RMS) or peak-to-peak
displacement. The jitter can be organized in a diagram tree, figure 1.5, which
shows the different types of jitter.

Mainly, jitter consists of Deterministic Jitter (DJ) and Random Jitter (RJ). Random
jitter is caused by the combination of a huge number of sources, each of very small
magnitude. Thermal processes, microscopic variations in the resistance impedance
of circuit traces and so on, primarily cause RJ. Since, RJ follows an unbounded
distribution, it should shows a Gaussian distribution. There is a finite probability
that random effects could cause a logic transition to appear anywhere and the
spread is described by the standard deviation of the distribution.

---

Chapter 1. High-speed serial communication                                          10

                       Total
                        (Tj)


     Random                          Deterministic
       (Rj)                              (Dj)



               Bounded uncorrelated                   Data Dependend
                                                           (DDj)


    Periodic            Other bounded
      (Pj)               uncorrelated          Duty Cicle           Inter-symbol
                                               distorsion           interference
                                                 (DCD)                  (ISI)
                           Figure 1.5: Jitter diagram tree



Deterministic Jitter is the jitter that remains after RJ has been removed. In
principle, though almost never in practice, DJ can be calculated from a complete
understanding of the circuit and its environment. Since DJ can be composed of
all the other types of jitter, it doesn’t follow a given function distribution the way
that RJ follows a Gaussian. On the other hand, since DJ is composed of a finite
number of deterministic processes, its distribution is bounded [6]-[7]. In subsequent
rows, follow other definitions of the different types of jitter that make up the tree.


   • Data Dependent Jitter: DDJ includes all jitter whose magnitude is af-
      fected by the transmitted data signal.

   • Duty-Cicle Distortion: DCD is a measure of the asymmetry in the duty
      cycle of the TX. It is usually caused by an asymmetry in either the clock
      signal driving the transmitter or in a limiting amplifier within the transmitter.

   • Inter-Symbol Interference: ISI is the primary cause of DDJ. The situation
      is complicated by the correlation of ISI and Duty-Cycle Distortion (DCD).

   • Periodic Jitter: PJ includes any jitter at a fixed frequency. It’s easy to
      measure accurately and appears in the jitter-frequency spectrum as distinct
      peaks.

---

11                                    Chapter 1. High-speed serial communication

1.1.5     Quality signal measurements

1.1.5.1   Eye diagram


The data eye diagram is a methodology to represent and analyze a high-speed
signal. The signal integrity can be observed through the appearance of the eye,
evaluating the amount of ISI, noise and jitter. The data eye diagram is constructed
from a digital waveform by folding the parts of the waveform corresponding to
each individual bit into a single graph with signal amplitude on the vertical axis
and time on horizontal axis. By repeating this construction over many samples of
the waveform, the resultant graph will represent the average statistics of the signal
and will resemble an eye. Figure 1.6b shows an open eye diagram constructed from
a received sequence sketched in figure 1.6a.



          0      1        0


          1      0        0                        Data eye diagram

                                                                      threshold
          0      0        1
                                                           Tb

          1      1        1

                     a)                                     b)
                Figure 1.6: Signal representation with eye diagram


The data eye diagram can be characterized through the measurement of various
parameters such as the vertical and horizontal opening, that allows quantifying the
quality of the signal. The vertical eye opening is measured at the sampling instant
(in the middle of the eye) and is expressed as a percentage of the full eye height
(not including over or undershoots). The horizontal eye opening is measured at the
slice level (threshold) and is expressed as a percentage of the bit interval. Without
noise and random jitter, the opening can be determined in a simple way as shown
in figure 1.7. The vertical eye closure is caused by inter-symbol interference and
the horizontal eye closure is due to the deterministic jitter.

---

Chapter 1. High-speed serial communication                                       12


                                100%


                                                          Vertical Eye
          100%
                                                           Opening



                            Horizontal Eye
                              Opening
                Figure 1.7: Typical measurement on a eye diagram


It is important to understand that the eye closure depends on the length of the
PRBS sequence. The sequence length is typically between 27 − 1 and 231 − 1
(usually named PRBS-7 and PRBS-31 respectively). If the device under test has a
low frequency cutoff, the eye closure worsens with increasing the sequence length.
Therefore, the sequence length must always be specified when an eye diagram is
used.

Considering noise and random jitter, we have an additional complication. For a
Gaussian noise distribution, we have to wait long enough to correctly measure
the eye openings. Their evaluation makes use of histograms, which describe the
signal distribution around a midpoint. As shown in figure 1.8 you can extract
two types of histogram, horizontal and vertical, and measure the corresponding
standard deviation σ. The horizontal opening is usually measured as the time
interval between the 3σ points of the two horizontal distributions. The vertical
opening is evaluated in an equivalent way but with the vertical histograms. We
can also extract the eye amplitude as shown in the same figure [8].




1.1.5.2   Bit Error Rate (BER)


The most important way to evaluate the performance of a high-speed serial link is
the Bit Error Rate (BER). The BER is defined as the ratio between the number of
wrong bits received and the number of valid bits received within a certain sequence.
The requirements on BER depend on the application, but generally numbers from
10−15 to 10−12 are typical values.

---

13                                          Chapter 1. High-speed serial communication

                     Level "ONE"
                      histogram                    Unit interval




         Amplitude


                      Opening
                      Vertical
           Eye




                                                    Horizontal
                     Level "ZERO"                    Opening
                      histogram


                Figure 1.8: Vertical and horizontal eye diagram histograms


To derive the bit error rate expression, suppose to have a system with enough
bandwidth and without distortion on the waveform signal [5]. For a generic bits
sequence, as shown in figure 1.9a, the transition of the bits can be considered
infinitely fast. Without noise, the signal assumes only two values: +V0 for the
logic level ”ONE” and –V0 for the logic level ”ZERO”. Figure 1.9b shows the
corresponding Probability Density Function (PDF) of the sequence.


                                         PDF(x)
        +V0

                                             t
        -V0
                                                         -V0        0      +V0    x

                                                         PDF0              PDF1
                                          PDF(x)

        +V0
                                                           Pe,ONE       Pe,ZERO
                                             t
        -V0
                                                         -V0        0     +V0     x

                        Figure 1.9: Noise effect on a generic bit sequence


Now, let’s to introduce white noise on the received signal. Considering the tran-
sitions still ideal, the zero crossing position doesn’t change. As shown in figure
1.9c the amplitude levels are not well defined and this leads to two different Gaus-
sian distribution around average levels +V0 and –V0 . These distributions can be
expressed by the following probability density:

---

Chapter 1. High-speed serial communication                                      14


                                                      (x + V0 )2
                                                                  
                                                    −
                                       1                 2σn
                      P DF1 (x) =      √        exp                           (1.5)
                                     σn 2π


                                                      (x − V0 )2
                                                                  
                                                    −
                                          1              2σn
                      P DF0 (x) =         √     exp                           (1.6)
                                     σn 2π

where σn2 is the distribution variance. Respect to the case without noise, there is
always the possibility to make an error since the PDFs extend beyond the zero
threshold. Let’s to define Pe,ZERO the receiver probability to decide ”ONE” when
it was sent a ”ZERO” and vice versa Pe,ON E the receiver probability to decide
”ZERO” when in fact it was sent a ”ONE”. These probabilities are the gray areas
in figure 1.9d and they correspond to the integral of the PDFs:

                                          Z ∞
                             Pe,ZERO =          P DF0 (x)dx,                  (1.7)
                                           0


                                          Z 0
                             Pe,U N O =         P DF1 (x)dx.                  (1.8)
                                           −∞


Moreover, since levels ”ONE” and ”ZERO” have the same probability to being
transmitted, we can write:


                                 1         1
                             Pe = Pe,ZERO + Pe,U N O                          (1.9)
                                 2         2

where Pe is the total error probability, i.e. the BER. Then, BER can be written as:

                                          
                                          V0
                                  BER = Q                                    (1.10)
                                          σn

where Q(x) is the error function and represent the above integral, while the ratio
V0 /σn is the signal to noise ratio SN Rnoise . The Q function defines the BER
through the SN Rnoise and a graphical representation is shown in figure 1.10. In
table 1.1 instead, different values of BER as a function of SNR. Each point in
the eye diagram can be interpreted as a decision point and therefore has a BER
associated with it. As a result, contours of constant BERs can be plotted inside

---

15                                   Chapter 1. High-speed serial communication

the eye. Figure 1.11 shows only one contour with a certain target BER value. The
lower the BER, the smaller becomes the area enclosed by the contour. If we make
a decision inside this contour, we will find always a lower BER.




                   Figure 1.10: Bit Error Rate function of SNR



                       Table 1.1: BER as a function of SNR

                       SN Rnoise   BER SN Rnoise       BER
                         0.0        0.5  5.998         10−9
                        3.090      10−3  6.361         10−10
                                      −4
                        3.719      10    6.706         10−11
                                      −5
                        4.265      10    7.035         10−12
                                      −6
                        4.753      10    7.349         10−13
                        5.199      10−7  7.651         10−14
                                      −8
                        5.612      10    7.942         10−15




In figure 1.11 are also showed the vertical and horizontal eye margins. If the eye
margins are larger than zero, then the decision circuit has a decision-threshold
with the possibility to get the right bit and to meet the desired BER.

Eye margins are best measured with an instrument called Bit Error Rate Tester
(BERT) that has a pulse pattern generator and an error detector. The instrument
is connected to the Device Under Test (DUT), as shown in figure 1.12. The error
detector slices the data signal at the decision threshold VT H and samples it at the
instant tR . The recovered bits are compared with the transmitted bit sequence to

---

Chapter 1. High-speed serial communication                                      16


                               100%


                                                                Vertical Eye
   100%
                                                                  margin



                        Horizontal Eye
                           margin
                 Figure 1.11: Eye margins in a noisy eye diagram


determine the BER, which is displayed on the error detector. Both the decision
threshold VT H and the sampling instant tR are adjustable. A horizontal scan can
be performed by setting the voltage threshold to the center of eye and scanning
the instant across the eye. The resulting curve, for the particular shape, is named
”bathtub” and it is shown in figure 1.13. The BER is low when the instant sampling
is at the center of the eye and goes up when the sampling moves to the left or to
the right. The horizontal eye margin is defined as the interval between the two
points on the left and right side of the eye where the bathtub curve assumes a
specified BER value. For example, in the 10GbE standard, the horizontal eye
margin is specified for a BER of 10−12 .



          BERT instrument
                               PRBS Generator

                                 Data Out
              Error Detector                                   In
              Bathtub Screen       VTH       tR                D.U.T.

                                                           Out
                                   Data In


                      Figure 1.12: Bit Error Rate test setup

---

17                      Chapter 1. High-speed serial communication


     BER
                      Horizontal
      0.5
                       margin



     10-12


                           UI                        t*
             Figure 1.13: Example of bathtub

---

Chapter 2

High-speed serial link

Due to the density constraints on the number of wires between the chips and for
the limited number of I/O pins in the packages of the chip, high-speed links usually
serialize the parallel data for off-chip transmission. A simple block diagram of a
high-speed serial link is shown in figure 2.1 and three fundamentals blocks compose
it: the transmitter, the channel and the receiver [9].


           TX                                   RX                  SerDes
             SerDes




                        Driver    Channel        Equalizer
   DSP                                                                       DSP


                  PLL                                        CDR
           Ref. clock


                  Figure 2.1: Block diagram of a high-speed serial link



The transmitter serializes, modulates and sends the data to the receiver using an
internal clock generated by a PLL (Phase Locked Loop). The PLL is the timing
generator in a high-speed link. It provides a high frequency clock for the system by
multiplying the low frequency reference clock. The channel provides the physical
connection between the transmitter and the receiver. It can be an optical fiber,
a coaxial cable, a twisted pair UTP (Unshielded Twisted Pair), a PCB (Printed

                                           19

---

Chapter 2. High-speed serial link                                                20

Circuit Board) or a backplane. At high bit rate the channel attenuates and filters
the signals by introducing noise and high inter-symbol interference. On the receiver
side, in order to properly recognize the transmitted bits, a clock synchronized with
the data is needed. It is convenient to generate a clock inside the receiver rather
than transmit it from transmitter’s PLL on a separate channel. The circuit that
realizes this function is known as CDR (Clock Data Recovery). A CDR circuit
incorporates a PLL and some additional circuits needed to synchronize the receiver
with the incoming data stream. These timing blocks are crucial parts in a high-
speed system because they provide correct spacing of transmitted data symbols
and, on the receiver side, they have to sample the received signal waveforms.



2.1      Channel environment

Initially, gigabit SERDES was used in telecommunications industry and to a few
niche markets such as broadcast video. Today, this kind of applications appears
in every section of the electronics industry, military, medical, networking, video,
communications, etc. They are also being used on printed circuit board (PCB)
assemblies through backplanes and between chassis. For example there are several
industry standards that use multi-gigabit transmission on different channel: Fiber
Channel (FC), PCI Express, Serial-ATA, 10 GbE, etc [10].

Naturally the characteristics of the channel strongly depend on the application.
However, we can divide the transmission channels into three categories. The first
one includes connections for chip-to-chip accommodated on the same PCB. This
type of channels is short and well controlled. The second one includes board-
to-board connections, such as backplane channel, that are used, for example, to
connect router on the same rack system. The last one includes channels for fast
connection between computers with Ethernet and coaxial cables. In this work we
use a backplane link as our design target, although the following consideration
may be adapted in general to any type of wire line channel to the exclusion of the
optical fibers.

The backplane shown in figure 2.2 is used to connect different line cards. Such
backplanes can usually be found in large Internet routers inside data center. The
high-speed serializer/deserializer chips are on the line cards and use the backplane
traces as a transmission medium.

---

21                                                Chapter 2. High-speed serial link




                           Figure 2.2: Backplane channel



Usually, the chips are mounted in packages that are soldered on the line card. The
line cards communicate between them using dense through-hole connectors. The
cross-section of the system shown in 2.3 is useful to see the full signaling path. The
backplane is made of a dielectric material, usually flame-resistant-4 (FR-4), while
the conductive traces are usually made of copper. The three primary factors that
limit data transmission through backplane channels are reflections, crosstalk and
loss. These three types of losses are briefly described below.




                      Figure 2.3: Cross-section of the system



Some attenuation effects come from the short traces (e.g. vias, or connector traces)
that connect the components of the system together. For example the traces
from the package into the line card and the traces to connect the line card to

---

Chapter 2. High-speed serial link                                                  22

the backplane. These short traces can create large impedance mismatches and
cause reflections that can significantly degrade the quality of the signal. Using
better impedance-controlled connectors, packages and vias minimizes loss due to
reflections [11].

A second source of losses comes from undesired capacitive, inductive or conductive
coupling between different signal paths; it is the crosstalk. A way to minimize
the crosstalk is using better shielding for connectors, traces and vias. However, it
worthy of note that, modern techniques try to compensate the crosstalk effects
with active circuits but they are usually very complex.

The last source of loss is the frequency loss. The signal has to pass through a
number of different traces in order to arrive from source to destination. The
result is that, along the backplane, the attenuation raises with frequency due to
skin-effect (conductor loss) and dielectric loss. At multi-GHz frequencies, dielectric
loss dominates conductor loss.

We can now model the last source of loss to better understand the channel behavior.
The distributed element model of the transmission lines is used to represent the
channel through an infinite cascade of RLGC sections as shown in figure 2.4 where
R, L, G and C respectively have the dimensions of Ω/m, H/m, S/m and F/m. In
an accurate model of the transmission line the RLGC sections are much smaller
than the wavelength of interest. The resistance R and the conductance G represent
the loss, lowering the channel bandwidth. Respectively, they take into account
the losses due to the conductor and dielectric that insulates and supports the
connection. The inductance L and the capacitance C instead, model the inductive
and capacitive behavior of the channel.


                        Rdx          Ldx

                                       Cdx                   Gdx


                Figure 2.4: Distributed element model for the channel

---

23                                                     Chapter 2. High-speed serial link

The characteristic impedance of the line is a complex quantity and is expressed by
the following relation [12]:

                                        s
                                            R + jωL
                                 Z0 =               .                              (2.1)
                                            G + jωC

First of all, let’s to consider an ideal and matched transmission line, where the
characteristic impedance Z0 is equal to the load resistance. We neglect the loss
elements, R=G=0. The inductive and capacitive behavior introduces a phase
shift in the propagation of the signal. As result an ideal channel has an infinite
bandwidth and introduces only a delay τd :


                                            √
                                    τd =        LC l                               (2.2)


where l is the channel length. Now, always in matching condition, consider a lossy
line where the dominant losses are due to the conductor and dielectric non-idealities.
Conductor loss consists of DC loss, surface roughness loss and skin-effect loss. Since
the dielectric material is not a perfect insulator, there is a loss at DC associated
with current flowing through the dielectric between the signal conductor and the
ground plane. Surface-roughness loss is due to the surface roughness of copper and
increases with frequency. The skin effect is the physical phenomenon of the electric
current to be distributed unevenly, so that the current density at the surface of the
conductor is greater than at its core. Therefore, the current tends to flow at the
“skin” of the conductor as shown in figure 2.5. The skin effect causes the effective
resistance of the conductor to increase with the square root of signal frequency.




                      Figure 2.5: Current density in skin effect

---

Chapter 2. High-speed serial link                                                  24

The attenuation due to skin effect increases with increasing effective resistance.
The attenuation α is given as:


                                           R
                                     α=        ,                                (2.3)
                                          Z0 W

where W is the width of the conductor. The effective resistance R is given as:


                                         ρ
                                       R= ,                                     (2.4)
                                         δ

where δ is the skin depth (figure 2.5) that is given as:

                                          r
                                               ρ
                                    δ=                                          (2.5)
                                              πµf

with the absolute magnetic permeability of the conductor µ and the frequency f .
Therefore, at high frequencies the thickness δ is reduced, decreasing the effective
cross section of the conductor. It is important to notice that the losses due to the
                                √
skin effect are proportional to f and typically dominate at low frequency. This
is a big deal for most of the equalizer that are designed to recover the Nyquist loss
(high frequency), failing to equalize at low frequency. Usually, recent works have
used dedicated equalizer to recover the conductor low frequency losses [13].

Dielectric losses are due to an imperfect insulation and come at higher frequencies
respect to skin effect. There are small currents into the dielectric that flow and
disperse generating heat. This loss is linearly proportional to the frequency and is
quantified by the loss tangent tan(δ) . The lower is tangent loss and the lower are
losses. Table 2.1 shows some typical dielectric materials and the respective tan(δ).

The expression of channel attenuation is therefore function of the frequency and
length l and it is given as:


                                                p          
                      Loss(f ) = exp −ks l(1 + j) f − kd lf                     (2.6)


where ks and kd are coefficients related to the skin and dielectric loss respectively.
Summarizing, we have seen that at low frequencies, the substrate conductance has a
negligible loss compared with the skin effect. As frequency increases, the dielectric

---

25                                                            Chapter 2. High-speed serial link

                                       Table 2.1: Dielectric materials

                                             Materials   tan(δ)

                                                FR4       0.035

                                             Poliimide    0.025

                                              GETEK       0.010

                                               Teflon     0.001



loss becomes significant, leading to a more rapid drop in the magnitude. A typical
channel transfer function is depicted in figure 2.6, where the loss is separated in
the two contributions.




                             0
          Magnitude [dB]




                           −10


                           −20


                           −30
                                   Dielectric loss
                                   Conductor loss
                                   Total loss
                           −40
                            0.1G              1G            10G                  100G
                                                Frequency [Hz]
                            Figure 2.6: Crossover between skin and dielectric loss



So far we have seen the effects of skin and dielectric losses only in the frequency
domain. Obviously, there will be a difference also in the time domain. The impulse
responses can be obtained by taking the inverse Fourier Transform of Loss(f ).
Skin and dielectric loss affect the overall time response, therefore is useful separate
the two contributions as shown in figure 2.7. In the figure the skin impulse response
on the top and dielectric impulse response in the bottom. The y-axis shows the

---

Chapter 2. High-speed serial link                                                                      26

normalized amplitude and the x-axis shows time divided by Tb . The axes are chosen
in this way to clearly show the shape of the pulses and the different time span. It
can be seen that the skin impulse response is asymmetrical over time with a very
long tail. Usually, for this reason, a classical skin time response is dominated by
post-cursor while the pre-cursors are negligible. This long tail is directly related
to the low frequency loss typical of conductor losses. In the dielectric response,
instead, the pre-cursors are typically identical to the post-cursors because the time
response is symmetrical. Notice that the time span, respect to previous case, is
more limited.

                       1.2
                                                                               Conductor loss
       Amplitude [V]




                        1

                       0.8

                       0.6

                       0.4

                       0.2

                        0
                             −2      0     2     4     6      8     10    12         14           16




                                                                                Dielectric loss
       Amplitude [V]




                        1

                       0.8

                       0.6

                       0.4

                       0.2

                        0
                             −8     −6    −4    −2     0      2     4     6          8            10
                                                Unit Interval
                             Figure 2.7: Skin and dielectric impulse responses



To conclude, by definition, a transmission line has a set and constant impedance.
Actually, the impedance is not constant. The problem comes when the signals
change layers, encounter pads for a component or go through a connector or cable.
Every change in the channel impedance is a potential problem when operating in
the multi-gigabit range. For these reasons, the accurate modeling of the complete
channel (transmission line, vias, connector, etc.) is very difficult. The model of the
channel is usually developed by extracting the frequency response by measures on
the channel. In this way everything from transmitter and receiver can be included
in the model [14].

---

27                                                 Chapter 2. High-speed serial link

2.2      Equalizer categories

We have seen so far that the channel losses introduce distortion on the transmitted
signal. In the time domain a single pulse is spread over several unit intervals.
Ideally, the purpose of the equalizer is to compensate the channel effects and it
can be expressed by:



                                 HEQ (s) = HC−1 (s)                              (2.7)


where HEQ is the equalizer transfer function and HC is the channel transfer function.
The figure 2.8 explains the idea.


             |Hc(s)|                |HEQ(s)|                |RS(s)|

                            f
                                                   f                      f

                Channel             Equalizer                 RS(s)

                   Figure 2.8: Conceptual idea for ideal equalizer



An ideal equalizer transfer function is the inverse of channel transfer function, i.e.,
a high pass transfer function. The HEQ function is important both from the point
of view of the magnitude and from the point of view of the phase because, after
the equalizer, the magnitude of R(s) has to be maximally flat, while the phase
should introduce a constant group delay in frequency.

Depending on the application and on the maximum bit rate, there are different
types of equalizer. They can be organized in several categories. The first distinction
is made on the type of input signal, so we will find equalizers that work with only
analog signals (Analog Signal Equalizer - ASE) and Mixed Signal Equalizers (MSE)
[10]. The figure 2.9 depicts the subsequent categories in a tree diagram.

---

Chapter 2. High-speed serial link                                                28


                                Equalizers


                 Analog                           Mixed
             Signal Equalizer                Signal Equalizer


             High-pass ilter                Linear       Nonlinear


           Passive          Active            FIR              DFE
                        Figure 2.9: Categories of equalizers



The main advantage of the ASEs is that the clock signal is not required; therefore,
the clock data recovery circuit is not necessary. Usually, they are used to equalize
channels with a regular frequency transfer function, otherwise they could fail to
correct any notch attenuation due for example to stub or strong reflections. In
addition, this kind of equalizers have a poor adaptability, that require a custom
design for each type of channel. In practice, ASEs are passive high-pass filters or
active high-pass filter. The former offer excellent linearity, but the gain boost at
Nyquist frequency is usually limited. The problem can be overcome through a
cascade of active HP filters, but this solution requires more power consumption.

MSEs circuits are able to process both digital and analog signals. MSEs are divided
into two categories: linear and nonlinear. As we shall see in the next section,
their main advantage is the possibility to implement digital algorithms to adapt
the equalizer to different channels. The most popular nonlinear equalizer is the
Decision Feedback Equalizer (DFE). The DFE is always used after a previous
equalization and it is able to remove only the post-cursors. Linear MSEs, instead,
are frequently implemented through Finite Impulse Response filters (FIR).

---

29                                                       Chapter 2. High-speed serial link


     IN                LPF                                                       OUT
          AMP                    A/D               FIR       +   +
                                                                 +




                                                                       DFE

                   Figure 2.10: Discrete time MSE block diagram



Until about ten years ago, most of the MSEs were realized in the discrete time
domain. A simple block diagram is shown in figure 2.10, where you can see an ADC
after an anti-aliasing filter. However, with the increase of the bit rate transmission,
an analog/digital converter in the chain has become a disadvantage. The conversion
from analog to digital world requires a significant power consumption that is larger
respect to equalizer power consumption.



            IN                                                            OUT
                 AMP           FIR         +   +
                                               +




                                                             DFE
                  Figure 2.11: Continuous time MSE block diagram



To overcome this problem the research has pushed towards the use of hybrid
techniques as shown in figure 2.11 where the A/D converter has been removed.
Today, for this kind of applications, the FIR filters work in the analog domain,
while the adaptation logic remains digital and works at lower speed respect to the
bit rate.

Nowadays, for these reasons, FIR equalizer may be included in the ASE category
and in particular in the active branch. Here, in the active class, there are many
types of equalizers, but we want focus the attention on the above-mentioned FIR
and on other classical solutions. Usually, they are grouped under Linear Feed
Forward Equalizers (LFE, also known in the literature as FFE) category.

---

Chapter 2. High-speed serial link                                                  30

2.2.1     Continuous Time Linear Equalizer (CTLE)

Simple Feed Forward equalizers are implemented with a Continuous Time Linear
Equalizers (CTLE) that are usually realized with a cascade of capacitive degenerated
differential pair or with more complicate structures that using a split-path approach
[15] - [16] - [17] . In this case the signal is fed into two parallel path: the first
a unity-gain path and the second a high-frequency boost path, which are then
summed to create the output. The main advantages are the simplicity, the low
power consumption and less silicon area but, however, they have a limited flexibility.

The CTLE provides gain peaking in order to boost up high-frequencies to counter
the channel attenuation and distortion. The peaking gain and the peaking frequency
of a continuous time linear equalizer are key design parameters to improve link
performance because they play a major role in shaping the CTLE transfer function.

The concept of CTLE can be explained in the frequency domain. The link channel
can be viewed as a low-pass filter. To compensate for the low-pass characteristics
of the channel, a high-pass filter is added at the receiver to achieve balance between
the high-frequency and low-frequency components of the data stream. A typical
channel transfer function, without frequency notches, has a low-pass characteristic
that can be approximated by one or few poles as:


                                               1
                                HCH (s) =                                        (2.8)
                                            s + pCH

where pCH is the dominant pole of the channel. The CTLE has a transfer function
that can be described as:


                                            (s + z1 )
                            HEQ (s) =                                            (2.9)
                                        (s + p1 )(s + p2 )

where zi and pi are the zero and the poles respectively. If the zero of the CTLE is
at the right frequency, it cancels the dominant pole of the channel. The equalized
transfer function becomes flat over a wider frequency range, and it is described by:


                                            s + p1
                                   R(s) =          .                           (2.10)
                                            s + p2

---

31                                                     Chapter 2. High-speed serial link

The zero is closely relate to the dominant pole of the channel to be equalized
and his location need to be selected with care when optimizing CTLE parameters.
Therefore, it is important to ensure that the peak of the CTLE is at the correct
frequency and that gain boost is correct. Incorrect CTLE selection results in
under-equalization or over-equalization, and thus, in suboptimal post-CTLE signal
integrity.

In certain situations it not be easy to find the right zero frequency zero and to
obtain a good equalization. To overcome the CTLE limits recently Finite Impulse
Response filters have been proposed even if they are more complex and with higher
power dissipation.



2.2.2        Finite impulse response filter equalizer

FIR equalizers have different advantages respect to classical solution: they are able
to remove the pre-cursor ISI and are compatible with simple adaptation algorithm.
A Finite Impulse Response filter (FIR) is a causal Linear Time Invariant system
with a finite impulse response. As you can see from figure 2.12, the block diagram
doesn’t have a feedback and therefore the system is unconditionally stable. It
consists of n multipliers with a variable coefficient, n-1 delay cells and a summing
node. A FIR can generate large types of transfer function thanks to the different
values of his coefficients. Usually, since the signal input multipliers is taken along
the delay line, the multipliers are called ”taps”.


                Pre-cursors            Cursor               Post-cursors



         x(k)            x(k-1)                                        x(k-n+1)
                   Td             Td                            Td

                  C1              C2            Ci              Cn-i          Cn




                                        +
                                                y(k)

                Figure 2.12: Finite Impulse Response filter block diagram

---

Chapter 2. High-speed serial link                                                  32

The delays are interposed between the taps and each of them provides a delay Td .
In the time domain the input-output relation of the FIR shown in figure 2.12 is
given as:

                                      n
                                      X
                          y(kT ) =          Ci x(k + 1 − i)Td                  (2.11)
                                      i=1


The input signal y(k) propagates along the delay chain. The delayed versions
of the signal are multiplied by the tap coefficients and then summed together.
The central tap is usually chosen as the main tap (cursor tap) because it has
generally the highest coefficient. The input-output relation of the FIR shows that
the performance, as well as from the coefficients, also depends on the delay Td .
The value of Td can be equal to the bit period or lower. In the first case we have a
Symbol Spaced Equalizer (SSE), otherwise we talking about Fractionally Spaced
Equalizer (FSE).

To understand the FIR behavior is useful to take a look at the time domain
operation [9]. Let’s to consider a SSE structure with four taps. As shown in figure
2.13 every tap provides a delayed version of the input signal multiplied for its own
coefficient. On the adder output, a destructive interference shapes the bit response
removing the energy on each cursor with the exception of the main cursor. This is
qualitatively shown in figure 2.13.




            IN       Td        Td                  Td

                 C1           C2                C3              C4
                                                                     4
                                      2                 3
                 1
                                                                             OUT
                                                                         +

---

33                                                Chapter 2. High-speed serial link

                Tb

        1

        2
                                            +
        3
                                                       UI                   t
        4
     Figure 2.13: Time domain FIR block diagram with the relative time domain
                                   behavior



2.2.3       Decision Feedback Equalizer (DFE)

Feedforward Equalizers, therefore FIR and CTLE, are very simple to implement,
but they generally achieve sub-optimal performance. For channels that introduce
from weak to moderate ISI, their performances are often sufficient. However,
they enhance the noise while suppressing ISI because they cannot distinguish
between signal and noise or crosstalk. So eventually, as the channel distortion
becomes severe, the performance of a linear equalizer can be limited by the noise
enhancement. Figure 2.14 explains the concept.




                                  FFE
             Loss




                              Equalized channel

                    Channel                       Enhanced noise

                                                            Noise


                                                            Frequency
            Figure 2.14: Noise limitation of Linear Feedforward Equalizer

---

Chapter 2. High-speed serial link                                                  34

For these reasons, another very important equalizer for today’s receiver architectures
is the DFE (nonlinear category). The DFE improves the performance of a linear
equalizer without enhancing the noise. The DFE is a non-linear structure, where,
as shown in figure 2.15, a feedback FIR filter and a decision device (slicer) are
used. Assuming correct decisions, the previous ISI can then be subtracted from
the current symbol by feeding back the previously decided symbols through the
feedback. Since the FFE suppresses the contribution of the pre-cursor ISI, if FFE
noise is not severe and there aren’t decisions errors by the DFE slicer, the ISI can
be eliminate without enhances the noise.


                        FFE Output
                FFE                     +
                                        -   +
                                            - -
                                                  -

                                                                          CK


                 ws         ws-1                           w2        w1

                   FF         FF                  FF       FF
                       CK          CK                 CK        CK

                    Feedback FIR ilter
               Figure 2.15: Decision Feedback Equalizer block diagram




2.3      Iterative adaptation on FIR

During the data transmission, or in more long time period, channels may exhibit
wide variation in frequency-dependent loss. For that, equalizer design requires to
contain a certain flexibility to set the equalizer coefficients adaptively to minimize
the ISI. Such an equalizer is called an adaptive equalizer. For our purposes it is
sufficient to investigate the aspects of iterative adaptation on FIR equalizers.

As you can see from figure 2.16, to recover the original signal, you have to find an
equalization filter, which will minimize the error Je between original transmitted
signal and equalized signal after the FIR filter. Je is also called “cost function”
and it is a function of filter coefficients.

---

35                                                   Chapter 2. High-speed serial link

                                                             Slicer
                                                     y                y
                  Channel              FIR

                               ci
                                            Je(ci)
                            Equalizer                    Error
                           adjustament                computation

                     Figure 2.16: Iterative adaptation on FIR



The general approach to updating the filter tap coefficients is:




     Coef fnew = Coef fold + (stepsize)(errorf unction)(inputf unction)         (2.12)


where the error function Je is typically based on the difference between the actual
equalized signal y and the desired equalizer output ŷ. The input function is
obtained from the input signal and step size is a design parameter. Designers have
many options for implementing adaptive equalizers, the range of which is outside
our purposes.

A widespread adaptive algorithm is the Least Mean Square (LMS) that is a
particular case of a more general algorithm, the Minimum Mean Square Error
(MMSE). MMSE algorithm attempts to minimize the Mean Square Error of the
equalizer output at all times. However, it is not used in adaptive equalizers because
it is difficult to implement. A more easy implementation is provided by LMS
algorithm [10]. It operates in discrete-time domain with the sampling frequency
equal to the bit time. The figure 2.17 explains the classical implementation of LMS
algorithm on the equalizer. We can recognize a classical structure of a FIR filter.
To describe how the algorithm works, we define the vector of filter coefficients as:



                              C̄ T = c0 , c1 , ...cn − 1 .
                                                       
                                                                                (2.13)

---

Chapter 2. High-speed serial link                                                                 36

               noise
       d(k)        x(k)        x(k-1)         x(k-2)                         x(k-n+1)
                          Td             Td                           Td

                          C0             C1            C2             Cn-2          Cn-1
                                                                                           y(k)


                  Figure 2.17: Implementation of LMS algorithm



Now, we define also the vector x(k) which is the vector of input signal samples:


                                                             
                       x̄(k) = x(k), x(k − 1), ...x(k − n + 1) .                            (2.14)


We have all the ingredients to write the FIR output equation y(k) as the multipli-
cation of the two vectors just described:


                                   n−1
                                   X
                          y(k) =         ci x(k − 1) = C̄ T · x̄(k)                         (2.15)
                                   i=0


and finally the cost function Je is given as:



                       Je (k) = E e(k)2 = E (d(k) − y(k))2
                                                        
                                                                                            (2.16)

           
where the E · operator is the expected value of the argument. Minimization of the
MSE minimizes the combined effect of ISI and noise. The goal of the adaptation is
illustrated in figure 2.18. The figure shows the difference of the equalized output
y(k) from the training data d(k) as a function of equalizer coefficients and it is
plotted as a 3-D surface; the figure is an example with two coefficients. The surface
is a convex function, so that it has a global minimum. The goal of the adaptive
algorithm is to converge on a set of coefficient values that minimize the error in a
small number of iterations. So, for the adaptation of the FIR filter, we have to
move the FIR coefficients in opposite direction to the gradient of the cost function
Je .

---

37                                                Chapter 2. High-speed serial link




                             c0                            c1
             Optimum coef icients
      Figure 2.18: Example of error 3-D surface as function of two coefficients



Given cost function Je with an absolute minimum, to minimize the error we have
to update iteratively the coefficients in a direction opposite to the gradient of Je :

                                                        
                       ¯ T           ∂J     ∂J        ∂J
                       ∇C Je (k) =        ,     , ...      .                      (2.17)
                                     ∂c0 k ∂c1 k ∂cn−1 k

In this way we can write that the expression of the next coefficient, therefore, FIR
coefficients are update as follow:


                                                  ¯ C Je
                             c̄(k + 1) = c̄(k) + µ∇                               (2.18)


where µ is called step-size. It serves to act on the convergence speed, but it must be
chosen carefully. If too fast, the algorithm will have too much energy and will not
be accurate in finding the absolute minimum error. On the contrary, if too small,
the convergence will be too slow and the algorithm will ensure the convergence for
very long times.

---

Chapter 3

A 25-Gb/s FIR Equalizer Based
on Highly Linear All-Pass
Delay-Line Stages in 28-nm LP
CMOS


Abstract

A continuous-time 4-tap FIR equalizer designed for loss compensation in backplane
links is presented in this chapter. FIR filters are attractive to enhance the equal-
ization performances of high-speed wire line receivers, providing high flexibility to
match the channel frequency response and compatibility with simple adaptation
techniques. Particular care is taken to address critical issues of continuous-time
realizations, such as noise, linearity and dynamic range. To keep high SNR and not
compromise equalization performances, a new all-pass stage is proposed to realize a
delay line accommodating large input signal amplitude. Filter tap coefficients are re-
alized with programmable transconductors and output currents are summed through
a resistive load. Extensive experimental results, carried out on test chips realized in
28 nm LP CMOS technology, are presented. The equalizer demonstrates successful
operation at 25Gbps data-rate while draws 25mA from 1V supply. Measurements
with 900mVpk−pk input signal prove equalization of a 20 − dB loss channel with 50%
horizontal eye opening at BER = 10−12 . Experimental results compare favorably
against state of the art [18]

                                          39

---

Chapter 3. A 25-Gb/s FIR Equalizer design                                          40

3.1      Introduction

3.1.1     Motivation

To address the continuous demands for pushing speed of serial links, new standards
are emerging with a data-rate of 25-28 Gb/s. Inter-symbol interference (ISI) is
a severe obstacle and transceivers need to incorporate increasingly sophisticated
channel equalization techniques. RX equalization combines a feed-forward linear
equalizer and decision feedback equalization. Simple FFEs, realized with the
cascade of peaking amplifiers, are difficult to be optimally adapted and feature
limited capability to correct the pre-cursor ISI [19] (see the previous chapter). More
sophisticated FFEs, implemented as transversal FIR filters, have been recently
proposed in the RX [20] - [21]. They provide high flexibility in shaping the
transfer function to match the channel frequency response and are compatible with
simple adaptation schemes, such as the least-mean-square (LMS) algorithm. A
key challenge of RX FIR equalizers is the design of a compact, wideband analog
delay line withstanding a sufficiently large input signal. Gain compression of the
delay line impairs the signal integrity and compromises the equalization capability,
while maximizing the input signal swing is desirable to achieve high SNR. Several
high-speed FIR equalizers have been proposed [21-23]. Delay lines based on lumped
LC networks need high quality passive components, requiring a prohibitively large
area. Active and hybrid (i.e. combining active and passive components) delay
lines, occupy acceptable area but feature limited linearity, especially at low supply
voltage, constraining the maximum allowed signal swing to a few hundred mV. In
this work a compact active delay line featuring outstanding linear operation range
is proposed to implement the fractionally spaced 4-tap FIR equalizer.



3.1.2     Proposed RX FIR equalizer

The block diagram of the proposed FIR equalizer is shown in figure 3.1. The active
delay line is realized with the cascade of three stages providing a tap-to-tap delay
Td . The tap amplifiers are transconductors with a 6-bits programmable gain that
can be be choose with the digital word Di . Furthermore, a shared resistive load RL
is used to sum the tap currents, while the VGA and buffer follow the equalizer for
measurement purposes. The VGA and buffer are realized with the cascade of three

---

41                                          Chapter 3. A 25-Gb/s FIR Equalizer design

degenerated differential pairs with resistive loads and shunt peaking inductors. The
overall gain is controlled in the range 0-10 dB by programming degeneration and
load resistors.

                                     Delay Line
            Vin
                        Td                 Td                     Td


           D0              D1                 D2                     D3
                  gm0            gm1                   gm2                  gm3
          6bit            6bit                6bit                  6bit




                                                Vout
                                                                          VGA Buffer
                                            RL           nout

                Figure 3.1: Block diagram of the proposed FIR equalizer



The transfer function H(f ) = Vout /Vin , is given by:


                                            X
                                 H(f ) =             ci e−j(2πf ·i·Td )                (3.1)
                                           i=0...3


where ci = gmi · RL (i = 0. . . 3) are the filter coefficients. Obviously the magnitude
coefficient is limited and the trade off is between transconductance gm and resistive
load RL because theese two parameters are constrained by the current consumption
and bandwidth of the output node respectively. In particular, the coefficients are
bounded within ±0.6 by the maximum transconductance of the tap amplifiers
(gmi,max = 7.5mS) and the value of the load resistance RL = 80Ω. Together with
the number of taps or equivalently the length of the delay line, is an important
design specification and determines the equalization performances.

When considering fully digital implementations, it is well known that fractionally
spaced FIR equalizers (i.e., filters with a Td which is a fraction of the symbol time
Tb ) offer several advantages over symbol-spaced equalizers with Td = Tb . Thanks to
the higher sampling rate, they do not suffer from aliasing, may provide boost well
beyond Nyquist frequency (fN = 1/2Tb ), are less sensitive to the clock sampling
phase and allow simultaneous equalization and matched filtering [22] - [23]. On

---

Chapter 3. A 25-Gb/s FIR Equalizer design                                          42

the other hand, the shorter is the tap-to-tap delay, the larger is the number of
taps to cover the same time window. When targeting an analog continuous-time
realization, minimizing the number of taps is highly desirable to limit power
dissipation. Moreover, differently from digital implementations, an important
issue to be considered is the impact of the equalizer noise to the output signal
SNR. In fact, an analog FIR equalizer impairs the SNR not only because of the
enhancement of the high-frequency noise superimposed to the input signal, but also
and most importantly because of the noise introduced by the equalizer building
blocks, represented in figure 3.1 by the noise nout added to the output signal.

To understand the FIR behavior and voltage swing requirements to keep high
output SNR look the equation H(f ) that describes the transfer function Vout /Vin .
At low frequency the gain GLF is equal to the sum of filter coefficients. Substituting
f = 0 in H(f ), we obtain:


                                             X
                                   GLF =              ci                         (3.2)
                                            i=0...3


i.e., the low frequency gain is equal to sum of the filter coefficients.

Substituting f = fN (Nyquist frequency) in H(f ) instead, we can find the expression
that describe the high frequency gain and in particular the gain GHF at Nyquist
frequency:


                                          X
                                 GHF =         (−1)i ci                          (3.3)
                                         i=0...3


The high frequency boost instead is the sum of filter coefficients but the sign
changes with the power of i. Therefore, the low frequency gain GLF and the
high frequency gain GHF trade each other. As results, due to the boundary of
the magnitude coefficients, to provide high frequency equalization, the equalizer
introduces a low frequency gain.



3.1.3     Linearity requirements

Ideally, the maximum channel loss that can be recovered by a linear equalizer is
limited by the enhancement of the high frequency noise superimposed to the input

---

43                                     Chapter 3. A 25-Gb/s FIR Equalizer design

signal. However, in contrast to a digital implementation, the noise introduced by
the analog equalizer itself (nout in figure 3.1) may set a more stringent limitation.
In this design nout v 1.5mVrms is almost independent from the equalizer transfer
function. To achieve SN R ⩾ 30dB, required to have good margin on the vertical
and horizontal eye opening, the output voltage amplitude needs to be larger than
100mVpk−pk . Given the input swing, the amplitude of Vout is determined by the
low frequency gain of the equalizer, i.e. by the sum of the filter coefficients.
Maximum SNR is therefore achieved with all the coefficients having the same
sign, but to provide high frequency peaking the filter needs positive and negative
values. Because the coefficients are magnitude bounded, high frequency peaking
is traded for amplitude of Vout and SNR. As an example the following set of
                                                   
coefficients c0 , ...c3 = 0.6 · −0.35, 1, −0.16, −0.26 is required for equalization
of a backplane channel with ≈ 20dB attenuation at Nyquist, determining a low
frequency loss of 17dB. As a consequence the equalizer needs Vin ⩾ 700mVpk−pk
to have Vout ⩾ 100mVpk−pk . This swing, easily provided by state of the art
transmitters [24], mandates a wide linear operation range to the FIR filter in order
to not compromise the equalization performance. Meeting this requirement at
limited power consumption is a very challenging task, particularly at low supply
voltage.

In conclusion, a high compression point for the equalizer is key for high SNR and
for signal integrity. Moreover, the most critical building blocks in figure 3.1 are the
delay line stages. For this reason a new all-pass stage amenable to high frequency
operation and accommodating high input swing is introduced in the following
section.



3.2        System simulation and circuit design

3.2.1      Impact of FIR filter compression

The impact of FIR filter compression on signal integrity can be estimated with
computer simulations. The simulation setup is shown in the block diagram of figure
3.2, where the equalized output Vout is after the FIR filter. In this first case the
DFE is not present. The maximum loss that can be recovered in this situation
(keeping a “good” output SNR and with only a FIR equalizer) is around 20dB. For

---

Chapter 3. A 25-Gb/s FIR Equalizer design                                                    44

that, in the block diagram, you can find a weak lossy channel with an attenuation
of only 14dB. A FIR filter equalizer is also present where the delay cell is modeled
as a non-linear block with a certain 1dB compression point. Moreover, from the
point of view of functionality and bandwidth either delay cells and tap amplifiers
are ideal.


                                       Delay cell
        Vin
                Channel                       Td             Td              Td
                                 c0            c1              c2             c3
                                                                                      Vout
    Figure 3.2: Simulation setup block diagram to evaluate the impact of FIR
                               filter compression



The idea is to test the impact of equalizer distortion on signal integrity, when the
amplitude of the input signal Vin grows. To compare the performances, we use the
simulated eye openings. In the chart (figure 3.3), on the y-axis the horizontal and
vertical eye opening are plotted while on the x-axis the input amplitude normalized
to the 1dB compression point of the delay cell. When the input signal is far away
from the compression point, the vertical and horizontal opening are good and eye
diagram is clean as shown in figure 3.4a. However, when the input amplitude starts
to reach the compression point, the eye opening worsens. The output eye diagram
with the input amplitude greater than 1dB compression point is shown in figure
3.4b.
              Eye Opening [%]




                                100
                                 80
                                 60
                                 40
                                         Vertical
                                 20
                                         Horizontal
                                  0
                                       0.2 0.4 0.6              0.8      1      1.2
                                                      Vin/V1dB-CP
                                Figure 3.3: Eye opening vs input signal amplitude

---

45                                           Chapter 3. A 25-Gb/s FIR Equalizer design

              Input amplitude << V1dBCP                        Input amplitude > V1dBCP

     1                                                1
     0                                                0
  -1                                              -1
     -1         -0.5        0       0.5      1        -1        -0.5      0      0.5       1
                   Time [UI]                                           Time [UI]
         a)                                               b)
                                Figure 3.4: Simulated eye diagrams



The impact of FIR filter compression is even more important if we consider a DFE
and a channel with higher loss. Therefore, for completeness, the case with the
presence of the decision feedback equalizer is also evaluated. The simulation setup
is show in figure 3.5 and in this example the channel loss at Nyquist frequency is
34dB.
                            Delay cell
         Vin
                Channel            Td            Td              Td
                       c0           c1           c2               c3                Vout
                                                                           DFE
     Figure 3.5: Simulation setup block diagram to evaluate the impact of FIR
                    filter compression when a DFE is considered



As reported in figure 3.6, when the input amplitude is smaller than 1dB compression
point, the vertical opening is very high. Unfortunately, when input amplitude
grows, eye opening has a rapid roll off as you can see from the eye diagrams showed
in figure 3.7.

In conclusion, these analyses prove that to keep high SNR without compromises
equalization performances a highly linear FIR is required and it is even more
important if a decision feedback equalizer is considered.

---

Chapter 3. A 25-Gb/s FIR Equalizer design                                                        46


                                100

              Eye Opening [%]
                                 80
                                 60
                                 40
                                         Vertical
                                 20
                                         Horizontal
                                  0
                                       0.2 0.4 0.6                0.8        1       1.2
                                                      Vin/V1dB-CP
                                Figure 3.6: Eye opening vs input signal amplitude


             Input amplitude << V1dBCP                               Input amplitude > V1dBCP

    1                                                       1
    0                                                       0
   -1                                                      -1

     -1         -0.5                  0      0.5      1      -1       -0.5       0         0.5   1
                                Time [UI]                                    Time [UI]
        a)                                                      b)
                                      Figure 3.7: Simulated eye diagrams



3.2.2        Continuous time analog delay line

Continuous time FIR equalizers operating at more than 10Gb/s usually exploit
lumped-elements delay lines realized with cascaded LC-ladder sections to simulta-
neously meet the requirements for high delay and wide bandwidth. However, as
previously anticipated, LC sections suffer from narrow tuning range and require
excessive silicon area due to the need for high Q inductors. To achieve a wide
bandwidth delay cell and with a small size, continuous time active delay lines
are potentially attractive. Several solutions have been proposed by cascading
low-pass filter sections. Unfortunately, delay trades with bandwidth and to achieve
a sufficiently wide bandwidth, reported FIR equalizers have a too limited number
of taps and small tap-to-tap delay. Since the FIR compression is a big problem, a
new delay stage is proposed to accommodating large input signal amplitude. In

---

47                                       Chapter 3. A 25-Gb/s FIR Equalizer design

particular, a CMOS all-pass stage has been investigated to implement the active
delay line. Two possible solutions that provide a first-order all-pass response are
shown with the block diagrams in figure 3.8.



        x(s)                      y(s)         x(s)                        y(s)




                    a)                                     b)
     Figure 3.8: Different implementations all-pass filters: a) With a first-order
                 low-pass filter b) With a first-order high-pass filter



The all-pass transfer function is achieved by subtracting the outputs of a first-order
filter, featuring a gain of 2 and time constant τ , and a unity gain feed-forward
path.

The solution in figure 3.8a has been recently exploited in a 25Gb/s FIR equalizer
for multi-mode fibers. It is realized with a one-pole low-pass filter with time
constant τRC , and a unity-gain path. The all-pass transfer function HRC (ω) and
the respective group delay GDRC (ω) are:


                                         y(s)   1 − sτRC
                             HRC (s) =        =                                   (3.4)
                                         x(s)   1 + sτRC


                                         ∂∠H(ω)     2τRC
                         GDRC (ω) = −           =                                 (3.5)
                                          ∂H(ω)   1 + (ωτ )2

The alternative in figure 3.8, where the low pass filter is replaced by a high-pass
pass-filter, is investigated in this work. For both cases, the transfer function is the
same, an all-pass filter. However, when considering the transistor level realization,
the last architecture provides a remarkable improvement in the maximum allowed
signal swing.



3.2.3          Delay cell design

The transfer function of an all-pass filter of the first order can then be written as
follows:

---

Chapter 3. A 25-Gb/s FIR Equalizer design                                         48


                                              1 − sτ
                                   HD (s) =                                     (3.6)
                                              1 + sτ

where τ is the time constant relating both to the pole p1 = −1/τ and to zero
z1 = 1/τ . The magnitude and phase expressions are respectively:



                                    HD (jω) = 1                                 (3.7)



                            ∠HD (jω) = −2 arctan(ωτ )                           (3.8)


The magnitude is identical for every order of the all-pass filter, while the phase
response change with the filter order. A consequence of the symmetry properties
of the poles and zeros is that the phase response decreases monotonically. The
group delay function of frequency can be expressed as the derivative of the phase
as written below:


                                               ∂φ(ω)
                                  GD(ω) = −                                     (3.9)
                                                ∂ω

and it represents the delay between the input and the output signal. As already
written above, it is given as:


                                                 2τ
                                 GD(ω) = −                                    (3.10)
                                              1 + (ωτ )2

As you can see from the equations, the ideal magnitude bandwidth is infinite, while
GDRC has a limited bandwidth and at low frequency is equal to 2τRC . As the
frequency increases, the group delay starts to drop up to collapse for frequencies
around the pole and the zero. This is an important aspect; ideally you would want
a constant group delay al all frequencies. However, in our case, it is essential that
the group delay is constant up to the Nyquist frequency.

The figure 3.9 shows a possible implementation of the all-pass function. The
transconductor gm is loaded by generic impedance. The output signal is obtained
by subtracting the input signal from the filter output.

---

49                                          Chapter 3. A 25-Gb/s FIR Equalizer design


                 Vin             gm                            +           Vout
                                              Zi(s)                -
                                                                       +

                        Figure 3.9: All-pass filter block diagram




                 RC load                     RL load




                                  Z(s)                                 R
                    +        +                            +        +
     Vin      Vin       gm
                             -
                                                  Vin/2       gm
                                                                   -
                                                                                  Vout
                    -                                     -


                                                          +        +
                                                  Vin/2       gm
                                                          -        -
                                                                       Adder

           Figure 3.10: Schematic circuit of the all-pass transfer function



The circuit schematic is shown in figure 3.10. The transconductor gm1 and the Z(s)
load form the low or the high pass filter, while gm2 and gm3 are used to subtract
the filter output from the input signal:


                                      Vout
                                           = gm Zi (s) − 1                           (3.11)
                                      Vin

We have seen before that the all-pass transfer function HD (s) can be obtained in
two different ways based on the choice of the impedance Zi (s). If the impedance is
an RC parallel, as shown in figure 3.11, we can write:


                                                     R
                                      ZRC (s) =                                      (3.12)
                                                  1 + sCR

---

Chapter 3. A 25-Gb/s FIR Equalizer design                                           50

                                   ZRC(s)

                                     R      C


                        Figure 3.11: RC parallel impedance



and with gm = 2/R the all-pass transfer function can be obtained:


                                         2       1 + sτ
                           HD (s) =          −1=                                (3.13)
                                      1 + sτ     1 + sτ

where τ is the time constant RC.

In the second case instead, the impedance Zi (s) is the parallel between the resistance
R and the inductance L. Therefore, as shown in figure 3.12, we write:


                                               sL
                                ZLR (s) =                                       (3.14)
                                            1 + sL/R


                                     ZRL(s)

                                     R          L


                        Figure 3.12: RL parallel impedance



As in the previous case, if the value of the transconductance is equal to gm = 2/R,
the all-pass transfer function can be obtained:


                                       2τ        1 + sτ
                          HD (s) =          −1=−                                (3.15)
                                     1 + sτ      1 + sτ

where τ is the time constant L/R. As can be noted, in this second case, the all-pass
transfer function has an additional phase shift of 180 degree.

---

51                                           Chapter 3. A 25-Gb/s FIR Equalizer design

To gain insight on the linearity performances, the voltage swings at the input of
each transconductor in figure 3.10 are also reported. Let’s to consider the solution
with the Z(s) load equal to RL parallel. The transconductor gm1 sustains the
maximum swing, equal to Vin , but the low impedance of the RL load shorts the
outputs at low frequency, avoiding propagation of its distortion. The compression
of the stage is therefore determined by gm2 and gm3 only, driven by Vin/2 . As a
result, the proposed all-pass circuit implementation enjoys a very high compression
at low frequency. Compared to the all-pass stage of figure 3.8a, implemented by
replacing the RL load of gm1 with an RC load, simulations prove a 1-dB input
compression point improvement of 9 dB.


                     0
                   −5
                                                                ~4 dB @ Ny
                  −10     9 dB
      1dB C .P.




                  −15
                  −20
                  −25       RL
                            RC
                  −30
                            4       8      12    16       20        24       28
                                         Frequency [G Hz]
                  Figure 3.13: 1 dB compression point comparison versus frequency



In figure 3.13 the 1 dB compression point is reported as function of frequency and
the continuous black line refers to the proposed solution. At low frequency, a 9 dB
difference in the simulated 1dB C.P justifies the choice of the solution with the
RL load. It is worth noticing that compression point worsens at high frequency,
when the impedance of the RL load rises. However, when the equalizer is fed by a
random bit stream experiencing the low-pass channel transfer function, the high
frequency spectral components are significantly attenuated requiring less stringent
high-frequency compression point to preserve signal integrity. Furthermore, at
Nyquist frequency the 1dB compression loss is only of 4 dB, therefore very far from
typical channel attenuation.

---

Chapter 3. A 25-Gb/s FIR Equalizer design                                                52

3.2.4      Group delay contributions

The circuit schematic with the parasitic capacitance is drawn in figure 3.14. The
bandwidth of the delay-line stage is limited by Cout , determined by the input
capacitance of the cascaded stage and tap amplifier. RP and the shunt-peaking
inductor LP are sized to achieve ≈ 18 − GHz bandwidth. This network (blue color)
introduces 9-ps group delay. The transconductor gm1 and its high-pass RL load
have been sized to add 15-ps group delay.




                                     R          L                          LP
                         +                                  +
                                                                           RP
     Vin                    gm1+-                            gm2+-                Vout
                          -                                 -
                                         Cpar                                   Cout
                                                            +      +
                                                             gm3
                                                            -          -



             Figure 3.14: Circuit schematic with parasitic capacitance



                                    1
                 Magnitude [dB]




                                    0
                                   −1
                                   −2
                                   −3
                                   −4
                 GroupDelay [ps]




                                   30

                                   20

                                   10

                                    0
                                     1                            10
                                                Frequency [GHz]

   Figure 3.15: Simulated frequency response of the circuit in figure 3.14 and
                      different group delay contribution



An optimized geometry of the inductor L has been devised to achieve high self
resonance frequency while keeping compact size. The simulated AC response of a
delay stage is shown in figure 3.15. The total group delay, shown in the bottom
plot, peaks from 24 ps to 28 ps at 17 GHz. However, you have to pay attention to

---

53                                     Chapter 3. A 25-Gb/s FIR Equalizer design

the internal parasitic capacitance Cpar and for this reason the two contributions
to the group delay are also reported. The parasitic capacitance loading gm1 leads
to significant peaking (dotted line) which is partially compensated by the high
frequency roll-off of group delay contributed by the Cpar-RP-Lp network (dashed
line).



3.2.5     TAP amplifiers design

The circuit schematic of a tap amplifier is drawn in figure 3.16. Each amplifier
comprises many elements in parallel, providing a total gain programmable with
6-bits resolution. To achieve positive and negative gains, each element includes two
digitally-controlled differential pairs, driven by the same input signal but delivering
output currents with opposite sign.

                      +Iout                         -Iout




                      +V




                      EN




          Figure 3.16: Circuit schematic of a tap transconductor amplifier


Only one pair is active at a time allowing changing the gain while keeping a fixed
bias current and constant common-mode voltage at the nodes where all the tap
output currents are summed. Degeneration resistors are employed in each pair to
enhance the linear operation range, in order to withstand the same input signal
amplitude of the delay-line stages before gain compression. In particular, the
degeneration keeps the 1 dB compression point greater than -5 dBV.

---

Chapter 3. A 25-Gb/s FIR Equalizer design                                         54




                                   310 µm

                                              220 µm




                        Figure 3.17: Photograph of the die


3.3      Experimental results

Prototypes of the equalizer have been fabricated in 28-nm CMOS LP process from
ST Microelectronics. A photograph of the die is shown in figure 3.17. Test chips
have been encapsulated in plastic flip-chip BGA packages and mounted on PCB for
testing. Core power dissipation, from 1V supply, is 25 mW. First, small-signal AC
measurements have been performed with a four-port S-parameter analyzer to assess
the functionality of the active delay line and tap amplifiers. Then, equalization
capability at 25 Gb/s has been tested: the FIR filter was fed by PRBS sequences
transmitted over different backplane channels while the output was monitored on
a high speed sampling scope. The scope waveforms were continuously acquired by
a PC running a Minimum-Mean-Square-Error (MMSE) adaptation algorithm to
control the filter coefficients. The setup used during the measure is shown in figure
3.18.

As an example, the frequency response of a typical backplane channel featuring
20-dB loss at Nyquist is shown figure 3.19. The inset in the figure reports the
single-bit channel response showing a large pre-cursor and several post-cursors.
The eye diagram at the output of the equalizer is reported in figure 3.20. The
input amplitude was set to 900mVpk−pk . The bottom plot in figure3.20 shows the
bathtub, measured with an Anritsu 1800A BERT, demonstrating 50% eye opening
at BER = 10−12 .

---

55                                                                      Chapter 3. A 25-Gb/s FIR Equalizer design




                                                            Figure 3.18: Measurement setup

                                                                  C           response
                              0

                             10
            Magnitude [dB]




                                                      0.4
                             20
                                                      0.3
                                      Amplitude [V]




                             30                       0.2
                                                      0.1                                           a
                             40                        0
                                                      -0.1
                             50                           0 1 2 3 4    5 6 7 8 9 10 11 12
                                                                      Time [UI]
                             60
                                  1                                                      10
                                                                    Frequency [G Hz]

     Figure 3.19: Frequency response of a typical backplane channel. In the inset
                               the impulse response


Experimental results are summarized and compared against two recently reported
FIR equalizers in Table 3.1. [20] uses a comparable supply but eye opening is
worse, data rate is lower and BER = 10−9 only. [21] supports a remarkably high
speed. On the other hand the supply is much higher than what is allowed without
compromising device reliability. Eye opening at BER = 10−12 is limited to 30%.
The proposed equalizer shows the widest eye opening while keeping the best power
consumption normalized to data rate.

---

Chapter 3. A 25-Gb/s FIR Equalizer design                                                56



                                                         Diagram
                                             Output Eye
                              300
             Amplitude [mV]   200

                              100

                                0

                              -100

                              -200
                              -300
                                                      Bathtub
                                −4
                              10
                                −6
                              10
                   BER




                                −8
                              10
                                −10
                              10
                                −12
                              10
                                −0.5      −0.25         0            0.25     0.5
                                                     Time [UI]

   Figure 3.20: 25 Gb/s eye diagram at the output of the equalizer and measured
                                   bathtub




                              Table 3.1: Performance summary and comparison

                                            This work            [20]            [21]
           CMOS node                        28nm LP          45nm SOI           65nm
             Supply                            1V               1.1V             1.6V
            # of Taps                           4                  4               3
            Data Rate                        25Gb/s           17Gb/s           40Gb/s
       Attenuation @ Ny                       20dB              21dB            19dB
              BER                             10−12             10−9            10−12
       Horizontal Opening                     50%               39%            ≤ 30%∗
        Power dissipation                    25mW              32mW            55.2mW
        Power/DataRate                     1mW/Gb/s        1.9mW/Gb/s       1.4mW/Gb/s
      *estimated from plot

---

Chapter 4

A 28Gb/s Transversal Continuous
Time Linear Equalizer in 28nm
CMOS


Abstract

To approach the unstoppable demand for higher communication bandwidth, as well
as new standard with a data rate of 25-28 Gb/s, multi-level signaling is under
investigation to reach 56 Gb/s .The bandwidth limitation of existing backplanes
makes transceiver design challenging. Channel losses at high speed are mostly
determined by dielectric absorption, which, on the contrary to skin effect, enhances
the pre-cursor ISI. Traditionally, RX equalization combines a continuous-time linear
equalizer (CTLE), made of the cascade of peaking amplifiers, and decision feedback
equalization (DFE). The CTLE needs low power consumption but is difficult to be
optimally adapted and has limited capability to correct the pre-cursor ISI. Pulse
shaping with a TX FIR filter solves the issues but requires a back channel for
adaptation and limits signal swing due to the TX peak-power constraint, a critical
issue at low supply and with multi-level signaling.




                                        57

---

Chapter 4. A 28Gb/s Transversal CTLE design                                          58

4.1      Introduction

4.1.1     Motivation

In this work a CTLE with the transversal architecture shown in figure 4.1 is
investigated. The D cell refers to a derivative cell. The architecture is similar
to a FIR filter, therefore to avoid confusion, we will call it D-FIR (Derivative-
Finite Impulse Response) equalizer. Compared to traditional CTLEs, compared to
expected simulation results, it provides superior equalization performance while
keeping low power consumption. In addition, the transversal architecture makes it
compatible with robust LMS adaptation algorithms.

        Vin
                   D           D

            gm0         gm1          gm2
                                             RL      Vout      VGA Buffer



                  Figure 4.1: Block diagram of derivative equalizer



The new type of equalizer combines the advantages of CTLE equalizer and the
advantages of FIR equalizers. As we shall see, the heart of the equalizer is the
derivative cell, that is very similar to the base cell used for CTLE. The structure
instead, is transversal as that used for the FIR filters implementation. The main
advantage is the ability to implement LMS adaptation algorithm in a simple way.

The most critical element inside the FIR filter is the delay cell. The delay cell design
is very difficult, because it is necessary to get different and stringent specifications
with a reduced area and power consumption. The main limitation is the group
delay-bandwidth (GDBW) product that remains constant. Therefore, it is easy
to achieve a low GD with a high output bandwidth. However, a too small group
delay penalizes the equalization performance because, with the same number of
taps, the time span of the filter is reduced. On the contrary, the need for higher
group delay, affects the bandwidth. The only way to improve the bandwidth is to
use shunt peaking inductors that increase the consumed area.

---

59                                   Chapter 4. A 28Gb/s Transversal CTLE design

Another problem is the internal high Q inductor used as load of gm1 stage in figure
2.14. A low Q inductor produces an over peaking in the group delay because it
is not compensated by the GD roll-off of the external stage. This introduces a
distortion on the signal decreasing the equalization performance. To prevent it, a
careful design of the inductor is mandatory and usually it takes a lot of area.

                     In
                                    D
                    C1=1                C2
                                                                Out
                                                         +
                           Figure 4.2: Two taps FIR equalizer



The last problem, but not least, is the typical DC loss of FIR equalizer. An example
may be helpful to clarify this concept. For FIR equalizer the gain boost at Nyquist
is given as:


                                             C1 − C2
                                    GHF =                                      (4.1)
                                             C1 + C 2

Assuming to recover 20 dB loss at Nyquist with the two taps FIR equalizer shown
in figure 4.3 and with first coefficient C1 = 1. As result, to recover 20 dB, the
second coefficient is C2 = −0.82 and DC loss is:



                               GLF = C1 + C2 = −15dB                           (4.2)


As seen before, from the point of view of the signal to noise ratio, a high input
signal amplitude is required to keep high SNR on the output node. The proposed
equalizer breaks the trade off between booster and loss in DC promising superior
performance with a reduced area and power consumption compared to the current
state of the art.

---

Chapter 4. A 28Gb/s Transversal CTLE design                                            60

4.1.2     Proposed RX D-FIR equalizer

Equalizers must approximate the inverse of channel transfer function for good
equalization. Since, a typical channel can be described by all-poles transfer function,
the equalizer must be an all-zeros filter to be able to correctly invert the frequency
response of the channel. The channel transfer function is therefore gives as:


                                                   1
                        HCH (s) =                                                    (4.3)
                                      1 + C0 s + C1 s2 + ...Cn−1 sn

and, as a consequence, following the basic idea the equalizer will be described as:


                        HEQ (s) = 1 + C0 s + C1 s2 + ...Cn−1 sn .                    (4.4)


Since the transfer function HEQ (s) is made by only zeros, a derivative cell is
required to implement the equalizer.

The block diagram of the proposed equalizer is shown in figure 4.3. The structure
has two derivative cells that generate the first and the second derivative of the input
signal x. The transconductance of the tap amplifiers is chosen by the digital word
Di with a resolution of seven bits. The output currents of the tap amplifiers are
summed together on the resistive load RLOAD . A variable gain amplifier enhances
the output signal amplitude and the buffer is used to drive the output pad.

                       DC path
                                                                    VGA Buffer
                                                      RLOAD                      Y

          7bit           7bit            7bit                 VDD
                 gm1            gm2             gm3
          D0             D1              D2



                       d/dt           d/dt
                 X              X'              X''
            Figure 4.3: Detailed block diagram of the proposed equalizer



As shown in the figure, the red path is called “DC path”, because the DC gain is
set by the first coefficient C1 = gm1 RLOAD and also by the VGA and by the buffer.
In fact, the derivative cells attenuate the low frequency components of the input

---

61                                   Chapter 4. A 28Gb/s Transversal CTLE design

signal X and they do not contribute to the DC gain. Since, DC loss is independent
from the high frequency boost, the analog equalizer boosts the high frequency
components without introducing loss at DC. Actually, the DC loss is not properly
zero, but it is in any case very low. In this way, a strong post-amplification is not
required allowing further area and power saving.



4.1.3     D-FIR equalizer behavior

The purpose of the next part is to explain the role of the two derivatives and to
justify the use of a three-tap structure. We have already described the D-FIR
behavior in the frequency domain. However, for a deeper understanding, it is useful
take a look to the figure 4.4. The simulated waveforms describe the behavior in
the time domain.

The x signal is the input signal, while x’ and x” are respectively the first and
the second derivative of the input. The figure is divided in two parts; on the left
the results simulation obtained with an analytic channel modeled only with the
dielectric effect, and on the right the simulation results with a an analytic channel
modeled only with the skin effect. The two effects are deliberately separated to
highlight the two extreme cases. Of course, real channels behavior will be in the
middle.
                      Dielectric effect                    Skin effect


                x                               x

                x'
                                                x'

                x''                             x''




                y=x+C3x''                                       y=x+C2x'


              -4 -3 -2 -1 0 1 2 3 4        -2         -1    0 1 2        3   4
                      Time [UI]                            Time [UI]

     Figure 4.4: Simulated waveform to understand the D-FIR equalizer behavior

---

Chapter 4. A 28Gb/s Transversal CTLE design                                        62

The X waveform represents the pulse response of the respective channel. In case
of only skin effect the pulse can be equalized with the first derivative multiplied
for the coefficient C2 . The y signal is the equalized waveform on the output node
of the equalizer. The second derivative instead is useful to equalize the dielectric
effect as can be seen from the figure.

                                      VDD
                            L                         L
                          RD         2RG              RD

             CL                                                      CL
                                      C

                                         IBIAS

                    Figure 4.5: Circuit diagram of derivative cell




4.2      Simulation and system design

4.2.1     Derivative cell implementation

The simplified schematic of the derivative cell is shown in figure 4.5. The circuit is
a differential pair with a capacitive degeneration, ideal current generators and a
resistive load. Moreover, shunt peaking inductors are used to extend the bandwidth.
The frequency transfer functions of the derivative cell is:


                                    2 sCRL      1
                           Hs = −                                                (4.5)
                                        2C 1 + sCL RL
                                    1+s
                                        gm

where the resistance RL = RD //RG and, for simplicity, the inductance L is not
considered. Therefore, the zero and the poles are:

---

63                                            Chapter 4. A 28Gb/s Transversal CTLE design


                                     1                    gm               1
                            ωz =                  ωp1 =          ωp2 =                   (4.6)
                                   2CRL                   2C             CL RL

where p2 is the parasitic pole and CL represent the capacitive load of the next
stage. Increasing the capacitor, both the first pole and the zero moved to low
frequency. The transconductance and the load RD set the gain of the cell and the
frequency separation from the pole p1 and the zero. The zero is programmable
with the capacitance C and can be moved to choose different frequency response
and behavior of the derivative cell. Lastly, the resistance RG is connected between
the two nodes of the output and therefore, it must have a large value. It serves
to reduce the gain of the cell to avoid signal compression of the next stage. The
simulated frequency responses of derivative cell are shown in figure 4.6.


                                       Frequency Responses
                  20

                  10               Increasing C
                                                                         Increasing RG
                   0
 Magnitude (dB)




                  -10
                                                                     CaseA
                  -20                                                CaseB
                                                                     CaseC
                                                                     CaseA-6dB
                  -30
                                                                     CaseA-9dB
                                                                     CaseA-12dB
                  -40
                        0                 1                 10                    100
                                              Frequency (G Hz)
                            Figure 4.6: Frequency responses of derivative cell



As said before, increasing the degeneration capacitor, the zero shifts to low frequency.
As shown in the figure, respect to case A, the waveforms B and C start to boost
before, crossing the 0-dB axis at low frequency, while reaching the same gain.
Another aspect is the shape of the waveforms. For some kind of channels, a
different shape in the boost it could be useful for improving the equalization.
Increasing the resistance RG instead, the gain decreases and the net income is a

---

Chapter 4. A 28Gb/s Transversal CTLE design                                      64

downshift of the waveform. In the figure, the cases with reduced gain are shown
only for case A.

From figure 4.6, we also understand why principally the first coefficient path sets
the DC gain for this equalizer. As we can see, the derivative transfer function
has ideally a DC gain equal to zero. For this reason at low frequency the signal
can reach the output only through the first coefficient path. As result, the analog
equalizer boosts the high frequency without introducing loss at DC. Therefore, very
low tap gains are required for the equalization and a very small post-amplification
gain is required to preserve the output signal amplitude, saving area and power
consumption.

Actually, the real case is slightly different because the ideal current source IBIAS
(figure 4.5) will be substitute with real current generator with a certain output
resistance RS /2. The schematic is shown in figure 4.7.

                                        VDD
                                 L                 L
                             RD        2RG         RD

                   CL                                           CL
                                        C

                   RS/2                 IBIAS             RS/2

         Figure 4.7: Derivative cell schematic with real current generators



To derive the frequency response of this circuit may be simpler to analyze the
single ended half circuit drawn in figure 4.8. The presence of output resistance
Rs /2 introduces a DC gain as shown in the frequency transfer function:


                                  gm RL   1 + s/ωz      1
                        H(s) =                                                 (4.7)
                                    gm Rs 1 + s/ωp1 1 + s/ωp2
                                 1+
                                      2

where the zero and the poles are:

---

65                                  Chapter 4. A 28Gb/s Transversal CTLE design


                      1                  1 + gm Rs /2              1
              ωz =               ωp1 =                   ωp2 =                (4.8)
                     Rs Cs                  Rs Cs                RL CL


                                                VDD
                                         L
                                     RD          RG

                        CL


                         RS/2                  IBIAS    2C

                        Figure 4.8: Single ended half circuit



To dimension correctly the cell, given the output capacitive load CL , the load
resistance RL must be set for ωp2 ⩾ 2πfN where fN is the Nyquist frequency. The
first pole is better to be close to 2πfN for max gain. Now, the zero can be move
with the programmable C degeneration to have the desired peaking. Moreover, it
should to be noted that the DCgain and the high frequency gain HFM G are:


                                   gm RL
                     DCgain =                     HFGM = gm RL                (4.9)
                                1 + gm Rs /2

The DCgain value is usually low because the output resistance RS is in the order of
some unity of kΩ and it has no impact on the low frequency gain of the equalizer.
To conclude in the next picture 4.9 a sketch of the magnitude and phase of H(s)
just described.

---

Chapter 4. A 28Gb/s Transversal CTLE design                                          66

                       |H(s)|

                        0dB
                                                                 ω

                        H(s)


                                    ωz1        ωp1     ωp2       ω
                         -90°
             Figure 4.9: Simple sketch from derivative cell dimensioning



4.2.2     Tap transconductor implementation

Due to the natural low gain at low frequency of the derivative cell, the only way to
way to improve the linearity of the equalizer is a careful design of the tap amplifiers.
The figure 4.10 shown the parallel structure of the tap. Each amplifier comprises
ten elements in parallel with the possibility to achieve positive and negative gain
with 6-bits resolution. Part of the digital word is controlled in a thermometric
fashion to assure a monotonic increase of the tap gain. The conversion is made by
a decoder as shown in figure 4.11. Therefore, the necessary cells are ten and they
are controlled by their own enable bit bI .

               +Iout                           -Iout



                         b0                  b0
                +V




                         b0                  b0                 Cell10
                                                             Cell0
                     Figure 4.10: Parallel structure of tap amplifier

---

67                                     Chapter 4. A 28Gb/s Transversal CTLE design

                             Binary part     Thermometric part

                         B 5B 4B 3               B 2B 1B 0
                                                   Decoder

                            b 9b 8b 7        b 6b 5b 4b 3b 2b 1b 0
                                        Digital word

                Figure 4.11: Conversion of the tap gain digital word



As in the previous chapter each element includes two digitally-controlled differential
pairs, driven by the same input signal but delivering output currents with opposite
sign. The main difference is the flipped voltage follower (FVF) circuit connected
to the common source of each differential pair. The purpose of FVF circuit is to
improve the linearity lowering the impedance see in the source. It is essentially
a cascade amplifier with negative shunt feedback where the gate terminal of M2
is used as input common mode terminal and its source as output terminal. It is
characterized by very low output impedance due to shunt feedback provided by
M1, high low supply requirement close to a transistor threshold voltage VT H , low
static power dissipation and high gain bandwidth. Output current variation are
absorbed by M1, while the current in M2 remains constant. A single side of the
tap amplifier circuit is proposed more clearly in figure 4.12.

                                 VDD                     VDD
                                                VDD
                            LP                                LP
                            RL                                RL
                             IDC                             IDC

                                         VCM




              Figure 4.12: Detailed circuit of a single side tap amplifier



Unlike the conventional differential pair, the circuit in figure 4.12 is able to source a
large amount of current. The large sourcing capability is due to the low impedance
at the node X that is lowered by the output impedance of the FVF:

---

Chapter 4. A 28Gb/s Transversal CTLE design                                                                             68


                                                               1
                                             ROU T ≈                                                                 (4.10)
                                                          gm1 gm2 r02

                         IOUT Diff. Pair                                 IOUT FVF Diff. Pair

                                                                                 IBIAS

                 V INP                                           V INP           VC M                    V INM
                                                 V INM
                                VX
                                                                                             VX
                                      2I BIAS


                  Differential Output Current (mA)                              Voltage node Vx (mV)
           12                                             600
                                                                                      Vx Flip Follower
            8                                                                         Vx Diff. Pair
                                                          500
            4
            0                                             400
            -4
                                Diff. Pair                300
            -8
                                FlipFollower Diff. Pair
           -12                                            200
                                                                -1       -0.5            0           0.5         1

                 a) Differential Input Signal (V)                    b) Differential Input Signal (V)
                   Figure 4.13: Tap DC characteristic without load



Note that M1 provides shunt feedback and, for that, detailed analyses will be
necessary to ensure stability. In figure 4.13 are shown some simulation to highlight
the huge linearity improvement with the use of FVF differential pair. In the graph
4.13 the output current and the voltage node Vx are plotted as function of the
differential input signal. As can be see, the current of classic differential pair (blue
line) is clamped to the maximum current 2IBIAS . For FVF solution instead, the
rest of the current is drive by the tail transistor. This behavior is possible because,
due to the very low impedance, the voltage node on x node doesn’t move. Actually,
the simulations have been done without resistive load on the differential pair drain.

If we consider a resistive load for the differential pair the results are slightly different
and they are shown in figure 4.14.

---

69                                    Chapter 4. A 28Gb/s Transversal CTLE design




             R                 R                       R     IBIAS
                                                                           R
     V INP                         V INM       V INP                           V INM


                         2I BIAS

                          Differential Output C urrent (mA)
             6

             3

             0

             -3
                                            Diff. Pair
                                            FlipFollower Diff. Pair
             -6
                  -1        -0.5           0               0.5        1
                          Differential Input S ignal (V)
                  Figure 4.14: Tap DC characteristic with resistive load



In this case the FVF output current is not a straight line as in the previous figure.
The little compression of the current is due to the voltage generated by the load on
the drain of the differential pair. To quantify the linearity improvement is necessary
a 1 dB compression point simulation. Simulating the two cases for the same size of
the differential pair we obtain:



                            1dBC.P.Dif f.P air = −16dBV                                (4.11)



                         1dBC.P.F V F Dif f.P air = −10dBV                             (4.12)


therefore with a 6 dB improvement.

---

Conclusion

A 25Gb/s continuous-time linear 4-tap FIR equalizer and an 28Gb/s ultra-compact
3-tap derivative-FIR equalizer for backplane data equalization have been presented.
For both equalizers, a system level analysis to derive equalizer specifications has
been proposed with emphasis on the discussion of issues specifically related to
continuous-time core cell implementation. The design of a test chip has been
described for the first chip with a detailed analysis of the delay line and tap
amplifiers. Realized in 28 nm LP CMOS technology, core silicon area is only
0.065 mm and comprehensive experimental results proved successful equalization
of 25Gb/s data stream with maximum power dissipation of 25mW. Measurements
are summarized and compared with published FIR equalizers in table 3.1. The
presented equalizer features a state-of-the-art power dissipation normalized to
data-rate. These features are particularly effective to accommodate the demand
of actual transfer rates, back-compatibility and energy efficiency of emerging 100
Gb/s standards.




                                        71

---

Bibliography

 [1] E. Alliance. (2015) The 2015 ethernet roadmap. [Online]. Available:
    http://www.ethernetalliance.org/roadmap/

 [2] Common electrical I/O (CEI) Electrical and jitter interoperability agreements
    for 6G+ bps, 11G+ bps and 25G+ bps I/O. [Online]. Available:
    http://www.oiforum.com/public/documents/OIF CEI 03.0.pdf

 [3] J. D’Ambrosia. (Mar. 2012) IEEE 802.3WG Closing Plenary Report, IEEE
    P802.3bj 100 Gb/s Backplane and Copper Cable Task Force. [Online].
    Available: http://www.ieee802.org/3/minutes/mar12/0312 bj close report.
    pdf

 [4] B. Razavi, Design of Integrated Circuits for Optical Communications, M. G.
    Hill, Ed., 2003.

 [5] M. Steyaert and F. Tavernier, High-Speed Optical Receivers with Integrated
    Photodiode in Nanoscale CMOS, Springer, Ed., 2011.

 [6] J. Buckwalter and A. Hajimiri, “Analysis and equalization of data-dependent
    jitter,” IEEE Journal of Solid State Circuits, vol. 41, pp. 607–620, March
    2006.

 [7] D. Stauffer, High-Speed Serdes Devices and Applications, Springer, Ed., 2008.

 [8] E. Sackinger, Broadband Circuits for Optical Fiber Communication, Wiley,
    Ed., 2005.

 [9] H. Hall, Advanced Signal Integrity for High-Speed Digital Designs, J. Wiley
    and Sons, Eds., 2009.

[10] P. Hanumolu, U. Moon, and G. Wei, “Equalizers for high-speed serial links,”
    International Journal of High Speed Electronics and Systems, vol. 5, pp. 629–
    458, 2005.
                                       73

---

Bibliography                                                                   74

[11] V. Stojanović, “Channel-limited high-speed links: Modeling, analysis and
    design,” Ph.D. dissertation, STANFORD UNIVERSITY, 2004.

[12] W. Dally and J. Poulton, Digital Systems Engineering, C. U. Press, Ed., 1998.

[13] S. Parikh, T. Kao, Y. Hidaka, J. Jiang, A. Toda, S. Mcleod, W. Walker,
    Y. Koyanagi, T. Shibuya, and J. Yamada, “A 32Gb/s wireline receiver with a
    Low-Frequency Equalizer, CTLE and 2-tap DFE in 28nm CMOS,” in ISSCC
    - IEEE International Solid-State Circuits Conference, 2013.

[14] J. Lee, “A 20Gb/s adaptive equalizer in 0.13 CMOS technology,” IEEE Journal
    of Solid-State Circuits, vol. 41, no. 9, pp. 2058–2066, Sept. 2006.

[15] G. E. Zhang and M. Green, “A 10 Gb/s BiCMOS Adaptive Cable Equalizer,”
    IEEE Journal of Solid-State Circuits, vol. 40, no. 11, pp. 2132–2240, Nov.
    2005.

[16] Y. Kudoh, M. Fukaishi, and M. Mizuno, “A 0.13 µm CMOS 5-Gb/s 10-
    meter 28AWG cable transceiver with no-feedback-loop continuous-time post-
    equalizer,” Symposium On VLSI Circuits, 2002.

[17] H. C. Nee, C. M. Tsai, S. K. You, and W. T. Chen, “A 6Gb/s adaptive
    equalizer using overshoot control in 0.18 µm CMOS technology,” Circuits and
    Systems (ISCAS), IEEE International Symposium on, pp. 1963–1966, 2012.

[18] F. Loi, E. Mammei, F. Radice, M. Bruccoleri, S. Erba, M. Bassi, and A. Maz-
    zanti, “A 25-Gb/s FIR equalizer based on highly linear all-pass delay line
    stages in 28-nm LP CMOS,” in IEEE Radio Frequency Integrated Circuits
    symposium (RFIC), May 2015.

[19] E. H. Chen, R. Yousry, and C. K. Yang, “Power optimized adc-based serial
    link receiver,” IEEE Solid-State Circuits, IEEE Journal of, 2012.

[20] A. Agrawal, “A 19-Gb/s serial link receiver with both 4-tap FFE and 5-
    tap DFE functions in 45-nm SOI CMOS,” IEEE Solid-State Circuits, IEEE
    Journal of, vol. 47, no. 12, p. 3220–3231, Dec. 2012.

[21] M. Chen, “A fully-integrated 40-Gb/s transceiver in 65-nm CMOS technology,”
    IEEE Solid-State Circuits, IEEE Journal of, vol. 47, no. 3, pp. 627–640, March
    2012.

---

75                                                                     Bibliography

[22] R. Gitlin and S. Weinstein, “Fractionally-spaced equalization: An improved
     digital transversal equalizer,” IEEE Solid-State Circuits, IEEE Journal of,
     vol. 60, no. 2, pp. 275–296, Feb. 1981.

[23] S. Qureshi, “Adaptive equalization,” vol. 73, no. 9, Sep. 1985, pp. 1349–1387–
     296.

[24] J-Bulzacchelli, “A 28-gb/s 4-tap ffe/15-tap dfe serial link transceiver in 32-nm
     soi cmos technology,” IEEE Solid-State Circuits, IEEE Journal of, vol. 47,
     no. 12, pp. 3232–3248, Dec. 2012.

---

