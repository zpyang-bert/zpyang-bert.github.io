---
layout: post
title:      "lecture13 ee720 fwd clk deskew"
date:       2026-04-21 10:23:10
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

Lecture 13: Forwarded Clock Deskew Circuits




                 Sam Palermo
         Analog & Mixed-Signal Center
             Texas A&M University
Announcements
• Project Preliminary Report due today
• Exam 2 Apr 25
  • Focuses on material from Lectures 7-14
  • Previous years’ Exam 2s are posted on the website for
    reference

• Project Final Report due May 2
• Project Presentations May 4 (12:30PM-2:30PM)




                                                            2
Agenda
• Forwarded Clock I/O Overview
• Data & Clock Skew Performance Impact
• Jitter Impulse Response and Jitter Transfer
  Function
• Forwarded Clock Deskew Architectures
  • PLL/PI
  • DLL/PI
  • ILO
    • Fundamental, Super-Harmonic, Sub-Harmonic

                                                  3
Forwarded Clock I/O Architecture
                  • Common high-speed reference
                    clock is forwarded from TX chip
                    to RX chip
                      • Mesochronous system
                  • Used in processor-memory
                    interfaces and multi-processor
                    communication
                      • Intel QPI
                      • Hypertransport
                  • Requires one extra clock
                    channel
                  • “Coherent” clocking allows low-
                    to-high frequency jitter tracking
                  • Need good clock receive
                    amplifier as the forwarded clock
                    is attenuated by the channel
                                                      4
Forwarded Clock I/O Limitations
                  • Clock skew can limited forward
                    clock I/O performance
                     • Driver strength and loading
                       mismatches
                     • Interconnect length
                       mismatches


                  • Low pass channel causes jitter
                    amplification

                  • Duty-Cycle variations of
                    forwarded clock




                                                     5
Forwarded Clock I/O De-Skew
                • Per-channel de-skew allows for
                  significant data rate increases

                • Sample clock adjusted to center
                  clock on the incoming data eye

                • Implementations
                   • Delay-Locked Loop and Phase
                     Interpolators
                   • Injection-Locked Oscillators

                • Phase Acquisition can be
                   • BER based – no additional
                     input phase samplers
                   • Phase detector based
                     implemented with additional
                     input phase samplers
                     periodically powered on
                                                    6
Forwarded Clock I/O Circuits
                  • TX PLL
                  • TX Clock Distribution
                  • Replica TX Clock Driver
                  • Channel
                  • Forward Clock Amplifier
                  • RX Clock Distribution
                  • De-Skew Circuit
                     • PLL/PI
                     • DLL/PI
                     • Injection-Locked Oscillator
                                                     7
 Data & Clock Skew Performance Impact
• High speed forwarded clock
allows jitter tracking
between clock and data

•Clock to data skew causes
that high frequency clock
and data jitters become out
of phase on the receiver




                                        8
Impact of Clock to Data Skew on Jitter
Tracking
                              Jitter Frequency = 100MHz
                                                data jitter
             0.5
 JD(UI)




               0                                                                                        𝐽       𝐽 sin 2𝜋𝑓 𝑈𝐼 · 𝑛
             -0.5
                    0   0.1   0.2   0.3   0.4       0.5        0.6   0.7   0.8   0.9
                                                                                          -8
                                                                                              1
                                                                                                      skew of mUI between
                                                                                       x 10
                                                clock jitter                                             data and clock
             0.5
 JC(UI)




               0
                                                                                                  𝐽    𝐽 sin 2𝜋𝑓 𝑈𝐼 · 𝑛        2𝑚𝜋𝑓 𝑈𝐼
             -0.5
                    0   0.1   0.2   0.3   0.4       0.5        0.6   0.7   0.8   0.9          1
                                                                                          -8
                                                                                       x 10
                                           differential jitter
             0.5
 Jdiff(UI)




               0                                                                                            𝐽         𝐽    𝐽
             -0.5
                    0   0.1   0.2   0.3   0.4       0.5        0.6   0.7   0.8   0.9          1
                                                   time                                   -8
                                                                                       x 10



                                                     UI = 100ps
                                           Assuming 5UI skew in this example
                                                                                                                                    9
