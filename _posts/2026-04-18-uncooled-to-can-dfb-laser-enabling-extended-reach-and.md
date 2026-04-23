---
layout: post
title:      "Uncooled TO-Can DFB Laser Enabling Extended Reach and Record Power Budget for Burst-Mode Upstream in 200-Gb/s VHSP SC-PON"
date:       2026-04-18 12:53:20
author:     "Bert"
tags:
  - Mineru
---
Yuhao Fang1, Weiqi Lu1, Haojie Zhu1, Puzhen Yuan1, Dayu Shi1, and William Shieh1,2, \* 1 School of Engineering, Westlake University, Hangzhou 310030, China 2 Westlake Institute for Optoelectronics, Hangzhou 311400, China \* Author e-mail address: shiehw@westlake.edu.cn

Abstract: We demonstrate a cost-effective burst-mode SC-PON, employing an uncooled DFB laser and SOA at each ONU. Eliminating the fast LO tracking at OLT, our system achieves 228 -Gb/s upstream transmission over 40.72 km SSMF, attaining a record 37-dB power budget. © 2025 The Authors

## 1. Introduction

In recent years, the field of optical access networks has experienced rapid and substantial global growth, propelled by the rising demand for cutting-edge Internet applications. The International Telecommunication Union Telecommunication Standardization Sector (ITU-T) has initiated studies on the next-generation PON standard, known as very-high-speed PON (VHSP) [1], with target line rates of 100-Gb/s and 200-Gb/s.

Both intensity modulation with direct detection (IM/DD) utilizing multiple wavelength pairs and coherent transmission have emerged as promising candidate technologies for VHSP [2–4]. However, both approaches encounter significant challenges when scaled to 200 Gb/s. For IM/DD systems, wavelength-division multiplexing (WDM) introduces greater complexity in wavelength allocation. Coherent solutions, by contrast, are limited by the high cost of deploying coherent lasers and DSP ASICs at the optical network unit (ONU), making them less viable for cost-sensitive access networks [5]. Furthermore, for coherent PON (C-PON), burst-mode detection presents additional challenges: local oscillator (LO) alignment between the ONU and OLT, particularly when using uncooled DFB lasers at the ONU, further increases system complexity and implementation cost [6].

Recently, the advancement of self-coherent PON (SC-PON) has introduced new alternatives for very high-speed passive optical networks (VHSP), with successful demonstrations across both integrated and discrete component platforms [7]. In this paper, we present a cost-effective burst-mode SC-PON solution for VHSP applications. By employing an uncooled DFB laser and a semiconductor optical amplifier (SOA) at each ONU, we achieve 228-Gb/s upstream transmission over 40.72-km of C-band SSMF. Notably, the proposed architecture fully eliminates the need for any additional fast wavelength tracking schemes at the OLT side. We attain a record power budget of 37-dB under the 2×10⁻² threshold (15.3% O-FEC [8]), surpassing class D/E2 requirements. To the best of our knowledge, this is the first demonstration of a burst-mode SC-PON enabling extended-reach and cost-effective VHSP with 37-dB margin.

![](images/56015476f80d6a1ce8745667addd8206575265a6245107fbd9b1e72d1da1b8e3.jpg)  
Fig. 1: Proposed burst-mode detection. OLT: optical line terminal, ODN: optical distribution network, ONU: optical network unit, SOA: semiconductor optical amplifier, EDFA: erbium-doped fiber amplifier, ADC: Analogue to Digital Converter, DSP: digital signal processing.

## 2. SC-PON burst-mode architecture and experiment setup

A burst-mode SC-PON detection scheme for VHSP applications is shown here. At each ONU, an uncooled TO-CAN packaged DFB laser is employed as the transmitter, while an SOA is used both for burst signal generation and dynamic power pre-leveling. The SOA is triggered by a function generator synchronized to the clock signal in each burst cycle, and the trigger voltage (Vpp) can be dynamically adjusted to compensate for varying ODN losses across different

![](images/2c5f638419b8fa4cb70d78940f884688f2681facb62d79e3ce6b1e8b796d5ac1.jpg)  
Fig. 2: (a) Experimental setup and DSP flow charts, (b) Burst signal. VODL: variable optical delay line, PC: polarization control, PBC: polarization beam combiner, BPD: balanced photodiode, DSP: digital signal processing, BM: burst mode. RLS: recursive least squares, DD-LMS: Decision-Directed Least Mean Square.

ONUs. At the OLT, an EDFA with fixed gain, followed by a Stokes Vector receiver, enables direct detection. Thanks to the self-coherent architecture, which eliminates the need for an additional local oscillator and complex wavelength tracking algorithms. As illustrated in Fig. 1, nearby ONUs with loud bursts require lower SOA driver voltage, while more distant ONUs with weak bursts use higher driver voltage, ensuring all burst signals arriving at the OLT have approximately equal power. This power pre-leveling scheme allows for the use of a fixed-gain EDFA and simplifies receiver design.

