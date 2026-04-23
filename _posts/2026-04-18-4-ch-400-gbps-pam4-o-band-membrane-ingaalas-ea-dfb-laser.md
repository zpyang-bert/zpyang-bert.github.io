---
layout: post
title:      "4-ch × 400-Gbps PAM4 O-band Membrane InGaAlAs EA-DFB Laser Array on a Si Photonics Platform"
date:       2026-04-18 12:25:46
author:     "Bert"
tags:
  - Mineru
---
Takuma Aihara1,2,\*, Tatsurou Hiraki1,2, Yoshiho Maeda1,2, Takuro Fujii1,2, Masashi Ota1, Tomonari Sato1,2, and Shinji Matsuo2

1Device Innovation Center, NTT, Inc., 3-1, Morinosato Wakamiya, Atsugi-shi, Kanagawa, 243-0198. Japan. 2Device Technology Labs, NTT, Inc., 3-1, Morinosato Wakamiya, Atsugi-shi, Kanagawa, 243-0198. Japan. \*takuma.aihara@ntt.com

Abstract: We demonstrate a heterogeneously integrated 4-channel O-band membrane InGaAlAs EA-DFB laser array on Si, achieving 400- and 448-Gbps PAM4 per channel using 100-µm-long modulators at 0.5-V swing, resulting in a 3.2-Tbps/mm shoreline density.

## 1. Introduction

The continued growth of data center traffic places increasing demands on short-reach optical links for higher perlane baud rates and integration density. Si photonics is an essential platform for high-density integration. To date, Si microring modulators have been widely adopted owing to their ultra-compact footprint; however, their modulation bandwidth scalability is fundamentally limited by the photon lifetime. Although 400-Gbps operation has been reported using Si slow-light modulators [1], high optical loss and large drive voltage remain critical challenges.

Electro-absorption modulators (EAMs) are attractive owing to their compact footprint, low power consumption, simple voltage-driven operation, and high-speed capability. GeSi EAMs have demonstrated 3-dB E–O bandwidths exceeding 110 GHz [2]; however, achieving high modulation efficiency and O-band operation remains challenging.

To overcome these challenges, heterogeneously integrated III–V modulators on Si are highly promising. However, previously reported heterogeneously integrated EAMs typically employ relatively wide mesa structures, which limit the intrinsic modulation bandwidth due to increased junction capacitance [3]. By reducing the mesa width, improved high-speed performance has been demonstrated in EA–DFB lasers fabricated on InP substrates [4].

In this work, we demonstrate a Si photonic integrated circuit (PIC) incorporating a four-channel membrane InGaAlAs EA-DFB laser array. The membrane structure is highly advantageous for heterogeneous integration with Si, as it enables III–V semiconductor regrowth on a Si substrate. Moreover, increased optical confinement in the core layer and reduced device capacitance contribute to improved modulation bandwidth and lower power consumption [5]. By refining the doping profile at the boundary of the multiple quantum well (MQW) core region, the 100-µm-long EAM achieves a higher modulation efficiency (3.8 dB/V) than previous devices (\~2 dB/V [5]), enabling 400-Gb/s operation at 0.5-V swing. By leveraging Si waveguides for channel routing, we densely integrate four channels, enabling 4 × 400-Gbps operation and achieving a shoreline density of 3.2 Tbps/mm in the O-band.

## 2. Device Structure and Basic Characteristics

Figure 1(a) shows a schematic of the PIC incorporating four membrane InGaAlAs EAMs (100-µm long) and two DFB lasers (300-µm long). Each DFB laser provides two outputs, each coupled to an EAM through Si waveguides. In the current configuration where two EAMs share a single laser, the architecture can scale to multi-laser integration for redundancy or backup, while any reduced output power can be compensated by adding an semiconductor optical amplifier (SOA) after the EAM or at the receiver to maintain an energy-efficient optical link [6]. The adjacent EAM pitch is 250 µm. SiOx waveguides are integrated at the chip facet for fiber coupling. The InGaAlAs MQW region, with a photoluminescence peak wavelength of 1.26 m, is embedded within a 230-nmthick InP membrane with a lateral p–i–n junction, as shown in Fig. 1(b). To improve the uniformity of the lateral electric-field distribution across the MQW core, the Zn (acceptor) diffusion annealing temperature was increased from 480 to $4 9 0 ~ ^ { \circ } \mathrm { C } ,$ slightly deepening the doping profile compared with our previous device [5]. The EAM is designed without a Si core to achieve strong confinement, whereas the DFB laser forms a supermode with the Si core for stable lasing and higher output power. Figure 1(c) shows a photograph of the PIC with an attached fiber array block, where the fiber pitch is 84 m. The dashed red box indicates the active device region including EAMs and lasers (2.0 mm × 0.5 mm), and the shoreline density is defined based on the active device width of 0.5 mm.

![](/img/mineru_output/Th4A.1/auto/images/10d2821532ed6539e04dc1adcf153922c176e4b0f0cd1252e5090ae788151b4f.jpg)

