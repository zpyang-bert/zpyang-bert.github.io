---
layout: post
title:      "Digital Signal Processing for Optical Coherent Communication Systems"
date:       2026-04-19 00:27:45
author:     "Bert"
tags:
  - DSP
  - Mineru
  - Optical
  - Systems
---
Zhang, Xu

Publication date: 2012

Document Version Publisher's PDF, also known as Version of record

Link back to DTU Orbit

Citation (APA):   
Zhang, X. (2012). Digital Signal Processing for Optical Coherent Communication Systems. Technical University of Denmark.

# Digital Signal Processing for Optical Coherent Communication Systems

Xu Zhang

Delivery Date: April 27th 2012

DTU Fotonik

Department of Photonics Engineering

Technical University of Denmark

Building 343

2800 Kgs. Lyngby

DENMARK

DTU Fotonik

## Abstract

In this thesis, digital signal processing (DSP) algorithms are studied to compensate for physical layer impairments in optical fiber coherent communication systems. The physical layer impairments investigated in this thesis include optical fiber chromatic dispersion, polarization demultiplexing, light sources frequency and phase offset and phase noise. The studied DSP algorithms are considered as key building blocks in digital coherent receivers for the next generation of optical communication systems such as 112-Gb/s dual polarization (DP) quadrature phase shift keying (QPSK) optical transmission links.

Highlight results presented in this PhD thesis include three areas. First, we present an experimental demonstration of enhanced tolerance to phase noise using pilot-tone-aided phase noise mitigation DSP algorithms. To the best of our knowledge, it is the first experimental demonstration of high phase noise tolerance of 40-Gb/s coherent DP-QPSK systems using vertical cavity surface emitting lasers (VCSELs) as transmitter and local oscillator lasers. Second, in order to fulfill the strict constrains of spectral efficiency, this thesis shows the pioneering experimental demonstration of high spectrum narrowing tolerance 112-Gb/s DP-QPSK optical coherent systems using digital adaptive equalizer. The demonstrated results show that off-line DSP algorithms are able to reduce the bit error rate (BER) penalty induced by signal spectrum narrowing. Third, we also investigate bi-directional transmission of carrierless amplitude and phase (CAP) modulation format signal. In this thesis we focus on the experimental demonstration of DSP channel estimation implementations with CAP signal in the bi-directional optical transmission system.

Furthermore this thesis proposes reconfigurable and ultra dense wavelength division multiplex (U-DWDM) optical coherent systems based on 10-Gbaud QPSK. We report U-DWDM 1.2-Tb/s QPSK coherent system achieving spectral efficiency of 4.0-bit/s/Hz. In the experimental demon-

stration, digital decision feed back equalizer (DFE) algorithms and a finite impulse response (FIR) equalizer algorithms are implemented to reduce the inter channel interference (ICI). This PhD thesis also investigates a parallel block-divided overlapped chromatic dispersion DSP compensation algorithm. The essential benefit of using a parallel chromatic dispersion compensation algorithm is that it demands less hardware requirements than a conventional serial chromatic dispersion compensation algorithm.

In conclusion, the digital signal processing algorithms presented in this thesis have shown to improve the performance of digital assisted coherent receivers for the next generation of optical fiber transmission links.

## Abstrakt

I denne afhandling studeres algorithmer til processering af digitale signaler (digital signal processing - DSP), med det form˚al at kompensere for fysiske begrænsninger i koherente optiske fiberkommunikationssystemer. De fysiske begrænsninger som adresseres i denne afhandling ang˚ar den kromatiske dispersion i fiberen, polarisations demultipleksning, off-set i lyskildernes frekvens og fase, samt fasestøj. De undersøgte DSP algorithmer regnes som kerneelementer i koherente digitale modtagere til brug i fremtidige optiske kommunikationssystemer, s˚asom 112-Gb/s ”dual polarization (DP) quadrature phase-shift keying (QPSK)” optiske transmissionssystemer.

De vigtigste resultater fra denne PhD afhandling kan opdeles i tre omr˚ader. Først præsenteres en eksperimental demonstration af forbedret tolerance over for fasestøj med DSP algorithmer som reducerer støjen vha. en ”pilot-tone”. Dette er s˚a vidt vides den første eksperimentelle demonstration af høj fasestøjstolerance i 40-Gb/s koherente DP-QPSK systemer baseret p˚a ”vertical cavity surface emitting lasers” (VCSELs). Dernæst præsenteres et pionerforsøg hvori der demonstreres høj tolerance over for spektral begrænsning (”spectral narrowing”) i 112-Gb/s DP-QPSK koherente optiske kommunikationssystemer, hvilket har stor betydning for den spektrale effektivitet. Resultaterne fra dette forsøg viser at off-line DSP algorithmer kan reducere den bit error rate (BER) penalty som opst˚ar pga. den spektrale begrænsning. For det tredje undersøges bi-direktionel transmission af ”carrier-less amplitude- og fase-modulerede” (CAP) signaler. I denne afhandling fokuseres der p˚a den eksperimentelle implementering af DSP baseret kanal estimering i bi-direktionelle optiske transmissionssystemer med CAP signaler.

Denne afhandling indeholder ogs˚a et forslag til rekonfigurerbare, ”ultradense wavelength division multiplexed” (U-DWDM) optiske koherente systemer baseret p˚a 10-Gbaud QPSK. Vi demonstrerer et U-DWDM 1.2-Tb/s

QPSK koherent system med en spektral effektivitet p˚a 4.0 bit/s/Hz. I dette eksperiment anvendes s˚akaldte ”digital decision feed back equalizer” (DFE) og ”finite impulse response (FIR) equalizer” algorithmer til at reducere interferensen mellem kanalerne. Denne afhandling undersøger ogs˚a en s˚akaldt ”parallel block-divided overlapped chromatic dispersion DSP compensation” algoritme. Denne algoritme har den væsentlige fordel at den stiller mindre krav til hardwaren i forhold til konventionelle, serielle kromatiske dispersionskompenserings algoritmer.

Det konkluderes at de DSP algoritmer som præsenteres i denne afhandling p˚aviseligt kan forbedre koherente digitale modtagere i den næste generation af optiske transmissionssystemer.

## Resum´e

Xu Zhang er født i Tianjin City, Kina, i 1983. Han modtog B.Sc. graden i Electronic Science and Technology fra Jilin University i Changchun, Kina, i 2006. Dernæst modtog han M.Sc. graden i Radio Frequency Communication Engineering fra Southampton University, Southampton, England, i 2008. P˚a nuværende tidspunkt er Xu Zhang Ph.-d. studerende p˚a Institut for Fotonik ved Danmarks Tekniske Universitet. Hans nuværende forskningsomr˚ader er højhastigheds koherent optisk kommunikation og digital signal processerings teknologi.

# Acknowledgements

First, I want to express my gratitude to my supervisor, Professor. Idelfonso Tafur Monroy. Professor, I could not finish this thesis without your support, you gave me a lot of suggestions and criticisms with your rich research experience. I have learnt so much form you, not only about scientific knowledge, but also the professional ethics. I am grateful to my co-supervisor, Associate Professor Darko Zibar, for helping me to solve a lot of fundamental problems and provide me many useful guidance.

And I would like to express my sincere gratitude to my co-supervisor Richard Younce from Tellabs US and Gert Schiellerup from Tellabs Denmark for supporting me and always giving valuable input at project meeting.

I also would like to thank my colleagues at DTU Fotonik metro access group, Xiaodan, Lei, Ying, Xianbin, Jesper, Antonio, Robert, Roberto, Valeria, Alexander, Thang, Silvia, and special thanks to Maisara for your home made delicious noodles, for your always kindly supporting.

To my family in China, Mom Xiuzhen Liu, Dad Cungen Zhang, thanks for your always supporting and encouraging me from the very beginning of my study. Special thanks to my wife, Qian, I couldn’t always stay with you, but you never complain and always support me.

And last but not least, thanks to my best friends Evarist,Janaina, Kamau, Neil, Hua Ji, Jin Liu, ... list is too long, but you are all and always in my heart.

# Summary of Original Work

This thesis is based on the following original publications:

[1] Xu Zhang, Darko Zibar, Idelfonso Tafur Monroy, Richard Younce. “Engineering rules for chromatic dispersion compensation in digital receivers for optical coherent PolMux QPSK links”, IEEE Photonics Society, 2010 23rd Annual Meeting of the, Nov 2010.

[2] Xu Zhang, Valeria Arlunno, Jesper B. Jensen, Idelfonso Tafur Monroy, Darko Zibar and Richard Younce. “1.2 Tb/s ultradense WDM long reach and spectral efficiency access link with digital detection”, Photonics Conference (PHO), 2011 IEEE, Nov 2011.

[3] Xu Zhang. and Xiaodan Pang. and Anton Dogadaev. and Idelfonso T. Monroy. and Darko Zibar. and Richard Younce. “High Spectrum Narrowing Tolerant 112 Gb/s Dual Polarization QPSK Optical Communication Systems using Digital Adaptive Channel Estimation”, in Proceedings of the Optical Fiber Communication Conference and Exposition and the National Fiber Optic Engineers Conference, OFC’2012, Los Angles, CA, USA., paper number JW2A.49, March 2012.

[4] Valeria Arlunno, Xu Zhang, Knud J. Larsen, Darko Zibar, and Idelfonso Tafur Monroy. “Digital non-linear equalization for flexible capacity ultradense WDM channels for metro core networking”, in Proceedings of the 37th European Conference on Optical Communication, ECOC’2011, Geneva, Switzerland, September 2011.

[5] Valeria Arlunno, Xu Zhang, Knud J. Larsen, Darko Zibar, and Idelfonso Tafur Monroy. “Digital non-linear equalization for flexible capacity ultradense WDM channels for metro core networking”, Opt. Express, vol. 19, no. 26, pp. B270-B276, 2011.

[6] Robert Borkowski, Xu Zhang, Darko Zibar, Richard Younce, and Idelfonso Tafur Monroy. “Experimental adaptive digital performance monitoring for optical DP-QPSK coherent receiver”, in Proceedings of the 37th European Conference on Optical Communication, ECOC’2011, Geneva, Switzerland, September 2011.

[7] Robert Borkowski, Xu Zhang, Darko Zibar, Richard Younce, and Idelfonso Tafur Monroy. “Experimental demonstration of adaptive digital monitoring and compensation of chromatic dispersion for coherent DP-QPSK receiver”, Opt. Express, vol. 19, no. 26, pp. B728- B735 2011.

## Other scientific reports associated with the project:

[8] Neil Guerrero Gonzalez, Antonio Caballero Jambrina, Robert Borkowski, Valeria Arlunno, Tien Thang Pham, Roberto Rodes, Xu Zhang, Maisara Binti Othman, Kamau Prince, Xianbin Yu, Jesper B. Jensen, Darko Zibar and Idelfonso Tafur Monroy. ”Reconfigurable Digital Coherent Receiver for Metro-Access Networks Supporting Mixed Modulation Formats and Bit-rates”, accepted for oral presentation at the Optical Fiber Communication Conference and Exposition and the National Fiber Optic Engineers Conference OFC’2011, Los Angeles, USA., paper number OMW7, March 2011.

[9] Maisara Binti Othman, Jesper B. Jensen, Xu Zhang, and Idelfonso Tafur Monroy. “Performance evaluation of spectral amplitude codes for OCDMA PON” Optical Network Design and Modeling (ONDM), 2011 15th International Conference on Feb. 2011.

[10] Lei Deng, D. Liu, Xiaodan Pang, Xu Zhang, Valeria Arlunno, Ying Zhao, Antonio Caballero Jambrina, Anton K. Dogadaev, Xianbin Yu, Idelfonso Tafur Monroy, M. Beltr´an, and R. Llorente. “42.13 Gbit/s

16QAM-OFDM photonics-wireless transmission in 75-110 GHz band” Electromagnetic Waves, vol. 126, pp. 449-461, 2012.

[11] Lei Deng, Marta Beltran, Xiaodan Pang, Xu Zhang, Valeria Arlunno, Ying Zhao, Xianbin Yu, Roberto Llorente, Deming Liu, and Idelfonso Tafur Monroy. “Fiber Wireless Transmission of 8.3-Gb/s/ch QPSK-OFDM Signals in 75–110-GHz Band”, IEEE Photonics Technology Letters, vol. 24, no. 5, pp. 383-385, 2012.

## Contents

Abstract i   
Abstrakt iii   
Resum´e v   
Acknowledgements vii   
Summary of Original Work ix   
1 Introduction 1   
1.1 Motivation 1   
1.2 State-of-the-art 2   
1.3 Objective and Scope 3   
1.4 Contributions . . 3   
1.5 Structure of the Thesis . 4   
2 Coherent Detection for optical 100 Gb/s Links 7   
2.1 Introduction . 7   
2.2 Theory Overview of Coherent Detection 9   
2.2.1 Single Coherent Detection with Single Photodiode . 9   
2.2.2 Single Coherent Detection with Balanced Photodiode 10   
2.2.3 Quadrature Coherent Detection with 90◦-hybrid 11   
2.2.4 Dual Polarization Coherent Detection . . . 13   
2.2.5 Homodyne and Heterodyne Coherent Detection 14   
2.3 Transmission impairments in optical 100 Gb/s links 16   
2.3.1 Fiber Losses . 17   
2.3.2 Chromatic Dispersion 18   
2.3.3 Polarization Mode Dispersion 19   
2.3.4 Nonlinear Transmission Impairments 21   
2.3.5 Four Wave Mixing 22   
2.4 Summary 23   
3 Coherent Detection with DSP Algorithms 2 5   
3.1 Introduction . 25   
3.2 Chromatic Dispersion Compensation DSP Algorithm . 26   
3.3 Clock Recovery DSP Algorithm . 30   
3.4 Polarization Demultiplexing DSP Algorithm . 31   
3.5 Carrier Recovery DSP Algorithm . 34   
3.5.1 Viterbi-Viterbi Carrier Recovery Algorithm 34   
3.5.2 Pilot-aided Phase Noise Cancellation DSP Algorithm 36   
3.6 Spectrum Narrowing induced Inter Symbol Interference Com  
pensation DSP Algorithm 44   
3.7 Summary 52   
4 DSP Algorithms for Multi Dimension CAP Modulation 53   
4.1 Introduction . . 53   
4.2 Theoretical Overview of CAP Technique . 54   
4.3 DSP Algorithms for CAP Transmission Channel Estimation 59   
4.3.1 Theoretical overview of blind CMA Equalizer 59   
4.3.2 Bi-directional Multi Dimension CAP transmission demon  
stration 61   
4.4 Summary 68   
5 Ultra Dense WDM Systems with Coherent Detection 69   
5.1 Introduction . . 69   
5.2 Generation of Ultra Dense WDM Channels 70   
5.3 1.2 Tb/s Ultra Dense WDM System 71   
5.3.1 Ultra Dense WDM System Experiment Setup 72   
5.3.2 Experiment Results and Analysis 73   
5.3.3 Decision Feedback Equalizer . 76   
5.4 Summary 78   
6 Conclusion and Outlook 7 9   
Paper 1: Engineering Rules for Chromatic Dispersion Compensation   
in Digital Receivers for Optical Coherent PolMux QPSK Links 83   
Paper 2: 1.2 Tb/s ultredense WDM long reach and spectral efficiency   
access link with digital detection 87   
Paper 3: High Spectrum Narrowing Tolerant 112 Gb/s Dual Polariza  
tion QPSK Optical Communication Systems using Digital Adaptive   
Channel Estimation 91   
Paper 4: Digital non-linear equalization for flexible capacity ultra  
dense WDM channels for metro core networking 95   
Paper 5: Digital non-linear equalization for flexible capacity ultra  
dense WDM channels for metro core networking 99   
Paper 6: Experimental adaptive digital performance monitoring for   
optical DP-QPSK coherent receiver 107   
Paper 7: Experimental demonstration of adaptive digital monitoring   
and compensation of chromatic dispersion for coherent DP-QPSK   
receiver 111   
Bibliography 121

# Chapter 1

# Introduction

This thesis studies the implementation of digital signal processing algorithms for coherent optical communication systems. In this introduction chapter, we will elaborate on the motivation of this research and explain the significance of digital signal processing for next generation of optical communication systems.

## 1.1 Motivation

Today’s telecommunication services intensely rely on optical-fiber systems. Such optical communication systems are requested to handle high speed, multi-channels, long-haul signal transmission [1]. Recently, optical coherent 100 Gb/s communication links became a critical technology for communication networks. Moreover, digital signal processing is under consideration as a promising technique for optical signal modulation, fiber transmission, signal detection and dispersion compensation. There are different reasons why the utilization of coherent detection associated digital signal processing can be very beneficial. Firstly, coherent detection is a promising technology to increase optical receiver sensitivity, permitting a greater span loss to be tolerated. Secondly, coherent detection enables supporting of more spectrally efficient modulation formats such as quadrature phase shift keying (QPSK) and quadrature amplitude modulation (QAM). And finally, instead of implementing costly physical impairments compensation links, coherent detection allows digital signal processing for compensation of transmission impairments such as chromatic dispersion (CD), polarization mode dispersion (PMD), signal carrier offset, spectrum narrowing, etc. Furthermore, next generation optical transmission systems require adaptive fitting for time varying transmission impairments such as channel spectrum narrowing and random phase noise. Digital signal processing is a powerful solution for future adaptive optical transmission links.

## 1.2 State-of-the-art

Since 2007, coherent detection has been considered as the key technology of optical communication systems [2]. Major challenge for future optical transmission systems is the strict frequency band usage limitation, which is measured by spectral efficiency (SE). In order to improve spectral efficiency, coherent detection with advanced modulation formats has become promising solution. The development trend of advanced modulation formats implementation is shown in Figure 1.1 [3].

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/2edd4fcd6dd8ee2cbea3d2d34cf930ce65afba316fd5781ca2d29cdcc70e5f3b.jpg)  
Figure 1.1: Advanced modulation formats development trend.

Table 1.1 shows recent high spectral efficiency transmission experiment achievements over single mode fiber (SMF) transmission. As it can be noticed, such innovative optical transmission experiment results are all achieved by using coherent detection with digital signal processing implementation [4–8].

<table><tr><td>year/Ref.</td><td>Capacity</td><td>Modulation</td><td>SE (bit/Hz/s)</td><td>Distance (km)</td></tr><tr><td>2008 [4].</td><td>17 Tb/s</td><td>8PSK</td><td>4.2</td><td>662</td></tr><tr><td>2009 [5].</td><td>34 Tb/s</td><td>8QAM</td><td>4</td><td>580</td></tr><tr><td>2010 [6].</td><td>11.2 Tb/s</td><td>64QAM</td><td>6.4</td><td>240</td></tr><tr><td>2011 [7].</td><td>101.7 Tb/s</td><td>128QAM</td><td>11</td><td>165</td></tr><tr><td>2012 [8].</td><td>102.3 Tb/s</td><td>64QAM</td><td>9.1</td><td>240</td></tr></table>

Table 1.1: Experiment achievements for high capacity and spectral efficiency over SMF.

## 1.3 Objective and Scope

The objective and scope of this Ph.D. project is the investigation of various digital signal processing algorithms for compensation of different types of optical transmission impairments. For instance, we considered chromatic dispersion, polarization mode dispersion, signal carrier frequency offset, phase offset and spectrum narrowing compensation. According to such targets, this work focuses on system performance improvement by using novel structure and digital signal processing algorithms.

## 1.4 Contributions

PAPER 1 provided the first engineering rules for block length of blockoverlap chromatic dispersion (CD) compensation DSP algorithm. We consider block-overlap chromatic dispersion compensation in optical coherent dual polarization quadrature phase shift keying (DP-QPSK) links. In general, proposed algorithm enabled 112 Gb/s DP-QPSK transmission in simulation with different values of CD, and 20 Gb/s QPSK 40 km SMF transmission with experimental demonstration.

PAPER 2 demonstrated an ultra dense WDM coherent DP-QPSK system with sub-channels spaced at baud rate achieving 4.0 b/s/Hz spectral efficiency and aggregate capacity of 1.2 Tb/s bit rate over 80 km SMF transmission for long reach metro-access networking.

PAPER 3 demonstrated a high spectrum narrowing tolerant 112-Gb/s QPSK polarization multiplex system based on digital adaptive channel estimation method. The proposed algorithm is able to detect severe spectrumnarrowed signal even with 20 GHz 3 dB bandwidth.

PAPER 4 experimentally demonstrated that DSP algorithm of digital non-linear equalization allows for using independent tunable distributed feedback (DFB) lasers spaced at 12.5 GHz for ultra dense WDM PM-QPSK flexible capacity channels for metro networks.

PAPER 5 experimentally demonstrated ultra dense WDM with advanced digital signal processing. We demonstrated that a digital non-linear equalization allows to mitigate inter-channel interference and improve overall system performance in terms of OSNR. Evaluation of the algorithm and comparison with an ultra dense WDM system with coherent carriers generated from a single laser are also reported.

PAPER 6 presented an experimental demonstration of a digital optical performance monitoring (OPM) yielding satisfactory estimation accuracy along with adaptive impairment equalization. No observable penalty is measured when equalizer is driven by monitoring module.

PAPER 7 demonstrated DSP-based optical performance monitoring algorithm for CD monitoring in coherent transport networks. Dispersion accumulated in 40 Gb/s QPSK signal after 80 km SMF transmission is successfully monitored and automatically compensated without prior knowledge of fiber dispersion coefficient. Moreover, four different metrics for assessing CD mitigation are implemented and simultaneously verified proving to have high estimation accuracy.

## 1.5 Structure of the Thesis

This thesis is divided into six chapters. In order to facilitate understanding the work in this thesis, chapter 2 will give an general introduction to the essential theoretical concepts in coherent detection for optical 100 Gb/s transmission systems. Chaper 3 studies off-line DSP impairments compensation algorithms including chromatic dispersion compensation, polarization demultiplexing, carrier recovery, pilot-tone-aided phase noise cancellation, and adaptive spectrum narrowing compensation DSP algorithm for 112 Gb/s DP-QPSK coherent transmission experiment.

In chapter 4, optical advanced modulation formats using multi dimensional carrierless amplitude and phase (CAP) modulation are studied. Chapter 4 focus on experimental demonstration of DSP channel estimation implementations with CAP signal in the bi-directional optical transmission

system.

Chapter 5 will introduce ultra dense wavelength division multiplexing (WDM) optical transmission systems with coherent detection. 1.2 Tb/s dual polarization (DP) QPSK ultra dense WDM experiment results are presented. Moreover, inter channel interference compensation DSP algorithm is also be demonstrated.

Eventually chapter 6 draws the conclusions from the research results of this thesis. Furthermore, chapter 6 presents on outlook about the next generation of optical transmission systems and future DSP evolvement.

# Coherent Detection for optical 100 Gb/s Links

## 2.1 Introduction

Nowadays optical communication networks are severely challenged by enormous growth in the amount of data traffic transported over telecommunication networks [9]. As it is shown in Figure 2.1, fiber transmission systems are the backbone of core and metro access networks. Increasing number of optical line terminals (OLTs) urgently requires rapid growth of transmission system capacity. For instance, data rate demand of core network has developed from 10 Gb/s, 40 Gb/s towards 100 Gb/s.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/8c6336bce118636d9ea06064694643d8d0003d3b5719011d49622801e4146ef8.jpg)  
Figure 2.1: Structure of optical communication links.

Before the first appearance of the prototype erbium doped fiber amplifier (EDFA) [10], there were intensive researches concerning coherent detection techniques [11–15]. Due to the characteristic of receiver sensitivity enhancement, coherent detection was under consideration as a feasible solution for long distance transmission applications [16]. However, since the early of 1990s, employments of EDFA, dispersion compensating fiber (DCF), and on-off keying modulation have emerged as a simple and practical solution for optical communication systems.

During the last decade, capacity demand from telecommunication transports has experienced unprecedented growing [17]. However going towards 100 Gb/s data rate using only binary modulation and intense modulation direct detection (IM/DD) has been proved problematic, due to the mitigation of the increasing impact of fiber transmission impairments such as polarization mode dispersion (PMD) [18].

Meanwhile with the rapid development of integrated circuit [19], analogue to digital conversion processing speed is increasing by a factor of four every five years [20]. For instance, in 2007, reasonable analogue to digital conversion processing speed is 20 GSa/s [21]. In 2012, highly complex and commercial available analogue to digital convertor (ADC) is as fast as 80 GSa/s [22]. Nowadays’ ADC processing capability is possible and practical to perform extensive signal processing at the required data rates such as 100 Gb/s. Therefore coherent detection has come back as a promising solution for high capacity optical transmission link [23–25]. Moreover, in order to implement higher capacity and higher spectral efficiency optical transmission systems, coherent detection with high order modulation formats has been proposed. Different from IM/DD, coherent detection can take advantage of mature developed digital signal processing technique to compensate for fiber transmission impairments

In chapter 2, basic concepts and theoretical analysis of coherent detection will be introduced. Both of the advantages and disadvantages of coherent detection will be discussed. Chapter 2 is divided into three sections. After introduction, section 2.2 introduces basic concepts of coherent detection for optical 100 Gb/s link. Furthermore, section 2.2 will compare various coherent detection schematics and focus on dual polarization quadrature balanced coherent detection. Finally, section 2.3 presents major transmission impairments associated with optical 100 Gb/s link.

## 2.2 Theory Overview of Coherent Detection

In coherent detection systems, a complex modulated signal, whose information lies not only on its amplitude but phase as well, can be written as

$$
E _ { S } ( t ) = A _ { S } ( t ) \exp [ i ( \omega _ { S } t + \phi _ { S } ) ] ,\tag{2.1}
$$

where $\omega _ { s }$ and $\phi _ { s }$ are the signal’s carrier frequency and time dependent phase variable, and $A _ { S } ( t )$ is the amplitude component of the signal. The optical field associated with the local oscillator (LO) can be written as

$$
E _ { L O } ( t ) = A _ { L O } ( t ) \exp [ i ( \omega _ { L O } t + \phi _ { L O } ) ] ,\tag{2.2}
$$

where $\omega _ { L O } , A _ { L O } ( t )$ and $\phi _ { L O }$ are respectively the carrier frequency, amplitude and time dependent phase variable of the LO. The scalar notation is used for both $E _ { S } ( t )$ and $E _ { L O } ( t )$ due to assuming that two fields are identically polarized [26]. Moreover, in section 2.2, four different coherent detection schematics are under investigation, which are denoted as single coherent detection with single photodiode (PD), single coherent detection with balanced-photodiode (B-PD), quadrature coherent detection with $9 0 ^ { \circ } ,$ hybrid and dual polarization coherent detection.

## 2.2.1 Single Coherent Detection with Single Photodiode

Figure 2.2 shows the schematic of single coherent detection with single PD.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/11b89c9c798d6d8735675e8f279d578711945d104c9487d09a6b0bd0e36d111e.jpg)  
Figure 2.2: Single coherent detection with single PD.

As it can be seen, before optical field combination with optical 3 dB coupler, branches of received signal $E _ { S } ( t )$ , and LO $E _ { L O } ( t )$ respectively propagates through polarization controllers (PC), which are employed to control the polarization states. Afterward single PD is implemented to detect the received signal combined with LO. In this theoretical analysis, shot noise and thermal noise is assumed to be ignorable. Let the complex response for 3 dB coupler be given as

$$
{ \frac { 1 } { \sqrt { 2 } } } \left[ \begin{array} { l l } { 1 } & { i } \\ { i } & { 1 } \end{array} \right] ,\tag{2.3}
$$

where $i = \sqrt { - 1 }$ When the received signal $E _ { S } ( t )$ , and LO $E _ { L O } ( t )$ is incident on the coupler, the input signal to PD is presented as,

$$
E _ { i n } = \frac { 1 } { \sqrt { 2 } } \left[ \begin{array} { c c } { 1 } & { i } \\ { i } & { 1 } \end{array} \right] \left[ \begin{array} { c } { E _ { S } ( t ) } \\ { E _ { L O } ( t ) } \end{array} \right] = \frac { 1 } { \sqrt { 2 } } \left[ \begin{array} { c } { E _ { S } ( t ) + i E _ { L O } ( t ) } \\ { E _ { L O } ( t ) + i E _ { S } ( t ) } \end{array} \right] ,\tag{2.4}
$$

According to PD characteristic of square intensity, output from PD is given by $E _ { o } = R | E _ { S } + i E _ { L O } | ^ { 2 }$ , where R is a factor of detector responsivity1. Using Equation 2.1 and 2.2

$$
P _ { o } ( t ) = P _ { o } + P ( t ) \sin [ \Delta \omega t + \Delta \phi ] ,\tag{2.5}
$$

$$
P _ { o } = A _ { L O } ^ { 2 } ( t ) + A _ { S } ^ { 2 } ( t ) , \quad a n d \quad P ( t ) = 2 A _ { L O } ( t ) A _ { S } ( t ) ,\tag{2.6}
$$

where $\Delta \omega = | \omega _ { S } - \omega _ { L O } |$ is known as the intermediate frequency (IF) or frequency offset. Moreover $\Delta \phi = | \phi _ { S } - \phi _ { L O } |$ is defined as phase offset between received signal and LO. For simplicity, in Equation 2.5 shot and thermal noise from PD are assumed to be ignored. In this case, DC component from PD output can be discarded by using DC-block after PD. Due to carrier frequency centered at IF, the last two items of Equation 2.5 will remain, and represent the information of transmitted signal.

As it can be noticed from Equation 2.6, received signal is amplified by LO. This shows directly advantage of coherent detection in a system without any pre-amplification. While all of the analysis are based on noise ignorable assumption, single coherent detection with single PD is not able to reduce short and thermal noise effect. Such in-band noise will severely effect systems performance. Optical signal to noise ratio (OSNR) requirement is extremely high in the case of single coherent detection with single PD.

## 2.2.2 Single Coherent Detection with Balanced Photodiode

In order to improve OSNR tolerance of coherent detection system, schematic of single coherent detection with balanced PD is presented as in Figure 2.3.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/e427d5592b00065881f79d18bc4b9d402deeea0dfa3e8596957b06992aecf752.jpg)  
Figure 2.3: Single coherent detection with balanced PD.

Balanced PD employs two photodiodes cascaded configuration [27–29]. Using Equation 2.4 and Equation 2.5, outputs of two cascaded PD are presented respectively as

$$
E _ { 1 } ^ { + } ( t ) = P _ { o } + P ( t ) \sin [ \Delta \omega t + \Delta \phi ] + n _ { R I N } ( t ) ,\tag{2.7}
$$

$$
E _ { 1 } ^ { - } ( t ) = P _ { o } - P ( t ) \sin [ \Delta \omega t + \Delta \phi ] + n _ { R I N } ^ { ' } ( t ) ,\tag{2.8}
$$

where $n _ { R I N } ( t )$ and $n _ { R I N } ^ { ' } ( t )$ are relative intensity noises (RIN) of two received signals respectively. The thermal noise is assumed to be ignorable. Furthermore RIN from local oscillator and signal lasers are assumed to be identical. Therefore the substraction result of two cascaded balanced PD outputs is given as

$$
\begin{array} { r } { E _ { 1 } ( t ) = E _ { 1 } ^ { + } ( t ) - E _ { 1 } ^ { - } ( t ) = 2 P ( t ) \sin [ \Delta \omega t + \Delta \phi ] . } \end{array}\tag{2.9}
$$

Compared to single coherent detection with single PD, balanced detection is able to enhance the OSNR tolerance. This shows obviously advantage of coherent detection in a high sensitivity required system, such as near quantum-limited transmission [30] and unamplified application [31]. However, as it can be noticed from both of section 2.2.1 and section 2.2.2, degree of modulation freedom for coherent detection is only one. That means either only amplitude or only phase information can be detected. High level modulation formats require quadrature coherent detection.

## 2.2.3 Quadrature Coherent Detection with 90◦-hybrid

The schematic of quadrature coherent detection with 90◦-hybrid is shown as Figure 2.4. Compared to two types of coherent detection discussed before, quadrature coherent detection can detect both of amplitude and phase

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/4a603b00963fb975528e9849fa6a319338721719c6caf12ff51e7ba44f1c4842.jpg)  
Figure 2.4: Quadrature coherent detection with balanced PD.

information simultaneously. $9 0 ^ { \circ }$ -hybrid is simply assembled by optical couplers and fibers [32–34].

As it is shown in Figure 2.4, outputs from two balanced PD $E _ { 1 }$ $E _ { 2 }$ present in-phase and quadrature parts of transmitted signal respectively.

$$
\left[ \begin{array} { c c } { E _ { 1 } ^ { + } } \\ { E _ { 1 } ^ { - } } \\ { E _ { 2 } ^ { + } } \\ { E _ { 2 } ^ { - } } \end{array} \right] = \left[ \begin{array} { c c } { | E _ { S } + E _ { L O } | ^ { 2 } } \\ { | E _ { S } - E _ { L O } | ^ { 2 } } \\ { | E _ { S } + i E _ { L O } | ^ { 2 } } \\ { | E _ { S } - i E _ { L O } | ^ { 2 } } \end{array} \right] ,\tag{2.10}
$$

$$
\left[ \begin{array} { l } { E _ { 1 } ^ { + } } \\ { E _ { 1 } ^ { - } } \\ { E _ { 2 } ^ { + } } \\ { E _ { 2 } ^ { - } } \end{array} \right] = \left[ \begin{array} { l } { P _ { o } + P ( t ) \cos [ \Delta \omega t + \Delta \phi ] + n _ { I } ( t ) } \\ { P _ { o } - P ( t ) \cos [ \Delta \omega t + \Delta \phi ] + n _ { I } ^ { ' } ( t ) } \\ { P _ { o } + P ( t ) \sin [ \Delta \omega t + \Delta \phi ] + n _ { Q } ( t ) } \\ { P _ { o } - P ( t ) \sin [ \Delta \omega t + \Delta \phi ] + n _ { Q } ^ { ' } ( t ) } \end{array} \right] ,\tag{2.11}
$$

where $P _ { o } = A _ { L O } ^ { 2 } ( t ) + A _ { S } ^ { 2 } ( t )$ $P ( t ) = 2 A _ { L O } ( t ) A _ { S } ( t )$ . After $9 0 ^ { \circ }$ -hybrid, the outputs from balanced can be presented as

$$
\begin{array} { r } { E _ { I } ( t ) = E _ { 1 } ^ { + } ( t ) - E _ { 1 } ^ { - } ( t ) = 2 P ( t ) \cos [ \Delta \omega t + \Delta \phi ] , } \end{array}\tag{2.12}
$$

$$
E _ { Q } ( t ) = E _ { 2 } ^ { + } ( t ) - E _ { 2 } ^ { - } ( t ) = 2 P ( t ) \sin [ \Delta \omega t + \Delta \phi ] .\tag{2.13}
$$

The complex outputs from 90◦-hybrid and balanced PD is given as

$$
E _ { o } ( t ) = 2 P ( t ) \exp [ i ( \Delta \omega t + \Delta \phi ) ] .\tag{2.14}
$$

As a result, quadrature coherent detection with 90◦-hybrid is suitable for detecting any level of advanced modulation formats [35]. However, it also obviously shows that, this type of coherent detection requires accurate polarization alignment between received signal and LO.

## 2.2.4 Dual Polarization Coherent Detection

According to international telecommunication union (ITU) definition, channel spacing of 100 Gb/s optical communication systems is assigned to be 50 GHz. In order to fulfill such bandwidth requirements, dual polarization coherent detection with balanced PD will be under investigation in section 2.2.4. As it is explored by several researches [36–39], polarization diversity is under consideration as the third degree of modulation freedom. As it is discussed before, two of in-phase and quadrature modulation formats are capable for any level complex modulation. And dual polarization will further double the capacity of transmission systems [40]. For instance, 28 Gbaud electrical pseudo random binary sequence (PRBS) can drive 56 Gb/s optical QPSK signals using 30 GHz bandwidth Mach-Zehnder modulator (MZM). Using dual polarization modulation, entire system bit rate will be increased to 112 Gb/s. In stead of using scale number of 100 Gb/s for practical optical communication systems, 112 Gb/s systems is suitable for taking forward error correction (FEC) sequences into account [41].

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/1a5a40acc0b1355007adfdd7cf1a4e090e09d9b8dd37d03ee2079172453c4ec3.jpg)  
Figure 2.5: Dual polarization coherent detection with balanced PD.

