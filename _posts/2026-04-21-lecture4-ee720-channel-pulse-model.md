---
layout: post
title:      "lecture4 ee720 channel pulse model"
date:       2026-04-21 09:26:01
author:     "Bert"
tags:
  - Channel
  - Fundamentals
  - Lecture
  - SerDes
  - 深度学习
---

ECEN720: High-Speed Links
         Circuits and Systems
             Spring 2023

Lecture 4: Channel Pulse Model & Modulation Schemes




                   Sam Palermo
           Analog & Mixed-Signal Center
               Texas A&M University
Announcements
• Lab 2 report and Prelab 3 due Feb 13

• Reference material
  • Peak distortion analysis paper by Casper
  • Notes from H. Song, Arizona State
  • Papers posted on PAM-2/4 transceivers




                                               2
Agenda
• ISI and channel pulse model

• Peak distortion analysis

• Compare NRZ (PAM-2) and PAM-4 modulation




                                        3
Inter-Symbol Interference (ISI)
• Previous bits residual state can distort the current bit,
  resulting in inter-symbol interference (ISI)
• ISI is caused by
   • Reflections, Channel resonances, Channel loss (dispersion)
• Pulse Response
                   y   1
                             t   c t   ht 
                                      1


      c 1 t                   ht                  c 1 t 
                                                                     y 1 t 




                                                                                  4
NRZ Data Modeling
• An NRZ data stream can be modeled as a
  superposition of isolated “1”s and “0”s

    Data = “1000101”



 “1” Symbol            ck1 t   u t  kT   u t  k  1T 


 “0” Symbol            ck0  t   ck1 t 
                                                1 t  0
[Song]                           where u t   
                                                0 t  0
                                                                      5
 NRZ Data Modeling
• An NRZ data stream can be modeled as a
  superposition of isolated “1”s and “0”s




                                        
                            Vi t    ckd k  t 
                                      k  

[Song]                                                  6
 Channel Response to NRZ Data
• Channel response to NRZ data stream is
  equivalent to superposition of isolated
  pulse responses




                                               
                                                     
         Vo t   H Vi t    H ckd k  t    y d k  t  kT 
[Song]                          k                k  
                                                                            7
Channel Pulse Response

                                                                    cursor




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

                                                                                          8
Channel Data Stream Response
           Input Data Stream




            Pulse Responses




           Channel Response




                               9
     Channel “FIR” Model
                   c01 t                                  
                                                 H c01 t   y01 t 


c01 t                                                                     a0




D is the delay from the                                                            a1
 channel input to the
   output pulse peak
                                                 
                                      H c01 t   y01 t          a-1         a2 a
                                                                                           3




                                  y(1)(t) sampled relative to pulse peak:
                [… 0.003 0.036 0.540 0.165 0.065 0.033 0.020 0.012 0.009 …]
             a =[ … a-2         a-1     a0     a1         a2       a3   a4    a5        a6     …]

                                                                                                    10
Agenda
• ISI and channel pulse model

• Peak distortion analysis

• Compare NRZ (PAM-2) and PAM-4 modulation




                                        11
Peak Distortion Analysis
• Can estimate worst-case eye
  height and data pattern from
  pulse response
• Worst-case “1” is summation
  of a “1” pulse with all
  negative non k=0 pulse
  responses
                                
    s1 t   y   (1)
                  0     t    y d  t  kT  y t kT 0
                                       k

                              k  
                               k 0


• Worst-case “0” is summation s t   y ( 0) t    y d  t  kT 
  of a “0” pulse with all positive
                                   0    0            
                                                    k  
                                                                     k

                                                                        y t  kT  0

                                                     k 0
  non k=0 pulse responses
                                                                                     12
  Peak Distortion Analysis
 • Worst-case eye height is s1(t)-s0(t)
                                                                                                              
                                                                                                              
                                          
                                                                                   
s t   s1 t   s0 t   y0 t   y0 t     y t  kT 
                              (1)       (0)               d k 
                                                                                  y t  kT 
                                                                                        d k 
                                                                                                               
                                                                 y t  kT  0                 y t  kT  0
                                                  k                          k                          
                                                  k 0                           k 0                         
                                                                        
                                      Because y0( 0 ) t   1 y0(1) t 

                                                                                                
                          (1)                                                                 
               s t   2 y0 t    y t  kT 
                                            1
                                                                    y t  kT 
                                                                          1
                                                                                                 
                                                   y t  kT  0                 y t  kT  0
                                    k                          k                          
                                     k 0                          k 0                         

                                  “1” pulse worst-                    “1” pulse worst-
                                  case “1” edge                       case “0” edge

 • If symmetric “1” and “0” pulses (linearity), then only
   positive pulse response is needed
                                                                                                             13
Peak Distortion Analysis Example 1




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
                                                     14
 Worst-Case Bit Pattern
• Pulse response can be used to find the worst-case bit pattern
                 Pulse a  ... a 2       a1    a0    a1    a2     a3    a4    a5    a6 ...

