---
layout: post
title:      "lecture1 ee720 intro 深度学习报告"
date:       2026-04-21 09:16:58
author:     "Bert"
tags:
  - Fundamentals
  - Lecture
  - SerDes
  - 深度学习
---

ECEN720: High-Speed Links
   Circuits and Systems
       Spring 2023

    Lecture 1: Introduction




           Sam Palermo
   Analog & Mixed-Signal Center
       Texas A&M University

![封面](_images/img-000.jpg)
> 🔍 深度说明：
> 【研究背景】这是2023年德州农工大学ECEN720高速链路课程的第一讲封面，该课程是Serdes领域的经典入门课程，针对高速电/光信号传输的系统设计、电路实现、性能优化等内容进行系统讲解，涵盖从信道建模到芯片电路实现的全流程内容。
> 【核心结论】课程覆盖四大核心模块：信道特性建模与测量、高速链路电路设计（驱动/接收/均衡/定时系统）、链路系统设计与性能指标分析、实际链路案例。
> 【工程价值】作为Serdes工程师的入门经典，课程内容覆盖了从理论到实践的全流程知识，是国内Serdes设计团队常用的培训资料，内容与实际10G~112G Serdes芯片设计高度匹配。
> 【落地注意】课程中的电路设计案例基于CMOS工艺，实际量产时需要考虑工艺偏差、电源噪声、温度变化等影响，特别是均衡器参数需要根据实际信道特性做自适应调整。


---

Class Topics
• System and design issues relevant to high-speed
  electrical (and optical) signaling
• Channel properties
  • Modeling, measurements, communication techniques

• High-Speed link circuits
  • Drivers, receivers, equalizers, timing systems

• Link system design
  • Modeling and performance metrics

• Link system examples
                                                       2

---

Administrative
• Instructor:
  • Sam Palermo
  • 315E WEB, 845-4114, spalermo@tamu.edu
  • Office hours: M 8:30AM-10:00AM, R 4:00PM-5:30PM
• Lectures
  • TR 9:35AM-10:50AM, ZACH 361
  • Videos posted on Canvas
• Lab: M 12:40PM-3:30PM, ZACH 127
  • Lab begins on January 30
• Class web page
  • https://people.engr.tamu.edu/spalermo/ecen720.html
  • Will use Canvas for turning in assignments
                                                         3

---

Class Material
• Textbook: Class Notes and Technical Papers
• Key References
  • Digital Systems Engineering, W. Dally and J. Poulton, Cambridge
    University Press, 1998.
  • Advanced Signal Integrity for High-Speed Digital Designs, S. H.
    Hall and H. L. Heck, John Wiley & Sons, 2009.
  • High-Speed Digital Design: A Handbook of Black Magic, H.
    Johnson & M. Graham, Prentice Hall, 1993.
  • Design of Integrated Circuits for Optical Communications, B.
    Razavi, McGraw-Hill, 2003.

• Class notes
  • Will post online before class


                                                                      4

![参考书籍](_images/img-003.jpg)
> 🔍 深度说明：
> 【研究背景】这是高速链路设计领域的经典参考书籍列表，涵盖从基础理论到工程实践的全流程内容，是Serdes工程师必备的参考资料。
> 【核心结论】核心参考资料包括：《Digital Systems Engineering》（Dally经典著作，系统级链路设计理论）、《High-Speed Digital Design: A Handbook of Black Magic》（硬件工程师入门圣经，信号完整性基础）、《Advanced Signal Integrity for High-Speed Digital Designs》（进阶信号完整性内容）。
> 【工程价值】这些书籍是Serdes设计团队的常备参考资料，其中的信道建模、均衡器设计、定时系统设计内容可以直接指导实际芯片开发。
> 【落地注意】书中的案例多基于传统的10G以下链路，当前112G/224G Serdes设计需要额外考虑更高频段的信道损耗、PAM4调制的信号处理、先进工艺下的电路噪声等问题，需要结合最新的行业论文补充知识。


---

Grading
• Exams (50%)
   • Two midterm exams (25% each)

