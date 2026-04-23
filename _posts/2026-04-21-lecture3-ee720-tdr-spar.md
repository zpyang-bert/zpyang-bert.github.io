---
layout: post
title:      "lecture3 ee720 tdr spar"
date:       2026-04-21 09:23:02
author:     "Bert"
tags:
  - Fundamentals
  - Lecture
  - SerDes
  - TDR
  - 深度学习
---

ECEN720: High-Speed Links
            Circuits and Systems
                Spring 2023
Lecture 3: Time-Domain Reflectometry & S-Parameter Channel Models




                        Sam Palermo
                Analog & Mixed-Signal Center
                    Texas A&M University
Announcements
• Lab 1 report and Prelab 2 due Feb 6

• Reference Material Posted on Website
  • TDR theory application note
  • S-parameter notes




                                         2
Agenda
• Interconnect measurement techniques
  • Time-domain reflectometry (TDR)
  • Network analyzer
• S-parameters
• Cascading S-parameter models
• Full S-parameter channel model
• Transient simulations
  • Impulse response generation
  • Eye diagrams
  • Inter-symbol interference

                                        3
Lecture References
• Majority of TDR material from Dally
  Chapter 3.4, 3.6 - 3.7

• Majority of s-parameter material from Hall
  “Advanced Signal Integrity for High-Speed
  Digital Designs” Chapter 9




                                               4
Interconnect Modeling



• Why do we need interconnect models?
  • Perform hand calculations and simulations (Spice, Matlab, etc…)
  • Locate performance bottlenecks and make design trade-offs
• Model generation methods
  • Electromagnetic CAD tools
  • Actual system measurements
• Measurement techniques
  • Time-Domain Reflectometer (TDR)
  • Network analyzer (frequency domain)
                                                                      5
Time-Domain Reflectometer (TDR)
                                                            [Agilent]




[Dally]

• TDR consists of a fast step generator and a high-speed
  oscilloscope
• TDR operation
   • Outputs fast voltage step onto channel
   • Observe voltage at source, which includes reflections
   • Voltage magnitude can be converted to impedance
   • Impedance discontinuity location can be determined by delay
• Only input port access to characterize channel
                                                                        6
TDR Impedance Calculation




                                    Vr t  Z T t   Z 0
                         k r t          
                                     Vi      Z T t   Z 0
                    1  k r t            Vi  Vr t            V t  
   Z T t   Z 0                 Z 0                 Z 0               
                    1  k r t            Vi  Vr t            2Vi  V t  
                         If VSTEP  1V  Vi  0.5V
                         V t                                    2x 
        Z T t   Z 0                        ZT x   ZT  t     
                         1V  V t                                
                                                                                         7
TDR Waveforms (Open & Short)
• Open termination    Input step at 1ns



                       2td




• Short termination

                       2td




                                          8
TDR Waveforms (Matched & Mismatched)

• Matched termination




• Mismatched termination   2td    ZT > Z0


                                  ZT < Z0




                                            9
 TDR Waveforms (C & L Discontinuity)

• Shunt C discontinuity
                                                                   Z 0C
                                                            C 
                                                                    2
                                                      2td



• Series L discontinuity t = 10ps          r




                                                      2td

                                                                  L
Peak voltage spike   V    
                                         tr 
                                                        L 
       magnitude:
                          1  e     
                                                                2Z 0
                     V     t r               
                                                                          10
TDR Rise Time and Resolution
• TDR spatial resolution is set by step risetime
                       x  t r

• Step risetime degrades with propagation
  through channel
  • Dispersion from skin-effect
  • Lump discontinuities low-pass filter the step
• Causes difficulty in estimating L & C values
• Channel filtering can actually compensate
  for lump discontinuity spikes 
                                                    11
TDR Multiple Reflections




                           12
TDR Waveforms (Multiple Discontinuities)
               A        B          C    Load




                            BAB,
                            CBC
              A
                               BAC,
                    B   C      CBCBC,
                               CAB


              Note: Step comes at 1ns


                                               13