As it is shown in Figure 2.5, two 90◦-hybrids with four balanced PD are implemented to respectively detect two branches of orthogonally polarized received signals, which are denoted as $\vec { \bf x }$ and ${ \vec { \mathbf { y } } } .$

Both of the received signal and LO are divided into two orthogonally polarized branches by using polarization beam splitter (PBS). Outputs from two $9 0 ^ { \circ }$ -hybrids can be presented as

$$
\left[ \begin{array} { l } { E _ { 1 } ^ { + } } \\ { E _ { 1 } ^ { - } } \\ { E _ { 2 } ^ { + } } \\ { E _ { 2 } ^ { - } } \end{array} \right] = \left[ \begin{array} { l } { \vec { \bf x } | E _ { S } + E _ { L O } | ^ { 2 } } \\ { \vec { \bf x } | E _ { S } - E _ { L O } | ^ { 2 } } \\ { \vec { \bf x } | E _ { S } + i E _ { L O } | ^ { 2 } } \\ { \vec { \bf x } | E _ { S } - i E _ { L O } | ^ { 2 } } \end{array} \right] ,\tag{2.15}
$$

$$
\left[ \begin{array} { l } { E _ { 3 } ^ { + } } \\ { E _ { 3 } ^ { - } } \\ { E _ { 4 } ^ { + } } \\ { E _ { 4 } ^ { - } } \end{array} \right] = \left[ \begin{array} { l } { \vec { \bf y } | E _ { S } + E _ { L O } | ^ { 2 } } \\ { \vec { \bf y } | E _ { S } - E _ { L O } | ^ { 2 } } \\ { \vec { \bf y } | E _ { S } + i E _ { L O } | ^ { 2 } } \\ { \vec { \bf y } | E _ { S } - i E _ { L O } | ^ { 2 } } \end{array} \right] ,\tag{2.16}
$$

In-phase and quadrature parts of polarization $\vec { \bf x }$ and polarization $\vec { \bf y }$ are denoted as $E _ { x I } ( t ) , E _ { x Q } ( t )$ and $E _ { y I } ( t ) , E _ { y Q } ( t )$ , which are given as

$$
\begin{array} { r } { \left[ \begin{array} { l } { E _ { x I } ( t ) } \\ { E _ { x Q } ( t ) } \end{array} \right] = \left[ \begin{array} { l } { 2 P _ { x } ( t ) \cos [ \Delta \omega t + \Delta \phi ] } \\ { 2 P _ { x } ( t ) \sin [ \Delta \omega t + \Delta \phi ] } \end{array} \right] , } \end{array}\tag{2.17}
$$

$$
\begin{array} { r } { \left[ \begin{array} { l } { E _ { y I } ( t ) } \\ { E _ { y Q } ( t ) } \end{array} \right] = \left[ \begin{array} { l } { 2 P _ { y } ( t ) \cos [ \Delta \omega t + \Delta \phi ] } \\ { 2 P _ { y } ( t ) \sin [ \Delta \omega t + \Delta \phi ] } \end{array} \right] . } \end{array}\tag{2.18}
$$

Using Equation 2.17 and Equation 2.18, the complex outputs from balanced PD are presented as

$$
\left[ \begin{array} { l } { E _ { x } ( t ) } \\ { E _ { y } ( t ) } \end{array} \right] = \left[ \begin{array} { l } { 2 P _ { x } ( t ) \exp [ i ( \Delta \omega t + \Delta \phi ) ] } \\ { 2 P _ { y } ( t ) \exp [ i ( \Delta \omega t + \Delta \phi ) ] } \end{array} \right] .\tag{2.19}
$$

## 2.2.5 Homodyne and Heterodyne Coherent Detection

In general, there are two different types of coherent detection techniques, depending on whether or not IF $\Delta \omega$ equals zero [42]. They are denoted as homodyne and heterodyne coherent detection.

## Homodyne coherent detection

In case of homodyne coherent detection, LO frequency is selected to be coincide with received signal carrier frequency. In other words, $\Delta \omega$ is equal to zero [43]. From Equation 2.19, output from balanced PD can be presented as

$$
E _ { I } ( t ) = 2 P ( t ) \cos ( \Delta \phi ) ,\tag{2.20}
$$

$$
E _ { Q } ( t ) = 2 P ( t ) \sin ( \Delta \phi ) .\tag{2.21}
$$

Furthermore using optical phase lock loop (OPLL) implementation, homodyne coherent detection could be applied to demodulation of arbitrary multi-level phase and amplitude modulation formats such as $n { \mathrm { - } } \mathrm { P S K }$ [44]. The main advantage of homodyne coherent detection is the sensitivity enhancement. However as it can be obviously noticed from Equation 2.20 and Equation 2.21, the main drawback of homodyne coherent detection is phase noise intolerance. Theoretically, $\Delta \phi$ should maintain stable. In practical, due to the time dependent variable fluctuation of LO phase $\phi _ { L O }$ and signal phase $\phi _ { S }$ $\Delta \phi$ will jitter randomly. Additional challenge is accurate frequency matching between LO and transmitted signal of homodyne coherent detection. These problems can be avoid by using heterodyne coherent detection.

## Heterodyne coherent detection

In case of heterodyne coherent detection, LO frequency is selected to be different from received signal carrier frequency. That means $\Delta \omega \neq 0$ [45]. From Equation 2.19, outputs from balanced PD can be presented as

$$
E _ { I } ( t ) = 2 P ( t ) \cos ( \Delta \omega t + \Delta \phi ) ,\tag{2.22}
$$

$$
E _ { Q } ( t ) = 2 P ( t ) \sin ( \Delta \omega t + \Delta \phi ) .\tag{2.23}
$$

Similar to homodyne coherent detection, heterodyne coherent detection could be applied to demodulation of multi-level phase and amplitude modulation formats. The mean disadvantage of heterodyne coherent detection is known as heterodyne-penalty [46]. That means heterodyne coherent detection has the inherent 3-dB SNR penalty compared with homodyne [46]. On the contrary, the advantage of heterodyne detection is the simplified requirements of receiver design. For instance, the frequency offset between LO and received signal could be compensated by using off-line digital signal processing algorithms without stringent requirements of accurate frequency matching between LO and transmitted signal [47]. This feature makes heterodyne detection suitable for practical implementation of optical communication systems.

## 2.3 Transmission impairments in optical 100 Gb/s links

The common optical fiber transmission systems are mostly based on standard single mode fiber (SSMF). Structure of SSMF is shown as Figure 2.6. The outside layer is known as cladding. The transmitted light propagates meanly through the core layer. In order to achieve the reflection condition, the reflection index of the core layer is higher than cladding.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/ad555414a6a1794f502f56f705629c409ffb56f8b1c3c46ef27cfa714bc80764.jpg)  
Figure 2.6: Structure of the standard single mode fiber (SSMF).

Moreover the theoretical mode of optical propagation could be obtained by nonlinear Schr¨odinger equation [48], which is given as

$$
\frac { \partial A } { \partial z } + \beta _ { 1 } \frac { \partial A } { \partial t } + \frac { i \beta _ { 2 } } { 2 } \frac { \partial ^ { 2 } A } { \partial t ^ { 2 } } - \frac { \beta _ { 3 } } { 6 } \frac { \partial ^ { 3 } A } { \partial t ^ { 3 } } + \frac { \alpha ( z ) } { 2 } A = i \gamma | A | ^ { 2 } A ,\tag{2.24}
$$

where $A = A ( z , t )$ is the optical field. $\alpha ( z )$ is the fiber attenuation parameter and $\gamma$ is the Kerr nonlinear coefficient. $\beta _ { n }$ is the n-order frequency dependent chromatic dispersion parameters. These coefficients are represented different impairments of fiber transmission links. Furthermore the expression of $\beta ( \omega )$ in a Taylor series around the carrier frequency $\omega _ { 0 }$ is given as

$$
\beta ( \omega ) = \beta _ { 0 } + ( \omega - \omega _ { 0 } ) \beta _ { 1 } + \frac { 1 } { 2 } ( \omega - \omega _ { 0 } ) ^ { 2 } \beta _ { 2 } + \frac { 1 } { 6 } ( \omega - \omega _ { 0 } ) ^ { 3 } \beta _ { 3 } + \cdots ,\tag{2.25}
$$

where $\beta _ { 0 } \equiv \beta _ { \omega _ { 0 } }$ , and $\beta _ { n }$ is

$$
\beta _ { n } = ( \frac { d ^ { n } \beta } { d \omega ^ { n } } ) _ { \omega = \omega _ { 0 } }\tag{2.26}
$$

## 2.3.1 Fiber Losses

The parameter of fiber loss is presented in Equation 2.24 as $\alpha ( z )$ which is the attenuation in power of optical signal propagation through fiber. It can be presented as

$$
\alpha ( z ) = - \frac { 1 0 } { z } \log _ { 1 0 } ( \frac { P _ { o u t } } { P _ { i n } } ) ,\tag{2.27}
$$

where z is the length of fiber transmission distance, $P _ { o u t }$ and $P _ { i n }$ are output and input powers of fiber transmission span respectively. Fiber loss is meanly caused by material absorption and Rayleigh scattering. As it can be noticed from Figure 2.7, α(z) is a function of signal carrier wavelength.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/6940363bfeb646a354779b9ef46ee4ed5e3497406a247a3af489c9639d2473bf.jpg)  
Figure 2.7: Attenuation value for SSMF over optical channels.

For single mode fiber transmission, wavelength range of optical communication channels are divided into six bands, which are shown in Table 2.1. As it can be noticed, C band and L band have the minimum fiber loss (α = 0.2 dB/km) [49]. Such two bands are suitable for long-haul transmission [50].

<table><tr><td>Band</td><td>Wavelength (nm)</td></tr><tr><td>O band</td><td>1260 nm - 1360 nm</td></tr><tr><td>E band</td><td>1360 nm - 1460 nm</td></tr><tr><td>S band</td><td>1460 nm - 1530 nm</td></tr><tr><td>C band</td><td>1530 nm - 1565 nm</td></tr><tr><td>L band</td><td>1565 nm - 1625 nm</td></tr><tr><td>U band</td><td>1625 nm - 1675 nm</td></tr></table>

Table 2.1: Wavelength range for different bands in optical communication.

## 2.3.2 Chromatic Dispersion

Chromatic dispersion in single mode fiber is induced by carrier wavelength dependent refractive index. As it is shown in Figure 2.8, chromatic dispersion will result for time domain pulse broadening. Moreover pulse broadening will refer to inter symbol interference (ISI) in time domain. As it is described in Equation 2.25, the second order term $\beta _ { 2 }$ corresponds to dispersion coefficient D, which is also known as group velocity dispersion (GVD). In general, due to GVD effect, different pulses carried certain frequency components will propagate through SMF with different velocity or such GVD effect is known as chromatic dispersion.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/5dfad72c684e6b17ed90ac5eb4d5189f073b15d9e9d7ee9954c5c39df75043c2.jpg)  
Figure 2.8: Pulse broadening effect due to chromatic dispersion.

Material dispersion and waveguide dispersion are two mean factors for chromatic dispersion. Material dispersion refers to wavelength dependency of reflection index which can be controlled by changing fiber materials or dopant. Waveguide dispersion can be understood with Maxwell equation for cylindrical waveguide. Chromatic dispersion composed by material dispersion and waveguide dispersion are shown in Figure 2.9. In fiber transmission system, it is common to define the dispersion parameter D and the dispersion slope S which are the change of GVD and GVD slope with respect to the carrier wavelength. As it is shown in Equation 2.28 and Equation 2.29, D and S are given as

$$
D = \frac { \partial \beta _ { 1 } } { \partial \lambda } = - \frac { 2 \pi c } { \lambda ^ { 2 } } \beta _ { 2 }\tag{2.28}
$$

$$
S = { \frac { \partial D } { \partial \lambda } } = { \frac { 4 \pi c } { \lambda ^ { 3 } } } ( \beta _ { 2 } + { \frac { \pi c } { \lambda } } \beta _ { 3 } )\tag{2.29}
$$

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/39629d67b17ae754007863f1adb8f395524780731866601a66b71fa2e2085523.jpg)  
Figure 2.9: Chromatic dispersion parameter of SSMF [51].

Table 2.2 shows some commercial available single mode fibers.
<table><tr><td>Fiber type Trade name</td><td> $A _ { e f f }$   $\mu m ^ { 2 }$ </td><td> $\lambda _ { Z D }$  nm</td><td>D (C band) /(km nm)</td><td>Slope S  $p s / ( k m \cdot n m ^ { 2 } )$ </td></tr><tr><td>Corning SMF-28</td><td>80</td><td>1302-1322</td><td>16 - 19</td><td>0.090</td></tr><tr><td>Lucent AllWave</td><td>80</td><td>1300-1322</td><td>17 -20</td><td>0.088</td></tr><tr><td>Alcatel ColorLock</td><td>80</td><td>1300-1320</td><td>16 - 19</td><td>0.090</td></tr><tr><td>Corning Vascade</td><td>101</td><td>1300-1310</td><td>18 - 20</td><td>0.060</td></tr><tr><td>True Wave-RS</td><td>50</td><td>1470-1490</td><td>2.6 - 6</td><td>0.050</td></tr><tr><td>Corning LEAF</td><td>72</td><td>1490-1500</td><td>2 - 6</td><td>0.060</td></tr></table>

Table 2.2: Coefficients of commercial available SMF.

## 2.3.3 Polarization Mode Dispersion

Polarization of light is a property of electromagnetic waves that describes the orientation of the transverse electric field. In SMF, there exists two orthogonal polarization states, which are denoted as $\vec { \bf x }$ and $\vec { \bf y }$ [52]. Polarization of light can be described by representation of Stokes parameters, which can be straightforwardly expressed by using Poincar´e sphere. The software interface of Agilent 8509 polarization analyzer is shown in Figure 2.10. The Poincar´e sphere consists of four parameters in terms of optical power. As it is shown in Figure 2.11, Stokes parameters are denoted as $[ S _ { 0 } , S _ { 1 } , S _ { 2 } , S _ { 3 } ]$

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/e41f83ffd6030647f0218b10bb4f6d0ff26eeb9d78eb85ad08c6751a57ff6bdc.jpg)

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/f9dd146c97c8fea7a09b97465c28a195ba1e3e5cdca7045aa9bd7c7d8aa814fb.jpg)  
Figure 2.10: Agilent 8509 polarization analyzer interface.  
Figure 2.11: Poincar´e sphere.

$$
\left[ \begin{array} { c } { S _ { 0 } } \\ { S _ { 1 } } \\ { S _ { 2 } } \\ { S _ { 3 } } \end{array} \right] = \left[ \begin{array} { c } { E _ { x } ^ { 2 } + E _ { y } ^ { 2 } } \\ { E _ { x } ^ { 2 } - E _ { y } ^ { 2 } } \\ { 2 E _ { x } E _ { y } \cos ( | \phi _ { x } - \phi _ { y } | ) } \\ { 2 E _ { x } E _ { y } \sin ( | \phi _ { x } - \phi _ { y } | ) } \end{array} \right] ,\tag{2.30}
$$

where $E _ { x }$ and $E _ { y }$ are represented optical field of two polarization $\vec { \bf x }$ and ${ \vec { \mathbf { y } } } .$ $\phi _ { x }$ and $\phi _ { y }$ are the phase of optical field in $\vec { \bf x }$ and $\vec { \bf y }$ derection. Moreover the degree of polarization (DOP) is defined as

$$
 D O P = \frac { \sqrt { S _ { 1 } ^ { 2 } + S _ { 2 } ^ { 2 } + S _ { 3 } ^ { 2 } } } { S _ { 0 } }\tag{2.31}
$$

In the ideal case, two polarizations propagating through SMF will have the same group velocity. However, in the practical transmission systems, due to the fiber material can not be isotropic, two orthogonal polarized optical fields propagating through SMF will have different group velocity. Such effect is known as differential group delay (DGD), which is shown in Figure 2.12.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/8c20af5498473866c4f2085acca232242c2322b1cc49e4f9e1df087b57a11d3e.jpg)  
Figure 2.12: DGD effect of SSMF.

Moreover the difference in the group velocities can be defined as $\triangle \beta _ { 1 }$ which is given as

$$
\triangle \beta _ { 1 } = | \beta _ { 1 , x } - \beta _ { 1 , y } | = \frac { \omega } { c } | n _ { x } - n _ { y } | ,\tag{2.32}
$$

where $n _ { x }$ and $n _ { y }$ are the effective refractive indices for two orthogonal polarizations. The DGD effect results for polarization mode dispersion (PMD), which is defined as mean of the DGD,

$$
\left. \Delta \beta _ { 1 } \right. = P M D \cdot \sqrt { L } ,\tag{2.33}
$$

where L is the propagation length of fiber transmission, and  denotes the statistic average. Nowadays lower PMD coefficient type of SMF has developed, such as Corning LEAF SMF and TrueWave RS SMF.

## 2.3.4 Nonlinear Transmission Impairments

According to Table 2.2, the typical value of effective area $A _ { e f f }$ in SMF is around 50 to $1 0 0 \mu m ^ { 2 }$ . Such small core area results in stronger nonlinearity effect in SMF. From Schr¨odinger equation 2.24 nonlinear coefficient $\gamma$ is given as

$$
\gamma = \frac { n _ { 2 } \omega _ { 0 } } { c A _ { e f f } } ,\tag{2.34}
$$

where $n _ { 2 }$ is the nonlinear refractive index parameter and $\omega _ { 0 }$ is the carrier frequency. There three types of nonlinearities are considered in this thesis, which are known as self phase modulation (SPM), cross phase modulation (XPM), and four wave mixing (FWM).

## Self Phase Modulation

Nonlinearity effect of SPM refer to refractive index changing caused by light propagation. And the SPM induced nonlinear phase shift is given as

$$
\phi _ { S P M } = \gamma P _ { \mathrm { i n } } L _ { \mathrm { e f f } } ,\tag{2.35}
$$

where $L _ { \mathrm { e f f } } = ( 1 - \exp ( - \alpha L ) ) / \alpha$ is the effective interaction length which takes the fiber loss α into account. And L is the length of the fiber propagation. Equation 2.35 shows the light pulse with different intensity have different SPM-induced chirp.

In case of intensity modulated signals, the SPM can be ignored because no signal information is modulated by phase. However sever SPM-induced chirp will cause the pulse broadening, which will degrade the system performance.

In case of phase modulated signals, SPM has to be considered because phase is used to carry the signal information. The post-compensation method can be used to reduce SPM by appropriately choosing the residual chromatic dispersion at receiver [53].

## Cross Phase Modulation

In wavelength division multiplexing (WDM) systems, the nonlinear phase shift depends not only on the optical power in a single channel but also on the optical power in all channels. The contribution to the nonlinear phase shift of channel $j$ from the other channels is called cross phase modulation (XPM), and is given as

$$
\phi _ { j , X P M } = 2 \gamma L _ { \mathrm { e f f } } \sum _ { m \neq j } P _ { m } ,\tag{2.36}
$$

As it can be understood from Equation 2.36, power of the adjacent channels lead to phase changing of channel $j$ . In general, XPM effect increase with decreasing the wavelength spacing between the interacting WDM channels. In the subsequent chapter, digital signal processing algorithm compensating for inter channel interference will be discussed.

## 2.3.5 Four Wave Mixing

Four wave mixing (FWM) is a nonlinear effect between four different optical waves. According to the theory, if three sub-waves with frequencies $\omega _ { 1 }$ $\omega _ { 2 }$ and $\omega _ { 3 }$ own the same phase, and mix together, a forth sub-wave with frequency $\omega _ { 4 }$ will be created, where $\omega _ { 4 } = \omega _ { 1 } + \omega _ { 2 } + \omega _ { 3 }$ or $\omega _ { 4 } = \omega _ { 1 } + \omega _ { 2 } - \omega _ { 3 }$

Phase matching of efficient FWM is required. In the case of $\omega _ { 4 } =$ $\omega _ { 1 } + \omega _ { 2 } - \omega _ { 3 }$ , the phase matching requirement is given as

$$
\frac { 1 } { c } ( n _ { 3 } \omega _ { 3 } + n _ { 4 } \omega _ { 4 } - n _ { 1 } \omega _ { 1 } - n _ { 2 } \omega _ { 2 } ) = 0 ,\tag{2.37}
$$

where $n _ { i }$ is the refractive index at $\omega _ { i }$

Due to dispersion, it is generally easier to fulfill the phase matching condition in the degenerate case. In WDM systems employing a uniform channel spacing, four wave mixing can also lead to inter channel interference (ICI).

## 2.4 Summary

In chapter 2, basic concepts and theoretical analysis of coherent detection are presented. In general, the main advantages of coherent detection include:

Firstly, coherent detection is able to detect advanced modulation formats with improved spectral efficiency, such as quadrature phase-shift keying (QPSK).

• Secondly, compared to IM/DD, coherent detection provides potential for superior receiver sensitivity.

Moreover, optical coherent detection can benefit from intensive researches concerning digital signal processing algorithms to compensate for fiber transmission impairments.

Furthermore, fundamental analysis concerning fiber transmission linear impairments including fiber loss, chromatic dispersion and polarization mode dispersion are presented. Nonlinear impairments resulted from Kerr effect including SPM, XPM and FWM are also introduced. Due to the presence of these different propagation impairments in the fiber transmission, feasible DSP compensation algorithms are required. Various DSP algorithms will be depicted in the chapter 3.

Chapter 3

# Coherent Detection with DSP Algorithms

## 3.1 Introduction

In chapter 3, various digital signal processing (DSP) algorithms will be presented. The mean advantages of utilizing coherent detection with DSP algorithms can be summarized as follows. Firstly, coherent detection with DSP algorithms is able to detect advanced modulation formats with improved spectral efficiency, such as n phase-shift keying (PSK). Secondly, coherent detection with DSP algorithms provides potential for superior receiver sensitivity. Furthermore, coherent detection with DSP algorithms enables electrical off-line compensation for impairments arising due to fiber transmission [54]. Coherent detection with DSP algorithms can take advantage from continuously increasing electrical processing speed. Moreover optical coherent detection can benefit from intensive researches concerning digital signal processing algorithms. Consequently, it is efficient and simple to implement optical signal processing in digital domain. The common configuration of optical coherent receiver associated with DSP algorithms is shown in Figure 3.1. In this block diagram, several DSP algorithms are under consideration. CD compensation block is used to compensate for chromatic dispersion. Clock recovery block is implemented to correct digital sampling error which is made by analog to digital converters (ADC). Polarization demultiplexing is realized by using polarization demultiplex algorithm. Phase and frequency offset recovery block is employed to correct phase and frequency difference between received signal and LO. These different DSP algorithms will be discussed in details in subsequent sections.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/96101770b2f66f9c7033c411ea5b2f15f49e7c64267e3649ed5c5d5f62bf8ad0.jpg)  
Figure 3.1: Configuration of coherent detection with DSP.

## 3.2 Chromatic Dispersion Compensation DSP Algorithm

In this subsection, the combination of coherent detection with DSP algorithm is proposed to compensate for chromatic dispersion (CD) in dual polarization (DP) QPSK systems. The configuration diagram of optical DP-QPSK system with coherent digital receiver is shown in Figure 3.2.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/be00a7f600cfd47b14f63944b56fbbc1269f6af2e35dbbf482746c6cf99f54b5.jpg)  
Figure 3.2: Coherent DP-QPSK system configuration. (a) DP-QPSK transmitter. (b) coherent receiver optical front end. (c) off-line DSP algorithms blocks. (d) polarization demultiplexing butterfly structure.

The digital receivers for coherent DP-QPSK system comprise stages of digital signal processing algorithms to compensate for chromatic dispersion among other optical signal fibre transmission impairments. Those algorithms commonly require performing operations such as fast fourier transform (FFT) over a given block length of data samples. The chosen length of such block determines both the complexity of implementing those operations and the accuracy they can achieve in compensating for signal impairments. A conventional DSP algorithm for serial, frequency domain, CD compensation requires that the FFT optation is applied to entire data sample set [55]. As the length of the samples increases, FFT operation requires more computation capacity. The complexity of implementing real time system depends on the number of complex multiplication [56]. In the case of radix-2 FFT, the number of complex multiplication required may be expressed by ${ \scriptstyle { \frac { 1 } { 2 } } l o g _ { 2 } ( L ) }$ , where L is the length of FFT. In this thesis, an alternative DSP algorithm for CD compensation will be presented. It is known as block-overlap CD compensation algorithm [57].

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/d4cd6dbd511a0c6ccd0dcbb99fd7501d747578f96574e5169ac4bcb3249af0cc.jpg)  
Figure 3.3: Block-overlap CD compensation algorithm half-overlap.

The block-overlap CD compensation algorithm applies frequency domain equalization (FED) to blocks of samples instead of the entire data sample set. This block-overlap approach for CD compensation was first proposed by Riichi Kudo et al., [58]. The output signal of the ADC stage are data samples, that are divided into blocks (Figure 3.3.a) with fixed length N $( N < L )$ . For illustration purposes (Figure 3.3), case of the overlapped part length equal to half of the block length is under consideration. In this half-overlap case, half of the block is composed of the current samples (Figure 3.3.b), and the rest is composed of equally length, N, data samples from the left and right neighboring blocks. Although the FFT processing complexity is reduced to that of a single block, instead of the entire data sample set, inter-block-interference (IBI) may affect the system performance. To combat IBI, the result of the FFT due to the overlapped samples (Figure 3.3.b and Figure 3.3.c) are discarded. $N _ { 1 }$ denotes the length of the discarded FFT output samples.

Although a large discard length can reduce significantly IBI, it comes again at the expenses of complexity. However, it is possible to implement a block overlap algorithm with specific engineering rules for the block and discard length that can reduce IBI and achieve a targeted compensation level for a given CD value. In this paper, to compensate for CD, a frequency domain equalization (FED) algorithm is implemented (Figure 3.3.d), based on a frequency all-pass filter. The frequency response for an all-pass filter to compensate fibre CD can be expressed as,

$$
G ( z , \omega ) = \exp [ - j D \frac { \lambda ^ { 2 } } { 2 \pi c } \frac { \omega ^ { 2 } } { 2 } z + j S ( \frac { \lambda ^ { 2 } } { 2 \pi c } ) ^ { 2 } \cdot \frac { \omega ^ { 3 } } { 6 } z ] ,\tag{3.1}
$$

where D is the dispersion coefficient, $S$ is the dispersion slop, $\omega$ is the angular frequency, λ is the light wavelength, c is the light velocity, and $z$ is the fibre length. After CD compensation at frequency domain, IFFT inverts the sequence back to the time domain (Figure 3.3.e).

In order to validate the engineering rules for block-overlap CD compensation algorithm, case of half-overlap is under investigation. As it can be noticed, the number of blocks is equal to $2 \times [ L / N ] - 1$ , where square bracket is the ceil integer function. A single block FFT only needs ${ \scriptstyle { \frac { 1 } { 2 } } } l o g _ { 2 } ( N )$ complex multiplications compared to ${ \scriptstyle { \frac { 1 } { 2 } } l o g _ { 2 } ( L ) }$ required for serial compensation $( N < < L )$

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/1f4fbdfb56507841d91fe315148bd248cbb06bbf1ee59b39b9387feb7cd68c92.jpg)  
(a)

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/d1714b39fdbd91f59003c9fc8495223c259ea41a222241423e0e57cd76b07ad0.jpg)  
(b)  
Figure 3.4: Block-overlap CD BER performance: (a) BER vs OSNR with 16000 ps/nm CD; (b) block length requirements in block-overlap CD at 14 dB OSNR.

To avoid IBI, the value of the discarded data length $N _ { 1 }$ is chosen as the following engineering rule as,

$$
N _ { 1 } = D z { \frac { \Gamma \lambda ^ { 2 } } { c } } R _ { s }\tag{3.2}
$$

Where Γ is the full-wave-half-maximum of the signal, and $R _ { s }$ is sample rate. In the simulation, $R _ { s }$ is set to $5 6 ~ \mathrm { G S a / s } .$ The operating wavelength is 1550 nm. The dispersion slop parameter $S$ is set as 0. Nyquist criterions specify Γ to be 56 GHz. If CD is 16000 ps/nm, then $N _ { 1 } = 4 4 8 .$ In order to fulfil the radix-2 FFT requirement, $N _ { 1 }$ is set to $2 ^ { 9 }$ (512), which means in the case of half-overlap, the block length is $2 ^ { 1 1 }$ (2048), and that $2 ^ { 1 0 }$ (1024) samples are discarded (Figure 3.4(a)). From Figure 3.4, the simulation results show that, a given value of chromatic dispersion requires specific block length to approach the back to back transmission bit error rate performance. In order to avoid IBI, engineering rule block-overlap CD compensation algorithm ${ \frac { \alpha } { \beta } } \mathrm { - o v e r l a p }$ scheme, $\textstyle { \frac { \alpha } { \beta } } \in [ { \frac { 1 } { 2 } } , 1 )$ $\textstyle { \frac { \alpha } { \beta } }$ is the ratio of discarded samples length to block length, where α and $\beta$ are coprime integer. In the case of half-overlap, $\textstyle { \frac { \alpha } { \beta } }$ is equal to ${ \frac { 1 } { 2 } } .$ According to the engineering rule, the number of complex multiplication for one block is $\textstyle { \frac { 1 } { 2 } } l o g _ { 2 } { \bigl ( } { \frac { 2 \beta } { \alpha } } N _ { 1 } { \bigr ) }$ The number of complex multiplication for the entire data sample set is $\scriptstyle { \frac { 1 } { 2 } } l o g _ { 2 } \{ \beta ( L - 2 N _ { 1 } ) \}$ Therefore, the complexities of entire data sample set and one block achieve the minimum value when $\textstyle { \frac { \alpha } { \beta } }$ is equal to $\scriptstyle { \frac { 1 } { 2 } }$

$$
\left\{ \begin{array} { l l } { { \frac { 1 } { 2 } } l o g _ { 2 } ( { \frac { 2 \beta } { \alpha } } N _ { 1 } ) } & { { \mathrm { o n e ~ b l o c k } } } \\ { { \frac { 1 } { 2 } } l o g _ { 2 } \{ \beta ( L - 2 N _ { 1 } ) \} } & { { \mathrm { e n t i r e ~ d a t a ~ s a m p l e ~ s e t } } } \end{array} \right.\tag{3.3}
$$

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/2c5f4fc7f5dcb7b5ff686ed34ed1595b566f9df946e34050b63b72c565b93bf0.jpg)

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/309488de2ea7d8d9d4afbf73cfa284a67ef329c8b25c69db0fc14e4f16877599.jpg)  
Figure 3.5: Constellation comparison between received signal and CD compensation.

