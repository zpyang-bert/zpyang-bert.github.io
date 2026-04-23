---
layout: post
title:      "Driver-less 448 Gbps PAM4 and 1.2 Tbps 16-QAM IMDD/Coherent-lite transmission using TFLN optical DACs"
date:       2026-04-18 12:42:30
author:     "Bert"
tags:
  - Mineru
---
Charles St-Arnault1, Benton Qiu1, Derek Kita2, Kenton Anzai3, Christopher R. Cole2, Ross Dickson3, Bruce Beggs3, Naim Ben-Hamida3, Christian Reimer2 and David V. Plant1

1 Dept. of Electrical and Computer Engineering, McGill University, Montreal, QC, Canada 2 HyperLight Corporation, Cambridge, MA, USA 3 Ciena Corporation, Ottawa, ON, Canada charles.st-arnault@mail.mcgill.ca

Abstract: We report the highest achieved driver-less optical DAC transmission for IM/DD and Coherent with 448 Gbps PAM4 at 2 km and 1.2 Tbps 16-QAM at 10 km driven directly from CMOS logic gates. © 2026 The Author(s)

## 1. Introduction

The Ethernet roadmap is accelerating, driven by hyperscale AI systems that require scalable DCI transceivers with higher throughput at low power and latency. As a result, next-generation DCIs are increasingly limited by DAC/ADC bandwidth rather than the electro-optic devices, with the DAC often the tighter transmitter bottleneck. Recent attempts at increasing electronic DAC (eDAC) bandwidths have relied on frequency-domain interleaving with external multiplexers [1, 2]. However, these frequency interleaved approaches add complexity and power consumption and are not implemented in a CMOS process. This motivates CMOS-compatible transmitter architectures that deliver higher effective DAC bandwidth and throughput without external multiplexing, while reducing power and latency. In optical systems, the eDAC has three roles: (1) turning DSP-generated signals into multi-bit waveforms, (2) resampling the symbol stream to set the baud rate, and (3) mapping bits into multilevel formats (e.g., PAM4, 16-QAM). This raises the question: what if we removed transmitter DSP and the multi-bit eDAC? In advanced CMOS ASICs, logic gates can switch faster than practical eDAC bandwidths and naturally produce ∼0.7 V levels. In a “logic-driven” transmitter, digital pre-emphasis is unnecessary, pulse shaping can be handled by an analog filter, and the eDAC sampling rate is effectively replaced by clocked switching of binary logic gates. The remaining challenge is architectural: combining multiple binary gate outputs to synthesize the multilevel waveforms needed for formats like PAM4. This can be achieved using an optical DAC (oDAC) transmitter architecture. The objective of this work is to demonstrate the benefits of eliminating the eDAC and the associated transmitter-side DSP.

Using a thin-film lithium niobate (TFLN) binary-weighted Mach–Zehnder modulator (BW-MZM) oDAC architecture, we simplify the transmitter and drastically reduce component count, system complexity, and power consumption, enabling the first driver-less, logic-gate driven IM/DD and Coherent-lite demonstrations with no transmitter-side DSP. With this approach, we achieve the first optically generated 448 Gbps PAM4 at 2 km and 1.2 Tbps dual-polarization (DP) 16-QAM at 10 km with minimal measured implementation penalties. To the best of our knowledge, these demonstrations constitute the first driver-less oDAC implementations and deliver the highest oDAC data rates to date. Based on published DCI power consumption breakdowns [3, 4], eliminating the eDAC, Tx DSP, and RF drivers removes three of the dominant transmitter power consuming blocks, yielding substantial transceiver power reductions of ∼23% for Coherent and ∼30% for IM/DD, even under conservative assumptions.

## 2. Optical DAC Architecture

