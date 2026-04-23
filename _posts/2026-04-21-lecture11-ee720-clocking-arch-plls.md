---
layout: post
title:      "lecture11 ee720 clocking arch plls"
date:       2026-04-21 10:13:12
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
Announcements
• Project Preliminary Report due Apr 18
• Project Final Report due May 2




                                          2
Agenda
• Clocking Architectures

• PLLs
  • Modeling
  • Noise transfer functions




                               3
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
High-Speed Electrical Link System




                                    5
Clocking Terminology
              Synchronous
              • Every chip gets same frequency AND phase
              • Used in low-speed busses
              Mesochronous
              • Same frequency, but unknown phase
              • Requires phase recovery circuitry
                  • Can do with or without full CDR
              • Used in fast memories, internal system interfaces,
                MAC/Packet interfaces
              Plesiochronous
              • Almost the same frequency, resulting in slowly
                drifting phase
              • Requires CDR
              • Widely used in high-speed links
              Asynchronous
              • No clocks at all
              • Request/acknowledge handshake procedure
              • Used in embeddded systems, Unix, Linux
  [Poulton]                                                          6
I/O Clocking Architectures
• Three basic I/O architectures
   • Common Clock (Synchronous)
   • Forward Clock (Source Synchronous)
   • Embedded Clock (Clock Recovery)


• These I/O architectures are used for varying applications
  that require different levels of I/O bandwidth

• A processor may have one or all of these I/O types

• Often the same circuitry can be used to emulate different
  I/O schemes for design reuse

                                                              7
Common Clock I/O Architecture




   [Krauter]


• Common in original computer systems
• Synchronous system by design (no active deskew)
• Common bus clock controls chip-to-chip transfers
• Requires equal length routes to chips to minimize clock skew
• Data rates typically limited to ~100Mb/s                   8
Common Clock I/O Cycle Time




  [Krauter]

                              9
Common Clock I/O Limitations
• Difficult to control clock skew and propagation delay
• Need to have tight control of absolute delay to meet a given
  cycle time
• Sensitive to delay variations in on-chip circuits and board
  routes
• Hard to compensate for delay variations due to low
  correlation between on-chip and off-chip delays
• While commonly used in on-chip communication, offers
  limited speed in I/O applications



                                                                10
Forward Clock I/O Architecture
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
                                                     11
Forward Clock I/O Limitations
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




                                                     12
Forward Clock I/O De-Skew
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
                                                    13
Forward Clock I/O Circuits
                  • TX PLL
                  • TX Clock Distribution
                  • Replica TX Clock Driver
                  • Channel
                  • Forward Clock Amplifier
                  • RX Clock Distribution
                  • De-Skew Circuit
                     • DLL/PI
                     • Injection-Locked Oscillator


                                                     14
Embedded Clock I/O Architecture
                 • Can be used in mesochronous
                   or plesiochronous systems

                 • Clock frequency and optimum
                   phase position are extracted
                   from incoming data stream

                 • Phase detection continuously
                   running

                 • CDR Implementations
                    • Per-channel PLL-based
                    • Dual-loop w/ Global PLL &
                       • Local DLL/PI
                       • Local Phase-Rotator PLLs
                                                    15
Embedded Clock I/O Limitations
                 • Jitter tracking limited by
                   CDR bandwidth
                    • Technology scaling allows
                      CDRs with higher
                      bandwidths which can
                      achieve higher frequency
                      jitter tracking


                 • Generally more hardware
                   than forward clock
                   implementations
                    • Extra input phase samplers



                                                  16
Embedded Clock I/O Circuits
                 • TX PLL

                 • TX Clock Distribution

                 • CDR
                    • Per-channel PLL-based
                    • Dual-loop w/ Global PLL &
                       • Local DLL/PI
                       • Local Phase-Rotator PLLs
                       • Global PLL requires RX
                          clock distribution to
                          individual channels



                                                    17
Xilinx 0.5-32Gb/s Transceiver Clocking
                          Channels 1-4
 Frac-N LC PLL1, 2                                      Technology                CMOS 16nm FinFET
                                              Power Supply (Vavcc, Vavtt, Vaux)     0.9 V, 1. 2V, 1.8 V
      ∑                      Transmitter              Frequency range             500 Mb/s – 32.75 Gb/s
                                DCC                Transceiver Quad area          2.625 mm × 2.218 mm
    VCOLB                                              LC PLL range                   8-16.375 GHz
                              Receiver                Ring PLL range                    2-6.25 GHz
    VCOHB
                                               TX PRBS7 jitter at 32.75Gb/s       TJ: 5.39 ps, RJ: 190 fs
                             PI (D,X,S)       32.75Gb/s RX JTOL @ 30MHz                   0.45 UI
  PPF     2                    IQ CAL                               @ 100MHz              0.6 UI
                                                 Channel loss at 32.75Gb/s                 30 dB
                                DCC
                                                Measured BER at 32.75Gb/s                 < 10-15
                              Ring PLL         Power at 32.75Gb/s with DFE        577mW/ch (17.6pJ/b)

          I/Q1, I/Q2
   Active Inductor based Clock Distribution
                                                               [Upadhyaya VLSI 2016]

• LC-PLL with 2 LC-VCOs used to cover high data rates
  (8-32Gb/s)
• Ring-PLL used for lower data rates
• CML clock distribution with active inductive loads used
  for low jitter
                                                                                                       18
PLLs
• PLL modeling

• PLL noise transfer functions




                                 19
PLL Block Diagram




                                                    [Perrott]




• A phase-locked loop (PLL) is a negative feedback system
  where an oscillator-generated signal is phase AND
  frequency locked to a reference signal

                                                            20
PLL Applications
• PLLs applications
  • Frequency synthesis
    • Multiplying a 100MHz reference clock to 10GHz
  • Skew cancellation
    • Phase aligning an internal clock to an I/O clock
  • Clock recovery
    • Extract from incoming data stream the clock frequency and
      optimum phase of high-speed sampling clocks
  • Modulation/De-modulation
    • Wireless systems
    • Spread-spectrum clocking

                                                                  21
