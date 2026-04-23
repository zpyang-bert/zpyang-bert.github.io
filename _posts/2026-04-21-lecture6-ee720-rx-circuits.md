---
layout: post
title:      "lecture6 ee720 rx circuits"
date:       2026-04-21 09:48:22
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

    Lecture 6: RX Circuits




           Sam Palermo
   Analog & Mixed-Signal Center
       Texas A&M University
Announcements
• Lab 4 report and Prelab 5 due Mar 6
• Exam 1 Mar 7
  • Covers material through Lecture 6
  • Previous years’ exam 1s are posted on the
    website for reference


• Sampler and comparator papers are posted
  on the website


                                                2
Outline
• Receiver parameters
• T-coils at RX examples
• Analog front-end
• Clocked comparators
• Sensitivity & offset correction
• Demultiplexing
• PAM4 RX example
                                    3
High-Speed Electrical Link System




                                    4
Receiver Parameters
• RX sensitivity, offsets in voltage and time domain, and
  aperture time are important parameters
• Minimum eye width is determined by aperture time plus
  peak-to-peak timing jitter
• Minimum eye height is determined by sensitivity plus
  peak-to-peak voltage offset




                                        [Dally]

                                                            5
RX Block Diagram



• RX must sample the signal with high timing precision and resolve
  input data to logic levels with high sensitivity
• Input pre-amp can improve signal gain and improve input referred
  noise
   • Can also be used for equalization, offset correction, and fix sampler
     common-mode
   • Must provide gain at high-bandwidth corresponding to full data rate
• Comparator can be implemented with static amplifiers or clocked
  regenerative amplifiers
   • Clocked regenerative amplifiers are more power efficient for high gain
• Decoder used for advanced modulation (PAM4, Duo-binary)
                                                                              6
Outline
• Receiver parameters
• T-coils at RX examples
• Analog front-end
• Clocked comparators
• Sensitivity & offset correction
• Demultiplexing
• PAM4 RX example
                                    7
   56Gb/s PAM4 Input Network
[Pisati ISSCC 2019]




  • T-coil isolates ESD and input stage capacitance
  • Shunt peaking with termination network provides
    bandwidth extension
                                                      8
100Gb/s PAM4 Input Network




                                        [Loi ISSCC 2019]


• Bridged T-coil isolates ESD and provides further
  bandwidth extension
• Series peaking isolates input stage capacitance
                                                           9
Outline
• Receiver parameters
• T-coils at RX examples
• Analog front-end
• Clocked comparators
• Sensitivity & offset correction
• Demultiplexing
• PAM4 RX example
                                    10
   Analog Front-End (AFE)
[Pisati ISSCC 2019]




  • AFE provides equalization (CTLE) and gain stages
    (VGA) to optimize the signal for symbol detection
    (mixed-signal RX) or quantization (ADC-based RX)
  • Shrinking supply voltages make it difficult to
    efficiently achieve gain
                                                        11
RX Static Differential Amplifiers
• Differential input amplifiers often
  used as input stage in high
  performance serial links
   • Rejects common-mode noise
   • Sets input common-mode for
     preceding comparator

• Input stage type (n or p) often       Av  g m1 RL ro1   g m1 RL
  set by termination scheme

• High gain-bandwidth product
  necessary to amplify full data
  rate signal

• Offset correction and
  equalization can be merged into
  the input amplifier                                      g m1             g
                                        Av                                 m1
                                               g m 3  g o 3  g o 4  g o1 g m 3
                                                                                    12
Low-Voltage Gm-TIA Amplification




                                                [Pisati ISSCC 2019]


• Two-stage topology consisting of an input transconductance
  (Gm) stage followed by an output transimpedance (TIA)
  stage allows for low-voltage operation
• Both NMOS and PMOS transconductance can be utilized
• TIA stage allows for improved gain with better linearity, as
  mostly signal current passes through RF                      13
eSilicon 56Gb/s PAM4 CTLE Gm-Stage
• Input AC-coupling for optimal         [Pisati ISSCC 2019]

  common-mode to utilize both
  NMOS and PMOS Gm
• RC degeneration at main input
  transistors’ sources provides
  high-frequency peaking
• Additional tunable bias resistor at
  the NMOS input provides an
  additional zero for low-frequency
  channel compensation
• Gain control achieved through
  bias programmability

                                                          14