Optical DAC transmitters typically use segmented MZMs (SE-MZMs), where each segment encodes one bit and binary weighting is set by segment length [5–8]. However, SE-MZMs have a footprint that scales with bit count and, critically, do not ease drive requirements; the effective $V _ { \pi L }$ remains comparable to a push-pull MZM. We instead propose a parallel binary-weighted MZM (BW-MZM) on TFLN where the two MZM arms are driven independently by different differential logic-level signals. This dual-arm actuation combines binary lanes into multi-level outputs while remaining compatible with direct-drive voltages from a CMOS logic gate. BW-MZMs naturally support a local differential electrode pair $( S ^ { + } / S ^ { - } )$ per waveguide, enabling smaller electrode gap around the waveguide. This provides higher RF field intensity and waveguide overlap, reducing the intrinsic $V _ { \pi } L$ product relative to typical GSSG push-pull implementations. Moreover, native differential signaling on TFLN requires nonstandard electrode layouts (e.g., semi-differential designs) due to limited control over the crystal axis orientation; our architecture is directly compatible with differential drive on TFLN. The improved $V _ { \pi } L$ together with phase contributions from both arms relaxes the required drive voltage and enables the modulator to operate driver-less. Finally, BW-MZM allows binary inputs to be physically co-located and aligned on the PIC, eliminating the need for precise electrical delay tuning between segments that SE-MZM approaches require. The working principles of the BW-MZM and BW-IQM are shown in Fig. 1 (a). The intensity-modulated BW-MZM produces an output field where the amplitude depends on $( V _ { 1 } - V _ { 2 } ) / 2$ To create four amplitude levels from two binary signals, we apply a binary-weighted drive such that the effective MSB contribution is double the LSB contribution; $V _ { 1 } = 2 V _ { 2 }$ . Higher-order formats follow from alternative weightings (e.g., PAM6 with 3-level $V _ { 1 }$ and 2-level V2). BW-MZMs exhibit a residual phase term proportional to $( V _ { 1 } + V _ { 2 } ) / 2$ that creates chirp, causing pulse shortening or broadening in the presence of chromatic dispersion (CD). Operating in the O-band near the ∼1310 nm zero-dispersion wavelength of standard SMF minimizes the impacts of chirp. At this wavelength, we demonstrate 448 Gbps PAM4 transmission over distances of 2 km, consistent with DR8-2-class reach. For the Coherent BW-IQM, under standard IQM biasing, the phase term that is common to both arms does not translate into residual intensity chirp at the output, enabling chirp-less Coherent modulation.

![](/img/mineru_output/Th4B.2/auto/images/734bb57670493422e41c1d9f877fdfb7c7a5fadca4e957b410434162df2c514f.jpg)  
Fig. 1: (a) Architecture of the binary weighted-MZM (BW-MZM) and binary weighted-IQM (BW-IQM) oDAC. OOK signals are combined optically to generate PAM4 or 16-QAM. (b) IM/DD experimental setup. A 3 nm CMOS electronic DAC is used at 1-bit resolution to emulate a logic gate. The two logic gate outputs directly drives a TFLN oDAC with 600 mV differential to optically generate a PAM4-6-8 signal. (c) Coherent experimental setup. A BW-IQM is used instead with 4 emulated logic gates to optically generate a 16-32-64-QAM signal.

## 3. Experimental setup

