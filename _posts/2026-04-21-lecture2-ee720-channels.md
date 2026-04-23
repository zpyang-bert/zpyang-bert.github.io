---
layout: post
title:      "lecture2 ee720 channels"
date:       2026-04-21 09:17:14
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

Lecture 2: Channel Components, Wires, & Transmission Lines




                       Sam Palermo
               Analog & Mixed-Signal Center
                   Texas A&M University
Announcements
• Homework 1 due today
• Lab
  • Prelab 1 due Jan 30
  • Lab 1 report and Prelab 2 due Feb 6
  • TA Tong Liu
     • liut@tamu.edu
     • Office Hours M 10AM-12PM, WEB 160

• Reference Material Posted on Website
  • TDR theory application note
  • S-parameter notes

                                           2
Agenda
• Channel Components
  • IC Packages, PCBs, connectors, vias, PCB Traces
• Wire Models
  • Resistance, capacitance, inductance
• Transmission Lines
  • Propagation constant
  • Characteristic impedance
  • Loss
  • Reflections
  • Termination examples
  • Differential transmission lines
                                                      3
Channel Components
                              Packaged SerDes

                  Backplane trace

            Line card trace

           Edge connector

           Via stub
                                                        [Meghelli (IBM) ISSCC 2006]


   Pkg         Line card       Line card      Edge    Backplane
                 trace            via       connector    via
   Tx IC                            The Channel                   Backplane
                                                                  16” trace

   Pkg         Line card       Line card      Edge    Backplane
                 trace            via       connector    via
   Rx IC

                                                                                  4
IC Packages
• Package style depends                     Package Type                Pin Count
                                   Small Outline Package (SOP)              8 – 56
  on application and pin
                                   Quad Flat Package (QFP)                 64 - 304
  count
                                   Plastic Ball Grid Array (PBGA)          256 - 420
                                   Enhanced Ball Grid Array (EBGA)         352 - 896
• Packaging technology             Flip Chip Ball Grid Array (FC-BGA)   1089 - 2116
  hasn’t been able to                   SOP                          QFP
  increase pin count at
  same rate as on-chip
  aggregate bandwidth
  • Leads to I/O constrained
    designs and higher data            PBGA                         FC-BGA
    rate per pin


      [Package Images - Fujitsu]
                                                                                       5
IC Package Examples
• Wirebonding is most          Standard Wirebond Package

  common die attach method
• Flip-chip packaging allows
  for more efficient heat      Flip-Chip/Wirebond Package
  removal
• 2D solder ball array on
  chip allows for more         Flip-Chip/Solder Ball Package
  signals and lower signal
  and supply impedance

                                [Package Images - Fujitsu]
                                                             6
IC Package Model

Bondwires             Package Trace
• L ~ 1nH/mm          • L ~ 0.7-1nH/mm
•Mutual L “K”         •Mutual L “K”
• Ccouple ~ 20fF/mm   • Clayer ~ 80-90fF/mm
                      •Ccouple ~ 40fF/mm




                                    [Dally]


                                              7
IC Package Model Comparisons

                     • FCB packaging allows
                       for much less chip
                       interface impedance

        [Intel]




                                              8
Printed Circuit Boards
• Components soldered on
  top (and bottom)

• Typical boards have 4-8
  signal layers and an
  equal number of power
  and ground planes

• Backplanes can have
  over 30 layers

                            9
PCB Stackup
• Signals typically on top and
  bottom layers

• GND/Power plane pairs and
  signal layer pairs alternate in
  board interior

• Typical copper trace thickness
   • “0.5oz” (17.5um) for signal layers   [Dally]
   • “1oz” (35um) for power planes




                                                    10
Connectors
• Connectors are used
  to transfer signals
  from board-to-board

• Typical differential
  pair density between
  16-32 pairs/10mm


                         [Tyco]
                                  11
Connectors
• Important to maintain proper differential
  impedance through connector
• Crosstalk can be an issue in the connectors




                                    [Tyco]      12
Vias
• Used to connect PCB layers

• Made by drilling a hole through
  the board which is plated with
  copper
   • Pads connect to signal layers/traces
   • Clearance holes avoid power planes

                                            [Dally]
• Expensive in terms of signal
  density and integrity
   • Consume multiple trace tracks
   • Typically lower impedance and create
     “stubs”

                                                  13
    Impact of Via Stubs at Connectors
         Packaged SerDes
   Backplane trace