Time-Domain Transmission (TDT)
                                                   [Dally]



                                                      V2  j 
                                           H  j  
• Can measure channel transfer function               V1  j 
• Hard to isolate impedance discontinuities, as they are
  superimposed on a single rising edge
                      TDR           TDT




                                                                  14
Network Analyzer
                                           [Dally]




• Stimulates network with swept-frequency source
• Measures network response amplitude and phase
• Can measure transfer function, scattering
  matrices, impedance, …
• Test set is configured differently for each kind of
  measurement to be performed
                                                        15
Directional Coupler
                                                      [Dally]




• Test sets in high-frequency network analyzers make use
  of directional couplers
• Directional couplers are two transmission lines coupled
  over a short distance
• If the short line is properly terminated, it allows for the
  voltage across ZA to be proportional to the forward
  traveling wave and the voltage across ZB to be
  proportional to any reflected wave
                                                                16
Transfer Function & Impedance
Measurements


                                                                    [Dally]




• Transfer function measurement
   • The input signal is from a directional coupler which samples the forward
     traveling wave
   • The network output serves as the output
• Impedance measurement
   • The input signal is from a directional coupler which samples the forward
     traveling wave
   • The reflected wave from the network is compared with this input to
     characterize the impedance over frequency
                                                                                17
Scattering (S) Parameters
• Why S Parameters?
  • Easy to measure
  • Y, Z parameters need open
    and short conditions
  • S parameters are obtained
    with nominal termination
  • S parameters based on         [Dally]
    incident and reflected wave
    ratio


                                      18
Formal S-Parameter Definitions



[Agilent]




                                 19
Cascading S-Parameters
• Network analysis allows cascading of
  independently characterized structures

• However, can’t directly cascade s-
  parameter matrices and multiply

• Must first convert to an ABCD matrix (or T
  matrix)

                                               20
ABCD Parameters



                                                              [Hall]


        v1               v1               i1               i1
     A               B               C               D
        v2 i             i2 v             v2 i             i2 v
               2 0             2 0             2 0             2 0




                       v1 A B v2
                            
                       ii C D i2


                                                                         21
Converting Between S & ABCD Parameters




                                     [Hall]




                                          22
Example: Cascaded Via & Transmission Line




• Taken from “Advanced Signal Integrity for High-Speed Digital Designs” by Hall
                                                                              23
Example: Cascaded Via & Transmission Line




• Using conversion table:


• Can also use T matrixes to cascade
• Taken from “Advanced Signal Integrity for High-Speed Digital Designs” by Hall
                                                                              24
S-Parameter Channel Example




     [Peters, IEEE Backplane Ethernet Task Force]
                                                    25
  S-Parameter Channel Example
  (4-port differential)



   Data from 50MHz to 15GHz in
           10MHz steps




                                            b1   S11    S12    S13    S14   a1   S11        S12    S13    S14   v 
                                           b   S        S 22   S 23   S 24  a2   S 21   S 22   S 23   S 24   0 
                                            2    21                                 
                                           b3   S31     S32    S33    S34   a3   S31        S32    S33    S34   v 
                                                                                                                 
                                           b4   S 41    S 42   S 43   S 44  a4   S 41       S 42   S 43   S 44   0 
[Hall]
                                     bd 1           1
                         S dd 11                   S11  S33  S13  S31 
                                     ad 1 a  a  0 2
                                          2   4


                                     bd 2           1
                         S dd 21                   S 21  S 43  S 23  S 41 
                                     ad 1 a  a  0 2
                                          2   4
                                                                                                                                   26
S-Parameter Channel Example


                      S11




           S21




                              27
Impulse Response
• Channel impulse responses are used in
  • Time domain simulations
  • Link analysis tools




                    Y    H  X  
                                     
             y t   ht   xt    ht   x 
                                    

                      ht   F 1H w
                                                         28
Generating an Impulse Response from
S-Parameters

                              ht   F          S  
• Perform the inverse                       1
  Fourier transform on the
  s-parameter of interest