• Flip pulse matrix about cursor a0 and the bits are the inverted sign of
      the pulse ISI
 ... - sign a6   sign(a5 )  sign(a4 )  sign(a3 )  sign(a2 )  sign(a1 ) 1  sign(a1 )  sign(a2 ) ...

       Worst-Case Bit Pattern Eye                                         10kbits Eye




                                                                                                                  15
Peak Distortion Analysis Example 2
                                     y0(1) t   0.426
                         

                        y   t  kT  
                       k  
                                 1
                                             y t  kT  0
                                                               0.053
                       k 0
                          

                         y   t  kT  
                        k  
                                 1
                                              y t  kT  0
                                                               0.542
                         k 0

                   s t   20.426  0.053  0.542   0.338




                                                                         16
Agenda
• ISI and channel pulse model

• Peak distortion analysis

• Compare NRZ (PAM-2) and PAM-4 modulation




                                        17
PAM-2 (NRZ) vs PAM-4 Modulation
• Binary, NRZ, PAM-2
  • Simplest, most common modulation format
• PAM-4
  • Transmit 2 bits/symbol
  • Less channel equalization and circuits run ½ speed


              1                          10
                                        11

                                        01
               0                         00


                                                         18
Modulation Frequency Spectrum

          1                              10
                                         11

                                         01
          0                              00




     Majority of signal power   Majority of signal power
     in 1GHz bandwidth          in 0.5GHz bandwidth
                                                           19
Nyquist Frequency
• Nyquist bandwidth constraint:
   • The theoretical minimum required system bandwidth to detect RS
     (symbols/s) without ISI is RS/2 (Hz)

   • Thus, a system with bandwidth W=1/2T=RS/2 (Hz) can support a
     maximum transmission rate of 2W=1/T=RS (symbols/s) without ISI
                       1  R       R
                          S  W  S  2 (symbols/s/Hz)
                      2T   2      W

  • For ideal Nyquist pulses (sinc), the required bandwidth is only
    RS/2 to support an RS symbol rate

         Modulation      Bits/Symbol          Nyquist Frequency
             NRZ               1                   Rs/2=1/2Tb
            PAM-4              2                   Rs/2=1/4Tb

                                                                      20
NRZ vs PAM-4




• PAM-4 should be considered when
  • Slope of channel insertion loss (S21) exceeds reduction in PAM-4
    eye height
     • Insertion loss over an octave is greater than 20*log10(1/3)=-9.54dB
  • On-chip clock speed limitations
                                                                             21
PAM-4 Receiver




                             [Stojanovic JSSC 2005]

• 3x the comparators of NRZ RX

                                                 22
NRZ vs PAM-4 – Desktop Channel
                        Loss at 5GHz = -7.5dB



     Loss at 2.5GHz = -4.8dB




• Eyes are produced with 4-tap
  TX FIR equalization
• Loss in the octave between 2.5
  and 5GHz is only 2.7dB
  • NRZ has better voltage margin
                                                23
NRZ vs PAM-4 – T20 Server Channel


     Loss at 2.5GHz = -11.1dB



      Loss at 5GHz = -26.9dB




• Eyes are produced with 4-tap
  TX FIR equalization
• Loss in the octave between 2.5
  and 5GHz is 15.8dB
  • PAM-4 “might” be a better choice
                                       24
   PAM-4 Peak Distortion Analysis
Transmitter                Channel            Channel pulse response
  symbol                impulse response      A
                                                 c1         𝑦 𝑡   𝑐 𝑡 ∗𝑝 𝑡
 response                     𝑝 𝑡                             c2
                                                                   c3
    𝑐 𝑡                                                                 c4 c
                                      C-1                                   5   c5
                                                         Tb

               Tb
               PAM2 Eye Diagram                          PAM4 Eye Diagram
           a                                        a
                                            2a/3                                     2a/3
                                                   a/3
     2a                                                                              0
                                               -a/3
                                                                                     -2a/3
          -a                                        -a
            NRZ eye height                           PAM4 eye height
                                                       𝟏
          = 2(A –                                  = 2( A –
                                                          𝟑

  • PAM4 modulation is more sensitive to residual ISI
                                                                                             25
Multi-Level PAM Challenges
• Receiver complexity increases considerably
   • 3x input comparators (2-bit ADC)
   • Input signal is no longer self-referenced at 0V differential
      • Need to generate reference threshold levels, which will be dependent
        on channel loss and TX equalization

• CDR can display extra jitter due to multiple “zero
  crossing” times
• Smaller eyes are more sensitive to cross-talk due to
  maximum transitions
• Advanced equalization (DFE) can allow NRZ signaling to
  have comparable (or better) performance even with
  >9.5dB loss per octave
                                                                               26
Modulation Take-Away Points
• Loss-slope guidelines are a good place to start in
  consideration of alternate modulation schemes
• More advanced modulation trades-off receiver complexity
  versus equalization complexity
• Advanced modulation challenges
   • Peak TX power limitations
   • Setting RX comparator thresholds and controlling offsets
   • CDR complexity
   • Crosstalk sensitivity (PAM-4)

• Need link analysis tools that consider voltage, timing, and
  crosstalk noise to choose best modulation scheme for a
  given channel
                                                                27
Next Time
• Link Circuits
  • Termination structures
  • Drivers
  • Receivers




                             28
