---
layout: post
title:      "lecture8 ee720 rx adaptive eq"
date:       2026-04-21 10:00:51
author:     "Bert"
tags:
  - Fundamentals
  - Lecture
  - RX
  - SerDes
  - 深度学习
---

ECEN720: High-Speed Links
        Circuits and Systems
            Spring 2023

Lecture 8: RX FIR, CTLE, DFE, & Adaptive Eq.




                  Sam Palermo
          Analog & Mixed-Signal Center
              Texas A&M University
Announcements
• Lab 5 Report and Prelab 6 due Mar 27

• Equalization overview and circuits papers
  are posted on the website




                                              2
Agenda
• RX FIR equalization
• RX CTLE equalization
• RX DFE equalization
• Equalization adaptation techniques
• Advanced modulation/other techniques




                                         3
Link with Equalization




                         Deserializer
   Serializer




                                        4
TX FIR Equalization
• TX FIR filter pre-distorts transmitted pulse in order to invert channel
  distortion at the cost of attenuated transmit signal (de-emphasis)




                                                                            5
RX FIR Equalization
• Delay analog input signal and
  multiply by equalization
  coefficients
• Pros
   • With sufficient dynamic range, can
     amplify high frequency content
     (rather than attenuate low
     frequencies)
   • Can cancel ISI in pre-cursor and
     beyond filter span
   • Filter tap coefficients can be
     adaptively tuned without any
     back-channel
• Cons                                    [Hall]
   • Amplifies noise/crosstalk
   • Implementation of analog delays
   • Tap precision
                                                   6
RX Equalization Noise Enhancement
• Linear RX equalizers don’t discriminate between
  signal, noise, and cross-talk
  • While signal-to-distortion (ISI) ratio is improved, SNR
    remains unchanged




                                                   [Hall]

                                                              7
Analog RX FIR Equalization Example
• 5-tap equalizer with tap spacing of Tb/2
                                                                                   3rd-order delay cell




                                                                          1Gb/s experimental results




D. Hernandez-Garduno and J. Silva-Martinez, “A CMOS 1Gb/s 5-Tap Transversal Equalizer based on 3rd-Order Delay Cells,"
ISSCC, 2007.                                                                                                             8
Digital RX FIR Equalization
• Digitize the input signal with high-speed low/medium
  resolution ADC and perform equalization in digital domain
   • Digital delays, multipliers, adders
   • Limited to ADC resolution
• Power can be high due to very fast ADC and digital filters




                  [Hanumolu]

                                                               9
Digital RX FIR Equalization Example




• 12.5GS/s 4.5-bit Flash ADC in 65nm CMOS   [Harwood ISSCC 2007]
• 2-tap FFE & 5-tap DFE
• XCVR power (inc. TX) = 330mW, Analog = 245mW, Digital = 85mW
                                                              10
Agenda
• RX FIR equalization
• RX CTLE equalization
• RX DFE equalization
• Equalization adaptation techniques
• Advanced modulation/other techniques




                                         11
Link with Equalization




                         Deserializer
   Serializer




                                        12
RX Continuous-Time Linear Equalizer (CTLE)
• Passive R-C (or L) can implement
  high-pass transfer function to
  compensate for channel loss

• Cancel both precursor and long-tail
  ISI

• Can be purely passive or combined
  with an amplifier to provide gain

           Passive CTLE                    Active CTLE


                                           Vo+     Vo-

                                        Din-         Din+
   [Hanumolu]


                                                            13
Passive CTLE
• Passive structures offer excellent linearity,
  but no gain at Nyquist frequency

                                          R2          1  R1C1s
                             H s  
                                        R1  R2 1  R1 R2 C  C s
                                                             1  2
                                                   R1  R2
                                    1                        1
                            z         ,     p 
                                   R1C1               R1 R2
                                                             C1  C2 
                                                     R1  R2
                                            R2                  C1
   [Hanumolu]              DC gain               , HF gain 
                                          R1  R2             C1  C2
                                        HF gain  p R1  R2 C1
                          Peaking                 
                                        DC gain  z   R2 C1  C2




                                                                          14
Active CTLE
• Input amplifier with RC                                   [Gondi JSSC 2007]
  degeneration can provide
  frequency peaking with gain
  at Nyquist frequency
