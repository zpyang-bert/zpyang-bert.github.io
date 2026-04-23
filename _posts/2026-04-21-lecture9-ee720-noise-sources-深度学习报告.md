---
layout: post
title:      "lecture9 ee720 noise sources 深度学习报告"
date:       2026-04-21 10:09:59
author:     "Bert"
tags:
  - Fundamentals
  - Lecture
  - Noise
  - SerDes
  - 深度学习
---

ECEN720: High-Speed Links
   Circuits and Systems
       Spring 2023

   Lecture 9: Noise Sources




           Sam Palermo
   Analog & Mixed-Signal Center
       Texas A&M University

![课程封面](/img/serdes/fundamentals/lectures/lecture10_ee720_jitter_深度学习报告/_images/img-000.jpg)
> 🔍 深度说明：
> 【研究背景】这是ECEN720第九讲，主题是Serdes中的噪声源与抖动，噪声和抖动是限制Serdes性能的两个核心因素，决定了链路的最大传输距离和最低误码率。
> 【核心结论】内容覆盖噪声来源（热噪声、闪烁噪声、电源噪声、串扰噪声）、抖动来源（随机抖动RJ、确定性抖动DJ）、抖动的分解与测量、抖动对链路性能的影响、低噪声低抖动电路设计技术，是Serdes性能优化的核心参考。
> 【工程价值】理解噪声和抖动的来源，才能有针对性地进行电路和系统优化，提升链路性能；在实际调试中，通过分析抖动的成分，可以快速定位性能瓶颈，解决问题。
> 【落地注意】高速Serdes对电源噪声非常敏感，1mV的电源噪声可以导致1ps以上的抖动，因此电源网络设计非常重要，必须加入足够的去耦电容，同时电源噪声要求控制在10mVpp以下，才能保证抖动性能达标。


---

Announcements
• Lab 5 Report & Prelab 6 due Mar 27

• Stateye theory paper posted on website




                                           2

![噪声来源](/img/serdes/fundamentals/lectures/lecture1_ee720_intro_深度学习报告/_images/img-001.jpg)
> 🔍 深度说明：
> 【研究背景】Serdes中的主要噪声来源示意图，噪声会降低接收信号的信噪比，导致误码率升高。
> 【核心结论】噪声主要包括：1) 热噪声：电子的热运动产生，和温度成正比，是白噪声，无法消除；2) 闪烁噪声（1/f噪声）：和频率成反比，低频噪声，CMOS工艺中主要存在于MOS管中；3) 电源噪声：电源上的波动，通过电路耦合到信号路径中，是主要的噪声来源之一；4) 串扰噪声：相邻信号的耦合，和信号速率、走线间距有关。
> 【工程价值】噪声分析是Serdes链路预算的重要部分，总噪声必须小于信号幅度的1/3，才能保证误码率<1e-12；在电路设计中，需要针对性地优化，降低不同来源的噪声。
> 【落地注意】电源噪声是最容易被忽视的噪声来源，数字电路的开关噪声会耦合到模拟电路的电源上，导致Serdes性能下降，必须把模拟电源和数字电源分开，加入隔离和足够的去耦电容，模拟电源噪声控制在10mVpp以下。


---

Noise in High-Speed Link Systems




                                    [Dally]



• Multiple noise sources can degrade link
  timing and amplitude margin

                                              3

![抖动分类](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/img-002.jpg)
> 🔍 深度说明：
> 【研究背景】抖动的分类示意图，抖动是信号边沿偏离理想位置的偏差，会导致采样错误，是高速链路的主要性能限制因素之一。
> 【核心结论】抖动分为两大类：1) 随机抖动（RJ）：由热噪声等随机因素导致，服从高斯分布，没有边界，用rms值表示；2) 确定性抖动（DJ）：有固定来源的抖动，有界，包括周期性抖动、数据相关抖动、占空比失真等，用峰峰值表示；总抖动（TJ）= 14×RJ + DJ（对应误码率1e-12）。
> 【工程价值】抖动是Serdes的核心指标，发送端的输出抖动要求<0.1UI rms，接收端的抖动容忍度要求>0.3UI pp，才能保证链路的时序余量足够。
> 【落地注意】随机抖动主要由电路的热噪声决定，只能通过优化电路结构、降低噪声系数来减小；确定性抖动可以通过优化电路设计、电源设计、PCB设计来降低，比如优化时钟路径、降低电源噪声、减小串扰等。


