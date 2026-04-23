---
layout: post
title:      "1.6T (8200Gb/s) 2FR4 Silicon Photonic IMDD Transceiver with Monolithically Integrated Ultra-Low Crosstalk and Wideband Multiplexer"
date:       2026-04-18 11:54:54
author:     "Bert"
tags:
  - Mineru
---
Haijiang Yu1, 2\*, Gao Xudong1\*, Ming Su1, Jun Li1, Jian Chen1, Ruizhi Zhang1, Peng Gao1, Mengxue Tao1, Yang Wu1, Qin Li1, Yuan Yao1, Qiuhong Hu1, Qijian Xu1, Madhav Bhatta2, Changfei Hu1 1Wuhan HGGenuine Optics Tech Co., Ltd, HUST Science & Technology Park, Wuhan, Hubei, 430223 P.R. China 2Genuine Optics, 2580 North First Street, Suite 100, San Jose, CA 95131, USA Author e-mail address: yuhaijiang@genuine-opto.com; gaoxudong@genuine-opto.com; suming@genuine-opto.com

Abstract: We demonstrate a monolithically integrated 1.6T (8×200 Gb/s) 2×FR4 silicon photonic transceiver using a novel Bragg-grating-based Multiplexer (MUX). This design achieves a 15 footprint reduction, 10 dB lower crosstalk, and 5 nm broader bandwidth than conventional MZIbased MUXs. Validated in an OSFP module with 3nm DSP, the 106.25 GBaud PAM4 link shows 2\~2.5 dB TDECQ and as low as 110-13 BER, meeting IEEE 802.3dj requirements. © 2026 The Author(s)

## 1. Introduction

The rapid expansion of AI/ML clusters and hyperscale data centers is driving an urgent transition from 800G to 1.6T optical interconnects. Silicon Photonics (SiPh) has emerged as the premier platform for this scaling, leveraging highdensity monolithic integration and CMOS compatibility. However, migrating to 200 Gb/s per lane in 1.6T 2×FR4 Intensity-Modulation Direct-Detection (IMDD) systems imposes stringent requirements on optical power budgets and signal integrity. Traditional multiplexer (MUX) architectures—including arrayed waveguide gratings (AWGs), Echelle gratings, and cascaded Mach-Zehnder interferometers (CMZIs)—present critical design trade-offs [1]. AWGs and Echelle gratings typically suffer from high insertion loss and restricted flat-top bandwidth, while CMZIs and AWGs require a prohibitive physical footprint. Further more Echelle gratings often exhibit significant interchannel crosstalk, which degrades the bit-error-rate (BER) performance and complicates high-volume manufacturing for 2×FR4 architectures.

In this paper, we propose and demonstrate a novel, monolithically integrated Bragg-grating-based MUX design for 1.6T 2×FR4 SiPh transceivers. This design achieves a 5 nm broader flat-top response and a 10 dB reduction in crosstalk compared to CMZIs fabricated on the same platform. Additionally, it provides significantly wider bandwidth than Echelle gratings adopted in commercial SiPh products [2][3] while maintaining a compact footprint. We experimentally validate the architecture using a fully functional 1.6T 2×FR4 (8×200 Gb/s) OSFP transceiver module. The transmitter demonstrates superior performance, including a TDECQ of 2\~2.5dB, an extinction ratio (ER) >4 dB, and BER up to 110-13, To our knowledge, this is the first demonstration of a Bragg-grating-based MUX implemented in SiPh IMDD pluggable module, providing a scalable and manufacturable pathway for nextgeneration high-capacity optical links.

## 2. Structure, Design and Experiment Setup

Fig. 1(a) illustrates the schematic of the proposed monolithically integrated silicon photonics (SiPh) multiplexer (MUX), which comprises four serially cascaded multimode Bragg gratings (MBGs). To optimize the spectral response, we employed a finite Gaussian apodization profile combined with a positive dispersion design, enabling a Bragg filter with high-extinction single-side sidelobe suppression. By cascading these filters, the sidelobes on the reciprocal side are effectively suppressed, significantly reducing inter-channel crosstalk and ensuring high signal integrity for 200 Gb/s per lane operation.

The physical layout of the MUX is shown in Fig. 1(b). The device occupies a compact footprint of approximately 1400m  40m, representing a 15-fold area reduction compared to a conventional Cascaded Mach-Zehnder Interferometer MUX designed on the same reticle for performance comparison as shown in Fig. 1(c). This footprint efficiency is critical for high-density 1.6T 2FR4 architectures where space for co-packaged electronics and multiple optical channels is at a premium. The Bragg grating MUX is monolithically integrated into a complete SiPh