![](/img/mineru_output/Th4A.1/auto/images/2206c3268472d0bac2212ef39d8df562d9982872361f2fbb015a877fd62d61d2.jpg)

![](/img/mineru_output/Th4A.1/auto/images/b402264981efa0d4330bb8885d48c463c5203c4c077c31138e633887c6963b92.jpg)  
Fig. 1. (a) Schematic of the Si PIC and (b) cross-sectional view of EAM. (c) Photograph of the fabricated PIC with an attached fiber block.

The device characteristics were then measured. All measurements were conducted at $5 5 ^ { \circ } C ,$ except for the E–O response measured at $2 5 ^ { \circ } \mathrm { C } .$ Figure $2 ( \mathrm { a } )$ shows the lasing spectrum of the DFB laser at 50 mA, confirming singlemode O-band operation. As shown in Fig. 2(b), a 3.8-dB extinction ratio was achieved under a 0–1 V swing. The modulation efficiency (3.8 dB/V) is higher than that of the previously reported EA-DFB laser (\~2 dB/V [5]), owing to refinement of the doping profile and optimized wavelength detuning at $5 5 ~ ^ { \circ } \mathrm { C } .$ Figure 2(c) shows the E–O response without termination resistors. A 3-dB bandwidth of 103 GHz is achieved at $\mathrm { a } - 1 . 5 \mathrm { V }$ bias, owing to the low junction and parasitic capacitance of the 100-µm-long membrane lateral p–i–n structure.

![](/img/mineru_output/Th4A.1/auto/images/e55f19633220a4351e56d21eff0a5085ccc7425375a6cb6db4c3b7af7485d46f.jpg)

![](/img/mineru_output/Th4A.1/auto/images/f531a9310ea6016471771a894d4755f286352b9c13bdc011e8e8a27fbe1e9364.jpg)

![](/img/mineru_output/Th4A.1/auto/images/3e8c14e723ed61c6ee913ab37c5e76ef2d15768bd8627fd85127f14cae9b6ce9.jpg)  
Fig. 2. (a) Lasing spectrum of the integrated DFB laser at 55°C. (b) Static characteristics of the EAM at 55°C, with a low laser injection current (10 mA). (c) Small-signal E-O response of the EAM without termination resistors at $2 5 ^ { \circ } \mathrm { C } .$

## 3. Modulation experiments

Electrical PAM4 signals were generated by a 256-GSa/s arbitrary waveform generator (AWG, Keysight M8199B). For higher symbol-rate operation, a frequency-domain interleave unit (FDIU) was inserted after the AWG to extend the usable bandwidth by reducing high-frequency attenuation. The output signal was then amplified by a 135-GHz (6-dB bandwidth) RF amplifier and applied to the EAM through a GSG RF probe. The swing voltage at the probe was 0.5 and 0.4 V at 400 and 448 Gbps, respectively. The fiber-coupled output under modulation was -3.7 dBm at a laser injection current of 43 mA, corresponding to a laser power consumption of 93 mW. In the present experimental setup, the modulated optical signal was amplified by a praseodymium-doped fiber amplifier (PDFA) prior to detection. The received waveform was captured by a sampling oscilloscope through a high-speed OE converter with a 120-GHz 3-dB bandwidth and feed-forward equalization (FFE). Figure 3(a) shows the measured TDECQ as a function of symbol rate using a 21-tap FFE, where the target symbol error rate (SER) is $9 . 3 \times 1 0 ^ { - 3 }$ . The TDECQ is below 4 dB at 180 Gbaud and 4.7 dB at 200 Gbaud. Even when the FFE is reduced to 15 taps, the TDECQ at 200 Gbaud remains 4.7 dB. In comparison, Ref. [4] reported 5 dB at 175 Gbaud, indicating improved performance at higher symbol rates and successful extension to 200 Gbaud operation in this work. Figures 3(b–e) and 3(f–i) show the eye diagrams of all four channels at 400 Gbps and 448 Gbps, respectively, measured sequentially using a 21-tap FFE at $5 5 ^ { \circ } C$ . Extinction ratios exceed 3.0 dB, and TDECQ values below 6.4 dB were confirmed for all channels at 400 Gbps. At 448 Gbps, eye openings were obtained with extinction ratios exceeding 2.7 dB; however, the signal quality was insufficient for reliable TDECQ evaluation, due to the limited output swing. Integrating four 400-Gbps channels within a 0.5-mm device width results in a shoreline density of 3.2 Tbps/mm. Based on the measured laser power consumption, the laser energy cost is calculated to be 0.12 pJ/bit. To ensure sufficient optical input power at the receiver, on-chip optical amplification using a SOA is required. We have previously demonstrated that a membrane SOA provides 8 dB gain with a bias current of 10 mA for an input power of −3 dBm [7]. Therefore, even if additional gain is required, the overall optical link can maintain low total power consumption.

![](/img/mineru_output/Th4A.1/auto/images/52b5c26e86dbbab94c35ac3e91228254971e5c135d77b5e6ef83956e228f8017.jpg)

