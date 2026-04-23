---
layout: post
title:      "lecture9 ee720 noise sources"
date:       2026-04-21 10:05:31
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
Announcements
• Lab 5 Report & Prelab 6 due Mar 27

• Stateye theory paper posted on website




                                           2
Noise in High-Speed Link Systems




                                    [Dally]



• Multiple noise sources can degrade link
  timing and amplitude margin

                                              3
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
Proportional and Independent Noise Sources
• Some noise is proportional          • Some noise is independent
  to signal swing                       to signal swing
   • Crosstalk                           • RX offset
   • Simultaneous switching              • Non-IO power supply noise
     power supply noise               • Can overpower this noise
   • ISI
• Can’t overpower this noise
   • Larger signal = more noise

                            VN  K NVS  VNI
              Total noise                          Independent noise
                 Proportional noise     Signal swing
                 constant


                                                                       6
Common Noise Sources
• Power supply noise
• Receiver offset
• Crosstalk
• Inter-symbol interference
• Random noise




                              7
Power Supply Noise




                                                   [Hodges]
• Circuits draw current from the VDD supply nets and
  return current to the GND nets
• Supply networks have finite impedance
• Time-varying (switching) currents induce variations on
  the supply voltage
• Supply noise a circuit sees depends on its location in
  supply distribution network                                 8
Power Routing
     Bad – Block B will          Better – Block B will experience 1/2
     experience excessive        supply noise, but at the cost of double
     supply noise                the power routing through blocks




                                                         [Hodges]
     Even Better – Block A &
                                 Best – Block A & B
     B will experience similar
                                 are more isolated
     supply noise




                                                         [Hodges]
                                                                      9
 Supply Induced Delay Variation
• Supply noise can induce variations in circuit delay
   • Results in deterministic jitter on clocks & data signals




                                                                     [Hodges]

                C L VDD 2            C L VDD 2                    C LVDD
      t PHL                                                
                    I DSATN     WN vsat Cox VDD  VTN 2  2WN vsat Cox VDD  VTN 
                                                          
                                VDD  V  E L 
                                             TN  CN N     
                                               VDD
                                Delay                 VDD
                                           VDD  VTN

• CMOS delay is approximately directly proportional to VDD
   • More delay results in more deterministic jitter
                                                                                         10
Simultaneous Switching Noise
• Finite supply impedance
  causes significant
  Simultaneous Switching
  Output (SSO) noise
  (xtalk)
• SSO noise is proportional
  to number of outputs
  switching, n, and
  inversely proportional to
  signal transition time, tr
                  i   LV
        VN  L      n s
                 tr   Z 0t r
                               11
Common Noise Sources
• Power supply noise
• Receiver offset
• Crosstalk
• Inter-symbol interference
• Random noise




                              12
Receiver Input Referred Offset




• The input referred offset is primarily a function of Vth
  mismatch and a weaker function of  (mobility) mismatch
                          AVt                    A
                   V          ,     /  
                     t
                          WL                     WL
                                                             13
Receiver Input Referred Offset
                            AVt                    A
                    V           ,     /  
                      t
                            WL                     WL
• To reduce input offset 2x, we need to increase area 4x
   • Not practical due to excessive area and power consumption
   • Offset correction necessary to efficiently achieve good sensitivity


• Ideally the offset “A” coefficients are given by the design
  kit and Monte Carlo is performed to extract offset sigma
• If not, here are some common values:
   • AVt = 1mVm per nm of tox
       • For our default 90nm technology, tox=2.8nm  AVt ~2.8mVm
   • A is generally near 2%m
                                                                           14
Common Noise Sources
• Power supply noise
• Receiver offset
• Crosstalk
• Inter-symbol interference
• Random noise




                              15
Crosstalk
• Crosstalk is noise induced by one signal (aggressor) that
  interferes with another signal (victim)

• Main crosstalk sources
   • Coupling between on-chip (capacitive) wires
   • Coupling between off-chip (t-line/channel) wires
   • Signal return coupling


• Crosstalk is a proportional noise source
   • Cannot be reduced by scaling signal levels
   • Addressed by using proper signal conventions, improving channel
     and supply network, and using good circuit design and layout
     techniques

                                                                       16
 Crosstalk to Capacitive Lines
• On-chip wires have significant capacitance to adjacent
  wires both on same metal layer and adjacent vertical layers
• Floating victim
    • Examples: Sample-nodes, domino logic
    • When aggressor switches
          • Signal gets coupled to victim via a capacitive voltage divider
          • Signal is not restored



                                                              VB  kc VA
                                                                     CC
                                                              kc 
                                                                   CC  CO
[Dally]


                                                                             17
Crosstalk to Driven Capacitive Lines
• Crosstalk to a driven
  line will decay away
  with a time-constant
       xc  RO CC  CO                                                            [Dally]

                                                   Ideal Unit Step :
