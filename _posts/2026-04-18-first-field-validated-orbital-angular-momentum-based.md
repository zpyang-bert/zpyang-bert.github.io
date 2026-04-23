---
layout: post
title:      "First Field-Validated Orbital Angular Momentum-Based Submarine Communication"
date:       2026-04-18 12:54:58
author:     "Bert"
tags:
  - Mineru
---
Yongguang Xiao1 , Yingyu Chen1 , Zhibing Liu1 , Junyi Liu1 , Yuetong Shi1 , Jinkai Zhou2 , Jinpei Li1 , Ruqi Chen1 , Hanyu Gao1 , Bofan Guo3 , Cheng Du4 , Weixiong Wei4 , Xiaozhen Xie4 , Yuelin Yan5 , Lei Shen6\* , Shecheng Gao2\*, Jiajing Tu2\*, Zhengyong Liu1\*, Jie Liu1\*, Zhaohui Li1\* and Chao Lu7

1 Guangdong Provincial Key Laboratory of Optoelectronic Information Processing Chips and Systems and School of Electronics and Information Technology, Sun Yat-sen University, Guangzhou 510006, China.

2 Department of Electronic Engineering, College of Information Science and Technology, Jinan University, Guangzhou 510632, China. 3 IV-VI PIC Technology Co., Ltd, Hangzhou 310020, China.

4 Fiberhome Telecommunication Technologies Co., LTD, No.6 of the fourth Gaoxin Road, High-tech of Donghu District, Wuhan 430205, China. 5 China Mobile Communications Group Guangdong Co., Ltd. Zhuhai Branch, Zhuhai 519000, China.

6 State Key Laboratory of Optical Fiber and Cable Manufacture Technology, YOFC, Wuhan 430073, China.

7 Photonics Research Institute, Department of Electrical and Electronic Engineering, The Hong Kong Polytechnic University, Hong Kong SAR 999077, China

\*shenlei@yofc.com, gaosc825@163.com, tujiajing@jnu.edu.cn,liuzhengy@mail.sysu.edu.cn, liujie47@mail.sysu.edu.cn, lzhh88@mail.sysu.edu.cn

Abstract: We demonstrate a world-first field trial of end-to-end OAM-SDM submarine transmission with 2,232-channels in South China Sea via a hydrogen-loss-resistant and lowcrosstalk OAM cable, a uniform-gain OAM amplifier with high-spatial-efficiency pumping, and integrated mode multiplexers. © 2026 The Author(s)

## 1. Introduction

The rapid growth of the Internet and AI is driving increasing demand for communication capacity. However, singlemode fiber is limited by the nonlinear Shannon limit in the C+L band [1], making it inadequate for future needs. Space division multiplexing (SDM) offers a promising solution, with the potential to surpass the nonlinear Shannon limit and significantly boost the capacity of a single fiber [2], which is crucial for submarine cables carrying 99% of global traffic [3]. Submarine cables, however, typically support no more than 32 fiber pairs, constrained by the limited space of submarine repeater cabins and the low spatial efficiency of single-mode erbium doped fiber amplifiers (EDFAs) [4,5], which hinder capacity scaling. Overcoming these challenges requires enhancing channel density in a single fiber using SDM techniques. However, current SDM technologies, particularly those involving multiple modes in a single core, remain largely confined in laboratory, with practical deployment still a major hurdle.

The transition of SDM technology from the laboratory to practical submarine communication systems faces multiple challenges. While components and environments can be optimized in the laboratory, real-world deployment requires addressing issues like cable design, optical device manufacturing, and system robustness. Submarine cable design must account for hydrogen corrosion, fiber loss, mechanical stress, and environmental pressure to ensure stringent reliability and long-term stable transmission. Amplifier design requires high-spatial-efficiency pumping in compact size with high and uniform gain while minimizing splice loss and crosstalk. Mode multiplexer (MUX) design needs high integration and robustness with high mode purity and low insertion loss for stable operation across various environments. These challenges encountered in real-world deployment make the implementation of submarine SDM communication systems far more complex and demanding than laboratory testing.

