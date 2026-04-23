---
layout: post
title:      "lecture7 ee720 eq intro txeq"
date:       2026-04-21 09:55:32
author:     "Bert"
tags:
  - Fundamentals
  - Lecture
  - SerDes
  - TX
  - 深度学习
---

ECEN720: High-Speed Links
          Circuits and Systems
              Spring 2023

Lecture 7: Equalization Introduction & TX FIR Eq




                   Sam Palermo
           Analog & Mixed-Signal Center
               Texas A&M University
Announcements
• Lab 4 Report and Prelab 5 due Mar 10
• Exam 1 Mar 7
  • Covers material through Lecture 6
  • Previous years’ exam 1s are posted on the website for
    reference

• Equalization overview and circuits papers are posted
  on the website




                                                            2
Agenda
• Equalization theory and circuits
  • Equalization overview
  • Equalization implementations
     • TX FIR
     • RX FIR
     • RX CTLE
     • RX DFE
• TX FIR Equalization
  • FIR filter in time and frequency domain
  • MMSE Coefficient Selection
  • Circuit Topologies
• Equalization overview paper posted on website
                                                  3
High-Speed Electrical Link System




                                    4
Link with Equalization




                         Deserializer
   Serializer




                                        5
Channel Performance Impact




                             6
Channel Performance Impact




                             7
Channel Equalization
• Equalization goal is to flatten the frequency response out to the
  Nyquist Frequency and remove time-domain ISI




                                                                      8
TX FIR Equalization
• TX FIR filter pre-distorts transmitted pulse in
  order to invert channel distortion at the cost of
  attenuated transmit signal (de-emphasis)
                                                                R                                                              VDDA=1.2V
    Vout 0   I 1 D1  I 0 D0  I 1 D 1  I 2 D 2 TERM 
                                                                 2                                                 ESD
                                                                                                                                    50Ω

                                                                                                                                          Out-P


                                        VDD=1.0V                                 VDDA=1.2V                                                Out-N
                                                                     I-1                I0            I1              I2               (10Gb/s)
                                                       IDACs
                                                                           1/4               1             1/2             1/4
                                                         &
                                                        Bias
                                                       Control
                                                                           1x                4x            2x              1x


                           VDDIO=1.0V

                                                                 sgn-1              sgn0          sgn1           sgn2
                               1        2    (5Gb/s)
                      D0                                             D(1)               D(0)          D(-1)          D(-2)
                                                          L                         L             L              L
          (2.5Gb/s)




                               1        2
                      D1                     4:2
                               1        2   MUX
                      D2
                               1        2                 L      L                  L             L              L
                      D3


                                                   2
                                                      C2 (5GHz)
                                                   From on-chip PLL                 “A Low Power 10Gb/s Serial Link Transmitter in 90-nm
                                                                                    CMOS,” A. Rylyakov et al., CSICS 2005
                                                                                                                                                  9
6Gb/s TX FIR Equalization Example




•   Pros
     •   Simple to implement
     •   Can cancel ISI in pre-
         cursor and beyond filter
         span
     •   Doesn’t amplify noise
     •   Can achieve 5-6bit
         resolution
•   Cons
     •   Attenuates low
         frequency content due
         to peak-power limitation
     •   Need a “back-channel”
         to tune filter taps
                                    10
RX Equalization #1: RX FIR




• Pros
     • With sufficient dynamic range, can amplify
       high frequency content (rather than                                                                                 *
       attenuate low frequencies)
     • Can cancel ISI in pre-cursor and beyond
       filter span
     • Filter tap coefficients can be adaptively
       tuned without any back-channel
• Cons
     • Amplifies noise/crosstalk
     • Implementation of analog delays
     • Tap precision

*D. Hernandez-Garduno and J. Silva-Martinez, “A CMOS 1Gb/s 5-Tap Transversal Equalizer based on 3rd-Order Delay Cells,"
ISSCC, 2007.                                                                                                              11
RX Equalization #2: RX CTLE

                Vo+                 Vo-

             Din-                     Din+




