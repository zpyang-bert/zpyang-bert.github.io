---
layout: post
title:      "lecture15 ee720 optical io"
date:       2026-04-21 10:45:30
author:     "Bert"
tags:
  - Fundamentals
  - Lecture
  - Optical
  - SerDes
  - 深度学习
---

ECEN720: High-Speed Links
   Circuits and Systems
       Spring 2023

    Lecture 15: Optical I/O




           Sam Palermo
   Analog & Mixed-Signal Center
       Texas A&M University
Announcements
• Exam 2 Apr 25
  • Focuses on material from Lectures 7-14
  • Previous years’ Exam 2s are posted on the website for
    reference

• Project Final Report due May 2
• Project Presentations May 4 (12:30PM-2:30PM)




                                                            2
Optical Interconnects
• Electrical Channel Issues
• Optical Channel
• Optical Transmitter Technology
• Optical Receiver Technology
• Optical Integration Approaches




                                   3
High-Speed Electrical Link System




                                    4
Channel Performance Impact




                             5
Link with Equalization




                         Deserializer
   Serializer




                                        6
Channel Performance Impact




                             7
High-Speed Optical Link System




• Optical interconnects remove many               Optical Channel

  channel limitations
  • Reduced complexity and power
    consumption
  • Potential for high information density with
    wavelength-division multiplexing (WDM)
                                                              8
Wavelength-Division Multiplexing




                                          [Young JSSC 2010]

• WDM allows for multiple high-bandwidth (10+Gb/s)
  signals to be packed onto one optical channel

                                                          9
Optical Interconnects
• Electrical Channel Issues
• Optical Channel
• Optical Transmitter Technology
• Optical Receiver Technology
• Optical Integration Approaches




                                   10
Optical Channels
• Short distance optical I/O channels are
  typically either waveguide (fiber)-based or
  free-space
• Optical channel advantages
  • Much lower loss
  • Lower cross-talk
  • Smaller waveguides relative to electrical traces
  • Potential for multiple data channels on single
    fiber via WDM

                                                       11
Waveguide (Fiber)-Based Optical Links
• Optical fiber loss is specified            Optical Fiber Cross-Section
  in dB/km
   • Single-Mode Fiber loss
     ~0.25dB/km at 1550nm
   • RF coaxial cable loss ~100dB/km
     at 10GHz
                                          Single-Mode Fiber Loss & Dispersion
• Frequency dependent loss is
  very small
   • <0.5dB/km over a bandwidth
     >10THz
• Bandwidth may be limited by
  dispersion (pulse-spreading)
   • Important to limit laser linewidth
     for long distances (>1km)
                                                                 [Sackinger]
                                                                           12
Inter-Chip Waveguide Examples
    12-Channel Ribbon Fiber

                                  Optical Polymer Waveguide in PCB




                                        [Immonen 2009]
        [Reflex Photonics]
  12 channels at a 250m pitch     <100m channel pitch possible
  10Gb/s mod.  40Gb/s/mm          10Gb/s mod.  100+Gb/s/mm

• Typical differential electrical strip lines are at ~500m pitch

                                                                   13
Free-Space Optical Links
                                        [Gruber]




• Free-space (air or glass) interconnect systems
  have also been proposed
• Optical imaging system routes light chip-to-chip

                                                     14
CMOS Waveguides – Bulk CMOS
• Waveguides can be made in a bulk process with a
  polysilicon core surrounded by an SiO2 cladding
• However, thin STI layer means a significant portion of the
  optical mode will leak into the Si substrate, causing
  significant loss (1000dB/cm)
• Significant post-processing is required for reasonable loss
  (10dB/cm) waveguides in a bulk process




                      [Holzwarth CLEO 2008]
                                                                15
CMOS Waveguides – SOI
• SOI processes have thicker buried oxide layers to
  sufficiently confine the optical mode
• Allows for low-loss waveguides




                 [Narasimha JSSC 2007]
                                                      16
CMOS Waveguides – Back-End Processing

• Waveguides & optical
                               [Young JSSC 2010]
  devices can be fabricated
  above metallization
• Reduces active area
  consumption
• Allows for independent
  optimization of transistor
  and optical device
  processes


                                                   17
Optical Interconnects
• Electrical Channel Issues
• Optical Channel
• Optical Transmitter Technology
• Optical Receiver Technology
• Optical Integration Approaches




                                   18
Optical Modulation Techniques
• Due to it’s narrow frequency (wavelength) spectrum, a
  single-longitudinal mode (SLM) laser source often
  generates the optical power that is modulated for data
  communication
   • This is required for long-haul (multi-km) communication
   • May not be necessary for short distance (~100m) chip-to-chip I/Os