Fig. 1 (b)-(c) show the experimental setup and DSP stacks used in the IM/DD and Coherent-lite experiments. We emulate a CMOS logic gate output by operating a 3 nm CMOS 7-bit eDAC at effectively 1-bit resolution. The use of emulated logic gates removes the possibility to use transmitter side DSP. We send the binary streams to the logic gate output (2 gates for IM/DD, 4 for Coherent-lite). This emulated logic gate has a 6 dB bandwidth of 110 GHz and a differential output voltage of 600 mV. To perform binary weighting of the drive signals, the MSB signal (V1) turns on all 7 eDAC bits at once to represent a 1 or all off to represent a 0, while the LSB (V2) signal uses the first 6 LSB only, applying the $V _ { 1 } = 2 V _ { 2 }$ condition while retaining in essence the 1-bit resolution required to emulate a logic gate with binary weighting. This weighting could instead be done optically by shortening the LSB electrode. PAM6-8 signals are generated with more electrical levels (PAM6, 3-V1 and 2-V2; PAM8, 3-V1and 3-V2). The drive signals from the logic gate outputs are applied to the TFLN BW oDACs using a RF probe. The BW oDACs have a simulated 6 dB bandwidth well exceeding 100 GHz and a low-MHz differential $V _ { \pi }$ of 2.2V. A 20 dBm quantum-dot (QD) DFB laser set at 1310 nm generates the optical carrier. The modulated PAM signal travels through 500 m or 2 km of SMF, is detected by a 110 GHz photodiode (PD) and sampled by a 113 GHz real-time oscilloscope (RTO). We synchronize the received signal, apply 51 taps of T-spaced FFE with 11 taps of DFE and perform hard-decisions using a 1-tap MLSE and calculate BER. The Coherent-lite demonstration employs a BW-IQM with 4 emulated logic gate outputs. The same transmitter laser is used. The single polarization BW-IQM output is fed into a dual polarization (DP) emulator. The DP Coherent signal is amplified by a PDFA and travels through 500 m, 10 km or 20 km of SMF. The oDAC generated DP-QAM signal enters a $2 \times 8$ optical hybrid with a QD DFB local oscillator (LO) operated at 20 dBm. Four 70 GHz balanced PDs convert the optical signals to electrical. The signal is sampled by a 113 GHz RTO. These 70 GHz balanced PDs form the main bottleneck in this system; all other components in the system have bandwidths exceeding 100 GHz. We then deskew the IQ signal, resample to 2 samples per symbol and correct the frequency offset between carrier and LO. A 4×4 MIMO equalizer with real valued coefficients is used to compensate for linear distortion and phase noise as well as the balanced PD’s limiting 70 GHz of bandwidth. The recovered symbols are then used to count the BER. In the results section, we compare the oDAC to a typical push-pull MZM or IQM implementation. In order to make a just comparison, we employ the same BW-MZM or BW-IQM in both approaches. For the push-pull approach, we drive both arms with $V _ { 1 } = - \dot { V _ { 2 } }$ while employing a 7-bit eDAC, and adjust the modulated power to match that of the oDAC. This allows for an apples-to-apples comparison of performance, and importantly, an assessment of the implementation penalty of an oDAC for both IM/DD and Coherent.

## 4. Results and discussion

Fig. 2 (a)-(c) contain the Coherent BW-IQM oDAC results. The 16-QAM results (a) illustrate successful transmission of 800 Gbps (dual-polarization 125 Gbaud) under the 6.7% overhead HD-FEC (10 km) and c-FEC (20 km) BER limit and 1.2 Tbps (187.5 Gbaud) under the 25% SD-FEC limit at up to 10 km. At 800 Gbps, a small OSNR penalty of 0.34 dB is measured between the better performing push-pull IQM implementation and the oDAC. This 800 Gbps 16-QAM result indicates performance in line with current O-band Coherent 800G-LR1 signaling and BER targets [9] while operating with significantly reduced power consumption. The OSNR penalty is reduced at 1.2 Tbps to 0.25 dB. In our testbed, transmission performance beyond 150 Gbaud is greatly limited by the 70 GHz bandwidth limit of our balanced PDs. The 32-QAM results (b) show net transmission of 1.2 Tbps at 150 Gbaud under the 25% SD-FEC BER limit with an OSNR penalty of 0.6 dB compared to a traditional push-pull IQM. Fig 2 (d)-(e)-(f) show the oDAC constellations of the DP-16-QAM 800 Gbps and 1.2 Tbps achieved with DP-16-QAM at 10 km and 32-QAM at 500 m. The constellations are symmetric, highlighting clear transmission linearity. Fig. 2 (g) shows an eye diagram at 2 km of 225 Gbaud PAM4 transmission with a BER well under the 6.7% overhead HD-FEC limit. The driver-less logic gate drive is enough to achieve 3.76 dB of extinction ratio (ER), a value above the 200G IEEE standard minimum ER spec. The PAM4 results, shown in (h), indicate no performance difference between a back-to-back (B2B) and 2 km transmission. We highlighted previously that the IM/DD BW-MZM signal is chirped. For parallel-fiber architectures (e.g., DR8), where the laser is centered around the zero dispersion wavelength of SMF, this chirp shows no measurable performance drawback at 2 km. At 225 Gbaud PAM4, all three distances are well below the HD-FEC limit enabling net 421 Gbps PAM4 transmission. At 225 Gbaud PAM4, the received optical power (ROP) penalty for employing the oDAC is 0.4 dB. For PAM6 (i), all three distances perform similarly and net 410 Gbps is achieved using 175 Gbaud PAM6 at 2 km. PAM8 (j) also shows limited variations between all distances. At 162.5 Gbaud PAM8, net 425 Gbps is achieved under the c-FEC BER limit. With 225 Gbaud PAM8, net 540 Gbps is achieved under the 25% SD-FEC limit. While the modulation format for the next generation of DCIs has not been settled yet, we show that this oDAC-enabled, power and complexity saving architecture, can transmit either 4, 6 or 8 amplitude levels at the symbol rates required for 400G lanes. From published DCI power breakdowns [3, 4], removing the eDAC, Tx DSP, and RF drivers is expected to reduce total transceiver power by ∼23% for Coherent-lite and ∼30% for IM/DD.