As it is shown in Figure 3.5, engineering rules for block-overlap CD compensation algorithm has been experimentally validated with 20 Gbit/s QPSK links with 40 km SMF transmission operating at 1550 nm. Figure 3.5 shows the results for the constellation of received signal and with block-overlap CD compensation being implemented. The block-overlap CD compensation algorithm reduces the computational complexity of a serial frequency all-pass filter approach substantially, to that of a single block. Engineering rule indicates that for a given target value of CD compensation, the block length of block-overlap CD algorithm can be adjusted to achieve less computational complexity than the serial compensation approach.

## 3.3 Clock Recovery DSP Algorithm

In the optical coherent transmission systems, specific sampling frequency for analogue to digital converter (ADC) is required to process specific symbol rate of received signal. Usually two samples per symbol are necessary for off-line DSP. However in the practical systems, optimum sampling clock of ADC is always unknown. In general, any sampling clock errors significantly reduce system bit error rate (BER) performance. Therefore clock recovery DSP algorithm is demanded to determine the suitable sampling clock.

The clock recovery DSP algorithm implemented in this thesis is known as Gardner algorithm [59], which is widely used in the field of wireless communication systems. Structure of Gardner clock recovery is shown as Figure 3.6.

As it is illustrated by Figure 3.6, the numerically controlled oscillator (NCO) is drived by outputs from Gardner time error detector $e _ { x } ( n )$ and $e _ { y } ( n )$ , which are defined in Equation 3.4 and Equation 3.5,

$$
e _ { x } ( n ) = X _ { I } ( n ) [ X _ { I } ( n + 1 ) - X _ { I } ( n - 1 ) ] + X _ { Q } ( n ) [ X _ { Q } ( n + 1 ) - X _ { Q } ( n - 1 ) ] ,\tag{3.4}
$$

$$
e _ { y } ( n ) = Y _ { I } ( n ) [ Y _ { I } ( n + 1 ) - Y _ { I } ( n - 1 ) ] + Y _ { Q } ( n ) [ Y _ { Q } ( n + 1 ) - Y _ { Q } ( n - 1 ) ] ,\tag{3.5}
$$

where n-th element of time error represents difference between two adjacent samples from ADC. Sample period is equal to $\scriptstyle { \frac { T _ { s } } { 2 } }$ , where $T _ { s }$ is symbol period of transmitted signal. Furthermore, as it is can be noticed from Figure 3.6, the implementation of interpolator is used to interpolate adjacent symbols with new sampling clock. The mean purpose of Gardner clock recovery algorithm is to sample the adjacent sequences with the same time difference that $e _ { x } ( n )$ and $e _ { y } ( n )$ are equal to zero.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/087948b0c3385df0641f6cf8328dd93a9fab38d20f537418a2410b7471ee7666.jpg)  
Figure 3.6: Structure of Gardner clock recovery DSP algorithm.

## 3.4 Polarization Demultiplexing DSP Algorithm

As it has been discussed before, optical coherent receiver using polarization diversity detection structure can detect the complex signal of each polarization and emulate the state of polarization of received signal with off-line digital signal processing. At optical front end of coherent receiver, incoming signal with arbitrary state of polarization is separated into two linear polarization components, which are denoted as $E _ { x }$ and $E _ { y }$ As it is shown in Figure 3.7, finite impulse response (FIR) filter combined with butterfly algorithm is implemented for polarization demultiplexing. In order to emulate the cross-talk between the signals carried on two polarizations, Jones matrix is employed, which is given as

$$
\left[ \begin{array} { c c } { { \sqrt { \alpha } e ^ { i \delta } } } & { { - \sqrt { 1 - \alpha } } } \\ { { \sqrt { 1 - \alpha } } } & { { \sqrt { \alpha } e ^ { - i \delta } } } \end{array} \right] ,\tag{3.6}
$$

where α and δ denote the power splitting ratio and phase difference between two polarizations. Therefore the polarization multiplexed signal at the receiver side after fiber propagation can be presented as

$$
\left[ \begin{array} { c c } { E _ { x } } \\ { E _ { y } } \end{array} \right] = \left[ \begin{array} { c c } { \sqrt { \alpha } e ^ { i \delta } } & { - \sqrt { 1 - \alpha } } \\ { \sqrt { 1 - \alpha } } & { \sqrt { \alpha } e ^ { - i \delta } } \end{array} \right] \left[ \begin{array} { c c } { E _ { i n , x } } \\ { E _ { i n , y } } \end{array} \right] .\tag{3.7}
$$

As it shown in Equation 3.7, applying the inverse matrix of Equation 3.6 can make the incoming signal at the coherent receiver side become original transmitted signal. On the other hand the problem is the same as determining the value of α and δ. The inverse Jones matrix is given as

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/c53801c5a8a02355851ba223a4ce2b05e595c1d7a5121a8eee3b94b646316776.jpg)  
Figure 3.7: Polarization demultiplexing DSP algorithm.

$$
T ^ { - 1 } = \left[ \begin{array} { c c } { { r } } & { { k } } \\ { { - k ^ { * } } } & { { r ^ { * } } } \end{array} \right] ,\tag{3.8}
$$

where both of r and k are complex paraments. And symbol of ∗ represents conjugation of complex components. Using Equation 3.7 and Equation 3.8, received signal combined with inverse Jones matrix can be presented as

$$
T ^ { - 1 } \cdot \left[ \begin{array} { c c } { E _ { x } } \\ { E _ { y } } \end{array} \right] = \left[ \begin{array} { c c } { r \sqrt { \alpha } e ^ { i \delta } + k \sqrt { 1 - \alpha } } & { - r \sqrt { 1 - \alpha } + k \sqrt { \alpha } e ^ { - i \delta } } \\ { - k ^ { * } \sqrt { \alpha } e ^ { i \delta } + r ^ { * } \sqrt { 1 - \alpha } } & { k ^ { * } \sqrt { 1 - \alpha } + r \sqrt { \alpha } e ^ { - i \delta } } \end{array} \right] \left[ \begin{array} { c c } { E _ { i n , x } } \\ { E _ { i n , y } } \end{array} \right] .\tag{3.9}
$$

For simplicity, Equation 3.9 can be denoted as

$$
\left[ \begin{array} { l } { E _ { x } ^ { ' } } \\ { E _ { y } ^ { ' } } \end{array} \right] = \left[ \begin{array} { l l } { h _ { x x } } & { h _ { x y } } \\ { h _ { y x } } & { h _ { y y } } \end{array} \right] \left[ \begin{array} { l } { E _ { i n , x } } \\ { E _ { i n , y } } \end{array} \right] .\tag{3.10}
$$

As it can be noticed from Equation 3.9, h-factors are defined as polarization demultiplexing parameters, where $h _ { x y } = - h _ { y x } ^ { * }$ and $h _ { y y } = h _ { x x } ^ { * }$ Moreover, assuming the modulation format is n-PSK, normalized amplitude of each

input polarization components can be expressed as

$$
| E _ { x } ^ { ' } | ^ { 2 } = | E _ { y } ^ { ' } | ^ { 2 } = 1\tag{3.11}
$$

According to Equation 3.11, digital FIR filter combined with constant modulus algorithm (CMA) [60] can be employed to adaptively control the polarization demultiplexing parameters in Equation 3.10. Using least mean square (LMS) algorithm, polarization demultiplexing parameters can be presented as

$$
\begin{array} { r l } & { h _ { x x } ( n + 1 ) = h _ { x x } ( n ) + \mu ( 1 - | E _ { x } ^ { ' } ( n ) | ^ { 2 } ) E _ { x } ( n ) E _ { x } ^ { * } ( n ) } \\ & { h _ { x y } ( n + 1 ) = h _ { x y } ( n ) + \mu ( 1 - | E _ { x } ^ { ' } ( n ) | ^ { 2 } ) E _ { x } ( n ) E _ { y } ^ { * } ( n ) } \end{array}\tag{3.12}
$$

where $\mu$ is a step size parameter and n is the number of symbol. Furthermore the adaptive update in FIR filter is given as

$$
h _ { x x } ( n ) = \sum _ { m = - { \frac { M } { 2 } } } ^ { \frac { M } { 2 } } h _ { x x } ( n - m ) \quad a n d \quad h _ { x y } ( n ) = \sum _ { m = - { \frac { M } { 2 } } } ^ { \frac { M } { 2 } } h _ { x y } ( n - m ) .\tag{3.13}
$$

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/5144f52f0edaf6660faf5de670069e27fe3dcf406dc47b958ce43f2659d37e25.jpg)  
Figure 3.8: polarization demultiplexing parameters convergence.

As it is shown in Figure 3.8, step-size $\mu$ is selected to control the convergence speed of polarization demultiplexing parameters. According to

LMS algorithm, after symbol by symbol update, difference between 1 and $| E _ { x } ^ { ' } ( n ) | ^ { 2 }$ converge to zero, which means emulation of polarization demultiplexing parameters are equal to the parameters of inverse Jones matrix. As a result, X-polarization components of received signal are sorted in x-port. Y-polarization components of received signal are sorted in y-port.

## 3.5 Carrier Recovery DSP Algorithm

As it is depicted in Figure 3.1, DSP algorithms for carrier recovery including phase and frequency offset compensation is required after polarization demultiplexing. Both of phase and frequency offset are introduced by mismatching of signal carrier and LO. Conventional carrier recovery is implemented by using optical phase lock loop (OPLL). Instead of using costly compensation method, off-line DSP algorithms are recommended in section 3.5, which consist of Viterbi-Viterbi recovery algorithm and pilot-tone aided phase noise cancellation algorithm.

## 3.5.1 Viterbi-Viterbi Carrier Recovery Algorithm

The feed forward Viterbi-Viterbi algorithm is considered as a common solution for phase offset recovery [61], because of the simple and efficient processing procedure. The structure of feed forward Viterbi-Viterbi carrier recovery algorithm is shown in Figure 3.9. In order to explore the principle of Viterbi-Viterbi algorithm, modulation format of QPSK is under consideration. According to n-fold rotational symmetry of n-PSK constellation, the received digital QPSK signal can be presented as

$$
E _ { S } ( k ) = A _ { S } ( k ) \exp [ i ( \frac { 2 \pi m } { 4 } + \theta _ { x } ( k ) ) ] + n _ { k } , \quad ( m = 0 , 1 , 2 , 3 )\tag{3.14}
$$

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/2b14bee4c716e11f53aa403a6272b59ae9f8eecdac38198fdd26dc0a1a723bdf.jpg)  
Figure 3.9: Viterbi-Viterbi phase recovery algorithm.

In Equation 3.14, $A _ { S } ( k )$ is the QPSK signal amplitude. $\theta _ { x } ( k )$ represents the phase offset between received signal and LO. And $n _ { k }$ is the additive white Gaussian noise (AWGN). $N _ { 1 }$ and $N _ { 2 }$ are chosen according to processing method. In case of serial processing, Viterbi-Viterbi carrier recovery algorithm is applied to the received signal symbol by symbol. Moreover phase offset $\theta _ { x } ( k )$ can be modeled as a Wiener variable with zero mean and variance $\sigma ^ { 2 } = 2 \pi \Delta \nu T$ , where $\Delta \nu$ is the combination of transmission and LO laser linewidth [62]. As it is shown in Figure 3.9, phase modulation of received QPSK signal is removed by using n-power rules. According to QPSK modulation, n-power rule is reformulated to power-4 process which can be represented as

$$
E _ { S } ^ { 4 } ( k ) = S _ { k } + N _ { k } ,\tag{3.15}
$$

$$
\left\{ \begin{array} { l } { { S _ { k } = A _ { S } ^ { 4 } ( k ) \exp [ i ( 2 \pi m + 4 \theta _ { x } ( k ) ) ] } } \\ { { N _ { k } = n _ { k } ^ { 4 } + 4 S _ { k } n _ { k } ^ { 3 } + 6 S _ { k } ^ { 2 } n _ { k } ^ { 2 } + 4 S _ { k } ^ { 3 } n _ { k } } } \end{array} \right.\tag{3.16}
$$

As it can be noticed from Equation 3.16, $S _ { k }$ consists of the phase offset $\theta _ { x } ( k )$ , and $N _ { k }$ is the cross term between signal and noise. Since $\exp ( i 2 \pi m ) = 1$ , data dependency is removed. After time domain averaging, phase tracking and phase unwrapping, phase offset estimation can be presented as

$$
\theta _ { x } ^ { ' } ( k ) = \frac { 1 } { 4 } \arg \{ \sum _ { k = N _ { 1 } } ^ { N _ { 2 } } E _ { S } ^ { 4 } ( k ) \}\tag{3.17}
$$

Viterbi-Viterbi carrier recovery requires phase unwrapping because function of $\textstyle { \frac { 1 } { 4 } } \arg ( \cdot )$ returns the results only between $- { \frac { \pi } { 4 } }$ and $\scriptstyle { \frac { \pi } { 4 } }$ . The phase unwrapping function allows the phase offset estimation from −∞ to +∞ [63]. Furthermore the results after Viterbi-Viterbi carrier recovery can be given as

$$
E _ { S } ^ { ' } ( k ) = E _ { S } ^ { ' } ( k - D ) \cdot \exp [ - i \theta _ { x } ^ { ' } ( k ) ]\tag{3.18}
$$

where D presents number of sequence delay in received signals. As a result, if $\theta _ { x } ( k ) = \theta _ { x } ^ { ' } ( k )$ , Viterbi-Viterbi carrier recovery algorithm is able to entirely mitigate phase offset effect. However, according to the existence of cross term between signal and noise $N _ { k } , \theta _ { x } ( k )$ can not be the same value as $\theta _ { x } ^ { ' } ( k )$ In general, using Viterbi-Viterbi carrier recovery algorithm is able to recover the carrier offset with limited phase noise tolerance. More efficient and simple phase noise cancellation DSP algorithm is proposed in the section 3.5.2.

## 3.5.2 Pilot-aided Phase Noise Cancellation DSP Algorithm

In section 3.5.2, a novel phase noise cancellation DSP algorithm is proposed. In order to facilitate the theoretical analysis, experimental dual polarization (DP) quadrature phase-shift keying (QPSK) coherent systems based on pilot-tone-aided phase noise (PN) cancellation is under consideration. Figure 3.10 depicts the experiment setup of DP-QPSK optical coherent systems. In this experimental demonstration, vertical cavity surface emitting lasers (VCSELs) with approximate 300 MHz line-width are employed as transmitters and local oscillators for coherent detection of optical DP-QPSK signals. The proposed system, with central wavelength at 1540.49 nm, operates at 40 Gb/s over 80 km standard single mode fiber (SSMF) as part of a passive optical network (PON). At the transmitter side, one Oclaro
R optical QPSK modulator with 28 GHz bandwidth is employed. Fujistu
R 28 GHz 3 dB bandwidth coherent receiver is used for coherent detection.

The deployment of pilot-tone-aided PN cancellation algorithm guarantees a bit error rate (BER) performance below the forward error correction (FEC) threshold. Moreover, in order to detect the pilot tone in the signal spectrum, a novel digital signal processing (DSP) algorithm for adaptive pilot tone detection is evaluated.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/231f43ae08871e3ab73cf1fb2a1a06328e5a8f4529d9973630313329705bfd2d.jpg)  
Figure 3.10: DP-QPSK coherent systems experiment setup.

## Theoretical overview of the pilot-tone-aided technique

A complex modulated signal, whose information lies not only on its amplitude but phase as well, can be written as

$$
E _ { s } ( t ) = [ A _ { I } ( t ) + i A _ { Q } ( t ) ] \exp [ i ( \omega _ { s } t + \phi _ { s } ) ] ,\tag{3.19}
$$

where $\omega _ { s }$ and $\phi _ { s }$ are the signal’s carrier frequency and time dependent phase variable, and $A _ { I } ( t )$ and $A _ { Q } ( t )$ are respectively the real (in phase) and imaginary (quadrature) parts of the signal. In coherent system, the detection of the received signal is achieved by combining it with an external optical field represented by the local oscillator (LO). In this experimental implementation, the coherent receiver is of heterodyne type, meaning that the central frequency of the LO is different from the central frequency of the transmitted signal. Similarly to the received signal, the optical field associated with the LO can be written as

$$
E _ { L O } ( t ) = A _ { L O } ( t ) \exp [ i ( \omega _ { L O } t + \phi _ { L O } ) ] ,\tag{3.20}
$$

where $\omega _ { L O } , A _ { L O } ( t )$ and $\phi _ { L O }$ are respectively the carrier frequency, amplitude and time dependent phase variable of the LO. The pilot tone insertion, enabled by external double sideband modulation, can be written as

$$
E _ { p } ( t ) = A _ { p } ( t ) \exp [ i ( \omega _ { s } t - \omega _ { p } t + \phi _ { p } ) ] + A _ { p } ( t ) \exp [ i ( \omega _ { s } t + \omega _ { p } t + \phi _ { p } ) ] ,\tag{3.21}
$$

with $\omega _ { p } , A _ { p } ( t )$ and $\phi _ { p }$ being the double sideband carrier frequency, amplitude and time dependent phase variable of the additive pilot tone. The schematic diagram of double sideband first-null-point pilot-tone aided spectrum is shown in Figure 3.11.

Hence, the signal at the input of the coherent receiver (excluding the LO) can be expressed as

$$
\begin{array} { r } { E _ { i n } ( t ) = E _ { s } ( t ) + E _ { p } ( t ) + n ( t ) , } \end{array}\tag{3.22}
$$

where $n ( t )$ is the additive in-band Gaussian noise with zero mean and $\sigma _ { n } ^ { 2 }$ variance. The signals into the coherent receiver are assumed to be identically polarized. However, polarizations mismatch issues are solved at the receiver by an off-line DSP polarization demultiplexing algorithm. Therefore the output signal from the $9 0 ^ { \circ } .$ hybrid and balanced photodetectors is given as

$$
\begin{array} { r } { E _ { o } ( t ) = E _ { R } \exp [ i ( \Delta \omega t + \omega _ { p } t + \Delta \phi ^ { ' } ) ] } \\ { + E _ { R } \exp [ i ( \Delta \omega t - \omega _ { p } t + \Delta \phi ^ { ' } ) ] } \\ { - E _ { A } \exp [ i ( \Delta \omega t + \Delta \phi ) ] } \end{array}\tag{3.23}
$$

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/37769807edd1f6dce7d5a7502034848ea9b310283d7a28f0ae8aae27d31880e0.jpg)  
Figure 3.11: Schematic diagram of double sideband first-null-point pilot-tone aided spectrum.

with

$$
\left\{ \begin{array} { l } { E _ { R } = 8 E _ { p } ( t ) E _ { L O } ( t ) , } \\ { \Delta \omega \equiv \omega _ { s } - \omega _ { L O } , } \\ { E _ { A } = E _ { L O } ( t ) [ A _ { I } ( t ) + i A _ { Q } ( t ) ] . } \end{array} \right.\tag{3.24}
$$

As it can be seen, the output signal $E _ { o } ( t )$ consists of three terms, where the first and second term represent the double sideband pilot tone combined with the $\mathrm { L O ^ { 1 } }$ . The third term represents the beating between signal and LO, and as the detection is heterodyne then $\Delta \omega \neq 0$ The phase offsets, $\Delta \phi$ and $\Delta \phi ^ { ' }$ , respectively of the original signal and pilot tone in (5) are given as

$$
\left[ \begin{array} { l } { \Delta \phi } \\ { \Delta \phi ^ { ' } } \end{array} \right] = \left[ \begin{array} { l } { \phi _ { s } - \phi _ { L O } + \phi _ { n } } \\ { \phi _ { p } - \phi _ { L O } + \phi _ { n } ^ { ' } } \end{array} \right] ,\tag{3.25}
$$

where $\phi _ { n }$ is the random phase noise of the original signal and $\phi _ { n } ^ { ' }$ is the phase noise of pilot tone.

As the output signal from the 90◦-hybrid $E _ { o } ( t )$ is sampled by analog to digital converters (ADC), the k-th element of the output from the sampling process is denoted by $E _ { o } ( k )$ . Due to DSP utilization, the pilot-tone-aided PN cancellation algorithms firstly employs digital phase lock loop (DPLL) to compensate the frequency offset $\Delta \omega ( k )$ :

$$
E _ { o } ^ { ' } ( k ) = E _ { o } ( k ) \exp [ - i \Delta \omega ( k ) ] .\tag{3.26}
$$

Digital low-pass filtering is required to determine $E _ { A } \exp [ i ( \Delta \phi ) ]$ in 3.23. Consequently the adaptive pilot-tone detection-filter is implemented to detect pilot tone and estimate phase noise. In the experiment, pilot tone

and transmitted signal share the same phase noise, hence $\Delta \phi = \Delta \phi ^ { \prime }$ . This means that analysis of signal PN cancellation is expressed as

$$
E _ { P N C } ( k ) = E _ { A } ( k ) \exp [ i \Delta \phi ] \exp ( - i \Delta \phi ^ { ' } ) ,\tag{3.27}
$$

which results in the phase noise combined with transmitted signal to be canceled out

$$
E _ { P N C } ( k ) = E _ { A } ( k ) .\tag{3.28}
$$

## Adaptive pilot tone detection

The general configuration of the adaptive pilot-tone detection algorithm is shown in Figure. 3.12. This algorithm is widely used to suppress the narrowband interference in a wideband signal in spread-spectrum wireless communication. In the case of pilot-tone-aided PN cancellation, the transmitted signal sequence $E _ { o } ( k )$ is assumed to be wideband, and the pilot tone $E _ { p } ( k )$ is assumed to be a narrowband sequence instead. As, in the time domain, the two sequences are uncorrelated, a adaptive feed forward finite impulse response (FIR) filter design is able to detect the narrowband pilot tone from the transmitted signal.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/eb36167cf61305b6a29d68b1dddcc165af60f928c33cbbf1922e55d73fd37971.jpg)  
Figure 3.12: Pilot-tone-aided PN cancellation using adaptive pilot tone detection schematic.

Because of the narrowband characteristics of the pilot tone, the delayed sample $E _ { o } ( k - D )$ is used to estimate the pilot tone in the spectral domain. As the spectrum of the pilot tone is much narrower compared to the signal, then $D = 1$ is selected in order to meet the uncorrelation requirement. The resulting output of the FIR filter is given as

$$
E _ { p } ^ { ' } ( k ) = \sum _ { n = 0 } ^ { N - 1 } h ( n ) E _ { o } ( k - n - D ) , ( k = 1 , 2 , . . . ; n = 0 , 1 , 2 , . . . , N - 1 ) ,\tag{3.29}
$$

where $h ( n )$ are the FIR filter coefficients. And the error signal used in adaptive FIR filter coefficients optimization is $e ( k ) = E _ { o } ^ { ' } ( k ) - E _ { p } ^ { ' } ( k )$ . The minimum summation of errors leads to the determination of the optimal FIR coefficients. According to the delay D, the least mean square (LMS) algorithm for the coefficients optimization is

$$
h _ { k } ( n ) = h _ { k - 1 } ( n ) + e ( k ) E _ { o } ( k - n - D ) , ( k = 1 , 2 , . . . ; n = 0 , 1 , 2 , . . . , N - 1 ) ,\tag{3.30}
$$

moreover pilot-to-signal ratio (PSR) at first-null-point of the signal spectrum has a significant influence on receiver performance. Spectrum characteristic of pilot tone is assumed to be Gaussian normal distribution. PSR is defined as $\mathrm { P S R } = - 1 0 \log _ { 1 0 } \exp ( - \Delta v ^ { 2 } )$ , where $\Delta v$ is the pilot tone laser linewidth. In the experiment, PSR> 7dB is selected to guarantee linewidth tolerance is approximate 300 MHz per laser in the 10 Gbaud DP-QPSK coherent system.

## Experiment setup

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/de8db980147fd931bb23b8f5c7be39c715d07247d1e0541be57a976e03a9a198.jpg)  
Figure 3.13: Pilot-tone-aided PN cancellation experiment setup

Figure. 3.13 shows the experiment setup for a 40 Gb/s DP-QPSK transmission system based on pilot-tone-aided PN cancellation algorithm. At the transmitter side, the optical source consists of a single VCSEL operating at 1540.49 nm (194.6085 THz), which is used to generate both signal and pilot tone. The electrical signal source is a pulse pattern generator (PPG) working at 10 Gbaud and generating a pattern of $2 ^ { 1 5 } – 1$ bits used to drive the optical $\mathrm { I } / \mathrm { Q }$ modulator. An external Mach-Zehnder modulator (MZM) driven by an electrical synthesizer is used to generate the pilot tone, which is placed at the double sideband first-null-point (10 GHz) of the signal spectrum. Hence, after they are optically combined, both pilot tone and QPSK signal experience the same type of phase noise. In order to generate a dual polarization state, the optical signal is separated into two orthogonal polarizations by a polarization beam splitter (PBS). Before recombination in a polarization beam combiner (PBC), one of the polarization states propagates through an optical delay line, which decorrelates it from the other orthogonal state. The resulting optical signal is a pilot-tone aided 40 Gb/s DP-QPSK signal.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/7b3a3faf8720fab82232b2e83542aa5f495681ad18fe5112891865a39ca0f42e.jpg)  
Figure 3.14: Pilot-tone-aided received signal spectrum.

The pre-amplified receiver consists of a second VCSEL operating at 1540.48 nm (194.6098 THz) used as LO, two 90◦-hybrids (dual polarization operation), balanced detectors, a 40 GSa/s digital sampling oscilloscope which is used to sample the in-phase and quadrature components from the received signal, and a computer for signal processing. The pilot-tone aided received signal spectrum is shown in Figure 3.14. The first block consists of clock recovery, followed by pilot-tone aided PN cancellation. The frequency domain chromatic dispersion (CD) compensation algorithm is used to compensate for 80 km SMF transmission, and is followed by the constant modulus algorithm (CMA), utilized to enable polarization demultiplexing. Phase and frequency recovery based on Viterbi-Viterbi algorithm is employed to compensate the residual phase and frequency offset after pilot-tone-aided PN cancellation. A decision feed-forward and a decision feedback FIR equalizer are implemented to compensate inter symbol interference (ISI), and hence improve system performance. Bit error detection is also applied to evaluate the system’s BER performance.

## Experiment results

Figure. 3.15 shows the constellations diagrams for the 40 Gb/s DP-QPSK signal generated by using the Viterbi-Viterbi or the pilot-tone-aided algorithm. Constellation rotation caused by phase noise is successfully compensated by using the pilot-tone-aided algorithm.

Received Signal  
![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/a620b89613043efa1d69bbbccb6116a4110dfd66d0157d4a2a4af3f7bbac58fd.jpg)

w/ Viterbi-Viterbi  
![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/b1d48c605a52df6cabd0d684b024adb38182925cb6c17bcebd7168de3cae95c5.jpg)

w/ Pilot-tone-aided  
![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/81f7223b679664961031e6db2036bcca23f2bcf7dcd0f2ddbc6e77b3d4ffb458.jpg)

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/8670f1e2039c5eb8c4874aa4f7a666b71f1a5147eeb09ba62e8b6cd0d01cb954.jpg)

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/77e9843ebd38cc8efdc65e0e47bedd5e2376e90e54e9264a8b56624d9015410c.jpg)

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/821f68a339c041810eeaf15ab1cf64cdfa0b194d7a732e317a63e05f24640522.jpg)  
Figure 3.15: Pilot-tone-aided PN cancellation experiment results of two orthogonally polarized signals constellation (a). received signal; (b). output of using Vibterbi-Viterbi carrier recovery algorithm; (c). output of using pilot-tone-aided PN cancellation.

Figure. 3.16 shows the phase tracking comparison results between pilottone aided PN cancellation algorithm and Viterbi-Viterbi phase recovery algorithm. As it can be noticed, the pilot-tone aided algorithm is able to track the original phase information from the received signal. Figure. 3.17 shows the measured BER performance for single- and dual-polarization QPSK systems in back-to-back and after 80 km transmission in SMF. CD compensation is performed via off-line processing at the receiver side. As a result, the BER performance difference between back-to-back and 80 km SMF transmission is less than 0.5 dB. Furthermore, the utilization of the pilot-aided tone PN cancellation guarantees the BER performance below the threshold of 7% overhead FEC.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/0b382aa69ea2003598c1fd5b105e5a31cd73a99b627315d58eb6038ff8a57dbe.jpg)  
Figure 3.16: Pilot-tone-aided samples phase tracking results.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/dbcc47d1f857a9251c8872e5a6929627092934ae7b711396042eda6d585cc621.jpg)  
Figure 3.17: BER performance of pilot-tone-aided PN cancellation experiment.

## Conclusion of pilot-tone-aided phase noise cancellation algorithm

In section 3.5.2, experimental results for a high phase-noise tolerant pilottone aided 40 Gb/s DP-QPSK optical coherent system are presented. Both transmitter and LO lasers were free running VCSELs with approximately 300 MHz linewidths. An 80 km SMF transmission for PON system was successfully demonstrated by using pilot-tone-aided and off-line DSP dispersion compensation algorithms. Additionally, this thesis presents also a comparison between pilot-tone-aided and Viterbi-Viterbi phase recovery algorithms. The implementation of the pilot-tone aided algorithm resulted in a BER performance below 7% FEC threshold.

A novel pilot-tone detection DSP algorithm based on adaptive FIR filtering is also presented. In this case, the pilot tone is employed at the double-side first-null-point of the signal spectrum with no need for overhead in the frequency domain. For instance, in 40 Gb/s DP-QPSK systems, the pilot tone is inserted at 10 GHz first-null-point of transmitted signal. According to theoretical analysis, a line-width tolerance of approximately 10 MHz per laser [64, 65]for a 40 Gb/s DP-QPSK coherent system has been improved to 300 MHz.

## 3.6 Spectrum Narrowing induced Inter Symbol Interference Compensation DSP Algorithm

As it is discussed in previous sections, with the rapid growth of capacity requirements of optical transmission networks, there is a strong need to realize high capacity and high spectral efficient (SE) optical communication systems. The ultra dense wavelength division multiplexing (U-DWDM) technology based on advanced modulation format is a promising solution and is being intensively studied [66, 67]. U-DWDM technology requires optical or electrical pre-filtering to fulfil Nyquist sampling criterion [68]. Details of theoretical analysis will be presented in the subsequent chapter. Meanwhile, to facilitate ease of optical networking, tolerance of spectrum narrowing is critical, as signal channel spacing is degraded after transmission through optical channel, especially when reconfigurable optical add/drop multiplexers (ROADMs) nodes are used in the network [69]. Schematic of metro access networks with ROADMs application is shown in Figure 3.18. ROADMs spectrum narrowing effect is depicted in Figure 3.19. As it can be noticed in Figure 3.19, fifteen Gaussian order 3 band pass filters cascaded introduce approximate 70% channel bandwidth narrowing.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/c3896f0082b274a5598de7bc0a40edbb333d64098620430a98b12ce853edc593.jpg)  
Figure 3.18: Schematic of metro access networks with ROADMs application.

Spectrum narrowing severely induce inter symbol interference (ISI) between continual transmitted sequences. Therefore, ISI compensation is essential to improve U-DWDM system performance in terms of optical signal to noise ratio (OSNR). Conventional digital signal processing (DSP) algorithm using adaptive decision feed forward equalizer is an inefficient solution, since this finite impulse response (FIR) filter enhance noise during compensation of spectrum narrowing [70].

Although maximum-likelihood sequence estimation (MLSE) method has been successfully proved to mitigate ISI [71], the complexity of MLSE is exponentially increasing with the length of transmitted sequence. When the sequence length is becoming large, optimal MLSE is unfeasible.

Therefore, in order to achieve high spectrum narrowing tolerant optical communication systems, an adaptive channel estimation DSP algorithms combined with decision feedback equalizer is proposed in section 3.6. As a result, a high spectrum narrowing tolerance of proposed algorithms for 112 Gb/s dual polarization (DP) quadrature phase shift keying (QPSK) transmission system is demonstrated by both simulation and experiment.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/5ad10da2643a777dd92c545a2029daea23a6f8108b68bed35f5624ef49a02f07.jpg)  
Figure 3.19: ROADMs bandwidth narrowing analysis.

## Theoretical overview of adaptive channel estimation technique

The proposed adaptive channel estimation algorithm schematic is shown in Figure 3.20. The polarization multiplexed signals are firstly fed into coherent detection receiver. Afterward, the received signals are sampled by analog to digital convertor (ADC) to two samples per symbol. The output digitized signals are fed into a butterfly filter composed of four feed forward FIR filters. As it is discussed in previous section, CMA algorithm is used to improve polarization demultiplex performance and compensate polarization rotation. The signals are sent to Viterbi-Viterbi carrier recovery block to demultiplex inphase and quadrature components and then to the adaptive channel estimation block.

The adaptive channel estimation requires estimation of noise level $\eta _ { k } ;$ feed forward FIR tap coefficients $c _ { k }$ and feed back equalizer tap coefficients $p _ { k }$ . For instance, in one orthogonal polarization, denoted as x-polarization, input of channel estimation is $x ( k )$ Since a finite length feed forward equalizer is unable to cancel noncausal ISI completely, the feed back filter coefficients should be optimized according to the MMSE criterion whereby the additive noise power resulting from residual ISI is minimized. The correct channel estimation of $c _ { k }$ and $p _ { k }$ is able to minimize minimum mean square error (MMSE) between original transmitted signals and decision signals [72], which can be presented as

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/8c5df047ca7a253663d2adc4fbd0396b8f426f98ca87f4f0dfa8b948016435b0.jpg)  
Figure 3.20: Schematic of adaptive channel estimation DSP algorithm.