• Potentially limited by gain-
  bandwidth of amplifier
                                                                      1
                                                                s
• Amplifier must be designed                    g
                                        H s   m
                                                                    RS CS
  for input linear range                        C p  1  g m RS 2 
                                                     s               s 
                                                                                 1 
                                                            RS CS          RD C p 
   • Often TX eq. provides some
                                              1            1  g m RS 2                1
     low frequency attenuation        z        , p1                  , p2 
                                           RS CS              RS CS                RD C p
• Sensitive to PVT variations                       g m RD
                                     DC gain                 , Ideal peak gain  g m RD
  and can be hard to tune                        1  g m RS 2
                                                     Ideal peak gain  p1
• Generally limited to 1st-order   Ideal Peaking 
                                                        DC gain
                                                                    
                                                                      z
                                                                           1  g m RS 2

  compensation                                                                              15
Active CTLE Example

      Vo+   Vo-

   Din-       Din+




                      16
Active CTLE Tuning
• Tune degeneration resistor and capacitor to adjust zero
  frequency and 1st pole which sets peaking and DC gain

                                                      CS
• Increasing CS moves zero and
  1st pole to a lower frequency
  w/o impacting (ideal) peaking

• Increasing RS moves zero to                    RS
  lower frequency and increases
  peaking (lowers DC gain)
   • Minimal impact on 1st pole              1           1  g m RS 2
                                      z        , p1 
                                           RS CS            RS CS


                                                                        17
Agenda
• RX FIR equalization
• RX CTLE equalization
• RX DFE equalization
• Equalization adaptation techniques
• Advanced modulation/other techniques




                                         18
Link with Equalization




                         Deserializer
   Serializer




                                        19
RX Decision Feedback Equalization (DFE)
                                          ~                 ~              ~
• DFE is a non-linear     z k  yk  w1 d k 1   wn 1 d k n 1  wn d k  n
  equalizer

• Slicer makes a symbol
  decision, i.e.
  quantizes input

• ISI is then directly
  subtracted from the
  incoming signal via a
  feedback FIR filter


                                                                                    20
RX Decision Feedback Equalization (DFE)
                                                                ~                 ~              ~
• Pros                                          z k  yk  w1 d k 1   wn 1 d k n 1  wn d k  n
   • Can boost high frequency
     content without noise and
     crosstalk amplification
   • Filter tap coefficients can be
     adaptively tuned without any
     back-channel


• Cons
   • Cannot cancel pre-cursor ISI
   • Chance for error propagation
         • Low in practical links (BER=10-12)
   • Critical feedback timing path
   • Timing of ISI subtraction
     complicates CDR phase
     detection                                                                                [Payne]

                                                                                                          21
DFE Example
• If only DFE equalization, DFE tap coefficients
  should equal the unequalized channel pulse
  response values [a1 a2 … an]

• With other equalization, DFE tap coefficients
  should equal the pre-DFE pulse response values
    •   DFE provides flexibility in the optimization of other
        equalizer circuits
    •   i.e., you can optimize a TX equalizer without caring
        about the ISI terms that the DFE will take care of
                                           [w1 w2]=[a1 a2]




                                                   a1
                                                        a2




                                                                22
  Direct Feedback DFE Example (TI)
                                                                                                               TAP1: 5 bits
• 6.25Gb/s 4-tap DFE




                                                                                             to demux
                                                                       A2
                                                                                                               TAP2: 4 bits + sign
                                                          CLK0/180                                             TAP3,4: 3 bits + sign
       • ½ rate architecture
       • Adaptive tap algorithm                                                                                               DFECLK




                                                                       A2
                                                                                         Latch             Latch      Latch
                                                                 VDD
       • Closes timing on 1st




                                                                                                                                  to demux
         tap in ½ UI for                           RXIN
                                                            A1
                                                                   RXEQ
         convergence of both




                                                                              TAP1



                                                                                      TAP2



                                                                                                        TAP3



                                                                                                                   TAP4
         adaptive equalization
         tap values and CDR                               CLK90/270                      Latch             Latch      Latch



                             Feedback tap mux




R. Payne et al, “A 6.25-Gb/s Binary Transceiver in 0.13-um CMOS for Serial Data Transmission Across High Loss
Legacy Backplane Channels,” JSSC, vol. 40, no. 12, Dec. 2005, pp. 2646-2657                                                                  23
Direct Feedback DFE Critical Path



                     A1




                              A2
                                              [Payne]




            tCLK QSA  t PROPMUX  t PROPA 2  1UI
