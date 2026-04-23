---
layout: post
title:      "lecture1 ee720 intro"
date:       2026-04-21 09:14:22
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

    Lecture 1: Introduction




           Sam Palermo
   Analog & Mixed-Signal Center
       Texas A&M University
Class Topics
• System and design issues relevant to high-speed
  electrical (and optical) signaling
• Channel properties
  • Modeling, measurements, communication techniques

• High-Speed link circuits
  • Drivers, receivers, equalizers, timing systems

• Link system design
  • Modeling and performance metrics

• Link system examples
                                                       2
Administrative
• Instructor:
  • Sam Palermo
  • 315E WEB, 845-4114, spalermo@tamu.edu
  • Office hours: M 8:30AM-10:00AM, R 4:00PM-5:30PM
• Lectures
  • TR 9:35AM-10:50AM, ZACH 361
  • Videos posted on Canvas
• Lab: M 12:40PM-3:30PM, ZACH 127
  • Lab begins on January 30
• Class web page
  • https://people.engr.tamu.edu/spalermo/ecen720.html
  • Will use Canvas for turning in assignments
                                                         3
Class Material
• Textbook: Class Notes and Technical Papers
• Key References
  • Digital Systems Engineering, W. Dally and J. Poulton, Cambridge
    University Press, 1998.
  • Advanced Signal Integrity for High-Speed Digital Designs, S. H.
    Hall and H. L. Heck, John Wiley & Sons, 2009.
  • High-Speed Digital Design: A Handbook of Black Magic, H.
    Johnson & M. Graham, Prentice Hall, 1993.
  • Design of Integrated Circuits for Optical Communications, B.
    Razavi, McGraw-Hill, 2003.

• Class notes
  • Will post online before class


                                                                      4
Grading
• Exams (50%)
   • Two midterm exams (25% each)

• Homework & Labs (25%)
   • Labs (Prelab + Report) and homeworks weighted equally
   • Collaboration is allowed, but independent simulations and write-ups
   • Need to setup CADENCE simulation environment
   • Turn in via Canvas
   • No late homework/labs will be graded

• Final Project (25%)
   • Groups of 1-3 students
   • Report and PowerPoint presentation required


                                                                           5
Prerequisites
• This is a circuits AND systems class
• Circuits
  • ECEN474/704 or approval of instructor
  • Basic knowledge of CMOS gates, flops, etc…
  • Circuit simulation experience (HSPICE, Spectre)
• Systems
  • Basic knowledge of s- and z-transforms
  • Basic digital communication knowledge
  • MATLAB experience

                                                      6
Simulation Tools
• Matlab
• ADS (Statistical BER link analysis)
• Cadence
• 90nm CMOS device models
  • Can use other technology models if they are a
    90nm or more advanced CMOS node

• Other tools, schematic, layout, etc… are
  optional
                                                    7
High-Speed Serial I/O
• Found in applications ranging from         AMD EPYC Rome Platform

  high-end computing systems to
  smart mobile devices

• Typical processor platform
   •   Processor-to-memory: DDR4
   •   Processor-to-peripheral: PCIe & USB
   •   Storage: SATA
   •   Network: LAN


• Mobile systems
   • DSI : Display Serial Interface
   • CSI : Camera Serial Interface
   • UniPRO : MIPI Universal Protocol
                                                                      8
Data Center Links
• Different interconnect
  technologies are used to
  span various distances

• Electrical I/O
   • Chip-to-module
   • Intra-rack


• Optical I/O
   • TOR switch to edge switch
                                 [Gigalight]
   • Future intra-rack



                                           9
     Increasing I/O Bandwidth Demand
             Ethernet Switch Bandwidth
                                         PAM2       PAM4




[Zhou Opt. Fiber Tech. 2017]

    • Aggressive scaling of I/O data rates is required for
      data centers and HPC systems
    • PAM4 modulation offers higher spectral efficiency
      and is commonly used in electrical I/Os operating
      above 50Gb/s                                        10
High-Speed Electrical Link System




                                    11
Electrical Backplane Channel