$$
\operatorname* { m i n } \{ E [ \hat { x } ( k ) - x _ { d } ( k ) ] ^ { 2 } \} ,\tag{3.31}
$$

where $E \{ \cdot \}$ represents statistical expectation, ${ \hat { x } } ( k ) , x _ { d } ( k )$ are the outputs from adaptive equalizer and decision slicer respectively. Moreover ${ \hat { x } } ( k )$ can be presented as

$$
\hat { x } ( k ) = x ^ { ' } ( k ) - \eta _ { x } ( k )\tag{3.32}
$$

with

$$
\left\{ \begin{array} { l l } { x ^ { ' } ( k ) = c _ { k } \cdot x ( k ) } \\ { x ^ { ' \prime } ( k ) = x ^ { ' } ( k ) - \eta _ { x } ( k ) } \\ { x _ { b } ( k ) = p _ { k } \cdot x _ { d } ( k ) } \end{array} \right.\tag{3.33}
$$

where $x ^ { ' } ( k )$ is the symbol estimation after feed forward FIR filter, $x ^ { \prime \prime } ( k )$ is noise subtracted result of $x ^ { ' } ( k )$ , and $x _ { b } ( k )$ is the output from decision feed back filter. Here, $c _ { k }$ is known as coefficient of feed forward FIR filter, $p _ { k }$ is coefficient of decision feed back filter, and $\eta _ { k }$ is the coefficient of noise level estimation. The stochastic adaptive algorithm to find $c _ { k } , \eta _ { k }$ and $p _ { k }$ can be implemented using the least mean square (LMS) algorithm [73]. The error factor is denoted as

$$
e _ { k } = x ^ { ' } ( k ) - x _ { d } ( k ) - \eta _ { x } ( k ) ,\tag{3.34}
$$

where $\eta _ { x } ( k )$ is the noise level estimation with linear expression of

$$
\eta _ { x } ( k ) = \eta _ { k } \cdot x _ { d } ( k ) .\tag{3.35}
$$

Moreover, the adaptive update equations of $c _ { k } , p _ { k }$ and $\eta _ { k }$ can be presented as

$$
\left\{ \begin{array} { l l } { c _ { k + 1 } = c _ { k } + \mu e _ { k } x ( k ) } \\ { p _ { k + 1 } = p _ { k } - \gamma e _ { k } x ( k ) } \\ { \eta _ { k + 1 } = ( 1 - \rho ) \eta _ { k } + \rho e _ { k } } \end{array} \right.\tag{3.36}
$$

where, $\mu$ is the step size of feed forward FIR equalizer; $\gamma$ is the step size of feed back equalizer and $\rho$ is an integration factor (a small value used to average $e _ { k }$ over time k) [73]. As a result, symbol estimation $x ^ { ' } ( k )$ is a estimation vector, which is given as

$$
x ^ { ' } ( k ) \in \{ x ^ { ' } ( k - n ) , x ^ { ' } ( k - n - 1 ) , x ^ { ' } ( k - n - 2 ) \ldots x ^ { ' } ( k - 1 ) \}\tag{3.37}
$$

where n is the length of feed back equalizer. Operation of noise subtracted $x ^ { ' } ( k )$ combined with proper channel estimation coefficients from received signals is used to cancel most of precursor ISI [74]. According to accuracy estimation requirement of noise level $\eta _ { x } ( k )$ , length of decision feed back equalizer can not be insufficient. Compared to the practical complexity requirements of MLSE algorithm, proposed adaptive channel estimation algorithm is feasible.

## Experiment setup and results

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/b637328976dba2d68af706c43d566581b5091b0edc47520876642ade31d36c26.jpg)  
Figure 3.21: 112 Gb/s DP-QPSK transmission experiment setup with adaptive channel estimation algorithm implementation.

Figure 3.21 shows the experiment setup of 112 Gb/s DP-QPSK optical communication system. A distributed feedback (DFB) laser operating at 1549.53 nm (193.47 THz) with 10 MHz line-width is used as optical signal source to generate the QPSK signal. The pulse pattern generator (PPG) working at 28 Gbaud $\cdot / \mathrm { s }$ is operated as electrical signal source with $2 ^ { 1 5 } - \mathrm { \dot { 1 } }$ bit length to drive the optical QPSK modulator. After the QPSK modulator, optical channel is separated into two orthogonal polarizations by a polarization beam splitter (PBS). Afterward, two branches of orthogonally polarized optical channels are combined by a polarization beam combiner (PBC) to generate the 112 Gb/s DP-QPSK signal. The Finisar wave-shaper is then used as spectrum pre-filtering optical bandpass filter (OBPF). The OBPF is able to tune full width at half maximum (FWHM) of transmitted signal. FWHM is defined as 3 dB bandwidth of transmitted signal. At the receiver side, the pre-amplified coherent receiver structure is implemented. A tunable optical band-pass filter (with 0.5 nm/62.5 GHz FWHM) is used after the pre-amplifier in order to remove ASE noise from the EDFA. The local oscillator (LO) is a wavelength tunable external cavity laser (ECL) with 100 kHz line-width. In the coherent receiver structure, tuning LO wavelength enables channel selection due to optical heterodyning at the photodiode. The coherent receiver consists of two 90◦-hybrids and balanced detectors. The 80 $\mathrm { G b } / \mathrm { s }$ digital sampling oscilloscope at the coherent receiver is used to sample the inphase and quadrature components.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/a6f907e9ecd8986e9491b1d5cc3f31c67eb860a268e8ed4d4bcf91a4bd52f6cf.jpg)  
Figure 3.22: BER performance of 112 Gb/s DP-QPSK coherent systems.

Figure 3.22 shows the back to back transmission bit error rate (BER) performance in terms of OSNR. In both results of simulation and experiment for back to back transmission, at 20 dB OSNR measurement point, BER performances are approaching zero, and at 16 dB OSNR measurement point, BER performances are around $1 0 ^ { - 3 }$ In the experiment, these two OSNR measurement points $( \mathrm { O S N R { = } 1 6 d B }$ and $\mathrm { O S N R = 2 0 d B } )$ are under consideration and adaptive channel estimation DSP algorithm is implemented to compensate ISI induced by spectrum narrowing effect. Moreover constant modulus algorithm (CMA) is also employed to enable polarization rotation compensation, various DSP algorithms discussed before, such as frequency and phase off set recovery, QPSK demodulation and bit error detection are also implemented in section .

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/dbde79a5aee3993c9e5f188fc0e351d006f11e80b9640ea00f3ca9b873fdf4d4.jpg)  
Figure 3.23: BER penalty vs. bandwidth narrowing with and without adaptive channel estimation algorithm @ 20 dB OSNR.

Figure 3.23 and Figure 3.24 show the experiment BER results. In the experiment, 20 dB OSNR and 16 dB OSNR measurement points are under consideration. At 20 dB OSNR measurement point, in case of without spectrum narrowing effect, BER performance is error free. As the signal spectrum space degrading, BER penalty grow dramatically. Meanwhile, using adaptive channel estimation algorithm, strongly reduce the BER penalty.

Especially at 20 GHz bandwidth (71% of original signal bandwidth), BER penalty is approximately reduced 2 dB by using adaptive channel estimation algorithms. At 16 dB OSNR measurement point, in case of with out spectrum narrowing effect, BER performance is around $1 0 ^ { - 3 }$ . At 20 GHz bandwidth (71% of original signal bandwidth), BER penalty is also approximately reduced 2 dB by using adaptive channel estimation algorithms.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/6d1edc63ba3743e6c2c505e1f156abce7b749601c89a9534007a46c0ccbbd762.jpg)  
Figure 3.24: BER penalty vs. bandwidth narrowing with and without adaptive channel estimation algorithm @ 16 dB OSNR.

Therefore the proposed adaptive channel estimation DSP algorithm is successfully demonstrated in high spectrum narrowing tolerant 112 Gb/s QPSK polarization multiplex optical communication systems. The experiment results show that in case of 71% spectrum narrowing, proposed algorithm mitigate 2 dB BER penalties with both 16 dB OSNR and 20 dB OSNR cases. Compared to high computational complexity requirement of MLSE algorithm, proposed adaptive channel estimation DSP algorithm is feasible and practical.

## 3.7 Summary

This chapter has presented various digital signal processing algorithms associated with DP-QPSK optical transmission coherent systems. Such DSP algorithms are used to compensate for different transmission impairments. DSP algorithms discussed in chapter 3 include:

• A block-overlap CD compensation algorithm, which enables the offline CD compensation with less complexity requirement than conventional serial frequency all-pass filter.

• A Gardner clock reovery algorithm, which enables sample clock mismatch compensation without the need for complicated optical phase lock loop.

• A butterfly FIR structure of polarization demultiplexing algorithm, which enables polarization multiplexing and rotation compensation.

• Comparison between Viterbi-Viterbi carrier recovery algorithm and pilot-aided phase recovery algorithm. Using feasible pilot-tone aided phase noise cancellation algorithm significantly improve laser line-width tolerance of optical transmission systems.

• A novel adaptive channel estimation algorithm, which enables the inter symbol interference compensation induced by spectrum narrowing effect.

Chapter 4

# DSP Algorithms for Multi Dimension CAP Modulation

## 4.1 Introduction

In the previous chapters, digital signal processing algorithms for optical coherent detection has been discussed. Optical coherent systems associated with DSP are considered as the promising solution for high capacity and high spectrum efficiency demand in next generation of optical transmission systems. Additional challenge of future optical networks is to support multiple users with access to multiple services such as voice, data, images and video while sharing the same physical infrastructure. Figure 4.1 shows the scenario of next generation optical networks supplying various services. In order to fulfill such requirements, carrierless amplitude-phase (CAP) modulation is considered as feasible solution. CAP modulation has been intensively studied for copper wires communication [75–77]. CAP is a multi dimensional and multi level signal modulation format employing orthogonal waveforms. These waveforms are generated by using FIR filters with orthogonal impulse responses in time domain, i.e. statistical expectation of correlation between different waveforms is zero. In principle, CAP modulation is similar to orthogonal frequency division multiplexing (OFDM) modulation, in the sense that both of CAP and OFDM support multiple levels modulation with more than one dimension or sub-carrier. Contrary to OFDM, generation of orthogonal sub-carriers in frequency domain is not required for CAP. Additionally, CAP supports modulation in more than two dimensions, provided that orthogonal pulse shapes can be identified [77]. This possibility of multi dimensional modulation makes CAP an attractive modulation format for next generation multiple services access networks. In chapter 4, DSP algorithms for multi dimensional multi level CAP modulation are under investigation. Similar as chapter 3, DSP algorithms used for CAP optical communication systems are implemented to compensate for transmission impairments. Chapter 4 is divided into three sections. After introductory section, general theoretical analysis for CAP modulation will be firstly introduced. Afterward, DSP algorithms for CAP optical transmission channel estimation are under investigation. Finally a bi-directional CAP transmission experiment using DSP channel estimation algorithm for passive optical networks will be demonstrated.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/487225511ff8640e8767b2b1de7a67b5c3413cc7b07ce88179d57bb20e3d75a0.jpg)  
Figure 4.1: Scenario of next generation optical networks supplying various services.

## 4.2 Theoretical Overview of CAP Technique

The basic idea of CAP generation is to use different pulse shapes as signature waveforms to modulate different data streams. At the transmitter side the signature waveforms are generated by orthogonal shaping FIR filters. At the receiver side the individual data streams are reconstructed by using match filter. The match filter used in the receiver has an impulse response which is the time domain inversion of the impulse response of the transmitter filter. For instance, 2D CAP modulation employs a product of a square-root raised cosine filter and sine or cosine waveforms. Perfect reconstruction (PR) at the receiver is secured through the orthogonality of two FIR filters (sine and cosine). The square-root raised cosine waveform can be expressed as Equation 4.1,

$$
h _ { S R R C } ( t ) = \frac { 4 \alpha } { \pi \sqrt { T } } ( \frac { T ^ { 2 } } { T ^ { 2 } - 4 \alpha t } ) [ \cos ( \frac { ( 1 + \alpha ) \pi t } { T } ) + \frac { T } { 4 \alpha t } \sin ( \frac { ( 1 - \alpha ) \pi t } { T } ) ]\tag{4.1}
$$

where T is a symbol period and α is the roll-off factor. The α factor influences the signal excess bandwidth in frequency domain.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/360585a5921dd4ae0c85e54777a0bf5e4283dd2c5dc2e5c8e745ca895a449282.jpg)  
Figure 4.2: Schematic of n-dimensional CAP transponder.

The two orthogonal pulse shapes used as signature waveforms multiplied with the square-root raised cosine waveform are respectively given as

$$
\left\{ \begin{array} { l } { f _ { 1 } ( t ) = h _ { S R R C } ( t ) \cos 2 \pi f _ { c } t } \\ { f _ { 2 } ( t ) = h _ { S R R C } ( t ) \sin 2 \pi f _ { c } t } \end{array} \right.\tag{4.2}
$$

where $f _ { c }$ is the carrier frequency suitable for the pass-band filters. The pair of waveforms $f _ { 1 }$ and $f _ { 2 }$ constitute a Hilbert pair. The Hilbert pair consists of two pulse shapes with the same magnitude response but phase response shifted by 90 degree. Furthermore, different branches of modulated signals are combined as transmitted signals to drive the direct modulated laser. At the receiver side, the optical signals are detected by photodiode. The inversion of the transmission filters are implemented to retrieve the original sequence of symbols. The original data can be recovered after down sample and demapping process. The general configuration of n-dimension CAP transponder is shown in Figure 4.2.

Higher dimensionality CAP can be implemented by modulating the data streams using more than two signature waveforms. These signature waveforms need to maintain the orthogonality. In order to fulfill such requirement, the up sampling factor needs to be increased. In that sense, high dimensionality should not be treated as a straight-forward method of increasing spectral efficiency. The Hilbert pair used for 2D CAP can not be used for higher dimensional CAP. Therefore, the new set of match filters need to be designed. A mini-max optimization approach has been previously employed to extend the conventional 2D CAP scheme to higher dimensionality such as 3D and 4D CAP. In section 4.2, the optimization algorithm in [78] has been used. The advantage of this formulation is that the frequency magnitude response of the transmitter and receiver filters will be exactly the same at both sides. Additionally, it is a straight-forward method to extend the design to higher dimensionality CAP systems. In Equation 4.3 the variables $f _ { i }$ and $g _ { j }$ represents the CAP transmitter and receiver FIR filters respectively.

$$
\begin{array} { r l } & { P ( f _ { i } ) g _ { j } = \vec { \delta } , \quad i \in \{ 1 , 2 , 3 , 4 \} } \\ & { P ( f _ { i } ) g _ { j } = \vec { 0 } , \quad i , j \in \{ 1 , 2 , 3 , 4 \} \mathrm { ~ a n d ~ } i \neq j } \end{array}\tag{4.3}
$$

where $P ( f _ { i } )$ is a function of shift matrix that operates on vector $f _ { i } , \vec { \delta }$ is a vector with unity elements and $\vec { 0 }$ is a vector of all zeros. The optimization algorithm for high dimensionality CAP is described as follows

$$
\operatorname* { m i n } _ { f _ { 1 } , f _ { 2 } , f _ { 3 } , \ldots f _ { N } } \operatorname* { m a x } \left( | F _ { 1 } ^ { \prime } | , | F _ { 2 } ^ { \prime } | , | F _ { 3 } | , \ldots | F _ { N } ^ { \prime } | \right)\tag{4.4}
$$

subject to the PR condition in Equation 4.3 and

$$
g _ { i } = [ F _ { i } ] ^ { - 1 } , i \in \{ 1 , 2 , 3 , . . N \}\tag{4.5}
$$

where $F _ { i }$ is the discrete Fourier transform (DFT) of vector $f _ { i } .$ The $F _ { i } ^ { ' }$ is the out-of-band portion of the transmitter response above the boundary frequency $f _ { B } .$ which is used to ensure the receivers frequency response will be exactly the same as the transmitters. This means that the out-of-band spectral content of the filters is designed to be zero. For the multi dimension CAP system, there is minimum bandwidth requirement denoted as $f _ { B , m i n }$ that will allow a PR condition. Any value smaller than $f _ { B , m i n }$ will not result in a PR solution. For instance, the $f _ { B }$ for 3D CAP system is at least equal to or greater than $\scriptstyle { \frac { 3 } { 2 T } }$ to preserve the PR condition [78]. Time domain cross correlation responses of match filters are shown in Figure 4.3. Moreover Figure 4.4 shows the optimized match filter impulse and frequency responses for 3D CAP.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/99c3d4b4d8c3740beed98d209f471e1503dea25bc690d2c9ee41755dee83e79a.jpg)  
Figure 4.3: 3D CAP cross correlation responses of transmitter-receiver match filters.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/8f603fd98e9bcfaa37a64b0cf2d7654d9036a3c5022394267e604a1476b66549.jpg)  
Figure 4.4: 3D CAP optimal match filter impulse and frequency responses.

## 4.3 DSP Algorithms for CAP Transmission Channel Estimation

In optical multi dimensional CAP transmission systems, inter symbol interference (ISI) induced by transmission impairments and multi dimensions cross talk is the main factor of system performance degrading. In section 4.3, a blind equalization using constant modulus algorithm (CMA) for CAP transmission channel estimation will be proposed. As it is stated in previous section, CMA equalizer is capable of tracking channel characteristic adaptively and compensating for transmission impairments effectively [79]. Moreover, blind CMA equalizer is simple to implement and suitable to equalize constant envelope signal, such as n-PSK signal. However, such CMA equalizer is not able to be used directly to multi dimensional CAP with advanced modulation format such as 16 QAM. Therefore, a coordinate transformed CMA equalizer is presented in this thesis for optical multi dimensional CAP transmission systems.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/c83fe966984c76ea7e739357054d1936afb7c185a4936a48ddf224bba1593e25.jpg)  
(a)

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/2b9fa6c708196fe7dcd74eed1ef2c242c508d451b5640172128addd4ab848384.jpg)  
(b)  
Figure 4.5: Blind CMA Equalizer for 16 QAM Constellation: (a) conventional circle classed CMA for 16 QAM; (b) coordinate transformed CMA 16 QAM with highlighted unified circle.

## 4.3.1 Theoretical overview of blind CMA Equalizer

To fulfil the theoretical analysis of blind CMA Equalizer, multi dimensional CAP with 16 QAM modulation format is under investigation. In general, two types of CMA equalizer are capable of n-QAM modulation format channel estimation. Figure 4.5(a) and Figure 4.5(b) show the principle of conventional circle classed CMA and coordinate transformed CMA for 16 QAM based on constellation diagram. In case of conventional circle classed CMA, signals of 16 QAM are divided into three categories with different radius. That means three different structures of CMA equalizer are required to implement conventional circle classed CMA. Since the sixteen clusters of 16 QAM constellation are transformed into unified circle to generate four clusters as QPSK, coordinate transformed CMA is simple and feasible to employ.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/3efefc01aedffa722456a05ec8aef33b0db270b271986a549f4dca53340a770f.jpg)  
Figure 4.6: Structure of n dimensional CAP transmission channel estimation using coordinate transformed (CT) blind CMA equalizer.

The transformed signals by using coordinate transformed CMA can be presented as

$$
x _ { n , n e w } ^ { ' } ( k ) = \{ x _ { n , R } ^ { ' } ( k ) - 2 \mathrm { s i g n } [ x _ { n , R } ^ { ' } ( k ) ] \} + i \{ x _ { n , I } ^ { ' } ( k ) - 2 \mathrm { s i g n } [ x _ { n , I } ^ { ' } ( k ) ] \}\tag{4.6}
$$

where sign[ ] represents sign function. $x _ { n , R } ^ { \prime } ( k )$ and $x _ { n , I } ^ { ' } ( k )$ are real (inphase) and image (quadrature) part of one dimensional CAP signals after signal detection. The update function of adaptive N-taps weight vector $w _ { n } ( k )$ using least mean square (LMS) algorithm is given as

$$
w _ { n } ( k + 1 ) = w _ { n } ( k ) + \mu x _ { n , n e w } ^ { ' } ( k ) e ( k ) x _ { n } ^ { * } ( k )\tag{4.7}
$$

where $\mu$ is the step size of LMS algorithm and e(k) is the error function, which can be presented as

$$
e ( k ) = R ^ { 2 } - | x _ { n , n e w } ^ { ' } ( k ) | ^ { 2 }\tag{4.8}
$$

where R is the radius of unified circle. Moreover sufficient length of adaptive N-taps weight vector is required to validate the coordinate transformed CMA.

## 4.3.2 Bi-directional Multi Dimension CAP transmission demonstration

As it is discussed in the section 4.3.1, implementation of channel estimation DSP algorithms is under consideration as a promising solution to enable the multi Gb/s passive optical networks (PON) transmission. In section 4.3.2, an experimental demonstration concerning bi-directional multi dimension CAP transmission will be presented. To the best of author’s knowledge, this is the first demonstration of a bi-directional optical link using multi dimensional CAP and employing directly modulated (DM) vertical cavity surface emitting lasers (VCSELs) operating around 1550 nm wavelength (193.4145 THz) as transmitters.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/64413d608f17173e4353f55f19a209c836676d86b49d3ab0bd0b9640ecc4b863.jpg)  
Figure 4.7: Experiment setup of multi dimensional CAP bi-directional transmission.

Figure. 4.7 shows the setup implemented in the experiment. The arbitrary waveform generator (AWG) with 12 GSa/s is used to generate the 3D and 4D CAP with 2 Level/Dimension $\left( \mathrm { L } / \mathrm { D } \right)$ and 4 Level/Dimension (L/D) signals. For example, 3D CAP constellations with $\scriptstyle 2 \mathrm { - L } / \mathrm { D }$ and 4-L/D are shown in Figure 4.8 and Figure 4.9. As it can be noticed, denotation of $\scriptstyle 2 \mathrm { - L } / \mathrm { D }$ can be considered as QPSK in two dimensional modulation format, as well the denotation of $\scriptstyle 4 - \mathrm { L } / \mathrm { D }$ can be considered as 16 QAM in two dimensional modulation format.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/46db1ffe3fe7cc0e91c1e6bba70fd8705fc1e40f4a2d30558baf375951ff6113.jpg)  
Figure 4.8: 3D CAP with 2-L/D.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/4389313e3a6199460d072eac31ae119fc35a1dfab6aec38e4137bf12f671bf96.jpg)  
Figure 4.9: 3D CAP with 4-L/D.

As it is shown in the experiment setup configuration, for down link, data in the transmitter side is firstly mapped according to the given modulation level, such as 2-L/D and $\scriptstyle 4 - \mathrm { L } / \mathrm { D }$ . Those symbols are up sampled and later shaped (or filtered), according to the optimization algorithm. The transmitter signature filters are implemented as fixed FIR filters. The 3D CAP signals at bit rate of $4 . 5 \ : \mathrm { G b / s } \ : ( \mathrm { 2 - L / D ) }$ with an up sampling factor of 8 and 7.2 Gb/s (4-L/D) with an up sampling factor of 10 are generated by the arbitrary waveform generator (AWG). Meanwhile, for 4D-CAP, signals at bit rate of 4 Gb/s (2-L/D) with an up sampling factor of 12 and 5.3 Gb/s (4-L/D) with an up sampling factor of 18 are generated. Afterward, optical CAP signals are directly modulated with 1548.24 nm (193.63 THz) VCSEL with 4.5 GHz bandwidth operating at 4 mA bias level.

<table><tr><td>Signal</td><td>3D 2-L/D</td><td>3D  $\scriptstyle 4 - \mathrm { L } / \mathrm { D }$ </td><td>4D  $\scriptstyle 2 \mathrm { - L } / \mathrm { D }$ </td><td> $\mathrm { 4 D ~ 4 - L / D }$ </td></tr><tr><td>BR (Gb/s) inc. 7% FEC</td><td>4.5</td><td>7.2</td><td>4</td><td>5.3</td></tr><tr><td>SE (bits/s/Hz)</td><td>2.25</td><td>3.6</td><td>1</td><td>1.325</td></tr><tr><td>Up sampling factor</td><td>8</td><td>10</td><td>12</td><td>18</td></tr><tr><td>Bandwidth (GHz)</td><td>2</td><td>2</td><td>4</td><td>4</td></tr><tr><td>Symbol rate (Gbaud)</td><td>1.5</td><td>1.2</td><td>1</td><td>0.67</td></tr></table>

Table 4.1: 3D/4D CAP up & down link: bit rate, spectral efficiency, up sampling factor, bandwidth and symbol rate with $\scriptstyle 2 \mathrm { - L } / \mathrm { D }$ and $\scriptstyle 4 - \mathrm { L } / \mathrm { D }$

In the down link receiver side, a photodiode with 10 GHz bandwidth is used for direct detection. A 40 GSa/s digital sampling oscilloscope (DSO) is employed to sample the received analog signals. As it has been discussed in previous section, off-line DSP algorithms include receiver match filter, down sampling, signal demapping and DSP algorithm for channel estimation. Finally the BER performance in terms of received optical power are obtained to measure the CAP system performance. Mean parameters of bi-directional 3D and 4D CAP transmission experimental demonstration with $\scriptstyle 2 \mathrm { - L } / \mathrm { D }$ and $\scriptstyle 4 - \mathrm { L } / \mathrm { D }$ modulation formats are shown in Table 4.1. Furthermore, the similar transmitter-receiver structure is used for the up link transmission. However the carrier frequency is assigned to be different from down link carrier. The optical CAP signals of down link are directly modulated with 1548.96 nm (193.54 THz) VCSEL. As it can be noticed, approximate 100 GHz channel spacing between up and down link is employed to mitigate cross talk interference. Moreover, off-line DSP algorithms of blind CMA channel estimation equalizer are implemented to compensate for inter symbol interference (ISI) induced by 20 km standard single mode fiber (SSMF) transmission impairments.

Results of BER performances in terms of received optical power are presented as below. Figure 4.10 and Figure 4.11 show the comparison between with and without channel estimation DSP algorithm for 3D 2-L/D CAP in both of down and up transmission links. Figure 4.12 and Figure 4.13 show the comparison between with and without channel estimation DSP algorithm for 4D 2-L/D CAP in both of down and up transmission links. In short, BER performances are improved approximate 0.5 dB by using channel estimation DSP algorithm after 20 km SSMF transmission in both case of 3D and 4D 2-L/D CAP.

Figure 4.14 presents BER performance of 3D CAP with 2-L/D modulation for back to back and 20 km SMF transmission. Figure 4.15 shows BER performance of 4D CAP with 2-L/D modulation for back to back and 20 km SMF transmission. Such BER performances in terms of received optical power are all obtained by using DSP algorithm of blind CMA equalizer.

In Figure 4.16 and Figure 4.17, BER performances of 3D and 4D CAP with $\scriptstyle 4 - \mathrm { L } / \mathrm { D }$ modulation for back to back and 20 km SSMF transmission are presented.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/6b5079076414f24af0df21ce28434938c203032825fdd3191ab584a0298de504.jpg)  
Figure 4.10: Comparison between with and without channel estimation for 3D $\scriptstyle 2 \mathrm { - L } / \mathrm { D }$ CAP bi-directional transmission down link.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/9e154d289fe3cb283f82db316cd0dec84c96fdfadab8b49caf8f39ee287988fe.jpg)  
Figure 4.11: Comparison between with and without channel estimation for 3D $\scriptstyle 2 \mathrm { - L } / \mathrm { D }$ CAP bi-directional transmission up link.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/a365ff0c4949984b4bc0fc5cfbd66bfa3bd13150815ca732827fce688a8fb0b1.jpg)  
Figure 4.12: Comparison between with and without channel estimation for 4D 2-L/D CAP bi-directional transmission down link.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/31470fd5c7e327544ca275e6351f1084195ca8c4dbc533a8a2ad9925b608d4ec.jpg)  
Figure 4.13: Comparison between with and without channel estimation for 4D 2-L/D CAP bi-directional transmission up link.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/6c54e53c3e3a4f4fe99c6a990466bde024db27c030e3db366fa4af64f979449c.jpg)  
Figure 4.14: BER vs received optical power of 3D 2-L/D CAP bi-directional transmission.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/84e459aa34f815c694278d7327835d90d6c53787bffeb56cc43fea2591636176.jpg)  
Received Optical Power (dBm)  
Figure 4.15: BER vs received optical power of 4D 2-L/D CAP bi-directional transmission.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/8dfd94cfc4c649c3057b696f2485c25f5758f645561d7efc53402e24ce329077.jpg)  
Figure 4.16: BER vs received optical power of 3D 4-L/D CAP bi-directional transmission.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/aa83a2df7da90c1e5733be8032f8b15bf57b06e64333bec88bc4e8347e57d775.jpg)  
Figure 4.17: BER vs received optical power of 4D 4-L/D CAP bi-directional transmission.

## 4.4 Summary

In Chapter 4, the generation and transmission of multi dimensional CAP modulation for optical communication systems have been demonstrated. Moreover off-line DSP algorithms of blind CMA equalizer compensating for multi dimensional CAP modulation transmission impairments are under investigation.

A bi-directional optical transmission using 3D/4D CAP with $\scriptstyle 2 \mathrm { - L } / \mathrm { D }$ and $\scriptstyle 4 - \mathrm { L } / \mathrm { D }$ modulation is demonstrated. In order to achieve metro-access reach, blind coordinate transformed CMA equalizer is implemented. This experiment demonstrated system provides potentially a cost effective solution for next generation access networks. The spectral efficiency for 2- level/dimension are 2,25 bits/s/Hz and 1 bits/s/Hz for 3D-CAP and 4D-CAP, 4-level/dimension are 3.6 bits/s/Hz and 1.325 bits/s/Hz for 3D-CAP and 4D-CAP are presented in this work. To the best of author’s knowledge this is the first demonstration of a bi-directional optical link using multi dimensional CAP and employing DM-VCSELs.

Chapter 5

# Ultra Dense WDM Systems with Coherent Detection

## 5.1 Introduction

Recent research experiments have demonstrated dense wavelength division multiplexing (DWDM) systems with advanced modulation formats, such as quadrature phase shift keying (QPSK) and orthogonal frequency division multiplexing (OFDM), achieving capacity of 1 Tb/s mainly for long haul application [80–82]. A dual polarization (DP) QPSK DWDM system with 10 sub-channels, employing 10 continuous-wave (CW) lasers achieving 3.0 b/s/Hz of SE has been demonstrated [80]. An optical OFDM WDM experiment based on single sideband modulation achieved 3.3 b/s/Hz of SE [81]. To best of our knowledge, the closest sub-channel spacing for conventional (non-OFDM) DWDM system achieved 1.1 times of baud rate with 3.6 b/s/Hz of SE [82].

In chapter 5, an alternative schematic known as ultra dense WDM with a flexible channel spacing less than 25GHz will be proposed. It may allow for the evolutionary path from conventional infrastructures towards more scalable and spectrally efficient networks. This trend is supported by the increased demand for more capacity, flexibility, upgrading of transmission technique while keeping some legacy ones, in particular in the metro-access segments of the optical network [83, 84]. Scenario of optical WDM system with fixed channel spacing is shown in Figure 5.1. However, to cope with the required bandwidth efficiency, future ultra dense WDM scheme will need to use extremely close channel spacing that implies taking measures to mitigate the resultant detrimental effects from crosstalk and neighboring channels interferences. Scenario of ultra dense WDM with flexible channel spacing system is shown in Figure 5.2.

Chapter 5 is divided into three sections. After introductory section, theoretical concept and analysis of ultra dense WDM systems will be presented. Furthermore, a ultra dense WDM optical communication coherent system using DSP decision feedback equalizer algorithm is experimentally demonstrated.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/bae2875b37c2004a206ad787d33a7ca19031c1faa182b9663c13b99ffb1453ca.jpg)  
Figure 5.1: Scenario of optical WDM system with fixed channel spacing

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/35f0d439cf98811a69518d91b06295695da24b9baf7c88610e88eef777fe04f5.jpg)  
Figure 5.2: Scenario of optical WDM system with flexible channel spacing

## 5.2 Generation of Ultra Dense WDM Channels

The conventional dense WDM systems use individual lasers to generate sub-channels with different central wavelength. The polarization multiplexing (PM) QPSK WDM system experiments demonstrate 10 sub-channels WDM with SE 3.0 b/s/Hz required 10 continue-wavelength (CW) lasers [80]. For ultra dense WDM systems generation, coherent OFDM (CO-OFDM) is under consideration as a feasible implementation [85]. The subcarriers in CO-OFDM system are spaced exactly at the baud rate and each carriers is phase-locked and also symbol transition-aligned to all other [86]. This approach is less sensitive to phase noise, since OFDM is applied inter carriers rather than intra carriers and the resulting symbol rate is large. An alternative approach is known as frequency domain comb generation.

The schematic of optical ultra dense WDM system generation using comb generator is depicted in Figure 5.3. The basic idea of frequency domain comb generation is to serially combine the duplicated signal carriers in frequency domain. Moreover channel spacing $\Delta \lambda$ can be controlled by using external electrical synthesizer. The common comb generation approach is known as single side band modulation using single Mach-Zehnder modulator (MZM). After comb generation, signal carriers with different carrier frequencies $[ \lambda _ { 0 } , \lambda _ { 1 } , \cdots , \lambda _ { n } ]$ are split into individual optical modulators. This ultra dense WDM structure is suitable for point-to-multipoint PONs to increase amount of users serviceable from a single central office. As it has been discussed previously, cognitive coherent detection is recommended. Experimental demonstration will be presented in section 5.3.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/d9ce1f085da7701d1940808f16bd4786933be52bb970caf3dab755b0c9b00f4f.jpg)  
Figure 5.3: Schematic of optical ultra WDM system generation

