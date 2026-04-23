---
layout: post
title:      "OnChip Signaling HighSpeed SerDes Transceivers NagyTadros 119p 中文版"
date:       2026-04-21 20:37:38
author:     "Bert"
tags:
  - SerDes
  - Thesis
---

开罗美国大学
AUC知识泉

论文与学位论文                                                                     学生研究


2-1-2015

芯片信号传输技术与高速SerDes（串行器/并行器）收发器
Ramy Nagy Tadros




更多作品请访问： https://fount.aucegypt.edu/etds


引用推荐


APA Citation
Tadros, R. (2015).芯片信号传输技术与高速SerDes（串行器/并行器）收发器 [Master's Thesis, the
开罗美国大学]. AUC知识泉.
https://fount.aucegypt.edu/etds/1245
MLA Citation
Tadros, Ramy Nagy. 芯片信号传输技术与高速SerDes（串行器/并行器）收发器. 2015. American
University in Cairo, Master's Thesis. AUC知识泉.
https://fount.aucegypt.edu/etds/1245


This material is brought to by AUC知识泉 (FOUNT). For more information, please visit
https://fount.aucegypt.edu/about.html. If you have questions or concerns, please contact
fountadmin@aucegypt.edu.
    The 开罗美国大学
        科学与工程学院




芯片信号传输技术用于
高速SerDes（串行器/并行器）收发器


               论文提交至
    电子工程系
    部分满足要求以获得
         理学硕士学位




                         By
                Ramy N. Tadros
                        2014
                         The 开罗美国大学
                            科学与工程学院

                         芯片信号传输技术用于
                          高速SerDes（串行器/并行器）收发器

                                    A Thesis Submitted By
                                       Ramy N. Tadros

                                            Submitted to
                           电子工程系
                          部分满足要求以获得
                                理学硕士学位


_______________________________________                             ___________________
Dr. Yehea Ismail                                                    Date
论文导师
Professor at the 开罗美国大学
纳米电子学与器件中心（CND）总监

_______________________________________                             ___________________
Dr. Maged Ghoneima                                                  Date
论文联合导师
Assistant Professor at the 开罗美国大学

_______________________________________                             ___________________
Dr. Mohab Anis                                                      Date
Associate Professor at the 开罗美国大学

_______________________________________                             ___________________
Dr.Mohamed Dessouky                                                 Date
Professor at Ain Shams University

_______________________________________                             ___________________
Dr. Karim Seddik                                                    Date
Assistant Professor at the 开罗美国大学
电子工程系毕业主管


                                                   i
   © 2014
Ramy N. Tadros




        ii
献给我的家人




       iii
                                  致谢

     First, I would express my gratitude to my professor Yehea Ismail for giving me the
opportunity to work in such professional research environment and benefit from his world class
experience.

     I would like to thank my co-advisor Dr.Maged Ghoneima for his careful guidance, precious
advice, and inspiring mentoring.

     Special gratitude to my colleague Abdelrahman H. Elsayed. We worked as one team for
almost 2 years and every success should be shared with him.

     I would like to thank Sally Safwat and Ezzeldin O. Hussein for their initial push and their time
whenever I needed their help.

     I want to thank all the CND family: the helpful faculty, the always there administration, and
of course, very sincere thanks to every researcher in CND for making the students’ lab as a second
home for me.

     Special thanks to Dr.Eslam yehea, eng.Mohamed Enany, and Hoda Hesham for their
contributions in the tape-outs.

     I want to thank my priceless family and dear friends for supporting me in the past 2 years.
This degree would have never been completed without their sincere love.




                                                    iv
                                                 目录


致谢 .....................................................................................................................iv

目录........................................................................................................................v

表格列表 ................................................................................................................................ ix

图列表 ............................................................................................................................... x

缩写列表 ................................................................................................................ xv

摘要 ..................................................................................................................................... xvi

1 INTRODUCTION ............................................................................................................................ 1

   1.1 并行化 ............................................................................................................................ 1

   1.2 核间网络 ............................................................................................................. 4

   1.3 本论文 ............................................................................................................................ 6

2 SIGNALING AND INTERCONNECTS BACKGROUND ...................................................................... 7

   2.1 偏斜与抖动 ..................................................................................................................... 7

   2.2 芯片上通信 ...................................................................................................... 8

   2.3 互连........................................................................................................................ 9

   2.4 线路端接 ................................................................................................................ 13

3 文献综述 .................................................................................................................. 16

   3.1 传统实现方案 ........................................................................................ 16

       3.1.1 整体系统概述 ...................................................................................... 16

       3.1.2 发射器 .......................................................................................................... 17

       3.1.3 互连 ......................................................................................................... 18

       3.1.4 接收器................................................................................................................ 18

       3.1.5 小结 ..................................................................................................................... 19


                                                                            v
   3.2 起点 ............................................................................................................... 20

       3.2.1 整体系统概述 ...................................................................................... 20

       3.2.2 信号传输技术 ............................................................................................. 21

       3.2.3 互连 ......................................................................................................... 23

       3.2.4 发射器 .......................................................................................................... 23

       3.2.5 接收器................................................................................................................ 25

       3.2.6 小结 ..................................................................................................................... 25

   3.3 最快链路 .................................................................................................................. 27

4 第一个设计 ............................................................................................................................. 29

   4.1 整体系统概述 ............................................................................................. 29

       4.1.1 系统’s 架构 ................................................................................................. 30

       4.1.2 信号传输技术 ............................................................................................. 30

       4.1.3 互连 ......................................................................................................... 32

       4.1.4 测试平台 ............................................................................................................ 32

   4.2 收发器 .................................................................................................................. 33

       4.2.1 发射器 .......................................................................................................... 33

           4.2.1.1 串行器 ....................................................................................................... 34

           4.2.1.2 时钟分频器 ................................................................................................. 36

           4.2.1.3 编码器和驱动器电路 ........................................................................... 36

       4.2.2 接收器................................................................................................................ 39

           4.2.2.1 解码器 ........................................................................................................ 40

           4.2.2.2 并行器 ................................................................................................... 42

       4.2.3 仿真结果....................................................................................................... 44

   4.3 流片 ...................................................................................................................... 46



                                                                          vi
       4.3.1 设计移植 ............................................................................................................. 47

           4.3.1.1 工作频率 ...................................................................................... 47

           4.3.1.2 所做的更改 .............................................................................................. 48

       4.3.2 版图................................................................................................................... 49

           4.3.2.1 发射器 ................................................................................................... 49

           4.3.2.2 互连 ................................................................................................. 51

           4.3.2.3 接收器 ........................................................................................................ 51

       4.3.3 测试与集成 ............................................................................................... 54

           4.3.3.1 测试电路 .................................................................................................. 54

           4.3.3.2 The Testing layout ............................................................................................... 55

           4.3.3.3 芯片集成................................................................................................... 55

       4.3.4 后端版图仿真 .............................................................................................. 57

   4.4 设计总结 ................................................................................................................. 62

5 第二个设计 ............................................................................................................................ 65

   5.1 整体系统概述 ............................................................................................. 65

       5.1.1 系统’s 架构 ................................................................................................. 66

       5.1.2 信号传输技术 ............................................................................................. 66

       5.1.3 互连 ......................................................................................................... 69

   5.2 收发器 .................................................................................................................. 69

       5.2.1 发射器 .......................................................................................................... 70

           5.2.1.1 串行器 ....................................................................................................... 70

           5.2.1.2 时钟分频器 ................................................................................................. 70

           5.2.1.3 编码器和驱动器电路 ........................................................................... 71

       5.2.2 接收器................................................................................................................ 74



                                                                          vii
           5.2.2.1 解码器 ........................................................................................................ 75

           5.2.2.2 并行器 ................................................................................................... 75

       5.2.3 仿真结果....................................................................................................... 75

   5.3 流片 ...................................................................................................................... 77

       5.3.1 设计移植 ............................................................................................................. 77

           5.3.1.1 工作频率 ...................................................................................... 77

           5.3.1.2 The Changes Made .............................................................................................. 78

       5.3.2 版图................................................................................................................... 79

           5.3.2.1 发射器 ................................................................................................... 79

           5.3.2.2 互连 ................................................................................................. 81

           5.3.2.1 接收器 ........................................................................................................ 81

       5.3.3 测试与集成 ............................................................................................... 84

       5.3.4 后端版图仿真 .............................................................................................. 86

   5.4 设计总结 ................................................................................................................. 90

6 小结 .................................................................................................................................... 93

   6.1 小结............................................................................................................................. 93

   6.2 比较 ........................................................................................................................ 95

   6.3 结论 .......................................................................................................................... 97

   6.4 未来工作 ....................................................................................................................... 98

参考文献 .................................................................................................................................... 99




                                                                           viii
                                                      表格列表

表 1.1 Effects of technology scaling-by-‘s’ in long channel and deep sub-micron technologies
             ........................................................................................................................................ 3

表 1.2 比较 between using parallel or serial communication for the on-chip inter-core
             network .......................................................................................................................... 5

表 4.1 The detailed power consumption distribution at 15.5 Gbps ........................................ 44

表 4.2 The results summary of the design in this chapter in 台湾半导体制造公司（TSMC） 65nm CMOS technology 45
表 4.3 The area distribution of the different parts of the design ............................................ 60
表 4.4 The post layout results summary of the design in 联华电子股份有限公司（UMC） 0.13μm CMOS ...................... 61

表 4.5 The results summary of the first design........................................................................ 64

表 5.1 The results summary of the design in this chapter in 全球晶圆代工厂（GF） 65nm CMOS technology ..... 77
表 5.2 The area distribution of the different parts of the design ............................................ 88

表 5.3 The post layout results summary of the design in 低功耗（LP） 全球晶圆代工厂（GF） 65nm CMOS ......................... 89

表 5.4 The results summary of the second design .................................................................. 92

表 6.1 The comparison summary between the designs in this work and other designs ........ 96




                                                                            ix
                                                    图列表

图 1.1 © [1] Moore's law. “The complexity for minimum component costs has increased at a
             rate of roughly a factor of two per year (see graph). Certainly over the short term this
             rate can be expected to continue, if not to increase.” .................................................. 1

图 1.2 © [2] An extrapolated version of Moore’s law with associated real implemented
             processors chips. ........................................................................................................... 2

图 1.3 © [3] The processors clock frequencies versus time. It should be noted how the
             frequencies began to decrease after the power wall in the deep sub-micron
             technologies. ................................................................................................................. 3

图 1.4 © [4] Better performance can be obtained using a number of cores........................... 4

图 1.5 © [5] Gate and interconnect delay versus feature size, showing the reverse scaling
             phenomenon................................................................................................................. 5

图 2.1 © [8]. The clock jitter is the range of uncertainty in the timing of the clock edge. ...... 7

图 2.2 © [8]. The eye diagram is an excellent way to present skew jitter since several
             characteristics of the eye pattern indicate the quality of a signal ............................... 8

图 2.3 The different types of on-chip communication [9]: (a) conventional parallel link, (b)
             serial link with mesochronous clocking, and (c) serial link with plesiochronous
             clocking. ........................................................................................................................ 9

图 2.4 The on-chip interconnect model as a lossy transmission line ..................................... 10

图 2.5 The attenuation and the propagation speed of a signal through a TL across frequency
             ..................................................................................................................................... 11

图 2.6 The magnitude of the characteristic impedance of the TL across frequency ............. 12

图 2.7 © [10] Step response of a capacitively terminated TL ............................................... 14

图 2.8 © [11] (a) The attenuation, and (b) the propagation speed, of the TL terminated with
             a resistor with the optimum value to eliminate 符号间干扰（ISI）. ................................................... 15




                                                                           x
图 2.9 © [11] Transient analysis of a random bit-stream for resistive and capacitive
              terminations................................................................................................................ 15

图 3.1 © [12] The block diagram of the whole SerDes（串行器/并行器） system .............................................. 17

图 3.2 © [12] The block diagram of the transmitter .............................................................. 17

图 3.3 © [12] The block diagram of the receiver ................................................................... 18

图 3.4 © [13] The block diagram of the whole system .......................................................... 21

图 3.5 The 三电平 signaling technique proposed in [15] and used in both [13] and this thesis’s
              first design presented in chapter 4 ............................................................................. 21

图 3.6 The power spectrum of a random bit stream using (a) the conventional 两电平 scheme
              at 24 Gbps, (b) the scheme in 图 3.5 at 12 Gbps ................................................. 22

图 3.7 The interconnect used and its characteristics ............................................................. 23

图 3.8 © [13] The encoder and driver circuit ......................................................................... 24

图 3.9 © [7] The top level block diagram of the phase detector ........................................... 25

图 3.10 © [13] The detailed circuit diagram of the phase detector ...................................... 26

图 3.11 © [14] The block diagram of the whole system ........................................................ 28

图 4.1 The block diagram of the whole system ...................................................................... 31

图 4.2 The 三电平 signaling technique proposed in [15] and used in both [13] and the design
              in this chapter ............................................................................................................. 31

图 4.3 The interconnect used in this design and its characteristics ....................................... 32

图 4.4 The test bench used to test the functionality of the transceiver ................................ 32

图 4.5 Illustration of SPICE model for a single π section of the TL ......................................... 34

图 4.6 The block diagram of the serializer. The ‘DET触发器（FF）’ is a Double-Edge Triggered 触发器,
              and its architecture is in 图 4.7. The subscript ‘TYP’ refers to typical threshold
              transistors, and ‘LVT’ to low threshold transistors ..................................................... 35

图 4.7 The block diagram of the ‘DET触发器（FF）’ used in 图 4.6................................................... 35




                                                                        xi
图 4.8 The block diagram of the clock divider’s part generating the four phases of clk/2 .... 36

图 4.9 The block diagram of the edge matching circuit used in the clock divider in 图 4.8
               ..................................................................................................................................... 37

图 4.10 The block diagram of the designed encoder and driver circuit ................................. 38

图 4.11 发射器 front end components -the inverters and multiplexers- are implemented
               using 传输门（TG）s ..................................................................................................................... 39

图 4.12 The block diagram of the decoder ............................................................................. 40

图 4.13 The phase detector detailed circuit with sizing methodology .................................. 41

图 4.14 The block diagram of the deserializer........................................................................ 43

图 4.15 The waveforms of the key signals of the encoder and driver circuit (see 图 4.10)
               ..................................................................................................................................... 45

图 4.16 The waveforms of the signals of the decoder circuit (see 图 4.12) .................... 46

图 4.17 The eye diagrams of the 三电平 signals at the front-end of both the 发射器（TX） and 接收器（RX）, and
               the extracted data and clock signals........................................................................... 47

图 4.18 The TL charactertics of the interconnect used in 联华电子股份有限公司（UMC） 0.13μm ................................ 48

图 4.19 The layout of the serializer ........................................................................................ 49

图 4.20 The layout of the clock divider................................................................................... 50

图 4.21 The layout of the encoder and driver circuit ............................................................. 50

图 4.22 The layout of the transmitter .................................................................................... 51

图 4.23 The layout of the interconnect .................................................................................. 52

图 4.24 The layout of the deserializer .................................................................................... 52

图 4.25 The layout of the decoder ......................................................................................... 53

图 4.26 The layout of the receiver .......................................................................................... 54

图 4.27 The block diagram of the chip testing methodology ................................................. 56

图 4.28 The layout of the 数控振荡器（DCO）................................................................................................ 56



                                                                            xii
图 4.29 The layout of the digital testing circuitry ................................................................... 57

图 4.30 The block diagram of the full system integrated ....................................................... 58

图 4.31 The layout of the full system integrated ................................................................... 59

图 4.32 The post layout simulated waveforms of the signals in the decoder circuit (see
              图 4.12) ................................................................................................................. 60

图 4.33 The post layout simulated waveforms of the signals in the encoder and driver circuit
              (see 图 4.10).......................................................................................................... 61

图 4.34 The post layout eye diagrams of the 三电平 signals at the front-end of both the 发射器（TX）
              and 接收器（RX）, and the extracted data and clock signals ...................................................... 62

图 5.1 The block diagram of the whole SerDes（串行器/并行器） system .......................................................... 67

图 5.2 The new 三电平 signaling scheme presente in this design .......................................... 68

图 5.3 The power spectrum of a random bit stream using (a) the conventional 两电平 scheme
              at 24 Gbps, (b) the scheme presented in [15] at 12 Gbps, and (c) the proposed scheme
              at 24 Gbps. .................................................................................................................. 69

图 5.4 The used interconnect characteristics ......................................................................... 70

图 5.5 The block diagram of the two-stage serializer ............................................................ 71

图 5.6 The block diagram of the divide-by-two unit used in the clock divider ...................... 72

图 5.7 The block diagram of the encoder and driver circuit .................................................. 73

图 5.8 The architecture of the special multiplexers used in the encoder and driver in 图 5.7
              ..................................................................................................................................... 74

图 5.9 The proposed architecture of the 三电平 inverter used in 图 5.7......................... 74

图 5.10 The block diagram of the decoder ............................................................................. 75

图 5.11 仿真 results for the key-signals in the encoder and driver in 图 5.7, in order:
              signal ‘1’: the 数据 −, the auxiliary signals ‘2’ and ‘3’, the clock, and the multiplexer
              output. ........................................................................................................................ 76




                                                                           xiii
图 5.12 The 仿真 results for the signals in the decoder shown in 图 5.10, in order:
               The ‘A’ 信号 arriving at the 接收器（RX） front-end, the output of the low threshold and high
               threshold inverters L1, and H1, signals N1 and N2, then finally the extracted clock and
               data signals. ................................................................................................................ 78

图 5.13 The used interconnect and its characteristics ........................................................... 79

图 5.14 The layout of the serializer ........................................................................................ 80

图 5.15 The layout of the clock divider................................................................................... 80

图 5.16 The layout of the encoder and driver circuit ............................................................. 81

图 5.17 The layout of the transmitter .................................................................................... 82

图 5.18 The layout of the interconnect .................................................................................. 83

图 5.19 The layout of the deserializer .................................................................................... 82

图 5.20 The layout of the decoder ......................................................................................... 83

图 5.21 The layout of the receiver .......................................................................................... 84

图 5.22 The layout of the 数控振荡器（DCO）................................................................................................ 85

图 5.23 The layout of the digital testing circuitry ................................................................... 85

图 5.24 The block diagram of the full system integrated ....................................................... 86