Impact of Clock to Data Skew on Jitter
Tracking
                                     Jitter Frequency = 200MHz

                                                        data jitter
                    0.5
        JD(UI)


                      0

                    -0.5
                           0   0.1    0.2   0.3   0.4       0.5        0.6   0.7   0.8   0.9          1
                                                                                                  -8
                                                                                               x 10
                                                        clock jitter
                    0.5
        JC(UI)




                      0

                    -0.5
                           0   0.1    0.2   0.3   0.4       0.5        0.6   0.7   0.8   0.9          1
                                                                                                  -8
                                                                                               x 10
                                                   differential jitter
                    0.5
        Jdiff(UI)




                      0

                    -0.5
                           0   0.1    0.2   0.3   0.4       0.5        0.6   0.7   0.8   0.9          1
                                                           time                                   -8
                                                                                               x 10




                                                                                                          10
Impact of Clock to Data Skew on Jitter
Tracking
                                           Jitter Frequency = 400MHz
                                                              data jitter
                          0.5
              JD(UI)
                            0

                          -0.5
                                 0   0.1    0.2   0.3   0.4       0.5        0.6   0.7   0.8   0.9          1
                                                                                                        -8
                                                                                                     x 10
                                                              clock jitter
                          0.5
              JC(UI)




                            0

                          -0.5
                                 0   0.1    0.2   0.3   0.4       0.5        0.6   0.7   0.8   0.9          1
                                                                                                        -8
                                                                                                     x 10
                                                         differential jitter
                          0.5
              Jdiff(UI)




                            0

                          -0.5
                                 0   0.1    0.2   0.3   0.4       0.5        0.6   0.7   0.8   0.9          1
                                                                 time                                   -8
                                                                                                     x 10




  The clock skew flips the jitter phase of clock faster for higher frequency
  jitter and results in higher differential jitter
                                                                                                                11
Impact of Clock to Data Skew
on Jitter Tracking
• Assuming infinite jitter
  tracking bandwidth (JTB)
• For a given skew, as the
  jitter frequency increases
  the differential jitter
  increases and become a
  maximum of 2X
• For a given jitter frequency,
  at a skew of 1/(6fj) the
  system will have a
  differential jitter greater
  than 1                          12
Optimum Jitter Tracking for 200MHz jitter
• Limit the JTB by attenuating the clock jitter using amplitude response
  of low pass function with pole frequency = JTB
• 𝐽    𝐽 sin 2𝜋𝑓 𝑈𝐼 · 𝑛   2𝑚𝜋𝑓 𝑈𝐼
                                        Jitter Frequency = 200MHz
• 𝐽    𝐽 |     |



 In 10Gb/s system,
 UI = 100ps




 Controllable JTB over
 70 - 800MHz is
 desired



                                                                           13
       Jitter Impulse Response(JIR) and Jitter Transfer
       Function(JTF) Analysis Method
         • JIR: test the system response on jitter
         • JTF: ratio of output to input jitter as a function of frequency,
           DTFT of JIR
                    Extraction of JIR in ½ rate system where both clock edges are using

                                                                              Ideal clock waveform superimposed with
                                                                              clock incorporating jitter impulse stimulus

                                                                              Output clock waveforms using ideal
                                                                              clock versus jitter impulse clock



                                                                               Jitter impulse response



      • A clock system’s effect on an input jitter sequence can be evaluated
        by convolving the jitter sequence with the jitter impulse response
B. Casper and F. O’Mahony, “Clocking analysis, implementation and measurement techniques for high-speed data links a tutorial,” IEEE Trans.
Circuits Syst. I, vol. 56, no. 1, pp. 683–688, Jan. 2009.
                                                                                                                                              14
       Filter/Amplifier Frequency Response
       & Jitter Transfer Response
                                                                                  • Low-pass frequency response
                                                                                    (buffer, distribution
                                                                                    interconnect) is similar to a
                                                                                    high-pass jitter filter
                                                                                          • High frequency jitter is
                                                                                            amplified
                                                                                  • High-pass frequency response
                                                                                    (AC coupling cap) is similar to an
                                                                                    all-pass jitter filter, except for
                                                                                    Nyquist-rate jitter (duty cycle
                                                                                    error)
                                                                                  • Band-pass frequency response
                                                                                    (band-pass filter) is similar to a
                                                                                    low-pass jitter filter with the
                                                                                    center frequency aligned with
                                                                                    the fundamental clock frequency
