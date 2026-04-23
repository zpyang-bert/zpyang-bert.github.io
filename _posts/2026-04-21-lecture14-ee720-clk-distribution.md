---
layout: post
title:      "lecture14 ee720 clk distribution"
date:       2026-04-21 10:38:27
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
Announcements
• Exam 2 Apr 25
  • Focuses on material from Lectures 7-14
  • Previous years’ Exam 2s are posted on the website for
    reference

• Project Final Report due May 2
• Project Presentations May 4 (12:30PM-2:30PM)




                                                            2
Agenda
• Wire Scaling
• Clock Distribution
• CML2CMOS Converters
• Multi-Phase Generation
• Multi-Phase Calibration




                            3
Clock Distribution in Serial I/O Systems
     Embedded Clock System          Forwarded Clock System




• On-die global clock distribution is necessary in multi-channel
  embedded and fowarded clock serial link systems
                                                              4
VLSI Interconnect (Wires)
                          45nm CMOS




      [Bohr ISSCC 2009]
                                      5
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
Wire Scaling - Delay


                               FO4 delay




                                                1cm wire


                                      [Ho Proc. IEEE 2001]
• Global on-chip wire RC delay becomes many
  (100+) gate delays (if driven w/ one lumped driver)
                                                         7
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
Agenda
• Wire Scaling
• Clock Distribution
• CML2CMOS Converters
• Multi-Phase Generation
• Multi-Phase Calibration




                            9
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
Huawei 60Gb/s PAM4 Clock Distribution


                [LaCroix ISSCC 2019]




• Wideband ½-rate single-ended clock distribution (2-16GHz)
• 2 independent data rates possible per 4-lane macro
• LDO-powered CMOS inverter-based distribution
• Metal shield around distribution wires to lower crosstalk 14
Mediatek 56Gb/s PAM4 Clock Distribution
    [Ali ISSCC 2019]




• Tuned standing-wave clock distribution
• Two shunt inductors placed in the middle set boundary
  conditions for the transmission line and tune nearly equal
  amplitude at the drop points
                                                               15
Inductive-Loaded Clock Distribution
[Shibasaki ISSCC 2016]




• 2-stage narrow-band buffer drives 2-lane
  2:1 MUXs and divider
• Minimal length 28GHz clock path
                                             16
Active-Inductor-Based Clock Distribution
                          Active Inductor CML Load




 [Upadhyaya ISSCC 2018]
                                                 17
Agenda
• Wire Scaling
• Clock Distribution
• CML2CMOS Converters
• Multi-Phase Generation
• Multi-Phase Calibration




                            18
CML2CMOS Converter (1)
                                [Balamurugan JSSC 2008]




• Differential input stage followed by high-swing
  output stage
• Can be sensitive to power-supply noise and reduce
  jitter benefits of low-swing distribution techniques
• Often require some type of duty-cycle control
                                                          19
 CML2CMOS Converter (2)
[Kossel JSSC 2008]




• AC-coupled self-biased
  inverter input stages and
  cross-coupled buffer stages
  can help improve duty cycle
  performance
                                20
Agenda
• Wire Scaling
• Clock Distribution
• CML2CMOS Converters
• Multi-Phase Generation
• Multi-Phase Calibration




                            21
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
IBM 100Gb/s PAM4 QDLL Phase Generation




                              [Cevrero ISSCC 2019]


                    • Low-complexity inverter-
                      based DLL generates ¼-
                      rate clock phases from
                      differential distribution
                                                  23
Agenda
• Wire Scaling
• Clock Distribution
• CML2CMOS Converters
• Multi-Phase Generation
• Multi-Phase Calibration




                            24
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
 128Gb/s PAM4 TX Clock Generation
[Toprak-Deniz ISSCC 2018]




 • DCC with current injection buffers

 • QEC with differential offset voltage in half-rate CML divider
                                                               28
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
Clock Generation & Distribution
Take-Away Points
• Low-noise clock distribution is necessary in
  high-performance serial links

• Jitter amplification must be avoided in multi-
  lane clock distribution

• Efficient multi-phase generation and
  calibration is necessary for ¼-rate front-ends

                                                 30