• Must resolve data and feedback in 1 bit period
  • TI design actually does this in ½UI for CDR
                                                        24
 DFE Loop Unrolling
                                                       dk|dk-1=1

                                                                                      dk-1
                                   yk


                                                        dk|dk-1=-1
                                                                [Stojanovic]


• Instead of feeding back and
  subtracting ISI in 1UI
• Unroll loop and pre-compute 2
  possibilities (1-tap DFE) with
  adjustable slicer threshold                               dk|dk-1=1

                                        =w1                             dk|dk-1=-1

• With increasing tap number,             ~    
                                                              
                                                                         ~
                                                sgn yk w1 " if" d k 1  1
                                          dk  
  comparator number grows as 2#taps                                    ~
                                               sgn  yk  w1  " if" d k 1  1
                                                                                             25
DFE Resistive-Load Summer



                                                         [Park]
                    Summer Swing  IR,   RC

• Summer performance is critical for DFE operation
• Summer must settle within a certain level of accuracy
  (>95%) for ISI cancellation
• Trade-off between summer output swing and settling time
• Can result in large bias currents for input and taps
                                                                  26
DFE Integrating Summer




                                                       [Park ISSCC 2007]




• Integrating current onto load capacitances eliminates RC settling time

• Since T/C > R, bias current can be reduced for a given output swing
   • Typically a 3x bias current reduction
                                                                           27
Digital RX FIR & DFE Equalization Example




• 12.5GS/s 4.5-bit Flash ADC in 65nm CMOS   [Harwood ISSCC 2007]
• 2-tap FFE & 5-tap DFE
• XCVR power (inc. TX) = 330mW, Analog = 245mW, Digital = 85mW
                                                              28
DFE with Feedback FIR Filter




                                     [Liu ISSCC 2009]




• DFE with 2-tap FIR filter in feedback will
  only cancel ISI of the first two post-cursors
                                                   29
“Smooth” Channel


                                                                        t
                                                                    
                                                                H 2e 




                             [Liu ISSCC 2009]

• A DFE with FIR feedback requires many taps to cancel ISI
• Smooth channel long-tail ISI can be approximated as
  exponentially decaying
   • Examples include on-chip wires and silicon carrier wires
                                                                            30
 DFE with IIR Feedback
[Liu ISSCC 2009]




• Large 1st post-cursor H1 is canceled with normal FIR
  feedback tap
• Smooth long tail ISI from 2nd post-cursor and beyond is
  canceled with low-pass IIR feedback filter
• Note: channel needs to be smooth (not many reflections) in
  order for this approach to work well                     31
DFE with IIR Feedback RX Architecture




                             [Liu ISSCC 2009]

                                           32
 Merged Summer & Partial Slicer
[Liu ISSCC 2009]




 • Integrating summer with regeneration PMOS devices to
   realize partial slicer operation
                                                          33
 Merged Mux & IIR Filter
[Liu ISSCC 2009]




 • Low-pass response (time constant) implemented by RD and CD
 • Amplitude controlled by RD and ID
 • 2 UI delay implemented through mux to begin cancellation at 2nd
   post-cursor

                                                                     34
Agenda
• RX FIR equalization
• RX CTLE equalization
• RX DFE equalization
• Equalization adaptation techniques
• Advanced modulation/other techniques




                                         35
Setting Equalizer Values
• Simplest approach to setting equalizer values (tap weights,
  poles, zeros) is to fix them for a specific system
   • Choose optimal values based on lab measurements
   • Sensitive to manufacturing and environment variations


• An adaptive tuning approach allows the optimization of the
  equalizers for varying channels, environmental conditions,
  and data rates

• Important issues with adaptive equalization
   • Extracting equalization correction (error) signals
   • Adaptation algorithm and hardware overhead
   • Communicating the correction information to the equalizer circuit
                                                                         36
TX FIR Adaptation Error Extraction
• While we are adapting the TX
  FIR, we need to measure the
  response at the receiver input

• Equalizer adaptation (error)
  information is often obtained
  by comparing the receiver
  input versus the desired
  symbol levels, dLev

