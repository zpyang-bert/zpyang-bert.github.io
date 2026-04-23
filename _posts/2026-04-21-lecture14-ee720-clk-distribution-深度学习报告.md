---
layout: post
title:      "lecture14 ee720 clk distribution 深度学习报告"
date:       2026-04-21 10:42:43
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

Lecture 14: Clock Distribution Techniques




                Sam Palermo
        Analog & Mixed-Signal Center
            Texas A&M University

![](/img/serdes/fundamentals/lectures/lecture10_ee720_jitter_深度学习报告/_images/img-000.jpg)
> 🔍 深度说明：
> 【研究背景】本讲介绍高速Serdes中的时钟分布网络设计，时钟分布负责将PLL产生的参考时钟分配到芯片内的各个模块，是决定全局时钟 skew 和抖动特性的核心电路，对Serdes系统的时序性能有决定性影响。
> 【核心结论】时钟分布架构的主要类型：1) H树架构：递归对称分支，保证到各端的延迟相等，skew低但布线复杂；2) 时钟网格（Clock Mesh）：全局网格结构，skew极低（<1ps）但功耗大；3) 鱼骨架构（Fishbone）：H树的变体，平衡skew和功耗；4) 分布式时钟：各模块独立 PLL，全局仅传参考时钟，skew最小但成本最高。高速Serdes通常采用分层时钟架构：PLL → 全局时钟树 → 本地时钟树。
> 【工程价值】时钟 skew 直接影响建立/保持时间余量，在56G PAM4系统中1ps skew约等于0.056UI，对时序收敛影响显著；低skew时钟网络可提升眼图质量约0.5dB，降低链路训练时间。
> 【落地注意】112G Serdes全局时钟skew要求<1ps rms，时钟路径长度差控制在10μm以内；加入时钟门控（Clock Gating）在模块空闲时关闭时钟，节省20%~30%动态功耗；时钟线要用shielding保护，隔离相邻信号串扰。

---

Announcements
• Exam 2 Apr 25
  • Focuses on material from Lectures 7-14
  • Previous years’ Exam 2s are posted on the website for
    reference

• Project Final Report due May 2
• Project Presentations May 4 (12:30PM-2:30PM)




                                                            2


> 🔍 深度说明：
> 【研究背景】本讲介绍高速Serdes中的时钟分布网络设计，时钟分布负责将PLL产生的参考时钟分配到芯片内的各个模块，是决定全局时钟 skew 和抖动特性的核心电路，对Serdes系统的时序性能有决定性影响。
> 【核心结论】时钟分布架构的主要类型：1) H树架构：递归对称分支，保证到各端的延迟相等，skew低但布线复杂；2) 时钟网格（Clock Mesh）：全局网格结构，skew极低（<1ps）但功耗大；3) 鱼骨架构（Fishbone）：H树的变体，平衡skew和功耗；4) 分布式时钟：各模块独立 PLL，全局仅传参考时钟，skew最小但成本最高。高速Serdes通常采用分层时钟架构：PLL → 全局时钟树 → 本地时钟树。
> 【工程价值】时钟 skew 直接影响建立/保持时间余量，在56G PAM4系统中1ps skew约等于0.056UI，对时序收敛影响显著；低skew时钟网络可提升眼图质量约0.5dB，降低链路训练时间。
> 【落地注意】112G Serdes全局时钟skew要求<1ps rms，时钟路径长度差控制在10μm以内；加入时钟门控（Clock Gating）在模块空闲时关闭时钟，节省20%~30%动态功耗；时钟线要用shielding保护，隔离相邻信号串扰。

---

Agenda
• Wire Scaling
• Clock Distribution
• CML2CMOS Converters
• Multi-Phase Generation
• Multi-Phase Calibration




                            3


