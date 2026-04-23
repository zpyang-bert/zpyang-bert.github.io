---
layout: post
title:      "Fully Integrated 1064 nm Transmitters with Widely Tunable GaAs Lasers and > 100-GHz Thin-Film LiNbO3 Modulators"
date:       2026-04-18 21:47:35
author:     "Bert"
tags:
  - Mineru
---
Boqiang Shen, 1, \* Kewei Bian, 2 ,\* Kaustubh Asawa, 1 Igor Kudelin, 1 Theodore Morin, 1 Bowen Song, 1 Yang Shen, 1 Joel Guo, 1 Jonathan Peters, 1 Catherine Nguyen, 1 Glenn Kim, 1 Nathan Kim, 1, Stephen Didde, 3 Ryohei Omori, 3 Daneil Lopez, 3 Zeyu Zhang, 1 Tin Komljenovic, 1 Minh Tran, 1 Yuan Yuan, 2,† Chong Zhang 1, †

1 Nexus Photonics, 6500 Hollister Avenue, Goleta, California 93117, USA 2Department of Electrical and Computer Engineering, Northeastern University, Oakland, California 94613, USA 3Keysight Technologies, 5301 Stevens Creek Boulevard, Santa Clara, CA 95051, USA \* These authors contributed equally †y.yuan@northeastern.edu; czhang@nexusphotonics.com

Abstract: We demonstrate the first fully integrated 1064 nm GaAs-on-TFLN transmitter combining widely tunable GaAs lasers with >100 GHz thin-film lithium niobate modulators. The device achieves 100 Gb/s NRZ and 160 Gb/s PAM4 transmission.

## 1. Introduction and Motivation

Optical interconnects have historically concentrated operation near 1310 nm and 1550 nm, largely because standard single-mode silica fiber is specified and optimized for low attenuation in these bands [1]. However, the scaling of distributed AI systems is elevating end-to-end latency as a first-order constraint. Hollow-core fiber (HCF) is therefore gaining attention since guiding light predominantly in air enables substantially lower propagation latency than solid-core fiber and reduces nonlinear impairments [2]. Recent nested antiresonant HCFs have demonstrated losses comparable to (or lower than) solid-core silica at several technologically relevant wavelengths including 660 nm, 850 nm, and 1064 nm, indicating that future HCF-based links may be less constrained by the conventional silica loss windows [3].

This reopened wavelength freedom makes the 1064 nm band attractive when combined with mature gain and amplification technologies in this region. Ytterbium-doped fiber amplifiers provide efficient gain over approximately 1030–1100 nm, enabling practical power scaling at this wavelength range [4]. At the device level, GaAsbased material systems are naturally suited for high-efficiency emission in the 0.8–1.1 µm range due to their direct bandgap and well-established AlGaAs/GaAs quantum well platforms [5]. GaAs also benefits from mature highvolume substrate manufacturing, strong differential gain in ∼1 µm quantum well designs, making it a scalable platform for compact, efficient 1 µm transmitters [6]. For modulation, thin-film lithium niobate (TFLN) offers strong Pockels electro-optic operation with demonstrated >100 GHz traveling-wave bandwidth in the telecommunication band [7]. Importantly, TFLN modulators are intrinsically broadband and have been experimentally demonstrated at 1064 nm [8], making them compatible with ∼1 µm GaAs sources. Despite these complementary strengths, full on-chip co-integration of GaAs lasers with TFLN modulators has not been demonstrated.

In this work, we demonstrate the first fully integrated GaAs-on-TFLN photonic platform, realizing a 1064 nm transmitter that combines GaAs distributed feedback (DFB) and widely tunable lasers with a record high frequency TFLN modulator at 1064 nm exhibiting >100 GHz electro-optic bandwidth. This heterogeneous integration unifies on-chip light generation, wavelength agility, and ultrafast modulation within a compact photonic integrated circuit, establishing a new platform for next-generation low-latency datacom enabled by HCF, free-space optical communication, and for SWaP-constrained optical systems.

## 2. Transmitter Architecture and Fabrication

The heterogeneous GaAs-on-TFLN photonic integrated circuit architecture is illustrated in Fig. 1. GaAs epitaxial layers containing the laser gain regions are bonded onto a processed TFLN photonic wafer using a low-temperature bonding process compatible with lithium niobate. The TFLN layer provides low-loss optical waveguides and supports high-speed electro-optic modulation.

Optical coupling between the GaAs laser sections and the TFLN waveguides is achieved using Nexus’s optical bridge methodology as detailed in [9]. The optical gain waveguides for DFB and widely tunable laser cavities are implemented in the GaAs while the distributed gratings as well as the external Vernier ring filters are realized in the TFLN. Electro-optic modulators are implemented as traveling-wave Mach–Zehnder interferometers (MZMs) in the TFLN layer with coplanar RF electrodes optimized for broadband impedance matching and velocity matching at 1064 nm. On-chip monitor photodiodes are also integrated, enabling operational control via reverse biasing of the GaAs epitaxial structure.

