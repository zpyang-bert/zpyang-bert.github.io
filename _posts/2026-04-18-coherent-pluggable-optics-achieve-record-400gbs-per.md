---
layout: post
title:      "Coherent Pluggable Optics Achieve Record 400Gb/s per Wavelength Over a 5,682 km Subsea Cable"
date:       2026-04-18 12:00:53
author:     "Bert"
tags:
  - Mineru
---
Sumudu Edirisinghe, Ekaterina Golovchenko, Serge Melle, Ales Kumpera, John van Weerdenburg, Pierre Mertz, Lee Dardis, Aditya Kakkar, Oriol Bertran Pardo, Julio Diniz, Eduardo Spotorno, Konstantin Gelov,

Rafael Diaz-Malaguilla and Manuel Morales

Nokia, 3201 Olympus Boulevard, Dallas, Texas, 75019, USA sumudu.edirisinghe@nokia.com

Abstract: We demonstrated a record 400G capacity-reach over a 5,682 km subsea cable using pluggable coherent optics. These results validate significant power, space, and cost savings for operators scaling networks for AI and cloud infrastructure.

## 1. Introduction

In recent years, impressive improvements of pluggable coherent optics performance and data rate improvements, positioned them as a viable rival to well established embedded coherent transceivers for metro and long-haul terrestrial applications [1, 2, 3]. Coherent pluggable optics, deployable into either IP routers, packet switches or transponders optimized for pluggable optics, offer important savings in power, space, and cost for network operators. However, their use has not been widely explored in ultra-long-haul repeatered subsea cable systems, where performance-optimized embedded coherent optics continue to be the prevalent solution deployed, due in part to the need to compensate for large amounts of accumulated dispersion and combat nonlinear and EEPN impairments [4]. Recent field trials reported in press releases [5] indicate that the work to introduce use of coherent pluggable optics into subsea applications has started.

In this work we used innovative 3nm-based CMOS coherent pluggable modules capable of operation up to 135Gbaud, and 400G, 600G and 800G line rates per wavelength. These were deployed alongside live customer traffic on a repeatered subsea fiber cable connecting USA with Puerto Rico. Results demonstrate operation with healthy performance margins and record capacity-reach for pluggable coherent optics, of 5,682 km at 400G when operating at 72Gbaud, and 2,841km at 600G when operating at 119Gbaud, and set new industry records for capacity-reach performance using commercially shipping pluggable coherent optics.

## 2. Field Trial setup

The 800G coherent OSFP and QSFP-compliant modules capable of operating with line rates tuneable from 200 Gb/s to 800 Gb/s. The module is fully tuneable over C-band and L-band with 3.125GHz granularity and comply with a wide range of standards, including the OIF-800ZR-01.0 and OIF-400ZR-03.0 implementation agreements, the OpenZR+ Rev 3.0 standard and the Open ROADM 6.0 standard. It supports OFEC on most modulation formats with FEC limit 6.32dB. In addition, the module supports LDPC based proprietary modulation formats with an improved FEC limit. At 400Gb/s, 600Gb/s and 800Gb/s baud rates ranging from 60Gbaud to 140Gbaud, allowed transmission over the direct point to point and the roundtrip distances.The field trial was conducted over dispersion uncompensated cable system with 2,841km total point to point reach and 5,862 km roundtrip based on EX2000 fiber with dispersion of 20.6 ps/nm/km at 1550 nm. The accumulated dispersion at 1550 was \~60.4ns/nm at 2,841km and \~120.8ns/nm for the roundtrip. The cable had 46 spans with 66km average span length, 20dBm output repeater power and 4.5dB noise figure.

The system was carrying traffic at the time of the field trial. The test channels were inserted into 2 parts of the spectrum where 150GHz wide gap was created by removing ASE from each part between 191.4-191.55 THz and 195.1-195.25 THz ensuring little impact on the live traffic (figure 1). The channels were added through a free WSS port on the legacy SLTE with automatic power control through the port disabled.

![](images/01e5fd448bdfb47bf3154b4723d3a8462619d91ebdb45469753d84c73cb51105.jpg)  
Fig. 1. Receive spectrum showing 600Gb/s 119Gbaud pluggable coherent channels with live service channels

## 3. Results

The Q margins of the pluggable channels were measured by varying the channel power relative to ASE noise loaders for a range of modulation format over the 2,841km point-to-point link between USA and Puerto Rico, at 191.415 THz and at 195.175THz. With increasing baud rate optimum launch power of the pluggable coherent optics shifts towards higher powers relative to ASE power; -2dB at 60/64Gbaud, -1dB at 72Gbaud and +1dB at 118/119Gbaud. Operation at both 400Gb/s and 600Gb/s line rates were achieved with excess margins. Remarkably 800Gb/s managed to achieve error free performance. The measurement results are depicted in Figure 2.