In this work, we report a first field trial of an end-to-end OAM-SDM submarine communication system based on an undersea OAM fiber cable deployed between two islands in Zhuhai, South China Sea, as shown in Fig. 1(a)- (b). To mitigate seawater corrosion and ensure mode division multiplexing (MDM) transmission reliability, the weakly-coupled OAM cable fiber is designed with an optimized core-cladding refractive index difference (RID), supporting three mode groups (MGs) with radial order 1 $\left( \mathbf { O A M _ { 1 1 } } , \mathbf { O A M _ { 2 1 } } , \mathbf { O A M _ { 3 1 } } \right)$ . Using a matching OAM EDFA with a gain of \~20 dB in C-band and a differential mode gain (DMG) below 1 dB, together with a compact MUX with \~4.5 dB insertion loss, we demonstrate a mode/wavelength/polarization division multiplexing system using only 4×4 MIMO DSP. All 2,232 channels achieve a BER below the 20% soft-decision FEC threshold of $2 . 4 \times 1 0 ^ { - 2 }$

## 2. OAM-SDM components towards submarine application

The submarine OAM fiber cable was deployed between Guishan Island and Wailingding Island, which has a total length of 30 km, including 25-km submarine cable under the sea and 5-km long cable on the land to connect terminal houses. The optical cable contains two OAM fibers with multi-layer armored protections serving to safeguard fibers against external stress and seawater (in Fig. 1(c)). A key challenge specific to undersea deployment is seawater corrosion. An excessive doping level will cause severe hydrogen-induced loss in fibers, constraining the doping level of fiber core and thereby limiting the core-cladding RID. However, weakly-coupled fibers require a sufficiently large RID to ensure adequate mode isolation for stable operation. To address this tradeoff, the core doping level is optimized to $\Delta = 0 . 7 5 \%$ in this work, enabling support for distinct $\mathrm { O A M _ { 1 1 } , O A M _ { 2 1 } }$ and $\mathrm { O A M } _ { 3 1 }$ MGs. Through meticulous process control during fiber drawing, the fabricated fiber precisely aligns with the designed index profile, exhibiting low loss (\~0.21 dB/km) and low MG crosstalk (<-31.9 dB/km). However, mechanical stress, which is absent in laboratory verifications, gradually degrades mode purity during the process from fiber cabling to deployment (Fig. 1(e)-(f)). Despite this field-induced degradation, the optimized RID ensures the maximum crosstalk remains as low as -29.4 dB/km, enabling reliable MDM propagation in undersea conditions.

![](images/10c2ec675283631c11ad8ce7767b8387e1f442f1654bc16e88505ab2a3fdeb54.jpg)

![](images/bd03aa40496ec9bffb3bd8063b7328da0c1c0e49c8e09e2c596e47f5065306d7.jpg)

![](images/d605a6f62710c7d2beb8d5cff1f246c1fd9963c2c2294c5662037f6c2a8ca62a.jpg)

![](images/15eb726763a64f4407850af57f9d04fec357912a9b2f11fd4b4c95314210e9fe.jpg)

![](images/ed3195ca07b075df93a33f35bda11a7c8360a7e0e830dc2f2ba8793d1323b407.jpg)  
Fig. 1: (a) Map of the Guishan and Wailingding Island shows the route of the deployed OAM fiber cable. (b) Enlarged map of the testbed area, shows the OAM submarine communication system. (c) Photography of the OAM submarine cable on a cable-laying ship. (d) Refractive index profile of the OAM fiber. (e) Attenuation and (f) crosstalk change from fiber fabricating to cabling and deploying.

![](images/9122c8219380e48f9fa5c53699c25ffbc17df0d8694fe5717727a3d3ba15344e.jpg)

![](images/bace202b40169ebe37346459ceb27d18dd08e0a96b6629aa9c1e79e51f26ea2f.jpg)

![](images/2347783f7a6e2b73f84bd0d6b4d86cda9c692f9a354d581905b70272d779a56d.jpg)

![](images/760bbb19a4e934ce7872e449f0f68722d906609cf22b104eea502f58443588dc.jpg)  
Fig. 2: (a) Schema of the OAM EDFA. (b) Wavelength-dependent gain, NF, and DMG of the OAM EDFA. (c) Process of the optical mode conversion and multiplexing and photography of the packaged device. (d) Wavelength-dependent loss of the multiplexer.