图 5.25 The layout of the full system integrated ................................................................... 87

图 5.26 The post layout simulated waveforms of the key-signals in the encoder and driver in
               图 5.7, in order: signal ‘1’: the 数据 −, the auxiliary signals ‘2’ and ‘3’, the clock,
               and the multiplexer output......................................................................................... 88

图 5.27 The post layout simulated waveforms of the signals in the decoder shown in
               图 5.10, in order: The ‘A’ 信号 arriving at the 接收器（RX） front-end, the output of the low
               threshold and high threshold inverters L1, and H1, signals N1 and N2, then finally the
               extracted clock and data signals. ................................................................................ 89

图 5.28 The post eye diagrams of the 三电平 signals (A) at the front-end of both the 发射器（TX） and
               接收器（RX）, and the extracted data and clock signals. ............................................................ 90



                                                                         xiv
                  缩写列表

             Serialization and
SerDes（串行器/并行器）                                    片上网络（NoC）       片上网络
              Deserialization

 比特误码率（BER）          比特 Error Rate              下拉网络（PDN）      Pull-down Network

 时钟数据恢复（CDR）     时钟 and 数据 Recovery          锁相环（PLL）     Phase Locked Loops

            Digitally Controlled
 数控振荡器（DCO）                                      上拉网络（PUN）       Pull-up Network
                 Oscillator
                                                  Process, 电源, and
  触发器（FF）             Flip Flop                工艺、电源与温度（PVT）
                                                     Temperature

 四倍扇出（FO4）         Fan-out-of-four               接收器（RX）           接收器

 全球晶圆代工厂（GF）          Global Foundries              传输门（TG）      Transmission Gate

                                                 Taiwan Semiconductor
 符号间干扰（ISI）     Inter-symbol Interference        台湾半导体制造公司（TSMC）
                                                 manufacturing company

  低功耗（LP）            Low power                  发射器（TX）         发射器

                                                 United Microelectronics
多路复用器（MUX）            多路复用器                联华电子股份有限公司（UMC）
                                                      Corporation




                                     xv
                                           摘要

     The general goal of the VLSI technology is to produce very fast chips with very low power
consumption. The technology scaling along with increasing the working frequency had been the
perfect solution, which enabled the evolution of electronic devices in the 20th century. However,
in deep sub-micron technologies, the on-chip power density limited the continuous increment in
frequency, which led to another trend for designing higher performance chips without increasing
the working speed. 并行化是最佳解决方案, and the VLSI manufacturers began the
era of multi-core chips.

     These multi-core chips require a full inter-core network for the required communication.
These on-chip links were conventionally parallel. However, due to reverse scaling in modern
technologies, parallel signaling is becoming a burden due to the very large area of needed
interconnects. Also, due to the very high power due to the tremendous number of repeaters, in
addition to cross talk issues. As a solution, on-chip serial communication was suggested. It will
solve all the previous issues, but it will require very high speed circuits to achieve the same data
rates.

     本论文提出了两个完整的SerDes（串行器/并行器）收发器设计 for on-chip high speed serial
communication. 两个设计都使用带有电容端接的长损耗芯片上差分互连 with capacitive
termination.

         第一个设计使用三电平自定时信号传输技术. This signaling technique is
totally jitter-insensitive, since both of the data and clock are extracted at the receiver from the
same signal. 设计了一种新的编码和驱动技术 to enable the transmitter to work
at a frequency equal to the data rate, which is half of the frequency of the previous designs, along
with achieving the same data rate. Also, this design generates the third voltage level without the
need of an external supply. 该设计对任何可能的变化都非常容忍, such as 工艺、电源与温度（PVT）
variations or the input clock’s duty cycle variations. This transceiver is prepared for tape-out in
联华电子股份有限公司（UMC） 0.13μm CMOS technology in June 2014.




                                                    xvi
     第二个设计使用一种新的三电平信号传输技术; the proposed technique uses a
frequency of only half the data rate, which totally relaxes the full transceiver design. The new
technique is also self-timed enabling the extraction of both the data, and the clock from the same
signal. 设计了新的编码器和解码器, and a new architecture for a 三电平 inverter is
presented. 该收发器实现了非常高的数据率. This new design is expected to be
taped-out using the 全球晶圆代工厂（GF） 65nm CMOS technology in August 2014.




                                                  xvii
                                        1 INTRODUCTION

1.1 并行化
      Processors are the core component for computers, personal mobile devices, and other
electronic devices and applications. The processor performance is a direct indicator of the
performance, and quality of all these products. Since anyone wants a faster computer, the speed
of any device is one of the most important performance metrics, along with the battery duration,
which reflects the effect of the power consumption metric.

      Therefore, the general goal of the VLSI technology is to produce very fast chips with very
low power consumption. This goal was achieved during the 20th century by ‘technology scaling’
following Moore’s law [1] as shown in 图 1.1. Moore wrote: “The complexity for minimum
component costs has increased at a rate of roughly a factor of two per year (see graph). Certainly
over the short term this rate can be expected to continue, if not to increase.” An extrapolated
version of Moore’s law is shown in 图 1.2, it also indicates the main processor chips fabricated
through VLSI history and the real values of implemented transistors count.




图 1.1 © [1] Moore's law. “The complexity for minimum component costs has increased at a rate of roughly a
factor of two per year (see graph). Certainly over the short term this rate can be expected to continue, if not to
increase.”



                                                           1
  图 1.2 © [2] An extrapolated version of Moore’s law with associated real implemented processors chips.

     The ‘technology scaling’, or scaling the transistor’s length ‘L’ by ‘s’, had the effects
summarized in 表 1.1. First, in long channels, the current scales down with the technology.
Also, the minimum capacitance scales down, which leads to the scaling of delay, and hence, an
improvement in speed. The power per device scales down quadratically as a result. And since the
number of devices per area increases quadratically, the power density doesn’t vary. However, as
shown in 表 1.1, technology scaling has different effects on deep sub-micron channels, since
the current does not scale with the channel length. Therefore, the power per device scales down
linearly due to the capacitance scaling only, which leads to the increase in power density.
Increasing the frequency, while ignoring the power density increment causes serious heat
generation problems in processor chips. This explains why large processors companies start to
decrease the clock frequencies used in their chips in the past few years as depicted in 图 1.3
, this is known by ‘the power wall’.



                                                         2
      Increasing the number of processor cores on the same chip has become the optimum
solution for processor manufacturers in order to achieve higher performance. Since the
implementation of a better single core became a tough challenge, better performance can be
obtained using a number of slower cores as shown in 图 1.4.

         表 1.1 Effects of technology scaling-by-‘s’ in long channel and deep sub-micron technologies


                                                                     After ( l = L/s )
                                           Before
                                           (l=L)                                   Deep
                                                         Long Channels
                                                                                Sub-Micron

                        电流              𝐼𝐷                𝐼𝐷 /𝑠                     𝐼𝐷

                     电容            𝐶𝑚𝑖𝑛              𝐶𝑚𝑖𝑛 /𝑠             𝐶𝑚𝑖𝑛 /𝑠

                      频率               𝑓                𝑓∗𝑠                  𝑓∗𝑠

                    Power/ Device             𝑃                𝑃/𝑠 2                𝑃/𝑠
                        No. of
                     Devices/Area
                                              𝑁               𝑁 ∗ 𝑠2               𝑁 ∗ 𝑠2

                    Power Density            𝑃𝑑                 𝑃𝑑                 𝑃𝑑 ∗ 𝑠




图 1.3 © [3] The processors clock frequencies versus time. It should be noted how the frequencies began to
decrease after the power wall in the deep sub-micron technologies.




                                                          3
                图 1.4 © [4] Better performance can be obtained using a number of cores.


1.2 核间网络
     As discussed in the previous section, the trend now in the VLSI industry is the increase of
the number of cores, and the industry is changing from the present multi-core chips to future
many-core chips. Consequently, a new problem has emerged, which is the need of a robust full
inter-core network on-chip. This thesis mainly discusses the physical layer of this inter-core
communication on chip.

     The first design decision is the choice between serial and parallel communication. Parallel
communication may seem simpler, because the simplicity of its design compared to serial
communication from the point of view of frequency. For example, if the system clock is 2 GHz,
and the desired bitrate is 64*2 Gbps for modern 64-bit processors, then the needed line bitrate
for a parallel design will equal 2 Gbps. However, for a serial design, the line bitrate will equal 128
Gbps on a single line. Moreover, parallel communication is more compatible, since all the
operations inside the core are parallel using parallel buses. However, parallel communication has
a serious limitation, which is the power and area overhead. This issue increases in severity with
the technology scaling, because interconnects are not scaling with the same rate as devices. This
phenomenon is called ‘reverse scaling’ as shown in 图 1.5. When the channel length
decreases, the gate delay decreases, but the interconnect delay increases [5]. Therefore, the
relative area and power overhead of the line interconnects for parallel communication increases,


                                                        4
relative to devices. Also, it should be noted, that 64 lines are needed to communicate between
each two cores, and this will be a very large area for a full network on chip. The power for the
large number of repeaters, due to large number of lines, is another disadvantage for parallel
communication. Moreover, there is the cross-talk issue between the different bit lines. These
problems become more severe as the technology scales down, and thus, on-chip serial
communication becomes an adeqaute solution to solve all these issues. 表 1.2 summarizes
the comparison between using parallel or serial communication for the on-chip inter-core
network.




   图 1.5 © [5] Gate and interconnect delay versus feature size, showing the reverse scaling phenomenon.

    表 1.2 比较 between using parallel or serial communication for the on-chip inter-core network


                                                 Parallel                            Serial

                 Area                 very large (reverse scaling)              much smaller

                                            very high
                Power                                                                 less
                               (large number of lines and repeaters)

              Cross Talk                          exists                         doesn’t exist

              频率                            low                             very high




                                                           5
1.3 本论文
     As previously described, the main objective of this work is to implement a full system
achieving on-chip serial communication between two distant cores. The scope is the physical
layer of this communication link, which means the transmitter, the receiver, and the interconnect
link between them. The design of a robust transceiver able to send binary data at a high speed
consuming low power is the ultimate objective.

     The needed background is discussed in chapter 2, it contains some signaling basics and the
on-chip interconnects characteristics. 章 3 reviews the previous publications, and designs
related to this work. It should be noted that this work is part of an already running project at the
Center of Nanoelectronics and Devices (CND). The work in [6] and [7] are the starting point for
this thesis’s work. 章 3 describes all the previous work.

     章 4 presents the first designed SerDes（串行器/并行器） system. It uses a 三电平 self-timed signaling
scheme. Its main advantage is the variation tolerance of the proposed driving technique. This
transceiver design, and simulation results were published in the 2014 IEEE International
Symposium on 电路s and 系统s (ISCAS 2014). This transceiver was laid out to be taped-out
using the 联华电子股份有限公司（UMC） 0.13μm CMOS technology in June 2014. When the chip will return in August 2014
as expected, this transceiver results will be summarized in a journal paper.

     章 5 presents the second designed SerDes（串行器/并行器） system. A new 三电平 self-timed signaling
scheme is proposed. This is a symbol based scheme as it will be explained. This transceiver’s main
advantage is the very high data rate achieved (20% faster than the fastest reported on-chip serial
transceiver). The design and simulation results will be sent to the next relevant conference. This
transceiver was laid out to be taped-out using the 全球晶圆代工厂（GF） 65nm CMOS technology in August 2014.
When the chip will return in September 2014 as expected, this transceiver results will be
summarized in a journal paper.

Finally, the summary, conclusions, and future work are discussed in chapter 6.




                                                    6
           2 SIGNALING AND INTERCONNECTS BACKGROUND

2.1 偏斜与抖动
      In modern technologies, and due to the very high working frequency, signals rise and fall
times, and pulses widths are getting much shorter, and hence, any slight variation in the edges
of the clock may cause some timing errors. This what made the skew and jitter very serious
problems in nowadays signaling [8].

      Skew is defined as “the magnitude of the time difference between two events that ideally
would occur simultaneously”. And jitter is “the time deviation of a controlled edge from its
nominal position” [8] as illustrated clearly in 图 2.1. In other words, the clock jitter is the range
of uncertainty in the timing of the clock edge, which is disastrous for signal detection in serial
receivers since it may destroy the synchronicity between the two terminals of the serial
transceiver. This is why the clock skew is the most severe limitation for the use of serial
communication on chip to achieve very high data rates, which will be explained in next section.

      The eye diagram measurement is an excellent way to present the clock jitter, since several
characteristics of the eye pattern indicate the quality of the signal as illustrated in 图 2.2. Also
the opening of the eye is a good indication of the quality of the transmission signaling.




           图 2.1 © [8]. The clock jitter is the range of uncertainty in the timing of the clock edge.




                                                             7
图 2.2 © [8]. The eye diagram is an excellent way to present skew jitter since several characteristics of the eye
pattern indicate the quality of a signal

2.2 芯片上通信
      图 2.3 shows the different types of on-chip communication. First, the conventional
parallel link is depicted in 图 2.3 (a). The parallel links usually contain several buffer repeaters.
It should be noted that the line delay should be smaller than the clock period to guarantee a
synchronized detection at the receiver. 图 2.3 (b) shows the serial links with mesochronous
clocking, where both the data and the clock are transmitted. The 发射器（TX） and 接收器（RX） clocks are the same
clock from the same source but with an unknown skew. A circuit is needed at the 接收器（RX） to adjust
this phase shift and synchronize the data and clock signals. Such circuits are power and area
hungry blocks. 图 2.3 (c) depicts the serial links with plesiochronous clocking, where the
clocks at the 发射器（TX） and 接收器（RX） are different. This method is simpler regarding the clock routing, however,
this induces a frequency mismatch in addition to the phase mismatch. Some circuitry is needed
at the 接收器（RX） to synchronize both clocks, this circuitry is power and area hungry also [9].

      So, the main challenge of the serial on-chip communication is the detection. This is due to
the mismatch between the transmitted data signal and the clock at the 接收器（RX）. Solving this issue by
heavy circuitry such as 时钟数据恢复（CDR） or 锁相环（PLL） is totally unacceptable, because the main objective, as



                                                             8
discussed in section 1.2, is to design a transceiver for inter-core network for multi-core chips.
Therefore, the designed module should be repeated for each core. So, if the area and power are
very large, this is not a solution.

      In this thesis, some approaches in literature are discussed in chapter 3, and then the
designed and proposed approaches are detailed in chapter 4 and 5. This work solves the solution
by signaling techniques that are based on embedding both the data and clock in the same signal.
When this signal is detected, the 接收器（RX） extracts both the data and the clock from the same signal,
which by definition, since it is the same single or differential signal, will have no skew whatsoever.
That is why the designs in this work are jitter insensitive, not because they solve the jitter issue,
but because there is no generated skew in the first place, and hence the jitter will have no effects
on the receiver circuits.




                                       发射器（TX）                              接收器（RX）



                                                      (a)

                               数据
                                                                            数据
                    发射器（TX）                      接收器（RX）                   发射器（TX）                      接收器（RX）
                               时钟

                                                                Clk1                     Clk2
                                (b)                                          (c)

图 2.3 The different types of on-chip communication [9]: (a) conventional parallel link, (b) serial link with
mesochronous clocking, and (c) serial link with plesiochronous clocking.

2.3 互连
      The off-chip interconnects are considered as lossless transmission lines compared to the
on-chip interconnects. The latter have higher resistance and they are considered as a very lossy




                                                            9
transmission line modeled as RLC network as shown in 图 2.4. It should be noted that a
resistance exists parallel to the capacitance, but it is usually ignored and will be neglected in this
thesis. Further details about the interconnects used in this work and their modeling are discussed
in section 4.1.4.

      In 图 2.4, if the load ZL equals the characteristic impedance of the TL, the line becomes
matched. And the voltage at any point, let it be x, and time t equals:

                                         𝑉(𝑥, 𝑡) = 𝑉𝑠 (𝑡) . 𝑒 −𝛾𝑥                             (2.1)
      Where γ is the propagation constant, which equals:


                                                          𝑅
                                   𝛾 = 𝑗𝜔√𝐿𝐶 √1 +            = 𝛼 + 𝑗𝛽                         (2.2)
                                                         𝑗𝜔𝐿

      Where α is the attenuation constant and β is the phase constant. RLC are the respective
values of the resistance, inductance, and capacitance of the model network of the TL.


                                       Rs                TL


                           Vs                     R      L                     ZL
                                                             C



                    图 2.4 The on-chip interconnect model as a lossy transmission line

      Three TL parameters are very important for the interconnects design and high speed serial
links, which are the attenuation constant, the propagation speed, and the characteristic
impedance.

      First, the attenuation constant, α, whose formula is detailed in Equation (2.3). α is plotted
against frequency in 图 2.5. The attenuation increases with frequency until it saturates at the
value in Equation (2.4). As a conclusion, in lossy TL, the propagation constant of the TL is
frequency dependent, different frequencies travelling on the same TL will have different


                                                        10
attenuation and phase shifts. This behavior results in signal dispersion, which is a severe issue for
using these interconnects as high speed serial links.


                                    1        𝑅 2
                          𝛼 = 𝜔√𝐿𝐶 √ (√(1 + ( ) ) − 1)                                                   (2.3)
                                    2        𝜔𝐿


                                                  𝑅 𝐶
                                         𝛼𝑠𝑎𝑡 =    √                                                     (2.4)
                                                  2 𝐿

     Second, the propagation speed, v, whose formula is detailed in Equation (2.5). v is plotted
against frequency in 图 2.5. Similar to the attenuation constant, the speed increases with
frequency until it saturates at the value in Equation (2.6). As a conclusion, the high frequency
components of the signal travel more quickly than the low frequency content, since the low
frequency content now becomes RC limited. This results in inter-symbol interference, which is
another severe issue for these interconnects.




        图 2.5 The attenuation and the propagation speed of a signal through a TL across frequency




                                                        11
                                                    1
                             𝑣=
                                       1         𝑅 2                                                (2.5)
                                  √𝐿𝐶 √2 (√(1 + (𝜔𝐿) ) + 1)


                                                        1
                                           𝑣𝑠𝑎𝑡 =                                                   (2.6)
                                                    √𝐿𝐶
     Third, the TL characteristic impedance, Z0, whose formula is detailed in Equation (2.7). |𝑍0 |