eSilicon 56Gb/s PAM4 CTLE TIA-Stage
                                 [Pisati ISSCC 2019]
• Inverter-based gain stage
  with feedback resistor
• Supply noise rejection
  achieved with a replica-bias
  regulated power supply
• As mostly signal current
  flows through RF, good
  linearity is achieved with
  high signal swing


                                                   15
Inverter-Based Design                        [Zheng CICC 2018]




• Inverter-based design allows for both NMOS and PMOS
  transconductance
• Cells can also be used as resistive and active-inductor loads
                                                              16
56Gb/s Inverter-Based CTLE
Replica Bias Loop                              [Zheng CICC 2018]




• Replica-biasing with ring oscillator-based process monitor
                                                               17
Outline
• Receiver parameters
• T-coils at RX examples
• Analog front-end
• Clocked comparators
• Sensitivity & offset correction
• Demultiplexing
• PAM4 RX example
                                    18
RX Clocked Comparators
• Also called regenerative amplifier, sense-amplifier,
  flip-flop, latch
• Samples the continuous input at clock edges and
  resolves the differential to a binary 0 or 1




                                              [J. Kim]

                                                         19
Important Comparator Characteristics

• Offset and hysteresis
• Sampling aperture, timing resolution,
  uncertainty window
• Regeneration gain, voltage sensitivity,
  metastability
• Random decision errors, input-referred
  noise


                                            20
Dynamic Comparator Circuits




    [J. Kim]                                                    [Toifl]
        Strong-Arm Latch                            CML Latch
• To form a flip-flop
   • After strong-arm latch, cascade an R-S latch
   • After CML latch, cascade another CML latch
• Strong-Arm flip-flop has the advantage of no static power
  dissipation and full CMOS output levels
                                                                          21
StrongARM Latch Operation
[J. Kim TCAS1 2009]




                            t=t0 t1   t2

[J. Kim]


• 4 operating phases: reset, sampling,
  regeneration, and decision

                                           22
StrongARM Latch Operation – Sampling Phase
[J. Kim TCAS1 2009]
• Sampling phase starts when
  clk goes high, t0, and ends
  when PMOS transistors turn
  on, t1
• M1 pair discharges X/X’
• M2 pair discharges out+/-

  vout s                    g m1 g m 2
            
  vin s                       g m 2 Cout  C x  
                          
                sCout C x  s                       
                                      Cout C x       
              g m1 g m 2    1
             2          
             s Cout C x s 2 s1 s 2
  where  s1  C x g m1 ,  s 2  Cout g m 2

                                                          23
StrongARM Latch Operation – Regeneration
[J. Kim TCAS1 2009]
• Regeneration phase starts
  when PMOS transistors
  turn on, t1, until decision
  time, t2
• Assume M1 is in linear
  region and circuit no longer
  sensitive to vin
• Cross-coupled inverters
  amplify signals via positive-
  feedback:
                      t t 
           GR  exp 2 1 
                       R 
        R  Cout / g m 2,r  g m 3,r 
                                           24
StrongARM Latch Operation – Diff. Output
[J. Kim TCAS1 2009]




                                           25
Conventional RS Latch
• RS latch holds output                        [Nickolic]
  data during latch pre-
  charge phase

                        Vcm+V
                           -V                         Vcm+V
                                                          -V

                                 1                 1   0
• Conventional RS latch
  rising output transitions          1 0   0   1
  first, followed by falling
  transition
                                                            26
Optimized RS Latch                               [Nikolic JSSC 2000]


• Optimizing RS latch for symmetric
  pull-up and pull-down paths
  allows for considerable speed-up
                                    Vcm+V
                                       -V                        Vcm+V
                                                                     -V
• During evaluation, large driver
  transistors are activated to
  change output data and the                 1                1   0
  keeper path is disabled

• During pre-charge, large driver
  transistors are tri-stated and      1 0                         0    1
  small keeper cross-coupled
  inverter activated to hold data

   Evaluation Mode (Clock High) Driver Branches
               Hold/Precharge Mode (Clock Low) Keeper Branches
                                                                       27
Delay Improvement w/ Optimized RS Latch


                                                  [Nikolic JSSC 2000]




• Strong-Arm flip-flop delay improves by close to a factor of two