•   Pros
     •   Provides gain and
         equalization with low
         power and area
         overhead
     •   Can cancel both pre-
         cursor and long-tail ISI

•   Cons
     •   Generally limited to 1st
         order compensation
     •   Amplifies noise/crosstalk
     •   PVT sensitivity
     •   Can be hard to tune
                                             12
RX Equalization #3: RX DFE
     Din                            DRX

                        clk
                  x           z-1
                 w1
                  x           z-1
                 w2




                  x           z-1
                 wn-1
                  x           z-1


•   Pros
                 wn


     •     No noise and crosstalk
           amplification
     •     Filter tap coefficients
           can be adaptively tuned
           without any back-
           channel

•   Cons
     •     Cannot cancel pre-
           cursor ISI
     •     Critical feedback timing
           path
     •     Timing of ISI
           subtraction complicates
           CDR phase detection
                                          13
Equalization Effectiveness
     Channel Responses




                                  Equalization
                                  Increasing


• Some observations:
  • Big initial performance boost with 2-tap TX eq.
  • With only TX eq., not much difference between 2 to 4-tap
  • RX equalization, particularly DFE, allows for further performance
    improvement
     • Caution – hard to build fast DFEs due to critical timing path
                                                                        14
Link with Equalization




                         Deserializer
   Serializer




                                        15
Channel Equalization
• Equalization goal is to flatten the frequency response out to the
  Nyquist Frequency and remove time-domain ISI




                                                                      16
    TX FIR Equalization – Time Domain
                                       For 10Gbps : W z   0.131  0.595 z 1  0.274 z 2




                    W   0.131 0.595  0.274

                Low Frequency Response (Sum Taps)
... 1 1 1 ...  0.131 0.595  0.274  ... 0.190 0.190 0.190 ...

   Nyquist Frequency Response (Sum Taps w/ Alternating Polarity)
   ...  1 1  1 ...  0.131 0.595  0.274  ... 1  1 1 ...
                                                                                           17
  TX FIR Equalization – Freq. Domain
                                             For 10Gbps : W z   0.131  0.595 z 1  0.274 z 2




         W  z   0.131  0.595 z 1  0.274 z 2
       w/ z  e j 2fTs  cos(2fTs )  j sin 2fTs                                              1 
                                                                 Nyquist Frequency Response  f      
           Low Frequency Response  f  0                                                        2Ts 

z  cos0  j sin(0)  1  W  f  0   0.190  14.4dB                                           1 
                                                            z  cos   j sin( )  1  W  f        1  0dB
                                                                                                   2Ts 

                                                                                           Note: Ts=Tb=100ps
 • Equalizer has 14.4dB of frequency peaking
       • Attenuates DC at -14.4dB and passes Nyquist frequency at 0dB
                                                                                                                  18
   TX FIR Coefficient Selection
  • One approach to set the TX FIR coefficients is a
    Minimum Mean-Square Error (MMSE) Algorithm


                                                                    TX Eq “w” Matrix
channel output vector, y                                    Rows = n+l-1 where n = tap number
Rows = k+n+l-2                                              Columns = l = input symbol number
where k = channel pulse model length
                           h0 0      0 ...    0          0       w0 0       0 ...     0          0     
       y 0                                                     w1 w0                                  c0 
                        h1 h0    0 ...    0          0                      0 ...   0           0                 
          y 1          ...
                                                                                                                  c  1
                                 ...   ... ...   ...       ...      ...   ...    ... ... ...        ...                 
           ...                                                                                            ... 
                                                                                                                
                        0     0     0 ... hk  1   hk  2  0       0      0 ... wn  1   wn  2              
   y l  n    k  3                                                                                        c l   1
                            0   0     0 ...    0       hk  1   0    0      0 ...   0        wn  1 

                               Channel “h” Matrix                                            l input symbols, c
                                Rows = k+n+l-2
                                Columns = n+l-1
                                                                                                                            19
 TX FIR Coefficient Selection