> 🔍 深度说明：
> 【研究背景】时钟 skew 的来源分析示意图，skew指时钟到达不同模块的相位差，过大的skew会导致时序违例，引发功能错误或降低良率。
> 【核心结论】Skew的主要来源：1) 互连线长度差异——不同路径的RC延迟不同；2) 缓冲器延迟偏差——工艺（Process）、电压（Voltage）、温度（Temperature）偏差导致各路缓冲器延迟不一致，即OCV效应；3) 负载差异——各分支时钟线的负载电容不同；4) 电源噪声耦合——不同区域的电源噪声不同，导致延迟调制；5) 串扰——相邻高速信号线耦合引起的不确定延迟。先进工艺（7nm/5nm）下OCV效应尤为严重，同一芯片不同区域的晶体管速度差异可达±20%。
> 【工程价值】在时序签核时必须考虑WC和BC下的skew差异，OCV derating因子通常设为5%~10%；深刻理解skew来源可指导时钟树综合（CTS）约束设置，降低签核难度。
> 【落地注意】112G Serdes时钟树综合时，目标skew设为<500fs（比最终要求更严苛），给OCV和老化留出余量；时钟根节点到各叶节点的深度要一致，缓冲器类型统一，确保PVT偏差对各路的影响相同。

---

Clock Distribution in Serial I/O Systems
     Embedded Clock System          Forwarded Clock System




• On-die global clock distribution is necessary in multi-channel
  embedded and fowarded clock serial link systems
                                                              4


> 🔍 深度说明：
> 【研究背景】低 skew 时钟分布设计技术，从架构、电路、版图多层面协同优化，目标是实现<1ps rms的全局时钟skew。
> 【核心结论】核心设计技术：1) 对称等长布线——时钟线的长度和绕线方式严格一致，使各路RC相同；2) 匹配缓冲器树——每路时钟分支使用相同类型和数量的缓冲器，延迟一致；3) 时钟屏蔽（Shielding）——时钟线两侧用地线包围，阻断串扰；4) 电源隔离——时钟电路使用独立的低噪声LDO供电，隔离数字噪声；5) 插指式布局（Interdigitated Layout）——将缓冲器交错排列，抵消 gradients（工艺/温度梯度）效应；6) 动态skew校准——在运行时通过可调延迟线（Delay Line）补偿静态skew误差。
> 【工程价值】采用这些技术可将全局skew从>5ps降低到<500fs，大幅提升时序余量；在Serdes系统中，这意味着各通道之间的同步性能提升，跨通道数据对齐更容易，降低了校准算法的复杂度。
> 【落地注意】插指式布局在先进工艺下对OCV补偿非常有效，但版图复杂度增加，需要用EDA工具自动化生成；动态校准的延迟线分辨率需要<100fs，才能有效校准残留skew，功耗和面积开销要综合考虑。

---

VLSI Interconnect (Wires)
                          45nm CMOS




      [Bohr ISSCC 2009]
                                      5


> 🔍 深度说明：
> 【研究背景】时钟抖动在时钟分布网络中的传递和放大机制，时钟分布网络本身也是抖动来源之一，会恶化PLL输出的时钟质量。
> 【核心结论】时钟分布抖动来源：1) 电源噪声耦合到时钟缓冲器——通过Supply Sensitivity效应将电源噪声转化为相位噪声；2) 串扰——相邻信号跳变通过耦合电容注入时钟路径；3) 热噪声——电阻的热噪声通过缓冲器放大。时钟分布网络的抖动传递函数类似低通滤波器，高频抖动（>100MHz）被抑制，低频抖动（<100kHz）几乎无衰减地传递。因此时钟分布主要放大中频段（1MHz~100MHz）抖动，这频段恰好是Serdes CDR环路的敏感频段。
> 【工程价值】时钟分布引入的抖动应控制在100fs rms以下，否则会侵蚀Serdes系统的抖动预算；在112G Serdes中，总抖动预算约0.1UI（~900fs rms），时钟分布应贡献<10%。
> 【落地注意】时钟缓冲器要选择低电源敏感度（PSRR>60dB）的类型；时钟线全程shielding，间距>3倍线宽；时钟区域与高速开关信号（TX/RX）保持足够距离（>50μm），避免耦合。

---

Wire Scaling
              Node “N”               Node “N+1”        Node “N+1”
                                    (ideal scaling)   (actual scaling)




[Ho]

• Ideally, we scale everything by 0.7x when we move to a more advanced
  technology node for 2x density