Line card trace
Edge connector
  Via stub




   • Legacy BP has default straight vias
         • Creates severe nulls which kills signal integrity
   • Refined BP has expensive backdrilled vias                 14
PCB Trace Configurations
• Microstrips are signal
  traces on PCB outer
  surfaces
  • Trace is not enclosed
    and susceptible to
    cross-talk
• Striplines are
  sandwiched between
  two parallel ground
  planes                      [Johnson]
  • Has increased isolation

                                          15
Wire Models
• Resistance

• Capacitance

• Inductance

• Transmission line theory


                             16
Wire Resistance
• Wire resistance is determined by material
  resistivity, ρ, and geometry
• Causes signal loss and propagation delay




      l       l     l  l
 R                R   2
      A        wh      A r               [Dally]



                                               17
Wire Capacitance
• Wire capacitance is determined
  by dielectric permittivity, ε,
  and geometry
• Best to use lowest εr
  • Lower capacitance
  • Higher propagation velocity



                                                                  [Dally]


        w              2                            w    2
   C           C                 C               C      
         s           logr2 r1         logs r          s log4s h 
                                                                         18
Wire Inductance
• Wire inductance is determined by material
  permeability, µ, and closed-loop geometry

• For wire in homogeneous medium
                  CL  
• Generally      0  4 10 H/m
                            7




                                              19
Wire Models
• Model Types
  • Ideal
  • Lumped C, R, L
  • RC transmission line
  • LC transmission line
  • RLGC transmission line
                                                              R
• Condition for LC or RLGC model (vs RC)                f0 
                                                             2L
           Wire              R         L        C        >f (LC wire)
   AWG24 Twisted Pair      0.08Ω/m 400nH/m    40pF/m        32kHz
   PCB Trace                5Ω/m    300nH/m   100pF/m      2.7MHz
   On-Chip Min. Width M6
                           40kΩ/m   4µH/m     300pF/m      1.6GHz
   (0.18µm CMOS node)
                                                                        20
RLGC Transmission Line Model




As dx  0
             V  x, t                      I  x, t 
                           RI  x, t   L               (1)
                                                                 General
               x                               t
                                                                 Transmission
            I  x, t                     V x, t 
                         GV  x, t   C
                                                                 Line Equations
                                                           (2)
               x                            t
                                                                            21
Time-Harmonic Transmission Line Eqs.
• Assuming a traveling sinusoidal wave with angular frequency, ω
                         dV  x 
                                   R  jL I  x  (3)
                          dx
                        dI  x 
                                  G  jC V  x        (4)
                         dx
• Differentiating (3) and plugging in (4) (and vice versa)

                            d 2V  x 
                                   2
                                          2
                                             V x    (5)
                                                                  Time-Harmonic
                              dx
                                                                  Transmission
                            d 2 I x 
                                  2
                                         2
                                             I x    (6)
                                                                  Line Equations
                              dx
• where  is the propagation constant
                    j    R  jL G  jC  m -1 
                                                                                   22
Transmission Line Propagation Constant
• Solutions to the Time-Harmonic Line Equations:

                V  x   V f  x   Vr  x   V f 0 e x  Vr 0 ex

                 I  x   I f  x   I r  x   I f 0 e x  I r 0 ex

     where       j          R  jL G  jC  m -1 
• What does the propagation constant tell us?
   • Real part () determines attenuation/distance (Np/m)
   • Imaginary part () determines phase shift/distance (rad/m)
   • Signal phase velocity
                                    (m/s)

                                                                             23
Transmission Line Impedance, Z0
• For an infinitely long line, the voltage/current ratio is Z0
• From time-harmonic transmission line eqs. (3) and (4)


                        V x    R  j L
                   Z0                      
                        I x    G  j C


• Driving a line terminated by Z0 is the same as driving an
  infinitely long line




                                                        [Dally]
                                                                  24
Lossless LC Transmission Lines
• If Rdx=Gdx=0
         j  j LC
      0      No Loss!

       LC
• Waves propagate w/o distortion
   • Velocity and impedance
     independent of frequency
   • Impedance is purely real

                 1
              
                 LC
              L
         Z0                       [Johnson]
              C
                                           25
Low-Loss LRC Transmission Lines
                                            j     R  jL G  jC 
• If R/L and G/C << 1                                               1
                                                      RC  GL       2
                                         j LC 1  j         
                                                        LC   