• Has better delay performance than other advanced flip-flop topologies


                                                                          28
 Sampler Analysis
• Sampler analysis provides insight into comparator operation
[Johansson JSSC 1998]


                              h 



          
vsample   vin  h d
          
• Switch can be modeled as a device which determines a
  weighted average over time of the input signal
• The weighting function is called the sampling function
                                                           29
 Sampling Function Properties
• Sampling function should (ideally) integrate to 1
                          

                           h d  1
                          

• Ideal sampling function is a delta function
     • Sampled value is only a function of exact sampling time

                                          
                               vsample   vin  h d
ideal h    t                       




                                                             30
Sampling Function Example
• Practical sampling function will weight the input
  signal near the nominal sampling time




                                       
                             vsample   vin  h d
                                       




          Practical h 
                                                           31
Sampler Frequency Response
• Fourier transform of the sampling function yields the
  sampler frequency response
• Sampler bandwidth is a function of sample clock
  transition time
             h                  F .T .h  




                                                     32
Sampler Aperture Time
• Aperture time is defined as the width of the SF
  peak were a certain percentage (80%) of the
  sensitivity is confined
                                  h 

     w80  t90  t10
           t10

    0.1   h d
           

           t90

    0.9   h d
           



                                                    33
Clocked Comparator LTV Model




                                           [J. Kim]

• Comparator can be viewed as a noisy nonlinear filter
  followed by an ideal sampler and slicer (comparator)
• Small-signal comparator response can be modeled with
  an ISF    ht , 
                                                         34
Clocked Comparator ISF
• Comparator ISF is a subset of a time-varying impulse
  response h(t,) for LTV systems:
                                  
                         y t    ht ,   x d
                                  

   • h(t,): system response at t to a unit impulse arriving at 


• ISF ()=h(tobs,)
   • For comparators, tobs is before decision is made
   • Output voltage of comparator
                                       
                        vo tobs    vi     d
                                       
   • Comparator decision
                                                  
      Dk  sgn vk   sgn vo tobs  kT   sgn  vi     d 
                                                     

                                                                         35
Clocked Comparator ISF
                 • ISF is defined with
                   respect to tobs, or
                   the decision time

                 • The comparator
                   provides the most
                   gain during the
                   sampling phase


                 [J. Kim]

                                         36
Clocked Comparator ISF
• ISF shows sampling aperture or timing resolution
• In frequency domain, it shows sampling gain and
  bandwidth

                                             [J. Kim]




                                                     37
  Characterizing Comparator ISF
[Jeeradit VLSI 2008]
                                                         Strong-Arm Latch




                                                                      [J. Kim]
                                                             CML Latch




                                                                      [Toifl]
  • For more details, see
    http://www.ece.tamu.edu/~spalermo/ecen689/ECEN720_lab4_2017.pdf
                                                                         38
Comparison of SA & CML Comparator (1)
               [Jeeradit VLSI 2008]




• Sampling time of SA latch varies with VDD,
  while CML isn’t affected much


                                               39
Comparison of SA & CML Comparator (2)
                         [Jeeradit VLSI 2008]




• CML latch has higher sampling gain with small input pair
• StrongARM latch has higher sampling bandwidth
   • For CML latch increasing input pair also directly increases output
     capacitance
   • For SA latch increasing input pair results in transconductance
     increasing faster than capacitance
                                                                          40
Low-Voltage SA – Schinkel ISSCC 2007




• Does require clk & clk_b
   • How sensitive is it to skew?
                                       41
Low-Voltage SA – Schinkel ISSCC 2007




                                       42
Low-Voltage SA – Schinkel ISSCC 2007




                                       43
Low-Voltage SA – Goll TCAS2 2009




• Similar stacking to conventional SA latch
• However, now P0 and P1 are initially on during evaluation
  which speeds up operation at lower voltages
• Does require clk & clk_b
   • How sensitive is it to skew?                             44
Low-Voltage SA – Goll TCAS2 2009




                                   45
Charge-Steering Latch
  First Stage (faster)   Second Stage (fast)




     [Chiang 2013 VLSI, Bai 2014 ISSCC]

 First stage has small aperture time, but both outputs discharge to GND
 Second stage has small delay, provides gain, and latches the
  differential output
 Only requires one clock phase
 Gain is limited
                                                                       46