1.6T 2FR4 transmitter, with the layout (after desensitization) depicted in Fig. 1(d). The chip was fabricated in a commercial 200 mm SiPh foundry to ensure a clear path to volume production. To mitigate the thermal sensitivity inherent in silicon, the material properties and process parameters from the Process Design Kit (PDK) were precisely tuned. This included optimizing MUX material, waveguide geometry and cladding layers to minimize the central wavelength shifts across the operating temperature range, thereby eliminating the needs for active thermal tuning.

![](images/4eb55a772a65c23ed082d1c556ac4b19a9ff9d2cd409b0a84feeebb56cb1438b.jpg)

![](images/4b8738034880487a3afacbbf1e2a1821c3301ff820e8a1c21be0c1ab0d6cd651.jpg)  
(b)

![](images/75b5aee6981dcc5dbd2a0ef8238cbbc8727dcdcefcef70a474d540ad044d5423.jpg)

![](images/7bbdcc2e45b27511b8e704fc26baf83c4a8e68ec5e3c9708e65e00f207a463bf.jpg)  
(d)

![](images/0a33c11cab45fb43dfb394e9c20b67575353c6ef6ef7a027755e165cb8cb04ee.jpg)  
(e)

![](images/674b79ae05712ebdc43f6c7e86ddb8c4156d20c7fb5530430c18f842b056c004.jpg)  
(f)  
Fig.1. (a) Schematic of Bragg grating based MUX design, (b) Layout of Bragg grating based MUX, (c) Layout of CMZI MUX, (d) Layout of 2FR4 Transmitter with Bragg grating MUX, (e) 1.6T OSPF 2FR4 module, (f) 1.6T OSFP 2FR4 module test setup

For system-level validation, the SiPh transmitter was integrated into a 1.6T (8×200 Gb/s) OSFP module utilizing a state-of-the-art 3nm DSP, as shown in Fig. 1(e). The 2×FR4 architecture employs two sets of four CWDM wavelengths (1271–1331 nm), each modulated at 106.25 GBaud PAM4 (212.5 Gb/s per lane). The fully packaged module was characterized according to the IEEE 802.3dj framework using an evaluation board (EVB) as shown in Fig.1(f). Transmitter performance was evaluated by driving the transceiver with an SSPRQ signal from the DSP on EVB. The optical output was captured by a 120GHz Keysight DCA (N1032A) to measure TDECQ, ER and OMA. For receiver characterization, the signal was routed through a variable optical attenuator (VOA) and a 90/10 splitter for real-time power monitoring. The receiver’s electrical output was analyzed by the DSP on EVB board to generate BER waterfall curves, with sensitivity defined at the KP4 FEC threshold (2.4×10−4).

## 3. Experiments and Results

The spectral characteristics of the fabricated SiPh CMZI- and Bragg-grating-based MUXs were evaluated using a broadband light source and an optical spectrum analyzer (OSA). As illustrated in Fig. 2(a)-(b) and summarized in Table 1, the Bragg-grating-based MUX achieves a 5 nm wider 1-dB bandwidth than the reference CMZI, which significantly relaxes laser wavelength tuning tolerances and enhances thermal robustness. Furthermore, the Bragg grating MUX improves insertion loss (IL) by 0.1–0.3 dB and reduces inter-channel crosstalk by 10 dB relative to the CMZI, ensuring superior signal isolation for high-baud-rate PAM4 signaling when it’s used as DeMUX in the receiver side. While CH2 and CH4 currently exhibit slightly narrower flat-top bandwidths due to minor design deviations, these will be further optimized in the next iteration through the fine tuning of grating period.

![](images/0f0d9c1141676d83319a0053a6451385ae338f748c9ea64681805c1a0c5740bf.jpg)

![](images/b0df6a06da2b6ea340769cd6c5e4dd7ff9ddf54472331f84324b8499a1475599.jpg)  
(b)  
Fig.2. (a) Measured spectrum of CMZI MUX, (b) Measured spectrum of Bragg grating MUX