is plotted versus frequency in 图 2.6. Similar in behavior to the attenuation constant and the
propagation speed, the magnitude of the characteristic impedance varies with the frequency,
but this time it decreases, until it saturates at the value in Equation (2.8). As a conclusion, the TL
cannot be matched for all frequency components.

                                                 𝐿      𝑅
                                           𝑍0 = √ √1 +                                             (2.7)
                                                 𝐶     𝑗𝜔𝐿


                                                         𝐿
                                               𝑍0𝑠𝑎𝑡 = √                                           (2.8)
                                                        𝐶




             图 2.6 The magnitude of the characteristic impedance of the TL across frequency



                                                            12
     Three main problems for the use of on-chip interconnects as high speed serial links were
discussed: the signal dispersion, the inter-symbol interference, and the frequency dependence
of the characteristic impedance which limits the matching bandwidth. 设计ers have proposed
many solutions for these problems, they can be divided into two categories. First, solutions
dealing with interfering the data spectrum in order to make the system works. These methods
include the equalization techniques, the modulation and up-conversion techniques, and the
encoding techniques. Second, solutions dealing with the way the TL is terminated, whether
capacitively terminated or resistively terminated.

     The line termination techniques are discussed briefly in next section. Regarding this thesis,
the designed systems and transceivers use the signal encoding techniques with simple and
conventional capacitive termination, as an approach to solve the on-chip interconnects
problems.

2.4 线路端接
     Actually, the response of the lines illustrated in the previous section were for a TL without
reflections, whether it is matched, which cannot be done for the whole spectrum as previously
discussed, or it is an infinite TL, where the attenuation is large enough to neglect the effect of the
reflections. Now considering the more practical and complicated situation of sending a voltage
step through a line of finite length, terminated with a small capacitance. Usually, on-chip, digital
lines are terminated with capacitance, since the inverter or flip-flop at the receiver-end
represents a capacitive load. The response of the capacitive terminated line to a step is depicted
in 图 2.7. An initial attenuated step at the output is due to the high frequency components
propagating down the transmission line at near the speed of light. And later the slower RC effect
charges the entire line to the unit voltage. Because of that RC effect, the voltage at the receiver
end may take a long time to reach the final value, which causes inter-symbol interference as
illustrated in 图 2.9, limiting the maximum data rate on the line [9].




                                                     13
                      图 2.7 © [10] Step response of a capacitively terminated TL

      The second way to terminate the line is using a resistance. Assuming that the line is
terminated with a resistance equal to the characteristic impedance, same as RF circuit designers
terminate their TLs, to prevent some of the received signal reflecting back into the line. Reflection
is less important in digital signaling because the lines are very lossy, the energy of any reflected
signal is dissipated by resistive loss. For resistively terminated lines, the high frequency
components arrive at the receiver with a certain amplitude, while the slower low frequency
component charges up the line to a voltage determined by a voltage divider formed by the total
parasitic series resistance of the line, and the termination resistance. This is the same case as the
capacitive terminated line, a step component that propagates quickly down the line, followed by
a slow RC component. If an optimum value of the termination resistance is chosen, to equate the
high frequency value with low frequency one, as illustrated in 图 2.8. The effect of the slow
component can be masked and the inter-symbol interference can be minimized. 图 2.9 shows
the response of a digital pattern with an optimally resistively terminated line. The received
amplitude is reduced, to that of the high frequency components, sacrificing received amplitude
for bandwidth. The inter-symbol interference is greatly reduced and the received bits can easily
be identified [9].

      The work in [9] and [10] tried to flatten the attenuation effect in order to eliminate
dispersion. While the work in [11], whose results are shown in 图 2.9, chose the resistive



                                                       14
termination value to flatten the propagation speed, in order to effectively eliminate the 符号间干扰（ISI）. An
approximate flat attenuation constant response was also obtained as shown in 图 2.8(a).

     图 2.9 shows the signal in the time domain at the receiver side for a random bit stream,
the resistive termination masks the dispersion effect, however, the signal swing is reduced from
1 V to around 180 mV. As a conclusion, neither termination is the absolute optimum, it actually
depends on how to use the advantages of each kind and rid of its disadvantages. As mentioned
in the previous section, the work in this thesis uses the conventional capacitively terminated TL.
And the work will be focused on the signaling techniques in order to achieve a high performance
transceiver using the normal TL characteristics.




                            (a)                                                    (b)
    图 2.8 © [11] (a) The attenuation, and (b) the propagation speed, of the TL terminated with a resistor
    with the optimum value to eliminate 符号间干扰（ISI）.




      图 2.9 © [11] Transient analysis of a random bit-stream for resistive and capacitive terminations




                                                           15
                               3 文献综述

      In this chapter, the three designs in [12], [13], and [14] will be explained with a different
degree of details in sections 3.1, 3.2, and 3.3 respectively. 节 6.1 shows the comparison
between the results of these works, the thesis’s works in chapters 4 and 5, along with other
different works. Mainly, the work in [12] shows an implementation of a conventional way for on-
chip serial communication using a 锁相环（PLL） and a phase interpolator at the 接收器（RX）. While the work in [13]
represents the precise starting point for this thesis. And finally, the work in [14] is the fastest
previously published SerDes（串行器/并行器） on-chip communication link.

3.1 传统实现方案
      The work in [12] presents an implementation of a conventional way for on-chip serial
communication. Generally speaking, the main drawback of any conventional circuit is the power
consumption, since some complex and power hungry blocks are needed to guarantee the
synchronization between the data and the clock as previously explained in section 2.2. The
following sections explain briefly the different parts of that design.

  3.1.1 整体系统概述
      This system, designed by Park et al. in 2009 [12], was implemented in 0.13μm CMOS
process, it achieves a 9Gbps data rate. The block diagram of the whole system is shown in
图 3.1. The clock generation block is an LC-oscillator-based-锁相环（PLL） which generates a differential
4.5GHz clock. This 锁相环（PLL） consumes 105mW, which is even larger than the whole systems of other
non-conventional schemes. This clock is fed to both the transmitter and the receiver. The
transmitter uses the 4.5GHz clock and interleaves two signals in a way to produce a 9Gbps signal.
The interconnects are differential and resistively terminated. The receiver contains a filter and a
phase interpolator as it will be discussed. It should be noted that the presence of analog
components in the system will reduce its ability to be a standard module used many times in the
chip, which is the case of the main objective of these designs: the inter-core networks. And finally,
that work used a self-test for error check, this part will not be discussed as it is out of the scope
of this literature review.



                                                    16
  3.1.2 发射器
     The block diagram of the transmitter is shown in 图 3.2. The clock divider is used to
provide the needed frequencies for the serializers. Two serializers converts a parallel 1.125GHz
data signal into a 4.5GHz signal, which is equivalent to the serialization of a 9Gbps single data
signal. Also two interleaved drivers are used, each one generates a 4.5Gbps data signal. However,
each pre-driver is active during one different half-cycle of the 4.5GHz clock, so their work is
alternated using a main line driver which allows the system to achieve the 9Gbps data rate.




                     图 3.1 © [12] The block diagram of the whole SerDes（串行器/并行器） system




                         图 3.2 © [12] The block diagram of the transmitter




                                                     17
  3.1.3 互连
     The interconnect used is a differential on-chip transmission line. Each line uses an
intermediate metal layer with width of 6μm and a separation of 3μm. A 21μm width ground
plate below these lines are used for shielding these micro strips, this plate is 3-layers distant from
the main lines. The length of lines is 5.8mm. The lines are terminated by a resistance whose value
was optimally selected to reduce the dispersion [10].

  3.1.4 接收器
     The block diagram of the receiver is shown in 图 3.3. It is conventional in the sense that
it uses a circuitry to determine the phase of the received signals, but it does not use the
conventional 时钟数据恢复（CDR） circuit. A comparator is used to detect the very low amplitude of the received
signals due to the use of resistively terminated interconnects as was explained in section 2.4. An
RC-CR filter and the phase interpolator are used to synchronize the phase of both the received
data signals and the clock signals which come from the 锁相环（PLL）. It should be noted that a digitally
adjusted phase control block is used to perform such synchronization.




                            图 3.3 © [12] The block diagram of the receiver



                                                       18
  3.1.5 小结
     In this section, 3.1, the implementation of the on-chip SerDes（串行器/并行器） system in [12] was explained.
It achieves a data rate of 9Gbps in 0.13μm CMOS technology with the consumption of 600mW.
Besides the 105mW of the 锁相环（PLL）, and the 240mW for the self-test circuitry. As previously
mentioned, any conventional way of implementing the on-chip serial communication will result
in such a very high power consumption. This nearly 1W consumption is totally unacceptable and
impractical for the main objective of using such module as the building cell of a complete inter-
core network. Also, the use of analog blocks is a serious drawback of any designed module for
that purpose, for many reasons:
        The area: The area of the 发射器（TX） and 接收器（RX） alone, without the 锁相环（PLL）, was 0.71mm 2. This is huge,
         as it will be shown in this thesis, many designs have much smaller area. The area is an
         important factor due to the fact that these circuits are to being repeated in several
         locations in the multi-core chips.
        Passive components: These components decrease the scalability of the design. Also,
         working at very high frequencies with such components will require deep insight to
         verify their electromagnetic effect on the rest of the design.
        Power management: In multicore chips, power management techniques are essential
         since the power consumption is currently the serious limit of technological
         advancement. This is quite noticeable in everyday used devices. The presence of analog
         circuitry will limit the flexibility of the chip to vary the supply level or the working
         frequency of the different cores to achieve the optimum overall performance.
        Portability: Analog designs require a lot of time and re-designing when porting the
         design from a technology to another. This will seriously affect the time-to-market of
         these designs. On the contrary of the all-digital designs.

     Moreover, this design is feeding both the 发射器（TX） and 接收器（RX） with the same clock signal from the
same 锁相环（PLL）. As shown in the chip micrograph in [12], both the 发射器（TX） and 接收器（RX） are close to the 锁相环（PLL）. This
is logical for the tape-out to silicon prove the on-chip SerDes（串行器/并行器） designs, even this thesis’ works will
do the same. The 发射器（TX） and 接收器（RX） will be floorplanned beside each other for testing purposes, while
the long interconnect will be snaking around. However, it should be noted very carefully, that


                                                    19
this is not the case when trying to use these circuits in real applications when a communication
is needed between far distant cores. The phase mismatch between the data and the clock due to
the routing of both over very long distances was not considered in [12], only the mismatch due
to the data travelling this distance was considered.

        Furthermore, this design needs some external digital adjustment to guarantee the
synchronization. This adjustment will need some self-calibration circuitry when it is intended to
be used in multicore chips. Whether this circuitry is applicable, its power and area consumption,
and whether it will support all mismatches that may occur, all of these were not investigated in
[12].

        As a conclusion, such system consumes a lot of power and area, it contains analog blocks,
and it requires deeper investigation to guarantee its functionality in the targeted environment.

3.2 起点
        The work in [13] presents an implementation of the on-chip serial communication. This
system designed by Safwat et al. in 2011 represents the starting point for the work done in this
thesis. The following sections will explain in details this design.

  3.2.1 整体系统概述
        This system was designed in 台湾半导体制造公司（TSMC） 65nm CMOS technology, it achieves a data rate of
12Gbps. The block diagram for the whole system is shown in 图 3.4. A 三电平 self-timed
signaling technique is used, this signaling technique was proposed in [15]. This signaling
technique is detailed in section 3.2.2, and it is the signaling technique used in the first designed
system in this thesis (chapter 4). The 数控振荡器（DCO） generates the system clock of 24GHz which equals the
double of the data rate achieved. The serializer serializes the 8-bit parallel input and feeds it to
the 三电平 encoder and driver. A differential interconnect is used with capacitive termination.
Then the receiver extracts both the data and the clock from the differential signals, and
deserializes the data to generate the 8-bit parallel output at 1.5GHz.




                                                     20
                            图 3.4 © [13] The block diagram of the whole system

   3.2.2 信号传输技术
      This system uses a 三电平 self-timed signaling technique. This technique was presented by
same authors in [15], it is depicted in 图 3.5. This signaling technique embed both the data
and the clock in a single signal, which enables the system to extract both of them from the same
signal. This is what makes this signaling scheme a self-timed signaling, and no external clock is
needed at the receiver. This makes any system using this technique a skew and jitter insensitive
system, since the data and clock are perfectly synchronized because they are extracted from the
same source. Deserializing the data signal at the receiver is done without the need of any phase
detection or feedback or any kind of calibration. Therefore, no complex circuitry, which usually
contains power hungry blocks such as 锁相环（PLL） and 时钟数据恢复（CDR）, is needed in the system. A simple decoder
circuit can simply extract both the data and the clock with minimum power and area
consumption.

                                                  0                  1




                                  VDD
                                ½VDD
                                  0

图 3.5 The 三电平 signaling technique proposed in [15] and used in both [13] and this thesis’s first design
presented in chapter 4

      Moreover, this signaling scheme is dc constant, which eliminates the need for equalization
whether in the transmitter or the receiver. The equalization also needs some power hungry




                                                         21
blocks and adds to the complexity of the system. It can be said that using such signaling technique
simplifies the whole design and makes it easily possible to implement it all-digitally using
standard cells. Another advantage is the effect of using such signals on the on-chip interconnects.
To explain this advantage, the power spectrum of this signaling technique is produced in
图 3.6(b). While the power spectrum of the conventional binary data scheme is produced in
图 3.6(a). The conventional scheme has a wide spectrum which results in a dispersion and
inter-symbol interference as was shown in 图 2.5 and 图 2.9. While the signaling scheme
used in this design has a shifted power spectrum to high frequencies. From 图 2.5 showing
the interconnect attenuation and propagation speed versus frequency, it can be concluded that
using this scheme will much reduce the dispersion and the 符号间干扰（ISI）. This is the result of that the
majority of frequency components of the signal have nearly the same propagation speed and are
exposed to the same attenuation.




图 3.6 The power spectrum of a random bit stream using (a) the conventional 两电平 scheme at 24 Gbps, (b) the
scheme in 图 3.5 at 12 Gbps

      To summarize, the signaling technique in 图 3.5 has the following advantages:
          It is jitter insensitive due to embedding both the data and the clock.
          It is dc constant.
          It has shifted power spectrum to eliminate dispersion and 符号间干扰（ISI）.



                                                          22
      This provides an approach to solve the problems discussed in section2.3. As previously
mentioned, the solution depends on the encoding and signaling scheme to overcome or even
benefit from the interconnect characteristics, it is a data spectrum solution.

  3.2.3 互连
      The interconnect used in this design is a differential line with capacitive termination. The
architecture of the lines and their characteristics are shown in 图 3.7. The two differential
lines are ground shielded both vertically and horizontally, which introduces the capacitances
indicated. Each line’s length is 3mm, with 1μm width and 0.5μm spacing. Besides the figure, the
parasitics values are indicated. More information about the meaning of these values is discussed
in section 4.1.4.




                          图 3.7 The interconnect used and its characteristics

  3.2.4 发射器
      As shown in 图 3.4, the transmitter is formed by the serializer and the encoder and
driver circuit. This section will focus on the designed encoder and driver circuit which is illustrated
in 图 3.8. This architecture generates the 三电平 signal in 图 3.5 in a straight forward way.
First, both the 𝑑𝑎𝑡𝑎 and the ̅̅̅̅̅̅
                             𝑑𝑎𝑡𝑎 are synchronized to Clk/2 (which equals 12GHz since the
system’s clock equals the double of the 12Gbps data rate as mentioned previously). Then the
                          ̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅
signals (𝑑𝑎𝑡𝑎 ⊕ 𝐶𝑙𝑘) and (𝑑𝑎𝑡𝑎   ⊕ 𝐶𝑙𝑘 ) are generated and synchronized to the system’s clock.
This was the encoding part, then the 三电平 signal is generated using the 传输门（TG）s driver. Two sets of
传输门（TG）s are used to generate the TL signal and its inverse. The system’s clock is used as a controller
for these gates. During the low half-cycle, all the 传输门（TG）s open the path for the third level, which




                                                       23
equals VDD/2. During the high half-cycle, the 传输门（TG）s conduct the (𝑑𝑎𝑡𝑎 ⊕ 𝐶𝑙𝑘) signals. Therefore,
the 三电平 signaling is generated, since the (𝑑𝑎𝑡𝑎 ⊕ 𝐶𝑙𝑘) is the ̅̅̅̅̅̅
                                                                  𝑑𝑎𝑡𝑎 during the Clk/2 first half
cycle, then the 𝑑𝑎𝑡𝑎 signal, which is exactly the description of this signaling scheme shown in
图 3.5.

     Another note to mention is that this design, and also this thesis’s work in chapter 4, use a
kind of source matching. The resistance of these 传输门（TG）s are close to the value of the characteristics
impedance of the TL. However, since the characteristic impedance is not a fixed value as
previously discussed in 图 2.6, then the TL cannot be totally matched. But designing the 传输门（TG）s
to have a resistance’s value close to the characteristic impedance at the working frequency will
actually benefit from the source matching characteristics. As explained in [16], when the
interconnect is capacitively terminated, reflections occur at the receiver-end. These reflections
return to the driver, then due to the source matching, they are not reflected but rather added to
the transmitted signals. In other words, the transmitted signals amplitude are doubled at the
driver end, which much enhances the voltage swing, leading to better detection. However, it
should be noted that this theoretical explanation provided in [16] is not totally applicable for the
used interconnects. This is due to the fact that these interconnects are very lossy and hence the
reflections are severely attenuated before they are added to the transmitted signals.




                             图 3.8 © [13] The encoder and driver circuit



                                                      24
  3.2.5 接收器
     As shown in 图 3.4, the receiver is formed by two low switching threshold inverters, a
phase detector and the deserializer. The inverters converts the 三电平 signals to a normal CMOS
两电平 signals by considering the third level as high. The produced 两电平 signals are A and B.
Then the phase detector extracts both the data and the clock from these signals, and feeds them
to the deserializer. Which deserializes the data and generates the 8-bit parallel 1.5GHz output.

     The phase detector block diagram is shown in 图 3.9, then detailed in 图 3.10. This
