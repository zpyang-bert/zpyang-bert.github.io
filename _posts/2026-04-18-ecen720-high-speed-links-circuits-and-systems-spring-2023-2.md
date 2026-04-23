---
layout: post
title:      "ECEN720: High-Speed Links Circuits and Systems Spring 2023"
date:       2026-04-18 17:29:33
author:     "Bert"
tags:
  - Lecture
  - Mineru
  - TDR
---
Lecture 3: Time-Domain Reflectometry & S-Parameter Channel Models

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/a06321391b10426c46bcc2d2739cf4d739a56819d2149cd83334ed1e5b97a461.jpg)

Sam Palermo Analog & Mixed-Signal Center Texas A&M University

## Announcements

● Lab 1 report and Prelab 2 due Feb 6

● Reference Material Posted on Website

TDR theory application note

• S-parameter notes

## Agenda

Interconnect measurement techniques

Time-domain reflectometry (TDR)

Network analyzer

• S-parameters

● Cascading S-parameter models

• Full S-parameter channel model

Transient simulations

Impulse response generation

Eye diagrams

Inter-symbol interference

## Lecture References

● Majority of TDR material from Dally Chapter 3.4, 3.6 - 3.7

Majority of s-parameter material from Hall "Advanced Signal Integrity for High-Speed Digital Designs'" Chapter 9

## Interconnect Modeling

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/ccf783b7359278fb00cc26c7750940478f67a37f74d620f2d98bc1691bb5f36b.jpg)

Why do we need interconnect models?

• Perform hand calculations and simulations (Spice, Matlab, etc...)

Locate performance bottlenecks and make design trade-offs

• Model generation methods

Electromagnetic CAD tools

Actual system measurements

Measurement techniques

Time-Domain Reflectometer (TDR)

Network analyzer (frequency domain)

## Time-Domain Reflectometer (TDR)

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/80ccf0b434daa283c250a94bdb715df0055fecb68bf58a6d5d33ed14cdd8f82a.jpg)

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/05a4d81272c32054d09cf224dff186c2c7fa832254117e4f0ad1b904b29409ad.jpg)

• TDR consists of a fast step generator and a high-speed oscilloscope

• TDR operation

• Outputs fast voltage step onto channel

• Observe voltage at source, which includes reflections

Voltage magnitude can be converted to impedance

Impedance discontinuity location can be determined by delay

Only input port access to characterize channel

## TDR Impedance Calculation

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/7653227a9411a8acb4e6dee7dbe15cff0945666678bd1ac585a2472b4c62c4b3.jpg)

$$
k _ { r } \left( t \right) = \frac { V _ { r } \left( t \right) } { V _ { i } } = \frac { Z _ { T } \left( t \right) - Z _ { 0 } } { Z _ { T } \left( t \right) + Z _ { 0 } }
$$

$$
Z _ { T } \left( t \right) = Z _ { 0 } \left( \frac { 1 + k _ { r } \left( t \right) } { 1 - k _ { r } \left( t \right) } \right) = Z _ { 0 } \left( \frac { V _ { i } + V _ { r } \left( t \right) } { V _ { i } - V _ { r } \left( t \right) } \right) = Z _ { 0 } \left( \frac { V \left( t \right) } { 2 V _ { i } - V \left( t \right) } \right)
$$

$$
\mathrm { I f } V _ { \mathrm { S T E P } } = 1 V \Rightarrow V _ { i } = 0 . 5 \mathrm { V }
$$