• Frequency dependent loss
  ̶ Dispersion & reflections

• Co-channel interference
  ̶ Far-end (FEXT) & near-end (NEXT) crosstalk
                                                 12
Channel Performance Impact




                             13
Channel Performance Impact




                             14
   Backplane Link Example


    A 10Gb/s 5-tap DFE / 4-Tap FFE
Transceiver in 90nm CMOS Technology

    Mounir Meghelli, Sergey Rylov, John Bulzacchelli, Woogeun Rhee,
    Alexander Rylyakov, Herschel Ainspan, Ben Parker, Michael
    Beakes, Aichin Chung, Troy Beukema, Petar Pepeljugoski, Lei
    Shan, Young Kwark, Sudhir Gowda and Dan Friedman


    IBM T. J. Watson Research Center, Yorktown Heights, NY




                                                                      15
                                                               Transmission Channel Impairments
                                                                                                                                                                                                           Eye FFE1 10.0Gb/s [OPEN,1e-8] No Xtalk
                                                                                                                                                                                    500mVDATA = RAND Tx 600mVpd AGC Gain -5.48dB


                                                       INPUT                                                               Packaged SerDes                                          400mV
                                                                                                                                                                                         XTALK = NONE             AGC 5.0GHz 0.00dB
                                                                                                                                                                                         PKG=0/0 TERM = 5050/5050 IC = 3/3


                                              Eye FFE1 10.0Gb/s [OPEN,1e-8] No Xtalk                                                                                                300mV

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
                                                                                                        Line card trace                                                             -200mV

                                                                                                                                                                                    -300mVHSSCDR = 2.3.2-pre2 IBM Confidential
                                                                                                                                                                                          Date = Sat 01/21/2006 12:00 PM
                       -100mV                                                                                                                                                             PLL=0F1V0S0,C16,N32,O1,L80FREQ=0.00ppm/0.00us
                                                                                                                                                                                    -400mVFFE = [1.000, 0.000]



                                                                                                      Edge connector
                       -200mV                                                                                                                                                       -500mV
                                                                                                                                                                                       -100ps            -50ps              0ps               50ps   100ps
                       -300mVHSSCDR = 2.3.2-pre2 IBM Confidential                                                                                                                                                          Time



                                                                                                                                                                                                                 OUTPUT
                             Date = Sat 01/21/2006 12:01 PM
                             PLL=0F1V0S0,C16,N32,O1,L80FREQ=0.00ppm/0.00us
                       -400mVFFE = [1.000, 0.000]




                                                                                                        Via stub
                       -500mV
                          -100ps            -50ps              0ps               50ps        100ps
                                                              Time




                                                                                        [OPEN,1e-8] Channel Response
                                      10                                                                                          60

                                       0                                                                                          50

                                     -10                                                                                          40

                                     -20                                                                                          30

                                     -30                                                                                          20
                                                                                                                                   |S11|,|S22|
                        |SDD21|
                        S21




                                     -40                                                                                          10

                                     -50                        -24.6dB @ 5GHz                                                    0

                                     -60                                                                                          -10

                                     -70                                                                                          -20

                                     -80                                                                                          -30

                                     -90                                                                                          -40
                                       0Hz                           2.0GHz                 4.0GHz        6.0GHz       8.0GHz   10GHz
                                                                                                 Frequency




                                                       Pkg                                   Line card                   Edge    Backplane   Edge      Line card                                                   Pkg
                                                                                               trace                   connector 16” trace connector     trace
      Tx IC                                                                                                                     The Channel                                                                      Rx IC
[Meghelli (IBM) ISSCC 2006]
                                                                                                                                                                                                                                                             16
               10Gb/s SerDes Main Features


 Tx with 1 baud-spaced 4-tap FFE

 Rx with 5-tap adaptive DFE and digital clock recovery

 LC-VCO based PLL for low noise clock generation

 90nm CMOS technology




[Meghelli (IBM) ISSCC 2006]
                                                          17
                                     Transmitter Architecture