The experimental setup and DSP flowcharts are illustrated in Fig. 2(a). At the ONU transmitter, 2-D SVDD transmitter (SVT) is employed. A continuous-wave (CW) signal from an uncooled DFB laser is amplified from 5 dBm to 13-dBm using a SOA. The amplified signal is then split into two paths: 90% is routed to a 40-GHz IQ modulator for signal generation, while the remaining 10% serves as the optical carrier. The IQ modulator is driven by a 60-Gbaud PS-16QAM signal with an entropy of 3.8-bits/symbol generated by a 120-GSa/s arbitrary waveform generator (AWG, Keysight M8194A). A VODL is inserted to precisely match the path length difference between the signal and carrier arms. The signal spectrum is shown in Fig. 2 (a), with the carrier-to-signal power ratio(CSPR) for the SVT set to 1-dB. At the OLT receiver, an EDFA with fixed gain is employed as a pre-amplifier and followed by a Stokes Vector Receiver (SVR). The output signal is captured by a real-time oscilloscope (RTO) with a 256-GSa/s sampling rate (KEYSIGHT UXR0594AP). The burst frame structure comprises a 50-ns transmitter turn-on period, a 150-ns preamble for frame synchronization and pre-equalization, and a 1.3-μs payload for channel equalization and decoding. The preamble contains 6000 symbols dedicated to MIMO equalization using the RLS algorithm. For the payload DSP , DD-LMS is applied, initialized with tap coefficients estimated from the preamble. As shown in Fig. 2(b), a real burst frame captured from the RTO is presented. A 100-ns guard interval is inserted between adjacent burst frames. Additionally, approximately 42-ns and 10-ns durations are excluded from data analysis to account for the burst-mode settling time caused by the RC transient response during each SOA on/off switching event.

![](images/31fc86b8914fbe8771f7884ed1218601c01302b950d51f78172ef87e66729b9a.jpg)

![](images/2aa210d33bacee635e2b22ec76bd8647efdbce56e136db64c1a9742327c8b1bc.jpg)  
(b)

![](images/029d54ab0f263ac17b0bf52c676b168c94efa668cdb433ffae33b38c8593d52f.jpg)  
(c)

![](images/e1fdf438869bd8430b3d83eeeb2b9460999f4f76af8a306e7f9cb2502998be28.jpg)

![](images/99810bce632b6558479e3e8bc431b02795f9b44ff7a8cbb013ea50a3ef91c0c4.jpg)  
(e)

![](images/6ccfb6141c5aaf3a7ef7dcb75a14bb0c9289676df434464a0b29a5845a554807.jpg)  
Fig. 3: (a) EDFA fixed gain optimization. (b) SOA drive voltage optimization. (c) BER versus ROP for BTB, 20.36km ,40.72km transmission. (d) Maximum budget. (e) BER versus ODN LOSS for SOA gain turning and fixed gain. (f) BER versus ODN LOSS for BTB, 20.36km ,40.72km transmission.

## 3. Results

As can be seen in Fig. 3(a), we first optimized the fixed gain of the EDFA at a transmission distance of 40.72-km and an SOA launch power of 6-dBm, which fully eliminates nonlinearity introduced by the SOA. Due to the maximum input power constraint of the BPDs (13-dBm) used in the experiment, the maximum EDFA gain was limited to 30- dB. This restriction can result in receiver overload when the received optical power (ROP) exceeds –10-dBm. Conversely, insufficient EDFA gain can lead to sensitivity loss. Based on our experiments, the EDFA gain was set to 28-dB as a trade-off between avoiding overload and maintaining sufficient sensitivity. Subsequently, with the fixed EDFA gain, we also optimized the SOA gain. The SOA gain was measured in continuous mode and the same drive voltage was applied during burst-mode operation. The main penalties associated with increasing SOA gain stem from enhanced gain nonlinearity and amplified spontaneous emission (ASE) noise. Fig. 3(c) presents the BER versus ROP for different transmission distances. Negligible performance difference is observed between back-to-back (BTB) and 40.72-km transmission, indicating effective dispersion compensation. The maximum power budget was achieved at a launch power of 9-dBm, resulting in a power budget exceeding 37-dB for 40.72-km transmission as can been seen in Fig. 3(d). Fig. 3(e) demonstrates the advantage of tuning the SOA drive signal.With fixed EDFA gian, for a given SOA gain (also means certain launch power), system performance is either limited by a restricted power budget (when gain is low) or by sensitivity degradation at high gain, which introduces excess ASE noise and gain nonlinearity, where dynamic gain turning make full use of SOA linear region. Fig. 3(f) shows BER versus ODN loss across different transmission distances. With dynamic gain tuning, an extended margin at a low BER is achieved, effectively avoiding overload conditions, the effective ODN loss margin is from 5-dB to 37-dB.

## 4. Conclusion

We report the first demonstration of a burst-mode SC-PON upstream scheme for extended-reach VHSP applications. By employing simple uncooled DFB lasers and SOA-based pre-power leveling and burst generation at the ONU, our system achieves a record power budget of 37-dB with more than 20-dB dynamic range for PS-16QAM transmission at an entropy of 3.8- bits/symbol over 40.72-km C-band SSMF, exceeding class D/E2. Notably, no additional fast wavelength tracking scheme is required at the OLT, owing to the self-coherent architecture. This work highlights the feasibility and potential of cost-effective SC-PON for next-generation extended-reach TDM VHSP.

## 5. References

[1] ITU-T, G.suppl.VHSP (2023).

[2] D. van Veen et al. JOCN 12(1), pp. A95–A103 (2020).

[3] I. B. Kovacs et al., JOCN 16(7), pp. C1-C10 (2024)

[4] V. Houtsma et al., J. Opt. Com. Net. 16(2), A98-A104 (2024).

[5] W. Lanneer et al., in OFC 2025, paper Tu2I.7.

[6] Borkowski, R. et al., OFC’2025, Th4C.5.

[7] Y Fang et al., OFC’2025, Th3G. 3.

[8] Wang, W, et al. OFC’2022, W3H.1.