Forward Clock I/O Circuits
                  • TX PLL
                  • TX Clock Distribution
                  • Replica TX Clock Driver
                  • Channel
                  • Forward Clock Amplifier
                  • RX Clock Distribution
                  • De-Skew Circuit
                     • DLL/PI
                     • Injection-Locked Oscillator


                                                     22
Embedded Clock I/O Circuits
                 • TX PLL

                 • TX Clock Distribution

                 • CDR
                    • Per-channel PLL-based
                    • Dual-loop w/ Global PLL &
                       • Local DLL/PI
                       • Local Phase-Rotator PLLs
                       • Global PLL requires RX
                          clock distribution to
                          individual channels



                                                    23
 PLL Design Challenges
 • Board-level reference clock frequencies don’t scale often
    • 156MHz is a common frequency
 • RX CDR bandwidth is hard to scale with PAM4 signaling and
   ADC-based front-ends
    • Typically 2-4MHz
 • PLL bandwidth must be kept less than 10MHz for stability
   and to filter reference jitter
 • VCO phase noise at low-frequency offsets due to flicker
   noise must be suppressed
                     32.75Gbps Transceiver PLL Simulated Jitter Numbers
    Receiver Type         PLL PN @1MHz      CDR BW           RJ           RJ in UI
   Analog based RX          -92.4dBc/Hz     12.7MHz        160.7fs        5.26mUI
    ADC based RX            -92.4dBc/Hz      2MHz           407fs         13.3mUI


[Turker ISSCC 2019]                                                                  24
Charge Pump PLL
                           PFD
         Fin           D           UP        ICP                       Fout = N*Fin
                               Q
               in(t)       R
                                                    Vctrl
                                                                 VCO       out(t)
               fb(t)       R       DN
                               Q                   R        C2
                       D
                                             ICP
                                                   C1

                                        Divider

                                         1/N



• Charge pump PLL is a common implementation
• Type-2 (2 integrators) allows for ideally zero phase error between
  the input and feedback phase
• Requires a stabilizing zero that is realized with the filter resistor
• A secondary capacitor C2 is often added for additional filtering to
  reduce reference spurs
• Modeled as a third-order system
                                                                                      25
Linear PLL Model
           Phase Detector      Loop Filter            VCO

                    e                       Vctrl    KVCO
    in                 KPD       F(s)                                out
                                                       s

          fb
                                    1
                                    N
                                 Divider

• Phase is the key variable of interest
   • Output phase response to a stimulus injected at a given point in the loop
   • Phase error response is also informative
• Linear “small-signal” analysis is useful for understand PLL dynamics if
   • PLL is locked (or near lock)
   • Input phase deviation amplitude is small enough to maintain operation in
     lock range
                                                                                 26
Understanding PLL Frequency Response
       Input phase response         VCO output phase response
out                              out
in                               vco


                              f                                 f
• Frequency domain analysis can tell us how well the PLL
  tracks the input phase as it changes at a certain frequency

• PLL transfer function is different depending on which point
  in the loop the output is responding to
                                                                27
Linear PLL Model
             Phase Detector                    Loop Filter                  VCO

                      e                                      Vctrl         KVCO
      in                     KPD                F(s)                                     out
                                                                             s

            fb
                                                     1
                                                     N
                                                Divider

                                                         𝐼
For Charge Pump PLL:                             𝐾
                                                         2𝜋
                                                     1       1
                                                          𝑠
                                                     𝐶      𝑅𝐶
                                         𝐹 𝑠
                                                          𝐶  𝐶
                                                  𝑠 𝑠
                                                          𝑅𝐶 𝐶
                                                    𝐾 𝐾                    1
                           𝜙    𝑠                                      𝑠
                                                      𝐶                   𝑅𝐶
            𝐻 𝑠
                           𝜙   𝑠               𝐶  𝐶                   𝐾 𝐾          𝐾 𝐾
                                     𝑠               𝑠                       𝑠
                                               𝑅𝐶 𝐶                    𝑁𝐶          𝑁𝑅𝐶 𝐶
                                                                                                  28
14GHz PLL Closed-Loop Transfer Function
  Parameter
    Fref            156.25MHz
      N                90
    Fvco             14GHz
      fu              2MHz
     m                60°
     f3dB            3.1MHz
    Kvco            2π*1GHz/V
      R               4k
     C1               74pF
     C2               5.8pF
     Icp             310uA




                                            𝐾 𝐾        1
                      𝜙        𝑠                   𝑠
                                              𝐶       𝑅𝐶
              𝐻 𝑠
                      𝜙       𝑠        𝐶  𝐶       𝐾 𝐾        𝐾 𝐾
                                   𝑠         𝑠           𝑠
                                       𝑅𝐶 𝐶        𝑁𝐶        𝑁𝑅𝐶 𝐶
                                                                     29
Common PLL Noise Sources
              Phase Detector
      Sin                                    SiCP Loop Filter                SvR   VCO    SVCO
                       e                                             Vctrl         KVCO
in                           KPD                       F(s)                                  out
                                                                                     s

             fb
                                                            1
                                                            N
                                                        Divider

                                      𝑆            𝑆       𝑁𝑇𝐹        𝑠

                                      𝑆            𝑆       𝑁𝑇𝐹        𝑠

                                      𝑆             𝑆      𝑁𝑇𝐹 𝑠

                                  𝑆             𝑆          𝑁𝑇𝐹            𝑠

                            𝑆             𝑆            𝑆          𝑆           𝑆
                                                                                                          30
Noise Transfer Functions
                𝜙         𝑠       𝑁 𝐿𝐺 𝑠
  𝑁𝑇𝐹       𝑠
                𝜙        𝑠       1 𝐿𝐺 𝑠
                                  𝑁
                𝜙        𝑠          𝐿𝐺 𝑠
                                 𝐾
 𝑁𝑇𝐹    𝑠
                𝑖       𝑠        1 𝐿𝐺 𝑠
                                     𝐾
                𝜙   𝑠                    𝑠
  𝑁𝑇𝐹 𝑠
                 𝑣 𝑠             1       𝐿𝐺 𝑠
                    𝜙        𝑠            1
 𝑁𝑇𝐹        𝑠
                    𝜙        𝑠       1    𝐿𝐺 𝑠


