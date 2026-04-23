---
layout: post
title:      "lecture7 ee720 eq intro txeq 深度学习报告"
date:       2026-04-21 10:00:01
author:     "Bert"
tags:
  - Fundamentals
  - Lecture
  - SerDes
  - TX
  - 深度学习
---

ECEN720: High-Speed Links
          Circuits and Systems
              Spring 2023

Lecture 7: Equalization Introduction & TX FIR Eq




                   Sam Palermo
           Analog & Mixed-Signal Center
               Texas A&M University

![课程封面](/img/serdes/fundamentals/lectures/lecture10_ee720_jitter_深度学习报告/_images/img-000.jpg)
> 🔍 深度说明：
> 【研究背景】这是ECEN720第七讲，主题是均衡器基础与发送端前馈均衡器（FFE）设计，均衡技术是Serdes的核心，没有均衡就无法实现高速传输。
> 【核心结论】内容覆盖均衡技术分类、线性/非线性均衡、FFE原理、FFE电路实现、预加重与去加重、FFE系数优化，是所有均衡技术的基础。
> 【工程价值】FFE是发送端标配的均衡技术，有效补偿信道高频损耗，降低接收端均衡压力，是短距链路的主要均衡方式。
> 【落地注意】FFE系数需要自适应调整适配不同信道，系数过大会导致过冲增大串扰，系数过小补偿不足，实际应用中需要通过训练协议和对端反馈优化系数。


---

Announcements
• Lab 4 Report and Prelab 5 due Mar 10
• Exam 1 Mar 7
  • Covers material through Lecture 6
  • Previous years’ exam 1s are posted on the website for
    reference

• Equalization overview and circuits papers are posted
  on the website




                                                            2

![均衡技术分类](/img/serdes/fundamentals/lectures/lecture1_ee720_intro_深度学习报告/_images/img-001.jpg)
> 🔍 深度说明：
> 【研究背景】均衡技术分类示意图，不同的均衡技术有不同的适用场景，功耗和性能也不同，需要根据应用选择。
> 【核心结论】均衡分为：1) 线性均衡：CTLE、FFE，结构简单功耗低，对噪声和串扰没有抑制作用；2) 非线性均衡：DFE、MLSE，结构复杂功耗高，可以抑制噪声和串扰，性能更好；3) 数字均衡：ADC+DSP，性能最好功耗最高，适合长距高损耗场景。
> 【工程价值】链路均衡方案选择需要平衡性能和功耗，短距低功耗场景优先选择CTLE+FFE，中长距场景加DFE，长距高损耗场景选择ADC+DSP全数字均衡。
> 【落地注意】112G PAM4链路，损耗<20dB选择CTLE+FFE；20~30dB加DFE；>30dB必须用ADC+DSP架构，才能满足误码率要求。


---

Agenda
• Equalization theory and circuits
  • Equalization overview
  • Equalization implementations
     • TX FIR
     • RX FIR
     • RX CTLE
     • RX DFE
• TX FIR Equalization
  • FIR filter in time and frequency domain
  • MMSE Coefficient Selection
  • Circuit Topologies
• Equalization overview paper posted on website
                                                  3

![FFE原理](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/img-002.jpg)
> 🔍 深度说明：
> 【研究背景】前馈均衡器（FFE）原理示意图，FFE是线性均衡的一种，可以在发送端或者接收端实现，发送端实现的FFE也叫预加重/去加重。
> 【核心结论】FFE由延迟线和加权加法器组成，通过对当前符号和相邻符号进行加权相加，抵消信道引入的码间干扰；发送端FFE的原理是对高频跳变沿进行放大，补偿信道的高频衰减。
> 【工程价值】FFE是最简单的均衡技术，功耗低，容易实现，是所有Serdes的标配功能，发送端FFE不需要额外的反馈信息，实现起来最简单。
> 【落地注意】FFE的阶数根据信道的脉冲响应长度决定，一般需要覆盖主要的码间干扰范围，NRZ链路一般2~3 tap，PAM4链路一般6~8 tap，阶数过大会增加功耗和延迟。


---

High-Speed Electrical Link System




                                    4

![预加重与去加重](/img/serdes/fundamentals/lectures/lecture1_ee720_intro_深度学习报告/_images/img-003.jpg)
> 🔍 深度说明：
> 【研究背景】发送端FFE的两种实现方式：预加重和去加重，两者效果相同，实现方式不同，各有优缺点。
> 【核心结论】预加重是放大高频跳变沿的幅度，保持低频电平不变，输出摆幅大；去加重是衰减低频电平的幅度，保持高频跳变沿不变，输出摆幅小，功耗更低，是当前主流的实现方式。
> 【工程价值】去加重的输出摆幅小，功耗更低，同时EMI性能更好，是当前发送端FFE的主流实现方式，112G Serdes都采用去加重实现发送端FFE。
> 【落地注意】去加重的系数需要根据链路长度调整，长距链路需要更大的去加重系数，短距链路系数要小，避免过冲太大导致串扰增大；实际应用中支持自适应调整系数。


---

Link with Equalization




                         Deserializer
   Serializer




                                        5

![FFE电路实现](/img/serdes/fundamentals/lectures/lecture11_ee720_clocking_arch_plls_深度学习报告/_images/img-004.jpg)
> 🔍 深度说明：
> 【研究背景】发送端FFE的电路实现示意图，采用电流模式驱动器实现，通过控制不同tap的电流权重实现FFE系数调整。
> 【核心结论】每个tap对应一个电流驱动阵列，通过开关控制导通的电流单元数量，调整该tap的权重，实现不同的FFE系数；一般支持正/负系数，系数精度6~8bit。
> 【工程价值】该结构的FFE可以和发送端驱动器集成在一起，不需要额外的电路，面积小，功耗低，适合高速Serdes实现。
> 【落地注意】FFE的电流单元需要良好的匹配，保证系数精度，否则会导致均衡性能下降；同时需要校准电路抵消工艺偏差带来的权重误差，保证不同芯片之间的性能一致性。