• Step 1: For ifft, produce      Positive     Negative
  negative frequency values     Frequency    Frequency
  and append to s-
  parameter data in the
  following manner

    S  f   S  f 
                      




                                                            29
Increasing Impulse Response Resolution
• Could perform ifft now,
  but will get an impulse          For 1ps resolution:
  response with time            zero pad to +/-500GHz
  resolution of
     1         1
                     33.3ps
   2 f max 215GHz 

                                     zero padding
• To improve impulse
  response resolution
  expand frequency axis
  and “zero pad”


                                                         30
Channel Impulse Response
• Now perform ifft to      • Can sanity check by doing an
  produce impulse response   fft on impulse response and
                             comparing to measured data




                                                        31
Impulse Response of Different Channels


                7” Desktop/0Conn



             17” Refined BP/2Conn




     17” Legacy BP/2Conn




                                         32
Channel Transient Response




                 *




                             33
Eye Diagrams




[Walker]
               34
Eye Diagrams vs Data Rate




                            35
Eye Diagrams vs Channel




                          36
Inter-Symbol Interference (ISI)
• Previous bits residual state can distort the current bit,
  resulting in inter-symbol interference (ISI)
• ISI is caused by
   • Reflections, Channel resonances, Channel loss (dispersion)


       Single Input Bit


             Output Pulse
             Response




                                                                  37
                            ISI Impact
                        • At channel input (TX output), eye diagram is
                          wide open
                        • As data pulses propagate through channel, they
                          experience dispersion and have significant ISI
                                            • Result is a closed eye at channel output (RX input)
                                                                                                                                                                              Eye FFE1 10.0Gb/s [OPEN,1e-8] No Xtalk




                                                       INPUT
                                                                                                                                                       500mVDATA = RAND Tx 600mVpd AGC Gain -5.48dB
                                                                                                                                                            XTALK = NONE             AGC 5.0GHz 0.00dB

                                                                                                              Packaged SerDes
                                                                                                                                                            PKG=0/0 TERM = 5050/5050 IC = 3/3
                                                                                                                                                       400mV


                                              Eye FFE1 10.0Gb/s [OPEN,1e-8] No Xtalk                                                                   300mV

                       500mVDATA = RAND Tx 600mVpd AGC Gain -6.02dB
                                                                                                                                                       200mV
                            XTALK = NONE             AGC 5.0GHz 0.00dB




                                                                                                                                Signal Amplitude Vpd
                                                                                                      Backplane trace
                            PKG=0/0 TERM = 5050/5050 IC = 3/3
                       400mV
                                                                                                                                                       100mV

                       300mV
                                                                                                                                                       -0.0mV

                       200mV
                                                                                                                                                       -100mV
Signal Amplitude Vpd




                       100mV

                       -0.0mV
                                                                                                 Line card trace                                       -200mV

                                                                                                                                                       -300mVHSSCDR = 2.3.2-pre2 IBM Confidential
                                                                                                                                                             Date = Sat 01/21/2006 12:00 PM
                       -100mV                                                                                                                                PLL=0F1V0S0,C16,N32,O1,L80FREQ=0.00ppm/0.00us
                                                                                                                                                       -400mVFFE = [1.000, 0.000]



                                                                                                Edge connector
                       -200mV                                                                                                                          -500mV
                                                                                                                                                          -100ps            -50ps              0ps               50ps   100ps
                       -300mVHSSCDR = 2.3.2-pre2 IBM Confidential                                                                                                                             Time



                                                                                                                                                                                    OUTPUT
                             Date = Sat 01/21/2006 12:01 PM
                             PLL=0F1V0S0,C16,N32,O1,L80FREQ=0.00ppm/0.00us
                       -400mVFFE = [1.000, 0.000]




                                                                                                Via stub
                       -500mV
                          -100ps            -50ps              0ps               50ps   100ps
                                                              Time




                   [Meghelli (IBM) ISSCC 2006]

                                                                                                                                                                                                                                38
Next Time
• Channel pulse response model

• Modulation schemes




                                 39
