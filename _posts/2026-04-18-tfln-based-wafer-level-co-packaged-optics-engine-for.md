---
layout: post
title:      "TFLN-based Wafer-Level Co-Packaged Optics Engine for Ultrahigh-Bandwidth Electro-Optical Modulation"
date:       2026-04-18 16:15:32
author:     "Bert"
tags:
  - Mineru
---
Yinshan Huang,1† Long Wang,1,2† Mingxuan Li,1 Ding Yan,2 Shuai Yuan,3 Guiling Wu,2 and Liang Zhou1

1State Key Laboratory of Radio Frequency Heterogeneous Integration, School of Integrated Circuit, Shanghai Jiao Tong University, Shanghai 200240, China

2State Key Laboratory of Photonics and Communications, School of Integrated Circuit, Shanghai Jiao Tong University, Shanghai 200240, China 3Wuhan ANPI Optoelectronics Co., Ltd, Wuhan 430202, China

†These authors contributed equally, Corresponding author: Guiling Wu, Liang Zhou (wuguiling@sjtu.edu.cn, liangzhou@sjtu.edu.cn)

Abstract: We heterogeneously integrate the TFLN EOM chip and its driving EICs, yielding a TFLN-based CPO engine with bandwidth over 100 GHz. Utilizing this engine, a time/frequency comparison with an unprecedented femtosecond-level precision is further demonstrated.

## 1. Introduction

Lithium niobate, benefiting its strong Pockels effect, has long been an important material for high-performance electro-optical (EO) modulation. The recent advent of thin-film lithium niobate (TFLN) has further transformed this field by bringing several outstanding material properties onto a chip-scale photonic integrated circuit platform. By tightly confining light in high-index-contrast waveguides, TFLN enables EO modulator (EOM) that simultaneously achieve low half-wave voltages (Vπ, below 3.5 V) and ultra-broadband operation (up to 110 GHz). This capability has accelerated progress in high-capacity optical communication (400 Gbps/lane) [1], optical frequency-comb (OFC) generation [2], quantum photonics [3], optical frequency division [4], and microwave-photonic [5].

However, the practical deployment of TFLN for high-bandwidth EO modulation is critically hindered by the packaging-induced performance degradation: (1) In most system-level high-bandwidth demonstrations, the TFLN chips are the only integrated component. The driving electronic devices, including the radio frequency (RF) multiplier, the low-noise amplifier (LNA), and the high-bandwidth power amplifier (PA), usually rely on discrete, bulky, and tabletop elements or equipment [5,6], thereby undermining the benefits of integrated photonics and even being limited to laboratory demonstrations. (2) Furthermore, when the bandwidth is over 70 GHz, if the approach of discrete board-level or module-level "loose interconnection" is still adopted, the long-distance interconnects and multi-stage electrical-optical interfaces inevitably introduce parasitic capacitance, inductance, and reflection discontinuities. These effects significantly compress the effective bandwidth and modulation efficiency of the TFLN modulator. In previous demonstrations, as much as 30 GHz of bandwidth was sacrificed after packaging, as illustrated in Fig. 1(e).

Here, to the best of our knowledge, we report the first demonstration of wafer-level heterogeneously integrated TFLN-based co-packaged optics (CPO) engine that co-packages the TFLN EOM with its driving electronic chips, providing an integrated solution for ultrahigh-bandwidth EO modulation. The proposed packaging and interconnect architecture is theoretically capable of supporting bandwidth beyond 200 GHz. Using a 110-GHz TFLN chip, we realize a 100-GHz TFLN-based CPO engine. Leveraging this engine, a high-precision time/frequency metrology application is conducted, and an unprecedented femtosecond-level precision is achieved.

## 2. Device Fabrication and Performance Evaluation

Figure 1 illustrates the wafer-level optoelectronic heterogeneous integration process. A 4-inch, 1-mm-thick highresistivity (＞4000 ohm·cm) silicon wafer is selected as the interposer substrate, and 300 nm Si₃N₄ thin films are deposited on both sides of the silicon wafer. Prior to fabrication, the three-dimensional geometries of the photonic (TFLN EOM) and electronic chips (CMOS SoC, GaN PA and InP LNA) are precisely measured, and a corresponding chromium photomask is designed. The integration process mainly contains the following six steps:

Step1: The wet-etch mask is first defined to remove the Si₃N₄ thin films at the designated locations, and the silicon wafer is then immersed in a KOH solution to perform anisotropic wet etching.

Step2: The dry etching technique is adopted to create cavities precisely matched to the chip dimensions. This approach enables compact gap filling and maintains an alignment accuracy better than ±5 μm.

Step3: Cr/Cu seed layers (30 nm/300 nm) are sputtered onto the wafer surface, followed by electroplating a 4 μmthick copper layer to form a continuous ground network electrically isolated from the high-resistivity silicon.

Step4: The chips are mounted into the etched cavities using conductive silver paste, which also fills the remaining gaps between the chips and the silicon-based interposer.