## 5.3 1.2 Tb/s Ultra Dense WDM System

In section 5.3, an experimental implementation is presented concerning a long reach ultra dense WDM system based on a single distributed feed back (DFB) laser to generate 30 sub-channels with DP-QPSK modulation. In this demonstration, sub-channel spacing is equal to the baud-rate, achieving 4.0 b/s/Hz of SE and 1.2 Tb/s of aggregate capacity over 80 km SMF for metro-access networking. To avoid the employment of arrayed waveguide grating, a coherent receiver with local oscillator (LO) laser is used to select the sub-channels. The off-line DSP algorithms are developed to compensate for optical transmission impairments including chromatic dispersion.

## 5.3.1 Ultra Dense WDM System Experiment Setup

The ultra dense WDM structure is realized using recirculated single side band modulation (SSB). Figure 5.4 shows the schematic of the experimental setup. A single DFB laser operating at 1549.53 nm (193.47 THz) with 10 MHz line-width is used as source to generate the sub-channels.

A Mach-Zehneder modulator operates as single side band modulator. An external synthesizer drives the single side band modulator to control the sub-channel generation loop, which is known as the comb generator. Comb generator shifts the first input channel by a frequency spacing determined by the external synthesizer clock output. In the experiment, frequency spacing is set equal to 10 GHz. As a result, each round generates one more sub-channel. A tunable optical band-pass filter with full width at half maximum (FWHM) of 5 nm (625 GHz) is used to control the bandwidth of the comb generator. After the comb generator, the sub-channels are separated into two orthogonal polarizations by a polarization beam splitter (PBS). The polarized sub-channels are then fed into two identical QPSK modulators. A non-return-zero (NRZ) pseudo random binary sequence (PRBS) with $2 ^ { 1 5 } - 1$ bit length provides the electrical data source. After the QPSK modulator, two uncorrelated branches of orthogonally polarized QPSK signals are combined by a polarization beam combiner (PBC) to generate the DP QPSK signals. Differently from [81] and [82], sub-channels are firstly generated and then modulate each polarization branch individually. This schematic provides the possibility of using a different modulation format for each polarization branch. Meanwhile, a polarization controller (PC) inside the comb generator is used to control polarization rotation during one round. If polarization maintaining fiber is used throughout the comb generator, the PC can be omitted.

A pre-amplified coherent receiver structure is then implemented. A tunable optical band-pass filter (0.5 nm/62.5 GHz FWHM) is used after the pre-amplifier in order to remove ASE noise from the EDFA. The local oscillator (LO) is a wavelength tunable external cavity laser (ECL) with 100 kHz line-width. In the coherent receiver structure, tuning LO wavelength enables channel selection due to optical heterodyning at the photodiode. The coherent receiver consists of two 90◦-hybrids and balanced detectors. 40 Gb/s digital sampling oscilloscope at the coherent receiver is used to sample the in-phase and quadrature components.

In this experiment, off-line DSP algorithms are employed to compensate for chromatic dispersion (CD), instead of using dispersion compensation fiber (DCF) after 80 km single mode fiber (SMF) transmission. A constant modulus algorithm (CMA) enables polarization rotation compensation; DSP algorithms implement frequency and phase off set removal, QPSK demodulation and bit error detection. Since the sub-channels are spaced at a frequency corresponding to the baud rate, crosstalk and overlap from sub-channels severely affects the BER performance. Therefore, DSP algorithm is required to reduce the detrimental effect of inter channel interference (ICI). Such nonlinear decision feedback equalizer (DFE) consisting of a feed forward filter (FFE) and a feedback filter (FBE) is then used to improve the system performances. The taps of the two equalizers are adjusted using a least mean square (LMS) stochastic algorithm.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/11b6c239ca04254a57090b3703bb6f7f041da9e5d149e166f9575bad5ba42fa8.jpg)  
Figure 5.4: Figure 1. Experiment setup: OBPF, optical band-pass filter; PC, polarization controller; ECL, external cavity laser; PBS, polarization beam splitter; PBC, polarization beam combiner; OSNR, optical SNR monitor.

## 5.3.2 Experiment Results and Analysis

The sub-channels signal spectra are presented below. Figure 5.5 shows the signal spectrum after sub-channel generation and Figure 5.6 shows the signal spectrum after modulation and transmission.

To avoid performance degradation, selected sub-channels with tone to noise ratio (TNR) are more than 15 dB. The TNR differences between different sub-channels are induced by the loop accumulated ASE noise from EDFA. From Figure 5.6, the generation of more than 30 sub-channels can be verified in 5 nm (625 GHz) bandwidth from 1545.10 nm to 1550.10 nm; even more sub-channels can be generated with a low noise EDFA to further improve system transmission bit rate. For 15 dB TNR and above, the subchannels are successfully detected with bit error rate (BER) below the 7% overhead FEC threshold as shown in the Figure 5.7.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/5bedaf310c2822dbaca6e1eb1cfd2488a2f76fc01036c3d8e03ef95a41fc45c0.jpg)  
Figure 5.5: Ultra dense WDM signal spectrum for 30 sub-channels after comb generator.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/ba1c67cd7c65e20c0183b05c4be52a9d3bc8f46a9833bcf186e15ebc91d2442f.jpg)  
Figure 5.6: Ultra dense WDM signal spectrum for 30 sub-channels after transmission.

The BER performances of the ultra dense WDM system with back to back and 80 km SMF transmission using DSP dispersion compensation algorithms are shown as following. Figure 5.7 shows the BER performance for back to back of 30 sub-channels. As a result, the BER performances for all of 30 sub-channels are below the 7% overhead FEC threshold. Variations observed in BER performance across sub-channels are due to differences in the TNR of the different sub-channels.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/e44e1432273e5d66fc2d3063ded51eb5badf7be98127e6985f0a28bf643e81b9.jpg)  
Figure 5.7: Ultra dense WDM signal back to back BER performance for 30 subchannels.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/5e165a26c7ceaff31df5b6a32cbe166266c46fa95bfaf0eabcd654825bcac1af.jpg)  
Figure 5.8: Ultra dense WDM $1 0 ^ { t h }$ sub-channels BER performance with back to back and 80 km SMF transmission compared with the BER performance of single channel 40 $\mathrm { G b } / \mathrm { s }$ DP-QPSK system, and ultradense WDM $1 0 ^ { t h }$ sub-channels transmission BER performance with DFE.

Figure 5.8 shows the BER performance for $1 0 ^ { t h }$ sub-channel back to back and 80 km SMF transmission with DSP compensation algorithms. One sub-channel $( 1 0 ^ { t h }$ sub-channel) is selected from the ultra dense WDM signals and measure the ICI penalty. For reference, the single channel 40 Gb/s DP-QPSK back to back and 80 km SMF transmission BER performance is presented. Figure 5.8 indicates that after 80 km SMF transmission, DSP compensation algorithms are able to compensate for CD. The BER performance of back to back and 80 km transmission measurement penalty is lower than 0.5 dB. Figure 5.8 also shows the $1 0 ^ { t h }$ sub-channel BER performance comparison between scenarios with and without DFE after 80km SMF transmission.

Since the ultra dense WDM sub-channels are spaced exactly at the baud rate. Therefore, conventional WDM demultiplexing using optical bandpass filter or AWG can not filter out the in band overlapping. The DFE algorithm is implemented to reduce ICI. As a result, from Figure 5.8, DFE algorithm improves the BER performance by about 2.7 dB.

## 5.3.3 Decision Feedback Equalizer

As the channel distortion or the ICI of ultra dense WDM transmission system is too severe for a linear equalizer to mitigate the channel impairments, non-linear equalizer has been used. A DFE is a non-linear structure that uses previous detector decision to eliminate the ISI on pulses currently demodulated.

The basic idea is that if the values of the symbols previously detected are known, then ISI contributed by these symbols can be canceled out exactly at the output of the forward filter (FFE) by subtracting previous symbol values with appropriate weighting factor. The DFE equalizer will not amplify the noise, cause according to its structure, the equalization process is done through the feedback, noiseless, data applying symbol-bysymbol detection with successive cancelation of the interference caused by the detected symbols.

A nonlinear DFE, shown in Figure 5.9, consisting of a feed-forward filter (FFE) and a feed-back filter (FBE) is used in coherent receiver, after the carrier phase recovery block, to improve the system performances [87]. The taps of the two equalizers are adjusted using a least mean square (LMS) stochastic algorithm.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/8101061957ef5e249e2129b272285ad9ff3d43ded055c8342be0a83c03f1e66a.jpg)  
Figure 5.9: Schematic of DFE DSP algorithm.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/03a1849d30dfed98307327fcd7a5161959468a519c15b1a47385b94d08451107.jpg)  
Figure 5.10: BER performance comparison between with and without DFE DSP algorithm.

Figure 5.10 shows the BER performance comparison between with and without DFE DSP algorithm for ultra dense WDM system after 80 km

SMF transmission. As a result, approximate 2.7 dB BER improvement can be obtained by using DFE algorithms to compensate for inter channel interference induced by ultra narrow channel spacing.

## 5.4 Summary

In chapter 5, by using single side band modulation method, transmit ultra DWDM 30×40 Gb/s DP-QPSK signals at 1.2 Tb/s bit rate with back to back and 80 km SMF has been experimentally demonstrated. The ultra dense WDM sub-channels spaced at exactly the baud rate. As a result, SE 4.0 b/s/Hz is achieved. The off-line DSP algorithms are implemented to compensate CD, PMD and ICI after 80 km SMF transmission. This ultra dense WDM system indicates higher SE, higher speed than conventional WDM system with all commercial available low cost equipments. Further increasing number of sub-channels with low noise EDFA can be achieved to increase the entire systems transmission bit rate.

## Chapter 6

## Conclusion and Outlook

The modern generation of optical communication networks are required to fulfill a set of different technical requirements, such as high capacity, better spectral efficiency and system flexibility. In that sense, optical transmission systems using digital signal processing (DSP) algorithms are under consideration as the promising solutions. In this thesis, various DSP algorithms have been studied to compensate for fiber transmission impairments in different optical transmission systems. Instead of using costly physical dispersion compensation technique, off-line DSP compensation algorithms are low-cost and feasible to implement. Moreover, in this thesis, coherent detection technique is also under investigation. There are different reasons why the utilization of coherent detection can be very beneficial, such as improved optical transmission sensitivity, high spectrum efficiency, and cost efficiency of transmission dispersion compensation. In general, several experimental demonstrations of optical communication systems associated with DSP algorithms have been presented in this thesis.

<table><tr><td>System type.</td><td>Capacity</td><td>Main achievements</td></tr><tr><td>Coherent DP-QPSK</td><td>20 Gb/s</td><td>less complexity requirement</td></tr><tr><td>Coherent pilot-aided</td><td>40 Gb/s</td><td>300 MHz line-width tolerance</td></tr><tr><td>Coherent DP-QPSK</td><td>112 Gb/s</td><td>71 % bandwidth narrowing toleracne</td></tr><tr><td>Coherent DP-QPSK</td><td>1.2 Tb/s</td><td>ultra dense WDM, 4.0 bit/s/Hz SE</td></tr><tr><td>CAP</td><td>7.2 Gb/s</td><td>3D/4D CAP supporting multi-users</td></tr></table>

Table 6.1: Mean novel experiment achievements for different fiber transmission systems over standard single mode fiber.

## Conclusion

Main achievements are briefly concluded in the Table 6.1. As it can be noticed, coherent dual polarization quadrature phase shift keying (coherent DP-QPSK) systems using various DSP algorithms are presented. Overall, block-overlap chromatic dispersion compensation algorithm has been proposed to fulfil less complexity requirement. A pilot-tone aided phase noise cancelation algorithm is used to improve laser line-width tolerance of 40 Gb/s DP-QPSK system from 10 MHz per laser to 300 MHz. Adaptive channel estimation algorithm is employed to compensate for 71% spectrum narrowing effect. Decision feed back equalizer is implemented to generate 1.2 Tb/s ultra dense WDM DP-QPSK system.

All of proposed DSP algorithms are used to compensate for transmission impairments to guarantee an acceptable system performance in case of propagation with deployed fiber channels for optical metro access networks. In this thesis, various transmission impairments are under investigation, such as chromatic dispersion, polarization mode dispersion and phase/frequency transmission offset. Basic concept analysis of conventional DSP compensation algorithms are also demonstrated in this thesis, including frequency domain all pass CD compensation, Gardner clock recovery algorithm, butterfly FIR equalizer polarization demultiplexing and Viterbi-Viterbi carrier recovery algorithm.

Moreover, multi dimension multi level carrierless amplitude/phase (CAP) transmission systems with blind channel estimation DSP algorithm has been proposed to fulfil additional challenge of supporting various services with different users in optical communication networks. In principle, the purpose of using DSP channel estimation algorithms is to compensate inter symbol interference induced by multi modulation levels cross talk effect in CAP transmission systems. As a result, in this thesis, 3D/4D with 2-level/dimension and 4-level/dimension CAP transmission systems using blind CMA equalizer channel estimation has been presented.

## Outlook

As it has been already discussed in this thesis, next generation of optical communication systems require high capacity, better spectrum efficiency and more system flexibilities. According to the enormous increasing of data rate demand of the optical fiber transmission systems, implementation of optical coherent detection associated with digital signal processing technique is a recommended in this thesis.

Nowadays, capacity demand of optical communication systems is evolving from 40 Gb/s, 100 Gb/s towards 400 Gb/s. In that sense, more advanced optical modulation formats are required. In the near future, fiber transmission systems using 16 QAM, 64 QAM, and even more advanced modulation formats associated with novel DSP compensation algorithms will become feasible. For instance, increasing the data rate to 400 Gb/s is prospected to be achieved by different techniques. First approach is taking advantage of digital sampling speed fast developing that increase DP-QPSK signal baud rate from 28 Gbaud to 80 Gbaud [88]. Another method is using CO-OFDM signal with 16-QAM subcarrier modulation through orthogonal band multiplexing [89].

For the next generation of optical transmission systems, in order to extend communication system reach, compensation algorithms for non-linear transmission impairments have to be considered. For instance, a pilot-tone aided nonlinearity compensation technique will be considered more favorably in future optical transmission systems [8]. Moreover in order to further increase the aggregate data rate carried on transmission fiber, spacing division multiplexing technique can play a important role. However that is a still open research topic of optical communication systems.

# Paper 1: Engineering Rules for Chromatic Dispersion Compensation in Digital Receivers for Optical Coherent PolMux QPSK Links

Xu Zhang, Darko Zibar, Idelfonso Tafur Monroy and Richard Younce. “Engineering Rules for Chromatic Dispersion Compensation in Digital Receivers for Optical Coherent PolMux QPSK Links”, IEEE Photonics Society, 2010 23rd Annual Meeting of the, Nov 2010.

# Engineering Rules for Chromatic Dispersion Compensation in Digital Receivers for Optical Coherent PolMux QPSK Links

Xu Zhang, Darko Zibar and Idelfonso Tafur Monroy DTU, Department of Photonics Engineering, Ørsteds Plads, DK 2800, Kgs. Lyngby, Denmark.

Abstract—We consider block overlap chromatic dispersion compensation in optical coherent polarization multiplex quadrature phase shift keying links. We validate engineering rules for block length to compensate different values of chromatic dispersion by simulation and experiment.

## I. INTRODUCTION

Digital receivers for Polarization Multiplex (PoLMux) Quadrature Phase Shift Keying (QPSK) optical coherent link comprise stages of digital signal processing algorithms to compensate for Chromatic Dispersion (CD), Polarization Mode Dispersion (PMD) among other optical signal fibre transmission impairments. Those algorithms commonly require performing operations such as Fast Fourier Transform (FFT) over a given block length of data samples. The chosen length of such block determines both the complexity of implementing those operations and the accuracy they can achieve in compensating for signal impairments. We deal with the case of chromatic dispersion compensation employing Block Overlap (BO) algorithm for PolMux QPSK links. The BO approach for CD compensation was first proposed by Riichi Kudo et al., [1]. With the purpose of achieving the lowest possible complexity, we draw new engineering rules for BO CD compensation to determine the required block length sufficient to achieve a given level of compensation.

## II. COHERENT POLMUX QPSK LINK

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/889a455973d9ea08fb352fa22e8f7e1463122ef33118a02bceeccfb14375d30b.jpg)  
Fig. 1. Coherent PolMux QPSK system link. (a) PolMux QPSK transmitter. (b) coherent receiver optical front end. (c) off-line DSP algorithms blocks. (d) PMD compensation butterfly structure.

Richard Younce

Tellabs,

1415 West Diehl, Road Naperville, IL 60563 USA.

The schematic diagram of the coherent PolMux QPSK link is shown as Fig.1. In the transmitter, two QPSK signals are modulated into two orthogonal polarizations. In the coherent receiver front end, each individual orthogonal polarization is mixed with optical local oscillator in a 90◦ optical hybrid. The resultant in-phase and quadraure electrical signals are fed into an Analog to Digital Converter (ADC). The digitized samples are used for off-line demodulation and digital signal processing algorithms such as CD compensation, PMD compensation, Frequency & Carrier recovery, and error counting.

## III. BLOCK OVERLAP CD COMPENSATION ALGORITHM

A conventional DSP algorithm for serial, frequency domain, CD compensation requires that the FFT operation is applied to entire data sample set [2]. As the length of the samples increases, FFT operation requires more computation capacity. The complexity of implementing real time systems depends on the number of complex multiplications [3]. In the case of radix-2 FFT, the number of complex multiplications required may be expressed by 1 log2(L), where L is the length of FFT. The Block Overlap (BO) CD compensation algorithm applies Frequency Domain Equalization (FED) to blocks of samples instead of the entire data sample set. The output signal of the ADC stage (Fig.1) are data samples, that are divided into blocks (Fig.2a) with fixed length N $( N < L )$ For illustration purposes (Fig.2), we consider the case when the length of the overlapped part is half of the block length. In this halfoverlap case, half of the block is composed of the current samples (Fig.2b), and the rest is composed of equally length, N , data samples from the left and right neighboring blocks. Although the FFT processing complexity is reduced to that of a single block, instead of the entire data sample set, Inter Block Interference (IBI) may affect the performance. To combat IBI, the result of the FFT due to the overlapped samples (Fig.2b and Fig.2c) is discarded. $N _ { 1 }$ denotes the length of the discarded FFT output samples. Although a large discard length can reduce significantly IBI, it comes again at the expenses of complexity. However, it is possible to implement a BO algorithm with specific engineering rules for the block and discard length that can reduce IBI and achieve a targeted compensation level for a given CD value. In this paper, to compensate for CD, a Frequency Domain Equalization (FED)

algorithm is implemented (Fig.2d), based on a frequency allpass filter. The frequency response for an all-pass filter to compensate fibre CD can be expressed as,

$$
G ( z , \omega ) = \exp ( - j D \frac { \lambda ^ { 2 } } { 2 \pi c } \frac { \omega ^ { 2 } } { 2 } z + j S ( \frac { \lambda ^ { 2 } } { 2 \pi c } ) ^ { 2 } \frac { \omega ^ { 3 } } { 6 } z )\tag{1}
$$

Where D is the dispersion coefficient, S is the dispersion slop, $\omega$ is the angular frequency, λ is the light wavelength, c is the light velocity, and z is the fibre length. After frequency domain CD compensation, IFFT inverts the sequence back to the time domain (Fig.2e).

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/891f838e350a60bd9cc87d560f1c33c3cd40e667ff1827a3944142ecd2812e73.jpg)  
Fig. 2. BO CD compensation algorithm half-overlap.

## IV. ENGINEERING RULES FOR BO CD COMPENSATION

We define α as the ratio of discarded samples length to block length, where α and $\beta$ are coprime integers, $\begin{array} { r } { \frac { \alpha } { \beta } \in [ \frac { 1 } { 2 } , 1 ) . } \end{array}$ In the case of half-overlap, the number of blocks is equal to $2 [ L / N ] - 1 ,$ where square bracket is the ceil integer function. A single block FFT only needs $\scriptstyle { \frac { 1 } { 2 } } l o g _ { 2 } ( N )$ complex multiplications compared to $\scriptstyle { \frac { 1 } { 2 } } l o g _ { 2 } ( L )$ required for serial compensation $( N < < L )$ To avoid IBI, the value of the discarded data length $N _ { 1 }$ is defined by the following engineering rule as,

$$
N _ { 1 } = D z { \frac { \Gamma \lambda ^ { 2 } } { c } } R _ { s }\tag{2}
$$

Where Γ is the full-wave-half-maximum spectrum bandwidth of the signal, and Rs is sample rate. In our computer simulation, $\scriptstyle { R _ { s } }$ is set to 56 GSa/s. The operating wavelength is 1550 nm. The dispersion slop parameter S is set as 0. Nyquist criterion specifies Γ to be 56 GHz. If CD is 16000 ps/nm, then $N _ { 1 } = 4 4 8 .$ In order to fulfil the radix-2 FFT requirement, $N _ { 1 }$ is set to $2 ^ { 9 }$ (512), which means the block length is $2 ^ { 1 1 }$ (2048), and that $2 ^ { 1 0 }$ (1024) samples are discarded (Fig.3a). From Fig.3, our simulation results show that, a given value of chromatic dispersion requires specific block length to approach the back to back transmission bit error rate performance. Engineering rule defines the number of complex multiplication required for one block and for entire data sample set as,

$$
\left\{ \begin{array} { l l } { \frac { 1 } { 2 } l o g _ { 2 } ( \frac { 2 \beta } { \alpha } N _ { 1 } ) } & { \mathrm { o n e ~ b l o c k } } \\ { \frac { 1 } { 2 } l o g _ { 2 } \{ \beta ( L - 2 N _ { 1 } ) \} } & { \mathrm { e n t i r e ~ d a t a ~ s a m p l e ~ s e t } } \end{array} \right.\tag{3}
$$

From (3), when $\scriptstyle { \frac { a } { B } }$ is equal to ${ \scriptstyle { \frac { 1 } { 2 } } } .$ the complexity required for one block achieves the minimum value, as a result it is also for the entire data sample. Therefore, half-overlap BO CD compensation is the least complex scheme to implement.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/e6057598e230ad693808624dd7269ce1cd089d8473c37b9c9ca51579bdb6c6c4.jpg)  
(a)

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/8095dabef43054b4f14cd3e6fedd569b158a2353c4a0fac334aeaa9fe43ed82a.jpg)  
(b)  
Fig. 3. BO CD BER performance: (a) BER vs. OSNR with 16000 ps/nm CD; and, (b) block length requirements in BO CD at 14dB OSNR.

## V. 20 GB/S QPSK EXPERIMENT WITH BO CD

We experimentally validate the engineering rules for a 20 Gbs/s QPSK link, with 40 km single mode fibre transmission operating at 1550 nm. The value of the laser linewidth is 2 MHz. At the receiver side, noise loading is used to emulate different values for optical signal to noise ratio (OSNR). The 200 kHz linewidth ECL laser is used as local oscillator. Fig.4 shows the results for the Bit Error Rate (BER), with and without BO CD compensation being implemented. We can observe that BO CD compensation algorithm reduces the CD induced BER penalty by 3dB. There is still a nearly 1.2 dB penalty remaining from other impairments not compensated for in our set-up. Moreover, our BO CD algorithm achieves the same BER performance as the serial all-pass frequency domain CD compensation algorithm.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/daef3093e204fcdad4f7e69bc141d1ea9ba31bc71dd37a8a211fe29cb3590ee9.jpg)  
Fig. 4. 20 Gb/s coherent QPSK link 40 km transmission BER vs. OSNR.

## VI. CONCLUSION

Block Overlap Chromatic Dispersion (BO CD) compensation in optical coherent PolMux QPSK 112 Gb/s link is proven by computer simulation and experimentally validated for a 20 Gb/s QPSK 40 km transmission experiment. The experimental results validate our derived engineering rule for BO CD compensation. The BO CD compensation algorithm reduces the computational complexity of a serial frequency all-pass filter approach substantially, to that of a single block.

## REFERENCES

[1] R. Kudo et al, IEEE JLT, Vol.27, No.16 (2009) pp 3721-3728.

[3] J. Leibrich et al, OFC 2010, OWV1.

[2] M. Alfiad et al, IEEE JLT, Vol.27, No.16 (2009) pp 3590-3598.

# Paper 2: 1.2 Tb/s ultredense WDM long reach and spectral efficiency access link with digital detection

Xu Zhang, Valeria Arlunno, Jesper B. Jensen, Idelfonso Tafur Monroy, Darko Zibar and Richard Younce. “1.2 Tb/s ultradense WDM long reach and spectral efficiency access link with digital detection”, Photonics Conference (PHO), 2011 IEEE, Nov 2011.

# 1.2 Tb/s Ultredense WDM Long Reach and Spectral Efficiency Access Link with Digital Detection

Xu Zhang(1), Valeria Arlunno(1), J. Bevensee Jensen(1), I. Tafur Monroy(1), Darko Zibar(1), Richard Younce(2)

(1) Department of Photonic Engineering, Technical University of Denmark, Ørsteds Plads DK2800, Kgs, Lyngby, Denmark (2) Tellabs, 1415 West Diehl Road, Naperville, IL 60563 USA.

xuzhn@fotonik.dtu.dk

Abstract— We experimentally demonstrate an ultradense WDM system with sub-channel spacing at the baud rate, achieving 4.0 b/s/Hz spectral efficiency and aggregate capacity of 1.2 Tb/s data transmission over 80-km SMF, for long reach access networking.

## I. INTRODUCTION

With the rapid growth of capacity requirements of optical transmission networks, there is a strong need to realize high bit rate and highly spectral efficient (SE) optical transmission technologies. Next-generation optical access networks will therefore consider supporting aggregate capacities beyond 40 Gb/s and in the longer term capacities approaching 1 Tb/s. The challenges for Tb/s access networks are related to efficient spectral usage, to benefit from well-established and mature components and technologies at the C and L bands; and to reduce complexity, particularly at the end-user side; and where possible in the whole system. Therefore, since digital coherent transmission technology is becoming preferable for next generation optical transport links, it is interesting to evaluate its performance and feasibility and derive requirements for its application in long reach metro-access links. Recent research experiments have demonstrated dense wavelength division multiplexing (DWDM) systems with advanced modulation formats, such as quadrature phase shift keying (QPSK) and orthogonal frequency division multiplexing (OFDM), achieving capacity of 1 Tb/s mainly for long haul application [1-3]. A dual polarization (DP) QPSK DWDM system with 10 sub-channels, employing 10 continuous-wave (CW) lasers achieving 3.0 b/s/Hz of SE has been demonstrated [1]. An optical OFDM WDM experiment based on single sideband modulation achieved 3.3 b/s/Hz of SE [2]. To best of our knowledge, the closest sub-channel spacing for conventional (non-OFDM) DWDM system achieved 1.1 times of baud rate with 3.6 b/s/Hz of SE [3].

In this paper, we report on an experimental implementation of a long reach ultradense WDM system based on a single distributed feed back (DFB) laser to generate 30 sub-channels with DP QPSK modulation. The sub-channel spacing is equal to the baud-rate, achieving 4.0 b/s/Hz of SE and 1.2 Tb/s of aggregate capacity over 80 km SMF for metro-access networking. To avoid the employment of arrayed waveguide grating, a coherent receiver with local oscillator (LO) laser is used to select the sub-channel. We have developed digital signal processing (DSP) algorithms to compensate for optical transmission impairments including chromatic dispersion (CD).

A decision feed back equalizer (DFE) algorithm has also been implemented in the DSP to mitigate the effects of inter-channel interference (ICI) in the ultradense WDM system. The employment of non-linear DFE equalizer guarantees system bit error rate (BER) back to back performance below the FEC threshold for all 30 sub-channels.

## II. EXPERIMENT SETUP

The ultradense WDM structure is realized using recirculated single side band modulation (SSB) [3]. Figure 1 shows the schematic of our experimental setup. A single DFB laser operating at 1549.53 nm (193.47 THz) with 10 MHz linewidth is used source to generate the sub-channels. A nested Mach-Zehneder modulator operates as single side band modulator. An external synthesizer drives the single side band modulator to control the sub-channel generation loop, which is also called the comb generator [3]. Comb generator shifts the first input channel by a frequency spacing determined by the external synthesizer clock output. In the experiment, frequency spacing is set equal to 10 GHz. As a result, each round generates one more sub-channel. A tunable optical band-pass filter with full width at half maximum (FWHM) of 5 nm (625 GHz) is used to control the bandwidth of the comb generator. After the comb generator, the sub-channels are separated into two orthogonal polarizations by a polarization beam splitter (PBS). The polarized sub-channels are then fed into two identical QPSK modulators. A non-return-zero (NRZ) pseudo random binary sequence (PRBS) with $2 ^ { 1 5 } – 1$ bit length provides the electrical data source. After the QPSK modulator, two uncorrelated branches of orthogonally polarized QPSK signals are combined by a polarization beam combiner (PBC) to generate the DP QPSK signals. Differently from [2] and [3], we first generate sub-channels and then QPSK modulate each polarization branch individually. This schematic provides the possibility of using a different modulation format for each polarization branch. Meanwhile, a polarization controller (PC) inside the comb generator is used to control polarization rotation during one round. If polarization maintaining fiber is used throughout the comb generator, the PC can be omitted. A pre-amplified receiver structure is then implemented. A tunable optical band-pass filter (0.5 nm/62.5 GHz FWHM) is used after the pre-amplifier in order to remove ASE noise from the EDFA. The local oscillator (LO) is a wavelength tunable external cavity laser (ECL) with 100 kHz line-width. In the coherent receiver structure, tuning LO wavelength enables channel selection due to optical heterodyning at the photodiode. The coherent receiver consists of two 90° hybrids and balanced detectors. 40 Gb/s digital sampling oscilloscope at the coherent receiver is used to sample the inphase and quadrature components. In our experiment, we employed DSP algorithms to compensate for chromatic dispersion (CD), instead of using dispersion compensation fiber (DCF) after 80 km single mode fiber (SMF) transmission. A constant modulus algorithm (CMA) enables polarization rotation compensation; DSP algorithms implement frequency and phase off set removal, QPSK demodulation and bit error detection. Since the sub-channels are spaced at a frequency corresponding to the baud rate, crosstalk and overlap from sub-channels severely affects the BER performance. Therefore we develop a DFE algorithm in DSP to reduce the detrimental effect of ICI.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/821542b2c7272989f29d01df06fbabb098ddb0d1f2b3c9a85e36797d0085580f.jpg)  
Figure 1. Experiment setup: OBPF, optical band-pass filter; PC, polarization controller; ECL, external cavity laser; PBS, polarization beam splitter; PBC, polarization beam combiner; OSNR, optical SNR monitor.

## III. RESULTS AND DISCUSSION

Figure 2 shows the sub-channels signal spectra, Figure 2 (a) shows the signal spectrum after sub-channel generation and Figure 2 (b) shows the signal spectrum after modulation and transmission. To avoid performance degradation, we select sub-channels with tone to noise ratio (TNR) more than 25 dB. The TNR differences between different sub-channels are induced by the loop accumulated ASE noise from EDFA [2]. From Figure 2, we can verify the generation of more than 30 sub-channels in 5 nm (625 GHz) bandwidth from 1545.10 nm to 1550.10 nm; we can generate even more sub-channels with a low noise EDFA to further improve system transmission bit rate. For 25 dB TNR and above, we successfully detect the subchannels with bit error rate (BER) below the 7% overhead FEC threshold as shown in the Figure 3.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/4076582147f2effdf9fd3deb41bf6a117998904e561a2cd68734997f44b0ba77.jpg)

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/eeb6272b38f8e74a5276fd3395cd756e54ffb07a497bfc433b565f5b01ffee54.jpg)  
Figure 2. Ultradense WDM signal spectrum for 30 sub-channels. (a) after Comb generator (b) after transmission.

Figure 3 shows the BER performance of the ultradense WDM system with back to back and 80 km SMF transmission using DSP dispersion compensation algorithms. Figure 3 (a) shows the BER performance for back to back of 30 sub-channels.

Figure 3 (a) shows the BER performance for all of 30 subchannels is below the 7% overhead FEC threshold. Variations observed in BER performance across sub-channels are due to differences in the TNR of the different sub-channels. Figure 3 (b) shows the BER performance for $1 0 ^ { \mathrm { t h } }$ sub-channel back to back and 80 km SMF transmission with DSP compensation algorithms. We select one sub-channel $( 1 0 ^ { 6 }$ sub-channel) from the ultradense WDM signal and measure the ICI penalty. For reference, we show the single channel 40 Gb/s DP QPSK back to back and 80 km SMF transmission BER performance. Figure 3 (b) indicates that after 80 km SMF transmission, DSP compensation algorithms are able to compensate for CD. The BER performance of back to back and 80 km transmission measurement penalty is lower than 0.5 dB. Figure 3 (b) shows the $1 0 ^ { \circ }$ sub-channel BER performance comparison between scenarios with and without DFE after 80km SMF transmission. Since the ultradense WDM sub-channels are spaced exactly at the baud rate, we implement the DFE algorithm to reduce ICI. As a result, from Figure 3 (b), DFE algorithm improves the BER performance by about 2.7 dB.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/0a7b613b3c2650d9cd72e27283049ae6fb0786bad8da6d40513c8316d96ae645.jpg)

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/ef5dda4cd3a0083b655e8fed54fa50ca052902258c8c84fe82c3a20f4949e3d3.jpg)  
Figure 3. Ultradense WDM signal BER performance for 30 sub-channels. (a) back to back BER performances for 30 sub-channels. (b) ultradense WDM 10th sub-channels BER performance with back to back and 80 km SMF transmission compared with the BER performance of single channel 40 Gb/s DP QPSK system, and ultradense WDM 10th sub-channels transmission BER performance with DFE.