• Peak crosstalk is                                      t 
                                       V t   k exp      
  inversely proportional                           B
                                                          
                                                            c
                                                                        xc

  to aggressor transition          Step with Finite Rise Time, t :             r


  times, tr, and driver          
                                 
                                                     t 
                                       k   1  exp 
                                                       xc
                                                                                     if t  t r
                                                             
                                               c
                                             t 
  strength (1/RO)                
                       V t   
                                B
                                                      r               xc

                                     k   xc  exp  t  t r   exp  t  if t  t
                                      c  t r     xc                 
                                                                                   
                                                                                                r
                                                                               xc


                                                                                              18
Capacitive Crosstalk Delay Impact
• Aggressor transitioning near victim transition can modulate
  the victim’s effective load capacitance
• This modulates the victim signal’s delay, resulting in
  deterministic jitter




         [Hodges]

                  Aggressor Static :         C L  C gnd  CC
           Aggressor Switching Same Way :        C L  C gnd
          Aggressor Switching Opposite Way : C L  C gnd  2CC
                                                                 19
Mitigating Capacitive (On-Chip) Crosstalk
• Adjacent vertical metal layers should be routed
  perpendicular (Manhattan routing)
• Limit maximum parallel routing distance
• Avoid floating signals and use keeper transistors with
  dynamic logic
• Maximize signal transition time
   • Trade-off with jitter sensitivity
• For differential signals, periodically “twist” routing to make
  cross-talk common-mode
• Separate sensitive signals
• Use shield wires
• Couple DC signals to appropriate supply
                                                                   20
Transmission Line Crosstalk
• 2 coupled lines:
  IA



  IB
                                                                 [Dally]

• Transient voltage signal on A is coupled to B capacitively

       dVB x, t       dV  x, t                       CC
                    kcx A            where   kcx 
         dt               dt                          C S  CC

• Capacitive coupling sends half the coupled energy in each direction with
  equal polarity




                                                                           21
Transmission Line Crosstalk
• 2 coupled lines:
  IA



  IB
                                                                                              [Dally]

• Transient current signal on A is coupled to B through mutual inductance
                    I A x, t     V  x, t 
                                  A
                         t           Lx
  dVB x, t       dI A  x, t  M  dVA  x, t         dV A  x, t            klx 
                                                                                          M
               M                                  klx                 where
    dx                 dt         L  dx                  dx                           L

• Inductive coupling sends half the coupled energy in each direction
  with a negative forward traveling wave and a positive reverse
  traveling wave
                                                                                                        22
   Near- and Far-End Crosstalk
[Hall]




                  •   Near-end crosstalk (NEXT) is immediately
                      observed starting at the aggressor transition
                      time and continuing for a round-trip delay
                  •   Due to the capacitive and inductive coupling
                      terms having the same polarity, the NEXT signal
                      will have the same polarity as the aggressor
                  •   Far-end crosstalk (FEXT) propagates along the
                      victim channel with the incident signal and is
                      only observed once
                  •   Due to the capacitive and inductive coupling
                      terms having the opposite polarity, the FEXT
                      signal can have either polarity, and in a
                      homogeneous medium (stripline) cancel out
                                                                   23
  Near- and Far-End Crosstalk

                         Reverse Coupling Coefficient
                                 krx (NEXT)

                         Forward Coupling Coefficient
                                 kfx (FEXT)
          tx
[Dally]
                                k 
                                    kcx  klx 
                                 rx
                                         4
                                      k  k 
                                k fx  cx lx
                                         2

                                For derivation of
                                krx and kfx, see
                                Dally 6.3.2.3


                                                    24
Off-Chip Crosstalk
   Occurs mostly in
    package and board-
    to-board connectors
   FEXT is attenuated
    by channel response
    and has band-pass
    characteristic
   NEXT directly couples
    into victim and has
    high-pass
    characteristic
                            25
Signal Return Crosstalk
• Shared return path with finite impedance
• Return currents induce crosstalk occurs among signals



                                                                     V


                                                                     -Vxr

      [Dally]


                                                      ZR
                Return Crosstalk Voltage : Vxr  V       k xr V
                                                      Z0



                                                                            26
Common Noise Sources
• Power supply noise
• Receiver offset
• Crosstalk
• Inter-symbol interference
• Random noise




                              27
Inter-Symbol Interference (ISI)
• Previous bits residual state can
  distort the current bit, resulting in
  inter-symbol interference (ISI)                                   cursor




y   d k 
             t   c t   ht 
                       d k                                            post-cursor ISI
                                                                                 …

                                             pre-cursor
                                                ISI




                         y(1)(t) sampled relative to pulse peak:
             [… 0.003 0.036 0.540 0.165 0.065 0.033 0.020 0.012 0.009 …]
      k =[ … -2         1         0      1       2        3   4     5        6       …]
                                By Linearity: y(0)(t) =-1*y(1)(t)

                                                                                          28