Charge-Steering Latch Headroom at Low-VDD
         Reset Phase         Active Phase
                                            [Bai 2014 ISSCC]




• Only one effective transistor stack
  • Maximizes gm of active transistors
  • Allows for low-voltage operation
                                                               47
 Charge-Steering Latch
 w/ Common-Mode Restore
[Bai 2014 ISSCC]




 • Differential output swing is proportional to output voltage
   common-mode (VCM) drop
 • However, excessive VCM drop can limit subsequent
   stages’ speed
 • Addition of PMOS capacitors allows for larger overall gain
                                                                 48
  65nm Charge-Steering Latch Performance
                   • Sampling aperture is ~17ps
                     (post-layout)




[Bai 2014 ISSCC]
                   • Latch has a gain >2

                   • Also possible to configure the
                     structure as a fast sample-and-
                     hold (S/H)

                                                       49
      Charge-Steering Latch w/ Regeneration
                      Mp1
                                           Mp2             Mp3
                                                                            clk
                 VX                                                          VDD
                                                             Vo


       VIN
                Mn1                  Mn2                   Mn3              Vx
                                                                              0
                                                                             VDD
clk
                                                                            Vo
                                                                             0



       Addition of small Mp3/Mn3 regeneration stage in parallel with
        second stage output provides a full-swing output
       Regeneration current set with an NMOS transistor
       Only requires one clock phase
       Overall, smaller delay relative to other low-voltage regenerative
        comparators (Schinkel latch)
      • Utilized in a 32Gb/s PAM4 DFE receiver [Elhadidy 2015 VLSI]
                                                                            50
Outline
• Receiver parameters
• T-coils at RX examples
• Analog front-end
• Clocked comparators
• Sensitivity & offset correction
• Demultiplexing
• PAM4 RX example
                                    51
RX Sensitivity
• RX sensitivity is a function of the input referred noise,
  offset, and minimum latch resolution voltage
                      v Spp  2v nrms SNR  vmin  v offset*

• Gaussian (unbounded) input referred noise comes from
  input amplifiers, comparators, and termination
   • A minimum signal-to-noise ratio (SNR) is required for a given bit-
     error-rate (BER)
                        For BER  10-12 ( SNR  7)

• Minimum latch resolution voltage comes from hysteresis,
  finite regeneration gain, and bounded noise sources
                              Typical vmin  5mV

• Input offset is due to circuit mismatch (primarily Vth
  mismatch) & is most significant component if uncorrected
                                                                          52
Front-End Noise
                                        Front-End                  Decision
                                                                    Circuit
                                                            Vo
                       RXIN
                                        CTLE/                                      Vout
                                         VGA
                       vn,in

                                 VCM                                   Φlatch
              Vn,in2             |H|2           Vn,FE2

                 
                                 f               f                      f
                                                           BWD
              Output Noise Power Spectrum: 𝑉 ,                   𝐻 𝑓        ·𝑉 ,   𝑓
          Integrating this noise spectrum over the decision circuit bandwidth
          BWD gives the total noise power experienced by the decision circuit

                               𝑣 ,           𝐻 𝑓         ·𝑉 ,    𝑓 𝑑𝑓

• Note that since H(f) generally rolls-off quickly, the exact upper bound is
  not too critical and could be set to a very high value (infinity)       53
56Gb/s Front-End Output Noise Example
                                      TX=3-tap, RX=14-tap FFE & 1-tap DFE




                                 𝑛𝑉
                         𝜂   8.2
                                 𝐻𝑧




• Iterating front-end configuration (DC gain, peaking,
  bandwidth) to compensate for a 37dB channel
• While front-end ISI is reduced with higher bandwidth
  and peaking, the rms noise also grows
• The optimum bandwidth is generally near or slightly
  higher than the Nyquist frequency
                                                                     54
Comparator Noise
                                                     • Device noise causes random
VOS   V2n,in                                           decisions even with zero input
                                   Voutp
                                           Count
                                                       signal
                                             1
                                   Voutn             • Noise variance can be found by
                                                       fitting output to a Gaussian
                         CLK
VOS1 VTH                                               CDF as the input is swept and
               Pr(1)=0     Input referred Gaussian
                                                       transient noise is enabled
 VOSm
                                  noise CDF
                               Prob                  • Noise can also be simulated
               Pr(1)=0.5
        VOSn                                           with PSS+PAC+PNOISE, but
               Pr(1)=1
                               VOS1 VOSm VOSn VOS
                                                       requires post processing to find
                                                       ISF from sideband transfer
                                                       function [Kim TCAS-I 2009]

                                                                                          55