• Total system
                         h0 0     0 ...      0           0        w0 0         0 ...     0              0     
        y 0                                                                                                        c0 
                      h1 h0   0 ...      0            0   w1 w0        0 ...     0             0                 
        y 1          ...                                                                                             c  1
                               ...   ... ...   ...          ...   ...     ...       ... ...   ...           ...                
         ...                                                                                                      ... 
                      0     0     0 ... hk  1      hk  2  0      0         0 ... wn  1             
                                                                                                           w n  2               
 y l  n    k  3                                                                                                 c l   1
                          0   0     0 ...    0          hk  1   0   0         0 ...   0            wn  1 

• Multiplying input symbols by TX Eq., wc=w*c
                                             h0 0      0 ...      0            0   
                            y 0                                                     wc0 
                                          h1 h0    0 ...      0          0                   
                            y 1          ...                                          wc  1
                                                   ...   ... ...    ...        ...                   
                             ...                                                         ...      
                                          0     0      0 ... hk  1    hk  2                 
                     y l  n    k  3                                              wcn  l  1
                                              0   0      0 ...    0        hk  1 

• We desire the output vector, y, to be ISI free
                       y n   1, n  Channel pre - cursor sample #  Eq precursor tap #  1
               ydes   des
                       ydes n   0, n  Channel pre - cursor sample #  Eq precursor tap #  1
                                                                                                                                       20
Lone-Pulse Equalization Example
                                              Channel pulse matrix H with 5 pre-
• With lone-pulse equalization,               cursor samples and 10 post-cursor
  l=1 input symbols, i.e. c=[1]               samples, 3 columns for 3 eq taps
                                       Ydes
                                               0 0.0004     0    0     
                                                                       
                                               0 0.0010 0.0004     0 
                                                                       
                                               0 0.0023 0.0010 0.0004 
                                                                       
                          Channel pre-         0 0.0052 0.0023 0.0010 
                                                                       
                          cursor samples       0 0.0812 0.0052 0.0023 
                                                 
                                               0 0.3437 0.0812 0.0052
                                                                                   3-tap Eq
                                                                       
                                               1  0.1775 0.3437 0.0812          Matrix, W
                          Ydes(5+1+1=7)=1                              
                                                                       
                                               0 0.0917 0.1775 0.3437 
                                                                         w0
                                               0 0.0526 0.0917 0.1775         
                        Equalization pre-          
                                                                         w1 1
                                               0 0.0360 0.0526 0.0917         
                        cursor taps                                     w2 
                                               0 0.0224 0.0360 0.0526 
                                                                       
                                               0 0.0162 0.0224 0.0360 
                                                                              Symbol Matrix,
                                               0 0.0152 0.0162 0.0224 
                                                                                  C for
                                               0 0.0097 0.0152 0.0162
                                                                               “Lone Pulse”
                                               0 0.0090 0.0097 0.0152
                                                                       
                                               0 0.0067 0.0090 0.0097
                                                                       
                                               0 0 0.0067 0.0090       
                                                                       
                                               0  0     0 0.0067       
                                                                       
                                                                                                21
TX FIR Coefficient Selection
• We can calculate the error w.r.t. a desired output
                   E  Y  Ydes  HWC  Ydes  HW  Ydes with pulse input
• Computing the error matrix norm2
                              2
                            E  W T H T HW  2Ydes
                                                T
                                                   HW  Ydes
                                                          T
                                                             Ydes

• Differentiating this w.r.t. tap matrix taps to find taps which yield
  minimum error norm2
                              d  2
                                E  2W T H T H  2Ydes
                                                     T
                                                       H 0
                             dW
                                  W T H T H  Ydes
                                                T
                                                   H

• Solving for optimum TX Eq taps, W                            
                                                        Wls  H T H    HY
                                                                       1   T
                                                                                des


• This will yield a W matrix to produce a value of “1” at the output cursor,
  i.e. an FIR filter with gain
    • Need to normalize by the total abs(tap) sum for TX FIR realization
                                                  W n 
                                  Wlsnorm n   n ls
                                                 Wls n
                                               i 1
                                                                                      22
