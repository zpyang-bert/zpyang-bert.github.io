---
layout: post
title:      "Advanced Digital Signal Processing in Coherent Fiber Optic Communication Systems"
date:       2026-04-18 16:41:29
author:     "Bert"
tags:
  - DSP
  - Mineru
---
Mahdi Malekiha

![](/img/mineru_output/Advanced_DSP_Coherent_Fiber_Optic_Comms_Malekiha_McGill_24p/auto/images/5197e0728eaba6ff00b6d84b8de6682836309f88c38f6364f7023e3ae2e6f7f7.jpg)

Department of Electrical & Computer Engineering McGill University Montr´eal, Canada

August 2016

A thesis submitted to McGill University in partial fulfillment of the requirements for the degree of Doctor of Philosophy. © 2016 Mahdi Malekiha

## Abstract

To satisfy the explosive growth in global Internet traffic, the development of transmission links that not only have high-capacity but are also flexible, reconfigurable, and adaptive is imperative. The advents of high speed digital-to-analog and analog-to-digital converters, and recent progress in complementary metal–oxide–semiconductor (CMOS) technology has facilitated the development of optical transceivers relying on coherent detection and digital signal processing (DSP) for the compensation of fiber impairments. Next generation coherent optical networks are anticipated to further approach the Shannon limit and deliver 400 Gb/s or 1 Tb/s data rates per channel, while providing flexibility and agility to maximize the utilization of the network resources. This thesis explores novel system architectures and advanced DSP algorithms to fulfill these design targets.

Currently, chromatic dispersion (CD) compensation and forward error correction (FEC) decoders are the major power consuming (more than 50%) blocks of a conventional transceiver application-specific integrated circuit (ASIC). This thesis presents the concepts and architectures of multi-sub-band (MSB) signaling for mitigation of CD, and eliminating the need for a CD compensating equalizer in reduced-guard-interval (RGI) orthogonal frequency-division multiplexing (OFDM) and single carrier systems. The performance of the proposed techniques are experimentally evaluated using a leading-edge optical long-haul transmission test-bed. It is shown that the MSB technique, in addition to the evidently lower computational complexity, allows for a highly efficient adaptive rate smart transceiver implementation with lower system overhead and simplified parallelism, while attaining the same or better transmission reach and performance as the conventional transceiver. This is due to its higher tolerance to fiber nonlinearity.

With coherent technology and advanced FEC, it is known that the capacity of current

fiber optic transmission systems is fundamentally limited by fiber nonlinearities. We have optimized the perturbation based nonlinearity compensation (PB-NLC) equalization scheme and proposed a novel adaptive nonlinear equalizer. The performances of the aforementioned DSP equalization schemes are numerically and experimentally studied. It is found that the optimized technique demonstrates lower computational complexity over conventional PB-NLC. In addition, the proposed adaptive nonlinear equalizer does not require prior calculations of perturbation coefficients and detailed knowledge of the transmission link parameters. It achieves comparable performance to the PB-NLC. Unlike previously studied adaptive nonlinear equalization techniques, our algorithm takes advantage of common symmetries, avoids replication of operations, and only uses a few adaptive nonlinear coefficients. Finally, its computational complexity is smaller than previously proposed adaptive nonlinear equalization schemes, which meets the requirements of next generation optical networks.

## R´esum´e

