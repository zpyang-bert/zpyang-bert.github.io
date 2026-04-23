---
layout: post
title:      "First Dual-Band Hybrid Window Antiresonant HCF with 0.13 dB/km loss at 1 µm and 0.11 dB/km at 1.55 µm"
date:       2026-04-18 12:50:00
author:     "Bert"
tags:
  - Mineru
---
Ghafour Amouzad Mahdiraji, 1 Seyed Mohammad Abokhamis Mousavi, 1 Dong Wu, 1 Thejus Varghese,1 Naveen Krishna Baddela, 2 Muhammad Rosdi B. Abu Hassan,1 Zahra Kakaei, 2 Abubakar Isa Adamu, 1 Ziwei Zhai, 1 Krystian Wisniowski,1 Shahab Bakhtiari Gorajoobi,1 Ali Shakiba,2 Mahmudur Rahman, 2 Jaroslaw Rzegocki, 2 Gianluca Guerra, 2 Eric Numkam Fokoua,1 Yong Chen, 1 Gregory Jasion, 2 and Francesco Poletti1,2\*

2. Optoelectronics Research Centre, University of Southampton, SO17 1BJ, UK, \*email: fp@soton.ac.uk

Abstract: We report the first hollow-core DNANF fiber with ultra-low loss in two separate antiresonance windows. The fiber, featuring a novel hybrid-thickness geometry, measures 0.11dB/km at 1550nm and, simultaneously, a record-low loss of 0.13dB/km at 1015nm. © 2026 The Authors

## 1. Introduction

The continuous growth in global data traffic is driving the optical transport network toward ever-higher capacity, motivating research into amplifiers and optical fibers that can extend usable spectral bandwidth beyond the conventional C- and L-bands. In standard glass-core single-mode fibers (SMFs), the combination of low loss, singlemode guidance, and acceptable bending performance is restricted to a relatively narrow spectral region. In contrast, hollow core fibers (HCFs) offer the prospect of significantly broader windows with low loss and dispersion, and effectively single-mode transmission [1]. Recent results have shown that, around the telecoms window, HCFs operating in the first antiresonant window (1st ARW) can support bandwidths 2.5 times broader than state-of-the-art SMFs [2]. In addition, HCFs can also guide light in a second ARW (2nd ARW). Prior work has exploited this either by shifting the 2nd ARW to \~1550 nm to improve fabrication yield and tolerance, at the expense of reduced low-loss bandwidth [3,4], or by enabling simultaneous guidance at 1550 nm (1st ARW) and 850/900 nm (2nd ARW). Although not yet optimized for achieving <0.2 dB/km loss in both windows, these dual-window fibers have attracted interest for their ability to transmit simultaneously single photons at their native wavelengths and telecoms traffic [5, 6].

An alternative and compelling opportunity is to explore dual-window operation around 1000 nm, in addition to the conventional 1550 nm band. Low-loss guidance in the 1 µm region would enable, for instance: (i) broadband data transmission exploiting the wide gain bandwidth of Yb-doped amplifiers [7]; (ii) data transmission at 1550 nm and simultaneous tens of W-scale laser delivery at \~1060 nm to power remote devices or antennas [8]; and/or (iii) remote optically pumped amplifiers (ROPA) with a high-power 980 nm pump. By tailoring the membrane thicknesses of HCF tubular resonators, it becomes possible to position the 2nd and 3rd ARWs at \~1550 nm and \~1000 nm, respectively. Building on this concept, we demonstrate the first DNANF-type HCF [9] achieving a loss of 0.13 dB/km or less at both \~1000 nm and \~1550 nm. Unlike previous low-loss DNANFs employing near-identical membrane thickness for all nested resonators, we introduce a new “hybrid-window” design: the outer resonators use thicker membranes to guide in the 2nd/3rd ARWs (1550/1000 nm), while the nested tubes use thinner membranes to guide in the 1st/2nd ARWs. We show that this idea enhances both bandwidth and fabrication yield compared with standard equal-thickness HCFs.

## 2. Modelling