• Input reference and charge pump noise is low-pass filtered
• Loop filter noise (VCO input noise) is band-pass filtered
• VCO output phase noise is high-pass filtered
                                                           31
PLL Phase Noise & Jitter                                    [Turker ISSCC 2018]




• PLL time-domain jitter is obtained by        • We can model an individual
  integrating the output phase noise             noise source’s contribution
             2                                     2
     𝜎,              𝑆     𝑓 𝑑𝑓            𝜎,                𝑆 𝑓 𝑁𝑇𝐹 𝑓   𝑑𝑓
             𝜔                                     𝜔

                                                       𝜎,          𝜎,

                         RMS Jitter 𝜎     𝜎,
                                                                              32
Wireline Transceiver Jitter Modeling




        [Richmond SiLabs]

• Relative jitter (dynamic phase error) between the RX CDR-generated
  sampling clock and input data sets the system timing margin
• This CDR high-pass response provides additional filtering
• Modeled as a 4MHz 1st-order response (IEEE 802.3 & OIF-CEI)
                        2
                𝜎   ,        𝑆 𝑓 𝑁𝑇𝐹 𝑓     𝐶𝐷𝑅 𝑓   𝑑𝑓
                        𝜔                                              33
Input Reference Noise
                            Phase Noise at 156.26MHz
Silicon Labs Ultra Low
Jitter Crystal Oscillator




• Reference jitter j,in = 226fsrms (10kHz – 10MHz)
                                                       34
Input Reference Noise
                             𝐾 𝐾        1
                                    𝑠
                               𝐶       𝑅𝐶
          𝑁𝑇𝐹   𝑠
                        𝐶  𝐶       𝐾 𝐾        𝐾 𝐾
                    𝑠         𝑠           𝑠
                        𝑅𝐶 𝐶        𝑁𝐶        𝑁𝑅𝐶 𝐶




• After PLL: j,in = 217fsrms (10kHz – 10MHz)
• Including CDR: j,in = 45fsrms (100Hz – 7GHz)
                                                      35
 Charge Pump Noise
                                           Tref
       MP                                               Trst=40ps, Tref=6.4ns
 VBP        in,MP
                              IN
                              FB
UP
                    iCP       UP
DN
                              DN
 VBN        in,MN
                                    Trst
       MN                     iCP


                          𝑇
            𝑆                       𝑆 ,           𝑆 ,
                          𝑇

• Charge pump noise current is injected into the loop filter
  during the PFD reset time
• Trade-off between charge pump noise contribution and
  deadzone robustness
• Transistor flicker noise can contribute significantly to PLL
  in-band phase noise                                                           36
Charge Pump Noise
                               𝐾       1
                                    𝑠
                                𝐶     𝑅𝐶
          𝑁𝑇𝐹   𝑠
                        𝐶  𝐶        𝐾 𝐾        𝐾 𝐾
                    𝑠          𝑠           𝑠
                        𝑅𝐶 𝐶         𝑁𝐶        𝑁𝑅𝐶 𝐶




• After PLL: j,CP = 205fsrms (10kHz – 10MHz)
• Including CDR: j,CP = 52fsrms (100Hz – 7GHz)
                                                       37
Loop Filter R Noise

         ICP
UP                                            w/ 4k Resistor
         Charging
                            Vctrl
                                          𝑆    4𝑘𝑇𝑅    162𝑑 𝐵 ⁄𝐻 𝑧
DN       Discharging   R     C2
         ICP
                       C1
                            F(s)



• Trade-off between resistor noise, loop filter
  capacitor size, and charge pump noise
     • Smaller resistor results in larger capacitors (higher area)
       and larger charge pump current (higher SiCP)
                                                                     38
Loop Filter R Noise
                                        𝐶   𝐶
                         𝐾       𝑠 𝑠
                                         𝑅𝐶 𝐶
          𝑁𝑇𝐹 𝑠
                      𝐶  𝐶             𝐾 𝐾        𝐾 𝐾
                  𝑠          𝑠                𝑠
                      𝑅𝐶 𝐶              𝑁𝐶        𝑁𝑅𝐶 𝐶




• After PLL: j,R = 128fsrms (10kHz – 10MHz)
• Including CDR: j,R = 81fsrms (100Hz – 7GHz)
                                                          39
VCO Noise
             LC-Oscillator
 w/ Differential Tank & Noise Sources
                          C1

                          Rp


                          in,Rp


                          L1
                         Vout


         in,M1                            in,M2
                    M1            M2



                 Vbias            in,M3
                         M3




• LC-VCO phase noise sources
  • Finite tank quality factor
  • Cross-coupled pair
  • Tail current source                           40
VCO Noise
                                      𝐶    𝐶
                              𝑠   𝑠
                                       𝑅𝐶 𝐶
         𝑁𝑇𝐹   𝑠
                       𝐶  𝐶           𝐾 𝐾          𝐾 𝐾
                   𝑠          𝑠                𝑠
                       𝑅𝐶 𝐶             𝑁𝐶         𝑁𝑅𝐶 𝐶




• After PLL: j,VCO = 257fsrms (10kHz – 10MHz)
• Including CDR: j,R = 125fsrms (100Hz – 7GHz)
                                                           41
Total Noise
                                                                          PLL Output
                                                        VCO     Ref Clk
                                                                 28%
                                                        38%

                                                               Charge Pump
                                                                    25%
                                                        Loop Filter
                                                           9%




                                                   Jitter
                                                  Variance                Ref Clk
                                                                            7%
                                                                          Charge Pump
                                                                              10%

                                                                  VCO       Loop Filter
                                                                  58%          25%

                                                                                    After CDR


• After PLL: j,Total = 414fsrms (10kHz – 10MHz)
   • Reference clock and charge pump noise dominates at low frequency
   • VCO dominates near loop bandwidth and higher