Pour satisfaire la croissance explosive du trafic Internet mondial, le d´eveloppement des liaisons de transmission qui ont non seulement une grande capacit´e, mais qui sont aussi flexibles, reconfigurables, et adaptables est imp´eratif. L’avancement en vitesse des convertisseurs num´eriques-analogiques et analogiques-num´eriques, et les progr\`es r´ecents dans la technologie des semi-conducteurs compl´ementaires \`a l’oxyde de m´etal (CMOS) ont facilit´e le d´eveloppement d’´emetteurs-r´ecepteurs optiques utilisant la d´etection coh´erente et le traitement num´erique du signal (DSP) pour la compensation des d´et´eriorations de la fibre. Il est pr´evu que les r´eseaux optiques coh´erents de la prochaine g´en´eration approcheront la limite de Shannon en livrant des d´ebits de donn´ees de 400 Gb/s ou 1 Tb/s par canal, tout en offrant la flexibilit´e et l’agilit´e pour optimiser l’utilisation des ressources du r´eseau. Cette th\`ese explore de nouvelles architectures de syst\`emes et algorithmes DSP pour r´epondre \`a ces objectifs de conception.

Pr´esentement, la compensation pour la dispersion chromatique (CD) et la correction d’erreur directe (FEC) sont les principales consommatrices d’´energie (plus de 50%) des blocs d’un circuit int´egr´e sp´ecifique (ASIC) d’un ´emetteur-r´ecepteur. Cette th\`ese pr´esente les concepts et architectures de signalisation multi-sous-bande (MSB) pour diminuer l’effet de la CD et ´eliminer la n´ecessit´e d’un ´egaliseur CD dans les syst\`emes \`a garde-intervalle r´eduite (RGI) \`a multiplexage par r´epartition en fr´equence orthogonale (OFDM). La performance des techniques propos´ees est exp´erimentalement ´evalu´ee \`a l’aide d’un banc d’essai de transmission optique \`a longue distance. Il est d´emontr´e que la technique MSB, en plus de r´eduire la complexit´e de calcul, permet le traitement en parall\`ele et rend possible de r´ealiser un ´emetteur-r´ecepteur intelligent tr\`es efficace avec une faible surcharge. Tout cela en atteignant la mˆeme ou une meilleure port´ee de

transmission et de performance que l’´emetteur-r´ecepteur classique. Ceci est dˆu \`a sa plus grande tol´erance \`a la non-lin´earit´e de la fibre.

Avec la technologie coh´erente et FEC moderne, il est connu que la capacit´e des syst\`emes de transmission \`a fibre optique est essentiellement limit´ee par la non-lin´earit´e de la fibre. Nous avons optimis´e la technique de compensation de non-lin´earit´e \`a base de perturbation (PB-NLC) et propos´e un nouvel ´egaliseur de non-lin´earit´e adaptable. La performance de ces algorithmes DSP est num´eriquement et exp´erimentalement ´etudi´es. On d´emontre que la technique optimis´ee a une complexit´e de calcul plus faible que la PB-NLC classique. En outre, cet ´egaliseur non lin´eaire adaptable ne n´ecessite pas de g´en´eration.

## Acknowledgments

I would like to express my most sincere gratitude to my supervisor, Prof. David Plant, for his support, resources, advice, experience, and guidance in the completion of this work. I am grateful to him for believing in my research ideas and for providing the right environment to make them flourish. Moreover, I highly appreciate Prof. Plant’s dedication to his work, which has resulted in a laboratory with high-end equipment that is necessary to perform not only my research but also that of other students in the Photonic Systems Group. I would like to acknowledge Prof. Shiva Kumar for giving me my first opportunity as Patel, Mohamed Morsy-Osman, Qunbi Zhuge, Xian Xu, Mathieu Chagnon and everyone else that have helped me in various forms to realize this project. My deepest love and appreciation goes to my parents for their unconditional love, support, and patience during my entire life. They devoted their heart and soul to advance my education and encourage me to love learning and work hard. I dedicate this thesis to my wife Mehrnoosh. I would not be where I am if it was not for her love and perseverance. I feel considerably lucky for having her by my side throughout my graduate studies.

Mahdi Malekiha

May 2016

## Associated Publications

The content of this thesis is based on published journal papers and conference proceedings. A list of the publications that I have authored is provided below. The contribution of the co-authors is stated below each item for the journal and conference papers directly related to this thesis.

## Journal Articles Directly Related to This Thesis

[1] M. Malekiha, I. Tselniker, and D.V. Plant,“Efficient nonlinear equalizer for intra-channel nonlinearity compensation for next generation agile and dynamically reconfigurable optical networks,” Optics Express, vol. 24, no. 4, pp. 4097-4108, 2016.

I conceived the idea, performed the simulation and experiment, and wrote the paper. The co-authors contributed in editing the paper and discussing the idea.

[2] M. Malekiha, and D.V. Plant,“Adaptive Optimization of Quantized Perturbation Coefficients for Fiber Nonlinearity Compensation,” IEEE Photonic Journal, vol. 6, no. 3, pp. 1-7, 2016.

I conceived the idea, performed the simulation and experiment, and wrote the paper. The co-authors contributed in editing the paper and discussing the idea.

[3] M. Malekiha, I. Tselniker, and D.V. Plant, “Chromatic dispersion mitigation in long-haul fiber-optic communication networks by sub-band partitioning,” Optics Express, vol. 23, no. 20, pp. 32654-32663, 2015.

I conceived the idea, performed the simulation and experiment, and wrote the paper. The co-authors contributed in editing the paper and discussing the idea.

[4] M. Malekiha, I. Tselniker, M. Nazarathy, A. Tolmachev, and D.V. Plant, “Experimental demonstration of low-complexity fiber chromatic dispersion mitigation for reduced guard-interval OFDM coherent optical communication systems based on digital spectrum sub-band multiplexing,” Optics Express, vol. 23, no. 25, pp. 25608-25619, 2015. I conceived the idea, performed the simulation and experiment, and wrote the paper. The co-authors contributed in editing the paper and discussing the idea.

## Conference Proceedings Directly Related to This Thesis

[5] M. Malekiha, and D.V. Plant,“Complexity reduction of dispersion mitigation based on sub-band partitioning,” Photonics North, Paper F71S, 2016.

I conceived the idea, performed the simulation, and wrote the paper. The co-authors contributed in editing the paper and discussing the idea.

[6] M. Malekiha, and D.V. Plant,“Adaptive quantization of perturbation coefficients for nonlinearity compensation,” Photonics North, Paper J9K8, 2016.

I conceived the idea, performed the simulation and experiment, and wrote the paper. The co-authors contributed in editing the paper and discussing the idea.

## Journal Articles Not Directly Related to This Thesis

[7] X. Xu, Q. Zhuge, B. Chˆatelain, M. Chagnon, M. Morsy-Osman, M. Malekiha, M. Qiu, Y. Gao, W. Wang, and D.V. Plant, “Experimental investigation on the nonlinear tolerance of root M-shaped pulse in spectrally efficient coherent transmissions,” Optics Express, vol. 23, no. 2, pp. 31966-31982, 2015.

[8] L. Xiaojun, S. Kumar, J. Shao, M. Malekiha, and D.V. Plant. “Digital compensation of cross-phase modulation distortions using perturbation technique for dispersion-managed fiber-optic systems,” Optics Express, vol. 22, no. 17, pp. 20634-20645, 2014.

[9] A. Rhys, M. Spasojevic, M. Chagnon, M. Malekiha, J. Li, D.V. Plant, and L.R. Chen. “Wavelength conversion of 28 Gbaud 16-QAM signals based on four-wave mixing in a silicon nanowire,” Optics Express, vol. 22, no. 4, pp. 4083-4090, 2014.

[10] S.A. Nezamalhosseini, L.R. Chen, Q. Zhuge, M. Malekiha, F. Marvasti, and D.V. Plant. “Theoretical and experimental investigation of direct detection optical OFDM transmission using beat interference cancellation receiver,” Optics Express, vol. 21, no. 13, pp. 15237-15246, 2013.

[11] M. Malekiha, D. Yang, and S. Kumar, “Comparison of optical back propagation schemes for fiber-optic communications,” Optical Fiber Technology, vol. 19, no. 1, pp. 4-9, 2013.

## Conference Proceedings Not Directly Related to This Thesis

[12] R. Adams, M. Spasojevic, M. Chagnon, M. Malekiha, J. Li, D.V. Plant, and L.R. Chen, “Four Wave Mixing Based Wavelength Conversion and Multicasting of 16QAM Signals in a Silicon Nanowire,” IEEE Photonics Conference, Post-deadline Paper PGS, 2013.

[13] S.A. Nezamalhosseini, L.R. Chen, Q. Zhuge, M. Malekiha, F. Marvasti and D.V. Plant, “A novel receiver for spectrally efficient direct detection optical OFDM,” IEEE Photonics Conference, pp. 539-540, 2013.

## Contents

1 Introduction   
1.1 Overview . 2   
1.2 Motivation 4   
1.3 5   
1.4 Thesis Structure . 7   
1 1   
2.1 Introduction 1 1   
1 2   
2.2.1 Attenuation 1 3   
2.2.2 ASE Noise 1 4   
2.2.3 Chromatic Dispersion . 1 5   
2.2.4 Polarization Mode Dispersion 1 7   
2.2.5 Fiber Nonlinearity 2 0   
2.2.6 Laser Phase Noise . 2 5   
2.3 Coherent Optical Transmission Systems . 2 6   
2.3.1 Optical Coherent Receiver Structure 2 8   
2.3.2 Single-Carrier System . 30   
2.3.3 CO-OFDM System 3 3   
2.4 Conclusion . 3 6   
3 Low Complexity Multi-Sub-Band Transceiver for   
Reduced-Guard-Interval OFDM 3 7   
3.1 Introduction 3 9   
3.2 Filter-Bank Based Communication Systems 4 1   
3.3 Underdecimated Filter Banks for Spectrally Efficient CO-OFDM   
Communication Systems 4 5   
3.4 4 8   
3.5 Receiver DSP Structure 5 1   
3.6 Experimental Setup 5 5   
3.7 Results and Discussion 5 7   
3.7.1 Back-to-Back Performance 5 8   
3.7.2 Transmission Performance and Comparison to Single Carrier Systems 60   
3.8 Conclu sion . . . . . . 6 2   
4 Chromatic Dispersion Mitigation Based on Multi-Sub-Band Single   
Carrier 64   
4.1 Introduction . 6 5   
4.2 Chromatic Dispersion Mitigation by Multi-Sub-Band Single Carrier   
Transmission 6 7   
4.2.1 Transmitter and Receiver DSP Structure 6 9   
4.2.2 Experimental/Simulation Setup 7 2   
4.2.3 Results and Discussion 7 4   
4.2.4 Simulation Results 74   
4.2.5 Experimental Results 7 6   
4.3 Multi-Band Equalization 7 9   
4.3.1 Simulation Results 8 1   
4.4 Conclusion . 8 3   
5 Efficient Adaptive Nonlinear Equalizer for Intra-channel Nonlinearity   
Compensation for Agile Optical Networks 8 4   
5.1 Overview . . . . 8 5   
5.2 Principles of Perturbation Based Nonlinearity Compensation 8 9   
5.3 Optimization of Quantized Perturbation Coefficients . 9 3   
5.3.1 Receiver DSP Structure 9 5   
5.3.2 Experimental Setup . 9 6   
9 8   
5.4 Adaptive Nonlinear Filter Equalization Technique 100   
5.4.1 Discussion and Results 105   
5.5 Conclusion onclusion . . . . . . . . . 108   
6 Conclusion 110   
6.1 Summary 110   
6.2 Future Work . 113   
References 115

## List of Figures

1   
1 8   
2.2 2 4   
2.3 Schematic of a coherent optical transmission system. 2 7   
2.4 Schematic of a single polarization coherent receiver. 2 8   
2.5 The DSP of the single-carrier system at the (a) transmitter and (b) receiver,   
and (c) the spectra of raised cosine pulse shaping filter with various roll-off   
factors. . 3 1   
2.6 The DSP of the CO-OFDM DSP at the (a) transmitter, (b) receiver and (c)   
illustration of OFDM spectrum. . 3 4   
3.1 A generic frequency-division multiplexed communication link based on a   
synthesis filter-bank in the transmitter and an analysis filter-bank in the   
receiver (notice that the usual combination of filter banks in DSP textbooks,   
for data compression purposes, has the opposite order of the analysis and   
synthesis filter banks). 42   
3.2 Equivalent filter-bank representation of the frequency-division multiplexed   
communication link based on discrete-time up/down converters and   
baseband prototype filters. 4 2   
3.3 Equivalent filter-bank representation of the frequency-division-multiplexed   
communication link based on M-points (I)DFT and M polyphase filters   
(corresponding to the uniform maximally decimated FBs). The receive   
filters were selected here to be matched filters relative to the transmit filters. 43   
3.4 Proposed digital multi-band data structure with an un-modulated (DC)   
RF pilot tone for carrier recovery: Each channel (assumed here 35.2 GHz)   
is digitally frequency-division de-multiplexed into M active sub-bands (here   
M=14). The extreme sub-band (partitioned into two wrapped-around   
halves) is dedicated for filtering the transition roll-off of DAC   
image-rejection filter, and the center sub-band is dedicated to the guard   
band for inserting a pilot tone. . 47   
3.5 Comparison of required CP length for (a) conventional OFDM and (b) MSB-  
RGI-OFDM. 4 8   
3.6 Conventional DFTS-OFDM. 4 9   
3.7 MSB-RGI-OFDM Transmitter. 5 1   
3.8 filter-bank based MSB-RGI-OFDM Receiver. 5 2   
3.9 Sub-band receiver processor for MSB-RGI-OFDM. 5 3   
3.10 Experimental setup. EDFA: Erbium-doped fiber amplifiers, BPF: band-pass   
filter, T-T BPF: Tunable bandwidth and tunable center frequency band-pass   
filter, LO: local oscillator, PC: polarization controller, SW: switch. . . . . 5 6   
3.11 Back-to-back performance of different modulation formats under different   
PSR. . 58   
3.12 Performance of each subcarrier in back-to-back and after transmission for   
MSB-RGI-OFDM with different modulation formats at optimum launch   
power and PSR.   
3.13 Average $\mathrm { Q ^ { 2 } } \mathrm { - }$ Q - factor after transmission for different launch power. Solid line   
and dashed line corresponds to MSB-RGI-OFDM and SC, respectively. . .   
3.14 Maximum transmission distance for different modulation formats. Solid line   
and dashed line corresponds to MSB-RGI-OFDM and SC, respectively. (a)   
QPSK transmission with BER of $3 . 8 \times 1 0 ^ { - 2 }$   
transmission with BER of $2 \times 1 0 ^ { - 2 }$   
(corresponding to the M polyphases of the prototype pulse-shaping filter),   
(b) optical spectra of transmitted multi-sub-band signal.   
4.2 (a) Receiver-side DSP based on twice under-decimated M-points DFT and   
polyphase filters (The M receive polyphase filters were selected to be matched   
to the transmit filters). (b) Conventional singe carrier receiver DSP. . . . .   
4.3 Experimental setup. EDFA: erbium-doped fiber amplifiers, BPF: band-pass   
filter, T-T BPF: tunable bandwidth and tunable center frequency band-pass   
filter, LO: local oscillator, PC: polarization controller, and SW: switch. . .   
4.4 Simulated Q-factor penalty versus number of sub-bands at different   
transmission distance for 32 Gbaud MSB-DP-16QAM.   
4.5 Simulated number of required sub-bands versus different transmission   
distance for 32 Gbaud MSB-DP-16QAM to fully mitigate the effects of CD.   
4.6 Experimental back-to-back performance of 32 GBuad conventional SC-DP-  
16QAM and different MSB-DP-16QAMs. .   
4.7 Experimental BER versus launch power for 32 Gbaud conventional SC-DP-  
16QAM and 8-MSB-DP-16QAM after 2240 km. 7 8   
4.8 Experimental maximum transmission distance versus launch power for 32   
Gbaud conventional SC-DP-16QAM and MSB-DP-16QAM at soft FEC BER   
threshold of $2 \times 1 0 ^ { - 2 }$ 7 9   
4.9 Inter-band interference equalizer. 8 0   
4.10 Block diagram of (a) transmitter and (b) receiver polyphase channelizer. . 8 0   
16QAM in back-to-back. 8 1   
3120 km. . 8 2   
$( | C _ { m , n } | / C _ { 0 , 0 } ~ \leq$   
−35 dB), with a span length equals of 80 km with lumped amplification and   
32 Gbaud root-raised-cosine pulse shaped with a 1% roll-off factor. . . 9 1   
5.2 Receiver DSP . . . . 9 6   
5.3 Experimental setup. EDFA: Erbium-doped fiber amplifiers, BPF: Band-pass   
filter, T-T BPF: Tunable bandwidth and tunable center frequency band-pass   
filter, LO: Local oscillator, PC: Polarization controller, SW: Switch. . . . . 9 7   
5.4 Q-factor after nonlinearity compensation with optimized and conventional   
(linear) quantization of perturbation coefficients. . 9 8   
5.5 Q-factor versus launch power for linear compensation and nonlinearity   
compensation with optimized and linear quantization of perturbation   
coefficients $( N _ { k } = 8 )$ 9 9   
5.6 Convergence of adaptive perturbation coefficients over time $( N _ { k } = 8 )$ 100   
5.7 Symbol indices for the perturbation based nonlinear compensation and the   
proposed adaptive nonlinear equalizer after 480 km of SMF. 104   
5.8 Experimental BER versus nonlinear equalizer depth (normalized by   
maximum CD-induced pulse broadening) for 32 Gbaud SC-DP-16QAM   
after 2560 km and 1 dBm launch power. 105   
5.9 Experimental BER versus launch power for 32 Gbaud SC-DP-16QAM after   
2560 km. . 106   
5.10 Experimental maximum transmission distance versus launch power for 32   
Gbaud SC-DP-16QAM at soft FEC BER threshold of $2 \times 1 0 ^ { - 2 }$ 107   
5.11 Convergence of adaptive perturbation coefficients over time. 108

## List of Tables

1.1 A summary of a few record breaking hero experiments in the fifth generation fiber optical transmission systems. (PDM: polarization-division multiplexing; QPSK: quadrature phase-shift keying; QAM: quadrature amplitude modulation; OFDM: orthogonal frequency-division multiplexing)

## List of Abbreviations

ADC Analog-to-digital converter   
ASE Amplified spontaneous emission   
AWGN Additive white Gaussian noiseBER Bit error rateBPF Bandpass filterBPSK Binary phase-shift keying ASIC Application-specific integrated   
AWGN Additive white Gaussia   
BER Bit error rate   
BPF Bandpass filter   
BPSK   
CD Chromatic dispersion   
CO Coherent optical   
CP Cyclic prefix   
CPR Carrier phase recovery   
CW Continuous wave   
DAC Digital-to-analog converter   
DBP Digital back-propagation   
DD-LRD decision-directed least radius distance   
DD-LMS decision-directed least mean square   
DEPN Dispersion-enhanced phase noise   
DGD Differential group delay   
DP Dual-polarization   
DPSK Differential phase-shift keying   
DSP Digital signal processing   
DWDM Dense wavelength-division multiplexing   
ECL External cavity laser   
EDFA Erbium-doped fiber amplifier   
EEPN Equalization-enhanced phase noise   
ENOB Effective number of bits   
FEC Forward error correction   
FFT Fast Fourier transform   
FIR Finite-duration impulse   
FO Frequency offset   
FPGA   
FWM   
GN   
GVD   
ICI Inter-carrier interference   
IFFT Inverse fast Fourier transform   
IFWM Intrachannel four-wave mixing   
IM/DD Intensity modulation / direction detection   
ISI Intersymbol interference   
ISPM Intrasymbol self-phase modulation   
LMS Least-mean square   
LO Local oscillator   
MSB Multi-sub-band   
ML Maximum-likelihood   
MZM Mach-Zehnder modulator   
NLSE Nonlinear Schr¨odinger equations   
OSA Optical spectrum analyzer   
OFDM Orthogonal frequency-divsion multiplexing   
OSNR Optical signal-to-noise ratio   
PAPR Peak-to-average power ratio   
PC Polarization controller   
PD Photodetector   
PDM   
PLL Phase-locked loop   
PDPR   
PMD   
PRBS Pseudo random binary sequence   
PS Pilot subcarrier   
QAM Quadrature amplitude modulation   
QPSK Quadrature phase-shift keying   
RDE Radius directed equalization   
RGI Reduced-guard-interval   
RF Radio frequency   
ROADM Reconfigurable optical add-drop multiplexer   
RRC Root-raised-cosine   
SC Single-carrier   
SMF Single-mode fiber   
SNR Signal-to-noise ratio   
SPM Self-phase modulation   
SSFM Split-step Fourier method   
SSMF Standard single-mode fiber   
SW Switch   
TDF Time-domain filter   
TF Tunable filter   
TS Training symbol   
VOA Variable optical attenuator   
WDM   
XPM Cross-phase modulation

“Only a life lived for others is a life worthwhile.”

Albert Einstein

## Chapter 1

## Introduction

e past decade has been marked by a significant increase in Internet access media and an abundance of cloud-based storage, high-definition multimedia streaming, and services providing software and platforms. This has resulted in an unprecedented demand in the speed and volume of data transfers. As forecasted by Cisco (Fig. 1.1), this demand will definitely continue to grow and global data traffic will increase nearly 3-fold from 2014 to 2019. By the year 2019, 10.4 zettabytes of data will be transferred per year [1].

![](/img/mineru_output/Advanced_DSP_Coherent_Fiber_Optic_Comms_Malekiha_McGill_24p/auto/images/895338d0d20c8298d43169303b18fc4579f9cda58a890222ce6e57a7c11736ab.jpg)  
Network traffic predictions for years 2014 to 2019 in zettabytes per Fig. 1.1year. Figure produced from data in [1].