The operation of antiresonant HCFs is mostly governed by the thickness of the tubular membranes (t) surrounding the hollow core. Studies of $1 ^ { \mathrm { s } }$ and 2nd ARW designs have shown that “thin membrane” 1st ARW designs (t\~500 nm for 1550 nm guidance) offer the widest bandwidth, while 2nd ARW designs (t\~1150 nm) offer an increased maximum yield per preform, due to an enhanced resistance of the thicker membranes to surface-tension-driven phenomena during the draw that can cause the tubes to contact inside the furnace. Here, we propose a hybrid window guidance approach (Hybrid ARW), that represents an excellent compromise between the two. At 1550 nm, the outermost tubes operate in the $2 ^ { \mathrm { n d } } \mathrm { A R W } ,$ while the middle and inner nested elements function in the 1st ARW. Fig.1(a) compares the simulated total loss of 1st, 2nd and Hybrid ARW DNANFs with the same: core size (27 µm), tube sizes (\~31, \~26 and \~12 µm) and inter-tube gaps (3 µm). The 1st ARW design shows the widest bandwidth at 1550 nm and a highorder window centered around 750 nm (tunable to \~850 nm if needed). In contrast, both the $2 ^ { \mathrm { n d } }$ and Hybrid ARW designs center their high-order window of operation around 1000 nm, where they achieve identical loss and bandwidth. However, in the window around 1550 nm the hybrid design offers a wider bandwidth (280 nm vs 240 nm below 0.2 dB/km) and slightly lower total attenuation than the $2 ^ { \mathrm { n d } } \mathrm { A R W }$ design. Besides, the Hybrid design is also more tolerant to fabrication imperfections. The simulations in Fig. 1(b) show that when the thickness of the middle and inner tubes are only 5% thicker and thinner (respectively) than those of the outer tubes, the loss and bandwidth of the 2nd ARW design worsens, while the Hybrid design is completely unaffected. This brings clear fabrication advantages.

![](/img/mineru_output/Th4B.8/auto/images/b7a71b45b2385b001c48ab7500eb34d5fe70a4e4668b68e30ee7691c6bbb912b.jpg)

![](/img/mineru_output/Th4B.8/auto/images/1f32e6926be52f5ca2afb61ae6f31c4b6a197433da739f437d9d4bb7e79f8d4c.jpg)

![](/img/mineru_output/Th4B.8/auto/images/a3e77bc2d947d0a3f3626b39b38bd099920a217582a2c7fcb01727daba8e05a8.jpg)  
Fig.1: (a) FEM simulation comparison between the total loss of the $1 ^ { \ast } , 2 ^ { \ast d }$ and Hybrid ARW designs; (b) Adding 5% thickness variation to the middle and inner tubes creates notable worsening in the loss and bandwidth of the 2nd ARW design, while the Hybrid case is unaffected.

## 3. Fabrication and Characterization

Fig. 2(a) shows the geometry of the Hybrid-DNANF (Hyb-DNANF), fabricated by a stack, fuse, and draw method. The fiber has 220 µm cladding and 27 µm core, uniform across the drawn length of 14 km, with only 0.7% variation from start of the pull (SOP) to end of pull (EOP). In this fiber, the outermost antiresonant capillaries have an outer diameter (OD) of \~30 µm and t\~1200 nm (2nd ARW), while the middle and inner nested tubes have OD \~25 and 10 µm, respectively, and $t { \sim } 5 0 0$ nm $( 1 ^ { \mathrm { s t } } \mathrm { A R W } )$ . Fig. 2(b) and (c) show a zoomed-in detail of a group of resonators from a conventional 1st ARW DNANF and from the Hyb-DNANF of this work, respectively. As an early prototype, the fiber still shows some asymmetries in tube size (thickness) and position. Despite this, its performance remains exceptionally good, in agreement with optical simulations above indicating that a hybrid design is less sensitive to fiber geometry variations.

![](/img/mineru_output/Th4B.8/auto/images/078065b0adeaae5bef61dc79141669ceaf5986eb321c86ec073301b469cb94b0.jpg)