• Including CDR: j,Total = 164fsrms (100Hz – 7GHz)
   • Now VCO noise clearly dominates total
   • Loop resistor noise is a larger percentage                                             42
PLL Noise Transfer Function Take-Away Points

• The way a PLL shapes phase noise depends
  on where the noise is introduced in the loop
• Optimizing the loop bandwidth for one noise
  source may enhance other noise sources
• Generally, the PLL low-pass shapes input
  phase noise, band-pass shapes VCO input
  voltage noise, and high-pass shapes
  VCO/clock buffer output phase noise

                                             43
  Oscillator Noise
            Jitter




[McNeill]            44
Oscillator Phase Noise Model




                                                                          [Perrott]

                                    Noise Spectral Density 
                    L f   10 log                         dBc/Hz 
                                       Carrier Power       
                                    2 FkT   1 f  2  f 3  
  Leeson’s Model:   Lf   10 log       1    o
                                                       1  1/ f  
                                    Psig   2Q f      f  
                                                                 
• For improved model see Hajimiri papers
                                                                                      45
Open-Loop VCO Jitter
                                                 [McNeill]




                           DT




• Measure distribution of clock threshold crossings
• Plot  as a function of delay T
                                                             46
Open-Loop VCO Jitter
                                         [McNeill]




                                          T OL  T    T




• Jitter  is proportional to sqrt(T)
•  is VCO time domain figure of merit
                                                              47
 VCO in Closed-Loop PLL Jitter




[McNeill]



• PLL limits  for delays longer than loop bandwidth L
                          L  1 2f L
                                                          48
  Ref Clk-Referenced vs Self-Referenced
 [McNeill]       CDR Example




Ref Clock for
Frequency Synthesis PLL




 • Generally, we care about the jitter w.r.t. the ref. clock (x)
 • However, may be easier to measure w.r.t. delayed version of output clk
     • Due to noise on both edges, this will be increased by a sqrt(2) factor relative
       to the reference clock-referred jitter                                       49
Converting Phase Noise to Jitter
                                                                                      [Mansuri]




                                                                8
• RMS jitter for T accumulation                      𝜎
                                                                𝜔
                                                                          𝑆 𝑓 𝑠𝑖𝑛 𝜋𝑓Δ𝑇 𝑑𝑓

• As T goes to ∞               2                     2 
                       T2          R  0          S       f df
                               o2                 2
                                                  o 0
• Actual integration range depends on application bandwidth
   • fmin set by assumed CDR tracking bandwidth
   • fmax set by Nyquist frequency (f0/2)
                                                       f0
                                                  2         2                  2
• Most exact approach                  T2 
                                               o2
                                                           S  f  H sys  f  df
                                                          0
                                               2
                       where H sys  f               is the system jitter transfer function      50
Time Domain Model
• Time domain models captures the discrete-time operation
  of the PLL architectures
   • Interaction between charge pump and loop filter
   • Cycle slipping behavior
• Allows modeling of non-linear control systems
   • Dynamic loop bandwidth control
   • Automatic frequency band selection
• Potential implementation tools
   • Matlab Simulink
   • CppSim
   • Cadence
                                                            51
Simulink Model




      PFD
                 Loop Filter




                               52
Frequency Step w/ Simulink Model
• VCO control voltage response to input frequency step
     KVCO=2*1GHz/V (LC Osc)              KVCO=2*10GHz/V (Ring Osc)




• Voltage spikes due to charge pump current driving loop filter resistor
• Cycle slipping occurs during lock acquisition due to large initial
  frequency difference
                                                                           53
CppSim Model                             [Perrott/Meninger]




• https://cppsim.com/
• C++ based allows for rapid
  simulation of advanced architectures
• Many useful building blocks included

                                                         54
Cadence Verilog-A Model




    VCO (Square Wave)
   Verilog-A Code Snippet




                            55
Next Time
• CDRs

• The following slides provide more details
  on PLL circuits. This 620 material may
  useful for the project, but won’t be covered
  in detail on Exam 2.




                                                 56
PLL Loop Gain
          Phase Detector
                                    Loop Filter                   VCO

                   e                             Vctrl           KVCO
   in                   KPD          F(s)                                out
                                                                   s

         fb
                                        1
                                        N
                                     Divider



                                                                     1
                            𝐾 𝐹 𝑠 𝐾            𝐾 𝐾            𝑠
                                                                    𝑅 𝐶
                   𝐿𝐺 𝑠
                               𝑁𝑠                                 𝐶   𝐶
                                               𝑁𝐶 𝑠       𝑠
                                                                  𝑅 𝐶𝐶

                         1                                          𝐶  𝐶
               𝜔            ,   𝜔       𝜔         0,      𝜔
                        𝑅 𝐶                                         𝑅 𝐶𝐶

                                                                                  57
Loop Gain Response
                        𝐾 𝐾      𝑠       𝜔
                𝐿𝐺 𝑠                               𝜔       𝜔     0
|LG|(dB)                𝑁𝐶 𝑠 𝑠       𝜔
                                                            1
                                                       𝜔
                                                           𝑅 𝐶
                                                           𝐶  𝐶
           z      u     p3                      𝜔
      0                                                   𝑅 𝐶𝐶



    LG
                                                   𝜔              𝜔
                                     Φ       tan           tan
 -135°           m                                𝜔              𝜔

 -180°



                                                                      58
Design Procedure for Max m
                            𝐾 𝐾      𝑠       𝜔       PLL Specs
                    𝐿𝐺 𝑠
 |LG|(dB)                   𝑁𝐶 𝑠 𝑠       𝜔       Parameter
                                                   Fref      156.25MHz
                                                    N            90
                                                   Fvco       14GHz
               z      u     p3
       0                                           fu         2MHz
                                                    m          60°


                                                   Kvco      2π*1GHz/V

     LG                                             R            ??
                                                    C1           ??

  -135°              m                             C2           ??
                                                    Icp          ??

  -180°