## IV. CONCLUSION

We experimentally demonstrate a WDM 30×40 Gb/s DP QPSK achieving 1.2 Tb/s transmission over 80 km SMF for long reach metro-access networking on a bandwidth of 300 GHz. The ultradense WDM sub-channel spacing at exactly the baud rate achieves 4.0 b/s/Hz of SE; DSP algorithms compensate for CD and ICI effects. Our results show that ultradense WDM systems can be realized with higher SE and higher capacity than conventional WDM and are suitable for potential applications in metro-access networking.

## REFERENCES

[1] Chongjin Xie and etc, “Hybrid 224-Gb/s and 112-Gb/s DP-QPSK Transmission at 50-GHz Channel Spacing over 1200-km Dispersion-Managed LEAF Spans and 3 ROADMs” OFC 2011 PDPD2.

[2] Yiran Ma and etc, “1-Tb/s Single-Channel Coherent Optical OFDM Transmission With Orthogonal-Band Multiplexing and Subwavelength Bandwidth Access” JLT Vol.28, No.4, February 15, 2010.

[3] Giancarlo Gavioli and etc, “Ultra-Narrow-Spacing 10-Channel 1.12 Tb/s D-WDM Long-Haul Transmission Over Uncompensated SMF and NZDSF” IEEE PTL Vol. 22, No. 19, October 1, 2010.

# Paper 3: High Spectrum Narrowing Tolerant 112 Gb/s Dual Polarization QPSK Optical Communication Systems using Digital Adaptive Channel Estimation

Xu Zhang. and Xiaodan Pang. and Anton Dogadaev. and Idelfonso T. Monroy. and Darko Zibar. and Richard Younce. “High Spectrum Narrowing Tolerant 112 Gb/s Dual Polarization QPSK Optical Communication Systems using Digital Adaptive Channel Estimation”, in Proceedings of the Optical Fiber Communication Conference and Exposition and the National Fiber Optic Engineers Conference, OFC’2012, Los Angles, CA, USA., paper number JW2A.49, March 2012.

# High Spectrum Narrowing Tolerant 112 Gb/s Dual Polarization QPSK Optical Communication Systems using Digital Adaptive Channel Estimation

Xu Zhang(1), Xiaodan Pang(1), Anton Dogadaev(1), Idelfonso T. Monroy(1), Darko Zibar(1), Richard Younce(2) (1) Department of Photonic Engineering, Technical University of Denmark, Ørsteds Plads DK2800, Kgs, Lyngby, Denmark (2) Tellabs, 1415 West Diehl Road, Naperville, IL 60563 USA. xuzhn@fotonik.dtu.dk

Abstract: We experimentally demonstrate high spectrum narrowing tolerant 112-Gb/s QPSK polarization multiplex system based on digital adaptive channel estimation method. The proposed algorithm is able to detect severe spectrum-narrowed signal even with 20GHz 3dB bandwidth. OCIS codes: (060.1660 Coherent communications)

## 1. Introduction

With the rapid growth of capacity requirements of optical transmission networks, there is a strong need to realize high capacity and high spectral efficient (SE) optical communication systems. The ultra-dense wavelength diversity multiplexing (U-DWDM) technology based on advanced modulation format is a promising solution and is being intensively studied [1,2]. U-DWDM technology requires optical or electrical pre-filtering to fulfil Nyquist sampling criterion [3]. Meanwhile, to facilitate ease of optical networking, tolerance of spectrum narrowing is critical, as signal channel spacing is degraded after transmission through optical channel, especially when reconfigurable optical add/drop multiplexers (ROADMs) nodes are used in the network [4]. Spectrum narrowing severely induce inter symbol interference (ISI) between continual transmitted sequence. Therefore, ISI compensation is essential to improve U-DWDM system performance in terms of optical signal to noise ratio (OSNR). Conventional digital signal processing (DSP) algorithm using adaptive decision feed forward equalizer is an inefficient solution, since this finite impulse response (FIR) filter enhance noise during compensation of spectrum narrowing [5]. Although maximum-likelihood sequence estimation (MLSE) method has been successfully proved to mitigate ISI [6], the complexity of MLSE is exponentially increasing with the length of transmitted sequence. When the sequence length is large, optimal MLSE becomes unfeasible. Therefore, in order to achieve high spectrum narrowing tolerant optical communication system, we implement adaptive channel estimation DSP algorithms combined with decision feedback equalizer. As a result, we experimentally demonstrate the high spectrum narrowing tolerance of proposed algorithms for 112 Gb/s dual polarization (DP) quadrature phase shift keying (QPSK) transmission systems.

## 2. Experiment Setup

Figure 1(a) shows the experiment setup of 112 Gb/s DP QPSK optical communication system. A DFB laser operating at 1549.53 nm (193.47 THz) with 10 MHz line-width is used as optical signal source to generate the QPSK signal. The pulse pattern generator (PPG) working at 28 Gbaud/s is operated as electrical signal source with $2 ^ { 1 5 } – 1$ bit length to drive the optical QPSK modulator. After the QPSK modulator, optical channel is separated into two orthogonal polarizations by a polarization beam splitter (PBS). Afterward, two branches of orthogonally polarized optical channels are combined by a polarization beam combiner (PBC) to generate the 112 Gb/s DP QPSK signal. The Finisar® wave-shaper is then used as spectrum pre-filtering optical bandpass filter (OBPF). The OBPF is able to tune full width at half maximum (FWHM) of transmitted signal. FWHM is defined as 3dB bandwidth of transmitted signal. At the receiver side, a pre-amplified coherent receiver structure is implemented. A tunable optical band-pass filter (with 0.5 nm/ 62.5 GHz FWHM) is used after the pre-amplifier in order to remove ASE noise from the EDFA. The local oscillator (LO) is a wavelength tunable external cavity laser (ECL) with 100 kHz line-width. In the coherent receiver structure, tuning LO wavelength enables channel selection due to optical heterodyning at the photodiode. The coherent receiver consists of two 90° hybrids and balanced detectors. The 80 Gb/s digital sampling oscilloscope at the coherent receiver is used to sample the inphase and quadrature components. Figure 1(b) shows the back to back transmission bit error rate (BER) performance in terms of OSNR. In both results of simulation and experiment for back to back transmission, at 20 dB OSNR measurement point, BER performances are approaching zero, and at 16 dB OSNR measurement point, BER performances are around 10-3. In the experiment, we focused on these two OSNR measurement points (OSNR=16dB and OSNR=20dB) and use DSP algorithm to compensate ISI induced by spectrum narrowing effect. We also employed constant modulus algorithm (CMA) to enable polarization rotation compensation, frequency and phase off set removal, QPSK demodulation and bit error detection.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/7b0d7bcdd6bf8833da73afda41d77a9273021ea60eaaf0b7d7f3294fa4939984.jpg)  
Figure. 1. (a) Experiment setup. (b) back to back BER vs. OSNR performance.

## 3. DSP Algorithms and Experiment Results

The proposed DSP algorithm schematic is shown in Figure 2. The polarization multiplexed signals are firstly fed into coherent detection receiver. Afterward, the received signals are sampled by analog to digital convertor (ADC) to 2 samples per symbol. The output digitized signals are fed into a butterfly filter composed of four FIR filters. CMA algorithm is used to improve polarization demultiplex performance and compensate polarization rotation. The signals are sent to carrier recovery block to demultiplex inphase and quadrature components and then to the adaptive channel estimation block. The adaptive channel estimation requires estimation of noise level $\eta _ { k } \mathrm { ; }$ feed forward FIR tap coefficients $c _ { k }$ and feed back equalizer tap coefficients $p _ { k ^ { + } }$ For instance, in one orthogonal polarization, denoted as x-polarization, input of channel estimation is x(k). Since a finite length feed forward equalizer is unable to cancel noncausal ISI completely, the feed back filter coefficients should be optimized according to the MMSE criterion whereby the additive noise power resulting from residual ISI is minimized. The correct channel estimation of $c _ { k }$ and $p _ { k }$ is able to minimize minimum mean square error (MMSE) between received signals and decision signals [7], i.e. min $\{ E [ x ^ { * } ( k ) - \eta - x ^ { \sim } ( k ) ] ^ { 2 } \}$ , where $x ^ { \prime } ( k ) = c _ { k } x ( k )$ and $x ^ { \prime } ( k ) = x ^ { \prime } ( k ) - p _ { k } x ^ { \prime } ( k )$ and $x ^ { \sim } ( k )$ is the slicer output from x ’’(k). The stochastic adaptive algorithm to find $c _ { k } , \eta _ { k }$ and $p _ { k }$ can be implemented using the LMS algorithm [8].

We denote error factor as $e _ { k } = x ^ { * } ( k ) - \eta _ { k } - x ^ { * } ( k )$ . Then we have following update equations: $c _ { k + l } = c _ { k } + \mu e _ { k }$ x(k); $p _ { k + I } = p _ { k } - \gamma e _ { k } x ^ { - } ( k )$ and $\eta _ { k + I } = \left( 1 - \rho \right) \eta _ { k } + \rho e _ { k }$ Here, $\mu$ is the step size of feed forward FIR equalizer; J is the step size of feed back equalizer and $\rho$ is an integration factor (a small value used to average $e _ { k }$ over time k) [8]. As a result, symbol estimation $x _ { m } \widetilde { \alpha } \widetilde { \alpha } )$ is a estimation vector: {x(k-n), x(k-n-1), x(k-n-2)… x(k-1)}, where n is the length of feed back equalizer. Operation of subtracting $x _ { m } ^ { - } ( k )$ combined with proper channel estimation coefficients from received signals is used to cancel most of precursor ISI [9]. According to accuracy estimation requirement of noise level, length of feed back equalizer can not be insufficient. Compared to the complexity requirement of MLSE algorithm, our proposed adaptive channel estimation algorithms are practical.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/cbc9fb12896c687b4d3cf5ea4bc70782cfd8aaa8c071618be7dc63ffb64f78b7.jpg)  
Figure. 2 The proposed DSP Algorithm Schematic

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/ed5b6f0ec9e2bb0f6d618abe7f901405436107b8c48deecf9cc5c6e97572d642.jpg)

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/ad9c4171f0ae0f951c11d02ff3b1ccf1351e04a06a90d634cfd1711949c8883d.jpg)  
Figure. 3 BER penalty vs. bandwidth narrowing with and without adaptive channel estimation algorithm. (a) @ 16dB OSNR. (b) @ 20dB OSNR

Figure 3 shows experiment results. In our experiment, we focus on 20 dB OSNR and 16 dB OSNR measurement points. At 20 dB OSNR, in case of without spectrum narrowing effect, BER performance is error free. As the signal spectrum space degrading, BER penalty grow dramatically. Meanwhile, using adaptive channel estimation algorithm, strongly reduce the BER penalty. Especially at 20 GHz bandwidth (71% of original signal bandwidth), BER penalty is reduced 2 dB by using adaptive channel estimation algorithms. At 16 dB OSNR, in case of with out spectrum narrowing effect, BER performance is around 10-3. At 20 GHz bandwidth (71% of original signal bandwidth), BER penalty is also reduced 2 dB by using adaptive channel estimation algorithms.

## 4. Conclusion

By using our proposed adaptive channel estimation DSP algorithms, we successfully demonstrate high spectrum narrowing tolerant 112-Gb/s QPSK polarization multiplex optical communication systems. The experiment results show that in case of 71% spectrum narrowing, our proposed algorithms mitigate 2 dB BER penalties with both 16 dB OSNR and 20 dB OSNR cases. Compared to high computational complexity requirement of MLSE algorithm, our proposed adaptive channel estimation DSP algorithm is feasible and practical.

## 5. References

[1] Nakazawa, M., Okamoto, S., Omiya, T., Kasai, K., and Yoshida, M. “256-QAM (64Gb/s) coherent optical transmission over 160 km with an optical bandwith of 5.4 GHz” IEEE Photonic Technol. Lett., 2010, vol.22, no.3.

[2] Valeria Arlunno, Xu Zhang, Knud J.Larsen, Darko Zibar and Idelfonso Tafur Monroy “Digital Non-Linear Equalization for Flexible Capacity Ultradense WDM Channels for Metro Core Networking” ECOC 2011 Tu3.K6.

[3] T. Sugihara, T. Kobayashi, Y. Konishi, S. Hirano, K. Tsutsumi, K. Yamagishi, T. Ichikawa, S. Inoue, K. Kubo, Y. Takahashi, K. Goto, T. Fujimori, K. Uto, T. Yoshida, K. Sawada, S. Kametani, H. Bessho, T. Inoue, K. Koguchi, K. Shimizu, and T. Mizuochi, “43 Gb/s DQPSK Preequalization employing 6-bit, 43GS/s DAC Integrated LSI for Cascaded ROADM Filtering” OFC 2010 PDPB6.

[4] S. Gringeri, R. Egorov, B. Basch, and G. Wellbrock, “Real-Time 127-Gb/s Coherent PM-QPSK Transmission over 1000km NDSF with >10 Cascaded 50GHz ROADMs” ECOC 2010 P4.09.

[5] S. J. Savory “Digital filters for coherent optical receivers,” Opt. Express 16, 804-817 (2008).

[6] K. Horikoshi, E. Yamazaki, T. Kobayashi, E. Yoshida, and Y. Miyamoto, “Spectrum-narrowing tolerant signal-processing algorithm using maximum-likelihood sequence estimation for coherent optical detection” Electronics Letter 12th May 2011, vol.47, no.10.

[7] Tommaso Foggi, Giulio Colavolpe, Enrico Forestieri, and Giancarlo Prati, “Channel Estimation Algorithms for MLSD in Optical Communication Systems” IEEE Photonic Technol. Lett., October 2006, vol.18, no.19.

[8] Wonzoo Chung, “Channel Estimation Methods Based on Volterra Kernels for MLSD in Optical Communication Systems” IEEE Photonic Technol. Lett., February 2010, vol.22, no.4.

[9] Heinrich Meyr, Marc Moeneclaey, and Stefan A. Fechtel Digital Communication Receiver-synchronization, channel estimation, and signal processing JOHN WILEY & SONS, INC.

# Paper 4: Digital non-linear equalization for flexible capacity ultradense WDM channels for metro core networking

Valeria Arlunno, Xu Zhang, Knud J. Larsen, Darko Zibar, and Idelfonso Tafur Monroy. “Digital non-linear equalization for flexible capacity ultradense WDM channels for metro core networking”, in Proceedings of the 37th European Conference on Optical Communication, ECOC’2011, Geneva, Switzerland, September 2011.

# Digital Non-Linear Equalization for Flexible Capacity Ultradense WDM Channels for Metro Core Networking

Valeria Arlunno, Xu Zhang, Knud J. Larsen, Darko Zibar and Idelfonso Tafur Monroy DTU Fotonik, Department of Photonics Engineering, Technical University of Denmark, DK-2800 Kgs. Lygnby, Denmark. vaar@fotonik.dtu.dk

Abstract: We experimentally demonstrate that digital non-linear equalization allows for using independent tunable DFB lasers spaced at 12.5 GHz for ultradense WDM PM-QPSK flexible capacity channels for metro core networking.

OCIS codes: (060.1660) Coherent communications; (060.4510) Optical communications

## 1. Introduction

Rigid and coarse granularity of wavelength-division-multiplexing (WDM) systems leads to inefficient capacity utilization. In flexible optical WDM (FWDM), spectral resources are allocated in a flexible and dynamic way; channel spacing and center wavelength are not fixed on the ITU-T grid, resulting in higher spectral efficiency [1-2]. Even in this higher-efficient bandwidth allocation scenario, the bandwidth is non optimally utilized as large guard bands are still employed. Ultra-dense (UD) WDM with a channel spacing of less than 25 GHz, may provide an evolutionary path from conventional infrastructures towards more scalable and spectrally efficient networks. This trend is supported by the increased demand for more capacity, flexibility and upgradeability of transmission technique while keeping some legacy ones, in particular in the metro segments of the optical network. Increasing the number of wavelengths within a fixed optical bandwidth (e.g., C band), by decreasing the spacing between neighboring channels, allows an increase in the system capacity without requiring of high-speed electronics (e.g., >40 Gb/s), while keeping compatibility with the 10 Gb/s SONET/SDH equipment. UDWDM systems with no aliasing condition (i.e. with channel spacing higher than the double the baud rate) have been studied, with particular attention to limitations introduced by fiber nonlinearity effects such as Four-Wave Mixing (FWM), Cross-Phase Modulation (XPM), fiber chromatic dispersion-induced symbol intersymbol interference (ISI) [3]. However, to cope with the required bandwidth efficiency, future UDWDM schemes will need to use extremely close channel spacing; this implies taking measures to mitigate the resultant detrimental effects from crosstalk and neighboring channels interferences.

In this paper we experimentally demonstrate that by employing a digital nonlinear equalizer, such as a Decision Feedback Equalizer (DFE), we can mitigate inter-channel interference, improve overall system performance in terms of OSNR and allow for a channel spacing of 12.5 GHz using conventional independent DFB light sources for a 40 Gb/s ultradense 3 channel WDM PM-QPSK system with coherent detection. Our proof of principle experiment demonstrates that in a 50GHz bandwidth (in accordance to the ITU-T grid) up to 4 channels can be transmitted, improving the total bit rate from 40 Gb/s to 160 Gb/s per slot, with small changes in the electronic equipment.

## 2. System setup

The general outline of the experimental setup for the UDWDM polarization multiplexing (PM) QPSK coherent optical (CO) system is shown in Fig. 1. At the transmitter side three carriers are generated employing three independent tunable distributed feedback lasers (DFB) with 10 MHz linewidth; one of them is fixed at a central wavelength $( \lambda _ { \mathrm { e } } )$ of 1550.511 nm. Different channel spacing values (20, 18, 16, 14, 13, 12, 11 and 10 GHz) between the 3 carriers have been realized by changing the wavelength of the right $( \lambda _ { * } )$ and left ( l) DFB lasers as to have the desired spectral separation. A 40 GHz bandwidth photodiode and an Electrical Spectrum Analyzer are used to verify correct spacing between the three channels. A polarization beam splitter divides the signal into two orthogonal polarization which are then fed into two optical I/Q modulator (nested Mach-Zender modulator). A 10 Gb/s pattern generator (PPG) generates the pseudo random binary sequence (PRBS), with $2 ^ { 1 5 } – 1$ bit length, that drives the two QPSK modulators. Two uncorrelated branches of polarization orthogonal QPSK signals are then combined with a polarization beam combiner (PBC) to generate the PM QPSK signals, at 10 Gbaud/s. An 80 km span of standard single mode fiber (SMF) is used as optical transmission link. At the receiver side an optical tunable band-pass filter (0.33 nm or 37.5 GHz full width at half maximum, FWHM, at1550 nm) is employed before the optical pre-amplifier; a second band-pass filter (0.5 nm or 62.5 GHz FWHM at 1550 nm) rejects the out of band ASE noise. An external cavity laser (ECL) with 100 kHz linewidth is used as local oscillator (LO). The PM coherent receiver consists of two $9 0 ^ { \circ }$ hybrids and balanced photodetectors. The photodetected inphase and quadrature outputs are sampled at 40 GS/s for offline demodulation. Digital signal processing (DSP) algorithms implement digital filtering, PM QPSK constant modulus algorithm (CMA) equalization, QPSK carrier phase recovery and bit error decision.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/53210e653fc7231849c9033e96a97e26fa95c64bfdb3f253ddce4c134b71aa2b.jpg)  
Fig.1. Experiment setup of UDWDM PM QPSK system; DFB: Distributed feedback laser; PD: 40G photodiode; ESA: Electrical Spectrum Analyzer; PC: polarization controller; PBS: polarization beam splitter; PBC: polarization beam combiner; EDFA: erbium-doped fiber amplifier; VOA: variable optical attenuator; OBPF: optical band-pass filter; ECL: external cavity laser.

As the channel distortion or the ISI of a transmission system is too severe for a linear equalizer to mitigate the channel impairments, non-linear equalizer has been used. A DFE is a non-linear structure that uses previous detector decision to eliminate the ISI on pulses currently demodulated. The DFE equalizer will not amplify the noise, cause according to its structure, the equalization process is done through the feedback, noiseless, data. A nonlinear DFE consisting of a feedforward filter (FFE) and a feedback filter (FBE) is used in our DSP receiver, after the carrier phase recovery block, to improve the system performances [4]. The taps of the two equalizers are adjusted using a least mean square (LMS) stochastic algorithm.

## 3. Results

After optimize the PM CMA algorithm structure, we've investigated the impact of a nonlinear decision feedback equalizer consisting of a 1 tap feedforward filter (FFE) and a 7 or 9 taps feedback filter (FBE) on the system performances (this structure is indicated as DFE in the graphs); the digital filter is then re-optimized to improve further the BER curves. The measured BER performances of the UDWDM PM QPSK for back-to-back (B2B) system are shown in Fig. 2. Fig. 2(a) shows the BER experimental performances as a function of the measured OSNR for a spacing of 14 GHz without nonlinear equalization, with the nonlinear equalization structure DFE and with further optimization of the digital filter. It can be observed that the non-linear equalization and the optimization of the digital filter afterward, can improve the system performances up to 4.5 dB in terms of OSNR and 0.6 dB in terms of BER. The BER versus carrier spacing for two fixed value of OSNR is shown if Fig. 2(b); the results show that the DSP implementation can improve the experimental BER results for all the different spacing. For a fix spacing the algorithm can improve the BER result, while for a fix BER value the use of DSP, it allows closer channel. Of particular importance is 12.5 GHz of spacing which, thanks to the nonlinear equalization, shows performances better then the UFEC limit for both the chosen OSNR.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/67561c47953426610d64c5cf397419d7e8a1e6b3e74af2f258c8bcd3280c9379.jpg)

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/ac85b8eccb11c1c193521af5a8c6f1af6f30922fdc6c65f28fa90d237674fe12.jpg)  
Fig.2.(a) BER as a function of OSNR for a spacing of 14GHz without nonlinear equalization, with DFE and with optimization of the digital filter. (b) BER as a function of the spacing for two fixed values of OSNR with and without nonlinear equalization.

(a)  
![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/7f978e456dbce7a6716e723182d9bd81bff78e67c69c0cb07b1893077c0e0da1.jpg)

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/fb7f7500402c3ea1bbcc5843562639304fee7d251b1eb8140316069fd5b8784d.jpg)  
Fig.3.(a) OSNR as a function of the spacing for two fixed values of BER with and without nonlinear equalization for Back-to-Back. (b) OSNR as a function of the spacing for two fixed values of BER with and without nonlinear equalization for 80Km of SMF.

Fig. 3 shows OSNR performance as a function of the spacing with and without nonlinear equalization for Backto-Back and 80 km of SMF optical transmission are presented. The BER is fixed $\textcircled { a } 1 0 ^ { - 4 }$ and $@ 1 0 ^ { - 3 }$ , both below the UFEC level. The improvement enabled by the DSP implementation on both BER and spacing values is remarkable. As shown in Fig. 3(a) we can improve \~2-3 dB for OSNR with the same spacing value between the carriers; on the other hand for a fix OSNR the carriers can be generated 6 GHz closer, moving from 20 GHz of spacing, case where we have no aliasing, to 14 GHz of spacing. The same behavior is obtained for 80 km of optical transmission. It can be observed in Fig. 3(b) that with the same spacing value between the carriers, the improvement in terms of OSNR is \~3 dB for $\operatorname { B E R } ( \widehat { a } , \dot { 1 } 0 ^ { - 3 }$ and \~5dB for BER@ $1 0 ^ { - 4 }$ ; for the same OSNR then the carriers can be \~6 GHz closer, moving to \~19 GHz to 13 GHz. It should be noticed that the length of the FBE is 7 or 9 taps compared to 1 tap for the FFE, indicating that the signal is affected by non-linearities.

The results obtained suggest more efficient and flexible utilization of the available bandwidth. In case of ITU-T grid with 50 GHz spacing, one single 40 Gb/s signal can be transmitted per slot. Using the proposed UDWDM with DSP non linear equalization, up to 4 channels (12.5 GHz of spacing) per slot can be transmitted with a total bit-rate of 160 Gb/s, with small changes in the electronic equipment. Better results per slot could also be obtained with a single carrier higher data rate signal (100 Gb/s), but this would imply higher speed electronics and no more compatibility with the existing 10 Gb/s SONET/SDH equipment.

## 4. Conclusion

We have experimentally demonstrated that by employing a DFE nonlinear equalizer in the DSP domain, an ultradense WDM PM QPSK can be realized. Performances below the UFEC limit are obtained for very closed channel spacing (down to 12.5 GHz). In a 50 GHz ITU-T grid, the structure proposed allows to quadruple the number of user in a flexible way, moving from a total bit rate of 40 Gb/s per slot to 160 Gb/s.

## 5. Acknowledgement

The research leading to these results has received funding from the European Community's Seventh Framework Programme [FP7/2007-2013] under grant agreement n° 258644, CHRON project.

## 6. References

[1] A. Patel, P. Ji, J. Jue and T. Wang, "Survivable Transparent Flexible Optical WDM (FWDM) Networks," in Proc. Optical Fibre Communication Conf., ( Los Angeles, CA, 2011), paper OTuI2

[2] A. Patel, P. Ji, J. Jue and T. Wang, "Defragmentation of Transparent Flexible Optical WDM (FWDM) Networks," in Proc. Optical Fibre Communication Conf., ( Los Angeles, CA, 2011), paper OTuI8

[3] M. Wu and W. Way, "Fiber Nonlinearity Limitations in Ultra-Dense WDM systems," JLT 22, 6 (2004)

[4] D. Zibar, R. Sambaraju, A. Caballero, J. Herrera and I. Tafur Monroy, "Carrier Recovery and Equalization for Photonic-Wireless Links with Capacities up to 40 Gb/s in 75-110 GHz Band," in Proc. Optical Fibre Communication Conf., ( Los Angeles, CA, 2011), paper OThJ4

# Paper 5: Digital non-linear equalization for flexible capacity ultradense WDM channels for metro core networking

Valeria Arlunno, Xu Zhang, Knud J. Larsen, Darko Zibar, and Idelfonso Tafur Monroy. “Digital non-linear equalization for flexible capacity ultradense WDM channels for metro core networking”, Opt. Express, vol. 19, no. 26, pp. B270-B276, 2011.

# Digital non-linear equalization for flexible capacity ultradense WDM channels for metro core networking

Valeria Arlunno,\* Xu Zhang, Knud J. Larsen, Darko Zibar, and Idelfonso Tafur Monroy

DTU Fotonik, Department of Photonics Engineering, Technical University of Denmark, DK-2800 Kgs. Lygnby,

\*vaar@fotonik.dtu.dk

Abstract: An experimental demonstration of Ultradense WDM with advanced digital signal processing is presented. The scheme proposed allows the use of independent tunable DFB lasers spaced at 12.5 GHz for ultradense WDM PM-QPSK flexible capacity channels for metro core networking. To allocate extremely closed carriers, we demonstrate that a digital non-linear equalization allow to mitigate inter-channel interference and improve overall system performance in terms of OSNR. Evaluation of the algorithm and comparison with an ultradense WDM system with coherent carriers generated from a single laser are also reported.

©2011 Optical Society of America

OCIS codes: (060.1660) Coherent communications; (060.4510) Optical communications.

## References and links

1. M. Jinno, B. Kozicki, H. Takara, A. Watanabe, Y. Sone, T. Tanaka, and A. Hirano, “Distance-Adaptive Spectrum Resource Allocation in Spectrum-Sliced Elastic Optical Path Network,” IEEE Commun. Mag. 48(8), 138–145 (2010).

2. N. Amaya, G. S. Zervas, M. Irfan, Y. R. Zhou, A. Lord, and D. Simeonidou, “Experimental demonstration of gridless spectrum and time optical switching,” Opt. Express 19(12), 11182–11188 (2011).

3. N. Amaya, M. Irfan, G. Zervas, K. Banias, M. Garrich, I. Henning, D. Simeonidou, Y. R. Zhou, A. Lord, K. Smith, V. J. F. Rancano, S. Liu, P. Petropoulos, and D. J. Richardson, “Gridless Optical Networking Field Trial: Flexible Spectrum Switching, Defragmentation and Transport of 10G/40G/100G/555G over 620-km Field Fiber,” in European Conf. Opt. Commun., OSA Technical Digest (CD) (Optical Society of America, 2011), paper Th.13.K.1.

4. D. J. Geisler, R. Proietti, Y. Yin, R. P. Scott, X. Cai, N. K. Fontaine, L. Paraschis, O. Gerstel, and S. J. B. Yoo, “The First Testbed Demonstration of a Flexible Bandwidth Network with a Real-Time Adaptive Control Plane,” in European Conf. Opt. Commun., OSA Technical Digest (CD) (Optical Society of America, 2011), paper Th.13.K.2.

5. A. Patel, P. Ji, J. Jue, and T. Wang, “Survivable Transparent Flexible Optical WDM (FWDM) Networks,” Optical Fiber Communication Conference, OSA Technical Digest (CD) (Optical Society of America, 2011), paper OTuI2.

6. A. Patel, P. Ji, J. Jue, and T. Wang, “Defragmentation of Transparent Flexible Optical WDM (FWDM) Networks,” in Optical Fiber Communication Conference, OSA Technical Digest (CD) (Optical Society of America, 2011), paper OTuI8.

7. P. N. Ji, A. Patel, D. Qian, J. Jue, J. Hu, Y. Aono, and T. Wang, “Optical Layer Traffic Grooming in Flexible Optical WDM (FWDM) Networks,” in European Conf. Opt. Commun., OSA Technical Digest (CD) (Optical Society of America, 2011), paper We.10.P1.102.

8. J. Berthold, “Toward 100G Networking and Beyond”, in European Conf. Opt. Commun., OSA Technical Digest (CD) (Optical Society of America, 2011), paper Tu.3.K.1.

9. M. Wu and W. Way, “Fiber Nonlinearity Limitations in Ultra-Dense WDM systems,” J. Lightwave Technol. 22(6), 1483–1498 (2004).

10. J. Kurzweil, An Introduction to Digital Communications (John Wiley & Sons, Inc., 1999), Chap. 10.

11. D. Zibar, R. Sambaraju, A. Caballero, J. Herrera, and I. Tafur Monroy, “Carrier Recovery and Equalization for Photonic-Wireless Links with Capacities up to 40 Gb/s in 75-110 GHz Band,” in Optical Fiber Communication Conference, OSA Technical Digest (CD) (Optical Society of America, 2011), paper OThJ4.

## 1. Introduction

Rigid and coarse granularity of wavelength-division-multiplexing (WDM) systems leads to inefficient capacity utilization, which partly results from the lost spectrum due to the difference between the real spectral occupancy of the signal and the ITU-T grid. A promising way would be to introduce the concept of a frequency slot instead of the current frequency grid [1], moving toward flexible grid and grid-less solutions [2–4]. In flexible optical WDM (FWDM), spectral resources are allocated in a flexible and dynamic way; channel spacing and center wavelength are not fixed on the ITU-T grid, resulting in higher spectral efficiency [5,6]. Standardization towards more flexible scenario specifying frequency slots of variable width rather than a fixed frequency grid is currently ongoing in ITU-T SG.15, Q.6. Even in this higher-efficient bandwidth allocation scenario, the bandwidth is non optimally utilized as large guard bands are still employed, as shown in Fig. 1 [7]. Ultra-dense (UD) WDM with a channel spacing of less than 25 GHz, may provide an evolutionary path from conventional infrastructures towards more scalable and spectrally efficient networks. This trend, supported by the increased demand for more capacity, flexibility and upgradeability of transmission technique while keeping some legacy ones will require a comprehensive reexamination of the way metro-core networks are designed and built [8].

Increasing the number of wavelengths within a fixed optical bandwidth (e.g., C band), by decreasing the spacing between neighboring channels, allows an increase in the system capacity without requiring of high-speed electronics (e.g., >40 Gb/s), while keeping compatibility with the 10 Gb/s SONET/SDH equipment. UDWDM systems with no aliasing condition (i.e. with channel spacing higher than the double the baud rate) have been studied, with particular attention to limitations introduced by fiber nonlinearity effects such as Four-Wave Mixing (FWM), Cross-Phase Modulation (XPM), fiber chromatic dispersion-induced symbol intersymbol interference (ISI) [9]. However, to cope with the required bandwidth efficiency, future UDWDM schemes will need to use extremely close channel spacing; this implies taking measures to mitigate the resultant detrimental effects from crosstalk and neighboring channels interferences.

In this paper we experimentally demonstrate that an upgraded digital signal processing (DSP) allows for closer channel spacing, up to 12.5 GHz, using conventional independent DFB light sources for a 40 Gb/s ultradense 3 channel WDM PM-QPSK system with coherent detection. The employment of a digital nonlinear equalizer, such as a Decision Feedback Equalizer (DFE), can mitigate inter-channel interference and improve overall system performance in terms of OSNR. Our proof of principle experiment demonstrates that in a 50GHz bandwidth (in accordance to the ITU-T grid) up to 4 channels can be transmitted, improving the total bit rate from 40 Gb/s to 160 Gb/s per slot, with a minor upgrade in the electronic equipment.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/74b240b3d6aa5e3ef79c99ea3fe5758157f10df1994a0205e71feb0842f01dc0.jpg)  
Fig. 1. Moving from fix to flex grid scenario. Large guard bands are still employed in both schemes.