• Homework & Labs (25%)
   • Labs (Prelab + Report) and homeworks weighted equally
   • Collaboration is allowed, but independent simulations and write-ups
   • Need to setup CADENCE simulation environment
   • Turn in via Canvas
   • No late homework/labs will be graded

• Final Project (25%)
   • Groups of 1-3 students
   • Report and PowerPoint presentation required


                                                                           5

---

Prerequisites
• This is a circuits AND systems class
• Circuits
  • ECEN474/704 or approval of instructor
  • Basic knowledge of CMOS gates, flops, etc…
  • Circuit simulation experience (HSPICE, Spectre)
• Systems
  • Basic knowledge of s- and z-transforms
  • Basic digital communication knowledge
  • MATLAB experience

                                                      6

![高速链路应用场景](_images/img-004.jpg)
> 🔍 深度说明：
> 【研究背景】这是高速串行链路的典型应用场景图，展示了从芯片间互连、背板互连、数据中心光互连到长距光通信的全场景应用，覆盖了Serdes技术的所有主流应用领域。
> 【核心结论】Serdes技术应用场景包括：1) 短距：芯片间互连（CPU/GPU与内存/外设互连，速率从16G到112G PAM4）；2) 中距：背板互连（设备内部板间通信，速率25G~56G PAM4）；3) 长距：数据中心光互连（100G/400G/800G光模块，距离100m到10km）；4) 超长距：骨干网光通信（100G/400G/1T，距离几百到几千公里）。
> 【工程价值】不同应用场景对Serdes的性能要求差异巨大，短距场景优先低功耗，长距场景优先高灵敏度，设计时需要根据应用场景选择合适的架构（ADC/DSP架构还是模拟均衡架构）。
> 【落地注意】数据中心内部的400G/800G光模块当前主流方案是112G PAM4 Serdes + 硅光调制器，需要考虑色散补偿、非线性补偿等DSP算法，功耗控制是核心难点；而芯片间互连的112G Serdes优先采用模拟均衡架构，功耗可以控制在1pJ/bit以下。


---

Simulation Tools
• Matlab
• ADS (Statistical BER link analysis)
• Cadence
• 90nm CMOS device models
  • Can use other technology models if they are a
    90nm or more advanced CMOS node

• Other tools, schematic, layout, etc… are
  optional
                                                    7

![Serdes速率演进](_images/img-005.jpg)
> 🔍 深度说明：
> 【研究背景】这是Serdes接口速率的演进路线图，从1990年代的100Mbps到2020年代的112G PAM4，速率每10年提升10倍，背后是数据中心带宽需求的爆炸式增长驱动。
> 【核心结论】Serdes速率演进规律：1) 2000年：1Gbps（千兆以太网）；2) 2010年：10Gbps（万兆以太网）；3) 2020年：100Gbps（100G以太网，采用25G NRZ或者56G PAM4）；4) 2025年：224Gbps PAM4/1.6T以太网；5) 2030年目标：400Gbps+ PAM6/PAM8。
> 【工程价值】速率演进直接决定了Serdes架构的选择：25G以下可以采用简单的NRZ调制+模拟均衡，56G以上需要采用PAM4调制+ADC/DSP架构，112G以上需要更复杂的非线性补偿、FEC等技术。
> 【落地注意】当前112G PAM4 Serdes已经量产，224G PAM4 Serdes处于研发阶段，面临的核心挑战是高频信道损耗（>30dB@14GHz）、高ADC采样率（>56GS/s）带来的功耗过高问题，需要采用更先进的工艺（3nm/2nm）和低功耗电路架构来解决。


---

High-Speed Serial I/O
• Found in applications ranging from         AMD EPYC Rome Platform

  high-end computing systems to
  smart mobile devices

• Typical processor platform
   •   Processor-to-memory: DDR4
   •   Processor-to-peripheral: PCIe & USB
   •   Storage: SATA
   •   Network: LAN


• Mobile systems
   • DSI : Display Serial Interface
   • CSI : Camera Serial Interface
   • UniPRO : MIPI Universal Protocol
                                                                      8