---

Noise Source Overview
• Common “noise” sources           • Crosstalk
   • Power supply noise               • One signal (aggressor)
   • Receiver offset                    interfering with another
   • Crosstalk                          signal (victim)
   • Inter-symbol interference        • On-chip coupling (capacitive)
   • Random noise                     • Off-chip coupling (t-line)
                                          • Near-end
• Power supply noise
                                          • Far-end
   • Switching current through
     finite supply impedance       • Inter-symbol interference
     causes supply voltage drops      • Signal dispersion causes
     that vary with time and            signal to interfere with itself
     physical location             • Random noise
• Receiver offset                     • Thermal & shot noise
   • Caused by random device          • Clock jitter components
     mismatches                                                           4

![抖动分解](/img/serdes/fundamentals/lectures/lecture1_ee720_intro_深度学习报告/_images/img-003.jpg)
> 🔍 深度说明：
> 【研究背景】抖动的分解与测量方法示意图，通过抖动分解可以定位抖动的来源，指导问题解决。
> 【核心结论】抖动测量常用方法：1) 实时光采样示波器：直接测量抖动波形，成本高，带宽有限；2) 采样示波器+抖动分析软件：可以进行抖动分解，区分RJ和DJ，定位抖动来源；3) 误码率 bathtub曲线：通过测量不同采样位置的误码率，间接计算抖动大小。
> 【工程价值】在Serdes调试中，通过抖动分解可以快速定位性能问题，比如周期性抖动一般来自电源或者时钟的干扰，数据相关抖动一般来自码间干扰或者均衡不足，针对性解决问题。
> 【落地注意】抖动测量时需要注意仪器的本底抖动，必须远小于被测信号的抖动，否则测量结果不准确；比如测量112G Serdes的抖动，要求仪器本底抖动<100fs rms，才能保证测量精度。


---

Bounded and Statistical Noise Sources
• Bounded or deterministic • Statistical or random noise
  noise sources              sources
   • Have theoretically              • Treat noise as a random process
     predictable values with             • Source may be psuedo-random
     defined worst-case bounds       • Often characterized w/ Gaussian stats
   • Allows for simple (but              • RMS value
     pessimistic) worst-case             • Probability density function (PDF)
     analysis                        • Examples
   • Examples                            • Thermal noise
      • Crosstalk to small channel       • Clock jitter components
        count                            • Crosstalk to large channel count
      • ISI
      • Receiver offset

• Understanding whether noise source is bounded or
  random is critical to accurate link performance estimation
                                                                            5

![低抖动设计](/img/serdes/fundamentals/lectures/lecture11_ee720_clocking_arch_plls_深度学习报告/_images/img-004.jpg)
> 🔍 深度说明：
> 【研究背景】低抖动电路设计技术示意图，抖动主要来自时钟电路和高速信号路径，需要针对性优化。
> 【核心结论】低抖动设计技术包括：1) 低噪声PLL设计：优化相位噪声，降低时钟抖动；2) 电源隔离：模拟电路和数字电路电源分开，加入去耦电容；3) 屏蔽：敏感的模拟和时钟路径用地线屏蔽，降低串扰；4) 差分信号：所有高速信号采用差分传输，抑制共模噪声。
> 【工程价值】抖动优化可以有效提升链路的时序余量，降低误码率，提升可靠性；发送端抖动降低0.05UI，链路的时序余量就可以提升0.05UI，相当于提升了0.5~1dB的链路余量。
> 【落地注意】PLL是抖动的主要来源，其相位噪声必须足够低，112G Serdes的PLL相位噪声要求<-100dBc/Hz@1MHz偏移，才能保证输出抖动<0.05UI rms；同时PLL的电源必须单独供电，加入额外的滤波电路，降低电源噪声的影响。

