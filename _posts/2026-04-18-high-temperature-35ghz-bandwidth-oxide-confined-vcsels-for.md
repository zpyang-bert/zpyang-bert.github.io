---
layout: post
title:      "High Temperature >35GHz Bandwidth Oxide-Confined VCSELs for 200G-PAM4 Links"
date:       2026-04-18 11:52:24
author:     "Bert"
tags:
  - Mineru
---
Yoshiaki Watanabea , Terukazu Narusea , Kota Tokudaa , Takahiro Koyamaa , Masaki Shiozakia , Naoki Jogana , Toshiharu Kiuchib , Hidekazu Kawanishia , Osamu Maedaa

a Laser Development Department, Analog LSI Business Division, Sony Semiconductor Solutions Corporation,

Atsugi Tec., 4-14-1 Asahi-cho, Atsugishi, Kanagawa, 243-0014 Japan

E-mail: Yoshiaki.Watanabe@sony.com

b Laser & Analog Device Products Department, Analog LSI Business Division, Sony Semiconductor Solutions Corporation, Atsugi Tec., 4-14-1 Asahi-cho, Atsugishi, Kanagawa, 243-0014 Japan E-mail: Toshiharu.Kiuchi@sony.com

Abstract: We developed oxide-confined VCSELs with >35 GHz bandwidth at 25 °C to $8 0 ~ ^ { \circ } \mathrm { C }$ for 200G-PAM4 links, achieving low noise, clear eye opening and over 10-year lifetimes, demonstrating state-of-the-art performance.

## 1. Introduction

Recent advances in xPU architectures have driven a substantial increase in bandwidth requirements for artificial intelligence (AI) and machine-learning workloads. In parallel, minimizing power consumption has become a critical design constraint for the realization of practical high-speed interconnects. Multimode vertical-cavity surface-emitting lasers (VCSELs) have emerged as promising optical sources for scale-up and scale-out network architectures in AI computing clusters, owing to their inherent advantages such as direct modulation capability, low energy consumption, and wide tolerance to optical coupling with multimode fibers [1], [2]. Among various implementations, oxide-confined VCSELs operating at a wavelength of 850 nm have achieved a high level of technological maturity and are widely recognized as a mainstream for short-reach multimode-fiber data-communication systems.

In this paper, we present the development of 850nm oxide-confined VCSELs for 200G-PAM4 at Sony. While various approaches are being explored to increase the modulation bandwidth of oxide-confined VCSELs [3], we have focused on achieving wide bandwidth, low noise at elevated temperatures, and practical reliability in our designs.

## 2. VCSEL Design and Fabrication

Wide bandwidth and low noise performance are essential for multi-level modulation formats such as PAM4. To meet these requirements for 200G-VCSEL, we have optimized the layer structure, growth conditions, chip layout, and chip structure based on our previous 100G-VCSEL design.

We have adopted an InGaAs-QW based 850nm oxide-confined VCSEL structure and optimized the following items to increase relaxation oscillation frequency: 1) the composition in the active layer to increase differential gain, 2) resonator cavity design to reduce carrier transport time, 3) carrier concentration profile in AlGaAs DBRs optimized to simultaneously reduce electrical resistance and optical loss, 4) the design of the resonator and DBR to reduce thermal resistance, and 5) the detuning between the Fabry-Perot cavity resonance wavelength and the gain peak of the active region. Each parameter is designed to simultaneously achieve high bandwidth and reliability. The pad layout was a GSG pattern to accommodate high frequency characteristics.

The epitaxial wafers were grown in our MOCVD reactor, with growth conditions optimized for both performance and reliability. The process also utilized our process fab, employing an ICP-based dry etching process to expose the oxide layer of the p-DBR above the active layer area, followed by a high-temperature wet oxidation process to form the oxide confinements. The size of the oxidation area was optimized to achieve both high-speed operation and reliability. Additionally, ion implantation was performed with optimized diameter on the mesa region, and BCB was used under the electrode pads to minimize the parasitic capacitance.

## 3. Evaluation results

Fig.1 shows the LIV characteristics of a representative at $2 5 ~ ^ { \circ } \mathrm { C }$ and $7 0 ~ ^ { \circ } \mathrm { C } .$ The output power at 8 mA was approximately 7.2 mW at $2 5 ~ ^ { \circ } \mathrm { C }$ and 6.3 mW at $7 0 ^ { \circ } \mathrm { C } ,$ , and the voltage at 8 mA was $2 . 6 \mathrm { \bar { ~ V } }$ at $2 5 ~ ^ { \circ } \mathrm { C }$ and 2.5 V at $7 0 ^ { \circ } \mathrm { C } .$

![](images/6b4e9b2f097928f43b1db3642e30a363abf75a4daecc12e1cb69665d5106df9e.jpg)  
(a)

![](images/34b8c3aaced2ca58169540feff047f43182e4301dd366266b03f57a915468d00.jpg)  
(b)  
Fig. 1. LIV characteristics, (a) L-I, (b) V-I

Fig.2 shows the S21 response. The S21 evaluation was performed by contacting a Form Factor GSG probe and measured using a Keysight N4373E PNA network analyzer. The modulation bandwidth was over 40 GHz at $2 5 ^ { \circ } \mathrm { C } ,$ 37 GHz at $7 0 ^ { \circ } \mathrm { C } ,$ and 36 GHz at $8 0 ~ ^ { \circ } \mathrm { C }$ . The overshoot level in the S21 response was confirmed to be low, around 2 dB at both $2 5 ~ ^ { \circ } \mathrm { C }$ to $8 0 ~ ^ { \circ } \mathrm { C } ,$ which is advantageous for PAM4 operation.