B. Casper and F. O’Mahony, “Clocking analysis, implementation and measurement techniques for high-speed data links a tutorial,” IEEE Trans.
Circuits Syst. I, vol. 56, no. 1, pp. 683–688, Jan. 2009.
                                                                                                                                              15
            Jitter Amplification
           • Low-pass frequency response (buffer, distribution
             interconnect) is similar to a high-pass jitter filter
                  • High frequency jitter is amplified as it propagates
                    across the channel
                                                                                              Jitter Transfer/Amplification
                       Channel Response                                                 3
            0




                                                         Jitter Amplification Factor
           -10                                                                         2.5


           -20
                                                                                        2
S21 (dB)




           -30
                                                                                       1.5
           -40

                                                                                        1
           -50


           -60                                                                         0.5
              0    2    4     6     8     10   12   14                                    0      1      2        3     4             5
                            Frequency (GHz)                                                            Frequency(Hz)          x 10
                                                                                                                                     9



                                                                                                                           16
       PLL or DLL/PI Forwarded Clock Deskew
                               • TX clock is forwarded along an independent
                                 channel to the RX chip where it is distributed
                                 to the RX channels
                                                                               • The PLL or DLL locks onto
                                                                                 the forwarded clock and
                                                                                 serves as a multi-phase
                                                                                 generator and a jitter filter

                                                                               • The PI mixes the phases to
                                                                                 produce sampling clocks at
                                                                                 the optimal phase for
                                                                                 maximum timing margin or
                                                                                 BER
B. Casper and F. O’Mahony, “Clocking analysis, implementation and measurement techniques for high-speed data links a tutorial,” IEEE Trans.
Circuits Syst. I, vol. 56, no. 1, pp. 683–688, Jan. 2009.
                                                                                                                                              17
PLL/PI Forwarded Clock Deskew Example




                                    [Prete ISSCC 2006]
• Fully buffered DIMM transceiver
                                                    18
 PLL/PI Forwarded Clock Deskew Example
• PLL low-pass jitter transfer characteristic filters high
  frequency jitter
    • Desired for uncorrelated jitter
    • Not desired for correlated high frequency jitter

                                                • PLL disadvantages
                                                    • Jitter accumulation in
                                                      VCO
                                                    • Stability
                                                    • More area and
                                                      complex than DLL
                                                      implementations



[Prete ISSCC 2006]
                                                                          19
 DLL/PI Forwarded Clock Deskew Example
• DLL displays an all-pass jitter transfer function
   • Desired for correlated jitter
   • Not desired for uncorrelated jitter

                                           • DLL advantages
                                              • No jitter accumulation
                                              • Inherently stable
                                              • Simpler and less area
                                                than PLL

                                           • Finite bandwidth of DLL
                                             delay line can result in
                                             jitter amplification

[Balamurugan JSSC 2008]
                                                                         20
            Injection Locking in LC Tanks

a) a free-running oscillator
consisting of an ideal
positive feedback amplifier
and an LC tank;

b) we insert a phase shift in
the loop. We know this will
cause the oscillation
frequency to shift since the
loop gain has to
have exactly 2π phase shift
(or multiples).




                                            21
          Phase Shift for Injected Signal


• Assume the oscillator “locks” onto the injected
current and oscillates at the same frequency.

• Since the locking signal is not in general at
the resonant center frequency, the tank
introduces a phase shift

• In order for the oscillator loop gain to be equal
to unity with zero phase shift, the sum of the
current of the transistor and the injected
currents must have the proper phase shift to
compensate for the tank phase shift.




                                                      22
       Injection Locked Oscillator Phasors