• Two modulation techniques
   • Direct modulation of laser
   • External modulation of continuous-wave (CW) “DC” laser with
     absorptive or refractive modulators




                                                                         19
Directly Modulated Laser




• Directly modulating laser output power
• Simplest approach
• Introduces laser “chirp”, which is unwanted frequency
  (wavelength) modulation
• This chirp causes unwanted pulse dispersion when passed
  through a long fiber
                                                            20
Externally Modulated Laser




• External modulation of continuous-wave (CW)
  “DC” laser with absorptive or refractive modulators
  • Adds an extra component
  • Doesn’t add chirp, and allows for a transform limited
    spectrum
                                                            21
Optical Sources for Chip-to-Chip Links
• Vertical-Cavity Surface-Emitting Laser
  (VCSEL)

• Mach-Zehnder Modulator (MZM)

• Electro-Absorption Modulator (EAM)

• Ring-Resonator Modulator (RRM)

                                           22
Vertical-Cavity Surface-Emitting Laser (VCSEL)
     VCSEL Cross-Section                  VCSEL L-I-V Curves




                                                             



• VCSEL emits light perpendicular
  from top (or bottom) surface                    ITH = 700A
                                                 = 0.37mW/mA
• Important to always operate
  VCSEL above threshold current,
  ITH, to prevent “turn-on delay”              Po   I  I TH 
  which results in ISI                                           P  W 
                                       Slope Efficiency            
• Operate at finite extinction ratio                             I  A 
  (P1/P0)
                                                                            23
VCSEL Bandwidth vs Reliability
 10Gb/s VCSEL Frequency Response [1]
                                                                  • Mean Time to Failure (MTTF) is
                                                                    inversely proportional to current
                                                                    density squared

                                                                                                    E A   1 1 
                                                                                                         
                                                                                    A               k   T j 373 
                                                                             MTTF  2 e                                      [2]
                                                                                    j

                                                                  • Steep trade-off between
                                                                    bandwidth and reliability
                                                                                                   1
                                                                                  MTTF 
                                                                                                  BW 4
              BW  I avg  I TH

1.   D. Bossert et al, "Production of high-speed oxide confined VCSEL arrays for datacom applications," Proceedings of SPIE, 2002.
2.   M. Teitelbaum and K. Goossen, "Reliability of Direct Mesa Flip-Chip Bonded VCSEL’s," LEOS, 2004.                            24
VCSEL Drivers
 Current-Mode VCSEL Driver           VCSEL Driver w/ 4-tap
                                     FIR Equalization




• Current-mode drivers often
  used due to linear L-I
  relationship
• Equalization can be added
  to extend VCSEL              S. Palermo and M. Horowitz, “High-Speed Transmitters in 90nm
                               CMOS for High-Density Optical Interconnects," ESSCIRC, 2006.
  bandwidth for a given
  current density
                                                                                          25
Electro-Absorption Modulator (EAM)
         QWAFEM Modulator*




  *N. Helman et al, “Misalignment-Tolerant Surface-Normal Low-Voltage Modulator for Optical Interconnects," JSTQE, 2005.

• Absorption edge shifts with changing bias voltage
  due to the “quantum-confined Stark or Franz-                                            Waveguide EAM [Liu]
  Keldysh effect” & modulation occurs
• Modulators can be surface-normal devices or
  waveguide-based
• Maximizing voltage swing allows for good contrast
  ratio over a wide wavelength range
• Devices are relatively small and can be treated as
  lump-capacitance loads
    •   10 – 500fF depending on device type
                                                                                                                           26
Ring-Resonator Modulator (RRM)




• Refractive devices which modulate by
  changing the interference light coupled into
  the ring with the waveguide light
• Devices are relatively small (ring diameters
  < 20m) and can be treated as lumped
  capacitance loads (~10fF)
• Devices can be used in WDM systems to
  selectively modulate an individual            Optical Device Performance from: I. Young, E.
  wavelength or as a “drop” filter at receivers Mohammed,    J. Liao, A. Kern, S. Palermo, B. Block,
                                                M. Reshotko, and P. Chang, “Optical I/O Technology
                                                              for Tera-Scale Computing," ISSCC, 2009.
                                                                                                        27
Wavelength Division Multiplexing
w/ Ring Resonators




                                                              [Rabus]




• Ring resonators can act as both modulators and add/drop filters to
  steer light to receivers or switch light to different waveguides
• Potential to pack >100 waveguides, each modulated at more than
  10Gb/s on a single on-chip waveguide with width <1m (pitch ~4m)
                                                                       28