• Behave similar to ideal                                       1  R 2 1  G 2 
                                           R      GZ 0
  LC transmission line,                 
                                          2Z 0
                                               
                                                    2
                                                        j LC 1  
                                                                 8   L
                                                                             
                                                                             8   C
                                                                                       
                                                                                       
  but …                                   R   D  j

  • Experience resistive and            R 
                                                R
                                                       Resistive Loss
                                               2Z 0
    dielectric loss
                                        D 
                                               GZ 0    Dielectric Loss
  • Frequency dependent                         2
    propagation velocity                          1  R 2 1  G 2 
                                           LC 1                
    results in dispersion                          8   L  8   C  

     • Fast step, followed by slow          1  R 2 1  G 2  
                                                                    1


       DC tail                        LC 1           
                                               8 L
                                                     8 C
                                                                
                                                                           
                                          


                                                                                        26
Frequency-Dependent Loss Mechanisms
• The resistive (R) and dielectric (D) loss terms
  cause a signal propagating down a transmission-
  line to become attenuated with distance


   V x       R   D  x
          e
   V 0 


• Resistive loss term is due to conductor skin effect
• Dielectric loss term is due to dielectric absorption
• Both terms increase with frequency, although at
  different rates                                      27
Skin Effect (Resistive Loss)
• High-frequency current density falls
  off exponentially from conductor
  surface
                                                                                   [Dally]
• Skin depth, , is where current falls                  d                             1
                                                     
                                                                        f   
  by e-1 relative to full conductor           J e                                    2



   • Decreases proportional to            For rectangular conductor:
     sqrt(frequency)                                             
                                                fs 
• Relevant at critical frequency fs                      h
                                                        
                                                                       2



  where skin depth equals half                           2         1
                                                               f 2
  conductor height (or radius)                  R f   RDC  
                                                               fs 
   • Above fs resistance/loss increases                                        1

     proportional to sqrt(frequency)           R 
                                                             RDC  f 
                                                                     
                                                                               2

                                                             2 Z 0  f s 


                                                                                           28
    Skin Effect (Resistive Loss)

  5-mil Stripguide
RDC  7  m, f s  43MHz

  30 AWG Pair
RDC  0.08  m, f s  67kHz




                           1
            RDC  f       2
     R          
            2Z 0  f s 




                                   [Dally]

                                             29
Dielectric Absorption (Loss)
• An alternating electric field                    G
                                        tan  D 
  causes dielectric atoms to                      C
  rotate and absorb signal
  energy in the form of heat
• Dielectric loss is expressed
  in terms of the loss
                                                       [Dally]
  tangent
                                       GZ 0 2fC tan  D L C
• Loss increases directly         D      
                                        2             2
  proportional to frequency
                                         f tan  D LC


                                                            30
Total Wire Loss




                  [Dally]




                            31
Advanced Board Dielectrics
                                                     [Samtec]




                                                     ~1.1dB/in
                                                     @ 56GHz
                                                     ~1.6dB/in
                                                     @ 56GHz
                                                     ~2dB/in
                                                     @ 56GHz




                                             50GHz
•   Megtron 6 25dB loss is 12.5”
•   Tachyon 25dB loss is 15.6”
•   PTFE (Teflon) 25dB loss is 22.7”
•   Cabled interconnects can support ~1.5m                32
Cabled Backplane
                                [Ghiasi IEEE802.3 2017]




• Cabled backplane with short daughter cards can
  support ~1m distances at 224Gb/s
                                                      33
Reflections & Telegrapher’s Eq.


                                                                [Dally]
• With a Thevenin-equivalent model of the line:
                                                   2Vi
                     Termination Current: I T 
                                                Z 0  ZT
• KCL at Termination:
              Vi                            Telegrapher’s Equation or
       If       , I r  I f  IT
              Z0                            Reflection Coefficient

              Vi    2Vi                         I r Vr ZT  Z 0
       Ir       
              Z 0 ZT  Z 0                  kr   
                                                I f Vi ZT  Z 0
              Vi  ZT  Z 0 
       Ir                 
              Z 0  ZT  Z 0 
                                                                          34
Termination Examples - Ideal
                              RS = 50
                              Z0 = 50, td = 1ns
                              RT = 50



                                 in (step begins at 1ns)



          50                    source
 Vi  1V            0.5V
          50  50 
        50  50                          termination
 k rT           0
        50  50
        50  50
 k rS          0
        50  50
                                                           35