Similar trends were observed at 195.175Hz, even though the performance degraded by 0.5-0.6dB compared to 191.475THz operation, and 1dB higher launch power was needed (Fig. 2) due to the OSNR tilt across the spectrum. With increasing baud rate, the optimum optical launch power shifts towards higher powers relative to ASE power; - 1dB at 60/64Gbaud versus ASE power, and +2dB at 118/119Gbaud. Both 400Gb/s line rates and 600Gb/s line rates were achieved with excess margins, while lower OSNR at 195.175THz resulted in loss of frame for 800Gb/s line rates.

![](images/9dd381a32cd720eaefde477d8f48744c212fe0d98c9281ef8066168d3bf866fa.jpg)  
Fig. 2. Q margin at 191.475THz and 195.175THz vs pre-emphasis for different operating modes of the pluggable coherent optics, operating at 400Gb/s, 600Gb/s and 800Gb/s

A looped back was applied after the WSS in Puerto Rico to filter and reinsert the signal back towards USA to achieve a total link length of 5,682km with total dispersion of approximately 126ns/nm at 191.475THz. Over this distance the performance of 400Gb/s modulation format was optimized leveraging the improved proprietary FEC to traverse the distance. 400Gb/s 72Gbaud mode provided the optimum performance trading off the EEPN with OSNR penalty. Figure 3 shows achieved performance at 400Gb/s vs preemphasis, and Figure 4 shows constellation diagrams for 800Gb/s at 2,841km, and 400Gb/s at 5,682km.

![](images/8806b4f5f84256f1d8a3551d8bc2ef7bf750ab1822e520285b3ac262ff4c148e.jpg)

![](images/583cf78494f619993b191c514e5836902e30a626db4db4d17217c38070b6e2ef.jpg)  
Fig. 3. Q margin for 400Gb/s at 191.475THz and 195.175THz across 5,682 km of transmission distance

![](images/dc3d542be4ef4fe717d3724f5e5feaa0e33cb3f56d3146dc194e9722db9a529f.jpg)

![](images/b0111edf68b40db2fb136c4bd0636cc3b93d415359b4b287546ec27cd5846ea0.jpg)

![](images/b65004af9f99fdd2fa42307577e611fc1f1f236f34470bfa2c9eea896a5d011f.jpg)

![](images/fa9a244e5db93c440c839400dfb4e2418253fcc9f7d78297b3d5132126eb7ed1.jpg)

![](images/a71d6b5a076fdd82fcc4dfdb4fca6b996b077c597942774fbb5762df6280a447.jpg)  
Fig. 4. Signal spectrum and constellation diagrams for 800Gb/s over 2,841km, and 400Gb/s over 5,682 km

## 4. Conclusion

In conclusion the reported field trial results are a significant milestone representing a dramatic advancement for optical networking in subsea networks. It demonstrates that the latest generation of 135Gbaud pluggable coherent optics can reliably operate over ultra-long repeatered subsea links, a capability previously limited to embedded optical systems. Extending pluggable optics to subsea applications allows network operators to dramatically reduce power consumption, space requirements, and cost per bit, while simultaneously meeting network capacity requirements. By enabling use in either pluggable-optimized transponders or IP routers, the benefits of pluggable coherent optics can be further extended by direct pluggability into router ports for IPoDWDM implementations, which can be managed by cross-domain management and orchestration platforms which can also manage the optical parameters of the pluggable devices through OpenConfig-based APIs.

## 5. References

[1] T. Monteiro, “Operationalizing Coherent Optical Pluggables in the Backhaul,” SubOptic, Lisbon, 2025.

[2] J. Pedro, “Coherent Pluggable Optical Transceivers: Performance Versus Interoperability,” in ELEKTRO, Zakopane, Poland, 2024.

[3] T. Zami, A. Morea, N. Rossi and B. Lavigne, "Performance of Core WDM Networks Equipped With 800Gb/s Coherent Pluggable Interfaces", Paper W3A.2, OFC'2026, March 2026

[4] J. Pedro, M. M. Hosseini and A. Napoli, “Extended network applications of coherent pluggable transceivers,” Journal of Optical Communications and Networking, vol. 17, no. 2, p. A210, 2025.

[5] M. Giannelis, “AARNet and Cisco Successfully Trial 400Gbps Coherent Pluggable Optics Across 4600km Network Link,” Tech Business News, 5 June 2025.