0  Tank impedance phase shift
  Phase shift between injected clock and output signal




  Note that the frequency of the injection signal determines the extra phase shift
  Φ0 of the tank. This is fixed by the frequency offset.
   The current from the transistor is fed by the tank voltage, which by definition
  the tank current times the tank impedance, which introduces Φ0 between the
  tank current/voltage.
   The angle between the injected current and the oscillator current θ must be
  such that their sum aligns with the tank current.
                                                                                      23
                    Injection Geometry




The geometry of the problem implies the following constraints on the injected
current amplitude relative to the oscillation amplitude.


                                                                                24
                                                      Locking Range
              I inj                             I inj sin 
 sin 0              sin  
              IT                        2
                                      I osc  I inj
                                                 2
                                                     2 I osc I inj cos 
                           I inj                      I inj
  sin 0,max                     , if . cos   
                          I osc                       I osc
A second‐order parallel tank consisting of L. C, Rp
exhibits a phase shift of:
             L     02
 0   tan (    1
                            )
     2         R p 02   2
                                       L  1 
  02   2  20 (0   ),               ,  tan 1 ( x)  tan 1 ( x 1 )
                                        Rp  Q 2
              2Q
  tan 0            (0   )
              0
                                                                                 Source: Razavi
              I inj
  tan 0            , I T  I osc
                                2
                                     I inj
                                         2

               IT

 At the edge of the lock range, the injected current is orthogonal to the tank current.

 The phase angle between the injected current and the oscillator is 90° + Φ0,max
                                                                                                  25
                                                  Locking Range
         I inj       2Q
                        ( 0   )
         IT          0
     I inj I osc I inj                      1
                      
     I osc I T    I osc                            2
                                                I inj                I inj  I osc
                                        1        2
                                                I osc
                                                                                               0       I inj
     
         I inj
                 
                          1
                                        
                                            2Q
                                                  ( 0   )
                                                                       , L   0   inj         
         I osc                     2        0                                                 2Q I osc
                              I   inj
                     1         2
                              I osc                                                                        I inj
                                                                     When : 0  10GHz, Q  5, K                   0.1
                                   0 I inj                                                                I osc
                                                         1
       0   inj                                                   , L  100 MHz
                               2Q I osc                         2
                                                             I inj
                                                        1     2
                                                             I osc

   Locking range is inversely proportional to oscillator Q

                                                                                                                           26
Digital Controlled Oscillator (DCO) with Injection Locking




Shekhar, Sudip et al, “Strong Injection Locking in Low-Q LC Oscillators: Modeling and Application in a Forwarded-Clocked I/O
Receiver”, IEEE JSSC, 2009.



The digitally controlled switch-capacitor bank tunes the free-running
frequency of DCO to adjust the phase of the forwarded clock and also
compensate for PVT.
                                                                                                                               27
Ring Oscillator ILO Example




                              [Hu JSSC 2010]   28
 Ring Oscillator ILO Example




[Hu JSSC 2010]
                               29
ILO Jitter Transfer
• ILOs have a first-order low-pass                                  JTFINPUT 
                                                                                     1
                                                                                         s
  filter function to input (injection                                            1
                                                                                         P
  clock) jitter
                                                                                     s
• ILOs have a first-order high-pass                                  JTFVCO 
                                                                                 P
                                                                                         s
  filter function to VCO jitter                                                 1
                                                                                     P

                                                              K2
          where P is the jitter tracking bandwidth : P          2

                                                              A2
                                                             2Q
                   For a parallel RLC resonant tank : A 
                                                             o

                                                                       A   
        is a function of the desired de - skew phase :  ss  sin 1   
                                                                       K   

                                                                                              30
ILO Jitter Transfer
                                                       1
                                     JTFINPUT 
                                                           s
                                                   1
                                                        P


                                               K2
                                      P           2

                                               A2

                                                  A    
                                      ss  sin 1   
                                                  K    

                                [Hossain JSSC 2009]


• ILO jitter transfer bandwidth decreases as the
  oscillator is locked further from the free-running
  frequency, o, to obtain a larger phase shift ss
                                                               31
ILO Jitter Transfer
                                                      1
                                    JTFINPUT 
                                                          s
                                                  1
                                                       P


                                              K2
                                     P           2

                                              A2

                                                 A    
                                     ss  sin 1   
                                                 K    

                               [Hossain JSSC 2009]



