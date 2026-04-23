---
layout: post
title:      "lecture6 ee720 rx circuits 深度学习报告"
date:       2026-04-21 09:54:56
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

    Lecture 6: RX Circuits




           Sam Palermo
   Analog & Mixed-Signal Center
       Texas A&M University

![课程封面](_images/img-000.jpg)
> 🔍 深度说明：
> 【研究背景】这是ECEN720第六讲，主题是接收端电路与连续时间线性均衡器（CTLE），是Serdes接收端模拟前端核心模块，直接决定接收灵敏度。
> 【核心结论】内容覆盖接收端架构、LNA设计、CTLE原理、VGA设计、噪声优化，CTLE通过高通特性补偿信道高频损耗，是功耗最低的均衡技术。
> 【工程价值】接收端前端噪声无法被后续电路消除，其性能直接决定Serdes极限灵敏度，CTLE可以补偿0~15dB的高频损耗，降低后续均衡压力。
> 【落地注意】112G Serdes要求CTLE带宽覆盖到28GHz以上，输入参考噪声<500uVrms，增益调节步进<1dB，同时ESD寄生电容必须<100fF避免额外高频损耗。


---

Announcements
• Lab 4 report and Prelab 5 due Mar 6
• Exam 1 Mar 7
  • Covers material through Lecture 6
  • Previous years’ exam 1s are posted on the
    website for reference


• Sampler and comparator papers are posted
  on the website


                                                2

![接收端架构](_images/img-001.jpg)
> 🔍 深度说明：
> 【研究背景】典型Serdes接收端模拟前端架构，从输入端口到采样器的完整路径，是接收端设计的基础框架。
> 【核心结论】架构包括ESD保护、终端匹配电阻、LNA、CTLE、VGA、采样器，不同应用场景可裁剪，短距应用可去掉LNA降低功耗。
> 【工程价值】架构选择直接决定接收端的功耗和性能，长距场景需要高增益低噪声架构，短距场景优先低功耗简化架构。
> 【落地注意】ESD电路寄生参数会严重影响高频性能，112G Serdes的ESD寄生电容必须控制在100fF以内，否则会引入3dB以上的额外高频损耗。


---

Outline
• Receiver parameters
• T-coils at RX examples
• Analog front-end
• Clocked comparators
• Sensitivity & offset correction
• Demultiplexing
• PAM4 RX example
                                    3

![CTLE原理](_images/img-002.jpg)
> 🔍 深度说明：
> 【研究背景】CTLE是连续时间线性均衡器，是最常用的模拟均衡技术，功耗仅为数字均衡的1/10。
> 【核心结论】CTLE本质是高通滤波器，提升高频分量抵消信道低通损耗，通过RC参数调整高频增益和零点位置，适配不同信道。
> 【工程价值】对于损耗<20dB的信道，仅用CTLE就可以让眼图张开，不需要复杂的DFE或者数字均衡，大幅降低功耗。
> 【落地注意】CTLE均衡档位需要支持多档可调，覆盖0~20dB@Nyquist频率范围，同时增益调节时相位变化必须<5°，避免引入额外抖动。


---

High-Speed Electrical Link System




                                    4

![CTLE电路](_images/img-003.jpg)
> 🔍 深度说明：
> 【研究背景】差分对加源极退化RC结构是当前高速Serdes最常用的CTLE电路实现方式，适合纳米CMOS工艺。
> 【核心结论】通过开关调整源极退化的电阻电容值，实现不同的均衡档位，工艺偏差下需要校准保证均衡精度。
> 【工程价值】该结构功耗低、面积小、带宽高，112G Serdes中该结构CTLE功耗仅为2~3mW，远低于数字均衡的功耗。
> 【落地注意】CTLE的RC参数受工艺偏差影响大，必须加入校准电路，自动调整参数抵消PVT变化，保证均衡性能一致性。


---

Receiver Parameters
• RX sensitivity, offsets in voltage and time domain, and
  aperture time are important parameters
• Minimum eye width is determined by aperture time plus
  peak-to-peak timing jitter
• Minimum eye height is determined by sensitivity plus
  peak-to-peak voltage offset




                                        [Dally]

                                                            5

![VGA电路](_images/img-004.jpg)
> 🔍 深度说明：
> 【研究背景】可变增益放大器VGA用于调整接收信号幅度到采样器最佳输入范围，保证判决精度。
> 【核心结论】VGA要求增益调节范围0~20dB，步进1dB，带宽高、线性度好，增益调节时相位变化小。
> 【工程价值】不同信道损耗下接收信号幅度从几十mV到几百mV变化，VGA可以统一调整到采样器最佳输入范围200~500mV，保证判决精度最高。
> 【落地注意】VGA增益调节时相位变化必须<5°，否则会引入额外相位误差，增大CDR抖动，降低链路余量，需要加入相位补偿电路抵消相位变化。