$$
\boxed { Z _ { T } \left( t \right) = Z _ { 0 } \Biggl ( \frac { V \left( t \right) } { 1 V - V \left( t \right) } }
$$

$$
Z _ { _ { T } } ( x ) { = } Z _ { _ { T } } { \Bigg ( } t = { \frac { 2 x } { \upsilon } } { \Bigg ) }
$$

## TDR Waveforms (Open & Short)

● Open termination

$$
\scriptstyle \longrightarrow \displaystyle \mathop { \underbrace { z _ { 0 } = 5 0 \Omega } } _  \scriptstyle \in \mathrm { ~ \tiny ~  ~ } , \scriptstyle \in \mathrm { ~ \tiny ~  ~ } , \mathrm { ~ \tiny ~  ~ } , \mathrm { ~  ~ } , \mathrm { ~  ~ } , \mathrm { ~  ~ } , \mathrm { ~  ~ } , \mathrm { ~  ~ } , \mathrm { ~  ~ } , \mathrm { ~  ~ } , \mathrm { ~  ~ } , \mathrm { ~  ~ } , \mathrm { ~  ~ } , \mathrm { ~  ~ } , \mathrm { ~  ~ } , \mathrm { ~  ~ } , \mathrm { ~  ~ } , \mathrm { ~  ~ } , \mathrm { ~  ~ } , \mathrm { ~  ~ } , \mathrm { ~  ~ } , \mathrm  ~ ( \begin{array} { l }  \mathrm { ~  ~ } , \mathrm { ~  ~ } , \mathrm { ~  ~ } , \mathrm { ~  ~ } , \mathrm { ~  ~ } , \mathrm { ~  ~ } , \mathrm { ~  ~ } , \mathrm { ~ ( \Lambda ~ ) } , \mathrm { ~ ( \Lambda ~ ) } , \mathrm { ~ ( \Lambda ~ ) } , \mathrm { ~ ( \Lambda ~ ) } , \mathrm { ~ ( \Lambda ~ ) } , \mathrm { ~ ( \Lambda ~ ) } , \mathrm { ~ ( \Lambda ~ ) ~ } , \mathrm { ~ ( \Lambda ~ ) } , \mathrm { ~ ( \Lambda ~ ) ~ } , \mathrm { ~ ( \Lambda ~ ) ~ } , \mathrm { ~ ( \Lambda ~ ) ~ } , \mathrm { ~ ( \Lambda ~ ) ~ } , \mathrm { ~ ( \Lambda ~ ) ~ } , \mathrm { ~ ( \Lambda ~ ) ~ } , \mathrm { ~ ( \Lambda ~ ) ~ } , \mathrm { ~ ( \Lambda ~ ) ~ } , \mathrm { ~ ( \Lambda ~ ) ~ } , \mathrm { ~ ( \Lambda ~ \Lambda ~ ) ~ } , \mathrm { ~ ( \Lambda ~ \Lambda ) ~ } , \mathrm { ~ ( \Lambda ~ \Lambda ) ~ } , \mathrm  ~ ( \Lambda \Lambda ) ~ ~ ( \Lambda  \end{array}
$$

● Short termination

$$
\scriptstyle \longrightarrow \overbrace { \sum _ { \mathrm { t } _ { \mathrm { d } } = 1 \land \mathrm { s } } \sum _ { \mathrm { ~ } \forall \mathrm { ~ } \tau } } ^ { Z _ { 0 } = 5 0 \Omega } = \Big \bigcup _ { \mathrm { ~ } } Z _ { \tau } = \mathtt { s h o r t }
$$

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/793e5b7c6a2ed2e5e5d54ce0d7ce0d22edc9aaa7f8d2388c2f8ad4d6ef06000c.jpg)

## TDR Waveforms (Matched & Mismatched)

Matched termination

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/038adfaecc603db4b27ac95b8f56451911f535fa1d6972e43c6b433f3ff48ccf.jpg)

● Mismatched termination

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/220dc142ed3dfb1603b8d40d7ea323518706ac283185c58be912db14f7bea809.jpg)

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/5253d8127c99f219727c3e4fdfb45f9f68a9885335d6f820ccb95a50b43eb20e.jpg)

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/3990ac5fa1f18bdadae6925c58d051328fbdc42b61e6fc3e3e1e41487aed8708.jpg)

## TDR Waveforms (C & L Discontinuity)

• Shunt C discontinuity

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/b2ff190af0312e15d75ad766d95497265d9f6507769ff22a52a8c58a461527a7.jpg)

● Series L discontinuity

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/6c07349e148dcc26d362c4a56023b28afd73523af8f9d70fff406e34e5ee4d3b.jpg)

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/7c4b01c2c0e801cfe7ba3d87c0ccf936f8bdb36a933672dd670f89ade66e6920.jpg)

$$
\cdot \cdot \mathbf { l }
$$

Peak voltage spike magnitude:

$$
\boxed { \frac { \Delta V } { V } = \left( \frac { \tau } { t _ { r } } \right) \left[ 1 - e ^ { \left( - \frac { t _ { r } } { \tau } \right) } \right] }
$$

## TDR Rise Time and Resolution

• TDR spatial resolution is set by step risetime

$$
\boxed { \Delta x > t _ { r } \upsilon }
$$

Step risetime degrades with propagation through channel