circuit’s name may give the impression that it is complex circuit for phase synchronization for
example, but this isn’t true. It is a quite simple circuit that only detects the order of the falling
edges of the A and B signals. It is a sequential circuit with embedded feedback to find out the
precedence of edge occurring. QA and QB are generated to express the falling edges of A and B,
NANDing these will produce the clock, while feeding them to an SR latch will generate the data
(the Out signal in the diagram). Further details and explanation are provided in section 4.2.2.1.




                     图 3.9 © [7] The top level block diagram of the phase detector

3.2.1 小结
     In this section, 3.2, the implementation of the on-chip SerDes（串行器/并行器） system in [13] was explained.
It achieves a data rate of 12Gbps in 台湾半导体制造公司（TSMC） 65nm CMOS technology with the consumption of
15.5mW. This design represents the starting point of the work in this thesis.

     The data rate achieved in this work is acceptable, however it is low compared to other
works using the same feature size. The power consumption is impressively low at such a data
rate, this is a result of the signaling idea and how it made all the circuits to be simple without the



                                                       25
                      图 3.10 © [13] The detailed circuit diagram of the phase detector


use of any complex circuitry. The 三电平 signaling scheme has proven effectiveness due to its
jitter insensitivity, dc-constant level, and concentrated spectrum in the saturation region of the
TL characteristics.

     Regarding the disadvantages or the flaws with this design, the main drawback is the use of
a clock frequency of double the data rate. This is the severe limit for increasing the data rate. In
order to make the system working at 16Gbps for example, the driver should be able to work at
32GHz which is very difficult. Also, for 12Gbps data rate, the signal on the line has the frequency
of 24GHz, which causes the line parasitics to have stronger effects.

     Moreover, the use of an external VDD/2 driver is an overhead for the layout of the design.
In a multicore chips, this means the routing of an additional supply to each core. If a simple
voltage divider with two resistors is used to generate such a level, this will interact with the
resistance of the 传输门（TG）s in the driver. Which will have two negative effects: the third level value will
not fixed, the 传输门（TG）s loading will affect it, and the current drawn will seriously depend on the
resistance value. This can cause a severe problem since the effect of 工艺、电源与温度（PVT） corners on the 传输门（TG）s and
the resistors are different.



                                                          26
     Furthermore, there are some synchronization issues inside the transmitter itself. This
design clock and clock/2 are independent from each other. Since one is divided to produce the
other without taking into consideration the variation of this frequency divider delay across 工艺、电源与温度（PVT）
corners. And the frequency divider used has some buffers and some synchronization feedback
circuits to match the clock/2 and its inverse. Therefore, this delay variations cannot be neglected.
This seriously affects the transition part from the encoder to the driver as shown in 图 3.8.
This makes this design susceptible to severe corner variations, which has led to a more variation
tolerant technique in chapter 4 of this thesis.

     As a conclusion, the main three drawbacks of this design are the need of a clock’s frequency
of double the data rate, the need of an external V DD/2 driver, and the synchronization issues in
the transmitter.

3.3 最快链路
     The work in [14] represents the fastest previously published SerDes（串行器/并行器） on-chip communication
link during the work of this thesis. The block diagram of the whole system is shown in 图 3.11.
It is designed by Rhew et al. in 2012. It was implemented in 65nm CMOS technology, and it
achieves a data rate of 20Gbps with power consumption of 27.2mW. The numbers noted on the
figure mentions that the data rate is 22Gbps, but the paper itself notes clearly that the achieved
data rate is 20Gbps.

     Since this work was done by the same group who designed the system in section 3.1, it uses
the same idea of serializing. Two interleaved serializers are used, each working at half the data
rate. Then two interleaved voltage-mode line drivers generates the 20Gbps signal on the
transmission line. The interconnect used is a 2μm wide micro strip, 10mm long, and resistively
terminated by an optimum resistance to eliminate dispersion same as presented in [9].

     At the receiver-end, the clock is synchronized using a delay control unit. The produced
clocks are used to operate the two interleaved comparators to sample the two signals of data,
which are deserialized using two interleaved deserializers to produce the output parallel 8-bit.




                                                   27
                        图 3.11 © [14] The block diagram of the whole system

     This design achieves a very high data rate with very low power consumption. However, it
has nearly the same logical flaws of the conventional design as discussed in section 3.1.5. The
design is feeding both the 发射器（TX） and 接收器（RX） with the same clock, and hence the mismatch due to the
clock travelling a long distance is neglected. Also, an external digitally controlled delay unit is
used, so calibration was not investigated to guarantee the functionality of this circuit as building
cell for inter-core network in multicore chips.




                                                     28
                                     4 第一个设计

     As previously mentioned, this thesis contains two different designed systems for on-chip
SerDes（串行器/并行器） communication. The first design is presented in this chapter, and it was published in the
2014 IEEE International Symposium on 电路s and 系统s (ISCAS 2014). The paper title is “A
Variation Tolerant Driving Technique for All-Digital Self-Timed 3-Level 信令 High-Speed
SerDes（串行器/并行器） Transceivers for On-芯片 Networks” by Ramy N. Tadros, Abdelrahman H. Elsayed, Maged
Ghoneima, and Yehea Ismail. As will be presented in this chapter, this transceiver was layouted
and prepared for tape-out in 联华电子股份有限公司（UMC） 0.13μm CMOS technology in June 2014. When the chip will
return in August 2014 as expected, this transceiver results will be summarized in a journal paper.

     This chapter construction is as follows: First, the whole system overview section, which
contains the information about the system architecture, the used signaling technique, the
interconnect, and the test bench and how to verify the system’s functionality. Second, the
circuits’ architecture of the different blocks of the transmitter and the receiver circuits. This part
explains in detail the variation tolerance property of the proposed driving technique, and also it
contains the simulation results of this system in 台湾半导体制造公司（TSMC） 65nm CMOS technology. Third, the tape-
out part, which discusses the porting from 台湾半导体制造公司（TSMC） 65nm to 联华电子股份有限公司（UMC） 0.13μm. It also presents the
layout of the system, the designed testing methodology, and the post layout simulation results.
Finally, the last part will summarize all the results of this design and discuss the pros and cons of
using such transceiver in multicore chips.

4.1 整体系统概述
      This system introduces a variation tolerant driving technique for self-timed 三电平 signaling
SerDes（串行器/并行器） transceivers for on-chip serial links. The new design generates the 三电平 signal without
a ½VDD driver, thus removing all the overhead and hassle of an additional supply as explained in
section 3.2.1. Moreover, the proposed all-digital scheme uses half the clock frequency while
maintaining the same data rate, and can be easily ported to different technologies. The circuit
for the proposed transceiver is designed for a 3mm long lossy on-chip differential interconnect




                                                    29
in 台湾半导体制造公司（TSMC） 65nm CMOS technology. The transceiver achieves a data rate of 15.5Gbps with power
consumption of 42.3mW. This chapter will discuss this design in details.

   4.1.1 系统’s 架构
      The block diagram of the whole system is shown in 图 4.1. The transmitter has two
inputs, the parallel 8-bit bus at 1.9375Gbps and the 31GHz clock (double the data rate) from the
数控振荡器（DCO）. The clock divider uses the 数控振荡器（DCO） clock to generate multiple phases of the 15.5GHz clock,
which is the system working frequency. It also generates 7.75G, 3.875G, and 1.9375GHz clocks
for the serializer to produce the serial data at 15.5Gbps. The proposed encoder and driver then
multiplexes the serial data with the clock phases in order to generate the 31GHz three-level signal
fed to the capacitively terminated transmission line. The driver is sized in a way to achieve source
matching to the line, this results in a high voltage swing at the termination due to doubling the
signal amplitude [16], this is an advantage over the resistively terminated lines. The receiver
consists of a simple decoder detecting both the serial data and the 15.5GHz clock from the same
signal, which makes the circuit insensitive to accumulated jitter. The receiver also contains a clock
divider similar to the one used in the 发射器（TX）, generates the needed clocks for the deserializer to
recover the parallel 8-bit at 1.9375Gbps.

   4.1.2 信号传输技术
      The used signaling technique is the same scheme proposed in [15] and used in [13] as was
mentioned in section 3.2.2. The signaling scheme in 图 3.5 is illustrated again in 图 4.2.
The third level is VDD/2. For a low bit, the signal half-high then half-low, and vice versa for the
high bit.

      As discussed in section 3.2.2, using such technique has many advantages: It makes the
system jitter insensitive, makes the circuits simple, it has a dc-constant level, and it has a shifted
power spectrum which eliminates dispersion and 符号间干扰（ISI） as shown in 图 3.6(b). Both data and
clock may be extracted from the same signals.




                                                    30
                           D5
                           D7
                           D1
                           D0

                           D2
                           D3
                           D4

                           D6
                                                                                      数控振荡器（DCO）
                                                        clk/2             2*clk
                                                             时钟
                                                      clk/4 Divider
                             串行器
                                                      clk/8




                                                                          clk180
                                                                          clk270
                                                                          clk90
                                                                           clk0
                                                                   编码器
                                           Serial 数据             & 驱动器
                           发射器（TX）




                                                                                        TL_in_bar
                                                                             TL_in
                                                                                        TL_out_bar
                                                                            TL_out
                          接收器（RX）              Serial 数据

                                                                  解码器

                                                                                     clk180
                                                                            clk0


                                                        clk/2
                                                      clk/4      时钟
                             并行器                       Divider
                                                        clk/8
                           D5
                           D1
                           D0

                           D2
                           D3
                           D4

                           D6
                           D7




                              图 4.1 The block diagram of the whole system

                                                  0                   1




                                 VDD
                               ½VDD
                                 0

图 4.2 The 三电平 signaling technique proposed in [15] and used in both [13] and the design in this chapter



                                                           31
  4.1.3 互连
     The interconnect used is shown in 图 4.3. It is the same microstrip as the one used in
[13] but without the above ground plate, this will reduce the capacitance. The interconnect is an
intermediate line whose width is 2μm, spacing 0.5μm, and length of 3mm. The line characteristics
are also shown in figure. Further details about the meaning of these characteristics are provided
in next section.




                         图 4.3 The interconnect used in this design and its characteristics

  4.1.4 测试平台
     It is not straightforward to test the functionality of the designed transceiver. This section
will explain how the system and the interconnect are simulated. 图 4.1 showed the system
block diagram, while 图 4.4 shows the block diagram of the test bench used.
                                                             8
                                                             /




     Random        8                    TL_in                               TL_out                   8      比特误码率（BER）
       字节
    Generator
                   /
                            发射器（TX）          TL_in
                                                          TL                TL_out
                                                                                       接收器（RX）            /
                                                                                                         Calculator
                               Clk




             Clk                                                      Clk


                  时钟
                Generator


                       图 4.4 The test bench used to test the functionality of the transceiver



                                                                 32
     The two blocks 发射器（TX） and 接收器（RX） are the only circuit designed blocks, all the remaining parts are
just behavioral models. The design is simulated in Cadence Analog Vituoso environment, and
hence the behavioral models are described using Verilog-A codes. A random byte generator
provides the system with random input to give a good estimation of the functionality without the
need of a large number of iterations. The clock generator used is just an ideal independent source
of pulses, but with simulated half sine transient behavior with practical values of rise and fall
times. The first part of the 发射器（TX） will be a clock buffer starting with a minimum sized input
capacitance, so that the actual clock fed to the system is quite close to the practical case after
adding the 数控振荡器（DCO）. A 比特误码率（BER） calculator is used to compare the input and output of the system, and
reports automatically whether the transceiver is working properly or not. The main scope of this
thesis is the physical layer of the link, so when a number of bits is fed to the 发射器（TX）, then the same
combination of bits is received correctly at the 接收器（RX）, this means that it just works. No further
protocols nor frames are considered, just the physical layer.

     Regarding the interconnect, it needs to be modeled in order to simulate its behavior. The
prediction model characteristics provided in [17] are used. This predictive technology provides
the inductance, resistance, and capacitance of the interconnect. Then, π-model sections are used
to construct a SPICE model for the simulations. An illustration of a single π-model is shown in
图 4.5. ‘S’ is the number of sections used, ‘R’ and ‘L’ are the total resistance and inductance
of the line respectively. ‘Ch’ is the horizontal coupling capacitance between two lines while ‘Cv’ is
the vertical one. According to [18], approximately 30 sections are enough for a very good
approximation. In the simulations of this thesis, 50 π-sections are used for even better accuracy.

4.2 收发器
     In this section, the circuits architecture of all the blocks are described in details. Also, the
proposed variation tolerant driving technique is discussed. And the simulation results in 台湾半导体制造公司（TSMC）
65nm CMOS technology are shown.

  4.2.1 发射器
     As described in 图 4.1, the transmitter has two inputs: the high speed 31GHz clock from
the 数控振荡器（DCO）, and the 1.9375GHz 8-bit parallel data. First, this clock is buffered to the clock divider to



                                                    33
                       图 4.5 Illustration of SPICE model for a single π section of the TL

provide four phases of the 15.5GHz clock, and also 7.75, 3.875, and 1.9375GHz. These low
frequency clocks are fed to the serializer which serializes the 15.5Gbps signal data. The encoder
and driver block receives the data signal and the four phase clocks to generate the 三电平 signals.

     4.2.1.1 串行器
      The serializer used in this design is the same used in [13], its architecture is illustrated in
图 4.6. ‘DET触发器（FF）’ is a double-edge triggered flip-flop, its architecture is illustrated in 图 4.7.
The DET触发器（FF） has two data inputs. At the low clock half-cycle, it generates the DL data, and at the
high half-cycle, it generates the DH data. Therefore, it serializes the two-input data to a double-
frequency single data signal. The 触发器（FF） used is a positive edge triggered C2MOS 触发器（FF） architecture, as
in the majority of this work. The positive level triggered latch and 多路复用器（MUX） are implemented using
传输门（TG） based architecture. Using this DET触发器（FF） in the three level as shown, and using Clk/8 then Clk/4
then Clk/2, will result in having the parallel data serialized to a singled data signal at Clk. It should
be noted that the first level working at Clk/8 is implemented using typical threshold transistors
while the rest is implemented using low threshold transistors. This is to avoid the leakage caused
errors in the part working at low frequency, and to increase the circuits’ speed of the part working
at high frequencies.




                                                            34
                       D0   DL
                             DET触发器（FF）
                       D4   DH
                                        TYP




                       D2   DL                      DL
                             DET触发器（FF）                   DET触发器（FF）
                       D6   DH                      DH
                                        TYP                  LVT
                                                                                           Serial
                                                                           DL
                                                                                           数据
                                                                            DET触发器（FF）
                                                                           DH
                       D1   DL                      DL                              LVT

                             DET触发器（FF）                   DET触发器（FF）
                       D5   DH                      DH
                                        TYP                  LVT




                       D3   DL
                             DET触发器（FF）
                       D7   DH
                                        TYP




                                 Clk/8                   Clk/4                  Clk/2

图 4.6 The block diagram of the serializer. The ‘DET触发器（FF）’ is a Double-Edge Triggered 触发器, and its architecture
is in 图 4.7. The subscript ‘TYP’ refers to typical threshold transistors, and ‘LVT’ to low threshold transistors



                                   DL         触发器（FF）

                                                                                  IN0
                                                                                   多路复用器（MUX）
                                                                                  IN1
                                                                                     Sel

                                  DH          触发器（FF）             Latch
                                                                                    Clk


                                              Clk                  Clk

                            图 4.7 The block diagram of the ‘DET触发器（FF）’ used in 图 4.6




                                                                 35
     4.2.1.2 时钟分频器
     The clock divider is constructed mainly by the divide-by-two 触发器（FF） circuit illustrated in

图 4.8. The idea of generating the four phases of the clk/2 is to alternate clk and clk, which
results in phase shift of half-cycle of the high speed clock (31GHz), which is equivalent to 90° of
the clk/2. Dividing the resultant clk/2 by another two divide-by-two units, will results in the two
other needed frequencies: clk/4 and clk/8. The edge matching circuit shown, has the same
architecture used in [13], which is illustrated in 图 4.9. This circuit is used to synchronize the

clk and clk signals generated from the clock divider at any frequency.

     4.2.1.3 编码器和驱动器电路
     As discussed in section 3.2.1, the design in [13] used an additional ½VDD driver in order to
generate the 三电平 signal. This extra voltage level necessitates an extra supply and power
distribution network to distribute to the different transceivers in the 片上网络（NoC） throughout the chip.


                                                                    Divide-by-two Unit




                                                                      Edge                Clk/2 (0°)
                        触发器（FF）                                          Matching
                                                                     电路             Clk/2 (180°)



                        Clk




                                                                      Edge                Clk/2 (90°)
                        触发器（FF）                                          Matching
                                                                     电路             Clk/2 (270°)




                         Clk

           图 4.8 The block diagram of the clock divider’s part generating the four phases of clk/2




                                                          36
                             Clk
                                                                                Clk



                                                                                Clk
                             Clk



        图 4.9 The block diagram of the edge matching circuit used in the clock divider in 图 4.8

Furthermore, it’s an additional source of variations for the system. The proposed driving
technique generates the third level without the need of an additional supply. Second, that design
was using a high speed clock of double the data rate for the driving procedure, while the
proposed design works only on half of this frequency, which relaxes the design. As a result of
these modifications, the system becomes more robust against all sorts of variations, such as 工艺、电源与温度（PVT）
corners, duty cycle variations of the 锁相环（PLL） clock, and different data rates.

     The block diagram of the designed new encoder and driver is shown in 图 4.10. The data
synchronization part is used to perfectly synchronize the serial data from the serializer, with the
buffered zero phase clock. These flip-flops are buffering the serial data to the driver. In such a
critical circuit, working at a very high frequency, any misalignment between different signals may
affect the circuit robustness, which is the reason behind the dummy delays units. For all the
driving signals (data, data_bar, clk0, clk0_bar, clk90, clk90_bar), they are running through exactly
same conditions. Therefore, perfect synchronization will be obtained across any corners, and the
whole misalignment margin is left for physical mismatches. These synchronization parts solve a
serious problem with the design in [13] as discussed in section 3.2.1.

     The main encoding idea that enabled the design to generate a third voltage level without
external driver, is obtaining that level by voltage dividing the supply. Each pair of front-end
multiplexers have a common node output (see 图 4.10). If both are either pulling-up or
pulling-down together, the node on the TL will be either pulled-up or down respectively.
However, if one of them is pulling-up, while the other one is pulling down, a current path from



                                                          37
the supply to the ground is created, and since the pull-up and pull-down networks are well
matched, the output node takes the level of ½VDD.

     The operation of the circuit is as follows: three main signals and their inverses are used for