Peak Distortion Analysis Example




                 y0(1) t   0.540
     

     y   t  kT  
   k  
             1
                         y t  kT  0
                                           0.007
    k 0
      

     y   t  kT  
    k  
             1
                          y t  kT  0
                                           0.389
     k 0

s t   20.540  0.007  0.389   0.288
                                                     29
Worst-Case Eye vs Random Data Eye



                                               Worst-Case Eye
                                               100 Random Bits
                                               1000 Random Bits
                                               1e4 Random Bits




• Worst-case data pattern can occur at very low probability!
• Considering worst-case is too pessimistic
                                                               30
Constructing ISI Probability Density
Function (PDF)
• Using ISI probability density
  function will yield a more accurate
  BER performance estimate

• In order to construct the total ISI
  PDF, need to convolve all of the
  individual ISI term PDFs together
   • 50% probability of “1” symbol ISI and
     “-1” symbol ISI




                                             31
Convolving Individual ISI PDFs Together



                 *                     =




                 *                     =




• Keep going until all individual PDFs convolved together
                                                            32
Complete ISI PDF




                   33
Cursor PDF – Data 1


                *                      =




• Data 1 PDF is centered about the cursor value
  and varies from a maximum positive value to
  the worst-case value predicted by PDA
  • This worst-case value occurs at a low probability!


                                                         34
Cursor Cumulative Distribution Function (CDF)

• For a given offset, what
  is the probability of a
  Data 1 error?
  • Data 1 error probability
    for a given offset is equal
    to the Data 1 CDF
              X
BER X    PDF dx
              


                                            35
Combining Cursor CDFs




                        36
Bit-Error-Rate (BER) Distribution Eye
• Statistical BER analysis
  tools use this technique
  to account for ISI
  distribution and also
  other noise sources
  • Example from Stateye
     • Note: Different channel &
       data rate from previous
       slides




                                    37
Common Noise Sources
• Power supply noise
• Receiver offset
• Crosstalk
• Inter-symbol interference
• Random noise




                              38
Random Noise
• Random noise is unbounded and modeled
  statistically
  • Example: Circuit thermal and shot noise
• Modeled as a continuous random variable
  described by
  • Probability density function (PDF)
  • Mean, 
  • Standard deviation, 
                                            
 PDF  Pn  x ,  n   xPn  x dx,     x   n  Pn  x dx
                                        2               2
                                        n
                                           
                                                                     39
Gaussian Distribution
• Gaussian distribution is normally assumed for random noise
   • Larger sigma value results in increased distribution spread
                                              x   n 2
                                   1       
                       Pn  x        e        2 2

                                  2 




                                                                   40
Signal with Added Gaussian Noise




• Finite probability of noise pushing signal
  past threshold to yield an error
                                               41
Cumulative Distribution Function (CDF)

• The CDF tells what
  is the probability
  that the noise
  signal is less than
  or equal to a
  certain value


                  x                 x                  u   n 2        [Dally]
                                            1       
    n x        Pn u du                 e        2 2
                                                                     du
                u              u     2 
                                                                               42
Error and Complimentary Error Functions
• Error Function:
                                                                 x
                                              erf  x  
                                                             2
                                                                  exp u 
                                                                           2
                                                                             du
                                                              u 0


• Relationship between normal                               1         x 
                                               x         1  erf     
  CDF (0,1) and Error Function:                             2          2 



• The complementary error                              1         x 
                                 Q x   1    x   1  erf    
  function gives the probability                       2         2 
                                                        x 
  that the noise will exceed a                  1
                                               erfc
                                                2
                                                            
                                                        2
  given value
                                  1     x 
                      Q  x   erfc     
                                  2     2 
                                                                                  43
Bit Error Rate (BER)
• Using erfc to predict BER:
                w/ Normal (0,1) PDF

                                       Conservative
                                      Upper-Bound
                                      Approximation




                                      [Dally]


• Need a symbol of about 7 for BER=10-12
  • Peak-to-peak value will be 2x this
                                                      44
Noise Source Classifications
• Determining whether noise source is
  • Proportional vs Independent
  • Bounded vs Statistical
• is important in noise budgeting




                                        45
  Noise Budget Example
 • Peak TX differential swing of 400mVppd equalized down 10dB
       • 200mV  63mV

                                            Value                                    +63mV
  Parameter             Kn         RMS
                                         (BER=10-12)                     31mV
Peak Differential
                                            0.4V
Swing
RX Offset +
                                            5mV
Sensitivity
Power Supply
                                            5mV
Noise                                                                    31mV
                                                                                     -63mV
Residual ISI            0.05                20mV
Crosstalk               0.05                20mV       • Conservative analysis
Random Noise                       1mV      14mV
                                                           • Assumes all distributions
Attenuation         10dB = 0.684           0.274V            combine at worst-case
Total Noise                                0.338V
                                                       • Better technique is to use
Differential Eye
Height Margin                              62mV          statistical BER link simulators

                                                                                         46
Next Time
• Timing Noise
• BER Analysis Techniques




                            47