Dispersion from skin-effect

Lump discontinuities low-pass filter the step

Causes difficulty in estimating L & C values

● Channel filtering can actually compensate for lump discontinuity spikes ©

## TDR Multiple Reflections

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/37ca94d973d68123e45865a84d1a9ce634d21e3314b78ebbf869c16e90fe4fb4.jpg)

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/d0dceff5833b80b1e8588950c1926a41a462819386cde62fa7516ee6667a4b94.jpg)

## TDR Waveforms (Multiple Discontinuities)

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/42afd56b6c21645387cde06d079805e122382e34b0c410598bdbcf3314f8c071.jpg)

## Time-Domain Transmission (TDT)

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/92968e75b8198149183fcfed4fbc8cdd12e9e5202ef1cee0a7adad184e6f8bfe.jpg)

● Can measure channel transfer function

$$
H { \left( j \omega \right) } = { \frac { V _ { 2 } { \left( j \omega \right) } } { V _ { 1 } { \left( j \omega \right) } } }
$$

Hard to isolate impedance discontinuities, as they are superimposed on a single rising edge

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/61535879816b24685cefa7f94b555abda59d1d812da91cedc512d0779a8c547e.jpg)

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/4ce4f994a97d366e4d4c81892f09684454e6e54072187c3e18837f1c97f75c5d.jpg)

## Network Analyzer

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/a0ef9806bc9db624d779f1f94c7d99c3060405336545e5d18dc87410774e2038.jpg)

• Stimulates network with swept-frequency source

• Measures network response amplitude and phase

● Can measure transfer function, scattering matrices, impedance, …

● Test set is configured differently for each kind of measurement to be performed

## Directional Coupler

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/3ed8fca769aa26343d2049b8f5a684ba28b53171daba45d99c7ab5c4c3fb11d7.jpg)  
Direction Coupler  
[Dally]

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/3a8c4e1afb238c62364ee226b291135af043cc4a9c24ea7d28b87db1967f54ae.jpg)

• Test sets in high-frequency network analyzers make use of directional couplers

• Directional couplers are two transmission lines coupled over a short distance

● If the short line is properly terminated, it allows for the voltage across $Z _ { \mathsf { A } }$ to be proportional to the forward traveling wave and the voltage across $Z _ { B }$ to be proportional to any reflected wave

## Transfer Function & Impedance Measurements

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/c9337e5f990591e62587fc5a74c8d00f541a3d02ce5d2546f3d060536cc1ad85.jpg)  
Test Set for Transfer Function

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/ee08c8e36ef49f49a226b854e1bff24ee97ba911d9d6d2c68f8138489e59cd16.jpg)  
Test Set for Impedance Measurements

Transfer function measurement

The input signal is from a directional coupler which samples the forward traveling wave

The network output serves as the output

Impedance measurement

The input signal is from a directional coupler which samples the forward traveling wave

The reflected wave from the network is compared with this input to characterize the impedance over frequency

## Scattering (S) Parameters

● Why S Parameters?

• Easy to measure

Y, Z parameters need open and short conditions

S parameters are obtained with nominal termination

• S parameters based on incident and reflected wave ratio

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/381c16e355917a0cca27b58d8542889977a6ce4b07dad2955a3b03fecf9d0f2c.jpg)

$$
{ \Bigg [ } B _ { 1 } { \Bigg ] } = { \Bigg [ } S _ { 1 1 } \ S _ { 1 2 } { \Bigg ] } \cdot { \Bigg [ } A _ { 1 } { \Bigg ] }
$$

S-matrix

[Dally]

## Formal S-Parameter Definitions

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/19bf56d81e112c7078c9cd7dc1c281b73e464241d0fbb5e9428886e025eade73.jpg)

[Agilent]

$\left. \mathsf { s } _ { 1 1 } = \frac { \mathsf { b } _ { 1 } } { \mathsf { a } _ { 1 } } \right| _ { \mathsf { a } _ { 2 } = 0 } =$ Input reflection coefficient with the output port terminated by a matched load $( Z _ { \mathrm { L } } { = } Z _ { 0 }$ sets $\mathsf { a } _ { 2 } \overset { \vartriangle } { = } 0 )$

