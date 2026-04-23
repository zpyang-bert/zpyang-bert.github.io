---
layout: post
title:      "First Coherent DSP and Pluggable Transceiver Capable of Distance-Resolved, Longitudinal Power Monitoring"
date:       2026-04-18 12:46:16
author:     "Bert"
tags:
  - Mineru
---
Takeo Sasai, Yukinobu Nakajima, Minami Takahashi, Runa Kaneko, Masanori Nakamura, Asuka

Matsushita, Fukutaro Hamaoka, and Etsushi Yamazaki

Network Innovation Laboratories, NTT, Inc., 1-1 Hikari-no-oka, Yokosuka, Kanagawa, 239-0847 Japan takeo.sasai@ntt.com

Abstract: We present the first realization of longitudinal power monitoring implemented fully on a real-time coherent DSP inside an OSFP, delivering up to 1005-km-range, 2.1-km-resolution monitoring using 800ZR+/400ZR+ traffic, with multi-vendor interoperability and negligible power overhead. © 2026 The Author(s)

## 1. Introduction

Over the past decade, continuous advances in coherent digital signal processors (DSPs) and coherent pluggable transceivers have expanded their role in optical networks. The application reach of coherent pluggables has extended from data-center interconnect (DCI) to metro and long-haul [1] as exemplified by ZR+ [2][3], while the link monitoring capability of coherent DSPs simplifies link diagnostics, enabling improved efficiency of network operation.

To date, the link performance metrics obtained from real-time coherent DSPs have been limited to cumulative values, lacking spatial resolution and localization capability. Longitudinal power monitoring (LPM), first demonstrated in 2019 [4], has been extensively investigated as it provides distributed power profiles solely from the network endpoint (i.e., the coherent receiver) without dedicated hardware such as OTDRs [4]-[10]. Its network applications are diverse, including bottleneck localization [4], link optimization [8][9], margin design, and automated path reconfiguration [9]. While prior studies of LPM successfully conducted field trials and demonstrations using commercial transponders[6]-[9], they have relied on offline processing outside the transceivers due to large computational load and memory footprint inherent to LPM (Table 1). Implementing LPM directly on coherent DSPs would make LPM a native function of coherent transceivers, particularly pluggable transceivers widely deployable from DCI to long haul, enabling in-service distributed monitoring and thus simplified operations of diverse optical network infrastructures.

In this work, we present the first coherent DSP that integrates LPM on chip, implemented inside an OSFP pluggable module, achieving distance-resolved monitoring over 1005 km with a 2.1-km sampling resolution using only the compact pluggable optics at link endpoints. The on-chip LPM operates in a fully blind manner, relying solely on the received ZR+ traffic without any dedicated probing or training sequences. We further demonstrate that the on-chip LPM is interoperable with third-party pluggables at the Tx side in both 800ZR+ (16QAM) and 400ZR+ (QPSK) modes, confirming vendor- and modulation-format-independent operation. We also show that this LPM incurs negligible power consumption, fully compliant with pluggable power constraints. These results upgrade coherent DSPs from cumulative to spatially-resolved monitoring, which allows pluggable transceivers deployable from DCI to long haul to function not only as cost-efficient transmission elements but also as distributed monitoring points, thereby simplifying operations of diverse optical networks.

## 2. Implementation of LPM on coherent DSP

Fig. 1(a) and (b) show the OSFP module with the on-chip LPM and a schematic diagram of the internal DSP chip, respectively. Due to the computational complexity of LPM, a straightforward implementation in the DSP ASIC would lead to a significant increase in power consumption. In this work, LPM is therefore implemented in a processing unit on the DSP chip, located alongside the main DSP chain. This LPM engine acquires the received traffic waveform from the Rx DSP pipeline and performs an algorithm inspired by [10] to estimate the distributed power along the link. However, a direct implementation of [10] requires a substantial computational load and memory footprint from megabytes to gigabytes, which is still prohibitive for on-chip implementation. To address this point, a closed-formassisted approach based on [11] is employed, enabling low-complexity and low-memory LPM suitable for the severely constrained computational resources of the DSP and OSFP. This LPM engine occupies well below 1% of the total core logic area, imposing negligible power consumption and hardware overhead and thus complying with strict sizeand power-constraints of the OSFP. All LPM computations, including power profile averaging, are done entirely within the Rx-side DSP chip, and the results are accessible via the standard I2C interface of the module.