• ILO jitter transfer bandwidth increases with
  injection strength
                                                              32
ILO Jitter Transfer
                                                      1
                                    JTFINPUT 
                                                          s
                                                  1
                                                       P


                                              K2
                                     P           2

                                              A2

                                                 A    
                                     ss  sin 1   
                                                 K    

                               [Hossain JSSC 2009]



• ILO jitter transfer bandwidth increases with
  injection strength
                                                              33
ILO Phase Noise Filtering
                               2                 2
              S out  JTFinput Sinj  JTFVCO SVCO
                                                                         • Up to jitter tracking
                                       K
                                            2

                                            cos 2  ss Sinj   2 SVCO
                                                                           bandwidth, ILO output
                                         
                     P Sinj   SVCO  A 
                      2         2

S out  jitter                                                         phase noise is dominated
                         P  
                            2    2
                                          K
                                               2

                                            cos  ss  
                                           A
                                                      2          2
                                                                           by injection clock
                                                                           • Can be better than VCO
                                                                           • JTB depends on desired
                                                                             de-skew phase


                                                                         • At high frequencies, VCO
                                                                           phase noise dominates




                                                                  [Hossain JSSC 2009]                 34
Ring Oscillator Super-Harmonic ILO Example

• Potential system application
  • ½ rate TX forwards clock to
    ¼ rate RX




                                                  [Hossain JSSC 2009]
                  f osc  mf inj   Here m  0.5
                                                                   35
Super-Harmonic ILO Phase Noise Filtering
                                                            2
                                                        K
                                                    2
                                                      m   cos 2 m ss S inj   2 SVCO
                                   S out  jitter     2
                                                         A
                                                         K
                                                           cos m ss  
                                                                   2             2

                                                          A




   f osc  mf inj   Here m  0.5


• Low frequency phase
  noise is actually better
  than injection oscillator
  by m2
                                              [Hossain JSSC 2009]
                                                                                           36
Ring Oscillator Sub-Harmonic ILO
Example w/ Clock Signal Injection
• Forwarding a lower speed clock avoids jitter
  amplification over low-pass channel

• Sub-Harmonic
  injection with clock
  signal can cause
  significant ILO
  amplitude variations
  and sub-harmonic
  spurious tones

                                  [Hossain ISSCC 2010]
                                                         37
Ring Oscillator Sub-Harmonic ILO
Example w/ Pulse Train Signal Injection
• Forwarding a pulse train signal reduces
  amplitude variations and ILO spurious tones

• Adjusting pulse
  width, d, changes
  effective injection
  strength and can
  be used to adjust
  jitter tracking
  bandwidth

                                 [Hossain ISSCC 2010]
                                                        38
 Effective Injection Strength of Pulse Train




[Hossain ISSCC 2010]




• Wider pulse separation (lower frequency sub-
  harmonics) reduces effective injection strength
                                                    39
Adjusting Jitter Tracking Bandwidth
w/ Pulse Train Signal




                                           [Hossain ISSCC 2010]
• Wider pulse separation (lower frequency sub-harmonics)
  reduces effective injection strength and results in lower
  jitter tracking bandwidth
• Reducing pulse width, d, for a given spacing reduces
  effective injection strength and results in lower jitter
  tracking bandwidth
                                                              40
 Phase Drifts with ILO-Based Clocking

                                       Data
Parallel                                                         Demuxed
Data In          8:4   4:1                                       Data Out


                                       PVT
                                    Phase Drift

                                                       ILRO
                             ILRO                     w/ Skew
                                     1/4 Rate         Tuning
                                     FWD Clk
           PLL
                                                     <±0.5UI
                                                  Deskew Range



• Voltage and temperature variations can cause the TX/RX
  ILOs’ free running frequency to change, and thus the
  phase relationship can drift with time
                                                                      41
 Low-Overhead CDR w/ILO-Based De-Skew


                                     Data
Parallel                                                   Demuxed
Data In          8:4   4:1                                 Data Out




                                                     CDR

                             ILRO
                                    1/4 Rate
                                    FWD Clk
           PLL