• Design procedure maximizes phase margin for a given fu
  and m specification [Hanumolu TCAS1 2004]                             59
Design Procedure for Max m
1. Set loop filter capacitor ratio based on m
                  𝐶
             𝐾            2 𝑡𝑎𝑛 Φ              𝑡𝑎𝑛 Φ          𝑡𝑎𝑛 Φ      1
                  𝐶
                               Φ           60° → 𝐾        12.9
2. Set loop filter values based on u & with R set for low noise
                                                  𝜔
                                       𝜔
                                               1      𝐾
                                            1             𝐶
                                   𝐶           , 𝐶
                                           𝜔 𝑅            𝐾
                    𝜔         2𝜋 ∗ 2𝑀𝐻𝑧 → 𝜔   2𝜋 ∗ 536𝑘𝐻𝑧
                  Set 𝑅       4𝑘Ω → 𝐶    74𝑝𝐹 & 𝐶     5.8𝑝𝐹
3. Set Icp to achieve required loop gain

              N𝐶 𝜔    𝜔            𝜔
         𝐼
               𝐾          𝜔     𝜔             𝜔           2𝜋 ∗ 7.45𝑀𝐻𝑧 → 𝐼   310𝜇𝐴
                                                                                     60
Simulated Responses
                                                  𝐾 𝐾        1
           𝐾 𝐾      𝑠       𝜔   𝜙    𝑠                   𝑠
                                                    𝐶       𝑅𝐶
    𝐿𝐺 𝑠                                     𝐶  𝐶       𝐾 𝐾        𝐾 𝐾
           𝑁𝐶 𝑠 𝑠       𝜔       𝜙   𝑠    𝑠         𝑠           𝑠
                                             𝑅𝐶 𝐶        𝑁𝐶        𝑁𝑅𝐶 𝐶




• Design achieves fu=2MHz and m=60°
• Closed loop response has f3dB=3.1MHz
                                                                      61
Charge-Pump PLL Circuits
• Phase Detector
• Charge-Pump
                                  PFD

• Loop Filter   Fin
                      in(t)
                              D
                                  R
                                      Q
                                          UP        ICP

                                                           Vctrl
                                                                              Fout = N*Fin

                                                                        VCO       out(t)
                                          DN
• VCO
                      fb(t)       R
                                      Q                   R        C2
                              D
                                                    ICP
                                                          C1


• Divider                                      Divider

                                                1/N




                                                                                           62
Phase Detector
              Phase Detector                                             IN
                                              Loop Filter
                                                                         FB
                      e                 ve                 vctrl
     in                     KPD                 F(s)                        
                                                                           avg 𝑣 𝑡      𝐾 Δ𝜙
            fb
                                                                                avg{ve(t)}
• Detects phase difference between feedback clock
  and reference clock
• The loop filter will filter the phase detector output,                                     KPD
  thus to characterize phase detector gain, extract
                                                                                                   
  average output voltage
• The KPD factor can change depending on the
  specific phase detector circuit
                      K PD units are V/rad when used with a dimension - less filter

           K PD units are rad -1 (averaged) or A/rad when combined with the charge - pump

                                  when used with a impedance filter                                 63
Analog Multiplier Phase Detector
           A1 cos 1t
                                  A1 A2                                     A1 A2
                                                cos1  2 t                  cos1  2 t   
                                        2                                       2
    A2 cos2t   
                         is mixer gain

• If 1=2 and filtering out high-frequency term
                                        A1 A2
                             y t               cos 
                                            2
                                                     A1 A2          
•   Near  lock region of /2: yt                   2
                                                              
                                                                2
                                                                    
                                                                      
                                                                       A1 A2
                                                            K PD  
                                                                         2




                                                                              [Razavi]
                                                                                                        64
XOR Phase Detector




                                                                 [Razavi]

• Assuming logic 1=“+1” and 0=“-1”, the XOR PD will lock
  when the average output is 0
   • Generally, /2 is a stable lock point and -/2 is a metastable point
• Sensitive to clock duty cycle                                             65
XOR Phase Detector



Width is same for both
leading and lagging
phase difference!        [Perrott]




                                     66
Cycle Slipping
• If there is a frequency difference between the input
  reference and PLL feedback signals the phase detector can
  jump between regions of different gain
   • PLL is no longer acting as a linear system


                                                                                 [Perrott]




                 (positive feedback operation)   (negative feedback operation)
                                                                                             67
Cycle Slipping




               Cycle Slipping




                                                    [Perrott]


• If frequency difference is too large the PLL may not lock
                                                                68
  Phase Frequency Detector (PFD)
                              • Phase Frequency Detector allows for
                   PFD          wide frequency locking range,
               D
 CLKIN             R
                       Q   UP   potentially entire VCO tuning range
                              • 3-stage operation w/ UP & DN outputs
 CLKFB             R          • Rising edge-triggered results in duty
                       Q   DN
               D                cycle insensitivity
                   Tref                              CLKFB           CLKIN
CLKIN                                 CLKFB                                         CLKIN
         te                                   UP=0           UP=0            UP=1
CLKFB                                         DN=1           DN=0            DN=0

                                                 CLKIN                 CLKFB
  UP                                                         Delay

  DN
              Trst                                           RST=1
   iCP


                                                                                      69
 Averaged PFD Transfer Characteristic
  UP=1 & DN=-1                     avg{ve(t)}
          PFD                         1
      D
              Q   UP
in       R

                       -4   -2
                                                          in-fb
fb       R
              Q   DN                      1     2   4
      D
                                          2
                                     -1



• Constant slope and polarity asymmetry about zero phase
  allows for wide frequency range operation
• The averaged PFD gain is 1/(2) with units of rad-1

                                                                70
Phase Detector

                  fref                fe



                            ffb




• Detects phase difference between feedback clock and reference clock
• The loop filter will filter the phase detector output, thus to characterize
  phase detector gain, extract average output voltage (or current for
  charge-pump PLLs)
                                                                            71
PFD Deadzone
                                                         Tref
      D           UP    ICP
              Q                         CLKIN
