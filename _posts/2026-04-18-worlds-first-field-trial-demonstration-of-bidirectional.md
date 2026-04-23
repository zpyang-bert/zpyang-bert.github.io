---
layout: post
title:      "World’s First Field-Trial Demonstration of Bidirectional 200G TFDM Coherent PON Enabled by Real-Time FPGA-Based Reception"
date:       2026-04-18 16:20:31
author:     "Bert"
tags:
  - Mineru
---
An Yan1† , Renle Zheng1† , Hao Xu2 , Penghao Luo1 , Zeyu Zhao3 , Minhu Shen3 , Shuhong He1 , Sizhe Xing1 , Yongzhu Hu1 , Xuyu Deng1 , Junhao Zhao1 , Boyu Dong1 , Yinjun Liu1 , Ouhan Huang1 , Dezhi Zhang4 , Luhua Zhang2 , Yingjun Zhou2 , Dong Guo5 , Ji Zhou5 , Nan Chi1 and Junwen Zhang1\*

1 Key Laboratory of EMW Information (MoE), Fudan University, Shanghai 200433, China; 2 China Telecom Corporation Limited Shanghai Branch, Shanghai 200120, China; 3 Information Office of Fudan University, Fudan University, Shanghai 200433, China; 4 China Telecom Research Institute, State Key Laboratory of Optical Fiber and Cable Manufacture Technology, Beijing 102200, China; 5 Beijing Institute of Technology, Zhuhai 519088, Beijing 100081, China

Corresponding Author: \*junwenzhang@fudan.edu.cn † Authors contribute equally to this work.

Abstract: We demonstrate the world’s first field-trial of bidirectional 200G TFDM coherent PON enabled by real-time FPGA-based reception with two subcarriers, achieving −34-dBm downstream sensitivity and −31-dBm upstream sensitivity at 4.5-dB subcarriers power-difference with 21-dB dynamic range. © 2026 The Author(s)

## 1. Introduction

The development of passive optical networks (PONs) is driven by bandwidth-intensive services, including artificial intelligence (AI), mobile broadband, and edge data-center access (DCA) [1-2]. With ITU-T 50G-PON (G.9804) standards in place [3], scaling the system service capacity of access toward 100G, 200G, and beyond has become a key next step. Existing standardized PONs predominantly adopt intensity modulation and direct detection (IM/DD) due to its cost effectiveness. However, achieving 100G per wavelength with IM/DD remains challenging, largely limited by the available power budget. Coherent PON offers an attractive alternative for 100G+ access by providing higher receiver sensitivity and an enhanced power budget enabled by coherent detection and advanced DSP [4].

However, practical deployment of coherent PON still faces critical challenges. Burst-mode upstream transmission requires fast DSP acquisition and rapid convergence [5], while most reported demonstrations rely on offline processing, with real-time FPGA-based implementations remaining limited for both downstream continuous mode and upstream burst mode. The first real-time burst-mode coherent reception for upstream DSP-based PON was reported in [5], demonstrating 20 Gb/s single-polarization QPSK burst signals. In [6–7], the first real-time TFDM-based coherent PON was demonstrated, supporting 12.5 Gb/s per subcarrier burst upstream and 50 Gb/s per subcarrier downstream transmission. To date, real-time burst-mode coherent reception beyond 100 Gb/s has not been demonstrated. For downstream continuous-mode operation, the highest reported line rate remains 120 Gb/s [8], achieved in laboratory demonstration and still below the 200G-class.

In this work, we demonstrate the world’s first field trials of bidirectional 200G TFDM coherent PON enabled by real-time FPGA-based reception. Both downstream and upstream transmissions adopt a two-subcarrier (2-SC) TFDM structure, with each subcarrier carrying 100.27008 Gb/s. For downstream transmission, a peak aggregate rate of 200.54016 Gb/s is achieved in the field trial, with a receiver sensitivity of −34 dBm. A maximum power budget of 42.8 dB is also demonstrated at 10-dBm launch power. For upstream transmission at the same 200G peak rate, a back-to-back (B2B) sensitivity of approximately −34 dBm and a dynamic range of 21 dB are achieved without burst-mode TIA. Under a 4.5-dB received-power imbalance between the two ONU upstream carriers in the field trial, a sensitivity of −31 dBm is obtained. At a 2-dBm launch power, a 33-dB power budget is supported.

## 2. Field-trial setup