driving: clk0, the serial data synchronized with clk0, and clk90. For a ‘0’ bit for example, all the
multiplexers are selecting the first input. First, clk0 is high, while clk90 is low, so ½VDD is
obtained, then clk90 goes high so does the output node, this was the first half, then the inverse
happens, clk0 goes low leading to ½VDD, then at the end, clk90 goes low so does the output
node.
                                                           data
                                                           drive
                                           data_bar
                                                      传输门（TG）
                  Serial 数据        数据
                                  Synchroni-
                                    -zation            data_bar
                                                         drive
                                    clk0




                                               data
                         To clk                       传输门（TG）
                          div
                                                                           S1 S0
                                                           clk0
                clk180                                     drive
                                  Dummy                                   多路复用器（MUX）
                                    触发器（FF）                                    (传输门（TG）)
                         To clk                       传输门（TG）                              TL_in
                                    VDD




                          div
                                                           clk180
                 clk0                                                     多路复用器（MUX）
                                  Dummy                     drive
                                    触发器（FF）                                    (传输门（TG）)
                                                      传输门（TG）
                                    VDD




                                                           clk90
                clk270                                     drive          多路复用器（MUX）
                                  Dummy
                                    触发器（FF）                                    (传输门（TG）)
                                                      传输门（TG）                            TL_in_bar
                                    VDD




                                                           clk270
                clk90                                                     多路复用器（MUX）
                                  Dummy                     drive
                                    触发器（FF）                                    (传输门（TG）)
                                                      传输门（TG）
                                    VDD




                  图 4.10 The block diagram of the designed encoder and driver circuit

     设计ing the inverters and the multiplexers is a little bit tricky due to the voltage dividing
issue, especially to work across the slow skewed corners, the solution to such problem is to use




                                                             38
transmission gates as shown in 图 4.11. The 多路复用器（MUX）es are implemented using two 传输门（TG）s
controlled by the select signal. The inverters are not simple CMOS inverters, but are rather
inverters implemented using 传输门（TG）s in both pull-up and pull-down networks. This is what makes the
driver more variation tolerant than using an external source. Because when the PMOS devices
are faster, the third level will be higher and also the receiver front end will have higher threshold,
which in its turn will compensate all these changes and the circuit will still function correctly. And
vice versa when NMOS are faster.

     Sizing the front end of both the 发射器（TX） and 接收器（RX） is done simultaneously. Matching the PMOS to
the NMOS of each single transmission gate is necessary. The sizes of the 多路复用器（MUX）es should be large
enough to be able to drive the large line. Also, sizes must ensure approximate source matching
to the line, this results in a high voltage swing at the termination due to doubling the signal
amplitude [16], this is an advantage over the resistively terminated lines as discussed in
section 3.2.4.

                                                                   S0_bar
                                                             in0
                                           S1
                                                 S0
                                   in0                             S0
                                          多路复用器（MUX）         out                      out
                                   in1    (传输门（TG）)
                                                                   S1_bar
                                                             in1

                                                                   S1




                                                              in        in_bar

                                     In                out               out

                                          传输门（TG）                  in        in_bar



   图 4.11 发射器 front end components -the inverters and multiplexers- are implemented using 传输门（TG）s


  4.2.2 接收器
     As Described in 图 4.1, the receiver has one input, which is the 三电平 differential signal.
And two outputs, which are the parallel 1.9375GHz 8-bit output and the extracted 15.5GHz clock.
First, the decoder detects the 三电平 signals and extracts both the serial data and the clock. Then


                                                              39
a clock divider similar in architecture to the one used in the 发射器（TX） (see section 4.2.1.2), is used to
provide the following clock frequencies: 7.75, 3.875, and 1.9375GHz. These clocks are fed to the
deserializer to generate the parallel 1.9375GHz 8-bit output.

     4.2.2.1 解码器
     The block diagram of the decoder is shown in 图 4.12. The 三电平s are detected by
relatively high threshold inverters producing the A and B signals. In other words, these signals
represents the 三电平 signals but with the third level pulled-up as high. The same phase detector
circuit in [13] is used (see 图 3.9 and 图 3.10), but with modifications. Then the produced
signals are processed by a NAND-based SR latch to produce the data and by a NAND gate to
recover the clock.

     The used phase detector is illustrated in 图 4.13. It is used to receive the 2-signals
information in A and B signals, and transforms is to the signals QA and QB. The waveforms of these
signals simulated are shown in the simulation results section (next one). According to the
signaling technique and the high threshold inverters used, the A and B signals will represent the
data by staying low for only ¼ of the data cycle. Whether the data is low or high determines the
location of this ¼ data cycle. That is why a phase detector is used, to detect which signals, from
A and B, had its own low ¼-cycle first. The QA and QB signals are pulled down for a ¼ cycle when



                         TL_out                          A_bar       A
                                                                           Phase
                                                                          Detector
                      TL_out_bar                         B_bar       B

                                                                            QA   QB
                           clk



                       Serial 数据                SR
                                                 Latch


                                 图 4.12 The block diagram of the decoder




                                                         40
                           I1
                         ‘w/2w’

                        QB               QB            M3
                                                      ‘4w’
                                              X
                                   M1                  M4                  I2
                       A          ‘2w’            A   ‘4w’               ‘w/2w’
                                                                                  QA
                                   M2                 M5           M6
                       QB         ‘2w’                ‘w’
                                                             B    ‘2w’




                           I1
                         ‘w/2w’

                        QA               QA            M3
                                                      ‘4w’


                                   M1                  M4                  I2
                       B          ‘2w’            B   ‘4w’               ‘w/2w’
                                                                                  QB
                                   M2                 M5           M6
                       QA         ‘2w’                ‘w’
                                                             A    ‘2w’




                   图 4.13 The phase detector detailed circuit with sizing methodology

a falling edge occurred at A first, and when a falling edge occurred at B first respectively. These
QA and QB can be fed to an SR latch to generate the data, and NANDing them will result in the
clock perfectly synchronized with the data to be able to deserialize it right.

     The circuit functions as follows: First case, when a falling edge occurs at A first, and B is
high, then A returns to high and B goes low then all returns to their high normal state. The above
circuit is explained: A and QB were high, so M1 and M2 were pulling X down, I1 was O触发器（FF）, also M4
and M5 were O触发器（FF）. When the falling edge occurs at A, M3 with M4, now ON, pull ̅̅̅̅
                                                                             QA up, and
hence QA goes low. Which will guarantee that QB stays high even if B goes low, due to I1 (in the
below circuit) now pulling the X node up and forcing it to stay high. When the falling edge occurs



                                                             41
at B, M6 now go ON and pulls ̅̅̅̅
                             QA down forcing QA to return high and hence the full system returns
to its original state waiting for which edge occurs. Second case, when the falling edge occurs first
at B, QB goes low in the same manner in the below circuit, therefore, I1 in the above circuit will
guarantee that X node is high and hence QA stays high. When the falling edge on A come, it will
pull QB up using M6 and I2 in the bottom circuit hence returning to the initial state.

      To conclude the functionality of this simple circuit, the capacitance at X node is the key of
the operation. It is maintained low at normal operation, and whenever an edge occurred on A or
B, it forces this node in the other circuit to go high, and hence taking the lead. That is why it is a
circuit that detects phase.

      The modifications were in the adding of a 传输门（TG） instead of a single transistor, and in the sizing
methodology. This 传输门（TG） enables the increment of the working frequency significantly and added to
the detection robustness. Because it makes the pull-up network of the node X sensitive to the
inverse of the Q signals, which will always change first, so it makes the network both very
sensitive and also has the needed high driving capability to be able to maintain the state at the X
node to preserve priority. The sizing is indicated on figure, it should be taken care that all the
branches have exactly equal driving capability except two critical parts. First, the pull-up network
of the X node as explained, which was solved by being sensitive to the inverse of Q signals rather
than only increasing the size, and M6 which the pull-down network responsible of detecting the
second falling edge and forcing the system to return back to its initial state. Increasing the size of
M6 will ensure the speed and sensitivity of the system to detect the second edge and quickly
return to the initial state waiting for another data bit.

     4.2.2.2 并行器
      The design uses the same deserializer used in [13], its block diagram is shown in 图 4.14.
Each stage deserializes the signal to two parallel signals. Three stages are used using clocks at
frequencies of Clk/2, Clk/4, and Clk/8. Small variations exist in the flow like an additional flip-flop
or an additional latch, these variations intend to avoid any mismatches or timing errors.




                                                     42
                                                            触发器（FF）         触发器（FF）      D0



                                                            Clk/4      Clk/8




                                                                       触发器（FF）      D4



                                                                       Clk/8




                               触发器（FF）            触发器（FF）             触发器（FF）         触发器（FF）      D2



                              Clk/4          Clk/4          Clk/4      Clk/8




       触发器（FF）                      触发器（FF）            触发器（FF）                        触发器（FF）      D6



       Clk/2                  Clk/4          Clk/4                     Clk/8
数据



       触发器（FF）      Latch           触发器（FF）                           触发器（FF）         触发器（FF）      D3



       Clk/2   Clk/2          Clk/4                         Clk/4      Clk/8




                               触发器（FF）            触发器（FF）                        触发器（FF）      D7



                              Clk/4          Clk/4                     Clk/8




                                                            触发器（FF）         触发器（FF）      D1



                                                            Clk/4      Clk/8




                                                                       触发器（FF）      D5



                                                                       Clk/8




                   图 4.14 The block diagram of the deserializer




                                             43
  4.2.3 仿真结果
     This section shows the simulation results of the designed system in 台湾半导体制造公司（TSMC） 65nm CMOS
technology with a 1V supply. The system functions correctly across all 工艺、电源与温度（PVT） within an uncertainty
margin of ± 5% in the clock duty cycles. And it can operate in a typical corner up to 15.5Gbps. All
the simulation results presented in this section are at the typical corner at 15.5Gbps. 图 4.15
shows the waveforms of the key signals of the encoder and driver circuit discussed in
section 4.2.1.3 (see 图 4.10). There are the signals driving the multiplexers: the data signal,
and two phases of the clock at 0° and 90°, also the generated 三电平 signal is shown. 图 4.16
shows the waveforms of the signals of the decoder circuit discussed in section 4.2.2.1 (see
图 4.12). There are the received 三电平 signal, A and B signals, QA and QB signals, and the
extracted data and clock signals. 图 4.17 shows the eye diagrams of the 三电平 signals at the
front-end of both the transmitter and the receiver, and the eye diagrams of the extracted data
and clock signals. The total power consumption is 42.3mW at 15.5Gbps, and a detailed analysis
of the different power consumption components are shown in 表 4.1. A summary of this
design results is summarized in 表 4.2.

                    表 4.1 The detailed power consumption distribution at 15.5 Gbps

                                           模块                           Power

                                串行器 & 时钟分频器                1.7 mW
                   发射器（TX）
                                     编码器 & 驱动器                     37.1 mW

                                          解码器                         2.8 mW
                   接收器（RX）
                               并行器 & 时钟分频器               0.7 mW

                                      Total                               42.3 mW




                                                      44
图 4.15 The waveforms of the key signals of the encoder and driver circuit (see 图 4.10)


 表 4.2 The results summary of the design in this chapter in 台湾半导体制造公司（TSMC） 65nm CMOS technology

                工艺                             台湾半导体制造公司（TSMC） 65nm

                   电源                                    1V

                 数据率                               15.5 Gbps

           功耗                             42.3 mW

                                               差分 intermediate
               互连
                                              L=3mm, W=2μm, S=0.5μm
             线路端接                           Capacitive

           工作频率                             15.5 GHz

                  信令                                三电平




                                                 45
4.3 流片
     The design in this chapter was prepared for tape-out in June 2014, in 联华电子股份有限公司（UMC） 0.13μm CMOS
technology. First, the differences between the two technologies are shown. Second, the layouts
are presented and discussed. Third, the testing methodology and the full system integration is
explained. And finally, the post layout simulations are presented.




              图 4.16 The waveforms of the signals of the decoder circuit (see 图 4.12)




                                                        46
图 4.17 The eye diagrams of the 三电平 signals at the front-end of both the 发射器（TX） and 接收器（RX）, and the extracted data
and clock signals

   4.3.1 设计移植
      As mentioned, the intended tape-out is in 联华电子股份有限公司（UMC） 0.13μm, and not in 台湾半导体制造公司（TSMC） 65nm as designed.
So, the first step is to port the full design and do the required changes.

     4.3.1.1 工作频率
      First of all, the expected working frequency depends on how much the 联华电子股份有限公司（UMC） 0.13μm is
slower than the 台湾半导体制造公司（TSMC） 65nm. To answer this question, the metric 四倍扇出（FO4） is used. 四倍扇出（FO4）: Fan-out-of-
four, it is a technology delay metric, is the delay of an inverter, driven by an inverter 4x smaller
than itself, and driving an inverter 4x larger than itself. The simulated 四倍扇出（FO4） of 台湾半导体制造公司（TSMC） 65nm is
14.57ps, while the one of 联华电子股份有限公司（UMC） 0.13μm is 38.875ps. Therefore, the expected data rate will be
2.67 time slower than the 15.5Gbps achieved in 台湾半导体制造公司（TSMC） 65nm, which equals 5.8Gbps. The achieved




                                                          47
data rate in the schematic level in 联华电子股份有限公司（UMC） 0.13μm was actually 6.7Gbps with power consumption
of 82.6mW.

     4.3.1.2 所做的更改
      In these high speed designs, most of the transistors used are low-threshold transistors.
However, in 台湾半导体制造公司（TSMC） 65nm, the leakage in these transistors was considerable, hence the use of
typical transistors, and even high-threshold inverters in the parts working at lower frequencies
was essential. Regarding the 联华电子股份有限公司（UMC） 0.13μm, the leakage was nearly neglected, and the use of
typical transistors when possible was performed only to save the power consumption and has
nothing to do with leakage. This technology does not even possess a high-threshold transistor in
the first place since leakage is not an issue.

      The mobility ratio between the NMOS and PMOS, is what define the sizing ratio between
the two MOS to match the 下拉网络（PDN） and 上拉网络（PUN） of any circuit. In 台湾半导体制造公司（TSMC） 65nm, this ratio was
approximately ‘2’, but in 联华电子股份有限公司（UMC） 0.13μm, it is approximately 3. This resulted in higher power
consumption due to the increment in the capacitances, and higher area.

      Regarding the interconnect, the same dimensions were used. However, the line parameters
and parasitics changed. The new line characteristics are shown in 图 4.18.

      So, to summarize, the new design is working in the schematic level at 6.7Gbps. The input
parallel 8-bit are at 0.8375GHz, the four phases of the clk/2 are at 6.7GHz. The clock divider
produces three frequencies: 3.35, 1.675, and 0.8375GHz




                  图 4.18 The TL charactertics of the interconnect used in 联华电子股份有限公司（UMC） 0.13μm




                                                       48
  4.3.2 版图
     This section shows the layout of the different parts of the design with few notes on each
block. The full system integration is in next section.

     4.3.2.1 发射器
     The layout of the serializer (see 图 4.6) is shown in 图 4.19. The left half is the first
stage, the right half contains the third stage in the middle and the second stage above and below.




                                 图 4.19 The layout of the serializer

     The layout of the clock divider is shown in 图 4.20. It is the part of the clock divider
responsible of producing the clocks for the serializer, the other part producing the four phases of
the clk/2 signals are layouted with the encoder and driver. It consists of three consecutive divie-
by-two units which was illustrated in 图 4.8.

     The layout of the encoder and driver circuit (see 图 4.10) is shown in 图 4.21. The
symmetry when routing the four phases of the clk/2 is very critical. The different parts are



                                                      49
detailed: the clock divider to provide the four phase and their strong buffers to be able to control
the very large sized front-end driver. Then the synchronization parts for both the clock and the
data. Then The 传输门（TG） inverters for driving, and finally the 传输门（TG） 多路复用器（MUX）es for driving the line.

     The layout of the transmitter (see 图 4.1) is shown in 图 4.22. The different parts
are identified: The serializer, clock divider and the encoder and driver circuits. Also, the clock
buffer is for the very high speed clock (6.7*2=13.4GHz). As mentioned in section 4.1.4, a
minimum input capacitance is used for the very high speed clock.




                                图 4.20 The layout of the clock divider




                          图 4.21 The layout of the encoder and driver circuit



                                                       50
                                图 4.22 The layout of the transmitter

     4.3.2.2 互连
     The differential interconnect with its ground shield is illustrated in 图 4.18. Its layout is
shown in 图 4.23.

     4.3.2.3 接收器
     The layout of the deserializer (see 图 4.14) is shown in 图 4.24. The layout’s outline
is similar to the schematic, the three stages are very clear.




                                                      51
     The layout of the decoder (see 图 4.12) is shown in 图 4.25. The different parts are
identified starting from the front-end: the high-threshold inverters and the following buffers, the
phase detector, the SR latch, the NAND gate and the clock buffer.




                               图 4.23 The layout of the interconnect




                               图 4.24 The layout of the deserializer




                                                     52
                                 图 4.25 The layout of the decoder

     The layout of the receiver (see 图 4.1) is shown in 图 4.26. The existence of an empty
space is inevitable for the sake of minimizing the interconnections length. This space’s area is
quite negligible to the full design area when adding the testing circuitry and the interconnect.




                                                     53
                                  图 4.26 The layout of the receiver

  4.3.3 测试与集成
     In section 4.1.4, the methodology of checking the functionality of the system during
simulations was discussed. This section discussed the methodology of checking the functionality
after tape-out. Also the chip integration is discussed in this section.

     4.3.3.1 测试电路
     The block diagram summarizing the testing circuitry is illustrated in 图 4.27. The chip
needs only 5 digital I/O pins: 4 inputs: IN, 数据/Ctrl, Low Speed Clk, and RESET, and a single ‘OUT’
output pin. The testing methodology is that since the SerDes（串行器/并行器） is working at very high frequency,
it will be simpler, and much more robust to not interact with this speed with off-chip. So, a kind
of ‘scan chain’ or ‘self-test’ mechanism is implemented. A 数控振荡器（DCO） will produce the system clock




                                                      54