![](/img/mineru_output/Th4B.8/auto/images/54af0a3a401c8421fa81892a43e087bb6fa82831478b8564a14da6c3ce64af54.jpg)

![](/img/mineru_output/Th4B.8/auto/images/e2a7036585676210d552e7ee14b9d50fdacd5f78e424e9e0543debc0ec419d56.jpg)

![](/img/mineru_output/Th4B.8/auto/images/42e009f0ec351b86b8ab0a87d94a3c79b957bff502385097deec0fd3ac30fd8c.jpg)

![](/img/mineru_output/Th4B.8/auto/images/928d56cc474b7103b2c17a306c8a47d515b7a9f272fedb30ae9c809a62ad02c5.jpg)

![](/img/mineru_output/Th4B.8/auto/images/39fc4f2c72cea310d76c06386ab7267b7b2e61ad4872f246768c62341d854e31.jpg)  
Fig.2 (a) Microscope image of the fabricated Hyb-DNANF; (b) a group of state-of-the-art (SotA) 1st ARW capillaries [2]; (c) a group of hybrid design capillaries fabricated in this report; (d) dual-band hybrid transmission window of the cutback fiber at 20 m and 14.19 km; (e) attenuation of the fabricated hybrid fiber measured by cutback and OTDR and validated by simulation compared to a PSCF; (f) OTDR trace of the fabricated fiber at 1550 nm with linear fit; (g) dispersion of the fabricated hybrid fiber simulated based on the fiber SOP and EOP.

The fiber loss was measured by cutback and bidirectional (BiDi) OTDR, and verified by simulation. The cutback was performed from the full length of 14.19 km, down to 20 m, with multiple cleaves to ensure measurement accuracy. Figure 2(d) shows the transmission of the long and short lengths, showing two ARWs: one in the 1 µm region and another spanning from O to L bands. The cutback trace in Fig. 2(e), indicates exceptionally low loss simultaneously in both transmission windows, in good agreement with simulations. At 1550 nm the cutback indicates 0.11 dB/km loss, while the linear fit to the BiDi OTDR trace in Fig. 2(f) shows a loss of 0.088 dB/km at 1550 nm, close to the simulated 0.082 dB/km. Note that, thanks to fabrication improvements, the detrimental $\mathrm { C O _ { 2 } }$ absorption lines in this waveband have been reduced by \~4x as compared to Ref. [2]. In the 1 µm region, the fiber exhibits a record-low loss of 0.13 dB/km at 1015 nm, improving the previous record in this waveband, also achieved in a DNANF HCFs, of 0.168 dB/km at 1080 nm [10]. Our fiber offers 74 nm where the loss remains below 0.2 dB/km. For comparison, at these wavelengths, SMF-28 and pure silica core fibers (PSCFs) have losses of 0.75 and \~0.7 dB/km, respectively.

The simulated dispersion of the Hyb-DNANF is shown in Fig. 2(g). The fiber has 6.0 ps/(nm·km) at 1015 nm and 5.2 ps/(nm·km) at 1550 nm, similar to $\mathrm { ~ a ~ } 2 ^ { \mathrm { n d } } ~ \mathrm { A R W }$ design and \~30% higher than an equivalent 1st ARW fiber with comparable core sizes. The intermodal interference (IMI) of the 14 km fiber, measured at 1550 nm with a swept wavelength scanning method [2], read – 56.4 dB/km, confirming quasi single mode operation. Procurement of equipment to measure its modal purity also in the 1 µm region is ongoing. We also checked its macrobend loss by winding the fiber on $3 ^ { \mathfrak { p } }$ and $2 ^ { \mathfrak { p } }$ diameter bobbins. Fig. 3(a) shows how the bend loss compares with that of a $2 ^ { \mathrm { n d } }$ ARW DNANF with supported tubes [4], and with various solid core SMFs. At bend radii \~30 mm and at 1550 nm, the new Hyb-DNANF slightly outperforms a standard G652.D SMF, and has similar performance as a $2 ^ { \mathrm { n d } }$ ARW DNANF.