in       R
                                                 te
                       iCP              CLKFB
fb       R
                              R           UP                              too narrow
      D
              Q                    C2
                  DN    ICP
                              C1          DN
                                                      Trst
                                           iCP


• If phase error is small, then short                        avg{ve(t)}
  output pulses are produced by PFD                          (Zoomed)


• Cannot effectively propagate these
                                                      Dead
  pulses to switch charge pump                        Zone
• Results in phase detector “dead                                            in-fb

  zone” which causes low loop gain
  and increased jitter
                                                                                       72
PFD Operation w/ Reset Delay
• Solution is to add delay in PFD
  reset path to force a minimum                              UP
                                            D                      ICP
  UP and DN pulse length          in           R
                                                    Q

                                                                  iCP
• In locked state both UP and
                                                        Td
  DN current sources are on for      fb        R
                                                    Q                    R    C2
  Trst, but ideally no net current          D
                                                             DN    ICP
  is delivered to loop filter                                            C1
                          Tref
         CLKIN
                   te
        CLKFB

            UP                       reliable width


           DN
                        Trst
             iCP

                                                                              73
   Problems Near 2
  • PFD cannot react to input
    rising edges during reset                                      UP
                                                  D                      ICP
  • This can result in the next          in          R
                                                          Q

    rising edge driving the loop in                                     iCP
    the wrong direction                                       Td
                                         fb          R
                                                                               R
  • Reset delay can increase                      D
                                                          Q                         C2
                                                                   DN    ICP
    acquisition time and sets a                                                C1
    max PFD operating frequency
           Tref     missed edge!
CLKIN
           te
CLKFB
  UP

  DN
                      Trst
   iCP

                                      wrong direction!
                                                                                    74
PFD Transfer Characteristic w/ Reset Delay
                                     avg{ve(t)}              Ideal PFD
                         wrong                               PFD w/ Trst
                       frequency          1
                      information!

                -4         -2
                                                                        in-fb
                                                        2        4

                                                                 Trst
                                                      2
                                                                 Tref
                                       -1


• PFD reset delay generates wrong frequency information
• If this becomes a large percentage of the reference cycle,
  then the PFD can fail to acquire frequency lock
                                              𝑇
                                  Max 𝑇
                                                  2
                                                        1
                       Max PFD Frequency
                                                       2𝑇
                                                                                  75
Charge-Pump PLL Circuits
• Phase Detector
• Charge-Pump
                                  PFD

• Loop Filter   Fin
                      in(t)
                              D
                                  R
                                      Q
                                          UP        ICP

                                                           Vctrl
                                                                              Fout = N*Fin

                                                                        VCO       out(t)
                                          DN
• VCO
                      fb(t)       R
                                      Q                   R        C2
                              D
                                                    ICP
                                                          C1


• Divider                                      Divider

                                                1/N




                                                                                           76
Charge Pump
                                           • Converts PFD output
     ICP
                                             signals to charge
UP   Charging
                                 Vctrl
DN   Discharging       R           C2      • Charge is proportional
     ICP                                     to PFD pulse widths
                      C1
                                 F(s)

             Un - Averaged Charge - Pump Gain  I CP Amps
                                                 I  Amps 
              Averaged Charge - Pump Gain  CP                
                                                 2  rad 
                                                   I  Amps 
             Total PFD & Charge - Pump Gain  CP                
                                                   2  rad 
           This gain can vary if a different phase detector is used
                                                                      77
Simple Charge Pump
                                              M2
                                        VBP
                                              M4
                                                    ICP
                       D           UP    UP
                               Q
             CLKIN         R
                                                   iCP
                                                                Vctrl
            CLKFB          R
                               Q
                                                          R     C2
                       D
                                   DN         M3
                                                    ICP C
                                                            1
                                        VBN
                                              M1


• Issues
   •   Skew between UPB and DN control signals
   •   Matching of UP/DN current sources
   •   Clock feedthrough and charge injection from switches onto Vctrl
   •   Charge sharing between current source drain nodes’ capacitance and Vctrl

                                                                                  78
  Simple Charge Pump Skew Compensation
  T-gate                           M2
                             VBP                            • Adding a transmission gate in the
          D           UP      UP M4
                                         ICP                  DN signal path helps to equalize
 CLKIN        R
                  Q
                                                              the delay with the UPB signal for
                                        iCP
                                                      Vctrl   better overlap between the UP
CLKFB                                          R
                                                              and DN current sources
              R
                  Q                                  C2
          D
                      DN      DN M3
                                         ICP C
                             VBN
                                                 1          • Poor matching of UPB and DN
                                   M1                         edge rates

3/2 Inverter Path
                                   M2
         FODN > FOUP         VBP

          D           UP   FOUP    M4
                                         ICP
                                                            • Utilizing a 3-inverter UP path
                  Q
 CLKIN        R
                                        iCP
                                                              and a 2-inverter DN path with
                                                      Vctrl
                                                              a higher fanout provides good
CLKFB         R                                R     C2
          D
                  Q
                      DN           M3
                                                              matching of both delay and
                           FODN          ICP C
                                                 1            edge rates
                             VBN
                                   M1

                                                                                               79
 Charge Pump Mismatch
                               Ideal locked condition, Actual locked condition
                                  but CP mismatch         w/ CP mismatch
      M2
                                                                   Tos
VBP                              UP                     UP
      M4
            IUP
                                DN                    DN
UP                                                                                                             ∆𝐼
                                 IUP                    IUP                                        𝐼       𝐼
           iCP
                       Vctrl                                                                                   2
                  R              IDN                    IDN                                                    ∆𝐼
DN                    C2               Trst                             Trst                  𝐼           𝐼
      M3                                                                                                       2
           IDN C                  iCP                    iCP
                   1
VBN
      M1                        Vctrl                  Vctrl
                                                  t                                            t
                                                               𝐼         𝑇            ∆𝐼 𝑇
• PLL will lock with static phase error
  if there is a charge pump mismatch                                             ∆𝐼 𝑇
                                                                    𝑇