![](images/bdef94ef5bded87257ed6c94921a17b01db17cb04a2276466560ef4cc9b75504.jpg)  
(a)

![](images/58de59483fec8bfb87508edfc8c83f3bd9425ef793110311cf8c0083e0490bf1.jpg)  
(b)  
Fig. 2. S21 response at bias currents of 7, 8, and 9 mA, temperatures of (a) $2 5 ^ { \circ } \mathrm { C } ,$ (b) $7 0 ~ ^ { \circ } \mathrm { C }$

RIN performance as shown in $\mathrm { F i g } . 3 ,$ , was measured with a Keysight N1092 sampling oscilloscope at a DC bias current. The RIN level stabilized at an average of -150dB/Hz or less at $7 0 ~ ^ { \circ } \mathrm { C } / 8$ mA, achieving low noise performance. We confirmed that the wide bandwidth and low noise performance were achieved simultaneously.

![](images/e565f3ff06bedf3aca56ff3e37d96881e7080183fe7ef5888a224b52c1284ea4.jpg)  
Fig. 3. RIN at 70°C/8 mA (N=10)

The optical eye diagram of 200G-PAM4 as shown in Fig. 4, was evaluated using a Keysight M8199B arbitrary waveform generator. The baud rate was 106.25 GBd PAM4 signal with a PRBS15Q pattern, an extinction ratio of approximately 2.5 dB, a 53.1 GHz filter and waveform correction of 7 taps on the Tx and 30 taps on the Rx. The signal was evaluated in a back-to-back transmission over 50um multimode fiber. Owing to the wide bandwidth and low noise performance of our VCSELs, sufficient eye opening was observed at both $2 5 ~ ^ { \circ } \mathrm { C }$ and $7 0 ^ { \circ } \mathrm { C } ,$ , with TDECQ remaining below 4 dB at each temperature.

![](images/8c640994f049b9e5d12544ab502eed701c603a66fe241913048787562ba88bec.jpg)  
(a)

![](images/b8cb8062767b0f980d4a7fb31b6518d552ea0697c1305fe8f4fad60b8aeb5020.jpg)  
(b)  
Fig. 4. Eye diagram with 200 Gbps operations at $( \mathrm { a } ) 2 5 ^ { \circ } \mathrm { C } / 8 \mathrm { m A }$ and $( \mathsf { b } ) 7 0 ^ { \circ } \mathrm { C } / 8 \mathrm { m A }$

Fig. 5 shows lifetime test results. For aging tests, the VCSELs were assembled in TO-CANs and stressed at $1 0 0 ~ ^ { \circ } \mathrm { C }$ with a constant bias current of 9.5 mA. A standard reliability model with acceleration factors was used for lifetime estimation. Currently lifetimes of over 10 years at $7 0 ~ ^ { \circ } \mathrm { C } / 8$ mA have been achieved, and more extensive reliability testing is ongoing to obtain more robust wear-out life statistics.

![](images/0d927e5d20f8f11e644937993373fc1c652ca4289669c9411c4d23d0f604ac97.jpg)  
Fig. 5. Lifetime test results converted to 70℃/8mA using an acceleration factors (N=29)

## 4. Conclusion

This paper reports on the performance of Sony's VCSELs for 200G-PAM4 standard multimode optical links. By further optimizing the existing oxide-confined VCSEL structure, we achieved a modulation bandwidth of over 35GHz from $2 5 ~ ^ { \circ } \mathrm { C }$ to 80 $^ \circ \mathrm { C }$ and an average RIN of below -150 dB/Hz at $7 0 ~ ^ { \circ } \mathrm { C } .$ . Furthermore, optical eye diagram evaluations at $2 5 ~ ^ { \circ } \mathrm { C }$ and $7 0 ~ ^ { \circ } \mathrm { C }$ confirmed sufficient eye opening with lower TDECQ levels. The lifetime exceeded 10 years at $7 0 ~ ^ { \circ } \mathrm { C } / 8$ mA, demonstrating practicality in both performance and lifetime in initial evaluations. To the best of our knowledge, these results demonstrate state-of-the-art and leading-level performance among 850 nm multimode VCSELs at the most widely used wavelength range in short reach applications.

## 5. Acknowledgement

The authors gratefully acknowledge Keysight technologies for their support in the eye diagram measurements.

## 6. References

[1] Kazuya Nagashima, “A High-Density Energy-Efficient 850-nm VCSEL-Based 106-Gb/s × 8-Channel CPO Transceiver for AI/ML Applications,” Journal of Lightwave Technology., vol. 44, issue. 3, pp. 955-966, Feb. 2026.

[2] Susnata Mondal, “A 108 Gb/s PAM-4 VCSEL-Based Direct-Drive Optical Engine for Co-Packaged Optics Applications,” IEEE JOURNAL OF SOLID-STATE CIRCUITS., vol. 61, issue. 1, pp. 33-46, Jan. 2026.

[3] Tzu Hao Chow, “200G VCSEL Development and Proposal of Using VCSELs for Near-Package-Optics Scale-Up Application,” Photonics 2026, 13, 90.