![](images/6b1e31dbb673cd176720c8862debb612b385dcf5223802f0994820b286506241.jpg)  
Fig. 1. Heterogeneous GaAs-on-TFLN platform. (a) Schematic cross-section illustrating GaAs gain layer heterogeneously integrated on TFLN. (b) An image of the GaAs epitaxial layer bonded on top of a 4-inch patterned TFLN wafer after substrate removal. (c) A 4-inch wafer completed with the full GaAs fabrication process. (d) An image of the wafer-level characterization of all devices. (e) Microscope image of the transmitter comprising a single-mode laser, a MZM with heater phase section for bias control, traveling-wave electrodes and high-speed GSG pads, a SOA for boosting output power with multiple monitor photodiodes for operation control - all on a single chip.

## 3. Integrated GaAs Laser Performance

Figure 2 summarizes representative measured performance of integrated GaAs lasers at 1064 nm. The DFB lasers exhibit stable single-mode operation with side-mode suppression ratio (SMSR) of >50 dB, threshold current of 27 mA, and on-chip output power coupled into TFLN waveguides of >10 mW under continuous-wave operation.

Widely tunable GaAs lasers are implemented using two Vernier ring resonators, enabling wavelength tuning over a range of >20 nm around 1064 nm. The tuning behavior is continuous and repeatable over the demonstrated range, and the output couples efficiently into the underlying TFLN waveguides. These measurements confirm robust laser operation following heterogeneous integration and provide on-chip light sources compatible with ultrafast modulation. In addition to serving as tunable lasers, the GaAs gain section also functions as a semiconductor optical amplifier (SOA), providing on chip gain to support higher output power and larger modulation signals.

![](images/e8f4d504c34e0c5ea40a233195c32f129a4268d2d6de2a1d67f962151f5f4583.jpg)

![](images/a0c65ba3a64d67eecbe81d6a15879ff69e295ef0990ed4616376c115cfd5fde1.jpg)

![](images/313c5b035d47475e8cca7248c71e6dcd1effaa25d979964bbf166e6c81b9042c.jpg)  
Fig. 2. Integrated GaAs laser performance at 1064 nm. (a) DFB laser’s L–I–V curve and (b) DFB laser’s optical spectra at different gain current, indicating stable single-mode operation (SMSR> 50 dB). (b) Vernier wavelength tuning with high SMSRs across the tuning range >20 nm.

## 4. High-Speed Laser–Modulator–SOA Integration

To evaluate the system-level capability of the platform, the heterogeneously integrated GaAs lasers are directly routed on-chip into TFLN MZMs, enabling a fully integrated 1064 nm high-speed transmitter. Figure 1(e) shows the integrated device, where a widely tunable GaAs laser is monolithically coupled to a 5.8 mm-long travelingwave TFLN MZM. The cross-section in Figure 3(a) shows a 360-nm-thick LN film with 180 nm etch depth, forming rib waveguides with ${ \sim } 6 2 ^ { \circ }$ sidewall angle. The capacitively loaded electrodes consist of 900-nm-thick gold optimized for broadband microwave propagation with simultaneous velocity and impedance matching.

The RF response in Figure 3(b) shows an electrical reflection $S _ { 1 1 }$ around −20 dB across the measured frequency range. The small-signal EO response in Figure 3(c) exhibits a 3 dB bandwidth exceeding 100 GHz, confirming efficient traveling-wave operation at 1064 nm. To the best of our knowledge, this represents the highest bandwidth demonstrated at this wavelength band [8]. Figure 3(d) shows the time-domain optical modulation response under a 2 MHz sinusoidal electrical drive at the minimum-transmission bias point. The half-wave voltage $V _ { \pi }$ is extracted from the measured modulation depth, yielding a $V _ { \pi }$ · L of 1.8 V·cm, demonstrating high EO modulation efficiency.

Large-signal measurements further validate system-level operation. A tunable GaAs laser serves as the optical source, followed by a TFLN MZM for high-speed modulation and a GaAs SOA for output power amplification, together demonstrating a fully integrated transmitter on a single chip. As shown in Fig. 3(e), a clear and open eye diagram is obtained at 100 Gb/s NRZ with a signal-to-noise ratio (SNR) of 14.61 dB. Figure 3(f) further demonstrates well-resolved eye openings at 160 Gb/s PAM4, with a post-FFE TDECQ of 0.04 dB. The currently achieved data rate is limited by the RF bandwidth of the test setup, which includes the arbitrary waveform generator, power amplifier, and optical receiver, exhibiting a combined attenuation of ∼ 20 dB at 50 GHz. A higher-bandwidth measurement setup, consistent with the >100 GHz bandwidth of the TFLN modulator, would enable higher data rates. These results confirm that heterogeneous integration of GaAs lasers and TFLN modulators preserves both modulation efficiency and high-speed performance, with no observable degradation introduced by the interface.

