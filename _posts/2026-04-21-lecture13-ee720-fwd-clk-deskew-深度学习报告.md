---
layout: post
title:      "lecture13 ee720 fwd clk deskew 深度学习报告"
date:       2026-04-21 10:25:45
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

Lecture 13: Forwarded Clock Deskew Circuits




                 Sam Palermo
         Analog & Mixed-Signal Center
             Texas A&M University

![课程封面](/img/serdes/fundamentals/lectures/lecture10_ee720_jitter_深度学习报告/_images/img-000.jpg)
> 🔍 深度说明：
> 【研究背景】这是ECEN720第十三讲，主题是前向时钟传输与去偏移技术，主要解决多通道并行传输或者前向时钟串行传输中的时钟偏移问题，保证多通道之间的同步。
> 【核心结论】内容覆盖时钟偏移的来源、前向时钟传输架构、去偏移电路设计、相位校准技术、多通道同步技术，适用于并行高速接口和前向时钟串行接口设计。
> 【工程价值】在多通道并行传输（如DDR、HBM、宽IO）或者前向时钟串行接口（如某些高速背板协议）中，去偏移技术可以保证通道之间的相位偏差小于0.1UI，实现多通道的同步传输，提升系统吞吐量。
> 【落地注意】多通道同步要求所有通道的走线长度差<50mil，对应时间偏差<1ps，PCB设计时需要严格做等长控制，同时加入片上去偏移电路，校准残留的相位偏差，保证同步精度。


---

Announcements
• Project Preliminary Report due today
• Exam 2 Apr 25
  • Focuses on material from Lectures 7-14
  • Previous years’ Exam 2s are posted on the website for
    reference

• Project Final Report due May 2
• Project Presentations May 4 (12:30PM-2:30PM)




                                                            2

![时钟偏移来源](/img/serdes/fundamentals/lectures/lecture1_ee720_intro_深度学习报告/_images/img-001.jpg)
> 🔍 深度说明：
> 【研究背景】前向时钟传输中的时钟偏移来源示意图，时钟和数据经过不同的路径，会产生相位偏差，导致采样错误。
> 【核心结论】时钟偏移的主要来源包括：1) PCB走线长度的差异，导致传输延迟不同；2) 发送端输出延迟的工艺偏差；3) 接收端输入延迟的工艺偏差；4) 温度和电压变化导致的延迟差异；总偏移可以达到几个UI，必须校准才能正常工作。
> 【工程价值】去偏移电路可以自动校准这些相位偏差，不需要人工调整，大大降低系统调试的复杂度，同时可以跟踪温度电压的变化，动态校准，保证系统始终同步。
> 【落地注意】去偏移电路的校准范围需要覆盖最大可能的偏移，一般要求±2UI以上，校准精度<0.05UI，才能保证采样时刻在眼图中心位置。


---

Agenda
• Forwarded Clock I/O Overview
• Data & Clock Skew Performance Impact
• Jitter Impulse Response and Jitter Transfer
  Function
• Forwarded Clock Deskew Architectures
  • PLL/PI
  • DLL/PI
  • ILO
    • Fundamental, Super-Harmonic, Sub-Harmonic

                                                  3

![前向时钟架构](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/img-002.jpg)
> 🔍 深度说明：
> 【研究背景】前向时钟传输架构示意图，时钟和数据一起传输，接收端用传输过来的时钟采样数据，不需要CDR模块，结构简单，功耗低。
> 【核心结论】前向时钟架构的优点是结构简单，不需要复杂的CDR模块，功耗低，成本低；缺点是需要额外的时钟通道，并且需要校准时钟和数据之间的相位偏差，传输距离有限，适合短距板级或者芯片间互连。
> 【工程价值】前向时钟架构非常适合短距高带宽的应用，比如芯片间互连、HBM内存接口、有源光缆等，功耗比带CDR的Serdes低30%以上。
> 【落地注意】前向时钟传输中，时钟路径和数据路径的长度要尽量匹配，偏差<100mil，减少初始的相位偏差，降低校准电路的压力；同时时钟和数据要走相同的物理层，保证温度电压变化时的延迟变化一致。


---

Forwarded Clock I/O Architecture
                  • Common high-speed reference
                    clock is forwarded from TX chip
                    to RX chip
                      • Mesochronous system
                  • Used in processor-memory
                    interfaces and multi-processor
                    communication
                      • Intel QPI
                      • Hypertransport
                  • Requires one extra clock
                    channel
                  • “Coherent” clocking allows low-
                    to-high frequency jitter tracking
                  • Need good clock receive
                    amplifier as the forwarded clock
                    is attenuated by the channel
                                                      4

![去偏移电路](/img/serdes/fundamentals/lectures/lecture1_ee720_intro_深度学习报告/_images/img-003.jpg)
> 🔍 深度说明：
> 【研究背景】典型的去偏移电路架构示意图，通过可调节的延迟线，调整数据或者时钟的延迟，使得时钟采样时刻位于数据眼图的中心位置。
> 【核心结论】去偏移电路主要由可调延迟线、相位检测器、控制逻辑组成，相位检测器比较时钟和数据的相位，控制逻辑调整延迟线的延迟，直到相位对齐，实现自动校准。
> 【工程价值】自动去偏移电路可以在系统上电时自动校准，不需要人工干预，大大降低了量产测试的成本，同时可以在工作过程中动态校准，抵消温度电压变化的影响，保证同步精度。
> 【落地注意】可调延迟线的步长要足够小，一般<1ps，才能达到高的校准精度；同时延迟范围要足够大，覆盖最大的相位偏移，一般要求±2UI以上。


---

Forwarded Clock I/O Limitations
                  • Clock skew can limited forward
                    clock I/O performance
                     • Driver strength and loading
                       mismatches
                     • Interconnect length
                       mismatches


                  • Low pass channel causes jitter
                    amplification

                  • Duty-Cycle variations of
                    forwarded clock




                                                     5

![多通道同步](/img/serdes/fundamentals/lectures/lecture11_ee720_clocking_arch_plls_深度学习报告/_images/img-004.jpg)
> 🔍 深度说明：
> 【研究背景】多通道同步技术示意图，在多通道并行传输中，需要保证所有通道的数据在接收端是对齐的，才能正确恢复出并行数据。
> 【核心结论】多通道同步的方法包括：1) 发送端发送训练序列，接收端检测训练序列的位置，调整每个通道的延迟，使得所有通道的训练序列对齐；2) 采用FIFO缓存，读出侧用统一的时钟读出，实现通道对齐；3) 相位校准，调整每个通道的采样相位，保证每个通道的采样时刻都在眼图中心。
> 【工程价值】多通道同步技术可以实现几十甚至上百个通道的并行传输，总吞吐量可以达到几十Tbps，是高带宽接口的核心技术，广泛应用于HBM、宽IO、高带宽交换机等场景。
> 【落地注意】多通道同步的校准需要定期进行，抵消温度电压变化导致的延迟变化，一般每隔几秒校准一次，或者在温度变化超过5℃时自动校准，保证同步精度。