$\left. \mathsf { s } _ { 2 2 } \mathrm { = } \frac { \mathsf { b } _ { 2 } } { \mathsf { a } _ { 2 } } \right| _ { \mathsf { a } _ { 1 } \mathrm { = 0 } } =$ Output reflection coefficient with the input terminated by a matched load $( \mathrm { Z } _ { \mathrm { S } } { = } \mathrm { Z } _ { 0 }$ sets $ { \mathrm { V _ { s } } } = 0 )$

$\mathbf { s } _ { 2 1 } = { \frac { \mathbf { b } _ { 2 } } { \mathbf { a } _ { 1 } } } { \bigg | } _ { \mathbf { a } _ { 2 } = 0 } =$ Forward transmission (insertion) gain with the output port terminated in a matched load.

$\mathbf { s } _ { 1 2 } = { \frac { \mathbf { b } _ { 1 } } { \mathbf { a } _ { 2 } } } { \bigg | } _ { \mathbf { a } _ { 1 } = 0 } =$ Reverse transmission (insertion) gain with the input port, terminated in a matched load.

## Cascading S-Parameters

● Network analysis allows cascading of independently characterized structures

● However, can't directly cascade sparameter matrices and multiply

Must first convert to an ABCD matrix (or T matrix)

## ABCD Parameters

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/9a08bfbefc785ab52af5b0de901b5badbefb16d7ef71894b72ca096261ec1620.jpg)

$$
A = \frac { \nu _ { 1 } } { \nu _ { 2 } } \bigg | _ { i _ { 2 = 0 } } \ B = \frac { \nu _ { 1 } } { i _ { 2 } } \bigg | _ { \nu _ { 2 = 0 } } \ C = \frac { i _ { 1 } } { \nu _ { 2 } } \bigg | _ { i _ { 2 = 0 } } \ D = \frac { i _ { 1 } } { i _ { 2 } } \bigg | _ { \nu _ { 2 = 0 } }
$$

$$
\left| { \begin{array} { c } { \nu _ { 1 } } \\ { i _ { i } } \end{array} } \right| = \left| { \begin{array} { c c } { A } & { B } \\ { C } & { D } \end{array} } \right| \bullet \left| { \begin{array} { c } { \nu _ { 2 } } \\ { i _ { 2 } } \end{array} } \right|
$$

## Converting Between S & ABCD Parameters

TABLE 9-3. Relationships Between Two-Port S and ABCD Parametersa

$$
 \left[ { \begin{array} { l l } { S _ { 1 1 } } & { S _ { 1 2 } } \\ { S _ { 2 1 } } & { S _ { 2 2 } } \end{array} } \right] \qquad { \left[ \begin{array} { l l } { { \displaystyle { \frac { B - Z _ { n } ( D - A + C Z _ { n } ) } { B + Z _ { n } ( D + A + C Z _ { n } ) } } } } & { { \displaystyle { \frac { 2 Z _ { n } ( A D - B C ) } { B + Z _ { n } ( D + A + C Z _ { n } ) } } } } \\ { { \displaystyle { \frac { 2 Z _ { n } } { B + Z _ { n } ( D + A + C Z _ { n } ) } } } } & { { \displaystyle { \frac { B - Z _ { n } ( A - D + C Z _ { n } ) } { B + Z _ { n } ( D + A + C Z _ { n } ) } } } } \end{array} \right] }
$$

$$
{ \left[ \begin{array} { l l } { A } & { B } \\ { C } & { D } \end{array} \right] } \qquad { \left[ \begin{array} { l l } { { \frac { ( 1 + S _ { 1 1 } ) ( 1 - S _ { 2 2 } ) + S _ { 1 2 } S _ { 2 1 } } { 2 S _ { 2 1 } } } } & { { Z _ { n } } { \frac { ( 1 + S _ { 1 1 } ) ( 1 + S _ { 2 2 } ) - S _ { 1 2 } S _ { 2 1 } } { 2 S _ { 2 1 } } } } \\ { { \frac { 1 } { Z _ { n } } } { \frac { ( 1 - S _ { 1 1 } ) ( 1 - S _ { 2 2 } ) - S _ { 1 2 } S _ { 2 1 } } { 2 S _ { 2 1 } } } } & { { \frac { ( 1 - S _ { 1 1 } ) ( 1 + S _ { 2 2 } ) + S _ { 1 2 } S _ { 2 1 } } { 2 S _ { 2 1 } } } } \end{array} \right] }
$$

${ } ^ { a } Z _ { n }$ is the termination impedance at the ports.

[Hall]

## Example: Cascaded Via & Transmission Line

