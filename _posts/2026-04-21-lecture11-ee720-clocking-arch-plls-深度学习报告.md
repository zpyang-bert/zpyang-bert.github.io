---
layout: post
title:      "lecture11 ee720 clocking arch plls 深度学习报告"
date:       2026-04-21 10:19:06
author:     "Bert"
tags:
  - Clocking
  - Fundamentals
  - Lecture
  - PLL
  - SerDes
  - 深度学习
---

ECEN720: High-Speed Links
      Circuits and Systems
          Spring 2023

Lecture 11: Clocking Architectures & PLLs




                Sam Palermo
        Analog & Mixed-Signal Center
            Texas A&M University

![课程封面](/img/serdes/fundamentals/lectures/lecture10_ee720_jitter_深度学习报告/_images/img-000.jpg)
> 🔍 深度说明：
> 【研究背景】Serdes时钟架构与PLL设计是高速Serdes的核心模块，决定了时钟抖动性能，直接影响链路误码率。
> 【核心结论】PLL由鉴相器、电荷泵、环路滤波器、VCO、分频器组成，负反馈实现时钟同步，相位噪声是PLL的核心指标。
> 【工程价值】低抖动PLL可以把输出抖动控制在50fs rms以下，提升Serdes时序余量0.1UI以上，大幅降低误码率。
> 【落地注意】112G Serdes要求PLL相位噪声<-100dBc/Hz@1MHz偏移，参考时钟抖动<1ps rms，PLL电源需要单独隔离滤波。


---

Announcements
• Project Preliminary Report due Apr 18
• Project Final Report due May 2




                                          2

![时钟架构](/img/serdes/fundamentals/lectures/lecture1_ee720_intro_深度学习报告/_images/img-001.jpg)
> 🔍 深度说明：
> 【研究背景】Serdes时钟分为发送端PLL时钟和接收端CDR恢复时钟，多通道Serdes可以共享PLL降低成本。
> 【核心结论】发送端时钟要求低抖动，接收端CDR要求快速锁定、大抖动跟踪范围，参考时钟质量直接影响PLL性能。
> 【工程价值】共享PLL架构可以降低芯片面积和功耗，16通道Serdes共享PLL可以节省30%以上的时钟模块面积。
> 【落地注意】参考时钟路径需要做等长设计，避免不同通道之间的相位偏差过大，影响同步性能；参考时钟走线要用地线屏蔽，降低串扰。


---

Agenda
• Clocking Architectures

• PLLs
  • Modeling
  • Noise transfer functions




                               3

![PLL原理](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/img-002.jpg)
> 🔍 深度说明：
> 【研究背景】PLL是负反馈系统，通过相位比较调整VCO频率，实现输出时钟和参考时钟的相位/频率同步。
> 【核心结论】环路带宽是PLL的核心参数，带宽大锁定快但参考噪声抑制差，带宽小噪声抑制好但锁定慢，Serdes PLL一般取1~10MHz。
> 【工程价值】合适的环路带宽设计可以平衡PLL的锁定速度和输出抖动，满足不同应用场景的需求。
> 【落地注意】环路滤波器的阻容参数需要精确设计，最好加入可调电容，支持片上校准，抵消工艺偏差的影响，保证环路带宽的精度。


---

References
• High-speed link clocking tutorial paper, PLL
  analysis paper, and PLL thesis posted on
  website
• Posted PLL models in project section
• Website has additional links on PLL and
  jitter tutorials
• Majority of today’s PLL material comes
  from Fischette tutorial and M. Mansuri’s
  PhD thesis (UCLA)
                                                 4

![相位噪声](/img/serdes/fundamentals/lectures/lecture1_ee720_intro_深度学习报告/_images/img-003.jpg)
> 🔍 深度说明：
> 【研究背景】PLL相位噪声在不同频率偏移处的来源不同，低频来自参考和电荷泵，高频来自VCO。
> 【核心结论】环路带宽以内的噪声由参考时钟和环路组件决定，带宽以外的噪声由VCO决定，优化时需要针对性处理。
> 【工程价值】通过相位噪声分析可以定位PLL的噪声瓶颈，针对性优化，降低输出抖动。
> 【落地注意】VCO是高频噪声的主要来源，需要采用高Q值电感，优化电源噪声抑制，降低VCO相位噪声，112G Serdes的VCO相位噪声要求<-120dBc/Hz@10MHz偏移。


---

High-Speed Electrical Link System




                                    5

![低抖动设计](/img/serdes/fundamentals/lectures/lecture11_ee720_clocking_arch_plls_深度学习报告/_images/img-004.jpg)
> 🔍 深度说明：
> 【研究背景】低抖动PLL设计需要从架构和电路两个层面优化，先进架构可以大幅降低输出抖动。
> 【核心结论】亚采样PLL、采样保持PLL等先进架构可以降低鉴相器噪声，比传统PLL输出抖动降低一半以上。
> 【工程价值】采用先进架构的PLL可以提升Serdes时序余量0.1UI以上，或者延长传输距离10%以上。
> 【落地注意】PLL模块需要和数字电路物理隔离，放在芯片角落，电源单独供电，加入LC滤波，降低数字开关噪声的耦合。