which is of a very high frequency. An on-chip digital circuit will represent the interface circuitry
with the off-chip domain. A control register will contain the bits determining the function of the
circuit. There will be a single input signal ‘IN’, and to determine whether it is data or a change to
the control bits, another input ‘数据/Ctrl’ is used. These inputs work at a low speed, which is the
frequency of the third input ‘Low Speed Clk’. The digital circuit has two main modes whether to
setup or to test, this is determined by a key bit in the control register, which is ‘Setup/Test’. First
mode is setup: a long series of binary data is fed from external and stored in a serial manner in
the i/p register bank. This storing uses the low speed clock, which is determined by the
multiplexer controlled by the setup/test bit. After the setup is finished, the control bits are
changed externally to switch to the second mode, test. In this mode the register bank works at
the high speed clock, this is actual system byte speed (data rate/8) generated by the 数控振荡器（DCO）. It acts
as a parallel shift register to feed the i/p of the SerDes（串行器/并行器） system. The SerDes（串行器/并行器） now runs normally at
its very high speed, and the o/p bytes are stored in the o/p parallel shift register. Then the sytem
goes to setup mode again for reading. The o/p are read at the low speed clock in a serial manner.
The transmitted and received data are saved and compared off-chip to check the functionality.
Regarding the frequency of operation, the 数控振荡器（DCO） provides a wide range of frequencies. The 4 bits
of frequency select represents a part of the control register, off-chip controls can change the
system frequency. The on-chip digital circuitry contains a frequency counter to report this
frequency count to the control register so that it can be read off-chip.

     4.3.3.2 The Testing layout
      First, the 数控振荡器（DCO） circuit which provides 16 different frequency according to frequency select
bits. The layout of 数控振荡器（DCO） is shown in 图 4.28. Second, the layout of the digital testing circuitry
was generated using the automatic place and route tool ‘SOC Encounter’ in Cadence. The layout
is shown in 图 4.29.

     4.3.3.3 芯片集成
      The block diagram of the full integrated system is shown in 图 4.30. Another small digital
part is a thermometer decoder used for the interface between the frequency select bits and the
programmable 数控振荡器（DCO）. The layout of the full system integrated is shown in 图 4.31. All the




                                                     55
different parts are shown: the transmitter, the receiver, the interconnect, the 数控振荡器（DCO）, the digital
circuitr, and the thermometer decoder.


                                             OUT



                                                                                                         Low
                                                                                              数据/
                                                                                       IN               Speed   RESET    OUT
                                                                                               Ctrl
                         数据/Ctrl                                                                        Clk




    IN                           数据 and Control registers


                   Setup/
                    Test

                                           i/p
       Low                               Register
     Speed Clk                            Bank                                                                                 Setup/
                    多路复用器（MUX）                                                                                     o/p
       High                                                                                                                     Test
     Speed Clk                                                                                            Register
                                                                                                           Bank
                                                              8                        8
                                                                     数据       数据
                 Programmable      Sys Clk
                  free running                                       Clk        Clk
                      数控振荡器（DCO）
                                                                           SerDes（串行器/并行器）
                                                                           系统
                 Freq.
                  Sel    4                                                                    Low
                                                                                            Speed Clk            多路复用器（MUX）

                                                                                              High
                                                              频率                     Speed Clk
                       Low                                      Value
                     Speed Clk                 频率                                                        Setup/
                                                              8                                                  Test
                                                Counter
                   Setup/Test


                         图 4.27 The block diagram of the chip testing methodology




                                               图 4.28 The layout of the 数控振荡器（DCO）




                                                                     56
                            图 4.29 The layout of the digital testing circuitry

4.3.1 后端版图仿真
     This section shows the post layout simulation results of the system. The system functions
typically up to 4.7Gbps with a power consumption of 85.8mW. 图 4.32 shows the waveforms
of the signals of the decoder circuit discussed in section 4.2.2.1 (see 图 4.12). There are the
received 三电平 signal, A and B signals, QA and QB signals, and the extracted data and clock signals.
图 4.33 shows the waveforms of the key signals of the encoder and driver circuit discussed in
section 4.2.1.3 (see 图 4.10). There are the signals driving the multiplexers: the data signal,
and two phases of the clock at 0° and 90°, also the generated 三电平 signal is shown. 图 4.34
shows the eye diagrams of the 三电平 signals at the front-end of both the transmitter and the
receiver, and the eye diagrams of the extracted data and clock signals. 表 4.3 shows the area
distribution of the different parts of the design. A summary of this design results is summarized
in 表 4.4.


                                                         57
      Thermometer
        解码器                                                             OUT
              30                                                        Reset


          /
                                                                      数据/Ctrl
          数控振荡器（DCO）                                                      Low-Speed Clk
                                                                            IN
                                 4
                                 /                                            数据 Out
                   Clk/16=D.Rate/8           Testing
                    8/                       电路ry
                                                                   Clk/16=D.Rate/8




数据 IN


                              TL_in                                 TL_out               8
                发射器（TX）            TL_in
                                                  TL                TL_out
                                                                                  接收器（RX）     /




               Clk=2*D.Rate




              图 4.30 The block diagram of the full system integrated




                                             58
图 4.31 The layout of the full system integrated




                           59
图 4.32 The post layout simulated waveforms of the signals in the decoder circuit (see 图 4.12)

                     表 4.3 The area distribution of the different parts of the design

                            模块                                              Area

                                串行器                      0.0018 mm2
         发射器（TX）                   时钟分频器                     0.0012 mm2              0.036 mm2
                           编码器 & 驱动器                      0.023 mm2
                                 解码器                        0.0009 mm2
         接收器（RX）                   时钟分频器                     0.0012 mm2              0.006 mm2
                               并行器                      0.002 mm2
                                   数控振荡器（DCO）                          0.0071 mm2
      Testing               Digital 电路ry                    0.137 mm2                   -
                        Thermometer 解码器                    0.00038 mm2
                        互连                                        0.019 mm2
              Total (Full 系统 Integrated)                                0.28 mm2




                                                     60
图 4.33 The post layout simulated waveforms of the signals in the encoder and driver circuit (see 图 4.10)

               表 4.4 The post layout results summary of the design in 联华电子股份有限公司（UMC） 0.13μm CMOS

                       工艺                            联华电子股份有限公司（UMC） 0.13μm

                          电源                                  1.2 V

                        数据率                               4.7 Gbps

                  功耗                             85.8 mW

                      Area (发射器（TX）+接收器（RX）)                             0.037 mm2

                                                      差分 intermediate
                      互连
                                                     L=3mm, W=2μm, S=0.5μm
                    线路端接                           Capacitive

                  工作频率                              4.7 GHz

                         信令                               三电平




                                                          61
图 4.34 The post layout eye diagrams of the 三电平 signals at the front-end of both the 发射器（TX） and 接收器（RX）, and the
extracted data and clock signals

4.4 设计总结
      In this chapter, the first design for an on-chip serial communication link was proposed and
explained. The design was simulated using 台湾半导体制造公司（TSMC） 65nm CMOS technology, then it was prepared
for tape-out using 联华电子股份有限公司（UMC） 0.13μm CMOS technology. The design presented a variation tolerant
driving technique for the all-digital system using the 三电平 signaling technique in [15]. The
advantages and problems solved are as follows:

        The proposed driver works in half the frequency of the previous designs. The system’s
         clock is at the data rate frequency. This totally relaxes the design and increases the
         robustness.
        The proposed driver generates the third level without the need of an additional supply
         driver. This eliminates a lot of integration problems when trying to route this additional



                                                         62
      supply to all the modules when using this design as a building cell for network in
      multicore chips.
     All the high speed signals used in the driver circuit are perfectly synchronized. Many
      dummies and redundant cells were added to guarantee this synchronization. This is a
      main factor for making such design a variation tolerant.
     The third level generated is not fixed at VDD/2, it moves with 工艺、电源与温度（PVT） corners. However, the
      detection circuit also moves with 工艺、电源与温度（PVT） corners. These variations follow the same flow,
      and they compensate each other to further increase the system’s robustness.
     Extracting both the clock and data from the same signal guarantee the perfect
      synchronization at the receiver for successful deserialization.
     The used 三电平 signaling scheme has proven effectiveness due to its jitter insensitivity,
      dc-constant level, and concentrated spectrum in the saturation region of the TL
      characteristics.
     The driver circuit achieves a source matching to the TL. This results in the increment of
      the voltage swing at the receiver’s front-end.
     The simple construction of the whole system, without any complex power hungry blocks,
      is what makes this design a perfect choice when building full on-chip inter-core network
      for many-core applications.
     The system is robust against duty cycle variations since it only affects the phase
      mismatch between the four phases of the clocks. The duty cycle of the system clocks are
      only dependent on a single edge of the input very high speed clock.

    Nevertheless, there are some issues with the design summarized as follows:

     The use of a 三电平 signal reduces the eye opening of the received signals, due to dividing
      the allowed swing to two regions.
     It is true that the system’s clock equals to the achieved data rate. However, the needed
      four phases of that clock needs a clock of double the frequency to generate such phases.
      This makes the design of the 数控振荡器（DCO） tougher, and also the clock divider.




                                                 63
        Using four phases of the clock adds to the susceptance to variations, and it is one of the
         bottle necks of the design to increase speed.
        The phase detector circuit is too critical, it represents a bottle neck at the receiver.
        The edge matching circuit is not effective, the clocks and their inverse have a
         considerable mismatch.
        In the clock divider, each clock divided is some way independent from its source clock,
         this may cause some serious synchronization problem.

     表 4.5 summarizes all the obtained results of this design, including simulations and tape-
out results in both technology kits.

                             表 4.5 The results summary of the first design


                           First 原理图               Ported 原理图                后端正图

    工艺               台湾半导体制造公司（TSMC） 65nm                                   联华电子股份有限公司（UMC） 0.13μm

        电源                    1V                                             1.2 V

         四倍扇出（FO4）                   14.57 ps                                     38.875 ps

     数据率                15.5 Gbps                       6.7 Gbps                    4.7 Gbps
      Power
                              42.3 mW                         82.6 mW                     85.8 mW
   Consumption
   Area (发射器（TX）+接收器（RX）)                    -                               -                     0.037 mm2

                      差分 intermediate                   差分 intermediate
   互连
                     L=3mm, W=2μm, S=0.5μm                       L=3mm, W=2μm, S=0.5μm
        Line
                              Capacitive                                   Capacitive
    Termination
      Working
                               15.5 GHz                        6.7 GHz                    4.7 GHz
     频率
     信令                  三电平                                      三电平




                                                       64
                                   5 SECOND DESIGN

      As previously mentioned, this thesis contains two different designed systems for on-chip
SerDes（串行器/并行器） communication. The second design in presented in this chapter, and a paper containing
the design and simulation results will be sent to the next relevant conference. The paper title will
be “A 24 Gbps SerDes（串行器/并行器） Transceiver for On-芯片 Networks Using a New Half-数据-Rate Self-Timed
三电平 信令 Scheme” by Ramy N. Tadros, Abdelrahman H. Elsayed, Maged Ghoneima, and
Yehea Ismail. As will be presented in this chapter, this transceiver was layouted and prepared for
tape-out in 全球晶圆代工厂（GF） 65nm CMOS technology in August 2014. When the chip will return in September
2014 as expected, this transceiver results will be summarized in a journal paper.

      This chapter construction is as follows: First, the whole system overview section, which
contains the information about the system architecture, the used signaling technique, and the
interconnect. Second, the circuits’ architecture of the different blocks of the transmitter and the
receiver circuits. This part explains in detail all the proposed circuits in the encoder and decoder,
and also contains the simulation results of this system in the schematic level. Third, the tape-out
part, which presents the layout of the system and the post layout simulation results. Finally, the
last part will summarize all the results of this design and discuss the pros and cons of using such
transceiver in multicore chips.

5.1 整体系统概述
      This system introduce a SerDes（串行器/并行器） transceiver design of on-chip inter-core communicaton
needs. The design uses a proposed almost-differential self-timed 三电平 signaling scheme, which
works using a frequency of half data rate, which relaxes the design. Also, the third voltage level
is created without the need for an external VDD/2 supply source, which is very advantageous as
explained in section 3.2.1. Moreover, a 三电平 inverter is proposed for the use in the front-end
of both the transmitter and the receiver. The transceiver is designed for a 5mm long lossy on-
chip differential interconnect in 全球晶圆代工厂（GF） 65nm CMOS technology. It achieves a data rate of 24Gbps
which is 20% faster than the fastest reported on-chip serial transceiver. This chapter will discuss
this design in details.



                                                    65
      The following three sections will discuss the system’s architecture, the signaling scheme
and the interconnect used. Regarding the test bench and how to check the system’s functionality,
it uses the same method described in section 4.1.4.

  5.1.1 系统’s 架构
     The block diagram of the whole system is shown in 图 5.1. The transmitter has two
inputs: the parallel 8-bits at 3 Gbps and the 12 GHz clock which can be generated from a free
running 数控振荡器（DCO）, as the system is totally jitter insensitive. The clock divider provides two clocks at 6,
and 12 GHz which are needed to serialize the 8-bit into two streams at 12 Gbps: the “data-” and
“data+”, which together represents a series symbol as will be discussed in next section. The
encoder and driver block generates the A and B signals, and provides a sufficient current to drive
the line. The line is a differential intermediate interconnect whose length is 5mm, the width of
each line is 5μm with lateral spacing of 0.5μm. The line is shielded horizontally and vertically by
ground strips. Regarding the 接收器（RX）, the decoder extracts both the 24 Gbps serial data and the 12
GHz clock. This is the only part working at the data rate speed itself. The same clock divider used
in the 发射器（TX） is used to provide the needed clocks to generate the parallel 8-bit signals as an output
besides the extracted clock.

  5.1.2 信号传输技术
     As discussed in the previous two chapters, mainly in section 3.2.2, the 三电平 signaling
technique presented in [15] (see 图 3.5 or 图 4.2). And it was used in both [13] and the
work in the previous chapter. Its advantages were the embedding of the data and clock which
results in the jitter insensitivity, the constant dc-level, and the reduction of the dispersion, and
the intersymbol interference as a result of its shifted power spectrum. The main drawback of that
scheme was its need for a clock frequency equal to twice the data rate, which is also the same
frequency of the signal transmitted on the interconnect. The design in the previous chapter used
the same signaling technique but with a different driving technique that enabled the use of a
frequency equal to the data rate, but the transmitted signal stayed at the double data rate
frequency. However, that design needed four phases of that clock and it used a very high speed
clock of double data rate frequency to produce these phases.



                                                    66
                          D5

                          D7
                          D3

                          D6
                          D0
                          D1
                          D2

                          D4
                                                                              数控振荡器（DCO）
                                                     clk/2
                                                           时钟
                                                    clk/4 Divider
                            串行器                                 clk



                                           数据 -            编码器
                                                             & 驱动器
                          发射器（TX）               数据 +




                                                                      A_in
                                                                               B_in
                                                                      A_out

                                                                               B_out
                         接收器（RX）            Serial 数据
                                                             解码器


                                                     clk/2
                                                           时钟
                                                    clk/4 Divider
                            并行器                                      clk
                          D5
                          D3

                          D6
                          D0
                          D1
                          D2

                          D4


                          D7




                         图 5.1 The block diagram of the whole SerDes（串行器/并行器） system

      The proposed scheme, in this chapter, solves both of those issues: it only uses a frequency
of half the data rate, and the signal transmitted is also at half the data rate frequency. This totally
relaxes the design of the whole transceiver. 图 5.2 shows the proposed scheme. It is a 2-bit
symbol-based scheme. The use of 2 signals: A & B, is necessary for making the signaling self-
timed. Whenever either signal is quiet for a clock cycle, the other one has an edge for clock
extraction. It should be noted that signals A and B are almost differential signals, but not fully.




                                                        67
                            clk

                                      “00”      “01”        “10”     “11”

                           数据

                           VDD
                         ½VDD     A
                             0

                          VDD
                         ½VDD
                           0
                                  B
                    图 5.2 The new 三电平 signaling scheme presente in this design

     So the advantages of the proposed scheme in 图 5.2 is the possibility of achieving very
high data rates without adding any complexities to the design. The transceiver achieves a data
rate of 24 Gbps, while the circuits are only working at 12 GHz. 图 5.3(c) shows the spectrum
of the proposed scheme. The spectrum of the conventional 两电平 signaling, and the spectrum
of the scheme used in the first design are shown in 图 5.3(a) and (b) respectively. As
mentioned in section 3.2.2, the conventional scheme has a wide spectrum, which results in a
significant distortion at the 接收器（RX）. The 三电平 scheme presented in [15] and used in the previous
design, solved this problem by encoding: the removal of dc components along with shifting the
spectrum to be concentrated at high frequencies. This reduced the distortion and enabled
working at high frequencies. The proposed scheme removes some of the dc components, and
shifts the spectrum to a certain degree. However, the increased distortion is amended by
lowering the frequency of the transmitted signal. The final result of this compromise achieves
considerably higher data rates.




                                                       68
图 5.3 The power spectrum of a random bit stream using (a) the conventional 两电平 scheme at 24 Gbps, (b) the
scheme presented in [15] at 12 Gbps, and (c) the proposed scheme at 24 Gbps.

   5.1.3 互连
      The interconnect used is shown in 图 5.4. It is the same architecture used in the first
design. It is an intermediate line with width of 5μm and spacing 0.5μm, it is 5mm long. The
meaning of the characteristics shown in figure was explained in section 4.1.4.

5.2 收发器
      In this section, the circuit’s architecture of all the blocks are described in details. Also, the
simulation results are presented.




                                                          69
  5.2.1 发射器
     As described in 图 5.1, the transmitter has two inputs: the parallel 8-bits at 3 Gbps and
the 12 GHz clock from the 数控振荡器（DCO）, and the clock divider which provides two clocks at 6, and 12 GHz
which are needed to serialize the 8-bit into two streams at 12 Gbps: the “data-” and “data+”,
which together represents what 图 5.2 considered a series symbol. The encoder and driver
block generates the A and B signals, and provides a sufficient current to drive the line.




                              图 5.4 The used interconnect characteristics

     5.2.1.1 串行器
     The serializer used in this system has the same architecture used in the previous design.
