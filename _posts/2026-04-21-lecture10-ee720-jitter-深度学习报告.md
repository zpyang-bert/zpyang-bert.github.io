---
layout: post
title:      "lecture10 ee720 jitter 深度学习报告"
date:       2026-04-21 10:12:33
author:     "Bert"
tags:
  - Fundamentals
  - Jitter
  - Lecture
  - SerDes
  - 深度学习
---

ECEN720: High-Speed Links
   Circuits and Systems
       Spring 2023

       Lecture 10: Jitter




           Sam Palermo
   Analog & Mixed-Signal Center
       Texas A&M University

![课程封面](/img/serdes/fundamentals/lectures/lecture10_ee720_jitter_深度学习报告/_images/img-000.jpg)
> 🔍 深度说明：
> 【研究背景】这是ECEN720第十讲，主题是抖动的深入分析，是前一讲噪声与抖动的延伸，重点讲解抖动的数学模型、对误码率的影响、抖动容限测试等内容，是Serdes测试与验证的核心参考。
> 【核心结论】内容覆盖抖动的概率分布、误码率与抖动的关系、 bathtub曲线、抖动容限测试、抖动预算、抖动传递函数，是Serdes系统设计和测试的必备知识。
> 【工程价值】抖动预算是Serdes系统设计的重要环节，合理的抖动分配可以保证整个系统的时序余量，避免出现时序问题；抖动容限测试是Serdes验收的核心测试项，直接决定了链路的可靠性。
> 【落地注意】系统抖动预算需要留足够的余量，一般要求总抖动<0.7UI，其中发送端抖动<0.2UI，信道抖动<0.2UI，接收端抖动容忍>0.3UI，保证最坏情况下还有0.1UI的时序余量。


---

Announcements
• Lab 6 Report due Apr 3

• Reference Material
  • Jitter application notes posted on website
  • Majority of today’s material from Hall reference




                                                       2

![抖动与误码率](/img/serdes/fundamentals/lectures/lecture1_ee720_intro_深度学习报告/_images/img-001.jpg)
> 🔍 深度说明：
> 【研究背景】抖动对误码率的影响示意图，抖动越大，误码率越高，两者之间有明确的数学关系。
> 【核心结论】当采样位置偏离理想位置时，误码率会快速升高，服从高斯分布的随机抖动导致误码率随采样偏移呈指数下降；总抖动在BER=1e-12时一般定义为14倍的随机抖动rms值加上确定性抖动的峰峰值。
> 【工程价值】通过测量不同采样位置的误码率，可以得到 bathtub曲线，从中计算出总抖动和时序余量，是Serdes性能验证的核心方法。
> 【落地注意】112G PAM4 Serdes的误码率要求<1e-6（经过FEC前），对应的抖动容限要求>0.3UI pp，保证在最坏情况下仍然有足够的时序余量；实际测试中需要在不同温度、电压、信道条件下测试，覆盖所有最坏场景。


---

Agenda
• Jitter Definitions
• Jitter Categories
• Dual Dirac Jitter Model
• System Jitter Budgeting




                            3

![Bathtub曲线](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/img-002.jpg)
> 🔍 深度说明：
> 【研究背景】误码率的Bathtub曲线示意图，是Serdes测试中最常用的曲线，直观展示了链路的时序余量。
> 【核心结论】Bathtub曲线的横轴是采样位置偏移，纵轴是误码率，曲线的底部越宽，时序余量越大；两个边沿的斜率由随机抖动决定，斜率越陡，随机抖动越小，中间平坦部分的宽度由确定性抖动决定。
> 【工程价值】通过Bathtub曲线可以快速评估链路的性能，计算出时序余量，判断链路是否满足要求；在调试中，通过Bathtub曲线的形状可以判断抖动的类型，定位问题。
> 【落地注意】测量Bathtub曲线需要足够的采样时间，测量误码率到1e-12一般需要几秒钟到几分钟的时间，实际量产测试中一般测量到1e-8或者1e-9，通过外推得到1e-12的性能，缩短测试时间。


---

Eye Diagram and Spec Mask
• Links must have margin in both the voltage AND
  timing domain for proper operation
• For independent design (interoperability) of TX
  and RX, a spec eye mask is used
Eye at RX
sampler




RX clock timing noise             [Hall]
or jitter (random noise
only here)
                                                    4

![抖动容限测试](/img/serdes/fundamentals/lectures/lecture1_ee720_intro_深度学习报告/_images/img-003.jpg)
> 🔍 深度说明：
> 【研究背景】抖动容限测试方法示意图，抖动容限是接收端能够容忍的最大输入抖动，是接收端的核心指标。
> 【核心结论】抖动容限测试是向发送信号注入不同频率、不同幅度的抖动，测量误码率保持在<1e-12时的最大抖动幅度，得到抖动容限曲线；抖动容限一般在低频时大，高频时小，符合CDR的抖动跟踪特性。
> 【工程价值】抖动容限是接收端抗抖动能力的直接体现，抖动容限越高，系统的兼容性越好，对发送端和信道的抖动要求越低。
> 【落地注意】112G Serdes的抖动容限要求在低频时>0.3UI pp，高频时>0.15UI pp，满足IEEE 802.3ck标准的要求；测试时需要覆盖不同的抖动频率，从100kHz到1GHz，验证全频段的抖动容忍能力。


---

Jitter Definitions
• Jitter can be defined as “the short-term variation
  of a signal with respect to its ideal position in time”
• Jitter measurements
  • Period Jitter (JPER)
     • Time difference between measured period and ideal period
  • Cycle to Cycle Jitter (JCC)
     • Time difference between two adjacent clock periods
     • Important for budgeting on-chip digital circuits cycle time
  • Accumulated Jitter (JAC)
     • Time difference between measured clock and ideal trigger clock
     • Jitter measurement most relative to high-speed link systems


                                                                        5

![抖动预算](/img/serdes/fundamentals/lectures/lecture11_ee720_clocking_arch_plls_深度学习报告/_images/img-004.jpg)
> 🔍 深度说明：
> 【研究背景】系统抖动预算示意图，抖动预算是Serdes系统设计的重要环节，合理分配各个环节的抖动指标，保证整个系统的时序余量足够。
> 【核心结论】总抖动预算包括：发送端输出抖动、传输信道引入的抖动、接收端的抖动容忍度，三者需要满足：发送抖动 + 信道抖动 < 接收抖动容限 - 余量；一般需要预留0.1UI以上的余量，应对最坏情况。
> 【工程价值】抖动预算可以指导各个模块的指标分配，避免某个模块的抖动超标导致整个系统无法工作，同时可以避免过度设计，平衡性能和成本。
> 【落地注意】实际系统中，信道的抖动往往被低估，比如PCB的串扰、连接器的抖动、电源噪声的影响等，因此在预算时需要给信道抖动预留足够的余量，一般预留0.15UI以上，避免实际部署时出现时序问题。