• Extra “ripple” on Vctrl                                                                  ∆𝐼
                                                                                 𝐼
                                                                                           2
      • Results in frequency domain spurs
        at the reference clock frequency                                             ∆𝐼                𝑇
                                                         𝜙          2𝜋
        offset from the carrier                                                           ∆𝐼           𝑇
                                                                             𝐼
                                                                                          2                    80
Charge Pump w/ Improved Matching

                     • Parallel path keeps current
                       sources always on

                     • Amplifier keeps current source
                       VDS voltages constant resulting
                       in reduced transient current
                       mismatch (charge sharing)




 [Young JSSC 1992]

                                                     81
Digital Leakage Compensation
                                                   [Fan ISSCC 2019]
• Charge pump off-state leakage causes PLL
  to lock with static phase error
• Compensated by additional digitally-controlled
  charge pump current pulses
• TDC detects phase error between input
  reference clock and feedback clock




                                                                      82
Charge Pump w/ Reversed Switches
• Swapping switches
  reduces charge injection
   • MOS caps (Md1-4) provide
     extra clock feedthrough
     cancellation
• Helper transistors Mx and
  My quickly turn-off current
  sources
• Dummy branch helps to
  match PFD loading
• Helps with charge
                                [Ingino JSSC 2001]
  injection, but charge
  sharing is still an issue
                                                     83
Charge-Pump PLL Circuits
• Phase Detector
• Charge-Pump
                                  PFD

• Loop Filter   Fin
                      in(t)
                              D
                                  R
                                      Q
                                          UP        ICP

                                                           Vctrl
                                                                              Fout = N*Fin

                                                                        VCO       out(t)
                                          DN
• VCO
                      fb(t)       R
                                      Q                   R        C2
                              D
                                                    ICP
                                                          C1


• Divider                                      Divider

                                                1/N




                                                                                           84
Charge Pump PLL Passive PI Loop Filter
             Single-Ended                   Fully Differential




• Simple passive filter is most commonly used
• Integrates low-frequency phase errors onto C1 to set average frequency
• Resistor (proportional gain) isolates phase correction from frequency
  correction
• Primary capacitor C1 affects PLL bandwidth
• Zero frequency affects PLL stability
• Resistor adds thermal noise which is band-pass filtered by PLL
                                                                      85
Loop Filter Transfer Function
• Neglecting secondary capacitor, C2




                                       86
Loop Filter Transfer Function
• With secondary capacitor, C2




                                 87
Why have C2?
• Secondary capacitor smoothes control voltage ripple
• Can’t make too big or loop will go unstable
   • C2 < C1/10 for stability
   • C2 > C1/50 for low jitter


                                         Control Voltage Ripple




                                                                  88
Loop Filter Capacitors
• To minimize area, we would like to use highest density caps
• Thin oxide MOS cap gate leakage can be an issue
   • Similar to adding a non-linear parallel resistor to the capacitor
   • Leakage is voltage and temperature dependent
   • Will result in excess phase noise and spurs

• Metal caps or thick oxide caps are a better choice
   • Trade-off is area

• Metal cap density can be <1/10 thin oxide caps
• Filter cap frequency response can be relatively low, as PLL
  loop bandwidths are typically 1-50MHz

                                                                         89
Charge-Pump PLL Circuits
• Phase Detector
• Charge-Pump
                                  PFD

• Loop Filter   Fin
                      in(t)
                              D
                                  R
                                      Q
                                          UP        ICP

                                                           Vctrl
                                                                              Fout = N*Fin

                                                                        VCO       out(t)
                                          DN
• VCO
                      fb(t)       R
                                      Q                   R        C2
                              D
                                                    ICP
                                                          C1


• Divider                                      Divider

                                                1/N




                                                                                           90
Voltage-Controlled Oscillator
                                                    out


                                                0                               KVCO
vctrl(t)           VCO              out(t)

                                                                                             Vctrl
                                                                          Vctrl0
                                                𝜔     𝑡      𝜔       Δ𝜔      𝑡     𝜔    𝐾     𝑣      𝑡

• Time-domain phase relationship
                                                            Laplace Domain Model
  𝜙        𝑡       Δ𝜔      𝑡 𝑑𝑡      𝐾      𝑣       𝑡 𝑑𝑡

                                   rad
                  KVCO units are                                            KVCO
                                   sV                    vctrl(t)                          out(t)
               2 1MHz              rad                                    s
                           2  10 6
                    V                 sV
                                                                                                     91
Voltage-Controlled Oscillators (VCO)
• Ring Oscillator
  • Easy to integrate
  • Wide tuning range (5x)
  • Higher phase noise


• LC Oscillator
  • Large area
  • Narrow tuning range (20-30%)
  • Lower phase noise



                                   92
Barkhausen’s Oscillation Criteria

                                                            [Sanchez]



                                         n


                                       H  j 
    Closed-loop transfer function:
                                     1  H  j 

• Sustained oscillation occurs if            H  j   1


• 2 conditions:
   • Gain = 1 at oscillation frequency 0
   • Total phase shift around loop is n360 at oscillation frequency 0
                                                                          93
Ring Oscillator Example




                                  𝐴
                        𝐻 𝑠
                                  𝑠
                              1
                                  𝜔


     Phase Condition: tan         45° → 𝜔       𝜔


      Gain Condition:             1→𝐴       2   𝑔   𝑅

                                                        94
LC Oscillator Example
               • Oscillation phase shift condition
                 satisfied at the frequency when
                 the LC (and R) tank load
                 displays a purely real
                 impedance, i.e. 0 phase shift

                          LC tank impedance

                                            RS  L1s
                        Z eq s  
                                      1  L1C1s 2  RS C1s

                                                RS2  L12 2
                  Z eq s  j  
                                2

                                       1  L C    R C 
                                            1   1
                                                    2 2        2
                                                               S   1
                                                                    2   2
