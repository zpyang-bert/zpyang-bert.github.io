---
layout: post
title:      "Experimental Demonstration of Closed-Loop Waveband Protection in S-C-L-Band IPoBDM Fiber Network using Multi-Granular Optical Nodes and TeraFlowSDN Controllers"
date:       2026-04-18 16:18:55
author:     "Bert"
tags:
  - Mineru
---
R. Emmerich1\*, A. Sgambelluri2,3, M. Enrico4, H. Zaid1, W. Akbar5, C. Schmidt-Langhorst1, J.M. Fàbrega5, D. Moor6, N. Psaromanolakis7, G. Katsikas7, D. C. Vaz8, A. Moser9, D. Rieben6, S. Hess6, L. Gifre5, R. Vilalta5, H. Neto8, P. Cabrita8, R. Muñoz5, N. Sambo2,3, D.M. Marom10, F. Rodrigues8, B Baeuerle9, J. Leuthold6, L. Poti3, I. Tomkos11, J.K. Fischer1, C. Schubert1 and R. Freund1,12

1 Fraunhofer Heinrich-Hertz-Institute, Einsteinufer 37, 10587 Berlin, Germany,

2 Scuola Superiore Sant’Anna, Pisa, Italy, 3 CNIT, Pisa, Italy, 4 HUBER+SUHNER Polatis Ltd, Cambridge, United Kingdom, 5 Centre Tecnològic de Telecomunicacions de Catalunya (CTTC), Castelldefels, Spain,

6 ETH Zurich, Institute of Electromagnetic Fields (IEF), Zurich, Switzerland, 7 UBITECH, Athens, Greece, 8 PICadvanced, 3830-352 Aveiro, Portugal, 9 Polariton Technologies, 8134 Adliswil, Switzerland 10 Institute of Applied Physics, Hebrew University of Jerusalem, Israel,

11 Department of Electrical and Computer Engineering, University of Patras, Greece,12 Technical University of Berlin, Germany \*robert.emmerich@hhi.fraunhofer.de

Abstract: This paper experimentally demonstrates multi-band IPoBDM networks based on TeraFlowSDN with service provisioning and autonomous self-healing wideband protection, utilizing wideband multi-granular optical node, spectral and polarization resolved optical performance monitoring, and a high-speed plasmonic transmitter. © 2026 The Author(s)

## 1. Introduction

The TeraFlowSDN controller (TFS) was established in recent years as a prominent open-source cloud-native softwaredefined networking (SDN) controller able to scale the management of a substantial number of flows and established a new ETSI open source group named TeraFlowSDN [1]. Recent implementations of TFS in optical networks have demonstrated several application scenarios: i) provisioning in optical networks based on space division multiplexing (SDM) and multi-band (MB) transmission [2]; ii) multi-layer orchestration involving packet and optical layers [3]; iii) vendor-neutral control of pluggable transceivers supporting digital sub-carrier multiplexing [4]. With new data plane advances in the context of bandwidth division multiplexed (BDM) flexible, scalable and energy efficient optical networking [5], additional work is required to further exploit the TFS optical controller.

New possibilities for reconfiguration based on TFS within such networks are related to switching nodes with full fiber spatial and spectral switching capabilities at different granularities based on a three-layer Multi-Granular Optical Node (MG-ON) architecture [6] that supports flex-band routing and selection of arbitrary spectral MB segments (i.e. switching portions of an optical band such as the C-band or just a slice of it), flex-band add/drop functionality and legacy wavelength access for routing, including add/drop based on traditional wavelength selective switching (WSS).

![](/img/mineru_output/Th4C.2/auto/images/3e943340b30b040453919df58c5d528badaa3a6fedb5dfc03d9d0d81a6440e12.jpg)  
Fig. 1: Experimental setup including data plane and control plan with end-to-end orchestrator, packet- and optical-SDN controller.