$$
\left[ S _ { 1 1 } \quad S _ { 1 2 } \right] _ { \mathrm { v i a } } = \left[ { { - 0 . 1 2 3 5 - j 0 . 1 5 1 6 } \quad \quad 0 . 7 5 9 7 - j 0 . 6 1 9 0 } \right]
$$

$$
\begin{array} { r l r } {  { \sum _ { z = - 1 } ^ { \mathsf { N } } \frac { Z _ { 0 } } { Z = - 1 } \frac { \beta } { Z = 0 } \sqrt { \mathsf { N } } } } & { \overset { R } { = } } & { [ \begin{array} { l l } { S _ { 1 1 } } & { S _ { 1 2 } } \\ { S _ { 2 1 } } & { S _ { 2 2 } } \end{array} ] _ { \mathrm { t r i n e } } = [ \begin{array} { l l } { 0 . 0 0 3 2 5 - j 0 . 0 0 3 2 3 } & { - 1 . 0 0 - j 0 . 0 0 3 2 } \\ { - 1 . 0 0 - j 0 . 0 0 3 } & { 0 . 0 0 3 2 5 - j 0 . 0 0 3 2 } \end{array} ] } \\ & { \equiv } & { [ \begin{array} { l l } { A } & { B } \\ { C } & { D } \end{array} ] _ { \mathrm { t r i n e } } = [ \begin{array} { l l } { - 1 } & { j 0 . 3 2 2 8 } \\ { j 0 . 0 0 0 1 2 9 } & { - 1 } \end{array} ] } \end{array}
$$

$$
{ \underset { = } { \overset { R } { \leq } } { \overset { \iff } { \sum } } \ } { \underset { = } { \overset { Z _ { 0 } } { \longrightarrow } } \ } { \overset { \beta } { \underset { = } { \overset { \beta } { \longrightarrow } } } { \longrightarrow } }  \underset { = } { \overset { } { \beta } } { \overset { } { \longrightarrow } } { \underset { = } { \overset { } { \beta } } { \longrightarrow } } { \overset { } { \beta } } { \underset { = } { \overset { } { \beta } } { \longrightarrow } }  \overset { } { \beta } { \underset { = } { \overset { } { \beta } } { \longrightarrow } } { \overset { } { \beta } } { \underset { = } { \overset { } { \beta } } { \longrightarrow } } { \overset { } { \beta } { \ Z _ { \mathrm { \pm \pm \pm \pm \beta } } } } = { \overset { } { \alpha } } { \overset { B } { \ Z } } { \overset { } { \ Z } } { \underset { = } { \overset { } { \ Z } } { \ Z } } { \overset { } { \ Z } } { \underset { = } { \overset { } { \beta } } { \ Z } } { \overset { } { \ Z } } { \underset { = } { \overset { } { \beta } } { \ Z } }
$$

● Taken from "Advanced Signal Integrity for High-Speed Digital Designs" by Hall

## Example: Cascaded Via & Transmission Line

$$
\begin{array} { r l r l } { \underset { \stackrel { \{ } = } { = } } { \overset { { \sum \sum } } { \sum } }  & { \quad \quad \quad \quad z _ { 0 } } & & { \beta } & { \quad \quad \quad \quad \quad \left[ \begin{array} { l l } { A } & { B } \\ { C } & { D } \end{array} \right] _ { \mathrm { c a s c a d e } } = \left[ \begin{array} { l l } { A } & { B } \\ { C } & { D } \end{array} \right] _ { \mathrm { v i a } } \left[ \begin{array} { l l } { A } & { B } \\ { C } & { D } \end{array} \right] _ { \mathrm { t i n e } } } \\ & { \quad \quad \quad \quad \quad \quad \overset { { \sum } } { = } { \overset { { \sum \operatorname { } } } { = } { } } } & & { \quad = \left[ \begin{array} { l l } { 0 . 7 9 0 } & { j 2 2 . 2 2 } \end{array} \right] \cdot \left[ \begin{array} { l l } { - 1 } & { j 0 . 3 2 8 } \\ { j 0 . 0 0 0 1 2 9 } & { - 1 } \end{array} \right] } \\ & { } & & { \quad \quad \quad \quad = \left[ \begin{array} { l l } { - 0 . 7 9 0 } & { - j 2 1 . 9 6 5 } \\ { - j 0 . 0 1 6 8 6 } & { - 0 . 7 9 5 } \end{array} \right] } \end{array}
$$

● Using conversion table:

$$
{ \left[ \begin{array} { l l } { S _ { 1 1 } } & { S _ { 1 2 } } \\ { S _ { 2 1 } } & { S _ { 2 2 } } \end{array} \right] } _ { \mathrm { c a s c a d e } } = { \left[ \begin{array} { l l } { - 0 . 1 2 5 9 - j 0 . 1 5 5 3 } & { - 0 . 7 6 3 5 + j 0 . 6 1 8 6 } \\ { - 0 . 7 6 4 5 + j 0 . 6 1 8 2 } & { - 0 . 1 2 0 0 - j 0 . 1 5 6 5 } \end{array} \right] }
$$

● Can also use T matrixes to cascade

• Taken from "Advanced Signal Integrity for High-Speed Digital Designs" by Hall

## S-Parameter Channel Example

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/048d1281389b65e7716bf8b9a403564714a8f605ef87ced175b028c5aed09646.jpg)  
[Peters, IEEE Backplane Ethernet Task Force]