Besides wider bandwidth and improved tolerance to fabrication imperfections than $2 ^ { \mathrm { n d } }$ ARW, the Hybrid design also outperforms $1 ^ { s t }$ and $2 ^ { \mathrm { n d } }$ ARW designs in terms of its potential for high draw yields. Fig. 3(b) shows a yield modeling comparison between $1 ^ { \mathrm { s t } } , 2 ^ { \mathrm { n d } }$ , and Hybrid ARW HCFs. When fabricating an HCF, a dynamic occurs between the tube expansion due to applied gas pressure and contraction due to surface tension which can result in detrimental mid-draw contact (MDC) between neighboring capillaries [11]. The MDC “pressure buffer” represents a safety buffer between the pressure values required to achieve a target fiber and those at which MDC occurs. Figure 3(b) shows that when increasing the yield of the preform (km of fiber per m of preform) the MDC buffer reduces. It also shows that a 2nd ARW design allows 2.5-3x greater yield than a 1st ARW design. The Hyb-DNANF has the same dynamics as the 2nd ARW, with the additional advantage that, since the middle and inner capillaries are thinner, they take up less space in the preform. This offers more room for thicker outer capillaries, which results in an additional yield advantage. In the simulated cases, the Hybrid HCF is estimated to produce 28 to 35% more fiber per preform than a $2 ^ { \mathrm { n d } }$ ARW.

![](/img/mineru_output/Th4B.8/auto/images/09f96e209862e8220065d015ffe3aaca1d10aa55c80ff820e60b1b088cf69677.jpg)

![](/img/mineru_output/Th4B.8/auto/images/14481271edd863175a2cca10cbcce89fec8e123a65596b9ec332071719227bd3.jpg)  
Fig. 3. (a) Bend loss comparison between the Hyb-DNANF, SMF-28 and G657 fibers, and $1 2 ^ { \circ }$ ARW DNANF [4]; (b) HCF draw modelling [11], showing how yield per preform can be increased from 1st to $2 ^ { \mathrm { s d } } \mathrm { A R W }$ , and how the Hybrid fiber surpasses both designs.

## 4. Conclusions.

We have demonstrated three breakthroughs: (a) the lowest loss fiber ever reported in the 1 µm region. The measured 0.13 dB/km at 1015 nm is not only considerably lower than the silica loss (0.7 dB/km) at these key wavelengths for laser delivery, but it is also lower than what silica fundamentally offers at 1550 nm; (b) the first demonstration that a suitably optimized HCF can have ultra-low loss over two antiresonant windows, enabling various impactful applications; (c) a new DNANF variant with a Hybrid guidance that offers similar loss as the 1st ARW designs, as well as wider bandwidth, less tolerance to manufacturing imperfections and ultimately higher yields than 2nd ARW.

Acknowledgements The authors would like to thank the Engineering and Production teams at Romsey for their assistance, and extend special thanks to Joshua Clements and Liam Carter for capturing the SEM images. EPSRC FASTNET project EP/X025276/1 is kindly acknowledged.

## 5. References

[1] F. Poletti, et al., Opt. Exp., 22, 20, (2014).

[2] M. Petrovich, et al., Nat. Photon., 19, (2025).

[3] S. Gao, et al., ECOC 2025, PDP.

[4] Y. Ding, et al., ECOC 2025, Tu.04.01.2.

[5] A. I. Adamu, et al., OFC 2024, M3J.1.

[6] L. Carosini, et al., Optica Quantum, 4, 2, (2026).

[7] X. Huang, et al., IEEE Photon. Tech. Letts., 36, 12, (2024).

[8] M. Matsuura, et al., IEEE Trans. Power Electron., 36, 4, (2021).

[9] G. T. Jasion, et al., OFC 2022 PDP, Th4C.7.

[10] J. Shi, et al., Nat. Commun., 8965, (2025).

[11] G. T. Jasion et al., Opt. Express, 27, 15, (2019