• This necessitates additional
  samplers at the receiver with
  programmable threshold levels
                                   [Stojanovic JSSC 2005]
                                                            37
  TX FIR Adaptation Algorithm
• The sign-sign LMS algorithm is
  often used to adapt equalization
  taps due to implementation
  simplicity
                    wnk1  wnk   wsign d n  k sign en 

w  tap coefficients, n  time instant, k  tap index, d n  received data,

           en  error with respect to desired data level, dLev

• As the desired data level is a
  function of the transmitter swing
  and channel loss, the desired data
  level is not necessarily known and
  should also be adapted
                       dLevn 1  dLevn   dLevsign en 

                                                            [Stojanovic JSSC 2005]   38
TX FIR Common-Mode Back-Channel
• In order to communicate FIR tap update information
  back to the TX, a back-channel is necessary
• One option is to use low data rate (~10Mb/s) common-
  mode signaling from the RX to TX on the same
  differential channel




                        [Stojanovic JSSC 2005]           39
TX FIR Data Encoder Back-Channel
• Another option is to use a high-speed TX channel on the
  RX side that communicates data back to the TX under
  adaptation
• Flexibility in data encoding (8B10B/Q) allows low data
  rate tap adaptation information to be transmitted back
  without data rate overhead




                    [Stonick JSSC 2003]                     40
CTLE Tuning with PSD Measurement
• One approach to CTLE tuning is to compare low-frequency
  and high-frequency spectrum content of random data
• For ideal random data, there is a predictable ratio between
  the low-frequency power and high-frequency power
• The error between these power components can be used in
  a servo loop to tune the CTLE

                                      sin fTb 
                                                      2

                       sx  f   Tb             
                                      fTb 
                  fm                
                                                          1
                   s  f df   s  f df  4
                  0
                        x
                                    fm
                                         x



                                             0.28
                            where f m 
                                              Tb


                                 [Lee JSSC 2006]              41
CTLE Tuning
w/ Output Amplitude Measurement
• CTLE tuning can also be done by comparing low-frequency and high-
  frequency average amplitude
• Approximating the equalized data as a sine wave, a predictable ratio
  exists between the low frequency average and high-frequency average
• Equalizer settings are adjusted until the high frequency peak-to-peak
  swing matches the low-frequency peak-to-peak swing




                           [Uchiki ISSCC 2008]                        42
CTLE Tuning
w/ Data Edge Distribution Monitoring
• The width and shape of the data
  edge distribution can be used to
  reliably calibrate an equalizer
• By oversampling the data bits
  with sub-period accuracy, this
  information can be obtained
• Objective is to maximize eye
  opening, or equivalently
  minimizing the standard
  deviation of the edge distribution




                          [Gerfers JSSC 2008]   43
DFE Tuning – FIR Feedback




• 2x oversampling the equalized signal at the edges can be
  used to extract information to adapt a DFE and drive a
  CDR loop
• Sign-sign LMS algorithm used to adapt DFE tap values
                       [Payne JSSC 2005]                     44
 DFE Tuning – IIR Feedback




[Huang ISSCC 2011]           45
Agenda
• RX FIR equalization
• RX CTLE equalization
• RX DFE equalization
• Equalization adaptation techniques
• Advanced modulation/other techniques




                                         46
Advanced Modulation
• In order to remove ISI, we attempt to
  equalize or flatten the channel response
  out to the Nyquist frequency
• For less frequency-dependent loss, move
  the Nyquist frequency to a lower value via
  more advance modulation
  • 4-PAM (or higher)
  • Duo-binary

• Refer to lecture 4 for more details
                                               47
    Multi-tone Signaling
         30Gb/s total in 2 bands                  56Gb/s total in 15 bands




                                                          [Kim ISSCC 2019]
10Gb/s duo-binary           2 Quarature
                            10Gb/s duo-binary
[Beyene AdvPack 2008]

   •   Instead equalizing out to baseband Nyquist frequency
   •   Divide the channel into bands with less frequency-dependent loss
   •   Should result in less equalization complexity for each sub-band
   •   Requires up/down-conversion
   •   Discrete Multi-tone used in DSL modems with very challenging channels
       • Lower data rates allow for high performance DSP
       • Recently seeing this in some high-speed link research prototypes    48
Next Time
• Link Noise and BER Analysis




                                49