Ring-Resonator-Based
Silicon Photonics Transceiver




                        [Li ISSCC 2013]

• High-voltage drivers with simple pre-emphasis to extend
  bandwidth of silicon ring-resonator modulators
• Forwarded-clock receiver with adaptive power-sensitivity RX
• Bias-based tuning loop to stabilize photonic device’s
  resonance wavelength
                                                           29
CMOS Modulator Driver
• Simple CMOS-style
  voltage-mode drivers can
  drive EAM and RRM due to
  their small size
                                           Pulsed-Cascode Driver
• Device may require swing
  higher than nominal CMOS
  supply
  • Pulsed-Cascode driver can
    reliably provide swing of
    2xVdd (or 4xVdd) at up to
    2FO4 data rate


                                S. Palermo and M. Horowitz, “High-Speed Transmitters in 90nm
                                CMOS for High-Density Optical Interconnects," ESSCIRC, 2006. 30
Mach-Zehnder Modulator (MZM)
                                                                 [Analui]




• Refractive modulator which splits incoming light into two paths,
  induces a voltage-controlled phase shift in the two paths, and
  recombines the light in or out of phase
• Long device (several mm) requires driver to drive low-impedance
  transmission line at potentially high swing (5Vppd)
• While much higher power relative to RRM, they are less sensitive to
  temperature variations
                                                                        31
Optical Interconnects
• Electrical Channel Issues
• Optical Channel
• Optical Transmitter Technology
• Optical Receiver Technology
• Optical Integration Approaches




                                   32
Optical Receiver Technology
• Photodetectors convert optical
  power into current
   • p-i-n photodiodes
   • Integrated metal-semiconductor-
     metal photodetector


• Electrical amplifiers then
  convert the photocurrent into a
  voltage signal
   • Transimpedance amplifiers
   • Limiting amplifiers
   • Integrating optical receiver


                                       33
p-i-n Photodiode
                                         Responsivity:
[Sackinger]
                                            pd q
                                                    8  10 5  pd  
                                     I
                                                                        mA/mW 
                                    Popt     hc

                            Quantum Efficiency:                     pd  1  e W


                             Transit-Time Limited Bandwidth:
                                                        2.4     0.45vsat
                                           f 3dBPD           
                                                       2 tr     W




• Normally incident light absorbed in intrinsic
  region and generates carriers
• Trade-off between capacitance and transit-time
• Typical capacitance between 100-300fF
                                                                                      34
 Integrated Ge MSM Photodetector
                                                                     XSEM                        SiO2
          Cu                           Cu
                                                                                               0.75 um                 Cu
                            Ge


                                     SiN waveguide                                     Ge
                Cu
                          2 um                                                                                         Silicon
                                                                                              SiO2
                                                                                                                       nitride

                                                                           Very low capacitance: <1 fF
                      Detector                                               Active area: < 2 um2
• Lateral Metal-Semiconductor-Metal (MSM Detector)
• Silicon Nitride Waveguide-Coupled
• Direct Germanium deposition on oxide
I. Young, E. Mohammed, J. Liao, A. Kern, S. Palermo, B. Block, M. Reshotko, and P. Chang, “Optical I/O Technology for Tera-
Scale Computing," IEEE Journal of Solid-State Circuits, 2010.                                                                    35
Optical Interconnects
• Electrical Channel Issues
• Optical Channel
• Optical Transmitter Technology
• Optical Receiver Technology
• Optical Integration Approaches




                                   36
Optical Integration Approaches
• Efficient cost-effective optical integration
  approaches are necessary for optical
  interconnects to realize their potential for
  improved power efficiency at higher data rates

• Hybrid integration
  • Optical devices fabricated on a separate substrate


• Integrated CMOS photonics
  • Optical devices part of CMOS chip


                                                         37
Hybrid Integration
 [Kromer]        [Schow]              [Mohammed]




Wirebonding   Flip-Chip Bonding

                                  Short In-Package Traces



                                                        38
Integrated CMOS Photonics
SOI CMOS Process
                    [Analui]
                               “Optics On Top”


                                Optical Layer


                                                 [Young]
Bulk CMOS Process




     [Batten]                                              39
 Future Photonic CMOS Chip




• Unified optical interconnect for on-chip core-to-core and off-
  chip processor-to-processor and processor-to-memory
I. Young, E. Mohammed, J. Liao, A. Kern, S. Palermo, B. Block, M. Reshotko, and P. Chang, “Optical I/O Technology for Tera-
Scale Computing," IEEE International Solid-State Circuits Conference, 2009.                                                   40
Conclusion
• Thanks for the fun semester!




                                 41
