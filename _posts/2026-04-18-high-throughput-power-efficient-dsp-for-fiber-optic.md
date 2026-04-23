---
layout: post
title:      "High-throughput power-efficient DSP for fiber-optic communication systems"
date:       2026-04-18 11:47:26
author:     "Bert"
tags:
  - DSP
  - Mineru
---

Thesis for the Degree of Licentiate of Engineering

# High-throughput power-efficient DSP for fiber-optic communication systems

Christoffer Fougstedt

![](/img/mineru_output/High_Throughput_Power_Efficient_DSP_Fiber_Optic_Fougstedt_67p/auto/images/9e228520b5776b3e344ad798f020cc3f6e523491b81ea29b4b53616016cd1ec9.jpg)

CHALMERS

Department of Computer Science and Engineering Chalmers University of Technology G¨oteborg, Sweden, 2018

ProQuest Number: 27753234

All rights reserved

INFORMATION TO ALL USERS The quality of this reproduction is dependent on the quality of the copy submitted.

In the unlikely event that the author did not send a complete manuscript and there are missing pages, these will be noted. Also, if material had to be removed, a note will indicate the deletion.

![](/img/mineru_output/High_Throughput_Power_Efficient_DSP_Fiber_Optic_Fougstedt_67p/auto/images/ce33d26971baf751f05edcf3be445ffea89cf72733330f28e986b49e220b62f3.jpg)

ProQuest 27753234

Published by ProQuest LLC ( ). Copyright of the Dissertation is held by the Author. 2020

All Rights Reserved. This work is protected against unauthorized copying under Title 17, United States Code Microform Edition © ProQuest LLC.

ProQuest LLC

789 East Eisenhower Parkway

P.O. Box 1346

Ann Arbor, MI 48106 - 1346

High-throughput power-efficient DSP for fiber-optic   
communication systems   
Christoffer Fougstedt

Copyright 
c Christoffer Fougstedt, 2017

Technical report 173L ISSN 1652-876X

Department of Computer Science and Engineering

Chalmers University of Technology

SE–412 96 G¨oteborg

Sweden

Telephone: +46–(0)31–772 10 00

Printed by Reproservice

Chalmers Tekniska H¨ogskola

G¨oteborg, Sweden, 2017

High-throughput power-efficient DSP for fiber-optic   
communication systems Systems   
Christoffer Fougstedt   
Department of Computer Science and Engineering   
Chalmers University of Technology

## Abstract

Communication networks are a vital backbone of the modern society. Power dissipation of optical communication links and digital signal processing (DSP) subsystems for these links are a major concern as throughput requirements increase, and the number of deployed systems grows. We are approaching fundamental integrated-circuit scaling limits quickly, and it is thus no longer possible to assume that feature-size scaling will enable implementation of ever more complex algorithms. Therefore, approaching DSP from an implementation perspective, and designing low-power high-performance algorithms will become increasingly more important.

This thesis considers power- and energy-efficiency improvements in real-time implementation of DSP algorithms. High-throughput parallel implementations of algorithms are presented and improvements in currently-employed major power-dissipating DSP subsystems (chromatic dispersion compensation and dynamic equalization) are considered. Implementation-aware design of advanced algorithms for long-haul transmission systems is considered. This thesis also considers possible power-reduction in short-haul systems through introduction of forward error correction.

Keywords: Application Specific Integrated Circuits, Communication Systems, Digital Signal Processing, Fiber Optic Communication, Nonlinear Impairment Mitigation, Forward Error Correction

## Publications

This thesis is based on the work contained in the following papers:

[A] Christoffer Fougstedt, Alireza Sheikh, Pontus Johannisson, and Per Larsson-Edefors. “Filter Implementation for Power-Efficient Chromatic Dispersion Compensation”, Submitted to IEEE Trans. Circuits Syst. I, Reg. Papers,

[B] Christoffer Fougstedt, Pontus Johannisson, Lars Svensson, and Per Larsson-Edefors. “Dynamic Equalizer Power Dissipation Optimization”, Optical Fiber Communications Conference, OFC 2016,

[C] Christoffer Fougstedt, Mikael Mazur, Lars Svensson, Henrik Eliasson, Magnus Karlsson, and Per Larsson-Edefors. “Time-Domain Digital Back Propagation: Algorithm and Finite-Precision Implementation Aspects”, Optical Fiber Communications Conference, OFC 2017,

[D] Christoffer Fougstedt, Lars Svensson, Mikael Mazur, Magnus Karlsson, and Per Larsson-Edefors. “Finite-Precision Optimization of Time-Domain Digital Back Propagation by Inter-Symbol Interference Minimization”, Proceedings of 43rd European Conference and Exhibition on Optical Communications, ECOC 2017,

[E] Christoffer Fougstedt, Krzysztof Szczerba and Per Larsson-Edefors. “Low-Power Low-Latency BCH Decoders for Energy-Efficient Optical Interconnects”, Journal of Lightwave Technology, 35, 23, 5210–5207, Dec 2017.

Related work by the author (not included in this thesis):

[F] Christoffer Fougstedt, Alireza Sheikh, Pontus Johannisson, Alexandre Graell i Amat, and Per Larsson-Edefors. “Power-Efficient Time-Domain Dispersion Compensation Using Optimized FIR Filter Implementation”, Signal Processing in Photonics Communications, SPPCom 2015, SpT3D.3, Jul 2015.

[G] Alireza Sheikh, Christoffer Fougstedt, Alexandre Graell i Amat, Pontus Johannisson, Per Larsson-Edefors, and Magnus Karlsson. “Dispersion Compensation Filter Design Optimized for Robustness and Power Efficiency”, Signal Processing in Photonics Communications, SPPCom 2015, SpT3D.2, Jul 2015.

[H] Krzysztof Szczerba, Christoffer Fougstedt, Per Larsson-Edefors, Petter Westbergh, Alexandre Graell i Amat, Lars Svensson, Magnus Karlsson, Anders Larsson, and Peter Andrekson. “Impact of Forward Error Correction on Energy Consumption of VCSELbased Transmitters”, 41st European Conference on Optical Communication, ECOC 2015, Sep 2015.

[I] Alireza Sheikh, Christoffer Fougstedt, Alexandre Graell i Amat, Pontus Johannisson, Per Larsson-Edefors, and Magnus Karlsson. “Dispersion Compensation FIR Filter with Improved Robustness to Coefficient Quantization Error”, Journal of Lightwave Technology, 34, 22, 5110–5117, Aug 2016.

[J] Lars Lundberg, Christoffer Fougstedt, Per Larsson-Edefors, Peter Andrekson, and Magnus Karlsson. “Power Consumption of a Minimal-DSP Coherent Link with a Polarization Multiplexed Pilot-Tone”, 42nd European Conference on Optical Communication, ECOC 2016, Sep 2016.