In this paper, we introduce a MB protection scheme, leveraging TFS for reliability purposes against soft failures – such as optical amplifier malfunction – relying on MG-ONs. Traffic recovery is performed leveraging the presence of primary and backup bands exploiting different portions of the spectrum. In the considered solution, there is no need for a per-connection end-to-end routing and spectrum assignment re-computation. The large scale and pan European integrated demonstration involves three TFS controller, four MG-ONs [6], one packaged plasmonic based modulator [7, 8] and the telemetry system leveraging a spectral resolved optical performance monitor (OPM) [9]. With respect to previous works, different innovations have been implemented: (i) TFS implementation of the complete closed loop activation for the optical domain, (ii) band-based protection scheme for the re-configuration over a backup band, (iii) management of telemetry capability for the optical bands in the MG-ONs.

## 2. Experimental Setup

Fig. 1 presents the experimental distributed setup across two lab premises: at CTTC (IP routers, packet controller, orchestrator) and at Fraunhofer HHI (optical data plane hardware, optical controller). In the data plane, four MG-ON nodes are considered, with MG-ON1 (left) and MG-ON4 (right) used to add and drop signals, while MG-ON2 and MG-ON3 (emulated nodes) act as transit. Two physically disjoint fiber links are considered: the upper space division multiplexed (SDM) link (connecting port 9o of MG-ON1 to port 1i of MG-ON4 via MG-ON2) consists of a 50 km 4- core multicore fiber (kindly provided by Heraeus Comvance) and the lower link (connecting port 10o of MG-ON1 to port 2i of MG-ON4 via MG-ON3) consists of 50 km SMF-28 Ultra fiber (kindly provided by Corning). The optical amplification in each path is achieved in the C- and L-bands with Erbium-doped fiber amplifiers (EDFAs) and in the S-band with Thulium-doped fiber amplifiers (TDFA). Following the MG-ON approach, the optical SDN controller activates four wavebands (marked as WB in Fig. 1) between MG-ON1 and MG-ON4 using the NETCONF OpenConfig southbound interface (SBI): the upper path is used for WB-S (on the S-band) and WB-C1 (on the C-band), while the lower path is exploited by WB-L (on the L-band) and WB-C2 (on the C band). WB-C2 and WB-C1 are configured to act as primary and backup wavebands, respectively. S-C-L-band super-channels (S1 and S2 represented in red, L1 and L2 in blue and C in green) are created in a noise loader stage and added as super-channels through wavelength ports (25i-29i) of the MG-ON1, together with the Channel Under Test (CUT) 80 GBd 4-QAM in the C-band (port 33i) generated by a fully packaged plasmonic IQ-modulator and received with a state of the art MB coherent receiver setup [10]. For the initial state\_a, S1 and S2 are transmitted from MG-ON1 to MG-ON4 over MG-ON2 via WB-S, L1 and L2 via WB-L and C and CUT via WB-C2 over MG-ON3. Optical band combination and separation inside the MG-ONs is experimentally realized by S-C-L-band combiners/splitters emulating the waveband selective switch (WBSS) functionality, while the optical cross connects (OXC) are implemented using an optical switch (kindly provided by H+S Polatis). The optical SDN controller adopts a gNMI streaming collector to retrieve per-waveband optical power levels from a spectrally and polarization resolved OPM attached at port 2i of MG-ON4. When the malfunction of the C-band EDFA is introduced on the lower path (impacting WB-C2), the automation loop in the optical controller detects the power level deviation, thanks to the telemetry framework, and performs automatically re-routing off all channels inside the affected waveband (WB-C2). The network moves to state\_b, with the optical controller able to reconfigure MG-ON1 and MG-ON4 to reroute C and CUT channels to the upper path via WB-C1, without reconfiguring the intermediate nodes MG-ON2 and MG-ON3 and with no impact on the other WBs.

## 3. Control Framework