Key Features:                                           FFE Taps                Full Scale       DAC bits
- Half-rate CML design         Pre-cursor                                       25%               4
- 4-tap FFE                                                                                                                 VDDA=1.2V
                               Cursor                                           100%              6
- Tap polarity control         1st Post-cursor                                  50%               5                            50Ω
- ESD protection                                                                                                ESD
                               2nd Post-cursor                                  25%               4
                                                                                                                                     Out-P
- 70mW (24mA main tap, no FFE)
                                                                                                                                     Out-N
                               VDD=1.0V                                  VDDA=1.2V
                                                                                                                                  (10Gb/s)
                                              IDACs
                                                &                  1/4                 1              1/2             1/4
                                               Bias
                                              Control
                                                                   1x                  4x             2x              1x


                  VDDIO=1.0V

                                                           sgn-1            sgn0             sgn1           sgn2
                      1        2    (5Gb/s)
             D0
                                                 L                          L                L              L
 (2.5Gb/s)




                      1        2
             D1
                                   4:2
                      1        2   MUX
             D2
                      1        2                 L         L                L                L              L
             D3


                                          2
                                             C2 (5GHz)
                                          From on-chip PLL           “A Low Power 10Gb/s Serial Link Transmitter in 90-nm CMOS”
[Meghelli (IBM) ISSCC 2006]                                          A. Rylyakov et al., CSICS 2005
                                                                                                                                             18
           Tx Output Eye Diagram @ 10Gb/s
                                         e FFE1 10.0Gb/s [OPEN,1e-8] No Xtalk

                                         x 600mVpdAGC Gain -6.02dB
                                                   AGC 5.0GHz 0.00dB
                                          = 5050/5050 IC = 3/0




No FFE, 24mA on main tap


                                          IBM Confidential
                                          EQ OFS = 0.00ppm/0.00us
                                         000]
                              Measured                             Simulated
                                         0ps                 0ps                50ps            100ps
                                                            Time




                                                Eye FFE4 10.0Gb/s [OPEN,1e-8] No Xtalk

                                            00mVpd      AGC Gain -6.02dB
                                                        AGC 5.0GHz 0.00dB
                                           5050 IC = 3/0




FFE 4=[0, 85%, -15%, 0, 0]

                                          nfidential
                                          Q OFS = 0.00ppm/0.00us        D/E OFST 1
                                          37, 0.000]



                                           ps                    0ps                     50ps           100ps
                                                                Time




[Meghelli (IBM) ISSCC 2006]
                                                                                                                19
                                        Receiver Architecture
                           From on-chip PLL (5GHz)
                                C2-I            C2-Q                                       VDDIO=1V
            Vcm                                           I-Clock control                        2    1
                                  Phase rotator                                                           D0
                                                                              CDR




                                                                                                               (2.5Gb/s)
                    50Ω                                                                          2    1
                                       PI      PI                             logic                       D1
                                                         Q-Clock control                    8    2    1
                                                                                                          D2
In_P                               I            Q
                                                                                                 2    1
In_N T-Coil Compensation                                                                                  D3
                                             Phase     Edge
                                                               2:8           8:16
            Network                         detector
 (10Gb/s)




                                                              DMUX           DMUX        Data
                                                                                         Amp
                                                       Data                              Edge
                                             DFE       Amp                               Clock
                          VGA                Block            Tap weights     DFE
                                                                              logic
                  ESD
                                                                            CML          Key Features:
            VDDA=1.2V                           VDD=1.0V                    CMOS logic
                                                                                         - Half-rate design
                                                                                         - 5-tap continuously adaptive DFE
                                                                                         - Variable gain amplifier
                                                                                         - Digital CDR
                                                                                         - ESD protection (HBM & CDM)
                                                                                         - 130mW (with DFE and CDR logic)

 [Meghelli (IBM) ISSCC 2006]
                                                                                                                           20
                                       DFE Approach
                (+H1)
                               I       I       I
                                                       Deven
            Σ           I          L       L       L

                (-H1)                                   Tap
                        I                                                           DFE Taps     Resolution
  Data                             Tap-feedback        weights      On-chip
                    H1-5           and weighting                                    H1             6 bits
                                                                     DFE
                (+H1)                                                               H2             5 bits
                                                                     Logic
                                                       Dodd                         H3, H4, H5     4 bits
            Σ           I          L       L       L
                               I       I       I
                (-H1)
                        I

                            Amplitude
            Σ
                    I                                            Key Features:
             Offset                                              - Half-rate DFE with H1 speculation and
                                                                 dynamic H2-H5 feedback allows 2UI for
         Received eye
                                                                 settling
                               ISI
                                                                 - DFE algorithm maximizes vertical eye
                                                                 opening at the data slicing instant
                                                                 - Offset adjustment at all the slicer inputs