# S-Parameter Channel Example (4-port differential)

<table><tr><td colspan="9">petexs_01_060sxzolchanne1 thxu reaponse</td></tr><tr><td>HZ S</td><td>RI</td><td>R 50</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>FREQ</td><td>s11 S21</td><td>S12 S22</td><td></td><td>S23 S13</td><td>S14</td><td></td><td></td><td></td></tr><tr><td></td><td>531</td><td>532</td><td></td><td>533</td><td>534 824</td><td></td><td></td><td></td></tr><tr><td></td><td>541</td><td>S42</td><td></td><td>543</td><td>544</td><td></td><td></td><td></td></tr><tr><td></td><td>REAL IMAG</td><td>REAL</td><td>IMAG</td><td>REAL IMAG</td><td>REAL IHAG</td><td></td><td></td><td></td></tr><tr><td>5.00000000e+007</td><td>6.279266901548e-002</td><td>-5.256007502766e-002</td><td>-1.995363973143e-001</td><td>-9.018006169275e-001</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>-1,993592781969e-001</td><td>-9.017752677900e-001</td><td>6.847049395661e-002</td><td>-3,537762509466e-002</td><td>6,592975593456e-004 7.405252014369e-002</td><td>-1.653914717779e-002 2.600793690373e-003</td><td>4.694410796534e-004</td><td>2.855671737566e-003</td></tr><tr><td></td><td>7.438370524663e-002</td><td>−1.650568516548e-002</td><td>6.663957537997e-004</td><td>2.723661634513e-003</td><td>5.641343731365e-002</td><td>-5.693035032892e-002</td><td>7.478976460177e-002 −2.070369894915e-001 -8.986367167361e-001</td><td>-1,488182269791e-002</td></tr><tr><td></td><td>3.380698172980e-004</td><td>2.715033111885e-003</td><td>7.497765935351e-002</td><td>-1.188516535615e-002</td><td>-2.063514808970e-001</td><td>-9.002700655371e-001</td><td>6.856095801756e-002</td><td>-3.019606086420e-002</td></tr><tr><td>6.00000000e+007</td><td>4.829977376755e-002</td><td>-6.288238652440e-002</td><td>-4.923832497425e-001</td><td>-7.721510464035e-001</td><td>6.298956599590e-002</td><td>-3.938489680891e-002</td><td>1.125377257145e-003</td><td>1.921732299021e-003</td></tr><tr><td></td><td>-4.925547500023e-001</td><td>-7.726263821707e-001</td><td>6.163450406360e-002</td><td>-4.486265928179e-002</td><td>1.299644022342e-003</td><td>1.492436402394e-003</td><td>6.462146347807e-002</td><td>-3.736630924981e-002</td></tr><tr><td></td><td>6.308085276969e-002</td><td>-3.947655302643e-002</td><td>1.386741613180e-003</td><td>1.653454474207e-003</td><td>4.393874455850e-002</td><td>-6.448913049207e-002</td><td>-4.992743919180e-001</td><td>-7.660808533046e-001</td></tr><tr><td></td><td>1.280875740087e-003</td><td>1.936760526874e-003</td><td>6.482369657086e-002</td><td>-3.743006383763e-002</td><td>-4.995203164654e-001</td><td>-7.674804458241e-001</td><td>6.284893613667e-002</td><td>-4.132139739274e-002</td></tr></table>