However, it consists of only two stages instead of three, since it produces two data signals at half
the data rate each. The block diagram of the serializer is shown in 图 5.5. Same as previous
design, the first stage is formed by typical transistors to decrease the leakage, and the following
stage uses low-threshold transistors to enhance the speed. ‘DET触发器（FF）’ blocks are the double edge-
triggered 触发器（FF）s discussed in section 4.2.1.1 (see 图 4.7).

     5.2.1.2 时钟分频器
     The block diagram of the used divide-by-two unit is shown in 图 5.6. The clock divider
consists of two units to obtain clk/4. This clock divider differs from the one used in the previous
design in the way it reduces the mismatches between the clock signal and its inverse. One of the
drawbacks of the previous design was the use of the edge matching circuit (see 图 4.9), which
was not quite effective and accurate in the mismatch reduction. The simple substitute to this
method, is the use of 触发器（FF）s working at the clock frequency needed to be divided. This simple



                                                       70
method could not be used in previous design because of the high frequency that needs to be
divided. For instance, to achieve 15.5Gbps, a clock of 31GHz was needed to be divide. While in
this design, in order to achieve the 24Gbps, a clock of only 12GHz needs to be divided. Also the
independency problem between the divided clock and the clock resulting from the division is
solved this way.

     5.2.1.3 编码器和驱动器电路
      The block diagram of the encoder and driver is shown in 图 5.7. From an abstract point
of view, the data signals are used to generate some auxiliary signals. These auxiliary signals
generate the 三电平 signals ‘A’ and ‘B’ using special multiplexers (shown in 图 5.8). Then 3-
level inverters are used to drive the line. The following part will explain the process of generating
the ‘A’ signal only, and the generation of ‘B’ follows the same idea. For the 三电平 signals, the
levels are ‘low’, ‘V/2’, and ‘high’.

                             D0   DL
                                   DET触发器（FF）
                             D4   DH
                                           TYP




                             D2   DL                      DL
                                   DET触发器（FF）                     DET触发器（FF）        数据-
                             D6   DH                      DH
                                           TYP                     LVT




                             D1   DL                      DL

                                   DET触发器（FF）                     DET触发器（FF）        数据+
                             D5   DH                      DH
                                           TYP                      LVT




                             D3   DL
                                   DET触发器（FF）
                             D7   DH
                                           TYP




                                       Clk/4                   Clk/2
                           图 5.5 The block diagram of the two-stage serializer



                                                        71
                                                                 触发器（FF）                Clk/2 (0°)


                       触发器（FF）
                                                                 触发器（FF）              Clk/2 (180°)
                        Clk
                                    Divide-by-two Unit            Clk


               图 5.6 The block diagram of the divide-by-two unit used in the clock divider


     From the scheme depicted in 图 5.2, it can be noticed that when the clock is low, ‘A’
represents the data itself, i.e, the first half of the symbol. So the first path of the C2MOS
multiplexer will produce the inverted data (as the signals are followed by another inverter as will
be discussed). The other half does equal V/2 for “00” and “10”, high for “01”, and low for “11”.
Following a simple logic table implementation, two auxiliary signals are produced, both of these
signals are high for “01”, low for “11” and one of them is low while the other is high for “00” and
“10”. The other two C2MOS paths are both active simultaneously, when the clock is high. If the
two signals are equal, these two paths will conduct the inverse normally, and if they are different,
a current path is created and the supply voltage is divided to introduce the third level. The clock
also passes through an always-enabled 触发器 to ensure perfect synchronization.

     The proposed 三电平 inverter is depicted in 图 5.9. First, MP1 and MN1 form a
conventional CMOS 两电平 inverter. R1 and R2 form a voltage divider to provide a continuous
current flow to the output. MN2 and MP2 represent a feedback buffer, but this buffer does not
provide a full swing since it uses an NMOS as a pull-up device instead of a PMOS and vice versa.
As ‘A’ and ‘B’ signals are not dc-constant signals, then they can drift or ramp to the high or low
levels. However, the continuous current flow provided by the resistors reduces the swing
intentionally, prevents the output signal from drifting, and provides a reference for the third
level. When the input is V/2, MP1 and MN1 are both ON, but due to variations or even some
perturbations in the input signal, either one can get turned O触发器（FF）. That is why the feedback buffer
is used: to maintain the third level at the input as soon as it detects it at the output. This buffer
acts as a self-induced force to prevent either signal from drifting away.



                                                         72
     As it can be noticed, using transistors instead of resistors R1 and R2, can be beneficial from
the point of view of variations dependency. However, the very large sizes needed to achieve the
same driving capability, will add a very large capacitance to the driving node, which will affect
the data rate. Also, this will make the 3rd level very sensitive to any source of variations, beside
the fact that the signaling has dc components, this actually will cause serious problems to the TL
signals shape and the ability to detect them at the 接收器（RX）.


                数据-
                                        触发器（FF）

                _____
                数据+                                                                    A_in
                数据-                   触发器（FF）               多路复用器（MUX）


               数据+
               数据-                    触发器（FF）

                _____
                数据-
                                        触发器（FF）


               数据+                                    1                                B_in
               _____
               数据-                    触发器（FF）               多路复用器（MUX）
                                                        2
              _____                                     3
              数据+
              _____
              数据-                     触发器（FF）




               clk                      触发器（FF）


              ___
              clk                       触发器（FF）

                                Always
                                Enabled

                        图 5.7 The block diagram of the encoder and driver circuit




                                                        73
                                      1                     2             3

                                                                         ___
                                      clk                                clk

                                                                         out
                                      ___
                                      clk                                clk


                                      1                     2             3




       图 5.8 The architecture of the special multiplexers used in the encoder and driver in 图 5.7

                                                                     MN2



                                                  MP1        R1
                                 IN                                      OUT

                                                  MN1           R2




                                                                     MP2

                 图 5.9 The proposed architecture of the 三电平 inverter used in 图 5.7

  5.2.2 接收器
     As described in 图 5.1, the receiver has one input, which is the almost-differential 3-
level signals. And it has two outputs which are the parallel 3GHz 8-bit data, and the extracted
12GHz clock. First, the decoder extracts both the 24 Gbps serial data and the 12 GHz clock. This
is the only part working at the data rate speed itself. The same clock divider used in the 发射器（TX） is used




                                                          74
to provide the needed clocks to generate the parallel 8-bit signals as an output besides the
extracted clock.

     5.2.2.1 解码器
     The block diagram of the decoder is shown in 图 5.10. First, the signals are received by
a 三电平 inverter, as in 图 5.9, with the feedback buffer removed to enhance the swing that
was reduced by the long line’s attenuation. The resistance ratio is skewed to provide high-
threshold, and low-threshold versions of the 三电平 inverters as indicated by the arrows in
图 5.10. NANDing both signals (L1,2 & H1,2), i.e., the signal considering the 三电平 as high, and
the other considering it as low. NANDing again the results produces the clocks. 数据 is obtained
using an SR latch, whose inputs are signals L1 and L2. The simplicity of the decoder enables the
functionality at such a very high frequency.

                   A_out
                                                H1

                                                L1                 N1          Extracted
                                                                                 时钟
                   B_out
                                                H2                 N2

                                                L2

                                                                               Extracted
                                           L1        S SR                        数据
                                           L2        R Latch

                                图 5.10 The block diagram of the decoder

     5.2.2.2 并行器
     It is exactly the same deserializer discussed in section 4.2.2.2 and shown in 图 4.14.

  5.2.3 仿真结果
     This section shows the simulation results of the designed system in 全球晶圆代工厂（GF） 65nm CMOS
technology with a 1.2V supply. The system functions correctly across 工艺、电源与温度（PVT） corners, and can
operate typically up to 24 Gbps. All the waveforms shown were simulated at the typical process
corner at 1.2V and room temperature. 图 5.11 shows the waveforms of the key signals of the


                                                           75
encoder and driver circuit discussed section 5.2.1.3 (see 图 5.75.2.1.3). There are the signals
driving the multiplexer: signal ‘1’: the ̅̅̅̅̅̅̅̅̅
                                         数据 −, the auxiliary signals ‘2’ and ‘3’, and then the clock
and the multiplexer’s output. 图 5.12 shows the waveforms of the signals in the decoder
circuit discussed in section 5.2.2.1 (see 图 5.10). There are the signals: the ‘A’ 信号 arriving
at the 接收器（RX） front-end, the output of the low threshold and high threshold inverters L1, and H1,
signals N1 and N2, then finally the extracted clock and data signals. These waveforms show the
attained 24 Gbps data rate. The total power consumption is 109.6mW at 24 Gbps. A summary of
this design results is summarized in 表 5.1.




图 5.11 仿真 results for the key-signals in the encoder and driver in 图 5.7, in order: signal ‘1’: the
̅̅̅̅̅̅̅̅̅
数据 −, the auxiliary signals ‘2’ and ‘3’, the clock, and the multiplexer output.




                                                            76
         表 5.1 The results summary of the design in this chapter in 全球晶圆代工厂（GF） 65nm CMOS technology

                     工艺                              全球晶圆代工厂（GF） 65nm

                        电源                                 1.2 V

                      数据率                               24 Gbps

                功耗                           109.6 mW

                                                    差分 intermediate
                    互连
                                                   L=5mm, W=5μm, S=0.5μm
                  线路端接                          Capacitive

                工作频率                             12 GHz

                      信令                               三电平



5.3 流片
      The design in this chapter was prepared for tape-out in August 2014, in 全球晶圆代工厂（GF） 65nm low-power
CMOS technology. First, the differences between the generic and low-power kits are discussed.
Second, the layouts are presented and discussed. Third, the testing methodology and the full
system integration is explained. And finally, the post layout simulations are presented.

  5.3.1 设计移植
      As mentioned, the intended tape-out is in the low-power kit of 全球晶圆代工厂（GF） 65nm CMOS, and not in
the generic kit as designed. So, the first step is to port the full design and do the required changes.

     5.3.1.1 工作频率
      As discussed in section 4.3.1.1, the metric 四倍扇出（FO4） is used to compare between the speed of
the two kits’ flavors to determine the working speed. The simulated 四倍扇出（FO4） of Generic 全球晶圆代工厂（GF） 65nm is
13.74ps, while the one of 低功耗（LP） 全球晶圆代工厂（GF） 65nm is 24.87ps. Therefore, the expected data rate will be 1.81
times slower than the 24Gbps achieved using the generic kit, which equals 13.3Gbps. The
achieved data rate in the schematic level in the 低功耗（LP） 全球晶圆代工厂（GF） 65nm was actually 11.3Gbps with power
consumption of 54.2mW.


                                                       77
图 5.12 The 仿真 results for the signals in the decoder shown in 图 5.10, in order: The ‘A’ 信号 arriving
at the 接收器（RX） front-end, the output of the low threshold and high threshold inverters L1, and H1, signals N1 and N2, then
finally the extracted clock and data signals.

      5.3.1.2 The Changes Made
       First, the leakage issues, actually there were not any considerable leakage issues in both
kits. Therefore, low-threshold transistors are used in all the parts working at the maximum
frequency, and typical transistors in any part working at lower frequency.

       Second, the mobility ratio between PMOS and NMOS to match the 下拉网络（PDN） and 上拉网络（PUN） of the
circuits. It was the same ration for both flavors, which is 2.2.

       Third, the interconnect used was changed. The dimensions are usually chosen to enhance
the performance of the overall system. The new line characteristics are shown in 图 5.13.




                                                              78
     So, to summarize, the new design is working in the schematic level at 11.3Gbps. The input
parallel bits are at 1.4125GHz, the 数控振荡器（DCO） input clock is at 5.65GHz. The clock divider produces two
clocks at frequency of 2.825 and 1.4125 GHz.




                          图 5.13 The used interconnect and its characteristics

  5.3.2 版图
     This section shows the layout of the different parts of the design with few notes on each
block. The full system integration is in next section.

     5.3.2.1 发射器
     The layout of the serializer (see 图 5.5) is shown in 图 5.14. It is only two stages to
produces the two streams of data.

     The layout of the clock divider is shown in 图 5.15. It is formed by two stages of the
divide-by-two unit illustrated in 图 5.6.

     The layout of the encoder and driver circuit (see 图 5.7) is shown in 图 5.16. The
different parts are shown: first, a part for buffering and synchronizing the output from the
serializer, then the logic gates, the synchronization 触发器（FF）s. Then the large sized parts are the driving
multiplexers and the explained 三电平 inverters. Perfect symmetry was targeted to perfectly
synchronize both the 三电平 signals A and B.

     The layout of the transmitter (see 图 5.1) is shown in 图 5.17. The different parts
are identified: The serializer, the clock divider, and the encoder and driver circuit. Also, the clock
buffer for the clock coming from the 数控振荡器（DCO）. As discussed in section 4.1.4, a minimum input
capacitance is used for the very high speed clock.


                                                        79
 图 5.14 The layout of the serializer




图 5.15 The layout of the clock divider




                       80
                         图 5.16 The layout of the encoder and driver circuit

     5.3.2.2 互连
     The differential interconnect with its ground shield is illustrated in 图 5.13. Its layout is
shown in 图 5.19. The line is layouted in a snake form in order to achieve a reasonable aspect
ratio for the whole system.

5.3.2.1 接收器
     The layout of the deserializer (see 图 4.14) is shown in 图 5.18. The layout outlook
is exactly the same as the schematic. The layout of the decoder (see 图 5.10) is shown in
图 5.20. The different parts are identified: First, the front-end 三电平 inverters, then the
buffers and NAND gates, followed by the clock and data paths.

     The layout of the receiver (see 图 5.1) is shown in 图 5.21. The different parts are
identified: The decoder, the clock divider and the deserializer.




                                                      81
图 5.17 The layout of the transmitter




图 5.18 The layout of the deserializer



                      82
图 5.19 The layout of the interconnect




  图 5.20 The layout of the decoder




                      83
                                图 5.21 The layout of the receiver

  5.3.3 测试与集成
     The same testing procedure and methodology discussed in section 4.3.3.1 is used in this
design. The layout of the used 数控振荡器（DCO） is shown in 图 5.22. This 数控振荡器（DCO） generates 16 different
frequency according to frequency select bits. The layout of the digital testing circuit was
generated using the automatic place and route tool ‘IC Compiler’ in Synopsis. The layout is shown
in 图 5.23.




                                                    84
         图 5.22 The layout of the 数控振荡器（DCO）




图 5.23 The layout of the digital testing circuitry




                             85
     The block diagram of the full integrated system is shown in 图 5.24. The differences
between this block diagram and the one in 图 4.30 for the previous system is the frequency
of the clocks. The 数控振荡器（DCO） in this system generates only a frequency of half the data rate, instead of
a frequency of double the data rate in the system of the previous chapter. The layout of the full
system integrated is shown in 图 5.25.

  5.3.4 后端版图仿真
     This section shows the post layout simulation results of the system. The system functions
typically up to 8.1Gbps with a power consumption of 52.8mW. 图 5.26 shows the waveforms
of the key signals of the encoder and driver circuit discussed in section 5.2.1.3 (see 图 5.7).


               Thermometer
                 解码器                                                               OUT
                         30                                                        Reset
                     /




                                                                                 数据/Ctrl
                   数控振荡器（DCO）                                                        Low-Speed Clk
                                                                                       IN
                                           4
                                           /                                             数据 Out
                              Clk/4=D.Rate/8            Testing
                               8
                               /                        电路ry
                                                                             Clk/4=D.Rate/8



        数据 IN


                                         TL_in                                 TL_out               8
                           发射器（TX）            TL_in
                                                             TL                TL_out
                                                                                             接收器（RX）     /




                          Clk=D.Rate/2




                         图 5.24 The block diagram of the full system integrated




                                                        86
                            图 5.25 The layout of the full system integrated

                                                                ̅̅̅̅̅̅̅̅̅
There are the signals driving the multiplexer: signal ‘1’: the (数据   −), the auxiliary signals ‘2’ and
‘3’, and then the clock and the multiplexer’s output. 图 5.27 shows the waveforms of the
signals of the decoder circuit discussed in section 5.2.2.1 (see 图 5.10). There are the signals:
the ‘A’ 信号 arriving at the 接收器（RX） front-end, the output of the low threshold and high threshold
inverters L1, and H1, signals N1 and N2, then finally the extracted clock and data signals.
图 5.28 shows the eye diagrams of the 三电平 signal ‘A’ at the front-end of both the
transmitter and the receiver, and the eye diagrams of the extracted data and clock signals.
表 5.2 shows the area distribution of the different parts of the design. A summary of this
design results is summarized in 表 5.3.




                                                       87
图 5.26 The post layout simulated waveforms of the key-signals in the encoder and driver in 图 5.7, in order:
signal ‘1’: the ̅̅̅̅̅̅̅̅̅
                数据 −, the auxiliary signals ‘2’ and ‘3’, the clock, and the multiplexer output.

                            表 5.2 The area distribution of the different parts of the design

                                   模块                                              Area
                                       串行器                     0.00055 mm2
                发射器（TX）                   时钟分频器                    0.00018 mm2             0.0103 mm2
                                  编码器 & 驱动器                     0.0083 mm2
                                        解码器                        0.0065 mm2
                接收器（RX）                   时钟分频器                    0.00018 mm2             0.0089 mm2
                                     并行器                     0.00107 mm2
                                          数控振荡器（DCO）                         0.00069 mm2
             Testing               Digital 电路ry                    0.071 mm2                   -
                               Thermometer 解码器                    0.00014 mm2
                               互连                                       0.0209 mm2
                     Total (Full 系统 Integrated)                                0.151 mm2




                                                            88
图 5.27 The post layout simulated waveforms of the signals in the decoder shown in 图 5.10, in order: The
‘A’ 信号 arriving at the 接收器（RX） front-end, the output of the low threshold and high threshold inverters L1, and H1, signals
N1 and N2, then finally the extracted clock and data signals.

                 表 5.3 The post layout results summary of the design in 低功耗（LP） 全球晶圆代工厂（GF） 65nm CMOS

                         工艺                                低功耗（LP） 全球晶圆代工厂（GF） 65nm
                            电源                                    1.2 V
                          数据率                                 8.1 Gbps
                    功耗                               52.8 mW
                        Area (发射器（TX）+接收器（RX）)                               0.019 mm2
                                                          差分 intermediate
                        互连
                                                         L=3mm, W=2μm, S=0.5μm
                      线路端接                         Capacitive
                    工作频率                               4.05 GHz
                           信令                                 三电平




                                                              89