Table 1 Relevant LPM demonstrations
<table><tr><td></td><td>Implcmentation location</td><td>Receiver type</td><td>Traffc-signal- based mcnitoring&#x27;</td><td>Iseoperaliliey demonstration</td><td>Distance</td></tr><tr><td>[4]</td><td>Offline</td><td>Discrese</td><td>No</td><td>No</td><td>260 km</td></tr><tr><td>[5]</td><td>omine</td><td>Discrete</td><td>No</td><td>No</td><td>&gt;10000 1m</td></tr><tr><td>[6]</td><td>omine</td><td>Trawsponder</td><td>Ya</td><td>No</td><td>900 km</td></tr><tr><td>[7]</td><td>omine</td><td>Trarsponder</td><td>No</td><td>No</td><td>163 km</td></tr><tr><td>[8]</td><td>omine</td><td>Transeeiver</td><td>Ys</td><td>No</td><td>200 km</td></tr><tr><td>[9]</td><td>Rx-adjacent + controller</td><td>Trarsponder</td><td>Yes</td><td>No</td><td>−400 km</td></tr><tr><td>This work</td><td>Fully on DSP chip</td><td>Plugable (OSFP)</td><td>Yes</td><td>Yes</td><td>1005 km (400ZR+) 450 1m (800ZR+)</td></tr></table>

1 Yes: uses payload data (i.e., Tx symbols are unknown)

![](images/685b6ec1a6b6f7a9c6c61e0e8e1068711bc4fdba21047f059d423f9b7a9be69d.jpg)

![](images/47a22e4f9058106e7de0696e87471185b7c3ed487b951b446d12a5b7582242b1.jpg)  
Fig. 1. (a) OSFP coherent pluggable module with LPM-integrated DSP inside. (b) Diagram of OSFP and DSP architecture. The LPM engine is implemented on chip alongside the Rx/Tx DSP ASIC.

![](images/5bf108db6382eedad88516e4f810c184d90d5a0a9eb57138fa484b970620a9c2.jpg)  
Fig. 2. (a) Tx-side pluggable transceiver operated using a commercial network tester. (b) Experimental setup for 1005-km transmission. (c) Transmitted and received (1005km) spectrum. (d) Relative Q value vs fiber launch power after 1005-km transmission. The LPM is operated at the power level that maximizes the Q factor.

The transmitted signal is not assumed to be known a priori for LPM as it is reconstructed from the demodulated signal within the DSP using hard decision of the pre-FEC data. Therefore, no special probing signal or training sequence is required, and the LPM can operate using in-service traffic signals, including those transmitted from thirdparty transceivers, enabling simultaneous communication and distributed monitoring, in an interoperable manner.

## 3. Experimental setup

Fig. 2 shows the experimental setup. At the transmitter side, three coherent pluggable transceivers were used: an OSFP (Vendor A) for both 800ZR+ 16QAM and 400ZR+ QPSK transmission, another OSFP (Vendor B) for 800ZR+, and a QSFP-DD (Vendor C) for 400ZR+ to verify multi-vendor interoperability of LPM (Fig. 2(b)). The symbol rate was 118.2 GBd for both 800ZR+ and 400ZR+. These pluggables were hosted by a VIAVI ONT-804 network tester (Fig. 2(a)). As such, no specialized signal was used and the LPM was operated on standard ZR traffic signals. The channel under test (CUT) was set at a center frequency of 193.7 THz and multiplexed with 24 WDM channels with 150-GHz spacing (a total bandwidth of 3.75 THz), emulated by spectrally shaped ASE, as shown in Fig. 2(c). The optical power of the CUT was adjusted to match that of the neighboring WDM channels. The transmission links consisted of 450 km (75 km × 6 spans) and 1005 km (75 km × 7 + 80 km × 6 spans) of fibers compliant with ITU-T G.652.D. The average attenuation coefficient and chromatic dispersion were 0.186 dB/km and 16.80 ps/nm/km, respectively. As shown in Fig. 2(d), the total fiber launch power was set to 17.0 dBm, corresponding to the optimum power level that maximized the Q factor recorded at the receiving OSFP. After transmission, the CUT was demultiplexed and received by a separate OSFP module (Vendor A). The DSP in the receiving OSFP is supplied by a different DSP vendor than those used in Vendor B and Vendor C at the Tx side, enabling LPM’s interoperability verification across different Txside DSP vendors. The receiving OSFP and DSP perform signal demodulation and LPM with a spatial sampling resolution of 2.1 km. We observed that the post-FEC BER was error-free during LPM operations.

## 4. Results