LC Oscillator Example
               • Transforming the series loss
                 resistor of the inductor to an
                 equivalent parallel resistance




                               RS2                    L12 2
                  LP  L1 1  2 2 , C P  C1 , RP 
                            L1                        RS
                    RP




                                         1
                                1                      [Razavi]
                                        LP C P
                                                                 96
LC Oscillator Example
                               Loop Gain
                                                [Razavi]




                                                      1
              • Phase condition satisfied at 1 
                                                     LP C P

              • Gain condition satisfied when g m RP   1
                                                       2



              • Can also view this circuit as a parallel
                combination of a tank with loss resistance
                2RP and negative resistance of 2/gm
              • Oscillation is satisfied when
                                 1
                                     RP
                                 gm
                                                              97
Supply-Tuned Ring Oscillator




                                            [Sidiropoulos VLSI 2000]
                             2nC stage
            TVCO  2nTD 
                             Vc  Vth 

                     fVCO     
            KVCO          
                      Vc    2nC stage
                                                                 98
Current-Starved Ring Oscillator




                                  [Sanchez]




                                         99
Capacitive-Tuned Ring Oscillator




                                   100
Symmetric Load Ring Oscillator
                                      [Maneatis JSSC 1996 & 2003]




                                2ID




• Symmetric load provides frequency tuning at excellent
  supply noise rejection
• See Maneatis papers for self-biased techniques to obtain
  constant damping factor and loop bandwidth (% of ref clk)
                                                              101
LC Oscillator
• A variable capacitor
  (varactor) is often used to
  adjust oscillation frequency

• Total capacitance includes
  both tuning capacitance and
  fixed capacitances which
  reduce the tuning range
              1                 1
    osc           
             LP C P     LP Ctune  C fixed 



                                                102
Varactors
• pn junction varactor
   • Avoid forward bias region to prevent oscillator nonlinearity




• MOS varactor                                                      [Perrott]

   • Accumulation-mode devices have better Q than inversion-mode




  n-well
                                                                    [Razavi]
                                                                           103
Charge-Pump PLL Circuits
• Phase Detector
• Charge-Pump
                                  PFD

• Loop Filter   Fin
                      in(t)
                              D
                                  R
                                      Q
                                          UP        ICP

                                                           Vctrl
                                                                              Fout = N*Fin

                                                                        VCO       out(t)
                                          DN
• VCO
                      fb(t)       R
                                      Q                   R        C2
                              D
                                                    ICP
                                                          C1


• Divider                                      Divider

                                                1/N




                                                                                       104
Loop Divider

                                 out(t)     1      fb(t)
                                             N

                          out(t)
                           fb(t)
                                            N=8
• Time-domain model                           • The loop divider is
                        1                       dimension-less in the PLL
           fb t       out t 
                        N                       linear model
                1              1
 fb t        out t dt  out t 
                N              N
                                                                            105
Basic Divide-by-2

                      Latch          Latch




• Divide-by-2 can be realized by a
  flip-flip in “negative feedback”

• Divider should operate correctly
  up to the maximum output clock
  frequency of interest PLUS
  some margin


                                             106
Divide-by-2 with TSPC FF
True Single Phase Clock Flip-Flop
                                                   Divider Equivalent Circuit
                                                   Note: output inverter not in left schematic

                                   Q




• Advantages
   • Reasonably fast, compact size, and no static power
   • Requires only one phase of the clock
• Disadvantages
   • Signal needs to propagate through three gates per input cycle
   • Need full swing CMOS inputs
   • Dynamic flip-flop can fail at low frequency (test mode) due to leakage, as
     various nodes are floating during different CLK phases & output states
       • Ex: Q_bar is floating during when CLK is low                                       107
Divide-by-2 with CML FF

               D    Q       D     Q

               DB QB        DB   QB

         CLK
        CLKB



• Advantages
   • Signal only propagates through two CML gates per input cycle
   • Accepts CML input levels
• Disadvantages
   • Larger size and dissipates static power
   • Requires differential input
   • Need tail current biasing
• Additional speedup (>50%) can be achieved with shunt peaking
  inductors                                                         108
  Binary Dividers:
   Asynchronous vs Synchronous
 Asynchronous Divider                              • Advantages
                                                        • Each stage runs at lower frequency,
                                                          resulting in reduced power
          D     Q   D        Q   D    Q        CLK/8
                                                        • Reduced high frequency clock
               QB        QB          QB
                                                          loading
CLK
                                                   • Disadvantage
                                                        • Jitter accumulation


                                                   • Advantage
                                                        • Reduced jitter
 Synchronous Divider
                                                   • Disadvantage
      D    Q        D    Q            D    Q
                                                        • All flip-flops work at maximum
          QB            QB                QB    CLK/8     frequency, resulting in high power
                                                        • Large loading on high frequency
CLK
                                                          clock

                                                                                          109
  Jitter in Asynchronous vs Synchronous Dividers
  Asynchronous                                       • Jitter accumulates with the
                                                       clock-to-Q delays through
          D     Q   D        Q   D    Q        CLK/8   the divider
               QB        QB          QB
                                                     • Extra divider delay can also
CLK                                                    degrade PLL phase margin




                                                     • Divider output is “sampled”
  Synchronous                                          with high frequency clock
      D    Q        D    Q            D    Q          • Jitter on divider clock is
          QB            QB                QB    CLK/8   similar to VCO output
CLK                                                  • Minimal divider delay

                                                                                     110
Dual Modulus Prescalers
                                   2/3

                                                         MC=0  3
                                                         MC=1  2


                                 15/16

[Razavi]


                                                             MC=0  15
                                                             MC=1  16


  Synchronous 3/4                         Asynchronous 4
• For /15, first prescaler circuit divides by 3 once and 4 three times
  during the 15 cycles
                                                                         111
 Injection-Locked Frequency Dividers
   LC-oscillator type (/2)            Ring-oscillator type (/3)




[Verma JSSC 2003, Rategh JSSC 1999]         [Lo CICC 2009]
• Superharmonic injection-locked oscillators (ILOs) can
  realize frequency dividers
• Faster and lower power than flip-flop based dividers
• Injection locking range can be limited
                                                                  112