As shown in Fig. 2, the closed-loop control framework operates in two main phases. The first phase is the activation of closed-loop components within the optical TFS instance to monitor MG-ONs. When the optical connectivity service is deployed, the optical controller activates the closed-loop: (i) creation of the KPI descriptor(s), (ii) creation and activation of a telemetry collector, and (iii) creation and activation of an analyzer instance for near real-time analysis (state\_a). When the Policy component detects the degradation of a waveband, the second phase of the closed-loop begins with the Automation component triggering the service update. In the considered scenario (i.e., malfunctioning of the C-band optical amplifier in the lower path), the service handler is invoked, requiring the re-routing of the channels transmitted over the affected waveband, moving to the backup waveband (i.e., a disjoint path). The optical controller reconfigures ingress and egress MG-ONs. This completes the automatic reconfiguration of bands (state\_b).

![](/img/mineru_output/Th4C.2/auto/images/93c4cec376e7240d5945c92d986079b72b64da7a880a8b4a2e77b8a21cab191d.jpg)  
Fig. 2: Control plane architecture and sequence diagram for telemetry based automatic closed-loop protection.

![](/img/mineru_output/Th4C.2/auto/images/c68d14f76c54833d0350355c6fa84910b74b3cbcb12edccf54414d6d224331c3.jpg)  
Fig. 3: Experimental results a) before and b) after the automatic reconfiguring over the TeraFlowSDN controller took place including the relevant optical spectra vs. wavelength from the setup of the optical line system in the lab and the TFS channel and band configuration state of MO-ON4

## 4. Experimental Results

Fig. 3 shows the main results of the experiments, in the two network states (a/b), including the optical spectra and the configurations of MG-ON4. In Fig. 3a, the steady state condition of the system is reported, showing the optical spectrum occupation along the link at the different MG-ONs (with C-band super-channel and CUT transmitted over WB-C2 via MG-ON3, in violet). Fig. 3b shows the network condition after the autonomous closed loop application took place, with C-band super-channel and CUT transmitted over WB-C1 via MG-ON2, in orange. The two tables highlight the MG-ON4 configurations, showing the details of the super-channels and the wavebands. In state\_a, superchannels 1 and 2 (C-band super channel and CUT) are transmitted over the waveband 2 (WB-C2), while in state\_b, the C-band super-channels are transmitted via waveband 1 (i.e., WB-C1).

## 5. Conclusions

The service provisioning and self-autonomous protection of multi-band optical connections based on TeraFlowSDN has been experimentally demonstrated in a distributed testbed including wideband multi-granular optical nodes, spectral and polarization resolved optical performance monitoring, and a high-speed plasmonic based transmitter. Closed loop automation has been successfully applied to a multi-band scenario with amplification malfunctioning.

This work was funded by the EU HORIZON-JTI-SNS-2022 program under the FLEX-SCALE Project (grant no. 101096909).

## References

[1] ETSI, “ETSI open-source Software Development Group TeraFlowSDN,” Oct. 2023, [Online]. Available: https://tfs.etsi.org.

[2] A. Sgambelluri et al., “TeraFlowSDN controlling SDM and wideband optical networks,” OFC, 2024.

[3] R. Munoz et al., “Dynamic management of IP virtual network topology over multi-granular (Wavelength and Waveband).…,” ECOC, 2024.

[4] W. Akbar et al., “Management of point-to-multipoint coherent pluggable transceivers to provision IP virtual network slice…,” ECOC, 2025.

[5] J. M. Fabrega et al., “FLEX-SCALE: A disruptive approach toward flexibly scalable energy efficient networking,” IEEE Comm Mag, 2025.

[6] C. Papapavlou et al., “Forthcoming optical x-haul infrastructure supporting 6G mobile network requirements,” JOCN, v17, I 11, 2025.

[7] U. Koch et al., “Plasmonics for Communication: Enabling 200 GBd Transmitters Through Co-Integration,” OFC, paper W3H.5, 2025.

[8] D. Moor et al., “Plasmonic Transceivers for the Terabaud Age,” IEEE Journal of Selected Topics in Quantum Electronics, v30, n4, 2024.

[9] J. M. Fabrega et al., “Cost-efficient Non-intrusive Performance Monitoring in Optical Networks Using Polarization-…,” ICTON, 2025.

[10] R. Emmerich et al., “Characterization of C-Band Coherent Receiver Front-Ends for Transmission Systems Beyond S-C-L-Band,” PTL, 2023.