To realize the OAM modes amplified in fiber, an OAM amplifier was designed, which comprises a matching 3- MG OAM EDF with a length of 3 meter, and a wavelength division multiplexer featuring a cladding-pumped structure with a high coupling efficiency exceeding 90%, as shown in Fig. 2(a). The cladding-pumped architecture minimizes the number of required pump sources and enables the simultaneous amplification of six spatial modes with high spatial utilization efficiency. This advantage facilitates its potential future application in submarine repeater cabins, allowing for the transmission of more spatial channels within a single cable. Fig. 2(b) shows wavelength-dependent characteristics of gain, noise figure (NF) and DMG at a pumping power of 5 W. Across C band, the overall average gain reaches 20 dB and the NF is less than 9 dB. Benefiting from a Er-doped scheme based on a bimodal Gaussian distribution, the DMG remains consistently low within a range from 0.2 to 1 dB.

The fabricated OAM MUX device based on multi-plane light conversion (MPLC) has a miniature integrated structure, showed by Fig. 2(c). Unlike a large-scale spatial optical coupling system, the integrated MUX device brings a reduction of \~100 times in volume and is fully compatible with field communication systems via a fiber pigtail. Fig. 2(d) shows the tested wavelength-dependent minimum, maximum and average insertion losses for all OAM modes. Across C band the MUX exhibits low insertion loss fluctuating slightly around 4.5 dB. The maximum mode differential loss is \~1 dB, demonstrating flatness over a wide wavelength range.

## 3. Field trials of the OAM-SDM submarine communication system

![](images/339813ea524ba94104bfbe543a753e1a3bdb74d8caa72dfce3c87d6d146d8034.jpg)

![](images/a53c7fea6b55f209329c2ed5abe05f061e1166f26665462a127b1c9e5979a23b.jpg)  
Fig. 3: (a) Experimental setup of the OAM-SDM submarine communication system with two OAM cable fibers, a matching amplifier and de/multiplexers devices. (b) Spectra of the input and output signals. (c) Measured BER of all 2,232 channels.

Fig. 3(a) shows the end-to-end OAM-SDM communication system setup based on the deployed submarine OAM cable with all matched components including OAM amplifier and packaged OAM MUX devices. 186 C-band WDM channels are modulated into 24G-QPSK dual-polarization signals, multiplexed via an OAM MUX and launched into a 60-km fiber link of two OAM fibers in the optical cable. At the end of cable link, an OAM amplifier is installed before a DEMUX to guarantee enough power for receiving signal, which is subsequently recovered by a 4×4 MIMO at receiver. Fig. 3(b) plots the optical spectra of three MGs on the transmitter and receiver side. As shown in Fig. 3(c), the BER is counted for 2,232 channels (comprising 186 wavelengths, 3 mode groups, 2 topological states, and 2 polarization states). As a result, it remains below the 20% soft-decision FEC threshold of $2 . 4 \times 1 0 ^ { - 2 } .$ achieving a transmission with a data capacity of 107 Tbit/s just in C Band.

## 4. Conclusions

This work demonstrates a first field trial of end-to-end OAM-SDM submarine transmission between two islands in Zhuhai. Using all OAM compatible components and 4×4 MIMO DSP, we achieved 2,232-channel (107 Tbit/s) transmission with BER below the 20% soft-FEC threshold, verifying OAM-SDM viability for submarine communications.

## 5. Acknowledgement

This work was financially supported by the National Key Research and Development Program of China under Grant (2024YFB2908100), and Guangdong S &T Programme (2024B0101030001). The OAM multiplexer and cladding pumping OAM EDFA in this work is packaged by IV-VI PIC Technology Co., LTD.

## 6. References

[1] P. J. Winzer et al., "Fiber-optic transmission and networking: the previous 20 and the next 20 years," Optics Express, 26, 24190–24239 (2018).

[2] M. van den Hout et al., "Reaching the pinnacle of high-capacity optical transmission using a standard cladding diameter coupled-core multicore fiber," Nature Communications, 16, 3833 (2025).

[3] J. Chesnoy, "Presentation of submarine fiber communication," Undersea Fiber Communication Systems, Academic Press, 3–19 (2016).

[4] J. D. Downie et al., "Assessing capacity and cost/capacity of 4-core multicore fibers against single core fibers in submarine cable systems," Journal of Lightwave Technology, 38, 3015–3022 (2020).

[5] M. A. Bolshtyansky et al., "Single-mode fiber SDM submarine systems," Journal of Lightwave Technology, 38, 1296–1304 (2020).