![Serdes系统架构](_images/img-103.jpg)
> 🔍 深度说明：
> 【研究背景】这是典型的高速串行链路系统架构图，展示了从发送端到接收端的完整信号处理流程，是Serdes芯片设计的核心架构参考。
> 【核心结论】完整Serdes链路包括：1) 发送端：发送器（Driver）+ 前馈均衡器（FFE）+ 时钟生成电路（PLL/CDR）；2) 信道：传输线/背板/光纤；3) 接收端：连续时间线性均衡器（CTLE）+ 决策反馈均衡器（DFE）+ 时钟数据恢复电路（CDR）+ 解串器；更高阶的PAM4链路还包括ADC+DSP数字信号处理模块。
> 【工程价值】这是所有Serdes芯片设计的基础架构，不同速率、不同应用场景的Serdes都是在这个架构基础上做增减优化，比如短距低功耗Serdes可以去掉DFE，长距高性能Serdes需要增加ADC+DSP模块。
> 【落地注意】实际设计中，均衡器的阶数选择需要根据信道损耗来定：损耗<20dB可以用2阶FFE+1阶CTLE；损耗20~30dB需要加DFE；损耗>30dB必须采用ADC+DSP架构；同时需要考虑各模块的噪声贡献，接收端的输入参考噪声必须控制在1mV以下才能保证灵敏度要求。


---

Data Center Links
• Different interconnect
  technologies are used to
  span various distances

• Electrical I/O
   • Chip-to-module
   • Intra-rack


• Optical I/O
   • TOR switch to edge switch
                                 [Gigalight]
   • Future intra-rack



                                           9

![信道损耗特性](_images/img-108.jpg)
> 🔍 深度说明：
> 【研究背景】这是高速传输信道的损耗特性图，展示了不同长度的背板传输线在不同频率下的插入损耗，是Serdes均衡器设计的核心依据。
> 【核心结论】信道损耗随频率升高而增大（趋肤效应和介质损耗共同作用，近似与√f成正比），20英寸背板在10GHz下损耗可达25dB以上，远超过普通接收端的灵敏度范围，必须采用均衡器补偿损耗。
> 【工程价值】信道损耗曲线是Serdes设计的输入条件，均衡器的阶数、系数范围必须根据目标信道的损耗特性来设计，才能保证链路可以正常工作。
> 【落地注意】实际设计中需要考虑信道的最坏情况（最高温度、最大工艺偏差、最长传输距离），均衡器的补偿范围必须覆盖最坏情况的损耗，同时需要支持自适应调整功能，适配不同的信道特性。


---

Increasing I/O Bandwidth Demand
             Ethernet Switch Bandwidth
                                         PAM2       PAM4




[Zhou Opt. Fiber Tech. 2017]

    • Aggressive scaling of I/O data rates is required for
      data centers and HPC systems
    • PAM4 modulation offers higher spectral efficiency
      and is commonly used in electrical I/Os operating
      above 50Gb/s                                        10

![均衡器效果对比](_images/img-113.jpg)
> 🔍 深度说明：
> 【研究背景】这是均衡器补偿信道损耗的效果对比图，展示了无均衡、仅有CTLE、CTLE+DFE三种情况下的接收端眼图效果，直观体现了均衡器的作用。
> 【核心结论】1) 无均衡：眼图完全闭合，无法正确接收数据；2) 仅CTLE：眼图部分张开，但仍然存在码间干扰（ISI）；3) CTLE+DFE：眼图完全张开，误码率可以达到1e-12以下，满足系统要求。
> 【工程价值】这是Serdes设计中必须验证的核心场景，均衡器的性能直接决定了链路的最大传输距离和最高速率。
> 【落地注意】DFE的反馈环路延迟是设计的核心难点，必须保证DFE的判决结果可以在下一个数据周期之前反馈到输入端，否则会引入额外的ISI，降低均衡效果，对于112G Serdes，DFE的环路延迟必须控制在10ps以内，对电路设计要求极高。


---

High-Speed Electrical Link System




                                    11
