---
layout: post
title:      "Digital Signal Processing Algorithms for High-Speed Coherent Transmission in Optical Fibers"
date:       2026-04-18 23:42:59
author:     "Bert"
tags:
  - DSP
  - Mineru
---

Universita degli studi di Padova \` Facolta di Ingegneria \`

Tesi di Laurea Specialistica in

Ingegneria delle Telecomunicazioni

# Digital Signal Processing Algorithms for High-Speed Coherent Transmission in Optical Fibers

Relatore

Candidato

Prof. Andrea Galtarossa

Marco Mussolin

Anno Accademico 2009/2010

Joy to the world! Hunter ”Patch” Adams

## Acknowledgements

There are so many people I would like to thank. Since I think it is impossible to thank them all, I apologies with all of those that are not mentioned.

First of all, my acknowledgment to my family that prompted me to applied for this experience that turn off like one of the best experience in my life and supported me during these amazing six months, thank you very much.

Another special thank you goes to my supervisor Andrea Galtarossa for proposing me this great opportunity that was really interesting and formative. Thank also for your kind help before, during and after my stay in Stockholm.

I would like to thank my industrial supervisor Marco Forzati for guiding and helping me every time I was stuck with my work. I have always felt home with you and during these six months in Acreo I had a great time. I will always be indebted and it was a pleasure working with you.

Many thanks also to Jonas M˚artensson, who was actually my second supervisor after Marco Forzati and Sergei Popov that played an important role between my Italian university and KTH.

After that, my special thanks to:

My girlfriend Angela for all the romantic moments spent in Stockholm. I

will never forget the first time I hugged you in Skavsta.

All the people I’ve met in Stockholm that made this experience wonderful. A piece of me will stay forever in Sweden. All the Italian (and acquired) friends in Kista. Paolo, Luigi, Daniel, Elisa, Stefano, Jessie, Valeria, Antonello, every Tuesday I’ll will think about you and Forno Romano. Thank you also for all the fun had together. A special thank you goes to Paola for putting me up in her place in my last Swedish week. All my Erasmus friends especially Bastien for all the football match played together (keep on training and maybe you will become stronger as me!); Alex, Arnau, Kathrin for all the dinner (in Kathrin’s kitchen) in Sundbyberg and for helping me in my last days without accommodation; Kuba for his specialty from Poland; Alicia for the parties in Bromma. Steffi, Sarah and Martina you left in December but we spent three months of great fun. A special thank you goes to Federico. You helped me really a lot in my first Swedish week and without you I would never met such a wonderful persons. Thank you also for all the crazy moment all around Stockholm. The Isotopes for all the matches played together. Everybody in Acreo and the students corner for all the fikas made together.

All my friend in Vicenza especially to the SanLore group guided by our leader Lush. Every time I was back to Italy it was amazing to find friends waiting for me.

CDSA members for all the wonderful time during these years of university.

The clowns of V.I.P. Clown Vicenza, since 2003 you are a special part of my life.

All my friend that visited me in Stockholm. Thank you for all the funny moments spent together.

I also would like to thank KGB, Ambassadeur, Soap Bar, Marie Laveau,

DKV, Nymble, Bl˚a D¨orren, Ica, Coop, SL, Skype and RayanAir.

## Introduction

Internship project was performed in the Transmission Group in Acreo AB under the supervision of Senior Scientist Marco Forzati.

## Acreo AB

Acreo AB was formed in 1999 by bringing together Swedish research institutes in the microelectronics and photonics area together. It has more than 150 employees in headquarter in Kista (Stockholm) and in two other regional offices. Acreo is owned by the group Swedish ICT Research AB. 60% of the latter is owned by Swedish Ministry for Industry and the rest is owned by the industry through consortium.

Acreo fulfills its mission by carrying out contract research and technical development. Acreo’s role is to bridge the gap between academic research and industrial commercialization.

## EURO-FOS network

The internship project was done in scope of EURO-FOS project. EURO-FOS is a Network of Excellence project and it was funded by the European Commission under the 7th Framework Program (FP7), Information and Communications Technologies (ICT). The aim of EURO-FOS is to create European network of research groups, who has proved to be leaders in the design, development and evaluation of photonic subsystems. EURO-FOS Network has several Centres of Excellence from which the Transmission Group of Acreo is involved in CE1: Digital Optical Transmission Systems. From the objectives of the Centre of Excellence on Digital optical Transmission Systems, we can mention the followings, which somehow coincide with the objectives of current internship project:

• to study the benefits of advanced modulation formats in combination with coherent detection and electronic distortion equalization to increase spectral efficiency and to reduce system complexity;

• analysis of techniques for electronic dispersion compensation and electronic mitigation of linear and non-linear transmission impairments;

• to study concepts of transmitter and receiver subsystems for 100 Gb/s systems;

• to study and analyze the implementation of subsystems for optical clock recovery.

One of the efficient ways of collaboration in the scope of EURO-FOS network is joint experiments, when experiments and results are open for all the collaborating groups. Especially during 2008 the experiments on QPSK modulation format for the Centre of Excellence on Digital optical Transmission Systems were done in Heinrich Hertz Institute (Germany) and Politecnico di Torino (Italy). For the current project it was decided to develop DSP algorithms targeted on the experiments performed in Politecnico di Torino.

## Abstract

Digital Signal Processing (DSP) is an indispensable technology for next generation 100 Gb/s optical coherent transmission system.

The aim of this thesis is to study DSP algorithms to compensate transmission impairments in a 100 Gb/s PolMux-QPSK coherent optical transmission system. The thesis can be divided in two parts: the first deals with testing different chromatic dispersion compensation techniques (Savory’s method, adaptive filters and frequency domain method) while the second part is focused on nonlinear transmission impairment compensation using a multispan backpropagation technique. Constant Modulus Algorithm butterfly structure and Viterby and Viterby methods are proposed for polarization de-multiplexingn and adaptive and for carries phase recovery. Results of the processing, presented in the last chapter, confirm that coherent detection at 100 $\mathrm { G b / s }$ will become feasible in the future using DSP for transmission impairments compensation.

## Contents

1 Optical fiber communications 1   
1.1 Signal propagation in optical fibers 2   
1.1.1 Attenuation . 2   
1.1.2 Chromatic dispersion 3   
1.1.3 Polarization mode dispersion . 5   
1.1.4 Nonlinear effect 6   
1.2 Data modulation 8   
1.3 Direct detection versus coherent detection 13   
2 Digital Signal Processing aided coherent optical detection 15   
2.1 Why Digital Signal Processing . 15   
2.2 Chromatic dispersion compensation 18   
2.2.1 Time domain technique . . 19   
2.2.2 Frequency domain technique . 24   
2.3 Polarization Mode Dispersion compensation 26   
2.4 Carrier phase recovery 29   
2.5 Nonlinear compensation 31   
3 Algorithm testing and results 33   
3.1 Chromatic dispersion compensation 33   
3.1.1 System setup 33   
3.1.2 Time domain methods 35   
3.1.3 Frequency domain method 39   
3.2 Nonlinear effects compensation 42   
3.2.1 System setup 42   
3.2.2 Single channel result 42   
3.2.3 Multichannel result . 44   
4 Conclusion and future work 47   
A DSP test code 53   
A.1 main.m . 53   
A.2 CD fil fde.m . 58   
A.3 overlap add.m . 60   
A.4 lms.m 62   
A.5 cma.m 63   
A.6 pmd cma samp.m 64   
A.7 CD fil.m 65   
A.8 phase compl.m 66   
A.9 CD and NLC 67

## List of Figures

1.1 Optical fiber attenuation 3   
1.2 Fiber imperfection[4] 5   
1.3 Perturbated fiber core[4] 5   
1.4 Impact of PMD on the propagating pulse . 6   
1.5 On-Off-keying constellation 8   
1.6 Binary PSK constellation . 9   
1.7 PSK-OOK transmitter using a Mach-Zehnder EAM optical   
modulator 9   
1.8 QPSK Grey coded constellation 10   
1.9 QPSK transmitter using a nested MZM modulator 11   
1.10 PolMux-QPSK block scheme . 12   
1.11 Evolution from PSK to POLMUX-QPSK[5] 12   
1.12 Schematic direct receiver 13   
1.13 Schematic coherent receiver[7] 14   
2.1 Transmission and DSP block scheme 16   
2.2 QPSK constellation from a PolMux-QPSK (section 1.2): (a)   
received data constellation diagram without DSP, (b) received   
data constellation diagram with DSP 17   
2.3 QPSK constellation from a PolMux-QPSK (section 1.2): (a)   
received data constellation diagram without DSP, (b) received   
data constellation diagram with only CD compensation 19   
2.4 Fir filter block . . 20   
2.5 Adaptive filter scheme 21   
2.6 LMS error evaluation 22   
2.7 FFT CD compensation algorithm scheme . 24   
2.8 Overlap add method 25   
2.9 Functionality of the digital filtering stage[6] 26   
2.10 QPSK constellation from a PolMux-QPSK (section 1.2): (a)   
received data constellation diagram before PMD compensa  
tion, (b) received data constellation diagram after PMD com  
pensation 28   
2.11 QPSK constellation from a PolMux-QPSK (section 1.2): (a)   
received data constellation diagram before carrier phase recov  
ery, (b) received data constellation diagram after carrier phase   
recovery 30   
2.12 Span[13] 31   
2.13 Nonlinear compensator[14] 32   
3.1 Schematic of 112 Gbit/s PM-QPSK coherent transmission sy  
stem 34   
3.2 OSNR required for BER of 10−3 versus the propagation dis  
tance using the Savory’s method . 36   
3.3 Number of taps required using the Savory’s method . . 36   
3.4 OSNR required for BER of 10−3 versus the propagation dis  
tance using CMA adaptive filter 37   
3.5 Number of taps required CMA adaptive filter 37   
3.6 OSNR required for BER of $1 0 ^ { - 3 }$ versus the propagation dis  
tance using Savory’s and CMA filters . 38   
3.7 FFT length in overlap add method 39   
3.8 OSNR required for BER of $1 0 ^ { - 3 }$ versus the propagation dis  
tance using FFT method . 40   
3.9 FFT length required versus the propagation distance . . . 40   
3.10 OSNR required for BER of $1 0 ^ { - 3 }$ versus the propagation dis  
tance using FFT method and CMA filter . . 41   
3.11 BER dependency on intra-polarization nonlinear parameter   
(α) and interpolarization parameter (β) . 43   
3.12 OSNR required for a bit error rate (BER) of $1 0 ^ { - 3 }$ versus the   
propagation distance with and without NLC . . . 44   
3.13 BER versus power launched in the fiber with and without NLC 45

## Chapter 1

## Optical fiber communications

With the increasing of global information exchange it’s becoming crucial to be able to transmit information over longer distance. An answer to this issue are optical fibers that are already used for most of the voice and data traffic all over the world.

Optical fibers are especially advantageous for long transmissions distance, because light propagates through the fiber with limited attenuation compared to electrical cables. The speed at witch the information in traveling along a single optical channel (bit rate) is limited by the speed of electronic components of the transmission system. However it’s possible to transmit several channels, at different wavelength, on the same medium using wave division multiplexing (WDM). This allows to reach a capacity system of several Tbit/s[1].

This chapter introduces to optical fiber communications. Section 1.1 discusses the main transmission impairment in high-speed transmission. In section 1.2, the modulation format used in data analyzed in section 3 is presented. Section 1.3 briefly reviews a comparison between direct detection and coherent detection.

## 1.1 Signal propagation in optical fibers

The goal of a communication system is to propagate a signal $A ( \mathrm { t , z } )$ from the transmitter to the receiver so that signal at the receiver $A ( \mathrm { t } , \mathrm { z } _ { e n d } )$ will be as similar to the transmitted one $A ( \mathrm { t } , 0 )$

The propagation of a light pulse in a optical fiber is described by the nonlinear Schro¨dinger equation (NLSE)[2]:

$$
j \frac { \partial A } { \partial z } = \frac { \beta _ { 2 } } { 2 } \frac { \partial ^ { 2 } A } { \partial t ^ { 2 } } - j \frac { \alpha } { 2 } A - \gamma | A ^ { 2 } | A ,\tag{1.1}
$$

A is the electric field, α is the attenuation coefficient, $\beta _ { 2 }$ is the dispersion parameter, $\gamma$ is the nonlinear coefficient, z and t are the propagation direction and time, respectively[3]. Each of the three terms on the right side of Eq. 1.1 describe impairments that cause signal distortion and need to be compensated for if error-free transmission is to be achieved.

## 1.1.1 Attenuation

Attenuation causes the power level of the signal to decrease while propagating and optical amplifiers are used for compensate for this power loss. The price to pay is that this introduces noise and increases the system cost.

Removing the effect of chromatic dispersion and Kerr nonlinearity the Eq. 1.1 can be solved and gives:

$$
| A ( t , z ) | ^ { 2 } = | A ( t , 0 ) | ^ { 2 } e ^ { - \alpha z } ,\tag{1.2}
$$

α is the attenuation constant and it’s measured in $\mathrm { m } ^ { - 1 }$ but usually it’s referred as $\alpha _ { d B }$ defined as:

$$
\alpha _ { d B } = 4 . 3 4 3 \cdot \alpha .\tag{1.3}
$$

There are different values of attenuation depending on the optical frequency range that can be divided in three window:

![](images/671b5359d83721bc6310e7358211b35dc40cca5b79ba09e68de9654a40444b76.jpg)  
Fig. 1.1: Optical fiber attenuation

• first window centered around 850 nm with typical value of attenuation of 2 to 3 dB/km;

• second window centered around 1300 nm with typical value of attenuation of 0.4 to 0.5 dB/km;

• third window around 1550 nm with attenuation of 0.2 to 0.25 dB/km.

## 1.1.2 Chromatic dispersion

Chromatic dispersion (CD) is due to propagation speed of light being a function of wavelength, so that the different spectral components of signal show a relative delay causing signal distortion.

Ignoring the nonlinearity and the attenuation in Eq. 1.1 the resulting system becomes linear and we can write the expression that shows the effects of CD on the envelope A(z,t):

$$
\frac { \partial A ( z , t ) } { \partial z } = - j \frac { \beta _ { 2 } } { 2 } \frac { \partial ^ { 2 } A ( z , t ) } { \partial t ^ { 2 } } ,\tag{1.4}
$$

where z is the propagation distance, t is time variable, and $\beta _ { 2 }$ is the groupvelocity dispersion (GVD), often called simply dispersion.

The group-velocity is the traveling speed of a light pulse in the fiber and it is a function of $\omega$ therefore different spectral components of the signal travel with different group velocity.

Solving analytically Eq. 1.4 in the Fourier domain gives:

$$
A ( z , \omega ) = A ( 0 , \omega ) e ^ { j \frac { \beta _ { 2 } } { 2 } \omega ^ { 2 } z } .\tag{1.5}
$$

It can be seen that in the frequency domain the chromatic dispersion introduces a distortion on the phase of the signal spectrum without changing the spectral power distribution and at the end of the propagation the pulse result broadened.

The GVD parameter $\beta _ { 2 }$ gives the time delay between two different spectral component separated by a certain frequency interval and it has units $\mathrm { s } ^ { 2 } \mathrm { m } ^ { - 1 }$ . Usually the dispersion is measured with the dispersion coefficient D defined as:

$$
D = - { \frac { 2 \pi c } { \lambda ^ { 2 } } } \beta _ { 2 } ,\tag{1.6}
$$

where $\lambda = - 2 \pi c / \omega$ is the carrier wavelength and $c$ is the speed of light. D gives the time delay between two different spectral component separated by a certain wavelength interval and it has units ps/nm/km.

It is possible to define a dispersion length defined as the propagation distance after a Gaussian pulse is broadened by 40%:

$$
L _ { D } = \frac { \tau _ { p } ^ { 2 } } { \left| \beta _ { 2 } \right| } ,\tag{1.7}
$$

where $\tau _ { p }$ is the pulse half width[1].

## 1.1.3 Polarization mode dispersion

As in long-haul link standard single mode fiber (SSMF) are used, the propagating filed is described as a single mode consisting of two degenerate modes each corresponding of two orthogonal polarizations. The degeneration is due to the cylindrical symmetry of the optical fiber. However real optical fibers have a physical structure that is not perfectly cylindrical to core imperfections and perturbations due to mechanical tension, thermal gradients etc.

![](images/30087b86e2e47c83e977b015ade08955b9c3f9eef969709ac8535ef9bb815729.jpg)  
Fig. 1.2: Fiber imperfection[4]

![](images/429b47d24d1cc1e3b83a6611b707ae8ba7fc4c6b00a0cbd2cdd1a259e04c98b2.jpg)  
Fig. 1.3: Perturbated fiber core[4]

Due to these imperfections, the two fundamental modes see different effective indexes of refraction (Fig. 1.3) and optical fibers acquire birefringence meaning that the two polarization modes are propagating with slightly different group velocity. The state of polarization varies during the propagation. The polarization state is dependent on the wavelength and evolves with propagation at the end of the link, the two pulse components with different polarizations will arrive with a relative delay called Differential Group Delay (DGD) (Fig. 1.4).

![](images/b9ad54fde8fc466a27665208f85067708dceca66a282cc0ca284977e6139afc7.jpg)  
Fig. 1.4: Impact of PMD on the propagating pulse

This phenomenon is called Polarization Mode Dispersion(PMD). It’s stochastic as a consequence of the random nature of its origin. The total DGD is given by:

$$
\sigma ( z ) = D _ { g } { \sqrt { z } } ,\tag{1.8}
$$

where $D _ { g }$ is the PMD coefficient and its typical value is in the range between 0.1 and 1 ps/km.

## 1.1.4 Nonlinear effect

The response of any dielectric to light becomes nonlinear with the increasing of the intensity of electromagnetic fields and optic fibers, made of silica,

behave this way. The origin of the non linear response comes from the interaction of the electromagnetic field with silica electrons.

Solving the 1.1 in absent of dispersion $( \beta _ { 2 } = 0 )$ we obtain:

$$
A ( t , z ) = A ( t , 0 ) e ^ { j \phi _ { N L } ( t , z ) } ,\tag{1.9}
$$

$\phi _ { N L } ( t , z )$ the nonlinear phase shift is given by:

$$
\phi _ { N L } ( t , z ) = \gamma P _ { 0 } | A ( t , 0 ) | ^ { 2 } \frac { 1 - e ^ { \alpha z } } { \alpha } ,\tag{1.10}
$$

where $P _ { 0 }$ is related with the pulse peak. The Eq. 1.10 shows that the amplitude introduces a nonlinear phase shift. This phenomenon is called self-phase modulation (SPM) and, in frequency domain, it brings a widening of the spectrum while the shape pulse remain unchanged. If the system uses a Wavelength Division Multiplexing (WDM), several signals are transmitted at different wavelengths and the one wavelength signal $A ( t , 0 )$ is affected by other nonlinear shifts duded to the neighbor channels. This phenomenon is called cross-phase modulation (XPM). The presence of different wavelength channels can also generate new frequencies as the four-wave mixing (FWM). Generally these effects can be divided in two categories: intra-channel and inter-channel nonlinear effects. The first deals with the nonlinear effects of a single channel on itself while the second deals with the effects due to neighbor channels.

## 1.2 Data modulation

In modern telecommunications system information is stored and transmitted as digital data represented by symbols chosen from a finite alphabet. Digital data modulations consist in associating every symbols value to a particular signal state. In binary transmission only two symbol values are allowed, 0 and 1. In an optical transmission data modulation encode the information over an optical signals using intensity, phase or frequency[1]. In this section is a brief introduction the modulation formats.

## Amplitude-shift keying

Amplitude-shift keying (ASK) is a form of modulation that uses the amplitude of the carrier wave to represent the digital data. While frequency and phase are kept constant, the amplitude varies according with the bit stream. For binary transmission the level of amplitude can be used to represent binary logic 0s and 1s (Fig. 1.5). We can think of a carrier signal as an ON or OFF switch. In the modulated signal, logic 0 is represented by the absence of a carrier, thus giving OFF/ON keying operation and hence the name On-Offkeying (OOK) given.

![](images/2d34f9501ec3ffd58b453146377a40789c5e6e70251366f07c007490c7418544.jpg)  
Fig. 1.5: On-Off-keying constellation

## Phase-shift keying

Using phase shift keying (PSK) the information is stored on the phase of the transmitted signal. Some of the advantages introduced by the modulation format is a better tolerance to noise at the receiver (receiver sensitivity) as well as the increasing of the spectral efficiency and the dispersion tolerance compared to On-Off keying (OOK)[1]. Figure 1.6 shows a Binary PSK (BPSK) constellation where the phase is digitally mapped in the two allowed phase states (0, π). The constellation can be obtained using a Mach-Zehnder EAM optical modulator that generates a PSK signal when driven by a single drive signal (Fig. 1.7).

![](images/65c981e5115f03b1ed3ef9cfe9e2cd0d2b7688af17dddf950b81534584c617dc.jpg)  
Fig. 1.6: Binary PSK constellation

![](images/a6bf93761414e80faeba99071eb2fdc7a316a00727a18aeabaf2a702142ba8a5.jpg)  
Fig. 1.7: PSK-OOK transmitter using a Mach-Zehnder EAM optical modulator

## Quadrature phase-shift keying

Sometimes known as quaternary or quadriphase PSK (QPSK), QPSK uses four points on the constellation diagram, equispaced around a circle on four phase value $( 0 , { \frac { \pi } { 2 } } , \pi , - { \frac { \pi } { 2 } } )$ . With four phases, QPSK can encode two bits per symbol (Fig. 1.8). This may be used either to double the data rate compared to a BPSK system while maintaining the bandwidth of the signal or to maintain the data-rate of BPSK but halve the bandwidth needed. Usually QPSK is implemented using a nested Mach-Zender modulator (MZM) structure (Fig. 1.9) where complex field is modulated both in-phase and quadrature direction.

![](images/6350d573e95e80256ec3c45d432882bbe82fb08e0388f9b6728cb10df676a467.jpg)  
Fig. 1.8: QPSK Grey coded constellation

## Polarization shift keying

In polarization shift keying (PolSK) the signal is encoded using the signal polarization state. A bit value 0 could be represented by a horizontal polarized signal and a bit value 1 by a vertical polarized signal. However, the polarization rotate randomly during the propagation of the optical field as explained in section 1.1.3. This problem limits the system performance especially for high power when non linear effects become stronger but can be compensated electronically with proper algorithms. It makes more sense to use the polarization degree of freedom to transmit two orthogonal polarized channels. An example of this is PolMux-QPSK that will described below.

![](images/fdd7f544846711d59acb414f4c291e9e726c45d0effd0fd1f1c2c967f004a3fb.jpg)  
Fig. 1.9: QPSK transmitter using a nested MZM modulator

## Polarization multiplexing of QPSK

Polarization multiplexing of QPSK (PolMux-QPSK) is the modulation format of the data analised in section 3. PolMux-QPSK is implemented using two MZMs and then the two QPSK signals are combined with a Polarization Beam Combiner (PBC) (Fig. 1.10). PolMux-QPSK helps to reduce the requirements on electrical and opto-electrical components because it requires half the baud rate needed by a QPSK (Fig. 1.11).

![](images/bf1056e0d0060975a23e4ea534bc77dfce86d8048fccdb5ebd00c0d42ed7cf5b.jpg)  
Fig. 1.10: PolMux-QPSK block scheme

![](images/01f16dd76ebcde3e2ba825867b8e8d0077a61abc9cac9e8a740e3599b9cec90f.jpg)  
Fig. 1.11: Evolution from PSK to POLMUX-QPSK[5]

## 1.3 Direct detection versus coherent detection

In direct detection, in an optoelectrical photodetector (a photodiode) the light intensity $| E | ^ { 2 }$ is converted in an electrical signal and the phase information is totally lost (Fig. 1.12). An alternative way to detect the optical signal is coherent detection in which the received signal is mixed with local laser being detected in the photodiode, and two detectors and proper phase delays are used (as explained below), both amplitude and phase can be preserved. While coherent detection was experimentally demonstrated as early 1979, its use in commercial systems has been hindered by the additional complexity, due to the need to track the phase and the polarization of the incoming signal (Fig. 1.13). In a digital coherent receiver these functions are implemented in the electrical domain leading to a dramatic reduction in the complexity of the optical receiver[6].

![](images/857f982cccdd97dca9a5895258d014d960a0782931085a6af3dd0dd03f55c378.jpg)  
Fig. 1.12: Schematic direct receiver

Since coherent detection maps both the intensity and the phase of the optical field into the electrical domain therefore maintaining all the information it maximizes the effectiveness of the signal processing. This allows impairments which have traditionally limited 100 Gb/s single channel systems to be overcome, since both chromatic dispersion and polarization mode dispersion may be compensated adaptively using linear digital filters.

![](images/321e7df38d9c7406577c3873301b6f50fa487fea876ad7b96c96d59f5589656f.jpg)  
Fig. 1.13: Schematic coherent receiver[7]

## Chapter 2

## Digital Signal Processing aided coherent optical detection

This chapter introduces the concept of Digital Signal Processing in optical communications. Section 2.1 briefly explains why Digital Signal Processing it’s becoming a need in long-haul optical fiber system. In section 2.2, 2.3 and 2.4 linear transmission impairments compensation techniques are presented, finally section 2.5 reviews a nonlinear effects compensator.

## 2.1 Why Digital Signal Processing

An important goal of a long-haul optical fiber systems is to transmit the highest data throughput over the longest distance without signal regeneration. Digital signal processing (DSP) is used at the receiver to remove the need for dynamic polarization control and also to compensate for linear (and some extent of non linear) transmission impairments[7].

An optical transmission system can be represented as shown in Fig. 2.1 where $E _ { T X }$ is the transmitted signal, H(ω) is the channel transfer function and $E _ { R X }$ is the received signal. The goal of DSP is to implement $H ^ { - 1 } ( \omega )$ that can be interpreted as the combination of all the linear effects that affect the signal during the propagation, and estimate $\hat { E } _ { T X }$ that represents the processed signal. In order to compensate all these effects, the received sampled electrical signal is elaborated with a series of algorithms in order to minimize the bit error rate (BER) that represents the main evaluation criterion for digital communication system quality. Another evaluation factor is the so called Constellation Plots or Diagrams (Fig. 2.2), a scatter plot of the modulated signal, amlitude and phase, in a two dimensional complex plane.

![](images/55cda79c022583e6d0f205ae795217e00a205f2a54e79b3b6701bb1b77c8640e.jpg)  
Fig. 2.1: Transmission and DSP block scheme

![](images/d9536e2a5674277c9790e85d91c8740ff897a80f7495caec6a2ee3d9ab91294f.jpg)

![](images/6470e24866fd42e673fa8b6e47ea5a7f225ede655a3c6ed559fba1e6d7459112.jpg)  
Fig. 2.2: QPSK constellation from a PolMux-QPSK (section 1.2): (a) received data constellation diagram without DSP, (b) received data constellation diagram with DSP

## 2.2 Chromatic dispersion compensation

Chromatic dispersion is one of the main limitation to long-haul direct detection optical fiber system. Its effect of broadening the pulse during propagation (see section 1.1.2) is extremely constraining if not compensated. A commonly adopted solution is the use of Dispersion-Compensating Fiber (DCF), however DCF introduces additional loss, therefore requiring additional optical amplifiers that increase noise and cost of the system. An alternative approach is to compensate entirely CD in the electric domain. At the beginning, equalization with training sequence was used but it was demonstrated that this method is good only for low dispersion system, as real system has a relative high CD, or system with DFC and residual CD[8]. A way to solve these problems is to deduce the needed equalized directly from the physics. As noted by Haykin ”Signal processing is at its best when it successfully combines the unique ability of mathematics to generalize with both the insight and prior information gained from the underlying physics of the problem at hand”[9].

From Eq. 1.4 we can rewrite the expression of the effect of chromatic dispersion on the envelope $A ( \mathrm { z , t } )$ :

$$
\frac { \partial A ( z , t ) } { \partial z } = j \frac { D \lambda ^ { 2 } } { 4 \pi c } \frac { \partial ^ { 2 } A ( z , t ) } { \partial t ^ { 2 } } ,\tag{2.1}
$$

Solving Eq. 2.1 in the frequency domain it gives:

$$
A ( z , \omega ) = A ( 0 , \omega ) e ^ { - j \frac { D \lambda ^ { 2 } } { 4 \pi c } \omega ^ { 2 } z } .\tag{2.2}
$$

The frequency domain transfer function $G ( \mathbf { z } , \omega )$ can be obtained from Eq. 2.2[6]:

$$
G ( z , \omega ) = e ^ { - j { \frac { D \lambda ^ { 2 } } { 4 \pi e } } \omega ^ { 2 } z } ,\tag{2.3}
$$

where $\omega$ is the angular frequency. Using Fourier transforms Eq. 2.3 the filter in time domain can be obtain[6]:

$$
g ( z , t ) = \sqrt { \frac { c } { j D \lambda ^ { 2 } z } } e ^ { j \frac { \pi e } { D \lambda ^ { 2 } z } t ^ { 2 } }\tag{2.4}
$$

From theory, filters for dispersion compensation in frequency and time domains can be obtained inverting the sign of the chromatic dispersion in Eq. 2.3 and Eq. 2.4. Fig. 2.3 shows the effect of CD on a QPSK constellation diagram.

In the next section time domain techniques will be presented then in section 2.2.2 frequency technique will be analyzed.

![](images/66b91c4dccb2ce89dcfdf9ee89b6ae8d1463caa26a6fdcf126cae2a8620d27d8.jpg)

![](images/9be6ca550336c4c5e62dfb7e3cffc128b73068eaa789da1f878aed10af9e8201.jpg)  
Fig. 2.3: QPSK constellation from a PolMux-QPSK (section 1.2): (a) received data constellation diagram without DSP, (b) received data constellation diagram with only CD compensation

## 2.2.1 Time domain technique

In time domain filtering corresponds to convolution operation which can be performed in digital domain by Finite Impulse Response (FIR) filter[10]. The schematic representation of it is in Fig. 2.4 and the formula for FIR filter is:

$$
y ( n ) = b _ { 0 } x ( n ) + b _ { 1 } x ( n - 1 ) + . . . + b _ { N } x ( n - N )\tag{2.5}
$$

where x is the input signal, $b _ { i }$ are the filter weights or as it is also called tap weights, N is the filter length and y is the output.

![](images/a2cba7cefa33062293908c27148198b51d65a101df6eb18e5b54bc55b98d00c3.jpg)  
Fig. 2.4: Fir filter block

Two different time domain techniques for CD compensation were analyzed: Savory’s method and blind adaptive equalizer such as least mean square (LMS) and constant modulus algorithm (CMA) algorithms.

## Savory’s method

In order to implement the CD filter in time domain (see the Matlab code in A.7), formulas should be derived for tap weights. As S.Savory demonstrated[6], expressions for tap weights and filter length come from Eq. 2.4 by truncating the impulse response to a finite duration. Since it is finite we can implement this digitally using a FIR filter where the number of the taps and the amplitude can be calculated using the formula:

$$
a _ { k } = \sqrt { \frac { j c T ^ { 2 } } { D \lambda ^ { 2 } z } } e ^ { - j \frac { \pi c T ^ { 2 } } { D \lambda ^ { 2 } z } k ^ { 2 } } ,\tag{2.6}
$$

with

$$
- \left\lfloor { \frac { N } { 2 } } \right\rfloor \leq k \leq \left\lfloor { \frac { N } { 2 } } \right\rfloor ,\tag{2.7}
$$

and

$$
N = 2 \times \left\lfloor \frac { | D | \lambda ^ { 2 } z } { 2 c T ^ { 2 } } \right\rfloor + 1 ,\tag{2.8}
$$

where N is the number of taps, $T$ is the sampling period and bxc is the integer part rounded toward $- \infty$

## Adaptive filters

An adaptive algorithm incorporates an iterative procedure (Figure 2.5) that makes successive corrections to the weight of the filter in order to minimize the mean error between the output $\hat { d } ( \mathrm { n } )$ and the desired symbol d(n). An extremely important parameter is the step size $\mu$ that is linked with the filter taps weight uploading. High value of $\mu$ means faster convergence but lower precision. On the other hand low value of $\mu$ bring to slower convergence but higher precision. A good compromise is the use of high value of $\mu$ to initialize the filters taps and then switch to a low value to get an accurate precision. Least mean square (LMS) algorithm and constant modulus algorithm (CMA)[11] will be presented in the next sections.

![](images/949e9a7b492703db8bddd522a855324b7a6c13ee5defce38596a44729bd7e88d.jpg)  
Fig. 2.5: Adaptive filter scheme

LMS method

Notation:

$$
x ( n ) \qquad { \mathrm { i n p u t } }\tag{2.9}
$$

$$
w ( n ) \mathrm { f i l t e r t a p w e i g h t s }\tag{2.10}
$$

$$
d ( n ) \qquad { \mathrm { d e s i r e d ~ r e s p o n s e } }\tag{2.11}
$$

$$
y ( n ) = \sum _ { K = 0 } ^ { \infty } w _ { k } ^ { * } x ( n - k )\tag{2.12}
$$

$$
\begin{array} { r l } { = } & { { } w ^ { H } ( n ) x ( n ) } \end{array}\tag{2.13}
$$

$$
\mathrm { { f i l t e r \ o u t p u t } }
$$

$$
e ( n ) = d ( n ) - y ( n )\tag{2.14}
$$

$$
\mathrm { e r r o r e s t i m a t i o n }
$$

$$
w ( n + 1 ) = w ( n ) + \mu * x ( n ) * e ^ { * } ( n )\tag{2.15}
$$

$$
\mathrm { \ u p l o a d i n g \ e q u a t i o n }
$$

![](images/c87946a96715337503118c80936d474e60e294d701d04d9eeaee0a3d2357c94c.jpg)  
Fig. 2.6: LMS error evaluation

At every step the algorithm (see the Matlab code in A.4) uploads the filter weight following the Eq. 2.15 and it estimates the error comparing the output at the step n with the desired response d(n) using a directed decision method (Fig. 2.6). The filter tap weights should be initialized. A solution is to set all the taps weight to zero except the central one that is set to unity corresponding to no filtering[6].

CMA method

Notation:

$$
x ( n ) \qquad \mathrm { i n p u t }\tag{2.16}
$$

$$
w ( n ) \mathrm { f i l t e r t a p w e i g h t s }\tag{2.17}
$$

$$
y ( n ) = \sum _ { K = 0 } ^ { M - 1 } w _ { k } ^ { * } x ( n - k )\tag{2.18}
$$

$$
\begin{array} { r l } { = } & { { } w ^ { H } ( n ) x ( n ) } \end{array}\tag{2.19}
$$

$$
\mathrm { { f i l t e r \ o u t p u t } }
$$

$$
\begin{array} { l l l } { { e ( n ) } } & { { = } } & { { 1 - | y ( n ) | ^ { 2 } } } \end{array}\tag{2.20}
$$

$$
\mathrm { e r r o r e s t i m a t i o n }
$$

$$
\begin{array} { r c l } { w ( n + 1 ) } & { = } & { w ( n ) + \mu * x ^ { * } ( n ) * e ( n ) * y ( n ) } \end{array}\tag{2.21}
$$

$$
\mathrm { \ u p l o a d i n g \ e q u a t i o n }
$$

After CD compensation for phase modulation signals the amplitude of the symbols is constant. For this reason the error is calculated imposing a constrain on the intensity (Eq. 2.20) and not using direct decision as in LMS case. As CMA doesn’t take any decision, it brings better performance in terms of convergence than LMS as results will show in section 3. The taps weight are initialized as the LMS case.

## 2.2.2 Frequency domain technique

## Fast Fourier Transform method

In frequency domain the filtering of the input stream is obtained by multiplication operation. The formula for the digital filter weights in frequency domain can be obtained from Eq. 2.3:

$$
f _ { k } = e ^ { j { \frac { D \lambda ^ { 2 } } { 4 \pi c } } z \omega _ { k } ^ { 2 } }\tag{2.22}
$$

where $\begin{array} { r } { \omega _ { k } = \frac { 2 \pi } { T L _ { F F T } } , L _ { F F T } } \end{array}$ is the Fast Fourier Transform (FFT) length and $T$ is the sampling period (see the Matlab code in A.2). As the frequency domain

![](images/95c302966ff7accd5111b121bb77e371d8fae1dbcb011214b4cecb4472e4c09c.jpg)  
Fig. 2.7: FFT CD compensation algorithm scheme

compensation uses the FFT function it is not advantageous working with long sequence of data because it increases the complexity of the algorithm. The received data should be split in smaller windows but connecting directly different blocks after the compensation results in errors at the edges. For that reason the overlap-add method is used. The overlap-add method has this procedure[10]:

• decompose the received signal into smaller windows;

• each window is padded on the both side (grey part in Fig. 2.8) with a sequence of zero (zero-padding technique);

• the portion of the signal enters in the scheme shown in Fig. 2.7. FFT, multiplication with the filter and inverse Fast Fourier Transform (IFFT) is made;

![](images/d943f75299951f909b5553508e7836fff8df9a794d6f4b05620131202bb92725.jpg)  
Fig. 2.8: Overlap add method

• the windows are recomposed overlapping the grey part as showed in the Fig. 2.8.

There are two crucial parameters in this method: the FFT length (that is equal to the filter length) and the zero padding length. The FFT length must be long enough to allow the compensation of the chromatic dispersion accumulated during the fiber propagation and, as FFT algorithm is defined, it must be a power of two. The zero padding length is related to the dispersive effect on the samples at the edge of the windows in which the signal is split. If the padding is not long enough the filtered portion of data will exceed the time window and this will rise to aliasing. If L is the number of samples of each window and G is the total overlap length (G/2 at the beginning of the window and G/2 at the end), we fix L = F F T length−G with $\begin{array} { r } { G = \frac { F F T l e n g t h } { 2 } } \end{array}$ (see matlab code in A.2).

One issue of our investigation was the calculation of the FFT length and the zero padding length that guaranties a right value of BER. The results will be presented in section 3.1.

## 2.3 Polarization Mode Dispersion compensation

Polarization tracking (section 1.3) can be archive using an adaptive CMA butterfly structure (see the Matlab code in A.6)[6][7]. The structure is com-

![](images/1fbe112c9fc1e11827d96737cbb83319c5d8a23e6efb1ab81980f7456373a8fd.jpg)  
Fig. 2.9: Functionality of the digital filtering stage[6]

posed by four CMA adaptive filters $( h _ { x x } , h _ { y x } , h _ { x y }$ and $h _ { y y } )$ related each other by these formulas:

$$
\begin{array} { r c l } { h _ { x x } } & { = } & { h _ { x x } + \mu \cdot e _ { x } \cdot x _ { o u t } \cdot x _ { p } ^ { * } } \end{array}\tag{2.23}
$$

$$
\begin{array} { r c l } { h _ { x y } } & { = } & { h _ { x y } + \mu \cdot e _ { x } \cdot x _ { o u t } \cdot y _ { p } ^ { * } } \end{array}\tag{2.24}
$$

$$
\begin{array} { r c l } { h _ { y x } } & { = } & { h _ { y x } + \mu \cdot e _ { y } \cdot y _ { o u t } \cdot x _ { p } ^ { * } } \end{array}\tag{2.25}
$$

$$
\begin{array} { r c l } { h _ { y y } } & { = } & { h _ { y y } + \mu \cdot e _ { y } \cdot y _ { o u t } \cdot y _ { p } ^ { * } } \end{array}\tag{2.26}
$$

where $x _ { o u t }$ and $y _ { o u t }$ are given by:

$$
\begin{array} { r c l } { x _ { o u t } } & { = } & { h _ { x x } ^ { T } \cdot x _ { p } + h _ { x y } ^ { T } \cdot y _ { p } } \end{array}\tag{2.27}
$$

$$
\begin{array} { l l l } { y _ { o u t } } & { = } & { h _ { y x } ^ { T } \cdot x _ { p } + h _ { y y } ^ { T } \cdot y _ { p } } \end{array}\tag{2.28}
$$

$e _ { x }$ and $e _ { y }$ are the errors defined as:

$$
\begin{array} { r c l } { e _ { x } } & { = } & { 1 - | x _ { o u t } | ^ { 2 } } \end{array}\tag{2.29}
$$

$$
\begin{array} { r c l } { e _ { y } } & { = } & { 1 - | y _ { o u t } | ^ { 2 } } \end{array}\tag{2.30}
$$

Filters are initialized with all the tap weights to zero except for the central tap of $h _ { x x }$ and $h _ { y y }$ that are set to the unity[6]. As the equalizer is free from any constrain and it could happen that the equalizer converge to the same output (singularity problem). To avoid this it is possible to initialize $h _ { x x }$ and $h _ { x y }$ and run the algorithm then $h _ { y y }$ and $h _ { y x }$ can be set using the result obtained[12]:

$$
\begin{array} { r c l } { h _ { y y } ( t ) } & { = } & { h _ { x x } ^ { * } ( - t ) } \end{array}\tag{2.31}
$$

$$
\begin{array} { r c l } { h _ { y x } ( t ) } & { = } & { - h _ { x y } ^ { * } ( - t ) } \end{array}\tag{2.32}
$$

As during the first stage of CD compensation some residual CD could not be compensated this algorithm takes care of it. Fig. 2.10 shows the differences, on a QPSK constellation, with and without PMD compensation after the first stage of CD compensation.

![](images/650eca6e50bfa9470402d867430dfdbb66c1ad18f3e6c07fd3c05888b1b12db2.jpg)

![](images/0762146a2a59e26af043373861e525bd7bac5c5361b9cddd599b1d818ef02173.jpg)  
Fig. 2.10: QPSK constellation from a PolMux-QPSK (section 1.2): (a) received data constellation diagram before PMD compensation, (b) received data constellation diagram after PMD compensation

## 2.4 Carrier phase recovery

The local oscillator at the receiver runs at a frequency which is only nominally equal to the transmitter laser. The relative small offset in frequency causes the detected signal to accumulate a phase error. This is taken care in the DSP by carrier phase recovery or phase noise compensation. During this step frequency and phase offset between local oscillator and signal is compensated using a ”Viterby-and-Viterby” carrier phase estimation (CPE) method (see Matlab code in A.8) as it has been used by Chris R. S. Fludger[8]. Power of four is used to remove the quaternary phase modulation and for each symbols the phase shift value is averaged with the neighbors on both side using a sliding window of length N . The formula for the phase shift is:

$$
\hat { \phi } ( k ) = a r g \left( \sum _ { n = - N } ^ { N } x ^ { 4 } ( k + n ) \right)\tag{2.33}
$$

where $\hat { \phi } ( k )$ is the phase correction that has to be applied to the symbol k.

When the spontaneous emissions (ASE) are dominant in the system, N should be higher to average the Gaussian noise and optimize the phase shift estimation. On the other hand in presence of higher phase noise a smaller number of N is preferred as it permits to follow change in phase with more precision. In all the simulations an optimization of N was performed.

Fig. 2.11 shows the differences, on a QPSK constellation, with and without carrier phase recovery after CD and PMD compensation.

![](images/904d6e2833398c6764e8198e954de0d9af8ae6f100ddf265865934ae981c3d96.jpg)  
Fig. 2.11: QPSK constellation from a PolMux-QPSK (section 1.2): (a) received data constellation diagram before carrier phase recovery, (b) received data constellation diagram after carrier phase recovery

## 2.5 Nonlinear compensation

As explained in section in section 1.1.4, nonlinear effects become an important constrain as power increases. Eq. 1.9 and 1.10 show that the nonlinear phase shift is proportional to the signal intensity.

Nonlinear effects can be compensated using the received intensity. The results that will be presented in section 3.2 were obtained using a nonlinear compensator (NLC) based on the technique of multi-span back-propagation (see Matlab code in A.9)[13]. In long-haul transmission systems the signal is periodically amplified throughout transmission to compensate for fiber loss. The optical link is therefore composed by a number of span (Fig. 2.12) made by an optical amplifier, Erbium Doped Fiber Amplifier (EDFA), followed by an optical fiber. It can be approximated that nonlinearities are concentrated just after the optical amplifiers where the power is higher. In this method we simplify things further by assuming that the nonlinear shift takes place instantaneously at the fiber input. Therefore the method consists in compensating for the CD accumulated during the span first and then treat the nonlinear effects.

![](images/08c36f7c5875a00470562f389d27b26889ad90ce4132afa32d36fda43ac60e43.jpg)  
Fig. 2.12: Span[13]

These steps are then repeated for each span. The structure of the filter is a FIR filter for the CD compensation followed by a butterfly NLC structure called NLC core as showed in the figure 2.13 a).

![](images/9333708af44d9f2f3c5e39127d1be41f95b2244e033a3da50db1535c8dcb042e.jpg)

![](images/722549eeb9e4c4fc473a42cedc13a522d983f7137f0431278991392ba501a1a1.jpg)  
Fig. 2.13: Nonlinear compensator[14]

The NLC, presented by T. Tanimura [14], introduces a phase shift on both of the digital streams according to these formulas, as represented by Fig. 2.13 b):

$$
E _ { x } ^ { o u t } = E _ { x } ^ { i n } e ^ { - j \left( \alpha I _ { x } + \beta I _ { y } \right) }\tag{2.34}
$$

$$
E _ { y } ^ { o u t } = E _ { y } ^ { i n } e ^ { - j \left( \alpha I _ { x } + \beta I _ { y } \right) }\tag{2.35}
$$

where $I _ { x } = | E _ { x } | ^ { 2 } , I _ { y } = | E _ { y } | ^ { 2 }$ , α is the intra-polarization nonlinearity parameter and $\beta$ is the inter-polarization nonlinearity parameter and have to be optimized. In section 3.2 optimization result will be presented.

## Chapter 3

## Algorithm testing and results

In this chapter results of the DSP algorithm tests will be presented. It is divided in two part. The first part is focused on the testing of CD compensation methods presented in section 2.2 using optical data generated with the simulation tool VPItransmissionMaker. The second part deals with nonlinear compensation using the result obtained in the first section on optical data generated in a laboratory experiment.

## 3.1 Chromatic dispersion compensation

## 3.1.1 System setup

The setup of the 112 Gb/s PolMux-QPSK coherent optical transmission system established using VPItransmissionMaker is illustrated in Fig. 3.1. The electrical data from four 28 Gb/s pseudo random bit sequence (PRBS) generators are modulated into two orthogonally polarized QPSK optical signals by two Mach-Zehnder modulators, which are then integrated into one fiber transmission channel by a polarization beam combiner to form the PolMux-QPSK optical signal. The received optical signals are mixed, with an optical local oscillator (LO) in the coherent receiver, to be transformed into four electrical signals by balanced photodetectors. In the dual polarization QPSK

![](images/5a147b6c65da3fe1d79746b57d47eca5a089f624d721dfb04e9a132739041873.jpg)  
Fig. 3.1: Schematic of 112 Gbit/s PM-QPSK coherent transmission system

transmitter, the number of bits output from the PRBS generator in each polarization is $6 5 5 3 6 \ ( 2 ^ { 1 6 } )$ , and the number of symbols in four components $( I _ { x } ,$ $Q _ { x } , I _ { y } , Q _ { y } )$ is $3 2 7 6 8 \ : ( 2 ^ { 1 5 } )$ . The linewidth of the transmitter laser and the LO laser as the the offset between the transmitter laser and the LO laser are set to be 0 Hz (i.e. no phase noise). In the fiber, the attenuation is set to 0 as well as PMD and the nonlinear index. The chromatic dispersion coefficient is set to be $1 6 ~ \mathrm { p s / n m / k m }$ In the coherent receiver, the $2 \times 4 ~ 9 0 ^ { o }$ hybrid structure is adopted to demodulate the received optical signal, which consists of 3 dB $2 \times 2$ fiber couplers and a phase delay components of $\pi / 2$ phase shift in one branch. The goal of these simulations is to understand how the different CD compensation methods behave and a good procedure is to neglect all the effects except for CD. The back to back (transmitter and receiver, without any transmission line) OSNR level required for a bit error rate (BER) of $1 0 ^ { - 3 }$ (limit value that allow full error recovery using forward error correction techniques) is 14.8 dB. As our goal is to fully compensate for CD, this value of required OSNR is expected for all the propagation distances.

## 3.1.2 Time domain methods

## Savory’s method

Savory’s filter is implemented using equation 2.6, 2.7 and 2.8 (section 2.2.1). Fig 3.2 and Fig. 3.3 show respectively OSNR required for a BER of $1 0 ^ { - 3 }$ versus propagation distance and number of taps required. As Savory’s formula is an approximation of equation 2.4 for short distance there is a penalty and the algorithm is not performing totally the CD compensation (Fig. 3.2). For longer distance it start to perform perfectly but we still have a penalty for 1000 and 5000 km as a matter of fact our simulations have only chromatic dispersion and it is expected to be fully compensated. The number of taps increase linearly as the taps equation (Eq. 2.8) is linearly dependent on the propagation length.

## Adaptive filters

Using a LMS adaptive filter it is possible to reach some expected OSNR level required for BER of $1 0 ^ { - 3 }$ as for back to back. This algorithm needs a time to converge and for longer distance it becomes a problem as a higher number of taps is needed. The issue was solved for 200 km using CMA algorithm that has better performance in convergence (section 2.2.1) and increasing the number of received symbols replying the received sequence. The longer the input sequence is, more convergence time the adaptive algorithm has. For 200 km it is enough to repeat the received data three time (65536×3 samples) but increasing the distance to 1000 km, the filter length required is too long and even CMA convergence is not reached.

![](images/e8cee29f91361d58c0089a242bf94b869c6d8f8ae4e3f632f40ec403938c0005.jpg)

Fig. 3.2: OSNR required for BER of $1 0 ^ { - 3 }$ versus the propagation distance using the Savory’s method  
![](images/45a4c69b2dbd68b6708efe11d93726c9d5abdc75446659534d6adcb6bf3f3398.jpg)  
Fig. 3.3: Number of taps required using the Savory’s method

![](images/e52155a9057a1a2410f280555e560277f5db9a97329c9c066c040f6f9dbd6522.jpg)  
Fig. 3.4: OSNR required for BER of $1 0 ^ { - 3 }$ versus the propagation distance using CMA adaptive filter

![](images/8087155dd7823fa427229a1d949957dd30525da9741614fe8a90b527c0587fe3.jpg)  
Fig. 3.5: Number of taps required CMA adaptive filter

## Savory + adaptive filter (CMA)

In this section CD compensation is performed with a combination of Savory method and CMA adaptive filter. First Savory’s filter is used to compensate most of the dispersion and then CMA adaptive filter with few taps is used for the residual dispersion. This structure is closer to a real system where a fixed long filter is used for the first stage of CD compensation and then the residual CD is treated by a shorter one. As in VPItransmissionMaker system the signal is sampled twice the symbol rate at the receiver, the algorithm has to chose the best sample to be used for the BER calculation. This decision is taken after the first CD compensation stage by plotting all the first and the second samples separately and choosing the one with the highest mean intensity. The best sample is passed to the CMA routine so that the filter weights are uploaded every 2 samples and downsampling is performed.

![](images/db40ca304f9d9bb58f00f8c25570325f2c4955cbf9021238a99d8748828ac3f2.jpg)  
Fig. 3.6: OSNR required for BER of $1 0 ^ { - 3 }$ versus the propagation distance using Savory’s and CMA filters  
Using Savory + CMA method leads to a required BER equal to back to

back. The number of taps required for the adaptive filter is related to the Savory’s filter behavior. As for short distance Savory’s method approximation is not accurate (Fig. 3.2), CMA required more taps while for more the 200 km only 7 taps are needed. This problem is avoided, as will be showed in the next section, using the frequency domain compensation.

## 3.1.3 Frequency domain method

As explained in section 2.2.2 an investigation on the length of the frequency filter was made to understand the behavior and the performance of this algorithm. The overlap-add method was firstly tested over three different propagation distance for a fixed OSNR level. FFT length was change to find the minimum required length to get the convergence of the BER value. As Fig. 3.7 shows for 20, 100 and 200 km of propagation FFT length of 32, 128 and 256 is required.

![](images/743fe3fd5487a82fc48dbfd449972f48ffbbbf4b32bb120a1d964fbdb821df08.jpg)  
Fig. 3.7: FFT length in overlap add method  
Fig. 3.8 shows the required OSNR versus the propagation distance for

![](images/1f2567829b367eaf3787fba68a08f6c8d73b35b79d300c9b8b840e3f6473aa08.jpg)

Fig. 3.8: OSNR required for BER of $1 0 ^ { - 3 }$ versus the propagation distance using FFT method  
![](images/4b4ef09c0b536fef2ebf4a128d4533216e73697a4100a11ae4121826cea3e0ac.jpg)  
Fig. 3.9: FFT length required versus the propagation distance

chromatic dispersion compensation performed using only the frequency domain method. Even for 5 km the results found in back to back were not reached and increasing the distance a strong penalty appeared. For 5000 km we measured a 3 dB penalty compared with the 14.8 dB required for 5 km propagation with the adaptive filter compensation (Fig. 3.8).

## Frequency domain method + CMA

As for the case Savory’s filer + CMA, chromatic dispersion compensation was also performed with a combination of FFT overlap add method and then CMA filter and the same result were reached (Fig. 3.10).

The CMA filter required only 7 taps that are needed for 500 km propagation while for shorter distance even 5 or 3 taps are necessary.

![](images/9adfcdc5c6324be1f94216290bdada61e363b629dc2b8da6321649b905d4e8a1.jpg)  
Fig. 3.10: OSNR required for BER of $1 0 ^ { - 3 }$ versus the propagation distance using FFT method and CMA filter

## 3.2 Nonlinear effects compensation

## 3.2.1 System setup

For the nonlinear impairments compensation, data from a 100 Gb/s PolMux-QPSK coherent optical transmission system were provided by Politecnico of Torino within the framework of the EURO-FOS1 project.

The transmission channel consists of a loop containing a SSMF long 63.6 km. Optical EDFA amplifiers were used for amplifying the signal after each fiber. For different experiments different number of loops can be used to emulate long-haul network. The fiber dispersion is 16.3 ps/nm/km. The receiver is composed of a polarization beam splitter (PBS) followed by 90o hybrids coupler and balanced photodetectors. Data is then stored in a digital oscilloscope for offline processing. The sampling of data is performed at the speed of 2 samples per symbols.

Two different type of data were provided: single channel system and 16 channels WDM system with 50 GHz spacing.

## 3.2.2 Single channel result

Single channel data were composed by different measures taken for 8, 16, 24 and 32 loops (respectively 508.8, 1017.6, 1526.4 and 2035.2 km) with two different OSNR levels 15 dB and 20 dB.

The DSP code used (A.1) is composed by:

• NLC and CD compensation using backpropagation (presented in section 2.5, see code in A.9):

– frequency domain filter with FFT length set to 128;

– NLC core.

• CMA butterfly structure with 25 taps for each filter (presented in section 2.3, see code in A.6);

• phase noise compensation using Viterby&Viterby method (presented in section 2.4, see code in A.8);

The α and $\beta$ parameter (Eq. 2.34 and 2.35) must be optimize[14]. As figure 3.11 shows, α and $\beta$ value were swept from 0 to 50. The best BER was found for $\alpha = \beta = 2 5$

![](images/accc104c952911539f02b33c57d13c54149403d7bc7e5638273a10bdf7fb45f9.jpg)  
Fig. 3.11: BER dependency on intra-polarization nonlinear parameter (α) and interpolarization parameter (β)

The result with and without the NLC are shown in figure 3.12. The input power level in the fiber is −3dBm. From the graph it can be seen that, as the power level and nonlinearities are not so high, the improvement is only 1 dB for 200 km propagation. The blue line in figure 3.12 was compared to result obtained without NLC by Politecnico of Torino2.

![](images/fa3ea0012b9be9d8501371bde2d4e0b9822013d30ce165f65f2b5db9abad51b1.jpg)  
Fig. 3.12: OSNR required for a bit error rate (BER) of $1 0 ^ { - 3 }$ versus the propagation distance with and without NLC

## 3.2.3 Multichannel result

In this section data for 16 channels WDM system with the same characteristic, as in 3.2.1, is processed. The channels are 50 GHz spacing and data is again provided by Politecnico of Torino3. Several measurements have been performed, for the central channel, a 1017.6 km (16 loops) propagation, a fixed attenuation per span and varying the power launched in the fiber form -1.2 dBm to 1.6 dBm. The DSP algorithms are the same used in section 3.2.2 with an α and $\beta$ set to 10.

As the figure 3.13 shows there is a little improvement using the NLC (as we said in the previous section the power level is not so high). If the nonlinearities were all compensated for, the blue line should continuing decreasing with the same slope even for a power of 1.6 dBm. Using the nonlinear structure, as there is no information about the neighbors channel, only SPM can be compensated while the penalty for 1.6 dBm comes from inter-channel nonlinearities as discussed in section 1.10.

![](images/3240bce538679f1f92570a096f0806124b928a61abe8a43d77e96580462e080c.jpg)  
Fig. 3.13: BER versus power launched in the fiber with and without NLC

## Chapter 4

## Conclusion and future work

Coherent detection at 100 Gb/s will become feasible in the future using DSP for linear impairments compensation. DSP allow polarization de-multiplexing, compensation of linear transmission impairments, as CD and PMD, and also gives higher OSNR tolerance. Increasing OSNR tolerance leads to increasing the maximal propagation distance that means less optical amplifiers, less noise and less costs of the system. On the other hand a more complex receiver is required as polarization tracking has to be performed but this is well paid by the improvement on system performance. The use of NLC (section 2.5) in DSP algorithm brings also important improving in performance but when inter-channel nonlinearities become predominant this advantage decreases.

Considering the future work, there are a lot of issue that can be addressed. First is to implement more complex and advanced adaptive algorithms for the PMD and residual CD compensation (especially step size updating algorithms) compared to the one used in section 2.3. Investigation over nonlinear effects compensation would also be interesting. As result in section 3.2.3 shows, multi-span backpropagation technique doesn’t compensate for interchannel nonlinearities. Advanced techniques based on Volterra compensator are interesting because can avoid this problem.

## Bibliography

[1] Marco Forzati. Phase Modulation Techniques for On-Off Keying in Optical Fiber. PhD thesis, Chalmers University of Technology, 2007.

[2] Govind P.Agrawal. Nonlinear Fiber Optics. Academic Press Second edition, 1995.

[3] Daniel J. F. Barros Joseph M. Kahn Ezra Ip., A. Pak Tao Lau. Coherent detection in optical fiber systems. Optics Express Vol. 16, No. 2, January 2008.

[4] M.Santagiustina. Progettazione e simulazione di circuiti ottici, 2009.

[5] Michael Finkenzeller. Delivering 100G per wavelength with today’s DWDM infrastructure. Motivation, Experiments and Standards RIPE 55, Amsterdam, October 2008. http://www.ripe.net/ripe/meetings/ripe-55/presentations/finkenzellerdelivering-100g.pdf.

[6] Seb J. Savory. Digital filters for coherent optical receivers. Optic Express 804, Vol. 16, No. 2, January 2008.

[7] Robert I. Killey P. Bayvel Seb J. Savory, G. Gavioli. Electronic compensation of chromatic dispersion using a digital coherent receiver. Optic Express 2120, Vol. 15, No. 5, March 2007.

[8] T. van den Borne D. Schulien C. Schmidt E.D. Wuth T. Geyer J. De Man E. Khoe Giok-Djan de Waardt Fludger, C.R.S. Duthel. Coherent equalization and POLMUX-RZ-DQPSK for robust 100-GE transmission. Journal of lightwave technology, Vol. 26, No. 1, January 2008.

[9] S.Haykin. Signal processing: where physics and mathematics meet. IEEE Signal process, MAG18, 2001.

[10] Steven W. Smith. The Scientist and Engineer’s Guide to Digital Signal Processing, Cap. 14,18.

[11] M.Montazeri P.Duhamel and K.Hilal. Classical adaptive algorithms (LMS, RLS, CMA, Decision Directed) seen as recursive structure. IEEE, 1993.

[12] Weizhen Yan Oda S. Hoshida T. Rasmussen J.C. Ling Liu, Zhenning Tao. Initial tap setup of constant modulus algorithm for polarization de-multiplexing in optical coherent receivers. OSA/OFC/NFOEC, 2009.

[13] Ezra Ip and Joseph M. Kahn. Compensation of dispersion and nonlinear impairments using digital backpropagation. Journal of lightwave technology, Vol. 26, No. 20, October 2008.

[14] Oda S. Tanaka T. Ohsima C. Zhenning Tao Rasmussen J.C. Tanimura T., Hoshida T. Systematic analysis on multi-segment dualpolarisation nonlinear compensation in 112 Gb/s DP-QPSK coherent receiver. ECOC, September, 2009.

[15] Noriaki Kaneda and Andreas Leven. Coherent polarization-divisionmultiplexed QPSK receiver with fractionally spaced CMA for PMD com-

pensation. IEEE Photonics technology letters, Vol. 21, No. 4, February 2009.

[16] J. Renaudier et al. Transmission of 100Gb/s coherent PDM-QPSK over 16x100km of standard fiber with allerbium amplifiers. IEEE Photonics technology letters, Vol. 21, No. 4, February 2009.

[17] Gabriel Charlet. Coherent detection associated with digital signal processing for fiber optics communication. C. R. Physique 9, 2008.

[18] Young-Kai Chen Andreas Leven, Noriaki Kaneda. A real-time CMAbased 10 Gb/s polarization demultiplexing coherent receiver implemented in an FPGA. OFC/NFOEC, 2008.

[19] I. Fijalkow J.R. Treichler and JR C.R. Johnson. Fractionally spaced equalizers. IEEE Signal Processing Magazine, 1996.

[20] I. Fijalkow J.R. Treichler and JR C.R. Johnson. Chromatic dispersion compensation using digital IIR filtering with coherent detection. IEEE Photonics technology letters, Vol. 19, No. 13, July 2007.

[21] Kiyoharu Aizawa Sanghoon Song and Mitsutoshi Hatori. A blind adaptive array based on CMA and LMS. Electronics and Communications in Japan, Part 3, Vol. 81, No. 7, 1998.

[22] Sander Lars Jansen Torsten Wuth Maxim Kuschnerov Guido Grosso Antonio Napoli Mohammad S. Alfiad, Dirk van den Borne and Huug de Waardt. A comparison of electrical and optical dispersion compensation for 111-Gb/s POLMUX-RZ-DQPSK. Journal of lightwave technology, Vol. 27, No. 16, August 2009.

# DSP test code

## A.1 main.m

```matlab
%Main program used
%The a l g o r i t h m i s composed by a s e r i e s o f module t h a t can be s w i t c h on or
o f f a s n e e d e d .
5
c l e a r a l l f u n c t i o n s ; c l c
c l o s e a l l
%% exp . parame ters
10 SymbolRate = ; % Baud
SamplesPerSymbol = ;
L o o p D i s p e r s i o n = ; % [ p s /nm ]
Re fWavelength = ; % [m] r e f . w a v e l e n g t h f o r d i s p e r s i o n c o m p e n s a t i o n
d i s t a n c e = ; %km
15 o s n r =
f f t l e n g t h = ; %must b e a power o f 2
%% module a c t i v a t i o n
%1 −−> a c t i v e
20
frequency domain CD = 0
time domain CD = 0
```

```matlab
NLC = 0
p h a s e n o i s e c o m p e n s a t i o n = 0
25 PMD compensation = 0
% number o f b i t s t o r e a d and s t a r t sample
NSymbols= ;
30 S t a r t S a m p l e= ;
EndSample = S t a r tS ample + NSymbols∗SamplesPerSymbol ;
%% read da t a
35 f i l e n a m e = [ ’ . / ’ n u m 2 s t r ( d i s t a n c e ) ’km/ ’ n u m 2 s t r ( L o o p D i s p e r s i o n ) ’ p s ’
num2str ( d i s t a n c e ) ’ km ’ num2str ( o s n r ) ’dB . mat ’ ] ;
l o a d ( f i l e n a m e )
r e a d I x = I x . band . E( S t a r t S a m p l e : EndSample ) ’ ;
40 read Qx = Qx . band . E( S t a r t S a m p l e : EndSample ) ’ ;
r e a d I y = I y . band . E( S t a r t S a m p l e : EndSample ) ’ ;
read Qy = Qy . band . E( S t a r t S a m p l e : EndSample ) ’ ;
45 read IQx=complex ( r e a d I x , read Qx ) ;
read IQy=complex ( r e a d I y , read Qy ) ;
%% resample
% i t u s e t h e m a t l a b f u n c t i o n r e s a m p l e
50
NewSamplesPerSymbol= ;
data IQx=re s ample ( read IQx , NewSamplesPerSymbol , SamplesPerSymbol ) ;
data IQy=re s ample ( read IQy , NewSamplesPerSymbol , SamplesPerSymbol ) ;
55
%% Cromatic d i s p e r s i o n compensa t ion i n f r e q u e n c y domain
i f frequency domain CD == 1
60 s a m p l e p e r i o d=1e12 / ( SymbolRate ∗NewSamplesPerSymbol ) ; %r e c o v e r i n g
s a m p l i n g p e r i o d i n ’ ps ’
D i s p e r s i o n=L o o p D i s p e r s i o n ∗ d i s t a n c e ;
```

```matlab
%C D f i l f d e g e n e r a t e s t h e f i l t e r and p e r f o r m t h e f i l t e r i n g i n t h e
%f r e q u e n c y domain
65 [ d a t a I Q x d a t a I Q y ]= C D f i l f d e ( d a t a I Q x , d a t a I Q y , f f t l e n g t h ,
D i s p e r s i o n , R e f W a v e l e n g t h ∗1 e9 , s a m p l e p e r i o d ) ;
%%%%%% Nonl inear compensa tor
i f NLC == 1
70
a l p h a = ;
be t a =
%t h e y need t o b e o p t i m i z e d
75 data IQx=data IQx . ∗ exp(− i ∗ ( a l p h a ∗ ( abs ( data IQx ) ) .ˆ2+ b e t a ∗ ( abs (
d a t a I Q y ) ) . ˆ 2 ) ) ;
data IQy=data IQy . ∗ exp(− i ∗ ( a l p h a ∗ ( abs ( data IQy ) ) .ˆ2+ b e t a ∗ ( abs (
d a t a I Q x ) ) . ˆ 2 ) ) ;
end
80 end
%% Sample da ta
% I t c h o o s e s t h e b e s t s a m p l e l o o k i n g a t t h e h i g h e s t a v e r a g e i n t e n s i t y o f
% t h e samples
85
F i r s t S a m p l e x=s a m p l e d a t a a d a p ( data IQx , NewSamplesPerSymbol ,
C a l c S t a r t S a m p l e ) ;
F i r s t S a m p l e y=s a m p l e d a t a a d a p ( data IQy , NewSamplesPerSymbol ,
C a l c S t a r t S a m p l e ) ;
90 %% PMD c o m p e n s a t i o n w i t h b u t t e r f l y CMA s t r u c t u r e
i f PMD compensation == 1
%% a v o i d s i n g u l a r i t y p r o b l e m
95
% i n i t i a l i z a t i o n o f t h e f i l e r w e i g h t s
tap num 1= ; % even number ( t h e r e a l number o f t a p s w i l l be tap num 1 +1)
```

```matlab
w 1=z e r o s ( tap num 1 +1 ,1) ;
w 1 ( tap num 1 /2+1)=1;
100 w 2=z e r o s ( tap num 1 +1 ,1) ;
w mat =[ w 1 w 2 ] ;
%p r e p a r i n g d a t a f o r d o w n s a m p l i n g i n s i d e t h e b u t t e r f l y s t r u c t u r e
i f F i r s t S a m p l e x == 2
105 data IQx = data IQx ( 2 : end ) ;
e l s e
data IQx = data IQx ( 1 : end −1) ;
end
i f F i r s t S a m p l e y == 2
110 data IQy = data IQy ( 2 : end ) ;
e l s e
data IQy = data IQy ( 1 : end −1) ;
end
115 amp x=mean ( abs ( data IQx ) ) ;
amp y=mean ( abs ( data IQy ) ) ;
data IQx=data IQx /amp x ;
data IQy=data IQy /amp y ;
120
myu= ;
[ f a k e x e r r x w]= pmd cma samp sing prob ( data IQx , data IQy , tap num 1 ,
myu , w mat ) ;
%% l i n e a r e f f e c t c o m p e n s a t i o n w i t h b u t t e r f l y s t r u c t u r e CMA
125
w11=w ( : , 1 ) ;
w12=w ( : , 2 ) ;
w21=−c o n j ( f l i p u d ( w12 ) ) ;
w22=c o n j ( f l i p u d ( w11 ) ) ;
130
w mat=[w11 w21 w12 w22 ] ;
myu= ;
[ data IQx data IQy e r r x e r r y w mat]=pmd cma samp ( data IQx , data IQy ,
tap num 1 , myu , w mat ) ;
135
end
```

```matlab
%% Phase n o i s e compensa t ion
140 i f p h a s e n o i s e c o m p e n s a t i o n == 1
window= ;
data IQx=phase comp ( data IQx , window ) ;
data IQy=phase comp ( data IQy , window ) ;
145
end
%% d a t a r e c o v e r y
150 r e c I x=r e a l ( data IQx ) >0;
rec Qx=imag ( data IQx ) >0;
r e c I y=r e a l ( data IQy ) >0;
rec Qy=imag ( data IQy ) >0;
155
a l l d a t a x=r e c I x ∗2−1+ j ∗ ( rec Qx ∗2−1) ;
a l l d a t a y=r e c I y ∗2−1+ j ∗ ( rec Qy ∗2−1) ;
%% BER c a l c u l a t i o n
160
BERstart =1000; %c a l c u l a t e BER c u t t i n g t h e f i r s t s a m p l e s
a l l d a t a x=a l l d a t a x ( BERstart +1: end ) . ’ ;
a l l d a t a y=a l l d a t a y ( BERstart +1: end ) . ’ ;
165
[ B E R d i f f x B E R d i f f y e r r s x e r r s y l e n g t h x l e n g t h y ]=BER( a l l d a t a x ,
a l l d a t a y , B i t S e q u e n c e x , B i t S e q u e n c e y ) ;
end % end o f b l o c k i n g r o u t i n e
```

## A.2 CD fil fde.m

```matlab
%C D f i l f d e CD c o m p e n s a t i o n i n f r e q u e n c y domain .
5 % −−− A l g o r i t h m i c d e t a i l s
%T h i s f u n c t i o n c o n s t r u c t t h e f r e q u e n c y f i l t e r and c a l l t h e O v e r l a p −add
%method main f u n c t i o n o f f i l t e r i n g u s i n g FFT .
%d a t a x , d a t a y a r e t h e i n p u t d a t a s t r e a m .
%f f t l e n g t h i s t h e l e n g t h o f t h e FFT, L i s t h e l e n g t h o f t h e d a t a window
10 %t h a t we c o n s i d e r and G i s t h e t o t a l z e r o pad l e n g t h t h a t i s a p p l i e d b e f o r e
and
%a f t e r t h e d a t a window .
f u n c t i o n [ d a t a I Q x d a t a I Q y ]= C D f i l f d e ( d a t a x , d a t a y , f f t l e n g t h , d i s p e r s i o n
, wavelength , s a m p l e p e r i o d )
15 m = s i z e ( d a t a x , 1 ) ;
i f m == 1
datax = datax ( : ) ;
datay = datay ( : ) ;
end
20
m = s i z e ( d a t a x , 1 ) ;
i f m == 1
datay = datay ( : ) ;
end
25
ndata = s i z e ( datax , 1 ) ;
i f f f t l e n g t h > 2 ˆ 2 0 ,
e r r ( g e n e r a t e m s g i d ( ’ f i l t e r T o o L o n g ’ ) , .
30 ’ F i l t e r s o f l e n g t h g r e a t e r t h a n 2 ˆ 2 0 a r e n o t s u p p o r t e d . Use d f i l t .
f f t f i r i n s t e a d . ’ ) ;
end
i f f f t l e n g t h > n d a t a
e r r ( g e n e r a t e m s g i d ( ’ f i l t e r T o o S h o r t ’ ) ,
35 ’ F i l t e r l e n g t h must be s h o r t e r t h a n d a t a l e n g t h ’ ) ;
e l s e
```

```matlab
%% L and G c a l c u l a t i o n
40 G = f f t l e n g t h / 4 ;
L = f f t l e n g t h / 2 ;
%% c o n s t u c t i o n o f t h e f i l t e r
%h e r e t h e f i l t e r i s c o n s t r u c t e d u s i n g t h e f r e q u e n c y domain f o r m u l a d i r e c t l y
45 %from t h e t h e o r y
C=3e 5 ; %s p e e d o f l i g h t i n km/ s
q=[− f f t l e n g t h / 2 : f f t l e n g t h / 2 − 1 ] ’ ;
omega=2∗ p i ∗ ( q ) / ( s a m p l e p e r i o d ∗ f f t l e n g t h ) ;
50 f i l t =exp(− j ∗ ( d i s p e r s i o n ∗ ( w a v e l e n g t h ) ˆ 2 / ( 4 ∗ p i ∗C) ) ∗omega . ˆ 2 ) ;
% f i l i s a s t r u c t u r e where are s a v e d a l l t h e parame ters needed f o r per form
t h e o v e r l a p method
f i l = s t r u c t ( ’ f i l t e r ’ , f i l t , ’ n f f t ’ , f f t l e n g t h , ’ window ’ , L , ’ n d a t a ’ , n d a t a ,
’ o v e r l a p ’ , G) ;
55 %main program
d a t a I Q x = o v e r l a p a d d ( f i l , d a t a x ) ;
d a t a I Q y = o v e r l a p a d d ( f i l , d a t a y ) ;
end
```

## A.3 overlap add.m

```matlab
%% O v e r l a p −add method o f FIR f i l t e r i n g u s i n g FFT .
% −−− A l g o r i t h m i c d e t a i l s
5 % b i s a s t r u c t u r e where are s t o r e d a l l t h e parame ter needed t o per form
t h e o v e r l a p
% add method .
% b = s t r u c t ( ’ f i l t e r ’ , . . . , ’ n f f t ’ , . . . , ’ window ’ , . . . , ’ n da t a ’ , . . . , ’
o v e r l a p ’ , . . . )
% f i l t e r i s t h e f i l t e r d e f i n e d i n f r e q u e n c y domain , n f f t i s t h e FFT
10 % l e n g t h , window i s t h e window d a t a l e n g t h , n d a t a i s t h e l e n g t h o f a l l
% t h e r e c e i v e d d a t a , o v e r l a p i s t h e z e r o p a d d i n g l e n g t h d e f i n e d a s n f f t /4
% The o v e r l a p / add a l g o r i t h m c o n v o l v e s b . f i l t e r w i t h b l o c k s o f d a t a , and
adds
% t h e o v e r l a p p i n g o u t p u t b l o c k s . I t u s e s t h e FFT t o compute t h e
15 % c o n v o l u t i o n .
f u n c t i o n y = o v e r l a p a d d ( b , d a t a )
%% l o a d i n g parame ters
20
n f f t =b . n f f t ;
ndata=b . ndata ;
L=b . window ;
G=b . o v e r l a p ;
25
B = f f t s h i f t ( b . f i l t e r ) ;
i f l e n g t h (B) ==1,
B = B ( : ) ; % make s u r e t h a t B i s a column
30 end
i f s i z e (B , 2 ) ==1
B = B ( : , o n e s ( 1 , s i z e ( d a t a , 2 ) ) ) ; % r e p l i c a t e t h e column B
end
i f s i z e ( d a t a , 2 ) ==1
35 d a t a = d a t a ( : , o n e s ( 1 , s i z e ( b , 2 ) ) ) ; % r e p l i c a t e t h e column d a t a
end
```

```matlab
y = z e r o s ( s i z e ( d a t a ) ) ;
i s t a r t = 1 ;
40 w h i l e i s t a r t <= ndat a
i e n d = min ( i s t a r t +L−1 , ndat a ) ;
i f ( i e n d − i s t a r t ) <= 0
break
e l s e
45 X = f f t ( [ z e r o s ( 1 ,G) ’ ; d a t a ( i s t a r t : i e n d , : ) ] , n f f t ) ;
end
Y = i f f t (X. ∗ B) ;
yend = min ( ndata , i s t a r t+n f f t −1) ;
y ( i s t a r t : yend , : ) = y ( i s t a r t : yend , : ) + Y ( 1 : ( yend− i s t a r t +1) , : ) ;
50 i s t a r t = i s t a r t + L ;
end
end
```

## A.4 lms.m

```matlab
f u n c t i o n [ y e r r w]= l m s ( x , N, F i r s t S a m p l e , myu , w)
% i n p u t d a t a stream , f i l t e r l e n g t h , b e s t s a m p l e c h o s e n l o o k i n g
% t h e h i g h e r mean i n t e n s i t y , s t e p s i z e , t a p w e i g h t s
5
f o r q=N+F i r s t S a m p l e : 2 : l e n g t h ( x )
X=x ( q : − 1 : ( q−N) ) ;
y ( q )=w’ ∗X ;
10 y r e=r e a l ( y ( q ) ) >0;
y r e 1=y r e ∗2 −1;
y im=imag ( y ( q ) ) >0;
y im 1=y im ∗2 −1;
15 d e c =( y r e 1+j ∗ y i m 1 ) ;
e r r ( q )=dec−y ( q ) ;
w=w+myu∗X∗ c o n j ( e r r ( q ) ) ;
end
20 e r r=e r r (N+F i r s t S a m p l e + 2 0 0 : 2 : l e n g t h ( x ) ) . ’ ;
y=y (N+F i r s t S a m p l e + 2 0 0 : 2 : l e n g t h ( x ) ) . ’ ;
end
```

## A.5 cma.m

```matlab
f u n c t i o n [ y e r r w]=cma ( x , N, F i r s t S a m p l e , myu , w)
% i n p u t d a t a stream , f i l t e r l e n g t h , a m p l i t u d e , b e s t s a m p l e c h o s e n l o o k i n g
% t h e h i g h e r mean i n t e n s i t y , s t e p s i z e , t a p w e i g h t s
5
y=z e r o s ( l e n g t h ( x ) , 1 ) ;
f o r q=N+F i r s t S a m p l e : 2 : l e n g t h ( x )
X=x ( q : − 1 : ( q−N) ) ;
y ( q )=X . ’ ∗ w ;
10
e r r ( q ) =1−(abs ( y ( q ) ) ) ˆ 2 ;
w=w+myu∗ c o n j (X) ∗ e r r ( q ) ∗y ( q ) ;
end
15 e r r=e r r (N+F i r s t S a m p l e + 2 0 0 : 2 : l e n g t h ( x ) ) ;
y=y (N+F i r s t S a m p l e + 2 0 0 : 2 : l e n g t h ( x ) ) ;
end
```

## A.6 pmd cma samp.m

f u n c t i o n [ x new y new e r r x e r r y w]=pmd cma samp ( x , y , N, myu , w, key ) %   
i n p u t d a t a s t r e a m s , f i l t e r l e n g t h , a m p l i t u d e , t a p w e i g h t s   
w xx=w ( : , 1 ) ;   
5 w yx=w ( : , 2 ) ;   
w xy=w ( : , 3 ) ;   
w yy=w ( : , 4 ) ;   
f o r q=N+ 1 : 2 : l e n g t h ( x )   
10 X=x ( q : − 1 : ( q−N) ) ;   
Y=y ( q : − 1 : ( q−N) ) ;   
x new ( q )=w xx . ’ ∗X+w xy . ’ ∗Y ;   
y new ( q )=w yx . ’ ∗X+w yy . ’ ∗Y ;   
15   
e r r x ( q ) =1−(abs ( x new ( q ) ) ) ˆ 2 ;   
e r r y ( q ) =1−(abs ( y new ( q ) ) ) ˆ 2 ;   
w xx=w xx+myu∗ e r r x ( q ) ∗ x new ( q ) ∗ c o n j (X) ;   
20 w xy=w xy+myu∗ e r r x ( q ) ∗ x new ( q ) ∗ c o n j (Y) ;   
w yx=w yx+myu∗ e r r y ( q ) ∗ y new ( q ) ∗ c o n j (X) ;   
w yy=w yy+myu∗ e r r y ( q ) ∗ y new ( q ) ∗ c o n j (Y) ;   
end   
25   
x new=x new (N+ 1 : 2 : end ) . ’ ;   
y new=y new (N+ 1 : 2 : end ) . ’ ;   
e r r x=e r r x (N+ 1 : 2 : end ) ;   
30 e r r y=e r r y (N+ 1 : 2 : end ) ;   
w=[w xx w xy w yx w yy ] ;   
end

## A.7 CD fil.m

```matlab
% d i s p e r s i o n compensa t ion i n t ime domain
% Chromatic d i s p e r s i o n i s d e s c r i b e d a s a l l −p a s s f i l t e r
% r e f [ Kuschnerov , ” A d a p t i v e c h r o m a t i c d i s p e r s i o n e q u a l i z a t i o n f o r
% non−d i s p e r s i o n managed c o h e r e n t s y s t e m s ”] (OMT1. p d f )
5
f u n c t i o n [ d a t a w]= C D f i l ( dat a , num taps , d i s p e r s i o n , w a v e l e n g t h ,
s a m p l e p e r i o d , c a l c t a p , w)
i f c a l c t a p==1
10 C=3e5 ; % Speed o f l i g h t (km/ s )
f o r q=1: num taps
a r g =( j ∗C∗ s a m p l e p e r i o d ˆ 2 ) / ( d i s p e r s i o n ∗ w a v e l e n g t h ˆ 2 ) ;
b ( q )=s q r t ( a r g ) ∗ exp(− a r g ∗ p i ∗ ( q−round ( num taps / 2 ) ) ˆ 2 ) ;
end
15
w=b . ∗ k a i s e r ( n u m t a p s ) ’ ;
end
20 d a t a= f i l t e r (w, 1 , data ’ ) ; %c h r o m a t i c d i s p e r s i o n e q u a l i z a t i o n
data=data . ’ ;
end
```

## A.8 phase compl.m

```matlab
% p h a s e n o i s e c o m p e n s a t i o n u s i n g v i t e r b i and v i t e r b i
f u n c t i o n [ p h r e c d a t a r o t a n g l e ]= phase comp ( data , window ) ;
5 c o n s t r o t=−p i / 4 ;
f o r q =1: l e n g t h ( d a t a )
n1=q−window ;
i f q−window<1
10 n1=1;
end
n2=q+window ;
i f ( q+window )>l e n g t h ( data )
n2=l e n g t h ( data ) ;
15 end
r o t a n g l e ( q )=a n g l e ( sum ( d a t a ( n1 : n2 ) . ˆ 4 ) ) ;
end
20 r o t a n g l e = [ ( l a s t a n g l e s ∗ 4 ) r o t a n g l e ] ;
r o t a n g l e =(unwrap ( r o t a n g l e ) ) / 4 ;
f o r qq =1: l e n g t h ( d a t a )
p h r e c d a t a ( qq )=data ( qq ) ∗ exp(− j ∗ r o t a n g l e ( qq ) ) ∗ exp ( j ∗ c o n s t r o t ) ;
25 end
```

## A.9 CD and NLC

```matlab
D i s p e r s i o n=L o o p D i s p e r s i o n ;
s a m p l e p e r i o d=1e12 / ( SymbolRate ∗NewSamplesPerSymbol ) ;
f f t l e n g t h = v a l u e ;
f o r s p a n = 1 : s t r 2 d o u b l e ( l o o p )
%% Chromatic d i s p e r s i o n c o m p e n s a t i o n u s i n g FFT f i l t e r %%
i f frequency domain CD
[ d a t a I Q x d a t a I Q y ]= C D f i l f d e ( d a t a I Q x , d a t a I Q y , f f t l e n g t h ,
D i s p e r s i o n , R e f W a v e l e n g t h ∗1 e9 , s a m p l e p e r i o d ) ;
%%Nonl inear compensa tor%%
i f NLC
a l p h a = v a l u e ;
b e t a = v a l u e ;
data IQx=data IQx . ∗ exp(− i ∗ ( a l p h a ∗ ( abs ( data IQx ) ) .ˆ2+ b e t a ∗ (
abs ( data IQy ) ) . ˆ 2 ) ) ;
data IQy=data IQy . ∗ exp(− i ∗ ( a l p h a ∗ ( abs ( data IQy ) ) .ˆ2+ b e t a ∗ (
abs ( data IQx ) ) . ˆ 2 ) ) ;
end
end
end
```