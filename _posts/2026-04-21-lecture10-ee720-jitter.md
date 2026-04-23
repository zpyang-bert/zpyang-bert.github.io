---
layout: post
title:      "lecture10 ee720 jitter"
date:       2026-04-21 10:10:42
author:     "Bert"
tags:
  - Fundamentals
  - Jitter
  - Lecture
  - SerDes
  - 深度学习
---

ECEN720: High-Speed Links
   Circuits and Systems
       Spring 2023

       Lecture 10: Jitter




           Sam Palermo
   Analog & Mixed-Signal Center
       Texas A&M University
Announcements
• Lab 6 Report due Apr 3

• Reference Material
  • Jitter application notes posted on website
  • Majority of today’s material from Hall reference




                                                       2
Agenda
• Jitter Definitions
• Jitter Categories
• Dual Dirac Jitter Model
• System Jitter Budgeting




                            3
 Eye Diagram and Spec Mask
• Links must have margin in both the voltage AND
  timing domain for proper operation
• For independent design (interoperability) of TX
  and RX, a spec eye mask is used
Eye at RX
sampler




RX clock timing noise             [Hall]
or jitter (random noise
only here)
                                                    4
Jitter Definitions
• Jitter can be defined as “the short-term variation
  of a signal with respect to its ideal position in time”
• Jitter measurements
  • Period Jitter (JPER)
     • Time difference between measured period and ideal period
  • Cycle to Cycle Jitter (JCC)
     • Time difference between two adjacent clock periods
     • Important for budgeting on-chip digital circuits cycle time
  • Accumulated Jitter (JAC)
     • Time difference between measured clock and ideal trigger clock
     • Jitter measurement most relative to high-speed link systems


                                                                        5
Jitter Statistical Parameters
• Mean Value
  • Can be interpreted as a fixed timing offset or “skew”
  • Generally not important, as usually can corrected for
• RMS Jitter
  • Useful for characterizing random component of jitter
• Peak-to-Peak Jitter
  • Function of both deterministic (bounded) and random
    (unbounded) jitter components
  • Must be quoted at a given BER to account for random
    (unbounded) jitter


                                                            6
Jitter Calculation Examples




    n       1        2        3        4      Mean      RMS       PP
   JPER    -0.06    0.02     -0.06    0.12     0.005    0.085    0.18
   JCC     0.08     -0.08    0.18       -      0.06     0.131    0.26
   JAC     -0.07    -0.05    -0.11    0.01    -0.055    0.05     0.12

 JPER = time difference between measured period and ideal period
 JCC = time difference between two adjacent clock periods
 JAC = time difference between measured clock and ideal trigger clock
                                                                        7
Jitter Histogram
                                   Threshold (Zero)
                                    Crossing Time
 High and Low Signal Voltage         Distribution
    Distribution at Time t




                                                            [Hall]

                               0           t          UI
• Used to extract the jitter PDF
• Consists of both deterministic and random components
   • Need to decompose these components to accurately estimate
     jitter at a given BER                                           8
Jitter Categories




                    9
Random Jitter (RJ)
• Unbounded and modeled with a gaussian distribution
   • Assumed to have zero mean value
   • Characterized by the rms value, RJ
   • Peak-to-peak value must be quoted at a given BER
• Originates from device noise
   • Thermal, shot, flicker noise
                                                    t 2
                                         1
                           RJ t  
                                                      2
                                                 e 2 RJ
                                       2  RJ




                                                           10
Deterministic Jitter (DJ)
• Bounded with a peak-to-peak value that can be predicted
• Caused by transmission-line losses, duty-cycle distortion, spread-
  spectrum clocking, crosstalk
• Categories
   • Sinusoidal Jitter (SJ or PJ)
   • Data Dependent Jitter (DDJ)
       • Intersymbol Interference (ISI)
       • Duty Cycle Distortion (DCD)
       • Bounded Uncoirrelated Jitter (BUJ)




                                                                       11
Sinusoidal or Periodic Jitter (SJ or PJ)
• Repeats at a fixed frequency due to modulating effects
   • Spread spectrum clocking
   • PLL reference clock feedthrough
• Can be decomposed into a Fourier series of sinusoids
                          SJ t    Ai cosi t   i 
                                    i


• The jitter produced by an individual sinusoid is
                                        1
                                                     A t
                       PDFSJ t     A2  t 2
                                        0            A t
                                    




                                                             12
Data Dependent Jitter (DDJ)
• Data dependent jitter is correlated with
  either the transmitted data pattern or
  aggressor (crosstalk) data patterns
• Caused by phenomena such as phase
  errors in serialization clocks, channel
  filtering, and crosstalk
• Categories
  • Duty Cycle Distortion (DCD)
  • Intersymbol Interference (ISI)
  • Bounded Uncorrelated Jitter (BUJ)
                                             13