## Data from 50MHz to 15GHz in 10MHz steps

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/29e857ec4cec66ce42967caba8303248e414dd59febc635fc1dfde9b74d87700.jpg)

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/54949fbe5ec3f21df8e98b3726cfff371d9e33822cbde9d11b64bdb1a95c576b.jpg)

$$
\begin{array} { r l r } { \underset { { \bf { \overline { { { e } } } } } } { \Longleftrightarrow } \underset { { \bf { \overline { { { e } } } } } } {  } \underset { { \bf { \overline { { { e } } } } } } {  } \underset { { \bf { \overline { { { e } } } } } } { \bf { \overbrace { { { P _ { 0 1 } } } } } } , ~ } & { { \bf { \overline { { { P o u t 2 } } } } } \underset { { \bf { \overline { { { \Psi } } } } } } {  } \underset { { \bf { \overline { { { \Psi } } } } } } {  } \quad } & { { \bf { \overline { { { W } } } } } } \\ { \underset { { \bf { \overline { { { e } } } } } } { \cong } \quad } & { { \bf { \overline { { { P _ { 0 1 } } } } } } } & { { \bf { \overline { { { { \Psi _ { 0 1 } } } } } } } } \\ { { \bf { \overline { { { { \Psi _ { 0 1 } } } } } } } } & { { \bf { \overline { { { \Psi _ { { 0 1 } } } } } } } } & { { \bf { \overline { { { \Psi _ { { 0 1 } } } } } } } } \\ { { { \bf { \overline { { { { \Psi _ { 4 1 } } } } } } } } } & { { \bf { { \overline { { { \Psi _ { { 4 2 } } } } } } } } } & { { \bf { \overline { { { { \Psi _ { 4 4 } } } } } } } } & { { \bf { \overline { { { \Psi _ { { 4 } } } } } } } } \end{array} \quad \quad \quad \begin{array} { r l }  [ \begin{array} { l } { { \mit { \tilde { b } _ { 1 } } } } \\  { \mit { \bf { b } _ { 2 } } } \\ { { \mit { \cal { b } _ { 3 } } } \\ { \mit { \cal { b } _ { 4 } } } \end{array} } ] = [ \begin{array} { l l l l } { { \mit { \tilde { S } _ { 1 1 } } } } & { { \mit { \cal { S } } _ { 1 2 } } } &   \mit  \cal  S  \end{array} \end{array}
$$

$$
S _ { d d 1 1 } = { \frac { b _ { d 1 } } { a _ { d 1 } } } \bigg | _ { a _ { 2 } = a _ { 4 } = 0 } = { \frac { 1 } { 2 } } \big ( S _ { 1 1 } + S _ { 3 3 } - S _ { 1 3 } - S _ { 3 1 } \big )
$$

$$
S _ { d d 2 1 } = { \frac { b _ { d 2 } } { a _ { d 1 } } } \Bigg | _ { a _ { 2 } = a _ { 4 } = 0 } = { \frac { 1 } { 2 } } \big ( S _ { 2 1 } + S _ { 4 3 } - S _ { 2 3 } - S _ { 4 1 } \big )
$$

## S-Parameter Channel Example

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/f4782df860aff278635b072ad589fd6d70516dfe983b7a8a3305c73abf355152.jpg)

## Impulse Response

● Channel impulse responses are used in

Time domain simulations

Link analysis tools

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/7a55178a701364606f49c8908067b23e94864b2ebbeb6bd97efce3981e34110e.jpg)  
Y(ω)= H(ω)X(ω)

$$
y ( t ) = h ( t ) \ast x ( t ) = \intop _ { - \infty } ^ { \infty } h ( t - \tau ) x ( \tau )
$$

$$
h ( t ) = F ^ { - 1 } \left\{ H ( w ) \right\}
$$

## Generating an Impulse Response from S-Parameters

● Perform the inverse Fourier transform on the s-parameter of interest

● Step 1: For ifft, produce negative frequency values and append to sparameter data in the following manner

$$
S ( - f ) { = } S ( f ) ^ { * }
$$

$$
h ( t ) = F ^ { - 1 } \left\{ S ( \omega ) \right\}
$$

T20 Backplane Channel  
![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/0c41d3ce3ed9962ad46faf303c0bf144aa3eada403eccb852a4c8706d054d97e.jpg)

## Increasing Impulse Response Resolution