(a)  
![](images/002a1e9fe2307a0983dfd53d8836e4a5586e95c381de8920e418e0b3f3ee1d1e.jpg)

![](images/4a60ce7d2c9545c4997127649de60d8dbc960b497fd987c026890d96a92d8ba5.jpg)

(c)  
![](images/78f1f22d9f7501a2bef850027ae40669115bdbcea1c815ad241e18244226b88e.jpg)

![](images/713ec03a081cae6868073d10f07cf2b4e2fed95c8de990abbc206f259c67c735.jpg)

![](images/0a85d3d6212a962085556dbb2c3bfa010d509a4e4fa79fdd680510d68fb7e102.jpg)

![](images/6667b6532b978a950aae084ef1397bb1abd124de1c90b42d84d84f26c5e37bf2.jpg)  
Fig. 3. High-speed modulation at 1064 nm using heterogeneous GaAs lasers and TFLN MZMs. (a) Cross-sectional schematic of the TFLN MZM. Measured (b) electrical $S _ { 1 1 }$ and (c) EO response $S _ { 2 1 }$ up to 110 GHz. (d) Transmission spectrum at null bias with 2 MHz sinusoidal modulation for $\mathrm { v } _ { \pi }$ extraction. Measured (e) 100 Gb/s NRZ and (f) 160 Gb/s PAM4 eye diagrams using fully integrated laser, MZM, and SOA.

## 5. Conclusion

We demonstrate the first fully integrated GaAs-on-TFLN photonic platform combining on-chip GaAs widely tunable lasers with 100-GHz-class thin-film lithium niobate electro-optic modulators at 1064 nm. The platform enables on-chip light generation, wavelength agility, and ultrahigh-speed modulation within a single chip, providing a new route toward compact, high-performance optical engines for latency-sensitive terrestrial links, free-space optical communications, and SWaP-constrained optical systems in the 1-µm band.

Acknowledgment. The authors gratefully acknowledge the support of Dr. Ray Beausoleil, Dr. Marco Fiorentino, Dr. Zhihong Huang, and Dr. Xuema Li at HPE Lab, Hewlett Packard Enterprise, for their support with the measurements. The authors also thank Prof. Andreas Beling and Prof. Joe Campbell at the University of Virginia for their support with large signal measurements; Prof. Jun-Chau Chien and Prof. Mengjie Yu at the University of California, Berkeley, for valuable discussions.

## References

1. International Telecommunication Union, “Characteristics of a single-mode optical fibre and cable,” Recommendation g.652, ITU-T (2024). ITU-T G.652 (08/2024).

2. Nokia, “Hollow-core fiber: Not just for low latency?” https://www.nokia.com/blog/ hollow-core-fiber-not-just-for-low-latency/. Accessed March 2026.

3. H. Sakr, Y. Chen, G. T. Jasion, T. D. Bradley, E. N. Fokoua, J. R. Hayes, D. J. Richardson, and F. Poletti, “Hollow core optical fibres with comparable attenuation to silica fibres between 600 and 1100 nm,” Nat. Commun. 11, 6030 (2020).

4. R. Paschotta, “Ytterbium-doped fiber amplifiers,” IEEE J. Quantum Electron. 33, 1049–1056 (1997).

5. I. Vurgaftman, J. R. Meyer, and L. R. Ram-Mohan, “Band parameters for iii–v compound semiconductors and their alloys,” J. Appl. Phys. 89, 5815–5875 (2001).

6. S. Adachi, GaAs and Related Materials: Bulk Semiconducting and Superlattice Properties (World Scientific, 1994).

7. C. Wang, M. Zhang, X. Chen, M. Bertrand, A. Shams-Ansari, S. Chandrasekhar, P. Winzer, and M. Loncar, “Integrated ˇ lithium niobate electro-optic modulators operating at cmos-compatible voltages,” Nature 562, 101–104 (2018).

8. M. M. De Freitas, X. Zhu, M. I. Isti, J. Arnold, R. Xue, J. Zhang, P. Yao, T. Creazzo, C. Cullen, S. Shi et al., “Thin-film lithium niobate mzm operating at 1-µm wavelength with low vπ and high bandwidth,” IEEE Photonics Technol. Lett. (2026).

9. M. A. Tran, C. Zhang, T. J. Morin, L. Chang, S. Barik, Z. Yuan, W. Lee, G. Kim, A. Malik, Z. Zhang et al., “Extending the spectrum of fully integrated photonics to submicrometre wavelengths,” Nature 610, 54–60 (2022).