Step5: A 12 μm-thick photosensitive BCB film is then spin-coated onto the reconstructed silicon wafer. After exposure and development in DS3000, the I/O pads and electrode regions of the TFLN EOM are exposed. The wafer is subsequently hard-cured in a nitrogen oven to ensure mechanical stability and dielectric reliability.

Step6: Cr/Cu seed layers (15 nm/150 nm) are sputtered again, and a 12 μm photoresist (AZ-4903) is spin-coated and patterned. Electroplating of 3 μm-thick copper and 1 μm-thick gold is then performed sequentially. After photoresist removal, ion-beam etching is used to strip the residual seed layer, completing the inter-chip interconnects and fan-out redistribution structures.

Finally, the wafer is diced to yield individual integrated optoelectronic assemblies. The optical facets of the chips are polished, followed by the mounting of RF decoupling capacitors and the attachment of coupling fibers. This completes the wafer-level optoelectronic heterogeneous integration process, ultimately realizing the TFLN-based CPO engine, as shown in Fig. 1(b). Figure 1(c) presents the measured performance of the TFLN EOM before and after packaging. Before packaging, the EOM exhibits a 3-dB electro-optic bandwidth of 110 GHz. After packaging, the measured 3-dB electro-optic bandwidth consistently remains above 100 GHz, while the RF return loss (S11) stays below −10 dB up to 100 GHz. In addition, the packaged EOM shows a low optical insertion loss of less than 4.2 dB and a Vπ of 4 V. These results confirm the low-loss integration capability of the proposed wafer-level optoelectronic heterogeneous integration process. Furthermore, Figure 1(d) illustrates the simulated high-frequency performance of the packaging structure. The simulation indicates a 3-dB bandwidth of over 200 GHz, with an interconnection loss of less than 0.5 dB at 100 GHz, indicating that the proposed architecture can support packaged EOM bandwidths beyond 200 GHz when packaged with a higher-intrinsic-bandwidth EOM. Figure 1(e) compares the bandwidths of different TFLN EOMs before and after packaging. It can be observed that the proposed approach preserves the bandwidth most effectively, yielding post-packaging performance closest to the unpackaged EOM response. In addition, the proposed process enables chip-scale optoelectronic high-density integration, which provides a promising and scalable packaging solution for ultra-broadband EO modulation and CPO.

![](/img/mineru_output/Th4A.6/auto/images/e35a7aa8b96022f9dde14a4a729457a184cd05cf7dfbcdb86175887ce16afba5.jpg)

![](/img/mineru_output/Th4A.6/auto/images/4251aae51d9eb50dd34c46cd6f77e8613b8de1d7e1cb6186968a9f4d0754d15c.jpg)

![](/img/mineru_output/Th4A.6/auto/images/5fce2afc1cfdc5113d03216bf7d2a36295832a33de4bff5c5f653ae78aa7613a.jpg)

![](/img/mineru_output/Th4A.6/auto/images/7b2727e1ef7371e56b2f837fdd0934aa60affb67d0e1dc5dedd7fa82798e43fc.jpg)  
Fig. 1 (a) Wafer-level optoelectronic heterogeneous integration process. PIC: Photonic Integrated Circuit, EIC: Electronic Integrated Circuit. (b) Photograph of the TFLN-based CPO engine. (c) Measured result of TFLN EOM before and after packaging. (d) Simulated results of the packaging structure. (e) Bandwidth comparison of reported TFLN EOMs (Bandwidth for Ref. [7] is defined by a 1-dB metric).

## 3. High-precision time/frequency comparison utilizing the TFLN-based CPO engine

In the field of time and frequency metrology, higher operating frequency or broader bandwidth can typically enable greater precision. Leveraging the partial function of the TFLN-based CPO engine, we conduct a fiber-optic time/frequency (T/F) comparison experiment, as illustrated in Fig. 2. The underlying principle is based on the twoway comparison method, similar to that described in our previous work [11]. The key distinction lies in the increase of the modulation frequency from 60 MHz to 94 GHz. As established in [12], a higher modulation frequency leads to improved T/F demodulation precision, thereby enabling high-precision T/F comparison.

Figure 2(a) depicts the EO modulation setup driven by an atomic clock. The outputs of the laser source and the radio frequency (RF) source are injected into the co-packaged TFLN engine. The $\mathrm { R } \dot { \mathrm { F } }$ source operates at 11.75 GHz, and the laser wavelength is set to 1550.12 nm (C34 channel). The RF signal is subsequently multiplied to 94 GHz, amplified to 24 dBm by the EICs, and modulated onto the optical carrier. This process generates an optically carried T/F signal, whose optical spectrum is shown in the inset of Fig. 2(b), presenting a high EO modulation efficiency.

Figure 2(b) illustrates the experimental configuration for conducting T/F comparison. At both the local and remote sites, the optically carried T/F signal is split into two branches. One branch serves as the local oscillator (LO) for coherent detection, while the other is launched into the fiber link and transmitted to the opposite site. To mitigate the effects of Rayleigh backscattering, two acousto-optic modulators (AOMs) are employed. After coherent detection, a digital frequency-domain phase demodulation algorithm is used to obtain the TF difference [11].