TX FIR Tap Resolution
• Using the above MMSE algorithm for the Refined
  Server Channel at 10Gb/s
      - 0.8180                                    - 0.1307 
                  normalizing by 6.2609                      
Wls  3.7245                           Wlsnorm  0.5949 
                                                             
      - 1.7184                                  - 0.2745 

    W  z   0.131  0.595 z 1  0.274 z 2
              1 pre main 1 post 
       0.131 0.595  0.274
• Generally, TX DAC resolution is limited to between
  4 to 6bits
• Mapping these equalization coefficients with this
  resolution may impact performance                 23
TX FIR Circuit Architectures
                                              Direct FIR
• Direct FIR vs Segmented DAC
• Direct FIR
  • Parallel output drivers for output taps
  • Each parallel driver must be sized to
    handle its potential maximum current
  • Lower power & complexity
  • Higher output capacitance                              [Zerbe]

• Segmented DAC
                                              Segmented DAC
  • Minimum sized output transistors to
    handle peak output current
  • Lowest output capacitance
  • Most power & complexity
     • Need mapping table (RAM)
     • Very flexible in equalization
                                                              [Zerbe]
                                                                     24
Direct FIR Equalization

                                                            R                                                              VDDA=1.2V
 Vout 0  I 1 D1  I 0 D0  I 1 D 1  I 2 D 2 TERM 
                                                             2                                                 ESD
                                                                                                                                50Ω

                                                                                                                                      Out-P


                                    VDD=1.0V                                 VDDA=1.2V                                                Out-N
                                                                 I-1                I0            I1              I2               (10Gb/s)
                                                   IDACs
                                                                       1/4               1             1/2             1/4
                                                     &
                                                    Bias
                                                   Control
                                                                       1x                4x            2x              1x


                       VDDIO=1.0V

                                                             sgn-1              sgn0          sgn1           sgn2
                           1        2    (5Gb/s)
                  D0                                             D(1)               D(0)          D(-1)          D(-2)
                                                      L                         L             L              L
      (2.5Gb/s)




                           1        2
                  D1                     4:2
                           1        2   MUX
                  D2
                           1        2                 L      L                  L             L              L
                  D3


                                               2
                                                  C2 (5GHz)
                                               From on-chip PLL                 “A Low Power 10Gb/s Serial Link Transmitter in 90-nm
                                                                                CMOS,” A. Rylyakov et al., CSICS 2005




                                                                                                                                              25
  Segmented DAC Example




                                                                             Sized only to
                                                                           deliver maximum
                                                                             total current




          Row = 4-bit data pattern              4 filtered bits
          Column = 6-bit weighting            (parallel) at 6-bit
                                                  resolution        [Casper ISSCC 2006]
 For this 4-bit pattern, send this 6-bit number
Combining taps in digital domain, not at output                                        26
Voltage-Mode TX FIR Driver #1




             [Wong JSSC 2004]                        [Sredojevic JSSC 2011]
• FIR equalization is typically more difficult to implement in voltage-mode
  drivers due to the series impedance
• An output voltage divider with a GND shunting path can realize the
  different voltage levels required by the FIR equalizer and also maintain
  impedance control
• Drawbacks to this approach
   • Output segmentation requires significant pre-dive logic whose complexity
     grows with equalization tap resolution
   • Time-varying current draw from the VREF supply
                                                                                27
Voltage-Mode TX FIR Driver #2




[Dettloff ISSCC 2010]                    [Sredojevic JSSC 2011]

• Adding a channel shunting path can realize the different
  voltage levels required by the FIR equalizer, maintain
  impedance control, and produce a constant current draw
  from the VREF supply
• The major drawback to this approach is even more
  complex output segmentation pre-drive logic
                                                              28
 Hybrid Voltage-Mode Driver
 with Current-Mode Equalization
[Song TCAS2 2012]




• A hybrid voltage-mode driver with current-mode equalization provides
  the advantages of both drivers