![](/img/mineru_output/Th4B.2/auto/images/2c7ac7a4682a37c57559c8e6020274978e2b3ca235128259b0e35c188d8ce966.jpg)

![](/img/mineru_output/Th4B.2/auto/images/c0957b031d1a711b0ac851a5506eeeb42834a87600354bba8ec6a3aba5ef8acf.jpg)

![](/img/mineru_output/Th4B.2/auto/images/09197d4a190cb69b4e7a115c5faa69f616332b75ccc3df7aff58432381a36a19.jpg)

![](/img/mineru_output/Th4B.2/auto/images/826cd2c5fddab6e587fb3dd55cd80b59b8ee10d53ffec101bd56ff19ed04bd7f.jpg)

![](/img/mineru_output/Th4B.2/auto/images/37adae4ec38d8b1053c9df7ce870d4cca24269dfa5c0a77e380398effdc47816.jpg)

![](/img/mineru_output/Th4B.2/auto/images/e4271b7ac02df61e6332f1a6ff4bf6643cb22c5a4332499462377417bf1dc91d.jpg)

![](/img/mineru_output/Th4B.2/auto/images/485ffbc2e1204761b8717954423331a339bceb5f985c45dc6c4908835d4c5dad.jpg)

![](/img/mineru_output/Th4B.2/auto/images/a364ca8a2f368fc3605451a8878016bb3216f01d7dd95934e8079b031a82ac2d.jpg)

![](/img/mineru_output/Th4B.2/auto/images/37e297874c5c8ed43c0eafe4b39be78a7a177d6e39bedb7e52528695fa689f84.jpg)

![](/img/mineru_output/Th4B.2/auto/images/7f876682c871647f0de7f266bd492594c1d72fd91437abbb3fe319a7cae67f84.jpg)  
Fig. 2: (a)-(c) oDAC generated 16-32-64-QAM vs push-pull IQM at 500 m, 10 and 20 km. (d)–(e) oDAC-generated DP-16-QAM constellations at 10 km (net 800 Gbps and 1.2 Tbps). (f) DP-32-QAM constellation at 500 m (net 1.2 Tbps). (g) Measured optical eye diagram of driver-less oDAC 448 Gbps PAM4 at 2 km. (h)-(j) oDAC generated PAM4-6-8 vs push-pull MZM at B2B, 500 m and 2 km.

## 5. Conclusion

We demonstrate the first driver-less, logic-gate-driven oDAC transmitter without Tx DSP or an eDAC for IM/DD and Coherent-lite, achieving 448 Gbps PAM4 (2 km) and 1.2 Tbps DP-16-QAM (10 km) with significant power reductions and negligible implementation penalties.

## References

1. C. Deakin et al., OFC2025, Th4B.7, (2025).

2. Keysight et al., Press release: 448 Gbps data transmission benchmark, (Apr. 2, 2025).

3. X. Ye and S. J. Savory, J. Lightw. Technol., vol. 43, no. 13, pp. 6017–6028, (2025).

4. F. Chang et al., IEEE P802.3df, chang 3df 01 2211, (Nov. 2022).

5. D. Patel et al., IEEE Photonics Technol. Lett., vol. 27, no. 23, pp. 2433– 2436, 2015.

6. A. Aimone et al., OFC2016, Th5C.6, (2016).

7. Z. Zheng et al., J. Light. Technol., vol. 40, no. 16, pp. 5457–5466, 2022.

8. S. Sygletos et al., IPC2024, MD1.3, (2024).

9. E. Maniloff et al., IEEE P802.3dj, maniloff 3dj 01 2507, (Jul. 2025).