Table 1. Key performance metrics comparison of the two kinds of MUX
<table><tr><td rowspan=1 colspan=1>MUX/DEMUX type</td><td rowspan=1 colspan=1>Insertion loss</td><td rowspan=1 colspan=1>Flattop BW</td><td rowspan=1 colspan=1>Cross-talk</td><td rowspan=1 colspan=1>Size</td></tr><tr><td rowspan=1 colspan=1>Bragg Grating</td><td rowspan=1 colspan=1>0.6-0.9dB</td><td rowspan=1 colspan=1>16-20nm</td><td rowspan=1 colspan=1>-25dB</td><td rowspan=1 colspan=1> $1 . 6 \mathrm { m m } \times 0 . 0 4 \mathrm { m m }$ </td></tr><tr><td rowspan=1 colspan=1>Cascaded MZI</td><td rowspan=1 colspan=1>0.9-1dB</td><td rowspan=1 colspan=1>11-14nm</td><td rowspan=1 colspan=1>-15dB</td><td rowspan=1 colspan=1> $2 . 2 \mathrm { m m } \times 0 . 4 \mathrm { m m }$ </td></tr></table>

The 1.6T 2xFR4 OSFP module was validated under 106.25 GBaud PAM4 modulation using the test setup shown in Fig.1(f). Fig.3(a) and (b) display representative optical eye diagrams for the four CWDM channels measured at 15℃ and $7 0 \%$ , respectively. All eight channels exhibit clear eye openings with an extinction ratio (ER) >4 dB, a linearity (RLM)0.96, an $\mathrm { O M A } { > } 1 . 5 \mathrm { d B m } ,$ and TDECQ values less than 2.5dB, falling well within the IEEE 802.3dj specifications for FR4 links. The system-level performance was evaluated using the 3nm DSP on EVB board. As shown in the BER waterfall curves in Fig. 3(c), the module achieves a pre-FEC BER as low as $1 \times 1 0 ^ { - 1 3 }$ and a receiver sensitivity better than -4dBm at a BER of $1 \times 1 0 ^ { - 6 } .$ . These results demonstrate a significant margin against the KP4 FEC threshold $( 2 . 4 \times 1 0 ^ { - 4 } )$ . These findings confirm that the monolithically integrated Bragg grating MUX effectively mitigates the insertion loss, bandwidth and crosstalk trade-offs typical of traditional MUX designs, enabling a high-performance and manufacturable solutions for 1.6T 2FR4 transceiver modules and next-generation high-capacity CWDM optical links.

![](images/87190251e457ed7dc40cf728aef2d0e7f67e18af3e0b92f5912ec650cff1d0d2.jpg)  
(a)

![](images/b8b6e8b596b948c1613371f7a60af31b0bf42b07b241c265a963a2f19572f3ff.jpg)  
(b)  
(c)  
Fig.3 Representative optical eye diagrams for the four CWDM channels under 106.25 GBaud PAM4 modulation: (a) measured at $1 5 ~ ^ { \circ } C .$ , (b) measured at $7 0 \ { } ^ { \circ } \mathrm { C } ,$ (c) BER curves from 8 channels of 2FR4 module measured at $7 0 \ \textdegree C$

## 4. Conclusions

In this paper, we have proposed and demonstrated a novel, monolithically integrated Bragg-grating-based MUX for 1.6T (8200Gb/s) 2×FR4 silicon photonics transceivers. Our architecture achieves a 15-fold footprint reduction compared to conventional CMZI structures while simultaneously providing a 5 nm broader flat-top bandwidth and a 10 dB reduction in inter-channel crosstalk suppression. The MUX was successfully integrated into a fully functional 1.6T 2×FR4 OSFP module driven by a state-of-the-art 3nm CMOS DSP. System-level validation under 106.25 GBaud PAM4 modulation yielded robust performance, with an TDECQ less than 2.5 dB, a pre-FEC BER as low as $1 \times 1 0 ^ { - 1 3 }$ and a receiver sensitivity of -4dBm at a BER of $1 \times 1 0 ^ { - 6 }$ , comfortably meeting IEEE 802.3dj requirements. These results establish the Bragg-grating-based SiPh platform as a highly scalable, high-performance, and manufacturable high-capacity optical connectivity solution for 1.6T and beyond hyperscale data centers.

## 5. References

[1] Wim Bogaerts, et al., "Silicon photonics non-resonant wavelength filters: comparison between AWGs, echelle gratings, and cascaded Mach-Zehnder filters", Proc. SPIE 9365, Integrated Optics: Devices, Materials, and Technologies XIX, 93650H (2 April 2015).

[2] H. Yu et al., “100Gbps CWDM4 Silicon Photonics Transmitter for 5G applications”, W3E.4, OFC 2020.

[3] Sunil Priyadarshi, “Charting the Path Toward 1.6T and 3.2T Optical Module Solutions, “ https://www.photonics.com/Articles/Charting-the-Path-Toward-16T-and-32T-Optical/a70490