![](/img/mineru_output/Th4A.1/auto/images/117c9697aab239f5816510120f1482223e89192e88e15b54ecdc9c2dc47d3e76.jpg)  
Fig. 3. (a) Measured TDECQ versus symbol rate. (b–e) Eye diagrams at 400 Gbps and (f-i) at 448 Gbps (sequentially measured).

We further investigated inter-channel crosstalk under simultaneous operation. Figure 4(a-d) compares the measured 200-Gbaud NRZ and PAM4 performance under single-channel driving and simultaneous dual-channel driving. Since the FDIU provides only a single output channel per four outputs of the AWG, the simultaneousdriving measurements were carried out using the AWG without the FDIU. Simultaneous driving was implemented using a GSGSG RF probe for two adjacent EAMs. For NRZ without equalization, the SNR remains 3.1 dB for both single and simultaneous driving. For PAM4, TDECQ increases only slightly from 6.1 dB (single-channel driving) to 6.4 dB (simultaneous driving). The TDECQ exhibits degradation compared to the result obtained with the FDIU because the FDIU improves the high-frequency response of the electrical signal. Figure 4(e) shows the crosstalk evaluated from the E–O response of Ch2 under two conditions: (i) an RF signal with DC bias applied to Ch2 and (ii) an RF applied to adjacent Ch1 while Ch2 was DC-biased. The difference between these responses quantifies the inter-channel crosstalk. The measured crosstalk is approximately −20 dB at 80 GHz and −10 dB at 110 GHz. Crosstalk can be mitigated by laterally shifting the EAM positions to increase the spacing between adjacent EAMs without increasing the device width. Therefore, further reduction of crosstalk is expected without compromising the shoreline density.

![](/img/mineru_output/Th4A.1/auto/images/6e6045daead77fdbff438013269cd561908eae753c8b35d732ce1923cfcb520c.jpg)

![](/img/mineru_output/Th4A.1/auto/images/5713bbab24cbe7bdc2c0111434fd8d9b783cea2bcb4da0b5ed88696211850113.jpg)

![](/img/mineru_output/Th4A.1/auto/images/c1e52c5ea1578dcf5faf6e1aee088969071d7859baac3726a18e71ea65144359.jpg)  
Fig. 4. (a-d) Comparison of 200-Gbaud NRZ and PAM4 performance under single-channel and simultaneous dual-channel driving of adjacent EAMs. (e) Measured inter-channel crosstalk extracted from the small-signal E-O response.

## 4. Conclusion

We demonstrated an O-band PIC consisting of membrane III–V EAMs, DFB lasers, and Si/SiOx waveguides on a Si photonics platform. A 100-µm-long membrane EAM achieved a 3-dB E-O bandwidth of 103 GHz and enabled 400- Gbps PAM4 operation with a 0.5-V swing. By densely integrating four channels on a single PIC, 400-Gbps PAM4 operation was achieved across all channels, resulting in a shoreline density of 3.2 Tbps/mm. These results highlight the potential of membrane III–V/Si photonics for scalable, bandwidth-dense, and energy-efficient optical interconnects.

## 5. Acknowledgement:

This paper is partly based on results obtained from the project, “Research and Development Project of the Enhanced Infrastructures for Post-5G Information and Communication Systems” (JPNP20017), commissioned by the New Energy and Industrial Technology Development Organization (NEDO).

## 6. References

[1] C. Han et al., “Exploring 400 Gbps/λ and beyond with AI-accelerated silicon photonic slow-light technology,” Nat. Commun., vol. 16, 2025.

[2] C. Bruynsteen et al., “110 GHz GeSi Electroabsorption Modulator on a 300mm SiPh Platform Enabling High-Density 400G/lane IM/DO Links,” in 51st European Conference on Optical Communications (ECOC), Th.03.01.4, 2025.

[3] A. Ostrovskis., “Heterogeneously Integrated InP Electro-Absorption Modulator for Beyond 300 Gb/s Optical Links,” Journal of Lightwave Technology vol. 43, 4, pp. 1826-1836, 2025.

[4] S. Okuda et al., “High-speed 340 Gbps PAM4 and 450 Gbps PAM6 Operations of Narrow High-Mesa EML,” in Optical Fiber Communication Conference (OFC) 2025, paper Tu2J, 2025.

[5] T. Hiraki et al., “Over-67-GHz-Bandwidth Membrane InGaAlAs Electro-Absorption Modulator Integrated With DFB Laser on Si Platform,” Journal of Lightwave Technology vol. 41, 3, pp. 880-887, 2023.

[6] W. Kobayashi et al., “Novel approach for chirp and output power compensation applied to a 40-Gbit/s EADFB laser integrated with a short SOA,” OpEx, vol. 23, 7, pp. 9533-9542, 2015.

[7] Y. Maeda et al., “Micro-Transfer-Printed InP-Based Membrane Photonic Devices on Thin-Film Lithium Niobate Platform,” Journal of Lightwave Technology vol. 42, 11, pp. 4023-4030, 2024.