Fig. 1 shows the field-trial experimental setup of the real-time FPGA-based bidirectional 200G TFDM coherent PON. The field trials are conducted on the platform from Fudan University. As shown in Fig. 1 (b), the field trial is conducted across three sites: (A) D3 Building, Shanghai Bay Valley Science and Technology Park; (B) the Law School Building, Fudan University; and (C) Interdisciplinary Complex Building 1, Fudan University. The fiber length from Site A to Site B is approximately 14.5 km, and that from Site B to Site C is approximately 0.5 km. Notably, the field trial is carried out in a loopback configuration, with both the OLT and two ONUs deployed at Site A. As shown in Fig. 1(a) and (b), the fiber lengths to the OLT are 29 km for ONU1 and 30 km for ONU2.

The downstream is transmitted at 1540 nm, while the upstream is transmitted at 1552.5 nm. In the downstream OLT transmitter side, 25.06752-GBaud dual-polarization (DP) QPSK signals are generated on two SCs and loaded into the 119.07072-Gsa/s arbitrary waveform generator (AWG, Keysight M8194A). The modulated optical signal is amplified to 2 dBm by a semiconductor optical amplifier (SOA) and then distributed to two ONUs over several allpassive optical distribution frames (ODFs) and field-deployed standard single-mode fiber (SSMF). In each ONU receiver side, a variable optical attenuator (VOA) is used to adjust the received optical power (ROP). The downstream signal is detected by an integrated coherent receiver (ICR). The signals are digitized and then processed by an FPGA (Xilinx XCVU13P) equipped with four analog-to-digital channels operating at a sampling rate of 28.20096 GSa/s. In the upstream ONU transmitter side, 25.06752-GBaud DP-QPSK burst signals are generated. At each ONU, the optical burst signal is amplified to 2 dBm by an SOA. Then the SC signals from ONU1 and ONU2 are transmitted over 14.5-km SSMF to Site B. The signal from ONU2 is then further sent over additional 0.5-km SSMF to Site C and looped back over 0.5-km SSMF to Site B. At Site B, the two upstream SCs are merged and sent back to the OLT over 14.5-km SSMF. Due to multiple ODF crossings in the deployed fiber route, additional insertion losses are introduced, leading to measured optical path losses of 23.5 dB and 28 dB for ONU1 and ONU2, respectively. There exists 4.5-dB inter-ONU power difference between two upstream SCs. Notably, the downstream and upstream reception DSP both run in real-time FPGA. Due to FPGA resource constraints, real-time processing is applied to one 100G subcarrier at a time during the experimental tests. Nevertheless, the physical layer operates with the full 2-SC 200G TFDM structure, and both subcarriers are individually tested under identical conditions.

![](/img/mineru_output/Th4C.4/auto/images/e9dcc64c2f0cfa058d46816b9ba5a66a5150e79a4c997a63e3fb586eaba3d0e3.jpg)  
Fig. 1 Field-trial setup of the real-time FPGA-based bidirectional 200G TFDM coherent PON through field-deployed fiber links. (a) The overall experimental setup; (b) Field-trial deployment map showing fiber routes and site locations, and the effective fiber lengths to the OLT are 29 km (ONU1) and 30 km (ONU2). Inset (i) is the network topology for the field-trail links.

## 3. Experimental results and discussion

Fig. 2 shows the field-trial experimental results. Fig. 2 (a) and (b) present the sensitivity performance in downstream transmission, for B2B and field trial case, respectively. Chromatic dispersion is compensated by the blind channel equalizer in the ONU receiver DSP, leading to essentially identical BER performance in the back-to-back (B2B) case and after fiber transmission. For performance evaluation, a 15% overhead soft-decision FEC with a BER threshold of 2×10⁻² [6] is assumed. Note that FEC decoding is not included in the FPGA implementation. When the OLT transmits two carriers to provide an aggregate rate of 200G (200.54016 Gb/s), each ONU demodulates only one SC. However, it still receives the combined optical power of both data SCs, and the measured sensitivity becomes −34 dBm. In Fig. 2(c), the downstream sensitivity is measured versus the OLT launch power, which is controlled by the SOA drive current. The sensitivity penalty emerges when the launch power exceeds 6 dBm. For launch power up to 10 dBm, increasing the launch power improves the power budget, reaching a maximum of 42.8 dB. Fig. 2 (d) presents the upstream performance under B2B condition. The upstream sensitivity is −37 dBm when only one ONU (ONU1 or ONU2) is active and transmits a single 100G carrier. When the aggregate upstream rate is 200G, the measured sensitivity is about −34 dBm, which holds for both cases where only one ONU is active and two carriers are transmitted or two ONUs are active and two carriers are transmitted. For both 100G and 200G upstream operation, a dynamic range of up to 21 dB is achieved. Fig. 2 (e) presents the upstream performance in the field trial.

![](/img/mineru_output/Th4C.4/auto/images/8d10bc8e9fcb0612d5c0d8465e88814258fd7d1e9262ec1dd71c83efd333842a.jpg)

![](/img/mineru_output/Th4C.4/auto/images/dd1bfae69d4b8d1f3777cd504938f147452574a5f20e0726bc8aa302f919c736.jpg)