Comparator Metastability


                               𝐶    𝑉
                      𝑡   ~
                                   𝐼

                               +
                                        𝑉
                      𝑡   ~𝜏       ln
                                        𝑉




• Comparator evaluation time grows proportional to ln(Vin-1)
• Metastability occurs when the input is too small and the
  comparator doesn’t have sufficient time to fully evaluate
• This metastability window is a major component of the
  comparator Vmin                                            56
RX Sensitivity & Offset Correction
• RX sensitivity is a function of the input referred noise,
  offset, and min latch resolution voltage
  v Spp  2v nrms SNR  vmin  v offset*                Typical Values : vnrms  1mVrms , vmin  voffset*  6mV

  For BER  10-12 ( SNR  7)  vSpp  20mV pp

• Circuitry is required to reduce input offset from a
  potentially large uncorrected value (>50mV) to near 1mV
                                              D[0]

                                       Clk0


                                              D[1]
                                                                             clk
                                                       clk         -                           clk
                                                                                   Out+
                                       Clk180
                                                                 Out


                                                 x16 x8 x4 x2                             x2 x4 x8 x16
                                                COffset[4:0]                                 COffset[5:9]
              Din+              Din-

                                                       IOffset         clk

                                                                                                              57
Comparator Offset
                                               • The input referred offset is primarily a
                                                 function of Vth mismatch and a weaker
                                                 function of  (mobility) mismatch
                                                                  AVt                    A
                                                           V          ,     /  
                                                            t
                                                                  WL                     WL


        60
                                               • To reduce input offset 2x, we need to
        50                                       increase area 4x
        40

                                               • Not practical due to excessive area and
Count




        30

        20

        10
                                                 power consumption
         0
        -30    -20   -10   0   10   20
              Comparator Threshold (mV)
                                          30
                                               • Offset correction necessary to
                                                 efficiently achieve good sensitivity


                                                                                              58
Offset Correction Range & Resolution
• Generally circuits are designed to handle a minimum
  variation range of 3 for 99.7% yield
• Example: Input differential transistors W=4m, L=150nm

          AVt       2.8mVm                              A          2% m
   V                          3.6mV ,     /                          2.6%
      t
          WL        4 m 150nm                          WL       4 m 150nm

• If we assume (optimistically) that the input offset is only dominated
  by the input pair Vt mismatch, we would need to design offset
  correction circuitry with a range of about 11mV
• If we want to cancel within 1mV, we would need an offset
  cancellation resolution of 5bits, resulting in a worst-case offset of
                         Offset Correction Range 22mV
                1LSB                            5    0.65mV
                                2 Resolution
                                             1  2 1


                                                                                       59
Current-Mode Offset Correction Example
                                        [Balamurugan JSSC 2008]
• Differential current injected into
  input amplifier load to induce an
  input-referred offset that can
  cancel the inherent amplifier
  offset
   • Can be made with extended
     range to perform link margining

• Passing a constant amount of
  total offset current for all the
  offset settings allows for constant
  output common-mode level

• Offset correction performed both
  at input amplifier and in
  individual receiver segments of
  the 2-way interleaved
  architecture
                                                                  60
Capacitive Offset Correction Example
• A capacitive imbalance in the
  sense-amplifier internal nodes
  induces an input-referred offset
• Pre-charges internal nodes to allow
  more integration time for more
  increased offset range
• Additional capacitance does
  increase sense-amp aperture time       90nm CMOS, Input W/L=4u/0.15u
• Offset is trimmed by shorting
  inputs to a common-mode voltage
  and adjusting settings until an even
  distribution of “1”s and “0”s are
  observed
• Offset correction settings can be
  sensitive to input common-mode

                                                                         61
Outline
• Receiver parameters
• T-coils at RX examples
• Analog front-end
• Clocked comparators
• Sensitivity & offset correction
• Demultiplexing
• PAM4 RX example
                                    62
Demultiplexing RX
• Demultiplexing allows for
  lower clock frequency
  relative to data rate
• Gives extra regeneration
  and pre-charge time in
  comparators