Fig. 3(a) and (b) present the on-chip LPM results over 1005 km using 400ZR+ (QPSK) and over 450 km using 800ZR+ (16QAM), respectively. Link anomalies of approximately 2.0 dB are emulated by inserting VOAs at 175 km and 724 km, and varying an EDFA gain at 450 km. Between the normal and anomalous states, highly stable and reproducible power profiles are observed in spans without anomalies, while clear power deviations are observed in the anomalous spans. The heatmap shows the normal-anomalous differences that exceed 4σ of the LPM noise, clearly localizing multiple impairments along the link. These LPM results also show good agreement with OTDR measurements, achieving RMS errors of 0.43 dB for 400ZR+ and 0.60 dB for 800ZR+ excluding the inter-span transition regions. Fig. 3(c) shows the relative variation of the Q-factor over time observed at the receiving OSFP. Stable Q values within ±0.04 dB are maintained, and post-FEC error-free are confirmed, irrespective of LPM on/off operation, confirming the on-chip LPM does not impact transmission performance and enables simultaneous communication and distributed monitoring. Fig. 3(d) further presents the module power consumption during LPM, and no measurable increase is observed when LPM is enabled, indicating that the on-chip LPM introduces negligible power consumption overhead and thus satisfies the strict power constraints of the OSFP module. Figs. 3(e) and (f) show the LPM results across different Tx vendors for 400ZR+ (1005 km) and 800ZR+ (450 km), respectively. The LPM remains consistent even when the third-party transmitters are used, with RMS deviations of 0.63 dB for 400ZR+ and 0.70 dB for 800ZR+, confirming LPM’s multi-vendor interoperability and its applicability to open optical network.

(a) 400ZR+(QPSK)  
![](images/2111740ac87a9b16c556b3bffc6bc4c76e14fc36ae58d7127eb5fafd47277225.jpg)

(b) 800ZR+(16QAM)  
![](images/824a6563c51a3078405a3b465502645e056101fecfbf4b32c7e578bd4572bb0b.jpg)  
(e) 40OZR+ interoperability

(d)  
![](images/ee89371909030917587b5c7ce3ef5eafb9f101f70c911f339ef81822287f1dde.jpg)

![](images/1284c9c6c4101e203a9399d1d55de0b5e08a6cc27521496faf179238db0e7115.jpg)  
(f) 8goZR+ interoperability

![](images/8293e7f634e15af4204d14df8278db1209a9f950347d85a0e0811ba0f455aa38.jpg)

![](images/50830aeb9b32324f96d8311c2eafe07f58d58f502b3bfc2dd45aea50f3a670b4.jpg)  
Fig. 3. On-chip LPM results. (a) LPM over 1005 km using 400ZR+ (QPSK) and (b) over 450 km using 800ZR+ (16QAM), with and without power anomalies at 175, 450, and 724 km. The heatmaps show normal-anomalous difference exceeding 4σ of the LPM noise. (c) Q and (d) power consumption stability during LPM on/off operation. (e),(f) Multi-vendor interoperability results for 400ZR+ and 800ZR+, respectively.

## 5. Conclusion

Since its first demonstration in 2019 [4], LPM has now been realized on a coherent DSP. We have shown that the onchip LPM achieves distance-resolved monitoring over a 1005-km link with a 2.1-km resolution solely using standard ZR traffic received at a pluggable, localizing multiple impairments along the link without impacting signal quality and power consumption. These results demonstrate that LPM can be a native monitoring function of coherent pluggables, enabling distributed monitoring of diverse optical network infrastructures from DCI to long haul without dedicated equipment and substantially simplifying network maintenance and operations.

## Acknowledgements

These results were obtained from the commissioned research (NoJPJ012368G60201) by National Institute of Information and Communications Technology (NICT), Japan. We thank the members of NTT Innovative Devices Corporation for their support.

## References

[1] J. Pedro, M. M. Hosseini and A. Napoli, "Extended network applications of coherent pluggable transceivers," JOCN 17(2), 2025.

[2] OpenROADM, https://openroadm.org/ [3] OpenZR+ MSA, https://openzrplus.org/

[4] T. Tanimura et al., “Experimental demonstration of a coherent receiver that visualizes longitudinal signal power profile…,” ECOC2019, PD.3.4.

[5] A. May et al., "Longitudinal power monitoring over a deployed 10,000-km link for submarine systems," OFC2023, Tu2G.3.

[6] J. Chang et al., "Demonstration of longitudinal power profile estimation using commercial transceivers…," ECOC2023, Tu.A.2.2.

[7] T. Sasai et al., “4D Optical link tomography: first field demonstration of autonomous transponder capable of distance…,” OFC2024, Th4B.7.

[8] L. Andrenacci et al., "DSP-based nonlinear interference estimation using linear least squares longitudinal power monitoring," JLT 43(8), 2025.

[9] A. Pacini et al., "Longitudinal power profile monitoring telemetry enabling self-healing optical networks," JOCN 17(7), 2025.

[10] T. Sasai et al., “Linear least squares estimation of fiber-longitudinal optical power profile,” JLT, 42(6), 2024.

[11] T. Sasai et al., “Closed-form expression for spatial correlation function of nonlinear fiber propagation and its…,” OFC2026, Tu3A.5.