![](/img/mineru_output/Th4C.4/auto/images/63de6fd460d273b48dc90a7f558961eb4569aa5c4f3c419786ed96ad31848301.jpg)

![](/img/mineru_output/Th4C.4/auto/images/34c5ee6f9128252cbb23ad736048949d10fdb7512a389008459fd3c803ecccc7.jpg)

![](/img/mineru_output/Th4C.4/auto/images/28f05002ff839ca6a7dd7fd0bc3b287d88d47415c96e4783a54158dd3e6602c1.jpg)

![](/img/mineru_output/Th4C.4/auto/images/b3056cc901c6aa85cf6fcbeda94aca285776a92db667524e4b449ca36d75416f.jpg)

![](/img/mineru_output/Th4C.4/auto/images/cc57849e54e5024adb99ddb2dbf94fd85eff722a563717f79a06e7427bfddb2c.jpg)

![](/img/mineru_output/Th4C.4/auto/images/03ba1b757f4d8ef86f58b8df7b7e36bab47cb69513544fbb7dc3a463507daf40.jpg)

![](/img/mineru_output/Th4C.4/auto/images/9e0f73c38ad2b633812deb5770a9ffd24c34daa279bb09b862971bc806883d86.jpg)

![](/img/mineru_output/Th4C.4/auto/images/1fbe3b4b1a00a8c7f780b0567fa090bf224e9a6a120d684e9fc86d54d8482284.jpg)  
Fig. 2 (a) B2B downstream sensitivity performance. (a) Field-trial downstream sensitivity performance. (c) Downstream power budget vs. SOA boost power. (d) B2B upstream performance. (e) Field-trial upstream performance. (f) Upstream time–frequency resource allocation: spectra and waveforms for 100G/200G cases. (g) OLT FPGA placement for upstream Rx DSP. (h) ONU FPGA placement for downstream Rx DSP. (j) Long-term DSP performance (200G) over time up to 24 h. (k) FPGA resource utilization.

The sensitivity is −37 dBm when only one ONU transmits a single 100G carrier. The sensitivity is −34 dBm when only one ONU transmits two carriers (200G). When both ONUs are active and each transmits a 100G single-carrier signal, resulting in a 200G aggregate rate, the measured sensitivity is −31 dBm. This is attributed to a 4.5-dB power imbalance between the two ONU carriers, and the sensitivity is evaluated based on the worst-performing carrier (SC2 in Fig. 2 (e)). In Fig. 2(f), the upstream time–frequency resource allocation is illustrated by the measured spectra and waveforms, corresponding to the several allocation cases in Fig. 2(e). Fig. 2 (j) shows the long-term DSP stability. The BERs for running for 24 h are all below the FEC threshold for both downstream and upstream. Therefore, the stability of the real-time DSP is confirmed. Finally, the FPGA placements of the OLT and ONU are shown in Fig. 2 (g) and (h), and the resource utilization is summarized in Fig. 2(k).

## 4. Conclusion

We demonstrate the world’s first field trials of bidirectional 200G TFDM coherent PON enabled by real-time FPGA-based reception. A two-subcarrier (2-SC) TFDM structure is employed, achieving an aggregate rate of 200.54016 Gb/s for both downstream and upstream transmissions, with each subcarrier carrying 100.27008 Gb/s. In the 200G downstream field trial, a receiver sensitivity of −34 dBm and a maximum power budget of 42.8 dB are achieved. For upstream transmission, a back-to-back sensitivity of −34 dBm and a dynamic range of 21 dB are obtained. Under field-trial conditions with a 4.5-dB received-power imbalance between the two ONU upstream carriers, a receiver sensitivity of −31 dBm and a 33-dB power budget are demonstrated.

Acknowledgment: This work was supported in part by the National Key Research and Development Program of China (2023YFB2905700), National Natural Science Foundation of China under Grants (62235005, 62525102) and Natural Science Foundation of Shanghai (24ZR1490500). References

[1] S. Bidkar, et al., in OFC 2018, paper Tu2K.3.

[2] R. Bonk, et al., IEEE Commun. Mag., 60.3, 48-54 (2022).

[3] Y. Luo, et al., J. Opt. Comm. Netw., 16.7, C106-C112 (2024).

[4] A. Yan, et al., J. Sel. Areas Commun., 43.5, 1536–1551 (2025).

[5] R. Koma, et al., J. Light. Technol., 35.8, 1392–1398 (2017).

[6] Z. Xing, et al., in OFC 2023, paper Th4C.4.

[7] J. Zhou, et al., J. Light. Technol., 42.4, 1193–1202 (2024).

[8] K. Dong, et al., in ACP 2025, pp. 1-5.