• Need precise phase
  spacing, but not as
  sensitive to duty-cycle as
  TX multiplexing

                               63
1:4 Demultiplexing RX Example




• Increased demultiplexing allows for higher data rate at
  the cost of increased input or pre-amp load capacitance
• Higher multiplexing factor more sensitive to phase offsets
  in degrees

                                                               64
Low-Voltage Serial I/O Transceiver




• Utilizes a high TX output multiplexing (4:1)
  and RX input multiplexing (1:8) factor for
  low-voltage operation
  Y.-H. Song, R. Bai, P. Chiang, and S. Palermo, “A 0.47-0.66pJ/bit, 4.8-8Gb/s I/O Transceiver in
  65nm-CMOS,” IEEE JSSC, vol. 48, no. 5, pp. 1276-1289, May 2013.                                   65
1:8 Input De-Multiplexing RX




• 1:8 input de-multiplexing allows input comparators
  to operate at low voltages
• Injection-locked-oscillator is used for efficient
  multi-phase clock generation and de-skew
  Y.-H. Song, R. Bai, P. Chiang, and S. Palermo, “A 0.47-0.66pJ/bit, 4.8-8Gb/s I/O Transceiver in
  65nm-CMOS,” IEEE JSSC, vol. 48, no. 5, pp. 1276-1289, May 2013.                                   66
0.47-0.66pJ/bit, 4.8-8Gb/s
GP 65nm CMOS Prototype
                                                                           Testing with 20cm FR-4 Channel
                                                                                                                                    0.8
                                                                                                                                             TX+RX                   TX (VDD=0.8V)
                                                                                                                                                                     RX (VDD=0.75V)
                                                                                                                                    0.7      TX




                                                                                                         Energy Efficiency [pJ/b]
                                                                                                                                             RX
                                                                                                                                    0.6    TX and RX    TX and RX
                                                                                                                                          (VDD=0.6V)   (VDD=0.65V)
                                                                                                                                    0.5

                                                                                                                                    0.4

                                                                                                                                    0.3

                                                                                                                                    0.2

                                                                                                                                    0.1
                                                                                                                                       4.8                6.4                         8
                                                                                                                                                   Data Rate [Gb/s]




• Optimal 0.47pJ/b energy efficiency achieved at 6.4Gb/s
   ̶      At low data rates, less amortization of static current
   ̶      At high data rates, higher voltage required for serialization timing
       Y.-H. Song, R. Bai, P. Chiang, and S. Palermo, “A 0.47-0.66pJ/bit, 4.8-8Gb/s I/O Transceiver in
       65nm-CMOS,” IEEE JSSC, vol. 48, no. 5, pp. 1276-1289, May 2013.                                                                                                        67
Outline
• Receiver parameters
• T-coils at RX examples
• Analog front-end
• Clocked comparators
• Sensitivity & offset correction
• Demultiplexing
• PAM4 RX example
                                    68
PAM4 RX Example                                                                                  [Roshan Zamir JSSC 2019]

                                                                           Output
                                              1-tap FIR, 1-tap
                  PAM4 Equalizer                  IIR DFE
                                          +             Z-1
                                                                                    MUX
                                                                                                               DFE
                                                                                                   DFE DFE
                                                                                                                IIR Slicer
                                                                                                   FIR    IIR
                                                                                                               Time Thre.
                                                                                                  Weight Amp.
                                                                                                              Const.
          Input                   2-bit Flash ADC
                  CTLE                              3            12
                                                                      D
                              +

                                          Error Sampler                                                  Adaptation
                                                                 4    ER
                                                                           4:8            8:32
                                                                                                           Logic
                                           Edge Sampler
                                                                 4    ED




                            Divider                  14 GHz
                             and                     LC-VCO
                            Buffers
                                                                                 BBPD




• 2b flash ADC (3 comparators) for PAM4 symbol decisions
• Swept error sampler for PAM4 threshold adaptation
• Edge samplers provide information for CDR & equalization adapt
• CTLE & DFE cancel ISI
                                                                                                                             69
PAM4 Slicer Threshold Adaptation
                     Ideal Thresholds                   Initial         Data Samplers
Ideal Error Offset                                    Calibration            TH3
                                        Ideal TH3                       