[Meghelli (IBM) ISSCC 2006]
                                                                                                              21
                                     CDR Loop
              Data Clock
                                                                             I Rotator
                 D          D          Early                                 Control
           Z-1                                                                        D/A                 PI




                                                                                                                                    From on-chip PLL
 Data                                                                 Digital
                     DMUX       XORs                                          Q Rotator
                                                                      Filter                                               C2-I
                 E          E          Late                                   Control
           Z-1                                                                        D/A                 PI
                                                                                                                           C2-Q
              Edge Clock

                                                                                         Jitter Tolerance
                                                                      Receiver Jitter tolerance curve ( BER<1e-9)
                                                                1.4



    Key Features:                                               1.2

                                                                 1
    - Fully digital loop
                                          Sine Jitter (UI pp)




                                                                                         Tracking bandwidth ~9MHz
                                                                0.8
    - Can handle up to +/- 4000ppm
                                                                0.6
    frequency offset
                                                                0.4
    - Independent I,Q control
                                                                0.2

                                                                 0
                                                                1.00E+05      1.00E+06         1.00E+07         1.00E+08     1.00E+09
                                                                                         Modulation Frequency



[Meghelli (IBM) ISSCC 2006]
                                                                                                                                                       22
              Chip-to-Chip Link Experiments


               Trace
     SerDes1                             Trace      5GHz losses          Number of vias
                                         Length     (Tx module + board   3.8mm via stub /
                       SerDes2                      trace + Rx module)   1.8mm via stub /
                                                                         1.8mm via through
                                         10” (#1)   12dB                 2/0/0
                                         10” (#2)   10dB                 0/2/0
                                         15”        25dB                 4/2/0
     SerDes1               SerDes2
                                         20”        15dB                 0/0/2
    Module                    Module


                                 Board

   Via stub        Trace




[Meghelli (IBM) ISSCC 2006]
                                                                                             23
                                            Chip-to-Chip Measurement Results
                                                                                                                      Trace              5GHz losses          Number of vias
                                                                                                                      Length
                                                                                                                                         (Tx module + board   3.8mm via stub /
                                                                                                                                         trace + Rx module)   1.8mm via stub /
                                                                                                                                                              1.8mm via through

                        Horizontal eye opening of the equalized 10” (#1)                                                                 12dB                 2/0/0
Horizontal Eye Opening (1e-9 BER)




                             eye at the receiver slicer input   10” (#2)                                                                 10dB                 0/2/0
                    60.00%                                      15”                                                                      25dB                 4/2/0
                                                                                                                      20”                15dB                 0/0/2

                    50.00%

                    40.00%
                                                                     DFE ONLY




                                                                                                                   DFE ONLY
                                                                                                                                         DFE+FFE
                                                                                                                                         DFE
                    30.00%
                                                                                                                                         FFE
                                                                                FFE ONLY




                                                                                                                              FFE ONLY
                    20.00%
                                                                                           DFE + FFE




                                                                                                       DFE + FFE
                                             DFE + FFE




                                                         DFE + FFE




                    10.00%

                                    0.00%
                            10" (#2)    15" 10" (#1)                                                               20"
       [Meghelli (IBM) ISSCC 2006] Link
                                                                                                                                                                               24
Preliminary Schedule




• Dates may change with reasonable notice
                                            25
Next Time
• Channels
  • Components
    • Chip packages, PCBs, Wires, Connectors
  • Modeling
    • Wires, Transmission Lines




                                               26