By utilizing the high-frequency 94 GHz signal, the stability of the T/F comparison is significantly enhanced. As shown in Fig. 2(c), an unprecedented femtosecond-level precision is achieved. The time deviation at 1-s averaging time is about 0.8 fs. Previously, this level of precision was achievable only with advanced optical frequency combs [18], which, however, suffer from large size, weight, and power (SWaP). In contrast, our system leverages the copackaged TFLN engine, offering a compact, low-SWaP solution. The frequency stability is presented in Fig. 2(d), with a MDEV of $1 \bar { . 2 } \times 1 0 ^ { - 1 5 }$ at 1 s averaging time. Figure 2(e) provides a comparison with state-of-the-art systems. Alongside enhanced integration, the system exhibits a marked improvement in overall performance.

![](/img/mineru_output/Th4A.6/auto/images/f34d7b74102ed2f901b9a6f0e37f409173f37a0a96073c3245c2b3e1cbf35113.jpg)

![](/img/mineru_output/Th4A.6/auto/images/087d7b6c6cfc14d9e7c4402d6617fc70e273a57d13de8a7b1bcd1d31d3cde17c.jpg)

![](/img/mineru_output/Th4A.6/auto/images/5e41425a4e76a25df25c545df0cc7baa6c767eba6f163eba5f5abb33c7a5adec.jpg)

![](/img/mineru_output/Th4A.6/auto/images/296decd8b930f17274135510b8d60e9c189c7bf83b593df0c95fc1ed4c557c96.jpg)

![](/img/mineru_output/Th4A.6/auto/images/dc54780f3b6ff33ebffe46fad108c5d2a32f3ca615b5ce528021b4bbfd87f613.jpg)

![](/img/mineru_output/Th4A.6/auto/images/db55c8ea300ecc625c7a0067fc8801dc3cc9622b18fff4abaf4a6d886eb79c1b.jpg)

![](/img/mineru_output/Th4A.6/auto/images/8d03559a0a3c715fd0eb35d2e69dc1e162b792ae5a927d6382ed1d51f14b5112.jpg)  
Fig. 2 (a) Schematic diagram of the high-frequency EO modulation realized by the TFLN-based CPO engine. (b) Scheme of conducting the fiber-optic time and frequency comparison. (c) and (d) are the achieved time and frequency stability, respectively. (e) Comparison between our work and the prior arts.

## 4. Conclusion and future outlook

In summary, we demonstrate the wafer-level heterogeneous integration of photonic TFLN EOM chip with its driving EICs, yielding a CPO engine with a bandwidth of 100 GHz. This engine features high bandwidth, high integrity, and high EO modulation efficiency. Then, a T/F comparison with fs-level precision is demonstrated.

Future works can be conducted in the followings: First, the proposed wafer-level heterogeneous integration method can be extended to develop a 200-GHz CPO engine when using a higher-bandwidth TFLN EOM, as indicated in Fig. 1(d). This would provide a packaging method toward future higher-capacity optical communication, such as 800 Gbps/lane. Second, other PICs, including the lithium-tantalate modulators [19] and UTC-PDs [20], can be heterogeneously integrated to realize more functionalities. Third, as illustrated in Fig. 2(a), the RF signals processed by the EICs can also be radiated into the free space, enabling simultaneous communication and sensing in both the optical and radio-frequency domain. This paves the way toward multifunctional optoelectronic microsystems.

## References:

[1] Y. He et al., JLT, 43, 10210–10217 (2025).

[2] M. Yu et al., Nature, 612, 252–258 (2022).

[3] J. Li et al., JQE, 60, 5200109 (2024).

[4] Y. He et al., Sci. Adv., 10, eado9570 (2024).

[5] S. Zhu et al., Nat. Photon., 19, 204–211 (2025).

[6] Z. Tao et al., Nature, 645, 80-87 (2025)

[7] Y. Yamaguchi et al., OFC2025-PDP, Th4D.4 (2025).

[8] T. Li et al., Chin. Opt. Lett., 22, 092201 (2024).

[9] Y. Liu et al., Light: Adv. Manuf., 6, 47 (2025).

[10] J. Li et al., JQE, 60, 5200109 (2024).

[11] C. Liu et al., OFC2025-PDP, Th4A.4 (2025).

[12] L. Wang et al., IEEE CCPQT, 66408 (2025)

[13] X. Guo et al., Chin. Phys. Lett., 41(6), 064202 (2024).

[14] F. Zuo et al., JLT, 39(20), 6373–6380 (2021).

[15] Y. He et al., Optica, 5(2), 138–146 (2018).

[16] D. Yu et al., Phys. Rev. Res., 6, 023005 (2024).

[17] A. Abuduweili et al., Opt. Express, 28(26), 39400–39412 (2020).

[18] E. Caldwell et al., Nature, 618, 721-726 (2023).

[18] C. Wang et al., Nature, 629, 784-790 (2024).

[19] L. Li et al., Nat. Photon., 19, 1301–1308 (2025).