Ideal Error Offset
                                                        State 1:
                                                                             TH2
                                        Ideal TH2    Top sampler        
                                                       threshold
                                                    (Fair statistics)
                                        Ideal TH1                       
                                                                             TH1


                                                        State 2:            THER
                                                    Bottom sampler      
                                                       threshold                     Error


• Fully adaptive background
                                                                                    Sampler
                                                    (Fair statistics)


  calibration to positon slicers in                     State 3:
                                                    Bottom sampler
                                                                          State 6:
                                                                         Bottom eye

  the middle of the PAM4 eyes                          threshold
                                                    (Random mode)
                                                                           height
                                                                         estimation


                                                        State 4:             State 5:
                                                      Top sampler            Top eye

• Error sampler tracks eyes edges                      threshold
                                                    (Random mode)
                                                                              height
                                                                            estimation

  and finds heights
                                                     [Roshan Zamir JSSC 2019]

                                                                                              70
  PAM4 Slicer Threshold Adaptation
                                                                         State1 (Statistical)
                        Initial Condition                          Bottom of the Top Eye Detected
   Ideal Error Offset
                                            Ideal TH3
                                                         Error Offset 1
                                                                                                                        Data Samplers
   Ideal Error Offset                                                                        THER,1
   Error Offset 1                            THER,0                                         %25  1
                                             %50  1                                        %75  0                      
       Ideal TH1                                                                             Follows TH3
                                             %50  0
                                                                                            Symmetrically                        TH3
                    State2 (Statistical)                               State3 (Random Data)
            Top of the Bottom Eye Detected                          Monitor Top of the Bottom Eye
                                                                                                                         
                                             Fixed                                           Fixed
                                                                                                                                 TH2
                                            THER,2       Error Offset 1                      THER,3
   Error Offset 1
                                            %75  1                                          Dn[1]=ERn                   
                                            %25  0
                  State4 (Random Data)                                  State5 (Random Data)
                                                                                                                                  TH1
             Monitor Bottom of the Top Eye                           Top of the Top Eye Detected                                  Error Sampler
                                                         Error Offset 2                     THER,5
                                                                                            Dn[3]≠ ERn                   
   Error Offset 1                            THER,4           Top
                                                                                             Fixed
                                            Dn[3]=ERn                                                                            THER
                                             Fixed                                           Fixed


                 State6 (Random Data)                                  State3 (Random Data)                   State4 (Random Data)
           Bottom of the Bottom Eye Detected                        Monitor Top of the Bottom eye        Monitor Bottom of the Top eye
                                                                                               Error Offset 3
                                             Fixed                                          Fixed Top                               THER,4
                                                                                                                                              State5
                                             Fixed     Error Offset 3                       THER,3
  Error Offset 2                            Dn[1]≠ ERn                                                                              Fixed
                                                          Bottom                            Dn[1]=ERn
     Bottom
                                            THER,6

                                     𝑇𝐻        ,         𝑇𝐻          ,                               𝑇𝐻         ,       𝑇𝐻   ,
                         𝑇𝐻                                                           𝑇𝐻
                                                     2                                                              2

[Roshan Zamir JSSC 2019]                                                                                                                               71
 56Gb/s PAM4 RX Test Setup

Channel w/
 20.8dB of
  loss @
  14GHz




                 GP 65nm
                 Prototype




                             72
  56Gb/s PAM4 RX Measured Results
GP 65nm Prototype   Equalization Adaptation   Threshold Adaptation




• 20.8dB channel
• 4.6pJ/b
    Timing Margin          Voltage Margin         Jitter Tolerance




[Roshan Zamir JSSC 2019]                                             73
RX Take-Away Points
• AFE provides equalization and gain stages to optimize
  the signal for symbol detection (mixed-signal RX) or
  quantization (ADC-based RX)
• Gm-TIA and inverter-based front-ends allow for higher
  gain with shrinking supply voltages
• Achieving good RX sensitivity requires careful front-end
  noise analysis and sampler offset correction
• Higher input stage demultiplexing relaxes clock
  frequencies at the cost of front-end loading and clock
  phase generation
• PAM4 receivers require extra threshold adaptation
                                                             74
Next Time
• Equalization theory and circuits
  • Equalization overview
  • Equalization implementations
    • TX FIR
    • RX FIR
    • RX CTLE
    • RX DFE
  • Setting coefficients
  • Equalization effectiveness
  • Alternate/future approaches
                                     75