• Results in 2x wire resistance, which dramatically increases wire RC delay
   • To compensate resistance wires get taller
• Cap grows at a smaller pace with scaling
   • Taller wires increase sidewall cap
   • Improved (low-k) dielectrics help reduce cap

                                                                         6


> 🔍 深度说明：
> 【研究背景】时钟分布网络的测试和验证方法，确保设计的时钟网络满足skew和抖动规格，是芯片设计流程中的关键验证步骤。
> 【核心结论】测试验证方法：1) 振荡器测量法（Ring Oscillator）——在被测时钟线上加入MUX和反向器，构成振荡器，测量频率从而推算延迟精度；2) 相位注入测量——在时钟线上注入已知相位偏移，测量传递函数，表征抖动灵敏度；3) 统计延迟测量——在大量芯片上统计skew分布，验证OCV derating是否充分；4) 全芯片时钟树仿真——包含PVT Corner仿真，确认所有Corner下skew满足规格。先进工艺还需进行老化（Bias Temperature Instability - BTI）效应仿真，确认时钟树在10年工作后仍满足skew要求。
> 【工程价值】充分的时钟分布验证可避免芯片回来发现skew问题导致改版；高频示波器（>30GHz带宽）和相位噪声分析仪是测量时钟skew/jitter的必要设备，设备成本高，但相比改版成本仍然值得。
> 【落地注意】测试时要在真实应用条件下（温度、电压、偏置）进行，加速老化测试（HTOL）可以在1000小时内模拟10年BTI效应；skew测试的采样点要足够多（>1000个点），覆盖整个芯片的角落和边缘区域。

---

Wire Scaling - Delay


                               FO4 delay




                                                1cm wire


                                      [Ho Proc. IEEE 2001]
• Global on-chip wire RC delay becomes many
  (100+) gate delays (if driven w/ one lumped driver)
                                                         7

---

Limited Wire Bandwidth
                  • Global on-chip wire
                    bandwidth is much
                    worse than chip-
                    to-chip channels

                  • RC-dominated on-
                    chip wires vs
                    (R)LC-dominated
                    off-chip wires

                                       8

---

Agenda
• Wire Scaling
• Clock Distribution
• CML2CMOS Converters
• Multi-Phase Generation
• Multi-Phase Calibration




                            9

---

Cascaded Clock Buffers
                                                                        [Kim ISSCC 2019]

                           ST1          ST2   ST3          STN




               ST1                 ST2          ST3                STN

     Tj_i   JTF1                 JTF2         JTF3               JTFN         Tj_o


                     PN1                PN2          PN3                PNN

      Tj_o=( … (((Tj_i * JTF1) + PN1) * JTF2) + PN2) * … ) * JTFN) + PNN


• Total output jitter in frequency domain can be obtained
  from per-stage JTFs and phase noise (PN)

                                                                                      10

---

Clock Buffer Jitter Transfer Function
             [Kim ISSCC 2019]
             12
                      14G, FO2, ST10   Jitter peaking                          12




                                                           Energy/bit (pJ/b)
                      14G, FO4, ST5
                                       near fclk                                                                    Quarter‐rate
|JTF| (dB)




                      28G, FO2, ST5
              8                                                                                                     Half‐rate
                                                                                8


              4                                                                4


                                                                               0
              0                                                                     20   40   60   80   100   120
                                                                                          Data‐rate (Gb/s)
                  0                                 fclk
                      Frequency (GHz)
             • Significant jitter amplification at 28GHz in the clock distribution chain
             • Motivates most 112Gb/s systems to use a quarter-rate clocking
               scheme with 14GHz clocks
             • Quadrature phase spacing and duty cycle correction is necessary for
               uniform output eyes
                                                                                                                             11

---

14GHz Quadrature Clock Distribution
                                                                                                                                [Kim ISSCC 2019]
   CK Distribution VCC_HV




                                                                       Noise Spectral Density [dBc/Hz]
                                                                                                          -70

                 Regulator                        VCC_Analog                                              -80
                                                                                                                                        PLL
                                                                                                                                        After IQGen
                                                                                                                                        After DCC,QEC,CK Fan-Up and TX Driver
                                                                                                          -90
                                                                                                                                        After 10MHz CDR Filter
                                                                                                                                        After 3MHz CDR Filter
                                                                                                         -100
                                             4
                                                            4:1
         4       4             4