Duty Cycle Distortion (DCD)
• Caused by duty cycle errors in TX serialization
  clocks and rise/fall delay mismatches in post-
  serialization buffers
• Resultant PDF from a peak-to-peak duty cycle
  distortion (DCD) is the sum of two delta functions
                             1    DCD    DCD 
             PDFDCD t        t       t    
                             2       2          2 




                                                            14
Intersymbol Interference (ISI)
• Caused by channel loss, dispersion, and reflections
• Equalization can improve ISI jitter


                                            No Equalization




                                            2-tap
                                            TX Equalization




                                                        15
Bounded Uncorrelated Jitter (BUJ)
• Not aligned in time with the data stream
• Most common source is crosstalk
• Classified as uncorrelated due to being
  correlated to the aggressor signals and not
  the victim signal or data stream
• While uncorrelated, still a bounded source
  with a quantifiable peak-to-peak value


                                                16
Total Jitter (TJ)
• The total jitter PDF is produced by
  convolving the random and deterministic
  jitter PDFs
                 PDFJT t   PDFRJ t * PDFDJ t 
 where PDFDJ t   PDFSJ t * PDFDCD t * PDFISI t * PDFBUJ t 




                                                                        17
Jitter and Bit Error Rate
• Jitter consists of both
  deterministic and random
  components

• Total jitter must be quoted at
  a given BER
   • At BER=10-12, jitter ~1675ps
     and eye width margin ~200ps
   • System can potentially achieve
     BER=10-18 before being jitter
     limited




                                      18
     Dual Dirac Jitter Model
   • For system-level jitter budgets, the dual Dirac model
     approximates the complex total jitter PDF and allows for the
     budgeting of deterministic and random jitter components

                                                     t 2
                                          1
                         RJ t  
                                                       2
                                                  e 2 RJ
                                       2  RJ




                        t  DJ  / 2   t  DJ  / 2 
           DJ t                            
                                 2                          2




                                1         t  2DJ 2 / 2    
                                                                  t  DJ  / 2
                                                                                
JT t   RJ t * DJ t  
                                                                         2
                                                                      2 RJ
                                        e           RJ
                                                             e                 
                             2 2  RJ                                        

                                                                                     19
Dual Dirac Jitter Model
• Jitter at a given BER is computed considering
  both leading and trailing edges




                                                                                                               Dominant Terms
                                                                     t
                    t  DJ  / 2         t  DJ  / 2                          UI  t  DJ  / 2          UI  t  DJ  / 2 
                  
BERlead t  0.5erfc               
                                    
                                            
                                       erfc               
                                                                                    
                                                               , BERtrail t  0.5erfc                    
                                                                                                              erfc                    
                                                                                                                                          
                       2 RJ                 2 RJ                                   2 RJ                       2 RJ       
                                                                              
                                                                          2
                                                      where erfct           e dx
                                                                                  2
                                                                                 x

                                                                           t
                                                                                                                                                20
 Dual Dirac Jitter Model Example
• Plot measured jitter
  PDF vs Q-scale
                               BER 
       QBER BER   2erf 1 1       
                                    T 

where  T is the transition density, typically 0.5


• Tails are used to
  extract RJ
• Extrapolate to Q(0) to
  extract separation of
                                                     DJ   Extracted seperation of dual - Dirac delta functions
  dual-Dirac delta
                                                     DJ pp  Actual deterministic jitter peak - to - peak value
  functions
                                                                                                                  21
Dual Dirac Jitter Model Example




                                    1         t  2DJ 2 / 2    
                                                                      t  DJ  / 2
                                                                             2
                                                                          2 RJ
                                                                                    
             Dual - Dirac PDF             e           RJ
                                                                 e                 
                                 2 2  RJ                                        




• Extracted dual Dirac model matches well with
  measured jitter PDF
                                                                                         22
System Jitter Budget
• For a system to achieve a minimum BER performance
               UI  DJ  sys   QBER RMS sys 

• The convolution of the individual deterministic jitter
  components is approximated by linear addition of the terms
                    DJ  sys    DJ  i 
                                    i

• The convolution of the individual random jitter components
  results in a root-sum-of-squares system rms value

                    RMS sys      RMS i 
                                      2

                                        i



                                                           23
Jitter Budget Example – PCI Express System

                 Architecture




                 Jitter Model




                            [Hall]


                                             24
Jitter Budget Example – PCI Express System
     DJ  sys   DJ  TX   DJ  channel   DJ  RX   DJ  clock 

     RMS sys    RMS
                     2
                         TX    RMS
                                   2
                                       channel    RMS
                                                      2
                                                          RX    RMS
                                                                    2
                                                                        clock 




                                                                                160

                       6.15 * 14.069 =
                                                                                    [Hall]




                                                                                             25
Next Time
• Clocking Architectures




                           26