Termination Examples - Open
                              RS = 50
                              Z0 = 50, td = 1ns
                              RT ~ ∞ (1M)



                                 in (step begins at 1ns)

                                         termination

          50                                source
 Vi  1V            0.5V
          50  50 
          50
 k rT           1
          50
        50  50
 k rS          0
        50  50
                                                           36
Termination Examples - Short
                              RS = 50
                              Z0 = 50, td = 1ns
                              RT = 0



                                 in (step begins at 1ns)



          50 
 Vi  1V            0.5V      source
          50  50 
        0  50
 k rT          1
        0  50
                                 termination
        50  50
 k rS          0
        50  50
                                                           37
Arbitrary Termination Example
                                RS = 400
                                Z0 = 50, td = 1ns
                                RT = 600



                                   in (step begins at 1ns)



         50 
Vi  1V             0.111V
         400  50                           termination 0.340
       600  50                             source 0.278V
k rT            0.846                      0.205V
       600  50                    0.111V

       400  50
k rS            0.778
       400  50
                                                              38
Lattice Diagram
                  RS = 400
                  Z0 = 50, td = 1ns
                  RT = 600



                     in (step begins at 1ns)

                    Rings up to 0.6V
                  (DC voltage division)




                                               39
Termination Reflection Patterns
                         RS = 25, RT = 25
                         krS & krT < 0
                         Voltages Converge
                                                          termination
 source

                                                 source

                         RS = 25, RT = 100
     termination
                         krS < 0 & krT > 0
                         Voltages Oscillate

                         RS = 100, RT = 25
                         krS > 0 & krT < 0
                         Voltages Oscillate


                                                termination
  source                 RS = 100, RT = 100
           termination                              source
                         krS > 0 & krT > 0
                         Voltages Ring Up
                                                                        40
Termination Schemes
• No Termination
  • Little to absorb line energy
  • Can generate oscillating
    waveform
  • Line must be very short              t r  nTround trip  2nl LC
    relative to signal transition time
     • n=4-6
  • Limited off-chip use
                                         t porch  2l LC
• Source Termination
  • Source output takes 2 steps up
  • Used in moderate speed point-
    to-point connections


                                                                        41
Termination Schemes
• Receiver Termination
  • No reflection from receiver
  • Watch out for intermediate
    impedance discontinuities
     • Little to absorb reflections at driver


• Double Termination
  • Best configuration for min
    reflections
     • Reflections absorbed at both driver
       and receiver
  • Get half the swing relative to
    single termination
  • Most common termination scheme
    for high performance serial links
                                                42
Differential Signaling
• Differential signaling advantages
  • Self-referenced
  • Common-mode noise rejection
  • Increased signal swing
  • Reduced self-induced power-supply noise

• Requires 2x the number of signaling pins
  relative to single-ended signaling
  • But, smaller ratio of supply/signal (return) pins
  • Total pin overhead is typically 1.3-1.8x (vs 2x)
                                                        43
Odd & Even Modes
                                                                 [Hall]




• Even mode
    •   When equal voltages drive both lines, only one mode propagates called even more
• Odd mode
    •   When equal in magnitude, but out of phase, voltages drive both lines, only one
        mode propagates called odd mode
• For a differential pair (odd mode), a virtual reference plane exists between
  the conductors that provides a continuous return current path
    •   Electric field is perpendicular to the virtual plane
    •   Magnetic field is tangent to the virtual plane

                                                                                         44
Balanced Transmission Lines
                                                                 [Dally]
• Even (common) mode
  excitation
  • Effective C = CC
  • Effective L = L + M
• Odd (differential) mode
  excitation                                             1
                                                  LM  2
                                        Z even      
  • Effective C = CC + 2Cd                         Cc 
  • Effective L = L – M                           LM  2
                                                             1

                                        Z odd            
                               Z even             Cc  2Cd 
   Z DIFF  2 Z odd ,   Z CM 
                                 2
                                                                     45
PI-Termination


                          Z even  R1




                 Z odd  R1 || R2 2  Z even || R2 2

                              Z odd Z even 
                      R2  2                
                              Z even  Z odd 


                                                   46
T-Termination


                  Z even  R2  2R1




                     Z odd  R2
                    1
                R1  Z even  Z odd 
                    2



                                      47
Next Time
• Channel modeling
  • Time domain reflectometer (TDR)
  • Network analysis




                                      48