• Introducing a low-overhead CDR into a forwarded-clock
  system allows tracking of low-frequency phase drifts, while
  maintaining correlated jitter tracking
                                                                42
 Multi-Phase Errors at Low VDD

                                       Data
Parallel                                                Demuxed
Data In          8:4   4:1                              Data Out


                                    Quadrature
                                    Phase Error
                                                  CDR

                             ILRO
                                     1/4 Rate
                                     FWD Clk
           PLL




                                                             43
Edge-Rotating 5/4X Sub-Rate CDR
                                                                                • An additional periodically
                                                                                  rotating edge sampler
                                                                                  provides the 4-eye phase
                                                                                  information to CDR logic

                                                                                • Allows tracking of phase
                                                                                  drift and optimization of
                                                                                  each sampler timing
                                                                                  margin




 H. Li, S. Chen, L. Yang, R. Bai, W. Hu, F. Zhong, S. Palermo, and P. Chiang, “A 0.8V, 560fJ/bit,
 14Gb/s Injection-Locked Receiver with Input Duty-Cycle Distortion Tolerable Edge-Rotating 5/4X          44
 Sub-Rate CDR in 65nm CMOS,” VLSI Symp., June 2014.
14Gb/s GP 65nm CMOS Prototype
                                         Tracking Non-Uniform Eyes                       Correlated Jitter Tolerance
               1mm                                                                                    100
                                                                                                                                                                           14Gbps
                                                                                                                                                                           12Gbps

                                                                                                              10




                                                                                 Normalized SJ (UI)
                                                                                                                                                                  Equipment Limit
                   Clock
                   Buffer

        Shift
                   ILRO
                          Shift                                                                                            1
       Register   Phase Register
                  Rotator          1mm
       CDR        PI array &
       Logic      Quantizer                                                                            0.1
               CTLE


                                                                                               0.01
                                                                                                0.001                                 0.01      0.1         1      10       100   1000
                                                                                                                                                SJ Frequency (MHz)

                                                                               Uncorrelated Jitter Tolerance
                                                                                                                                10
                                                                                                                                                                       14Gbps w/ CDR
                                                                                                                                                                       14Gbps w/o CDR
                                                                                                                                                                       12Gbps w/ CDR
                                                                                                                                                                       12Gbps w/o CDR




                                                                                                      Jitter Amplitude (UIpp)
                                                                                                                                 1




                                                                                                                                0.1




                                                                                                                      0.01
                                                                                                                        0.001            0.01         0.1          1        10          100
                                                                                                                                                  Jitter Frequency (MHz)

 H. Li, S. Chen, L. Yang, R. Bai, W. Hu, F. Zhong, S. Palermo, and P. Chiang, “A 0.8V, 560fJ/bit,
 14Gb/s Injection-Locked Receiver with Input Duty-Cycle Distortion Tolerable Edge-Rotating 5/4X                                                                                               45
 Sub-Rate CDR in 65nm CMOS,” VLSI Symp., June 2014.
 Optimum Jitter Tracking for 200MHz jitter
• Limit the JTB by attenuating the clock jitter using amplitude response
  of low pass function with pole frequency = JTB
• 𝐽      𝐽 sin 2𝜋𝑓 𝑈𝐼 · 𝑛     2𝑚𝜋𝑓 𝑈𝐼
                                        Jitter Frequency = 200MHz
• 𝐽      𝐽 |     |


  In 10Gb/s system,
  UI = 100ps

Objective: Implement
optimal JTB that yields
minimum differential jitter

 Controllable JTB over
 70 - 800MHz is
 desired


                                                                           46
Understanding of Jitter Reduction using
Bandpass Filtering
• Time Domain Jittery Clock Expression:
                  𝑐 𝑡    𝐴𝑐𝑜𝑠 2𝜋𝑓 𝑡 𝛽𝑠𝑖𝑛2𝜋𝑓 𝑡
   𝛽:phase noise amplitude; 𝑓 : Jitter frequency

• Frequency Domain Jittery Clock Expression:
                 𝐴              𝛽𝐴
           𝐶 𝑓     𝛿 𝑓 𝑓           𝛿 𝑓 𝑓       𝛿 𝑓   𝑓
                 2               4

                                                         𝑓   𝑓   𝑓

                                                         𝑓   𝑓   𝑓




                                                                     47