## 2. System setup

The general outline of the experimental setup for the UDWDM polarization multiplexing (PM) QPSK coherent optical (CO) system is shown in Fig. 2. At the transmitter side three carriers are generated employing three independent tunable distributed feedback lasers (DFB) with 10 MHz linewidth; RQH RI WKHP LV IL[HG DW D FHQWUDO ZDYHOHQJWK $( \lambda _ { < } )$ of 1550.511 nm. 'LIIHUHQWFKDQQHOVSDFLQJYDOXHVǻȜ DQG\*+]EHWZHHQWKH FDUULHUV KDYH EHHQ UHDOL]HG E\ FKDQJLQJ WKH ZDYHOHQJWK RI WKH ULJKW $( \lambda _ { e } )$ DQG OHIW Ȝl) DFB lasers as to have the desired spectral separation. A 40 GHz bandwidth photodiode and an Electrical Spectrum Analyzer are used to verify correct spacing between the three channels. A polarization beam splitter divides the signal into two orthogonal polarization which are then fed into two optical I/Q modulator (nested Mach-Zehnder modulator). A 10 Gb/s pattern generator (PPG) generates the pseudo random binary sequence (PRBS), with $2 ^ { 1 5 } – 1$ bit length, that drives the two QPSK modulators. Two uncorrelated branches of polarization orthogonal QPSK signals are then combined with a polarization beam combiner (PBC) to generate the PM QPSK signals, at 10 Gbaud. An 80 km span of standard single mode fiber (SMF) is used as optical transmission link. At the receiver side an optical tunable band-pass filter (0.33 nm or 37.5 GHz full width at half maximum, FWHM, at 1550 nm) is employed before the optical pre-amplifier; a second band-pass filter (0.5 nm or 62.5 GHz FWHM at 1550 nm) rejects the out of band ASE noise. An external cavity laser (ECL) with 100 kHz linewidth is used as local oscillator (LO). The PM coherent receiver consists of two $9 0 ^ { \circ }$ hybrids and balanced photodetectors. The photodetected inphase and quadrature outputs are sampled at 40 GS/s for offline demodulation. Digital signal processing (DSP) algorithms implement digital filtering, PM QPSK constant modulus algorithm (CMA) equalization, QPSK carrier phase recovery and bit error decision. As the channel distortion or the ISI of a transmission system is too severe for a linear equalizer to mitigate the channel impairments, non-linear equalizer has been used. A DFE is a non-linear structure that uses previous detector decision to eliminate the ISI on pulses currently demodulated. The basic idea is that if the values of the symbols previously detected are known, then ISI contributed by these symbols can be canceled out exactly at the output of the forward filter by subtracting past symbol values with appropriate weighting. The DFE equalizer will not amplify the noise, cause according to its structure, the equalization process is done through the feedback, noiseless, data applying symbol-by-symbol detection

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/bfa180c4d5a8be7a0dfd21d70f4458c30a98eacd352b0b5c9fa476b8f053d249.jpg)  
Fig. 2. Experiment setup of UDWDM PM QPSK system; DFB: Distributed feedback laser; PD: 40G photodiode; ESA: Electrical Spectrum Analyzer; PC: polarization controller; PBS: polarization beam splitter; PBC: polarization beam combiner; EDFA: erbium-doped fiber amplifier; VOA: variable optical attenuator; OBPF: optical band-pass filter; ECL: external cavity laser.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/70c48121f98f15b1d9abaabc1a020b0be2e0a4d48f4867f8bb541392977291ac.jpg)  
Fig. 3. Non-linear Decision Feedback Equalizer (DFE) structure.

with successive cancellation of the interference caused by the detected symbols [10]. A nonlinear DFE, shown in Fig. 3, consisting of a feed-forward filter (FFE) and a feed-back filter (FBE) is used in our DSP receiver, after the carrier phase recovery block, to improve the system performances [11]. The taps of the two equalizers are adjusted using a least mean square (LMS) stochastic algorithm.

## 3. Results

After optimize the PM CMA algorithm structure, we have investigated the impact of a nonlinear decision feedback equalizer on the system performances (this structure is indicated as DFE in the graphs); the best configuration is composed of a 1 tap feedforward filter (FFE) and a 7 or 9 taps feedback filter (FBE). The digital filter is then re-optimized to improve further the BER curves. The measured BER performances of the UDWDM PM QPSK for back-to-back (B2B) system are shown in Fig. 4. Figure 4(a) shows the BER experimental performances as a function of the measured OSNR for a spacing of 14 GHz without nonlinear equalization, with the nonlinear equalization structure DFE and with further optimization of the digital filter. It can be observed that the non-linear equalization and the optimization of the digital filter afterward, can improve the system performances up to 4.5 dB in terms of OSNR. The BER versus carrier spacing for two fixed value of OSNR is shown in Fig. 4(b); the results show that the DSP implementation can improve the experimental BER results for all the different spacing. For a fix spacing the algorithm can improve the BER result, while for a fix BER value the use of DSP, it allows closer channel. Of particular importance is 12.5 GHz of spacing which, thanks to the nonlinear equalization, shows performances better then the UFEC limit for both the chosen OSNR.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/b2277c3c7cf82dd4ea8e1d89e809270391b232ca919dcec7eaffb7bb370d7b83.jpg)

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/5a8373d578ea5e3ebeacd0060d6608ed869c9db19547e7730e5b202333ba725a.jpg)  
Fig. 4. (a) BER as a function of OSNR for a spacing of 14GHz without nonlinear equalization, with DFE and with optimization of the digital filter. (b) BER as a function of the spacing for two fixed values of OSNR with and without nonlinear equalization.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/4e6604c56aa0f7b78d441d29986e0736b1f0c31d53f5e81fc25bafaaf6ebaaf8.jpg)

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/a407409356c74470e779f79e29e48308fab0ca207529603b2adea6986093f16d.jpg)  
Fig. 5. (a) OSNR as a function of the spacing for two fixed values of BER with and without nonlinear equalization for Back-to-Back. (b) OSNR as a function of the spacing for two fixed values of BER with and without nonlinear equalization for 80Km of SMF.

Figure 5 shows OSNR performance as a function of the spacing with and without nonlinear equalization for Back-to-Back and 80 km of SMF optical transmission are presented. The BER is fixed $1 0 ^ { - 4 }$ and $1 0 ^ { - 3 } ,$ both below the UFEC level. The improvement enabled by the DSP implementation on both BER and spacing values is substantial. As shown in Fig. 5(a) the proposed algorithm can improve up to 3 dB of OSNR with the same spacing value between the carriers; on the other hand for a fix OSNR the carriers can be generated 6 GHz closer, moving from 20 GHz of spacing, case where we have no aliasing, to 14 GHz of spacing. The same behavior is observed for 80 km of optical transmission. It can be observed in Fig. 5(b) that with the same spacing value between the carriers, the improvement in terms of OSNR is 3 dB for BER $1 0 ^ { - 3 }$ and 5dB for BER $1 0 ^ { - 4 } ;$ for the same OSNR then the carriers can be 6 GHz closer, moving to 19 GHz to 13 GHz. It should be noticed that the length of the FBE is 7 or 9 taps compared to 1 tap for the FFE, indicating that the signal is affected by nonlinearities.

To prove the efficiency of the algorithm used, we have evaluated its performances in a system with 3 coherent carriers. Figure 6 shows the transmitter side of the two configuration under study, the UDWDM with different lasers previously presented, called from now on DFB, and the new scheme. A single tunable DFB with 10MHz linewidth is employed to drive a Mach-Zehnder modulator (MZM), to generate three coherent carriers. The different channel VSDFLQJ ǻȜ        DQG  \*+] EHWZHHQ WKH  FDUULHUV KDV QRZ EHHQ realized by operating the synthesizer, the input source to the MZM, as to have the desired spectral separation. From now on we will refer to the scheme as MZM.

After optimize the PM CMA algorithm structure, we have investigated the impact of the same nonlinear decision feedback equalizer of the UDWDM DFB case on the system performances; also in this case the digital filter is then re-optimized to improve further the BER curves. The BER versus carrier spacing for a fixed OSNR value is shown if Fig. 7(a); the

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/f63b2088c45cd4e5d025bfc30988289487c050adf34d50782835af665bfad4c0.jpg)  
Fig. 6. Experiment setup of transmitter side for UDWDM with DFB scheme and MZM scheme.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/ce2d67516e355839892e9ed910111678ea1c3146144634e1996b3a7c89539a23.jpg)

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/45dd2aad0c6948fc38d99dab8d0916b5791df9839b91ddaaf20ec84ccfa765ff.jpg)  
Fig. 7. (a) BER as a function of the spacing for a fixed value of OSNR with and without nonlinear equalization for UDWDM MZM case. (b) BER as a function of the spacing for a fixed value of OSNR for UDWDM DFB and MZM case.

results show that the DSP implementation can improve the experimental BER results for all the different spacing. In this case, the results show higher improvement for smaller frequency spacing between the 3 carriers. The employment of our suggested non-linear equalization 12.5 GHz of spacing shows performances better then the UFEC limit also for the UDWDM MZM case. No results are displayed for a frequency separation equals to 10 GHz, because in this case with this configuration, we will not have an UDWDM scheme, but an OFDM. Figure 7(b) shows the BER versus carrier spacing for the same fixed OSNR value for both cases under study. In both cases is appreciable the benefit introduced by non-linear equalization. For frequency separation between the 3 carriers higher than 14 GHz, the BER performances are better in the MZM case, but in the DFB case the DFE algorithm provides higher improvement. For frequency separation smaller than 14 GHz, in particular for the 12.5 GHz case, the BER performances of the schemes are comparable.

The results obtained suggest more efficient and flexible utilization of the available bandwidth. In case of ITU-T grid with 50 GHz spacing, one single 40 Gb/s signal can be transmitted per slot. Using the proposed UDWDM DFB with DSP non linear equalization, up to 4 channels (12.5 GHz of spacing) per slot can be transmitted with a total bit-rate of 160 Gb/s, with a minor upgrade in the electronic equipment and higher flexibility. Better results per slot could also be obtained with a single carrier higher data rate signal (100 Gb/s), but this would imply higher speed electronics and no compatibility anymore with the existing 10 Gb/s SONET/SDH equipment.

## 4. Conclusion

We have experimentally demonstrated a flexible ultradense WDM QPSK system with upgrading DSP algorithms. The DFE nonlinear equalizer structure proposed allows for extremely closed spacing (up to 12.5 GHz), where bit error rate performances below the UFEC limit are obtained. In a 50 GHz ITU-T grid, the structure presented in this paper allows to quadruple the number of users in a flexible way, moving from a total bit rate of 40 Gb/s per slot to 160 Gb/s. We believe that the upgradable and flexible structure proposed well suit in the trend towards next generation flex-grid and grid-less scenarios.

## Acknowledgments

The research leading to these results has received funding from the European Community's Seventh Framework Programme [FP7/2007-2013] under grant agreement n° 258644, CHRON project. The authors thank Teraxion for the technical expertise provided.

# Paper 6: Experimental adaptive digital performance monitoring for optical DP-QPSK coherent receiver

Robert Borkowski, Xu Zhang, Darko Zibar, Richard Younce, and Idelfonso Tafur Monroy. “Experimental adaptive digital performance monitoring for optical DP-QPSK coherent receiver”, in Proceedings of the 37th European Conference on Optical Communication, ECOC’2011, Geneva, Switzerland, September 2011.

# Experimental Adaptive Digital Performance Monitoring for Optical DP-QPSK Coherent Receiver

Robert Borkowski1, Xu Zhang1, Darko Zibar1, Richard Younce2, Idelfonso Tafur Monroy1

1 DTU Fotonik, Department of Photonics Engineering, Technical University of Denmark, Ørsteds Plads, Building 343, DK-2800 Kgs. Lyngby, Denmark 2 Tellabs, 1415 West Diehl Road, Naperville, IL 60563, USA

rbor@fotonik.dtu.dk

Abstract: We report on a successful experimental demonstration of a digital optical performance monitoring (OPM) yielding satisfactory estimation accuracy along with adaptive impairment equalization. No observable penalty is measured when equalizer is driven by monitoring module.

OCIS codes: 060.1660, 060.2330.

## 1. Introduction

Coherent digital optical communication is already well established and in commercial use. Nonetheless, a vital part of each communication system is a monitoring subsystem, which is still underdeveloped. Due to increasing bit rates, it is very important to be able to isolate impairments, such as chromatic dispersion (CD), polarization mode dispersion (PMD) or optical signal-to-noise ratio (OSNR), affecting transmitted optical signal and mitigate their influence as much as possible in order to ensure best reception quality and thus minimize the number of received bit errors. Digital signal processing (DSP)-based OPM does not require any additional optical hardware and can be seamlessly combined with digital data coming from the coherent receiver. So far, only computer simulations of blind CD equalization realized in monitoring module preceding timing recovery stage were reported in literature [1-3].

In this paper, for the first time, as to our knowledge, we show that experimental estimation of CD affecting the received signal is feasible in this arrangement and allows for entirely autonomous operation of an equalization-enabled digital coherent receiver. We present that the receiver, without prior knowledge of the channel, can adaptively adjust in order to mitigate signal degradation related to CD.

## 2. Blind Chromatic Dispersion Monitoring for Digital Coherent Receiver

We are considering a dual polarization quadrature phase-shift keying (DP-QPSK) receiver consisting of the optical front end and a DSP part, as shown in Figure 1, which follows structure presented in [2, 4]. Two samples per each transmitted symbol are processed by analog-to-digital converters (ADCs). First DSP block, which is of interest to this paper, is used for CD estimation and adaptive equalization performed with an adjustable transversal CD equalizer. Following that, timing recovery takes place. A short, 7-tap finite impulse response (FIR) filter is then used for polarization demultiplexing as well as to remove residual impairments. Finally, carrier recovery is performed which results in a stable received constellation.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/618242b91f3a198fe01690ef2dbf22dd13e88d5fcb4a6606be9a446a5398cb54.jpg)  
Fig. 1: Typical structure of a digital coherent receiver with CD monitoring and equalization block. Receiver in the figure monitors CD from time domain samples.

A generic scanning algorithm is employed for dispersion estimation. CD metric is used to assess if in samples after passing through the equalizer, CD influence has been removed or not. Range of interest of CD parameter is the lowest and highest value of CD that may affect the incoming signal. The algorithm works as follows. 1) Sweep range of interest of CD parameter, each time setting the transversal equalizer to a candidate transfer function $H _ { C D } =$ exp $\left( j f ^ { 2 } \pi \frac { \lambda ^ { 2 } } { c } C D \right)$ ( f being clock frequency, λ, signal wavelength and c the speed of light). As an engineering rule, scanning resolution for a simple maximum or minimum search shall not exceed 300 ps/nm with a recommended value of 200ps/nm for 28GBd signal, which scales proportionally to symbol rate squared. 2) Equalize the impaired signal with the candidate transfer function. 3) Find the metric of the equalized signal. 4) Repeat steps 2-3 for for each CD value in the swept range. 5) Once metric has been computed for all values of CD parameter in the range of interest, search for the value for which successful CD compensation is indicated by the metric feature.

Four different metrics were used to perform monitoring. First one is based on a constant modulus algorithm (CMA) and was presented in [1]. It penalizes deviation from an expected power. Another, which is a modification to the first one, compares mean power of the uneqalized signal with mean power of post-equalization samples thus judging on whether CD was compensated. Third method relies on observation of eigenvalues of channel autocorrelation matrix. These techniques work directly with time domain samples. Last method, frequency spectrum autocorrelation [3], is frequency domain-based. Each CD metric listed above results in a distinctive minimum/maximum when the data signal is correctly compensated for CD.

## 3. Experimental setup

In order to experimentally prove that this monitoring approach is feasible, we focus on a single branch of a polarization multiplexing (PolMux) QPSK transmitter. A pattern generator provides in-phase and quadrature signal at a bit rate of 20 Gbit/s. Resulting optical signal is thus a 40 Gbit/s single polarization (SP) QPSK. To test monitoring algorithms for different magnitudes of CD affecting the signal, two cases are investiagated. Firstly, back-to-back transmission (CD-free channel) and 80 km of standard single-mode fiber (SSMF) with a dispersion coefficient of approximately 16ps/(nm km), yielding 1280ps/nm CD in total. The reason for back-to-back trial is to check if the monitoring works correctly even if there is no CD present in the channel. In the next step, optical noise is added to the signal, starting with optical signal-to-noise ratio (OSNR) of 24 dB, down to 12 dB. A preamplifier just before the receiver is used in order to keep power entering a 100 G digital coherent receiver at a constant level of 10dBm. Local oscillator (LO) is tuned to 1548.88nm and signal wavelength is separated by less than 100MHz, both using DFB narrow linewidth lasers (NLLs). Digital storage oscilloscope (DSO) is used to capture the voltage signal after conversion from optical to electrical domain has been performed. Traces recorded by the DSO are then processed offline.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/b9df04515c0a77b17f0b7ef8ca8e10933b8b1e502a1586cf541231c1102a38fd.jpg)  
Fig. 2: Experimental setup of the transmission system. CW: continuous wave laser, PRBS: pseudorandom binary sequence generator, PBC: polarization beam combiner, EDFA: erbium-doped fiber amplifier, Preamp: preamplification block, VOA: variable optical attenuator.

## 4. Experimental results

Figure 3 shows bit error rate (BER) curves after demodulation of automatically equalized data, where Preset is a reference line showing performance of the receiver when CD filter is manually set with an apriori known CD value of either 0 ps/nm (Figure 3a) or 16 ps/(nm km)· 80km = 1280ps/nm (Figure 3b). Remaining lines show performance of the receiver for different CD metrics as OSNR is varied for both transmission distances. It may be observed that, regardless of the CD distortion present in the channel, lines depart only to a very small extent from the reference Preset line. This proves that CD DSP monitor produces accurate CD estimates allowing for adaptive equalization driven by feedback signal from monitor. It is necessary to point that this proof-of-concept works with SP-QPSK signal. It is, however, scalable to DP-QPSK as CD affects both polarizations equally.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/066a5184c47567cc889d5b729cfd34707d1c8631db3c0c9cda6ddbb6fa7fa5a0.jpg)  
(a) Back-to-back

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/77b77f10a8a97670e8fdd12d0b5347c09033dc652ce6c972c67fd446edde3b12.jpg)  
(b) 80 km SMF  
Fig. 3: BER curves for all methods as OSNR varies. Preset: reference line based on apriori known CD filter, CMA: constant modulus algorithm, Pav: mean signal power, Eig. spread: eigenvalue spread, Freq. AC: frequency spectrum autocorrelation

## 5. Conclusion

We experimentally demonstrated the use of DSP OPM algorithms in a CD compensation and estimation module preceding timing recovery stage. This allows for an autonomous operation of a digital coherent receiver in a dispersion noncompensated optical network. To the best of our knowledge this is the first demonstration showing feasibility of this receiver arrangement and algorithms in experimental setting. We found out that four different metrics for assessing dispersion mitigation provide estimations of CD accurate enough, that no penalty is observed when compared to a CD filter whose value was fixed prior to the transmission.

## 6. Acknowledgements

We would like to thank Teraxion for providing us PureSpectrum™-NLLs for this experiment. The research leading to these results is partially supported by the CHRON project (Cognitive Heterogeneous Reconfigurable Optical Network) with funding from the European Community’s Seventh Framework Programme [FP7/2007-2013] under grant agreement no. 258644.

## References

1. M. Kuschnerov, F. N. Hauske, K. Piyawanno, B. Spinnler, A. Napoli, and B. Lankl, “Adaptive Chromatic Dispersion Equalization for Non-Dispersion Managed Coherent Systems,” in Optical Fiber Communication Conference, OSA Technical Digest (CD) (Optical Society of America, 2009), paper OMT1.

2. F. N. Hauske, M. Kuschnerov, B. Spinnler, and B. Lankl, “Optical Performance Monitoring in Digital Coherent Receivers,” J. Lightwave Technol. 27, 3623-3631 (2009).

3. F. N. Hauske, C. Xie, Z. P. Zhang, C. Li, L. Li, and Q. Xiong, “Frequency Domain Chromatic Dispersion Estimation,” in National Fiber Optic Engineers Conference, OSA Technical Digest (CD) (Optical Society of America, 2010), paper JThA11.

4. Seb J. Savory, “Digital filters for coherent optical receivers,” Opt. Express 16, 804-817 (2008).

# Paper 7: Experimental demonstration of adaptive digital monitoring and compensation of chromatic dispersion for coherent DP-QPSK receiver

Robert Borkowski, Xu Zhang, Darko Zibar, Richard Younce, and Idelfonso Tafur Monroy. “Experimental demonstration of adaptive digital monitoring and compensation of chromatic dispersion for coherent DP-QPSK receiver”, Opt. Express, vol. 19, no. 26, pp. B728-B735 2011.

# Experimental demonstration of adaptive digital monitoring and compensation of chromatic dispersion for coherent DP-QPSK receiver

Robert Borkowski,1,∗ Xu Zhang,1 Darko Zibar,1 Richard Younce,2 and Idelfonso Tafur Monroy1

1 DTU Fotonik, Department of Photonics Engineering, Technical University of Denmark, Ørsteds Plads, Building 343, DK-2800 Kgs. Lyngby, Denmark 2 Tellabs, 1415 West Diehl Road, Naperville, IL 60563, USA

∗rbor@fotonik.dtu.dk

Abstract: We experimentally demonstrate a digital signal processing (DSP)-based optical performance monitoring (OPM) algorithm for inservice monitoring of chromatic dispersion (CD) in coherent transport networks. Dispersion accumulated in 40 Gbit/s QPSK signal after 80 km of fiber transmission is successfully monitored and automatically compensated without prior knowledge of fiber dispersion coefficient. Four different metrics for assessing CD mitigation are implemented and simultaneously verified proving to have high estimation accuracy. No observable penalty is measured when the monitoring module drives an adaptive digital CD equalizer.

© 2011 Optical Society of America

OCIS codes: (060.1660) Coherent communications; (060.2330) Fiber optics communications.

## References and links

## 1. Introduction

Coherent optical communication is already a commercially well established technology. One of the advantages of coherent receivers is that DSP algorithms, specifically impairment equalization schemes, can be implemented directly in the receivers’ electronics. Chromatic dispersion, one of the most important factors contributing to signal degradation in long and ultra long haul optical communication systems, can be relatively easy canceled in the DSP circuit of a coherent receiver [1]. This enables operation of dispersion non-compensated links due to the fact that dispersion maps or CD compensation units are no longer necessary to ensure best reception quality and minimize number of received bit errors. Nonetheless, even for DSP-based dispersion filters it is usually assumed that CD value that accumulates in the signal is both known and constant enabling the use of a static CD filter at the receiver. Although this assumption is valid in submarine or terrestrial point-to-point links, it does not hold when mixed or coherent transport networks with routing capabilities are considered. In the general case, CD value of the incoming signal may change dynamically. This challenge is addressed by a DSP-based CD monitoring subsystem.

In literature different approaches to CD monitoring directly from the received data (blind monitoring) have been presented, such as: parameter extraction from FIR filter coefficients [2], time- [3] or frequency-domain [4] monitors placed before timing recovery stage and delay-tap sampling technique [5].

On the other hand, as to the authors’ knowledge, no experimental trial of a monitoring module preceding timing recovery has been performed so far. In this paper we report on a successful experimental demonstration of CD estimation using the aforementioned method. We show that the receiver can adaptively adjust in order to mitigate signal degradation due to CD, even without prior knowledge of the fiber dispersion coefficient.

## 2. Blind chromatic dispersion monitoring for digital coherent receivers

We consider a polarization-division-multiplexing (PDM) quadrature phase-shift keying (QPSK) receiver consisting of the optical front-end and a DSP part, as shown in Fig. 1. The incoming optical signal is photodetected and sampled by analog-to-digital converters (ADCs) operating at twice the symbol rate. The CD monitor and equalizer block, which is of interest to this paper, is used for estimating and performing adaptive equalization of chromatic dispersion. Next, timing recovery takes place. A short, 7-tap finite impulse response (FIR) filter is then used for polarization demultiplexing and mitigation of residual impairments. Finally, carrier recovery is performed.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/76a8ffdcf36d325d8907f6c8e2279b1b049f710bcab825d397a5bd39105d6487.jpg)  
Fig. 1. Typical structure of a digital coherent receiver with CD monitoring and equalization block. The receiver in the figure monitors CD from time domain samples.

## 2.1. Generic scanning algorithm

The CD monitor and equalizer block in Fig. 1 uses a variable, transversal, frequency domain equalizer (FDE) for cancelation of inter-symbol interference (ISI) due to CD. The incoming signal $p \left[ k \right]$ representing received complex optical field is first divided into blocks of length $N _ { \ast }$ indexed consecutively with $k = 0 \dots N - 1$ , and transformed to frequency domain. The resulting signal is then multiplied with the $H _ { O D }$ digital filter

$$
H _ { C D } = \exp \left( j f ^ { 2 } \pi { \frac { \lambda ^ { 2 } } { c } } C D \right) ,\tag{1}
$$

where f is the clock frequency, λ the signal wavelength, c the speed of light and CD the value of CD. The rationale behind using an FDE is the number of required complex multiplications as compared to time domain approach [6]. Next, the signal $Q [ { \dot { k } } ]$ obtained after multiplication is transformed back to time domain as q [k] and constitutes the output of the equalizer. Signals $p$ and $q$ (or $Q ,$ depending on particular method) are fed to a CD DSP OPM module which computes the metric J. Since the value of CD present in the channel is unknown, the transfer function $H _ { C D }$ may not be computed. However, due to the fact that $H _ { O D }$ has only one degree of freedom, adaptation can be performed by sweeping over a range of CD parameter, every time updating $H _ { C D ^ { + } }$ until an optimal operating point is found. An interest range of CD values shall be specified, which in general will be different for each optical network and may depend on the topology and traffic characteristic. The CD parameter can be initialized as to coincide with the most probable CD value of the received signal in order to increase the convergence speed. The space of CD parameter is then gradually searched with a given resolution and the metric $J [ C D ]$ is computed for every value of CD under test.

As an engineering rule, CD scanning resolution for a simple maximum or minimum searchbased metric shall not exceed 300 ps/nm with a recommended value of 200 ps/nm for a 28 Gbaud signal, which scales proportionally to the symbol rate squared. Once metric has been computed for all values lying within the range of interest, the metric is examined for a particular feature (e.g. minimum or maximum) which indicates the value of CD parameter that should be used to recalculate $H _ { C D }$ to mitigate the CD ISI.

The algorithm can be further extended to take average of the metric over multiple blocks or include multiple passes, each time narrowing the scanning range and increasing the scanning resolution. An example of a two-pass scan based on experimental data is shown in Fig. 2. Range between 0 ps/nm and 4000 ps/nm is swept with a step of 200 ps/nm (coarse scan). Once this initial estimate is obtained, a second pass with a resolution of only 20 ps/nm sets in and ranges 800 ps/nm centered around the previously found estimate (fine scan). This allows to increase the accuracy of the estimation. In theory, if no other impairment than CD is present in the signal, the maximum estimation error should be half of the scanning resolution. In practice, estimation error resulting from a single run is much greater because metrics are computed from blocks of finite length. Nonetheless, the accuracy of CD estimation at this stage is not strictly important because residual CD is compensated in the MIMO FIR filter that follows the CD equalizer in the receiver’s DSP chain (comp. Fig. 1).

## 2.2. Dispersion metrics

This section provides a brief overview of algorithms for metrics computation. Four different metrics were implemented and experimentally verified in a transmission experiment. Figure 2 shows a comparison of those metrics generated from an experimental transmission of 20 Gbaud QPSK signal in a channel with 1280 ps/nm CD.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/aeb9b36f04b2ef5d71a70b1aebd3f7a8e3047382a4bf58cb8771291cc953336a.jpg)  
(a) Coarse scan (200 ps/nm)

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/f9c75aa661dce43bf6c2a1b0e9094acb7fb7c5310221dc511018e3e6e4eb3c96.jpg)  
(b) Fine scan (20 ps/nm)  
Fig. 2. Comparison of all metrics after normalization to [0, 1] range. Pav metric was subtracted from 1 for clearness of comparison. Bold dashed vertical line shows the actual value of CD present in the channel (1280 ps/nm).

## 2.2.1. CMA metric

The first evaluated metric is described in [3, 7] and references provide its evaluation in computer simulations. The algorithm for this metric is based on a modified constant modulus algorithm (CMA) where a deviation from a constant power $R _ { 2 }$ is the error function (metric). Since the received signal is sampled at twice the symbol rate, another normalization constant $R _ { 1 }$ has to be used. Both $R _ { 1 }$ and $R _ { 2 }$ have to be constantly estimated from the power of odd and even samples of the received signal. The metric J is then computed

$$
J [ C D ] = \frac { 1 } { N } \sum _ { k = 0 } ^ { N - 1 } \left( \Big | | q [ 2 k + 1 ] | ^ { 2 } - R _ { 1 } \Big | + \Big | | q [ 2 k ] | ^ { 2 } - R _ { 2 } \Big | \right) .\tag{2}
$$

The required normalization constants $R _ { 1 }$ and $R _ { 2 }$ are determined for each block. First, the mean power of odd and even samples, ¯q1 and ¯q2, is calculated

$$
\bar { q } _ { 1 } = \frac { 1 } { N } \sum _ { k = 0 } ^ { N - 1 } \left( q \left[ 2 k + 1 \right] \right) ^ { 2 } \qquad \bar { q } _ { 2 } = \frac { 1 } { N } \sum _ { k = 0 } ^ { N - 1 } \left( q \left[ 2 k \right] \right) ^ { 2 } .\tag{3}
$$

Based on the ratio of $\bar { q } _ { 2 }$ to ${ \bar { q } } _ { 1 } , R _ { 1 }$ and $R _ { 2 }$ normalization constants are determined as follows:

$$
\begin{array} { r } { \left[ R _ { 1 } \quad R _ { 2 } \right] = \left\{ \begin{array} { l l } { \left[ R _ { a } \quad R _ { c } \right] } & { \quad \mathrm { i f ~ } \frac { \hat { q } _ { 2 } } { \hat { q } _ { 1 } } > \xi } \\ { \left[ R _ { b } \quad R _ { b } \right] } & { \quad \mathrm { i f ~ } \xi ^ { - 1 } \leq \frac { \hat { q } _ { 2 } } { \hat { q } _ { 1 } } \leq \xi } \\ { \left[ R _ { c } \quad R _ { a } \right] } & { \quad \mathrm { i f ~ } \frac { \hat { q } _ { 2 } } { \hat { q } _ { 1 } } < \xi ^ { - 1 } } \end{array} \right. } \end{array}\tag{4}
$$

with proposed empirically adjusted parameters $\xi = 1 . 2 5 , R _ { a } = 0 . 6 , R _ { b } = 1 . 5$ and $R _ { e } = 2$ for the received complex signal power normalized to 1.

The curve of the metric presented in Fig. 2 was averaged over 8 different realizations, each having N = 256 samples.

## 2.2.2. Mean signal power

The second implemented metric is a simplified variant of the CMA-based metric. The mean power of samples at the input to the equalizer

$$
P = \frac { 1 } { N } \sum _ { k = 0 } ^ { N - 1 } \left| p [ k ] \right| ^ { 2 }\tag{5}
$$

is compared with the mean power of the signal after CD equalization and decimation to 1 sample/symbol stage. The post-decimation mean power, expressed in terms of signal q at the output of the CD equalizer is given by

$$
\widehat { P } = \frac { 2 } { N } \sum _ { k = 0 } ^ { \tilde { \Psi } - 1 } \left| q \left[ 2 k \right] \right| ^ { 2 } .\tag{6}
$$

Next, J metric is found according to

$$
J [ C D ] = \left| P - \widehat { P } \right| ,\tag{7}
$$

and the estimated value of CD parameter is indicated by the maximum of the metric.

In Fig. 2 the estimated CD value is found at a minimum as the metric was mirrored along the horizontal line at 0.5. Block size chosen for this metric was $N = 2 0 4 8$

## 2.2.3. Eigenvalue spread

An alternative metric, operating with time domain samples, relies on inspection of eigenvalue spread of the autocorrelation matrix. The concept, reviewed in [8], has not been used previously in relation to CD monitoring.

This metric uses samples from the CD equalizer after performing decimation to 1 sample/symbol.

The eigenvalue spread $\chi$ of the autocorrelation matrix R is a quantitative measure of signal distortion. Specifically, R is the following Toeplitz matrix of size $L \times L$

$$
\mathbf { R } = \left[ \begin{array} { c c c c } { r \left( 0 \right) } & { r ^ { * } \left( 1 \right) } & { \cdots } & { r ^ { * } \left( L - 1 \right) } \\ { r \left( 1 \right) } & { r \left( 0 \right) } & { \cdots } & { r ^ { * } \left( L - 2 \right) } \\ { \vdots } & { \vdots } & { \ddots } & { \vdots } \\ { r \left( L - 1 \right) } & { r \left( L - 2 \right) } & { \cdots } & { r \left( 0 \right) } \end{array} \right]\tag{8}
$$

where r is the autocorrelation of the signal q calculated as

$$
r ( m ) = \sum _ { k = L } ^ { \tilde { q } - 1 } q \left[ 2 k \right] q ^ { * } \left[ 2 \left( k - m \right) \right]\tag{9}
$$

and ∗ denotes complex conjugate. The eigenvalue spread of the autocorrelation matrix and the CD metric itself is then defined as

$$
J [ C D ] = \chi \left( \mathbf { R } \right) = \frac { \lambda _ { \operatorname* { m a x } } } { \lambda _ { \operatorname* { m i n } } } ,\tag{10}
$$

where $\lambda _ { \mathrm { m a x } }$ and $\lambda _ { \mathrm { m i n } }$ are eigenvalues of R with the largest and the smallest magnitudes respectively. If the dispersion was correctly compensated, the autocorrelation matrix is wellconditioned and the spread of eigenvalues approaches the theoretical minimum at 1. Otherwise, the matrix is ill-conditioned and the spread is significantly larger than that. This approach allows for construction of a minimum-search metric.

An engineering rule for the autocorrelation matrix size producing good results was found to be

$$
L = { \frac { C D _ { \mathrm { m a x } } - C D _ { \mathrm { m i n } } } { 7 5 } } ,\tag{11}
$$

where in the numerator the maximum and minimum values of CD parameter (expressed in ps/nm) in the range of interest are used (units neglected). It should be noted that eigenvalues computation is an expensive task in terms of required processing power and, therefore, practical use of this metric might be limited.

In the curve shown in Fig. 2, block size was chosen to be $N = 1 6 3 8 4$ and matrix size $L = 5 3$

## 2.2.4. Frequency spectrum autocorrelation

The last metric, frequency spectrum autocorrelation, uses post-equalization samples before the inverse fast Fourier transform (IFFT) block. This method was studied in simulation in [4]. It uses signal Q, which is the frequency domain representation of the CD equalizer output after multiplication with the filtering function HCD as presented in Fig. 1. First, a discrete circular autocorrelation is computed

$$
U \left[ m \right] = \frac { 1 } { N } \sum _ { k = 0 } ^ { N - 1 } \mathrm { c s g n } \left( \bigcirc _ { m } ( Q [ k ] ) \right) \cdot Q ^ { * } \left[ k \right] ,\tag{12}
$$

where $O _ { m } ( Q )$ is a circular shift operator that circularly shifts vector Q by m positions (m ∈ N) and csgn is a complex extension of the sign function sgn, defined as csgn $\dot { \mathbf { \Phi } } ( \dot { x } ) = \operatorname { s g n } \left[ \Re ( x ) \right] +$ ı sgn [ℑ(x)], with ℜ and ℑ denoting, respectively, real and imaginary part of a complex number. It is not necessary for m to cover all possible shifts and thus m ranging from $- [ 0 . 7 \frac { N } { 2 } ]$ up to $\lbrace 0 . 7 \frac { N } { 2 } \rbrace$ has been used.

The metric function $J [ C D ]$ for a single CD value under test is then calculated as

$$
J [ C D ] = \sum _ { m } | U [ m ] | ^ { 2 } ,\tag{13}
$$

where summation over m covers all applied circular shifts.

The metric curve shown in Fig. 2 was obtained after averaging 20 realizations, each calculated from a block Q of size $N = 2 5 6$ samples as to smoothen the obtained curve.

## 3. Experimental setup

In order to experimentally prove that CD monitoring with the investigated approach is feasible, we use a single branch of a PDM-QPSK transmitter, as outlined in Fig. 3. A pattern generator provides the in-phase and quadrature inputs to the optical modulator at a bit rate of 20 Gbit/s resulting in a 40 Gbit/s QPSK optical signal. In order to test the monitoring algorithms for different magnitudes of CD affecting the signal, two cases are investigated: the back-to-back case (CD negligibly small) and transmission over 80 km of standard single-mode fiber (SSMF) with a dispersion coefficient of approximately 16 ps/nm/km, yielding 1280 ps/nm accumulated CD in total. Back-to-back trial was performed to test if the monitoring algorithm works correctly in a CD-free channel. As the next step, optical noise is added to the signal, varying the optical signal-to-noise ratio (OSNR) from 24 dB, down to 12 dB. An EDFA preamplifier and an attenuator just before the receiver is used to keep the power entering a 100G coherent receiver at a constant level equal to 10 dBm. The local oscillator (LO) is tuned to 1548.88 nm and the signal wavelength is less than 100 MHz apart. The signal and LO lasers are distributed feedback (DFB) narrow linewidth lasers (NLLs). Digital storage oscilloscope (DSO) is used to capture the voltage signal after conversion from optical to electrical domain. Traces are stored and processed offline.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/5d3116e9500b4f8b691397e1a2a676402a3ecf3ff7df7b310792f5faa8d0220f.jpg)  
Fig. 3. Experimental setup of the transmission system. CW: continuous wave laser, PRBS: pseudorandom binary sequence generator, PC: polarization controller, PBC: polarization beam combiner, EDFA: erbium-doped fiber amplifier, ASE loading: amplified spontaneous emission noise loading, VOA: variable optical attenuator.

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/17d546d3a55619eb6c89e28baf89e75218f5befb1c124b5cf46b2e73e26c08cb.jpg)  
(a) Back-to-back

![](/img/mineru_output/DSP_Coherent_Optical_Communication_Systems_XuZhang_DTU_150p/auto/images/d9ec77be6a64801f08e9fe99a8d5ddd8429ab89df58d4db1d08ebb361f7481f1.jpg)  
(b) 80 km SMF  
Fig. 4. BER vs. OSNR curves for each metric under investigation. Preset: reference line based on a priori known CD filter, CMA: constant modulus algorithm, Pav: mean signal power, Eig. spread: eigenvalue spread, Freq. AC: frequency spectrum autocorrelation.

## 4. Experimental results

Figure 4 shows bit error rate (BER) curves after demodulation of the traces using an equalizer driven by the monitoring module, where Preset is a reference line showing performance of the receiver when CD filter is manually set with an a priori known CD value of either 0 ps/nm (Fig. 4a) or 1280 ps/nm (Fig. 4b). Remaining lines show the performance of the receiver for different CD metrics as OSNR is varied for both transmission distances. It may be observed that regardless of the CD distortion present in the channel, lines depart only to a very small extent from the reference Preset line. This shows that both: each metric and the CD DSP monitor itself are reliable enough as not to introduce any penalty when compared to a CD filter with a fixed CD value. The FIR filter used for polarization demultiplexing is too short to compensate CD after 80 km of fiber transmission; effectively only residual CD is mitigated via the FIR filter, while bulk of the dispersion is removed by the FDE CD equalizer driven by the monitoring module. It is necessary to point out that this proof-of-concept works satisfactory with single polarization QPSK signal and it should be scalable to PDM-QPSK as CD affects both polarizations equally.

## 5. Conclusions

We experimentally demonstrated the use of DSP OPM algorithms for CD compensation and estimation module preceding timing recovery stage. This allows for an autonomous operation of a digital coherent receiver in a dispersion non-compensated coherent transport network. To the best of our knowledge this is the first demonstration showing feasibility of the presented receiver arrangement and algorithms in experimental setting. We found out that the four different metrics for assessing dispersion mitigation provide reliable estimations of CD so as no penalty is observed when compared to a CD filter whose value was fixed prior to the transmission.

## Acknowledgments

We thank Teraxion for providing PureSpectrum™-NLLs for this experiment. The research leading to these results is partially supported by the CHRON project (Cognitive Heterogeneous Reconfigurable Optical Network) with funding from the European Community’s Seventh Framework Programme [FP7/2007-2013] under grant agreement no. 258644.

## Bibliography

[1] R. Ramaswami and K. Sivarajan. Optical Networks: A Practical Perspective. Wiley, Second edition, 2002. ISBN 1-55860-445-6.

[2] S. J. Savory. “Coherent detection - Why is it back?”, in Technical Digest IEEE Lasers and Electro-Optics Society Annual Meeting, LEOS’07, London, UK, Paper TuH1, October 2007.

[3] J. Yu and X. Zhou. “Ultra high capacity DWDM transmission system for 100G and beyond”, IEEE Communication Magazine, vol. 48, pp. 56–64, February 2010.

[4] J. Yu, X. Zhou, M.-F. Huang, Y. Shao, D. Qian, T. Wang, M. Cvijetic, P. Magill, L. Nelson, M. Birk, S. Ten, H. Matthew, and S. Mishra. “17 Tb/s (161 x 114 Gb/s) PolMux-RZ-8PSK transmission over 662 km of ultra-low loss fiber using C-band EDFA amplification and digital coherent detection”, in Optical Communication, 2008. ECOC 2008. 34th European Conference on, Paper Th.3.E.2, sept. 2008.

[5] X. Zhou, J. Yu, M.-F. Huang, Y. Shao, T. Wang, P. Magill, M. Cvijetic, L. Nelson, M. Birk, G. Zhang, S. Ten, H. Matthew, and S. Mishra. “32Tb/s (320x114Gb/s) PDM-RZ-8QAM transmission over 580km of SMF-28 ultra-low-loss fiber”, in Optical Fiber Communication - incudes post deadline papers, 2009. OFC 2009. Conference on, Paper PDPB4, march 2009.

[6] A. Sano, T. Kobayashi, A. Matsuura, S. Yamamoto, S. Yamanaka, E. Yoshida, Y. Miyamoto, M. Matsui, M. Mizoguchi, and T. Mizuno. “100x120-Gb/s PDM 64-QAM transmission over 160 km using linewidth-tolerant pilotless digital coherent detection”, in Optical Communication (ECOC), 2010 36th European Conference and Exhibition on, pp. 1 –3, sept. 2010.

[7] D. Qian, M.-F. Huang, E. Ip, Y.-K. Huang, Y. Shao, J. Hu, and T. Wang. “101.7-Tb/s (370x294-Gb/s) PDM-128QAM-OFDM transmission over 3x55-km ssmf using pilot-based phase noise mitigation”, in Optical Fiber Communication Conference and Exposition (OFC/NFOEC), 2011 and the National Fiber Optic Engineers Conference, Paper PDPB5, march 2011.

[8] A. Sano, T. Kobayashi, A. Matsuura, H. Kawakami, Y. Miyamoto, K. Ishihara, and H. Masuda. “102.3-Tb/s (224 x 548-Gb/s) C- and extended L-band all-raman transmission over 240 km using PDM-64QAM single carrier FDM with digital pilot tone”, in Optical Fiber Communication Conference and Exposition (OFC/NFOEC), 2012 and the National Fiber Optic Engineers Conference, Paper PDP5C.3, march. 2012.

[9] K. Tse. “AT&T’s photonic network”, in Optical Fiber communication/National Fiber Optic Engineers Conference, 2008. OFC/NFOEC 2008. Conference on, pp. 1 –6, feb. 2008.

[10] R. Mears, L. Reekie, I. Jauncey, and D. Payne. “Low-noise erbiumdoped fibre amplifier operating at 1.54 um”, Electronics Letters, vol. 23, no. 19, pp. 1026 –1028, 10 1987.

[11] K. Kikuchi, T. Okoshi, M. Nagamatsu, and N. Henmi. “Degradation of bit-error rate in coherent optical communications due to spectral spread of the transmitter and the local oscillator”, Lightwave Technology, Journal of, vol. 2, no. 6, pp. 1024 – 1033, dec 1984.

[12] T. Okoshi. “Recent advances in coherent optical fiber communication systems”, Lightwave Technology, Journal of, vol. 5, no. 1, pp. 44 – 52, jan 1987.

[13] D. Smith. “Techniques for multigigabit coherent optical transmission”, Lightwave Technology, Journal of, vol. 5, no. 10, pp. 1466 – 1478, oct 1987.

[14] I. Habbab and L. Greenstein. “Phase-insensitive zero-if coherent optical detection using sinusoidal phase modulation instead of phase switching”, in Optical Communication, 1988. (ECOC 88). Fourteenth European Conference on (Conf. Publ. No.292), pp. 65 –68 vol.2, sep 1988.

[15] A. Elrefaie, R. Wagner, D. Atlas, and D. Daut. “Chromatic dispersion limitations in coherent lightwave transmission systems”, Lightwave Technology, Journal of, vol. 6, no. 5, pp. 704 –709, may 1988.

[16] R. Linke and A. Gnauck. “High-capacity coherent lightwave systems”, Lightwave Technology, Journal of, vol. 6, no. 11, pp. 1750 –1769, nov 1988.

[17] A. Chralyvy. “Plenary paper: The coming capacity crunch”, in Optical Communication, 2009. ECOC ’09. 35th European Conference on, p. 1, sept. 2009.

[18] K. Roberts, D. Beckett, D. Boertjes, J. Berthold, and C. Laperle. “100g and beyond with digital coherent signal processing”, Communications Magazine, IEEE, vol. 48, no. 7, pp. 62 –69, july 2010.

[19] A. Saxena. Invention of integrated Circuits: Untold Important Facts. World Scientific, First edition, 2009. ISBN 10 981-281-445-0.

[20] S. Savory. “Electronic signal processing in optical communications”, Proceedings of SPIE - The International Society for Optical Engineering, vol. 7136, no. 71362C, pp. 1–9, 2008.

[21] C. Laperle, B. Villeneuve, Z. Zhang, D. McGhan, H. Sun, and M. O’Sullivan. “WDM performance and PMD tolerance of a coherent 40-Gbit/s dual-polarization QPSK transceiver”, Lightwave Technology, Journal of, vol. 26, no. 1, pp. 168 –175, jan.1, 2008.

[22] G. Raybon, P. Winzer, and et al. “8x320-Gb/s transmission over 5600 km using all-ETDM 80-Gbaud polarization multiplexed QPSK transmitter and coherent receiver”, in Optical Fiber Communication Conference and Exposition (OFC/NFOEC), 2012 and the National Fiber Optic Engineers Conference, Paper OTu2A, march. 2012.

[23] D.-S. Ly-Gagnon, K. Katoh, and K. Kikuchi. “Coherent demodulation of differential 8-phase-shift keying with optical phase diversity and digital signal processing”, in Lasers and Electro-Optics Society, 2004. LEOS 2004. The 17th Annual Meeting of the IEEE, vol. 2, pp. 607 – 608 Vol.2, nov. 2004.

[24] T. Clark, M. Dennis, and R. Sova. “Digital signal processing assisted coherent optical receiver for high dynamic range fiber optic

networks”, in Avionics Fiber-Optics and Photonics, 2005. IEEE Conference, pp. 69 – 70, sept. 2005.

[25] S. Tsukamoto, D.-S. Ly-Gagnon, K. Katoh, and K. Kikuchi. “Coherent demodulation of 40-Gbit/s polarization-multiplexed QPSK signals with 16-GHz spacing after 200-km transmission”, in Optical Fiber Communication Conference, 2005. Technical Digest. OFC/NFOEC, vol. 6, p. 3 pp. Vol. 5, march 2005.

[26] G. P. Agrawal. Fiber-Optic Communication Systems. John Wiley & Sons, Second edition, 2002. ISBN 9780471215714.

[27] S. Alexander. “Design of wide-band optical heterodyne balanced mixer receivers”, Lightwave Technology, Journal of, vol. 5, no. 4, pp. 523 – 537, apr 1987. doi:10.1109/JLT.1987.1075541.

[28] G. Abbas, V. Chan, and T. Yee. “A dual-detector optical heterodyne receiver for local oscillator noise suppression”, Lightwave Technology, Journal of, vol. 3, no. 5, pp. 1110 –1122, october 1985. doi:10.1109/JLT.1985.1074301.

[29] S. Machida and Y. Yamamoto. “Quantum-limited operation of balanced mixer homodyne and heterodyne receivers”, Quantum Electronics, IEEE Journal of, vol. 22, no. 5, pp. 617 – 624, may 1986. doi:10.1109/JQE.1986.1073022.

[30] J. P. H. Nicolas K. Fontaine, Ryan P. Scott and S. J. B. Yoo. “Near quantum-limited, single-shot coherent arbitrary optical waveform measurements”, Opt. Express, vol. 17, no. 15, pp. 12332–12344, 2009.

[31] C. M. Bo Zhang and T. J. Schmidt. “Design of coherent receiver optical front end for unamplified applications”, Opt. Express, vol. 20, no. 3, pp. 3225–3234, January 2012.

[32] G. Berenbrock and B. Schlemmer. “Active controlled fiber optical 90 degrees hybrid for coherent communications”, Photonics Technology Letters, IEEE, vol. 1, no. 4, pp. 86 –87, april 1989.

[33] L. Zimmermann, K. Voigt, G. Winzer, K. Petermann, and C. Weinert. “C-band optical 90-hybrids based on silicon-on-insulator 4x4 waveguide couplers”, Photonics Technology Letters, IEEE, vol. 21, no. 3, pp. 143 –145, feb.1, 2009.

[34] S.-H. Jeong and K. Morito. “Novel optical 90 hybrid consisting of a paired interference based 2x4 MMI coupler, a phase shifter and a 2x2 MMI coupler”, Lightwave Technology, Journal of, vol. 28, no. 9, pp. 1323 –1331, may1, 2010.

[35] K. Ho. Phase-Modulated Optical Communication Systems. Springer, First edition, 2005. ISBN 978-0387-24392-4.

[36] K. Kikuchi. “Polarization-demultiplexing algorithm in the digital coherent receiver”, in IEEE/LEOS Summer Topical Meetings, 2008 Digest of the, pp. 101 –102, july 2008.

[37] M. Faruk, Y. Mori, C. Zhang, and K. Kikuchi. “Proper polarization demultiplexing in coherent optical receiver using constant modulus algorithm with training mode”, in OptoeElectronics and Communications Conference (OECC), 2010 15th, pp. 768 –769, july 2010.

[38] X. Xie, F. Yaman, X. Zhou, and G. Li. “Polarization demultiplexing by independent component analysis”, Photonics Technology Letters, IEEE, vol. 22, no. 11, pp. 805 –807, june1, 2010.

[39] M. Kuschnerov, F. Hauske, K. Piyawanno, B. Spinnler, M. Alfiad, A. Napoli, and B. Lankl. “DSP for coherent single-carrier receivers”, Lightwave Technology, Journal of, vol. 27, no. 16, pp. 3614–3622, aug.15, 2009.

[40] X. Yao and L. Yan. “Polarization management for polarizationdivision-multiplexing and coherent detection systems”, in IEEE/LEOS Summer Topical Meetings, 2008 Digest of the, pp. 147 –148, july 2008. doi:10.1109/LEOSST.2008.4590532.

[41] B. Li, K. Larsen, D. Zibar, and I. Monroy. “Over 10 dB net coding gain based on 20% overhead hard decision forward error correction in 100G optical communication systems”, in Optical Communication (ECOC), 2011 37th European Conference and Exhibition on, pp. 1 –3, sept. 2011.

[42] G. P. Agrawal. Fiber-Optic Communication Systems. John Wiley & Sons, Fourth edition, 2010. ISBN 9780470505113.

[43] K. Kikuchi. “Phase-diversity homodyne detection of multilevel optical modulation with digital carrier phase estimation”, Selected Topics in

Quantum Electronics, IEEE Journal of, vol. 12, no. 4, pp. 563 –570, july-aug. 2006.

[44] M. Fice, A. Seeds, B. Pugh, J. Heaton, and S. Clements. “Homodyne coherent receiver with phase locking to orthogonal-polarisation pilot carrier by optical injection phase lock loop”, in Optical Fiber Communication - incudes post deadline papers, 2009. OFC 2009. Conference on, pp. 1 –3, march 2009.

[45] C. Middleton and R. DeSalvo. “Balanced coherent heterodyne detection with double sideband suppressed carrier modulation for high performance microwave photonic links”, in Avionics, Fiber-Optics and Phototonics Technology Conference, 2009. AVFOP ’09. IEEE, pp. 15 –16, sept. 2009.

[46] R. Zhu, K. Xu, Y. Zhang, Y. Li, J. Wu, X. Hong, and J. Lin. “QAM coherent subcarrier multiplexing system based on heterodyne detection using intermediate frequency carrier modulation”, in Microwave photonics, 2008. jointly held with the 2008 asia-pacific microwave photonics conference. mwp/apmp 2008. international topical meeting on, pp. 165 –168, 9 2008-oct. 3 2008.

[47] X. Zhou and J. Yu. “Digital signal processing for coherent optical communication”, in Wireless and Optical Communications Conference, 2009. WOCC 2009. 18th Annual, pp. 1 –5, may 2009.

[48] G. P. Agrawal. Nonlinear Fiber Optics. Academic Press, Fourth edition, 2006. ISBN 9780123695161.

[49] G. P. Agrawal. Lightwave Technology Telecommunication Systems. John Wily & sons, First edition, 2005. ISBN 978-0471215721.

[50] K. Nagayama, M. Kakui, M. Matsui, I. Saitoh, and Y. Chigusa. “Ultralow-loss (0.1484 db/km) pure silica core fibre and extension of transmission distance”, Electronics Letters, vol. 38, no. 20, pp. 1168 – 1169, sep 2002. doi:10.1049/el:20020824.

[51] S. V. Kartalopoulos. Optical Bit Error Rate: An Estimation Methodology. Wiley-IEEE Press, First edition, 2004. ISBN 0471615455.

[52] S. Huard. Polarization of Light. John Wily & sons, First edition, 1997.

[53] J.-P. Elbers, A. Farbert, C. Scheerer, C. Glingener, and G. Fischer. “Reduced model to describe SPM-limited fiber transmission in dispersion-managed lightwave systems”, Selected Topics in Quantum Electronics, IEEE Journal of, vol. 6, no. 2, pp. 276 –281, mar/apr 2000.

[54] X. Zhou and J. Yu. “Advanced coherent modulation formats and algorithms: higher-order multi-level coding for high-capacity system based on 100gbps channel”, in Optical Fiber Communication (OFC), collocated National Fiber Optic Engineers Conference, 2010 Conference on (OFC/NFOEC), pp. 1 –3, march 2010.

[55] M. Alfiad, D. van den Borne, S. Jansen, T. Wuth, M. Kuschnerov, G. Grosso, A. Napoli, and H. de Waardt. “A comparison of electrical and optical dispersion compensation for 111-Gb/s POLMUX-RZ-DQPSK”, Lightwave Technology, Journal of, vol. 27, no. 16, pp. 3590 –3598, aug.15, 2009.

[56] J. Leibrich and W. Rosenkranz. “Frequency domain equalization with minimum complexity in coherent optical transmission systems”, in Optical Fiber Communication (OFC), collocated National Fiber Optic Engineers Conference, 2010 Conference on (OFC/NFOEC), pp. 1 –3, march 2010.

[57] X. Zhang, D. Zibar, I. Monroy, and R. Younce. “Engineering rules for chromatic dispersion compensation in digital receivers for optical coherent PolMux QPSK links”, in IEEE Photonics Society, 2010 23rd Annual Meeting of the, pp. 598 –599, nov. 2010.

[58] R. Kudo, T. Kobayashi, K. Ishihara, Y. Takatori, A. Sano, and Y. Miyamoto. “Coherent optical single carrier transmission using overlap frequency domain equalization for long-haul optical systems”, Lightwave Technology, Journal of, vol. 27, no. 16, pp. 3721 –3728, aug.15, 2009.

[59] F. Gardner. “A BPSK/QPSK timing-error detector for sampled receivers”, Communications, IEEE Transactions on, vol. 34, no. 5, pp. 423 – 429, may 1986.

[60] D. Godard. “Self-recovering equalization and carrier tracking in twodimensional data communication systems”, Communications, IEEE Transactions on, vol. 28, no. 11, pp. 1867 – 1875, nov 1980.

[61] A. Viterbi. “Nonlinear estimation of PSK-modulated carrier phase with application to burst digital transmission”, Information Theory, IEEE Transactions on, vol. 29, no. 4, pp. 543 – 551, jul 1983.

[62] J. H. Lee and M. H. Sunwoo. “High-speed and low complexity carrier recovery for DP-QPSK transmission”, in Circuits and Systems (IS-CAS), 2011 IEEE International Symposium on, pp. 438 –441, may 2011.

[63] M. Secondini, E. Forestieri, and G. Prati. “Plc optical equalizer for chromatic and polarization-mode dispersion compensation based on mse control”, Photonics Technology Letters, IEEE, vol. 16, no. 4, pp. 1173 –1175, april 2004.

[64] M. Taylor. “Phase estimation methods for optical coherent detection using digital signal processing”, Lightwave Technology, Journal of, vol. 27, no. 7, pp. 901 –914, april1, 2009. doi:10.1109/JLT.2008.927778.

[65] J. Fabrega and J. Prat. “Digital phase estimation method based on Karhunen-Lo\`eve series expansion for coherent phase diversity detection”, in Optical Fiber Communication (OFC), collocated National Fiber Optic Engineers Conference, 2010 Conference on (OFC/NFOEC), pp. 1 –3, march 2010.

[66] M. Nakazawa, S. Okamoto, T. Omiya, K. Kasai, and M. Yoshida. “256-qam (64 gb/s) coherent optical transmission over 160 km with an optical bandwidth of 5.4 ghz”, Photonics Technology Letters, IEEE, vol. 22, no. 3, pp. 185 –187, feb.1, 2010.

[67] V. Arlunno, X. Zhang, K. Larsen, D. Zibar, and I. Monroy. “Digital non-linear equalization for flexible capacity ultradense wdm channels for metro core networking”, in Optical Communication (ECOC), 2011 37th European Conference and Exhibition on, pp. 1 –3, sept. 2011.

[68] T. Sugihara, T. Kobayashi, Y. Konishi, S. Hirano, K. Tsutsumi, K. Yamagishi, T. Ichikawa, S. Inoue, K. Kubo, Y. Takahashi, K. Goto, T. Fujimori, K. Uto, T. Yoshida, K. Sawada, S. Kametani, H. Bessho, T. Inoue, K. Koguchi, K. Shimizu, and T. Mizuochi. “43 Gb/s DQPSK pre-equalization employing 6-bit, 43GS/s DAC integrated LSI for cascaded ROADM filtering”, in Optical Fiber Communication (OFC), collocated National Fiber Optic Engineers Conference, 2010 Conference on (OFC/NFOEC), pp. 1 –3, march 2010.

[69] S. Gringeri, R. Egorov, B. Basch, G. Wellbrock, B. Zhang, C. Malouin, S. Liu, E. Ibragimov, S. Khatana, R. Lofland, R. Marcoccia, T. Schmidt, C. Pulikkaseril, M. Roelens, L. Fabiny, and S. Frisken. “Real-time 127-Gb/s coherent PM-QPSK transmission over 1000km NDSF with ¿10 cascaded 50GHz ROADMs”, in Optical Communication (ECOC), 2010 36th European Conference and Exhibition on, pp. 1 –3, sept. 2010.

[70] S. J. Savory. “Digital filters for coherent optical receivers”, Opt. Express, vol. 16, no. 2, pp. 804 –817, 2008.

[71] K. Horikoshi, E. Yamazaki, T. Kobayashi, E. Yoshida, and Y. Miyamoto. “Spectrum-narrowing tolerant signal-processing algorithm using maximum-likelihood sequence estimation for coherent optical detection”, Electronics Letters, vol. 47, no. 10, pp. 609 –611, 12 2011.

[72] T. Foggi, G. Colavolpe, E. Forestieri, and G. Prati. “Channel estimation algorithms for MLSD in optical communication systems”, Photonics Technology Letters, IEEE, vol. 18, no. 19, pp. 1984 –1986, oct.1, 2006.

[73] W. Chung. “Channel estimation methods based on volterra kernels for mlsd in optical communication systems”, Photonics Technology Letters, IEEE, vol. 22, no. 4, pp. 224 –226, feb.15, 2010. doi:10.1109/LPT.2009.2037726.

[74] M. M. Heinrich Meyr and S. A. Fechtel. Digital Communication Receiver-synchronization, channel estimation, and signal processing. John Wily & sons, First edition, 1998. ISBN 978-0-471-50275-3.

[75] A. Shalash and K. Parhi. “Comparison of discrete multitone and carrierless AM/PM techniques for line equalization”, in Circuits and Systems, 1996. ISCAS ’96., Connecting the World., 1996 IEEE International Symposium on, vol. 2, pp. 560 –563 vol.2, may 1996.

[76] A. Shalash and K. Parhi. “Three-dimensional carrierless AM/PM line code for the unshielded twisted pair cables”, in Circuits and Systems, 1997. ISCAS ’97., Proceedings of 1997 IEEE International Symposium on, vol. 3, pp. 2136 –2139 vol.3, jun 1997.

[77] A. Shalash and K. Parhi. “Multidimensional carrierless AM/PM systems for digital subscriber loops”, Communications, IEEE Transactions on, vol. 47, no. 11, pp. 1655 –1667, nov 1999.

[78] X. Tang, I.-J. Thng, and X. Li. “A new digital approach to design 3d cap waveforms”, Communications, IEEE Transactions on, vol. 51, no. 1, pp. 12 – 16, jan 2003. doi:10.1109/TCOMM.2002.807608.

[79] X.-L. Li and X.-D. Zhang. “A family of generalized constant modulus algorithms for blind equalization”, Communications, IEEE Transactions on, vol. 54, no. 11, pp. 1913 –1917, nov. 2006.

[80] C. Xie, G. Raybon, and P. Winzer. “Hybrid 224-Gb/s and 112-Gb/s PDM-QPSK transmission at 50-GHz channel spacing over 1200-km dispersion-managed LEAF spans and 3 ROADMs”, in Optical Fiber Communication Conference and Exposition (OFC/NFOEC), 2011 and the National Fiber Optic Engineers Conference, pp. 1 –3, march 2011.

[81] Y. Ma, Q. Yang, Y. Tang, S. Chen, and W. Shieh. “1-Tb/s singlechannel coherent optical OFDM transmission with orthogonal-band multiplexing and subwavelength bandwidth access”, Lightwave Technology, Journal of, vol. 28, no. 4, pp. 308 –315, feb.15, 2010.

[82] G. Gavioli, E. Torrengo, G. Bosco, A. Carena, S. Savory, F. Forghieri, and P. Poggiolini. “Ultra-narrow-spacing 10-channel 1.12 Tb/s D-WDM long-haul transmission over uncompensated SMF and NZDSF”, Photonics Technology Letters, IEEE, vol. 22, no. 19, pp. 1419 –1421, oct.1, 2010. doi:10.1109/LPT.2010.2062174.

[83] A. Patel, P. Ji, J. Jue, and T. Wang. “Survivable transparent flexible optical WDM (FWDM) networks”, in Optical Fiber Communication Conference and Exposition (OFC/NFOEC), 2011 and the National Fiber Optic Engineers Conference, pp. 1 –3, march 2011.

[84] A. Patel, P. Ji, J. Jue, and T. Wang. “Defragmentation of transparent flexible optical wdm (fwdm) networks”, in Optical Fiber Communication Conference and Exposition (OFC/NFOEC), 2011 and the National Fiber Optic Engineers Conference, pp. 1 –3, march 2011.

[85] S. Chandrasekhar, X. Liu, B. Zhu, and D. W. Peckham. “Transmission of a 1.2-tb/s 24-carrier no-guard-interval coherent ofdm superchannel over 7200-km of ultra-large-area fiber”, in Optical Communication,

2009. ECOC ’09. 35th European Conference on, vol. 2009-Supplement, pp. 1 –2, sept. 2009.

[86] G. Gavioli, E. Torrengo, G. Bosco, A. Carena, V. Curri, V. Miot, P. Poggiolini, M. Belmonte, F. Forghieri, C. Muzio, S. Piciaccia, A. Brinciotti, A. La Porta, C. Lezzi, S. Savory, and S. Abrate. “Investigation of the impact of ultra-narrow carrier spacing on the transmission of a 10-carrier 1Tb/s superchannel”, in Optical Fiber Communication (OFC), collocated National Fiber Optic Engineers Conference, 2010 Conference on (OFC/NFOEC), pp. 1 –3, march 2010.

[87] D. Zibar, R. Sambaraju, A. Caballero, J. Herrera, and I. Monroy. “Carrier recovery and equalization for photonic-wireless links with capacities up to 40 Gb/s in 75-110 GHz band”, in Optical Fiber Communication Conference and Exposition (OFC/NFOEC), 2011 and the National Fiber Optic Engineers Conference, pp. 1 –3, march 2011.

[88] G. Raybon, P. J. Winzer, A. A. Adamiecki, A. H. Gnauck, A. Konczykowska, F. Jorge, J.-Y. Dupuy, A. Sureka, C. Scholz, R. Delbue, P. J. Pupalaikis, L. L. Buhl, C. R. Doerr, S. Chandrasekhar, B. Zhu, and D. W. Peckham. “8x320 Gb/s transmission over 5600 km using all ETDM 80 Gbaud polarization multiplexed QPSK transmitter and coherent receiver”, in Optical Fiber Communication Conference and Exposition (OFC/NFOEC), 2012 and the National Fiber Optic Engineers Conference, pp. 1 –3, march 2012.

[89] X. Liu, S. Chandrasekhar, B. Zhu, P. Winzer, A. Gnauck, and D. Peckham. “448-Gb/s reduced-guard-interval CO-OFDM transmission over 2000 km of Ultra-Large-Area fiber and five 80-GHz-Grid ROADMs”, Lightwave Technology, Journal of, vol. 29, no. 4, pp. 483 –490, feb.15, 2011. doi:10.1109/JLT.2010.2084988.