IQ Gen                   DCC          QEC        Buffer    Pulse                                         -110

                                                            Gen                                          -120

                                                                                                         -130
                                                      4Driver Output
                               Coarse/Fine
                 Coarse/Fine




                                                                                                         -140
14GHz                                                      Stage
                                 Control
                   Control




LC-PLL                                           DCD/QED                                                 -150

                                                                                                         -160


                                                     FSM                                                 -170
                                                                                                                  10
                                                                                                                       6
                                                                                                                               10
                                                                                                                                    7
                                                                                                                                                  10
                                                                                                                                                       8
                                                                                                                                                                10
                                                                                                                                                                     9
                                                                                                                                                                                10
                                                                                                                                                                                     10


                                                                                                                           Offset Frequency [Hz]

• PLL output phase noise is multiplied                                                                          208fsrms w/ 3MHz CDR BW
  by clock distribution JTF                                                                                     185fsrms w/ 10MHz CDR BW
• CDR filter (high-pass) is applied to
  get the untracked effective TX jitter

                                                                                                                                                                                 12

---

Clock Distribution Regulation

Low-BW Op-amp sets
DC Level and LF PSRR     Source Follower
                         provides mid-
                         frequency PSRR
                         [Alon ’06]




                                Suppresses
                                HF ripple




                        [Turker ISSCC 2019]



                                             13

---

Huawei 60Gb/s PAM4 Clock Distribution


                [LaCroix ISSCC 2019]




• Wideband ½-rate single-ended clock distribution (2-16GHz)
• 2 independent data rates possible per 4-lane macro
• LDO-powered CMOS inverter-based distribution
• Metal shield around distribution wires to lower crosstalk 14

---

Mediatek 56Gb/s PAM4 Clock Distribution
    [Ali ISSCC 2019]




• Tuned standing-wave clock distribution
• Two shunt inductors placed in the middle set boundary
  conditions for the transmission line and tune nearly equal
  amplitude at the drop points
                                                               15

---

Inductive-Loaded Clock Distribution
[Shibasaki ISSCC 2016]




• 2-stage narrow-band buffer drives 2-lane
  2:1 MUXs and divider
• Minimal length 28GHz clock path
                                             16

---

Active-Inductor-Based Clock Distribution
                          Active Inductor CML Load




 [Upadhyaya ISSCC 2018]
                                                 17

---

Agenda
• Wire Scaling
• Clock Distribution
• CML2CMOS Converters
• Multi-Phase Generation
• Multi-Phase Calibration




                            18

---

CML2CMOS Converter (1)
                                [Balamurugan JSSC 2008]




• Differential input stage followed by high-swing
  output stage
• Can be sensitive to power-supply noise and reduce
  jitter benefits of low-swing distribution techniques
• Often require some type of duty-cycle control
                                                          19

---

CML2CMOS Converter (2)
[Kossel JSSC 2008]




• AC-coupled self-biased
  inverter input stages and
  cross-coupled buffer stages
  can help improve duty cycle
  performance
                                20

---

Agenda
• Wire Scaling
• Clock Distribution
• CML2CMOS Converters
• Multi-Phase Generation
• Multi-Phase Calibration




                            21

---

ILO-Based Multi-Phase Clock Generation
             [Chen, ISSCC 2018]



      inj          Coarse
             Freq Track Control
      CK0
                                   FTL
                                   DAC
    Coarse
     FTL                                         Vdet_p
                                    Vctrl V-to-I Vdet_n
                       Regulator                        QPD
                                   LPF
                     Vreg_ILRO
                                          Fine QLL
Injection                                                          Vreg_PI
Lock          inj
                                                  CK0,CK180
                                                                             DClk/DClk_b
                                                  CK45, CK225    CMOS
                                                  CK90,CK270
                                                  CK135, CK315    PI
              injb                                                           XClk/XClk_b



 • ILO generates multiple output phases from differential
   injected clock
 • Coarse frequency tuning loop ensures that the ILO will lock
 • Fine quadrature-locked loop minimizes phase error          22