● Could perform ifft now, but will get an impulse response with time resolution of

$$
\frac { 1 } { 2 f _ { \mathrm { m a x } } } = \frac { 1 } { 2 \big ( 1 5 \mathrm { G H z } \big ) } = 3 3 . 3 \mathrm { p s }
$$

• To improve impulse response resolution expand frequency axis and "zero pad"

For 1ps resolution: zero pad to +/-500GHz

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/03decb4299c784d07cbe4638450d44cefecc4a5a473c7d171bba14494aee22be.jpg)

## Channel Impulse Response

• Now perform ifft to produce impulse response

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/7a8478e99bba8682c885ddf6016b7d7f9602877d69402ea61fa75f1f12ca8b92.jpg)

● Can sanity check by doing an fft on impulse response and comparing to measured data

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/5151996b1e5fec9803f7f1e114dff8d888175eea234892b16223772b1f5c8309.jpg)

## Impulse Response of Different Channels

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/c00c33a3ba9af4eec00f74fe8608ba2f76a48ba7a30e4c90626699b1a5ca67a8.jpg)

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/e895a4da423d4510b693f8a003492819706fdadae8fadeecb056f3cea5bfd104.jpg)

## Channel Transient Response

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/9554a35c084ef515a75baf3b42e5d41c638ce92fb2915a426bda6f74fa63cad2.jpg)

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/34827964a195f1b2bd7fd232576864367c52f8787f846d6ffd9b704d3f9eef9d.jpg)

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/71a812f3a9168fddbe4fbf8ff3249bd2b88d18df8c171d2545aa4d2c845d10a6.jpg)

## Eye Diagrams

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/3772cefccc32d6331b60988924d7f03b977ca8a39515f8ab57c633f8d821bdf0.jpg)

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/a88ee6a9fea811bedf4b7aadf5b49f8f2600d07b6a53ccb0bed61699bbb61f39.jpg)

Use a precise clock to chop the data into equal periods

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/604c683925726ab6f37ab1ff75a20ffb5b0eeab2aaf5f048bc700aac6ef4dab0.jpg)

overlay each period onto one plot

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/cb4fb888c2cea53953fcae3c4e18cca4c227dde103af57477dff47b24419b441.jpg)

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/e8ce7e5c856fa464bd9fb888d29bb1c727203772bef3e9390d24925b734674c2.jpg)

## Eye Diagrams vs Data Rate

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/92d58121a35121f7d5f08ceba52d1019936c9a4972ce9fd423fdf0d5bbfd3055.jpg)

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/d2ab789ba4090a480ac97625080281817c989de760e6ccb5d3e177689b771c09.jpg)

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/f1656facb383929434b0c90bafe0158f1833ea857cc36d93223cb965a2074cbc.jpg)

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/55d212cb87562810db5cf43569f30c832895028b49e3c26c5d673f3308da3051.jpg)

## Eye Diagrams vs Channel

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/38f660c6d53f9acc9a187a575eacf0b0d6f58ca6ed6a4a4a92fb5ebc80f71a79.jpg)

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/dffb7b69b50bf44a9c7daa53af521a1d62b6665ed1547c9da687829e7ae0af15.jpg)

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/773aea5549da80e5c38fd19b32cf30c866c05224c19e2f1ed648d6130126f655.jpg)

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/f346986102a4ca551478be72b62267eb49a54d4d60dac1aa3e3f8f03d6512f24.jpg)

## Inter-Symbol Interference (ISI)

• Previous bits residual state can distort the current bit, resulting in inter-symbol interference (ISI)

• ISI is caused by

Reflections, Channel resonances, Channel loss (dispersion)

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/0ce804a48f26ada97527053f8421852e60691339136c218d7659978f822ea838.jpg)

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/d2e56bc4099d6eebe98a253bc1d5989759603a926925247e4b09a03d26e8e25e.jpg)

## ISI Impact

● At channel input (TX output), eye diagram is wide open

As data pulses propagate through channel, they experience dispersion and have significant ISI ● Result is a closed eye at channel output (RX input)

![](/img/mineru_output/lecture3_ee720_tdr_spar/auto/images/0e86b9fc1b1f8df0bd2b8a3fd69e717f4649e1b199f1fb2d4efb393021b0779b.jpg)  
[Meghelli (IBM) ISSCC 2006]

## Next Time

● Channel pulse response model

• Modulation schemes