Understanding of Jitter Reduction using
Bandpass Filtering
• The spectrum of received clock after filtering
          𝑆 𝑓       𝛿 𝑓    𝑓        𝛼 𝛿 𝑓   𝑓      𝛼 𝛿 𝑓   𝑓
    α , α and α are the gain of the bandpass function at f , f andf
•   Received clock expression in time domain:
                   𝑠 𝑡    𝐴 𝑐𝑜𝑠 2𝜋𝑓 𝑡 𝛽 𝑠𝑖𝑛2𝜋𝑓 𝑡

• Phase noise amplitude of the received clock
                                 𝛼    𝛼
                          𝛽               𝛽
                                   2𝛼

• For typical bandpass filtering, α    1and α      α    α . Thus, β
  β and the jitter of the transmitted clock is reduced by bandpass
  filtering


                                                                      48
Understanding of Jitter Reduction using
Bandpass Filtering
• Bandpass function is symmetrical and center at f , the transfer
  function can be expressed as a low-pass function with respect to the
  frequency offset from f ,
                                                𝐻 𝑗2𝜋𝑓
             𝐻 𝑗2𝜋 𝑓 𝑓       𝐻 𝑗2𝜋 𝑓 𝑓
                                                      𝑗𝑓
                                                 1
                                                      𝑓
   𝑓 :the offset frequency from 𝑓 ; BW :bandwidth of bandpass filter
                            𝑓    1/2 𝐵𝑊
• JTF of bandpass filtering:
               𝛽             𝐻 𝑗2𝜋 𝑓   𝑓    𝐻 𝑗2𝜋 𝑓      𝑓         1
 𝐽𝑇𝐹 𝑗2𝜋𝑓          𝑗2𝜋𝑓
               𝛽                       2𝐻 𝑗2𝜋𝑓                         𝑗𝑓
                                                               1
                                                                       𝑓




                                                                            49
                    Analysis of Bandpass Jitter Filtering Based on JIR
                    and JTF
                           -12
                        x 10      Jitter Impluse Reponse of Bandpass System                                                       Jitter Transfer of Bandpass System
                                                                                                                   0


                    8
                                                                                                                   -5




                                                                                    Jitter Amplification Factor
                    6
Normalized Jitter




                                                                                                                  -10

                    4


                                                                                                                  -15
                    2


                                                                                                                  -20
                    0



                    -2                                                                                            -25
                      15         20           25            30            35   40                                       0   0.5            1              1.5          2      2.5
                                              Clocking Cycle#                                                                                  Freq(Hz)                       9
                                                                                                                                                                           x 10




      • Transmitted jitter exhibits low-pass transfer
        characteristic through band-pass channel
      • Received high frequency uncorrelated jitter can be
        reduced by a bandpass filter
                                                                                                                                                                                    50
Optimum Jitter Tracking with Bandpass
Filtering
• Higher Q of bandpass filtering, smaller bandwidth, higher jitter
  filtering



                           1
         𝐽𝑇𝐹   𝑗2𝜋𝑓
                               𝑗𝑓
                       1
                               𝑓
           𝑓    1/2 𝐵𝑊




                                                                     51
Optimum Jitter Tracking with Bandpass
Filtering
• Apply JIR and JTF analysis to quantify the impact of Q on JTB of
  5GHz clock, UI = 100ps


                                                    Q tuning range over
                                                    3 -30 provides JTB
                                                    range over 97 – 790
                                                    MHz

                                                    To achieve JTB of
                                                    70MHz to optimize
                                                    jitter tracking with
                                                    10UI clock skew,
                                                    higher Q is required.




                                                                            52
Bandpass Filter for Forwarded-Clocks




                        [Hollis AICSP 2008]




                                              53
Bandpass Filter Jitter Filtering




• Bandpass filter is effective in filtering high-frequency jitter

• Low-maximum Q of the filter (Q=2.6) limits tuning to
  low-frequency jitter tracking bandwidths
   • Limited by the passive inductor Q

                                                                    54
Next Time
• Clock Distribution Techniques




                                  55