• The main driver tap is voltage-mode, which allows for reduced
  current for a given voltage swing
• High-resolution pre-emphasis equalization taps at minimum pre-drive
  complexity are possible with parallel current-mode drivers
• Does have some dynamic current variation, but is less than the
  original VM TX FIR #1

                                                                         29
     Impedance Modulated Equalization
       • Signaling power reduces as de-emphasis increases
       • Transition bits have 50 impedance
       • Longer run length data has higher impedance

        Segmented Implementation [2]




            [2] R. Sredojevic, et al., JSSC 2011
© 2014 IEEE                                     26.5: An 8-to-16Gb/s 0.65-to-1.05pJ/b 2-Tap Impedance-Modulated Voltage-Mode Transmitter with Fast
International Solid-State Circuits Conference   Power-State Transitioning in 65nm CMOS                                                               9 of 27
     Impedance Modulated Equalization
       • Signaling power reduces as de-emphasis increases
       • Transition bits have 50 impedance
       • Longer run length data has higher impedance

        Segmented Implementation [2]




            [2] R. Sredojevic, et al., JSSC 2011
© 2014 IEEE                                     26.5: An 8-to-16Gb/s 0.65-to-1.05pJ/b 2-Tap Impedance-Modulated Voltage-Mode Transmitter with Fast
International Solid-State Circuits Conference   Power-State Transitioning in 65nm CMOS                                                               10 of 27
      Relative Equalization Performance
       • Relative equalization performance depends on the channel
       • Channels with significant reflections (middle-trace
         backplane) can have >20% extra residual ISI
       • Well-controlled impedance channels (single-board CPW)
         display almost identical performance
                                          Channel Responses                                 10Gb/s Residual ISI w/ 2-tap EQ




© 2014 IEEE                                     26.5: An 8-to-16Gb/s 0.65-to-1.05pJ/b 2-Tap Impedance-Modulated Voltage-Mode Transmitter with Fast
International Solid-State Circuits Conference   Power-State Transitioning in 65nm CMOS                                                               11 of 27
                              Equalization Tap Control
       • Segmented pre-driver and output driver significantly
         increases dynamic power consumption with increased
         equalization resolution


                                                                                     Proposed non-segmented Implementation
        Segmented Implementation [2]




            [2] R. Sredojevic, et al., JSSC 2011
© 2014 IEEE                                     26.5: An 8-to-16Gb/s 0.65-to-1.05pJ/b 2-Tap Impedance-Modulated Voltage-Mode Transmitter with Fast
International Solid-State Circuits Conference   Power-State Transitioning in 65nm CMOS                                                               12 of 27
      TX Output Driver w/Analog Control
       • Global impedance modulation/control loops and voltage
         regulator allows for power amortization




                                                                                                                                           * EQ OFF-Mode




© 2014 IEEE                                     26.5: An 8-to-16Gb/s 0.65-to-1.05pJ/b 2-Tap Impedance-Modulated Voltage-Mode Transmitter with Fast
International Solid-State Circuits Conference   Power-State Transitioning in 65nm CMOS                                                                 13 of 27
             Impedance Modulated EQ Mode
       • Maximum transmitter output swing during a transition bit




© 2014 IEEE                                     26.5: An 8-to-16Gb/s 0.65-to-1.05pJ/b 2-Tap Impedance-Modulated Voltage-Mode Transmitter with Fast
International Solid-State Circuits Conference   Power-State Transitioning in 65nm CMOS                                                               14 of 27
             Impedance Modulated EQ Mode
       • De-emphasis transmitter output swing (Analog control)
         for run-length > 1




© 2014 IEEE                                     26.5: An 8-to-16Gb/s 0.65-to-1.05pJ/b 2-Tap Impedance-Modulated Voltage-Mode Transmitter with Fast
International Solid-State Circuits Conference   Power-State Transitioning in 65nm CMOS                                                               15 of 27
Next Time
• RX FIR
• RX CTLE
• RX DFE
• Alternate/Future Approaches




                                37