---

IBM 100Gb/s PAM4 QDLL Phase Generation




                              [Cevrero ISSCC 2019]


                    • Low-complexity inverter-
                      based DLL generates ¼-
                      rate clock phases from
                      differential distribution
                                                  23

---

Agenda
• Wire Scaling
• Clock Distribution
• CML2CMOS Converters
• Multi-Phase Generation
• Multi-Phase Calibration




                            24

---

Clock Error Calibration Loop
                                                                       CKQ/QB
                                                                      CKI/IB
                                                                                           1-UI
CK                                                                                      Pulse Gen
In                                                                                      (4:1 MUX)

                                                                                 DCD/
                                                                                 QED
               DCC                         QEC
           Fine  Coarse    Fine   Coarse         Fine     Coarse   Control       FSM


                                                        Coarse            Fine
                                                                                        [Kim ISSCC
Decoder
 Decoder                                                                                2019]
                                                 Ctrl
                                                                   Ctrl


  Bias        Range
 Control    Control (4b)
  (6b)                                     • 2-stage DCC & 4-stage QEC w/
                                             2-stage x-coupled buffers
Decoder                                    • DCC with current injection and
                                             QEC with C-DAC                                         25

---

Asynchronous Sampling Error Detection
                                                                  Quadrature error detection
                Duty-cycle error detection
                                                           CKIN
                                                                    D Q
                                CKP Cntr[23:0]             CKQP
     CKIP/QP                                                                        CK QP/IN Cntr[23:0]
                 D Q            DC offset[23:0]
     CKIN/QN                                               CKQP                                           FSM
                                CKN Cntr[23:0]    FSM      VSS
                                                                   D Q               Skew offset[23:0]


                                                                                    CKIP/QP Cntr[23:0]
                                                           CKQP
                                                                   D Q
                    DC
Asynchronous       detect
                                                           CKIP




                                                                       DC
                                                                                        [Kim ISSCC 2019]
                 VCO edge                          Asynchronous       detect

         CKIP                                              CKIP

         CKQP               Compare                        CKQP
                                                                          Compare
         CKIN
                                                           CKIN
        CKQN
                                                           CKQN


  • Asynchronous VCO samples final ¼-rate clocks
  • Duty cycle error minimized w/ equal P/N count
  • Quadrature error minimized w/ equal IP*QP/QP*IN count
                                                                                                                26

---

Background Quadrature Clock Calibration




                                Case 1: IQ Matched     Case 2: CK0 Early      Case 3: CK0 Late
                                  D1                    D1                    D1

                                  D2                    D2                    D2

                                CK 0                  CK 0                  CK 0

                               DDout,rep
                                  out                 Dout,rep
                                                       out                  D
                                                                            Dout,rep
                                                                              out



                                Dout,rep Duty = 50%   Dout,rep Duty > 50%    Dout,rep Duty < 50%


• Duty cycle error detected by low-pass filtering clocks
• IQ mismatch is detected by monitoring output duty cycle of replica mux
• Information is used to control independent I/Q VCDLs
                                                                                              27

---

128Gb/s PAM4 TX Clock Generation
[Toprak-Deniz ISSCC 2018]




 • DCC with current injection buffers

 • QEC with differential offset voltage in half-rate CML divider
                                                               28

---

DCC w/ Inverter Trip Point Adjustment
• Clocks are AC-coupled to      [Menolfi ISSCC 2018]

  input inverters that are
  biased at the trip point
  with feedback resistors
• IDC injected at inverter
  input shifts trip point and
  output duty cycle
• Monotonic control
  achieved with pull-
  up/down diodes
• RDC can also be adjusted
  to change tuning range

                                                       29

---

Clock Generation & Distribution
Take-Away Points
• Low-noise clock distribution is necessary in
  high-performance serial links

• Jitter amplification must be avoided in multi-
  lane clock distribution

• Efficient multi-phase generation and
  calibration is necessary for ¼-rate front-ends

                                                 30

---