图 5.28 The post eye diagrams of the 三电平 signals (A) at the front-end of both the 发射器（TX） and 接收器（RX）, and the extracted
data and clock signals.

5.4 设计总结
      In this chapter, the second design for on-chip serial communication link was proposed and
explained. The design was simulated using the generic kit of 全球晶圆代工厂（GF） 65nm CMOS technology, then it
was prepared for tape-out using the low-power kit in the same technology. The design presented
a very high speed all-digital system using a new proposed 三电平 signaling technique. The
advantages and problems solved are as follows:

         The proposed system achieves a 24Gbps data rate. This is 20% faster than the fastest
          published on-chip SerDes（串行器/并行器） system.
         The system works on a clock frequency equal to half the data rate. This totally relaxes
          the design and allows the system to achieve such very high data rate.



                                                            90
   The signal transmitted is also of a frequency equal to half the data rate.
   The third level is generated without the need of an external supply source. This
    eliminates a lot of integration problems when trying to route this additional supply to all
    the modules when using this design as a building cell for network in multicore chips.
   The three level signaling technique is embedding both the clock and the data in the same
    signal. Extracting both the clock and data from this signal guarantee the perfect
    synchronization at the receiver for successful deserialization, and makes the full system
    jitter insensitive.
   The introduced three level inverter prevents the 三电平 signals from drifting since they
    are not dc-constant, and maintains the 三电平 itself when it is needed.
   The third level generated is not fixed at VDD/2, it moves with 工艺、电源与温度（PVT） corners. However, the
    detection circuit also moves with 工艺、电源与温度（PVT） corners. These variations follow the same flow,
    and they compensate each other to further increase the system’s robustness.
   All the high speed signals used in the driver circuit are perfectly synchronized. Many
    dummies and redundant cells were added to guarantee this synchronization.
   The clock divider used solves two problems with the previous designs: It eliminates the
    mismatch between the two branches of the output differential clock, and it introduces a
    known dependency between the dividend and the output. This will better synchronize
    the different frequency domains of the system.
   The simple construction of the whole system, without any complex power hungry blocks,
    is what makes this design a perfect choice when building full on-chip inter-core network
    for many-core applications.

Nevertheless, there are some issues with the design summarized as follows:

   Same as the previous design, the use of a 三电平 signal reduces the eye opening of the
    received signals, due to dividing the allowed swing to two regions.
   The signaling technique isn’t dc constant, this is the main drawback of the use of the
    proposed signaling scheme.




                                              91
        The power consumption is quite high. This is the main drawback of the use of the
         proposed three-level inverter. This is due to the dc current in the resistors branch.
        The use of resistors is an issue for any all-digital systems, since it limits the possibility of
         writing such design in an automated way without manual interference.
        It is true that the whole transmitter works at a frequency equal to half the data rate.
         However, the receiver front-end detects the very high speed data signal at its actual data
         rate speed. This part is the bottle neck for increasing the speed of the whole system.
        The use of large width and long interconnect was needed in the design at these very high
         speeds to decreases dispersion.

     表 5.4 summarizes all the obtained results of this design, including simulations and tape-
out results in both design kits.

                            表 5.4 The results summary of the second design


                            First 原理图             Ported 原理图               后端正图

    工艺             Generic 全球晶圆代工厂（GF） 65nm                               低功耗（LP） 全球晶圆代工厂（GF） 65nm

        电源                     1.2 V                                     1.2 V

         四倍扇出（FO4）                   13.74 ps                                    24.87 ps

     数据率                  24 Gbps                      11.3 Gbps                  8.1 Gbps
      Power
                              109.6 mW                       54.2 mW                    52.8 mW
   Consumption
   Area (发射器（TX）+接收器（RX）)                       -                           -                    0.019 mm2

                      差分 intermediate                  差分 intermediate
   互连
                     L=5mm, W=5μm, S=0.5μm                      L=3mm, W=2μm, S=0.5μm
        Line
                              Capacitive                                  Capacitive
    Termination
      Working
                                12 GHz                       5.65 GHz                   4.05 GHz
     频率
     信令                     三电平                                  三电平




                                                       92
                                        6 总结

     This chapter represents the full summary and conclusion for the work in this thesis. The
first section summarizes the motivation and the achievements of this work. Then a comparison
between this work and other designs is shown. After that, the conclusions are presented. And
finally, the possible future work is discussed.

6.1 小结
     The VLSI industry has chosen parallelism as the solution for increasing the performance
instead of increasing the working frequency due to power issues. A full inter-core network is an
elementary component for designing high performance many-core chips. Parallel
communication is the conventional way to establish these connections. However, due to reverse
scaling, and the exponential increase in the number of parallel lines, a serial approach seems the
ultimate solution to overcome these increasing area and power problems.

     This thesis introduced two SerDes（串行器/并行器） designs for on-chip inter-core communication needs.
First, a literature review explaining several designs was done in chapter 3. This review explained
a conventional implementation in [12], the work in [13] which represented the starting point for
the work in this thesis, and the fastest on-chip SerDes（串行器/并行器） system previously published [14]. Then the
first design was presented in chapter 4, and the second design in chapter 5.

     The first design, in chapter 4, presented a new variation tolerant driving technique for an
all-digital SerDes（串行器/并行器） system using the signaling technique presented in [15] and used in [13]. The
design was simulated using 台湾半导体制造公司（TSMC） 65nm CMOS technology and achieved a data rate of 15.5Gbps
with power consumption of 42.3mW. Then it was prepared for tape-out using 联华电子股份有限公司（UMC） 0.13μm
CMOS technology and achieved a data rate of 4.7Gbps with power consumption of 85.8mW. The
block diagram of the whole system was depicted in 图 4.1. The design was summarized in
section 4.4, and results were summarized in 表 4.5. That design had many advantages:
            It worked at half the frequency of the previous design.
            It generated the third level without an additional supply.
            The design was robust against all kinds of variations.


                                                  93
           The clock and data were embedded in the same signal.
           The all-digital system was jitter insensitive.
           The driver benefited from the source matching.
           Simple circuits architecture without any complex power hungry blocks.

     The second design, in chapter 5, presented a new self-timed signaling technique for on-chip
serial communication. The design was simulated using the generic kit of 全球晶圆代工厂（GF） 65nm CMOS
technology, and achieved a very high data rate of 24Gbps with power consumption of 109.6mW.
Then it was prepared for tape-out using the low-power kit of the same technology. And it
achieved a data rate of 8.1Gbps with power consumption of 52.8mW. The block diagram of the
whole system was depicted in 图 5.1. The design was summarized in section 5.4 and, the
results were summarized in 表 5.4. That design has many advantages:
           It achieved a very high data rate.
           It worked on a low frequency clock equal to half the data rate.
           The third level was generated without an additional supply source.
           The three level signaling technique embedded both data and clock.
           The all-digital system was jitter insensitive.
           Simple circuits architecture without any complex power hungry blocks.




                                                   94
6.2 比较
      This section discusses the comparison between the designs in this work and other designs.
The comparison is summarized in 表 6.1. As detailed in sections 3.1.5 and 3.3, the problem
with designs [12] and [14], is that they consider the same clock at 发射器（TX） and 接收器（RX） neglecting the phase
mismatch that may occur due to the clock travelling, and also the designs need some external
digital adjustment to guarantee the synchronization without investigating the possibility of
achieving this calibration automatically on-chip. The first design of this work is very robust,
however, layouting the four phases of the clock represents the main challenge to guarantee
perfect synchronization and achieve higher data rates. Also, the design of the 数控振荡器（DCO） to generate a
frequency of double the data rate is tricky. The second design’s main issue is the very high power
consumption, but it achieves the highest data rate. The designs in [13] and [19] are sensitive to
variations, and require an additional supply. The working frequency in [13] is very high due to the
use of a clock of double the data rate. And the detection is very difficult in [19] due to the very
large dc-component without doing anything to compensate it. The design in [20] is very power
efficient, but it is a pure analog circuit. The use of analog circuits to design a building cell for inter-
core communication is a quite bad designing choice as discussed previously in section 3.1.5.




                                                       95
                  表 6.1 The comparison summary between the designs in this work and other designs

                                                               Park Safwat Hussein Lee     Rhew
                                 This Work       This Work
                                                              (2009) (2011) (2012) (2013) (2012)
                               (First 设计) (第二个设计)
                                                               [12]   [13]   [19]   [20]    [14]
                               台湾半导体制造公司（TSMC）      联华电子股份有限公司（UMC）      G. 全球晶圆代工厂（GF）     低功耗（LP） 全球晶圆代工厂（GF）                    台湾半导体制造公司（TSMC）       台湾半导体制造公司（TSMC）
工艺                     65nm     0.13μm    65nm      65nm
                                                                          0.13μm
                                                                                     65nm       65nm
                                                                                                          65nm       65nm


                                         Post                Post
           State               Sim.
                                        版图
                                                   Sim.
                                                            版图
                                                                           Fab.       Sim.      Sim.       Fab.      Fab.


                                                                                     1V&        1V&
        电源                  1V      1.2 V     1.2 V     1.2 V          1.5 V
                                                                                     0.5V       0.5V
                                                                                                           1V        1.3 V


                               14.57    38.875    13.74     24.87                    14.57      14.57
                四倍扇出（FO4）             ps        ps       ps        ps
                                                                             -
                                                                                      ps         ps
                                                                                                             -         -


                               15.5      4.7       24        8.1            9         12         16        4          20
 数据率                     Gbps     Gbps      Gbps      Gbps           Gbps      Gbps       Gbps      Gbps       Gbps

       Power                   42.3      85.8     109.6      52.8          600        15.5      18.1       0.43      27.2
      (发射器（TX）+接收器（RX）)                  mW        mW        mW        mW            mW         mW        mW         mW        mW

                                        0.037               0.019          0.71                           0.0034    0.0025
Area (发射器（TX）+接收器（RX）)                     -
                                        mm2
                                                     -
                                                            mm2            mm2
                                                                                        -         -
                                                                                                           mm2       mm2
                                                                               Single
                      Diff.    Diff.     Diff.     Diff.     Diff.         Diff.      Diff.                Diff.     Diff.
                                                                               Ended
 互连




                               Inter-  Inter-  Inter-  Inter-  Inter-  Inter-  Inter-
                  Layer                                                                                   Global    Global
                              mediate mediate mediate mediate mediate mediate mediate
                  Width        2 μm     2 μm      5 μm      2 μm           6 μm      1 μm       3 μm      0.5 μm     2 μm

                  Length       3 mm     3 mm      5 mm      3 mm          5.8 mm     3 mm       3 mm      10 mm     10 mm

                  Spacing 0.5 μm        0.5 μm    0.5 μm    0.5 μm         3 μm     0.5 μm     0.5 μm     1 μm      10.8 μm

   Line                                                                                                   Sense
                               Cap.      Cap.      Cap.      Cap.          Res.       Cap.      Res.                 Res.
Termination                                                                                               Amp.

  Working                      15.5      4.7        12       4.05          4.5         24         16        4         10
 频率                     GHz       GHz       GHz       GHz           GHz        GHz        GHz       GHz       GHz


   信令                  三电平   三电平   三电平   三电平       两电平   三电平    三电平    两电平   两电平


                                                                                    Sensitive Sensitive
 Additional                                                               节                      Analog       节
                                 -         -         -         -                     to         to
   Notes                                                                   3.1.5 variations variations 系统         3.3




                                                                     96
6.3 结论
     This thesis discussed the problem of designing an on-chip SerDes（串行器/并行器） link as a building cell for
full inter-core network in multicore chips. It explained the different signaling and interconnects
challenges, and detailed what other researchers have done in literature to overcome these
problems. Achieving a very high data rates, with low power consumption, low area overhead,
with simple circuits for the possibility of converting the design to a digital flow, robust link and
circuits, and reliable signaling are the main goals of any designed system.

     Two all-digital full system designs for on-chip SerDes（串行器/并行器） communication link were presented
for the use as a building cell for a full inter-core network in multicore chips as summarized in
section 6.1. These systems achieved an adequate and competitive performance compared to
other designs in literature as summarized in 表 6.1.

     These systems presented a new signaling technique, and analyzed in details the pros and
cons of using it. The new encoding techniques and new driver circuits were presented, and their
operation was explained. A new architecture for a 三电平 inverter was introduced and analyzed.
Simple decoding methods using some basic digital cells simplified the decoding methodology,
and hence allowed for higher data rates. 分析 of how to benefit from the on-chip
interconnects characteristics, and how to interfere with them was performed.

     To conclude, this thesis presented a good review, identified challenges, in addition to
presenting two new approaches to solve the inter-core communication problem for multi-core
chips.




                                                   97
6.4 未来工作
     To continue the research in this thesis, future work can be done in a several diverse
directions: to check some unresolved issues, to give more insight into the assumptions on which
the thesis was built, or to try to further improve the achievements. Some suggestions are
summarized as follows:

       Give more insight into the interconnects modeling. In this thesis, as discussed in
        section 4.1.4, predictive models were used to define the parameters of the SPICE models
        used. Investigating the TL modeling may lead to more accurate designs and simulations.
        Also, the measurements of the tape-outs will surely give a useful hint about this issue.
       The second design faced some serious dispersion problems. Investigating this issue and
        how to solve it or reduce its effects will lead to a further improvement of speed.
       The proposed 三电平 inverter is power inefficient. Trying to innovate an architecture
        more effective will enhance the entire performance of the design.
       Interfering with the termination types, and trying to benefit from previous ideas in
        communication and electromagnetics fields, since the interconnects act as TLs, and apply
        them into SerDes（串行器/并行器） systems, may be beneficial.
       The length of the interconnect may have a larger effect than expected. Actually, the
        dispersion increases with the length while the 符号间干扰（ISI） decreases. Trying to quantify an
        optimum will represent a good enhancement.
       Although the second design is working on a frequency equal to half the data rate. The
        receiver front-end detects the signals at its actual speed. This part is the bottle neck for
        increasing the data rate. Trying to create a decoding architecture that can extract the
        two data streams at the speed of half data rate will result in a huge leap in performance.




                                                   98
                                      REFERENCES

[1] G. E. Moore, "Cramming more components onto integrated circuits," Electronics, vol. 38,
    no. 8, 1965.

[2] R. Workman, "What is Moore's Law?," 22 March 2013. [Online]. Available:
    http://www.technewsdaily.com/17450-moores-law.html.

[3] N. I. W. Papers, "多核 Programming with NI LabVIEW," 14 June 2013. [Online].
    Available: http://www.ni.com/white-paper/14565/en/.

[4] D. Geer, "芯片 Makers Turn to 多核 Processors," Computer, vol. 38, pp. 11-13, 2005.

[5] R. H. Havemann and J. A. Hutchby, "High-Performance 互连: An Integration
    Overview," Proceedings of the IEEE, vol. 89, no. 5, pp. 586-601, May 2001.

[6] E. O. Hussein, On-芯片 互连 设计 For High Speed SerDes（串行器/并行器） Transceivers, Giza: Nile
    University, 2012.

[7] S. Safwat, SerDes（串行器/并行器） Transceiver 设计 for 多核 Communication, Giza: Nile University,
    2011.

[8] S. Corrigan, "Skew definition and jitter analysis," Analog Applications Journal, Analog and
    Mixed-信号 Products, Texas Instruments Incorporated, pp. 29-32, February 2000.

[9] M. P. Flynn and J. J. Kang, "Global 信令 over Lossy 传输线s," IEEE
    International Conference on Computer-Aided 设计 (ICCAD), pp. 985-992, 2005.

[10] J. J. Kang, J. Y. Park and M. P. Flynn, "Global High-Speed 信令 in Nanometer CMOS,"
     Asian Solid-State 电路s Conference, pp. 393-396, 2005.

[11] E. E.-D. O. Hussein and Y. Ismail, "Optimal interconnect termination for on-chip high speed
     signaling," International Conference on Energy Aware Computing (ICEAC), pp. 1-4, 2011.

[12] J. Park, J. Kang, S. Park and M. P. Flynn, "A 9Gbit/s serial Transceiver for On-芯片 Global
     信令 Over Lossy 传输线s," IEEE Transactions on 电路s And 系统s (TCAS),
     vol. 56, no. 8, pp. 1807-1817, August 2009.




                                                 99
[13] S. Safwat, E. E.-D. Hussein, M. Ghoneima and Y. Ismail, "A 12Gbps All Digital Low Power
     SerDes（串行器/并行器） Transceiver for On-芯片 Networking," 电路s and 系统s (ISCAS), 2011 IEEE
     International Symposium on, pp. 1419 - 1422, May 2011.

[14] H. G. Rhew, J. Park and M. P. Flynn, "A 22Gb/s, 10mm On-芯片 Serial Link over Lossy
     传输线 with 电阻端接," ESSCIRC, pp. 233-236, 2012.

[15] E.-D. Hussein, S. Safwat, M. Ghoneima and Y. Ismail, "A new signaling technique for a low
     power on-chip SerDes（串行器/并行器） transceivers," 2010 International Conference on Energy Aware
     Computing (ICEAC), pp. 1-2, 2010.

[16] A. Tsuchiya, Y. Gotoh, M. Hashimoto and Hidetoshi Onodera, "Performance Limitation of
     On-chip Global 互连 for High-speed 信令," Proceedings of the IEEE 2004
     Custom Integrated 电路s Conference, pp. 489-492, 2004.

[17] Y. Cao, "Predictive 工艺 Model," Nanoscale Integration and Modeling (NIMO) Group,
     Arizona State University, 2012. [Online]. Available: http://ptm.asu.edu/. [Accessed 2013].

[18] T. Sakurai, "Approximation of wiring delay in MOSFET LSI," IEEE Journal of Solid-State
     电路s, vol. 18, no. 4, pp. 418-426, 1983.

[19] E. E.-D. Hussein, S. Safwat, M. Ghoneima and Y. Ismail, "A 16Gbps Low Power Self-Timed
     SerDes（串行器/并行器） Transceiver for Multi-Core Communication," 2012 IEEE International Symposium on
     电路s and 系统s (ISCAS), pp. 1660-1663, 2012.

[20] S.-K. Lee, S.-H. Lee, D. Sylvester and D. Blaauw, "A 95fJ/b current-mode transceiver for
     10mm on-chip interconnect," 2013 IEEE International Solid-State 电路s Conference Digest
     of Technical Papers (ISSCC), pp. 262-263, 2013.




                                                100
