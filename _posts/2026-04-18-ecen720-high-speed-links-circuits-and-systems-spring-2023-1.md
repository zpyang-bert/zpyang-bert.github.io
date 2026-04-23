---
layout: post
title:      "ECEN720: High-Speed Links Circuits and Systems Spring 2023"
date:       2026-04-18 17:44:54
author:     "Bert"
tags:
  - Channel
  - Lecture
  - Mineru
---
Lecture 4: Channel Pulse Model & Modulation Schemes

![](/img/mineru_output/lecture4_ee720_channel_pulse_model/auto/images/fa0cc3f2e9e3a0d3cf373b013792dd68695c967b31c15b6611de2a31b92a3200.jpg)

Sam Palermo Analog & Mixed-Signal Center Texas A&M University

## Announcements

## ● Lab 2 report and Prelab 3 due Feb 13

## ● Reference material

• Peak distortion analysis paper by Casper

· Notes from H. Song, Arizona State

Papers posted on PAM-2/4 transceivers

## Agenda

• ISI and channel pulse model

● Peak distortion analysis

• Compare NRZ (PAM-2) and PAM-4 modulation

## Inter-Symbol Interference (ISI)

• Previous bits residual state can distort the current bit, resulting in inter-symbol interference (ISI)

ISI is caused by

Reflections, Channel resonances, Channel loss (dispersion)

• Pulse Response

$$
y ^ { ( 1 ) } ( t ) = c ^ { ( 1 ) } ( t ) * h ( t )
$$

![](/img/mineru_output/lecture4_ee720_channel_pulse_model/auto/images/7a684820f9e98d2b42942ac5a69c730da4161e066670a13253bc5a495154160b.jpg)

![](/img/mineru_output/lecture4_ee720_channel_pulse_model/auto/images/d91680174a96f4a2578cb4f2cadd78fe327ad16fa56e761634320158cbb523b9.jpg)

![](/img/mineru_output/lecture4_ee720_channel_pulse_model/auto/images/ccfd8cddf5a16f071080d869f9093a29b101c3a4c721cfd18d6aa5eb7cc0c420.jpg)

## NRZ Data Modeling

An NRZ data stream can be modeled as a superposition of isolated $\yen 123$ and $\ " 0 \%$

"1" Symbol

$$
\pm 1 \boxed { \begin{array} { r l } & { \underset { \{ 1 \} } { \overset { \mathsf { T } } { \longrightarrow } } } \\ & { \underset { \mathbf { k } } { \overset { \mathsf { k } } { \longrightarrow } } \quad \mathbf { t } \boldsymbol { \mathsf { T } } } \end{array} } \quad \begin{array} { r l } &  c _ { k } ^ { ( 1 ) } ( t ) \equiv u \big ( t - k T \big ) - u \big ( t - \big ( k + 1 \big ) T \big ) \end{array}
$$

"0" Symbol

$$
\frac { 1 \times \frac { k + 1 } { \pi } } { \pi } , t / \pi
$$

$$
c _ { k } ^ { ( 0 ) } ( t ) = - c _ { k } ^ { ( 1 ) } ( t )
$$

[Song]

where

$$
u ( t ) \equiv \left\{ { \begin{array} { l l } { 1 } & { t \geq 0 } \\ { 0 } & { t < 0 } \end{array} } \right.
$$

## NRZ Data Modeling

An NRZ data stream can be modeled as a superposition of isolated "1"s and $" 0 ^ { \prime \prime }$ S

![](/img/mineru_output/lecture4_ee720_channel_pulse_model/auto/images/6a63f2e77a0a1c47c49052f65462c6d517fb9309591ac9cd7de6880dae1b9bdb.jpg)  
[Song]

![](/img/mineru_output/lecture4_ee720_channel_pulse_model/auto/images/3e3d7be12cd7a2336c2e3225bdf5b69a2245c7576fe538800ee7a113e21adfc7.jpg)

$$
V _ { i } ( t ) = \sum _ { k = - \infty } ^ { \infty } c _ { k } ^ { ( d _ { k } ) } ( t )
$$

## Channel Response to NRZ Data

• Channel response to NRZ data stream is equivalent to superposition of isolated pulse responses

![](/img/mineru_output/lecture4_ee720_channel_pulse_model/auto/images/6024baa95190df46372e26b58c25c729d5c3718de7fe22ccfeb61fbf0f5237fd.jpg)

[Song]

$$
V _ { o } ( t ) = H ( V _ { i } ( t ) ) = \sum _ { k = - \infty } ^ { \infty } H ( c _ { k } ^ { ( d _ { k } ) } ( t ) ) = \sum _ { k = - \infty } ^ { \infty } y ^ { ( d _ { k } ) } ( t - k T )
$$

## Channel Pulse Response

![](/img/mineru_output/lecture4_ee720_channel_pulse_model/auto/images/a53b37868272527c6548e972378fb8eeb08d5f60f3485675fea007173713668b.jpg)

## Channel Data Stream Response

Input Data Stream  
![](/img/mineru_output/lecture4_ee720_channel_pulse_model/auto/images/50fb3bf631182d5bd62e3e4d8eb405abb7a8f6fbbd420c2c9dbb25213d3f3ddd.jpg)

Pulse Responses  
![](/img/mineru_output/lecture4_ee720_channel_pulse_model/auto/images/5a0e3a7412d93ba095ea59bbbec87fd79a5842ce5f78fc442145bb2ff4cef91e.jpg)  
Channel Response

![](/img/mineru_output/lecture4_ee720_channel_pulse_model/auto/images/093f2f60085e9dbb238d97f557dbeed59383014e0b3f154ff03ea1331972615d.jpg)

## Channel "FIR"Model

![](/img/mineru_output/lecture4_ee720_channel_pulse_model/auto/images/99e1b3aba9304982b642b3b550127344356cb8464df811a32f5782948bd349de.jpg)

![](/img/mineru_output/lecture4_ee720_channel_pulse_model/auto/images/bbfc01d51719868d5a137b8405aa06398f135e3c881ec7e84817d5a4a1866f06.jpg)

$\mathsf { y } ^ { ( 1 ) } ( \mathsf { t } )$ sampled relative to pulse peak:

$$
[ \dots 0 . 0 0 3 0 . 0 3 6 0 . 5 4 0 0 . 1 6 5 0 . 0 6 5 0 . 0 3 3 0 . 0 2 0 0 . 0 1 2 0 . 0 0 9 \dots ]
$$

$$
\bar { \mathsf { a } } = [ \mathsf { \ldots } \mathsf { a _ { - 2 } } \mathsf { a _ { - 1 } } \mathsf { a _ { - 1 } } \mathsf { a _ { 0 } } \mathsf { a _ { 1 } } \mathsf { a _ { 2 } } \mathsf { a _ { 3 } } \mathsf { a _ { 4 } } \mathsf { a _ { 5 } } \mathsf { a _ { 6 } } \mathsf { a _ { - 2 } } \mathsf { b _ { 6 } } \mathsf { a _ { 6 } } \mathsf { a _ { - 1 } } \mathsf { a _ { 6 } } \mathsf { a _ { - 2 } } \mathsf { b _ { 6 } } \mathsf { a _ { 6 } } \mathsf { a _ { - 2 } } \mathsf { b _ { 6 } } \mathsf { a _ { 6 } } \mathsf { a _ { 6 } } \mathsf { a _ { - 2 } } \mathsf { b _ { 6 } } \mathsf { a _ { 6 } } \mathsf { a _ { 6 } } \mathsf { a _ { - 2 } } \mathsf { b _ { 6 } } \mathsf { a _ { 6 } } \mathsf { a _ { 6 } } \mathsf { a _ { 6 } } \mathsf { a _ { - 2 } } \mathsf { b _ { 6 } } \mathsf { a _ { 6 } } \mathsf { a _ { 6 } } \mathsf { a _ { 6 } } \mathsf { a _ { 6 } } \mathsf { a _ { 6 } } \mathsf { a _ { 6 } } \mathsf { a _ { 6 } } \mathsf { a _ { 6 } } \mathsf { a _ { 6 } } \mathsf { a _ { 6 } } \mathsf { a _ { 6 } } \mathsf { a _ { 6 } } \mathsf { a _ { 6 } } \mathsf { a _ { 6 } } \mathsf { a _ { 6 } } \mathsf { a _ { 6 } } \mathsf { a _ { 6 } } \mathsf { a _ { 6 } } \mathsf { a _ { 6 } } \mathsf { a _ { 6 } } \mathsf { a _ { 6 } } \mathsf { a _ { 6 } } \mathsf { a _ { 6 } } \mathsf { a _ { 6 } } \mathsf { a _ { 6 } } \mathsf { a _ { 6 } } \mathsf { a _ { 6 } } \mathsf { a _ { 6 } } \mathsf { a _ { 6 } } \mathsf { a _ { 6 } } \mathsf { a _ { 6 } } \mathsf { a _ { 6 } } \mathsf { a _ { 6 } } \mathsf { a _ { 6 } } \mathsf { a _ { 6 } } \mathsf  a _ { 6 } 
$$

## Agenda

● ISI and channel pulse model

• Peak distortion analysis

• Compare NRZ (PAM-2) and PAM-4 modulation

## Peak Distortion Analysis

● Can estimate worst-case eye height and data pattern from pulse response

• Worst-case "1" is summation of a "1"pulse with all negative non k=0 pulse responses

$$
\boxed { S _ { 1 } ( t ) = y _ { 0 } ^ { ( 1 ) } ( t ) + \sum _ { { k = - \infty } \atop { k \neq 0 } } ^ { \infty } y ^ { ( d _ { k } ) } \big ( t - k T \big ) \big | _ { y ( t - k T ) < 0 } }
$$

• Worst-case "0" is summation of a "0"pulse with all positive non k=0 pulse responses

![](/img/mineru_output/lecture4_ee720_channel_pulse_model/auto/images/9d705de5fb4574d333cbc656275f144aa3939a662db095dc8cee354970c0cc03.jpg)

$$
\boxed  S _ { 0 } \big ( t \big ) = y _ { 0 } ^ { ( 0 ) } \big ( t \big ) + \sum _ { \stackrel { k = - \infty } { k \neq 0 } } ^ { \infty } y ^ { ( d _ { k } ) } \big ( t - k T \big ) \Big | _ { y ( t - k T ) > 0 \atop }
$$

## Peak Distortion Analysis

Worst-case eye height is ${ \sf s } _ { 1 } ( { \sf t } ) { \sf - s } _ { 0 } ( { \sf t } )$

$$
s ( t ) = s _ { 1 } ( t ) - s _ { 0 } ( t ) = \left( y _ { 0 } ^ { ( 1 ) } ( t ) - y _ { 0 } ^ { ( 0 ) } ( t ) \right) + \left( \sum _ { k = - \infty \atop k \neq 0 } ^ { \infty } y ^ { ( d _ { k } ) } ( t - k T ) \Big | _ { y ( t - k T ) \leq 0 } - \sum _ { k = - \infty } ^ { \infty } y ^ { ( d _ { k } ) } ( t - k T ) \Big | _ { y ( t - k T ) > 0 } \right)
$$

Because $y _ { 0 } ^ { ( 0 ) } ( t ) = - 1 \big ( y _ { 0 } ^ { ( 1 ) } ( t ) \big )$

$$
s ( t ) = 2 { \left( \underbrace { y _ { 0 } ^ { ( 1 ) } { \bigl ( } t { \bigr ) } + \sum _ { k = - \infty } ^ { \infty } y ^ { ( 1 ) } { \bigl ( } t - k T { \bigr ) } { \Bigr | } _ { y ( t - k T ) < 0 } } _ { k \neq 0 } - \sum _ { k = - \infty } ^ { \infty } y ^ { ( 1 ) } { \bigl ( } t - k T { \bigr ) } { \Bigr | } _ { y ( t - k T ) > 0 } \right)}  
$$

• If symmetric $" 1 ^ { \prime \prime }$ and $\ " 0 \prime \prime$ pulses (linearity), then only positive pulse response is needed

## Peak Distortion Analysis Example 1

![](/img/mineru_output/lecture4_ee720_channel_pulse_model/auto/images/6d8e4e83ebd9c0713c8af8043f2ae90251b9f53ff2a28674271a787fe5b786dd.jpg)

$$
\begin{array} { c } { { y _ { 0 } ^ { ( 1 ) } ( t ) = 0 . 5 4 0 } } \\ { { \displaystyle \sum _ { k = - \infty } ^ { \infty } y ^ { ( 1 ) } \big ( t - k T \big ) _ { | y ( t - k T ) \times 0 } = - 0 . 0 0 7 } } \\ { { \displaystyle \sum _ { k = - \infty } ^ { \infty } y ^ { ( 1 ) } \big ( t - k T \big ) _ { | y ( t - k T ) \times 0 } = 0 . 3 8 9 } } \\ { { \displaystyle k \approx 0 } } \\ { { s ( t ) = 2 \big ( 0 . 5 4 0 - 0 . 0 0 7 - 0 . 3 8 9 \big ) = 0 . 2 8 8 } } \end{array}
$$

![](/img/mineru_output/lecture4_ee720_channel_pulse_model/auto/images/36d1b244ccb419fd073d84d4056a2ff59e00318f72237721435af945264b27fc.jpg)

![](/img/mineru_output/lecture4_ee720_channel_pulse_model/auto/images/484f18833dcf73bd5989273b79afa74688cbe05b9d1d1bef3ffa988b98c5e326.jpg)

## Worst-Case Bit Pattern

Pulse response can be used to find the worst-case bit pattern

$$
{ \mathrm { P u l s e } } \quad { \mathrm { \bf { a } } } = \left[ \dots \ a _ { - 2 } \quad a _ { - 1 } \quad a _ { 0 } \quad a _ { 1 } \quad a _ { 2 } \quad a _ { 3 } \quad a _ { 4 } \quad a _ { 5 } \quad a _ { 6 } \ \dots \right]
$$

● Flip pulse matrix about cursor $\mathtt { a } _ { 0 }$ and the bits are the inverted sign of the pulse ISI

$$
\left[ \ldots - s i g n ( a _ { 6 } ) - s i g n ( a _ { 5 } ) - s i g n ( a _ { 4 } ) - s i g n ( a _ { 3 } ) - s i g n ( a _ { 2 } ) - s i g n ( a _ { 1 } ) \quad - s i g n ( a _ { 1 } ) \quad 1 - s i g n ( a _ { - 1 } ) \quad - s i g n ( a _ { - 2 } ) \ldots \right]
$$

Worst-Case Bit Pattern Eye

![](/img/mineru_output/lecture4_ee720_channel_pulse_model/auto/images/908a127d1730c8d7798425e143c00f84cdfe7a5f9fcea9dc3debe5ace30b4937.jpg)  
10kbits Eye

![](/img/mineru_output/lecture4_ee720_channel_pulse_model/auto/images/38e7ee91680f3a1302df7dbd956007c27113b103b0bbdd33713aba4a1cb4136a.jpg)

## Peak Distortion Analysis Example 2

![](/img/mineru_output/lecture4_ee720_channel_pulse_model/auto/images/99bb5a9630bf73f56c627ba67c344dd55b96e61ce1a72049c286c412d1b749a2.jpg)

![](/img/mineru_output/lecture4_ee720_channel_pulse_model/auto/images/5974695fbf79c881ce6fa40cf9117076020c077206b526e9fc9d3843c206b19a.jpg)

![](/img/mineru_output/lecture4_ee720_channel_pulse_model/auto/images/f6ca57b25156317d0dd9b776b8ce0977122d4317d20b93d3e7a643c8687f7e9c.jpg)

## Agenda

● ISI and channel pulse model

● Peak distortion analysis

• Compare NRZ (PAM-2) and PAM-4 modulation

## PAM-2 (NRZ) vs PAM-4 Modulation

● Binary, NRZ, PAM-2

Simplest, most common modulation format

● PAM-4

Transmit 2 bits/symbol

Less channel equalization and circuits run ¹/z speed

![](/img/mineru_output/lecture4_ee720_channel_pulse_model/auto/images/4f754ba2749bc8f75cd3d095fd8eb71bebef0c70c7a0845f2178ec2921dafaba.jpg)

![](/img/mineru_output/lecture4_ee720_channel_pulse_model/auto/images/9b87cb1e0741dd80cd6f60fe002b06022851183321f540dbc0911931b1ff2f03.jpg)

## Modulation Frequency Spectrum

![](/img/mineru_output/lecture4_ee720_channel_pulse_model/auto/images/29769b0a53366c8c6ac5e79a993c1d039eb2498237ce2d55cc2037a436d36173.jpg)

![](/img/mineru_output/lecture4_ee720_channel_pulse_model/auto/images/a275a666cfb5c61a68769437226711c491ce48bc029bad564f0bd615d7a33de2.jpg)

![](/img/mineru_output/lecture4_ee720_channel_pulse_model/auto/images/eb9344fd805fcbcf9434f82f797c47a6b16c381718d2d0689996266641b70aa7.jpg)  
Majority of signal power in iGHz bandwidth

![](/img/mineru_output/lecture4_ee720_channel_pulse_model/auto/images/3926db39c76f0bdbe4ed52a85068f99dadd4781bc4f216c0876d8b950b526d8f.jpg)  
Majority of signal power in 0.5GHz bandwidth

## Nyquist Frequency

• Nyquist bandwidth constraint:

● The theoretical minimum required system bandwidth to detect ${ \sf R } _ { \sf S }$ (symbols/s) without ISI is $\mathsf { R } _ { \mathsf { S } } / 2$ (Hz)

• Thus, a system with bandwidth $W { = } 1 / 2 \top { = } \mathsf { R } _ { \varsigma } / 2$ (Hz) can support a maximum transmission rate of $2 \mathsf { W } { = } 1 / \mathsf { T } { = } \mathsf { R } _ { \mathsf { S } }$ (symbols/s) without ISI

$$
\frac { 1 } { 2 T } = \frac { R _ { s } } { 2 } \le W \Rightarrow \frac { R _ { s } } { W } \le 2 ~ \mathrm { ( s y m b o l s / s / H z ) }
$$

For ideal Nyquist pulses (sinc), the required bandwidth is only $\mathsf { R } _ { \mathsf { S } } / 2$ to support an ${ \sf R } _ { \sf S }$ symbol rate

<table><tr><td rowspan=1 colspan=1>Modulation</td><td rowspan=1 colspan=1>Bits/Symbol</td><td rowspan=1 colspan=1>Nyquist Frequency</td></tr><tr><td rowspan=1 colspan=1>NRZ</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1> $\mathsf { R } _ { \mathsf { s } } / 2 { = } 1 / 2 \mathsf { T } _ { \mathsf { b } }$ </td></tr><tr><td rowspan=1 colspan=1>PAM-4</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1> $\mathsf { R } _ { \mathsf { s } } / 2 { = } 1 / 4 \mathsf { T } _ { \mathsf { b } }$ </td></tr></table>

## NRZ vs PAM-4

![](/img/mineru_output/lecture4_ee720_channel_pulse_model/auto/images/41f4996b05ea5a32cd53f9b4354ae3ba883594d75e337a04361e721a507d98cd.jpg)

![](/img/mineru_output/lecture4_ee720_channel_pulse_model/auto/images/1c02a0502e47d582a044ebca57ab5f05f51f76faf07a7a40703c2edc19fcaa2f.jpg)

## • PAM-4 should be considered when

● Slope of channel insertion loss $( \mathsf { S } _ { 2 1 } )$ exceeds reduction in PAM-4 eye height

Insertion loss over an octave is greater than $2 0 ^ { * } \mathsf { l o g } 1 0 ( 1 / 3 ) { = } { \boldsymbol { \cdot } } 9 . 5 4 \mathsf { d } 8$

• On-chip clock speed limitations

## PAM-4 Receiver

![](/img/mineru_output/lecture4_ee720_channel_pulse_model/auto/images/43c3159d87a4a3a103bcabaa80f7e93694c282dc018c6c644ea27d2117180b9c.jpg)

● 3x the comparators of NRZ RX

## NRZ vs PAM-4 – Desktop Channel

![](/img/mineru_output/lecture4_ee720_channel_pulse_model/auto/images/949a9b6c3aeb5ef34fcd22ccb87441ce35b443280c82ec717636758d2708548e.jpg)

● Loss in the octave between 2.5 and 5GHz is only 2.7dB 中 NRZ has better voltage margin

![](/img/mineru_output/lecture4_ee720_channel_pulse_model/auto/images/dc6a4a1a04caed7e2cd77f8f4dc122146a9f1da98f8f2c203a7cd2e7f4a5317c.jpg)

![](/img/mineru_output/lecture4_ee720_channel_pulse_model/auto/images/0bdd82692cb1ed9cfbb10fbbe247ac9ac6ba01ba2a3691a4bb03517ebd4af421.jpg)

## NRZ vs PAM-4 – T20 Server Channel

![](/img/mineru_output/lecture4_ee720_channel_pulse_model/auto/images/4f534313f0beec7dfe535d3baa9e24b1494ad477cc0b0d64c1e6e940b10a4176.jpg)  
• Eyes are produced with 4-tap TX FIR equalization

• Loss in the octave between 2.5 and 5GHz is 15.8dB

PAM-4 "might" be a better choice

![](/img/mineru_output/lecture4_ee720_channel_pulse_model/auto/images/c43db5ab7419df02e0bee5c6f447b519268a94a3cd818747112c23847328b330.jpg)

![](/img/mineru_output/lecture4_ee720_channel_pulse_model/auto/images/bba8cf6f9ca754e0fd09d280c532541acf3fbc4ba7a8bc1d821f1e4791ec6461.jpg)

## PAM-4 Peak Distortion Analysis

![](/img/mineru_output/lecture4_ee720_channel_pulse_model/auto/images/6f3e92b09e51bab9ecf834e539b6ce8810995e5c0624b4725cd0898d9de07840.jpg)

![](/img/mineru_output/lecture4_ee720_channel_pulse_model/auto/images/1ccb6afcf2e2e868f7dd16ca20cbe2246839be8cbe9b66ec67d9436207d546f1.jpg)

Channel pulse response

![](/img/mineru_output/lecture4_ee720_channel_pulse_model/auto/images/b84583b7e8abb2302991b23ef3aea59ad9c813b32e809791de7db83b6b39306b.jpg)

![](/img/mineru_output/lecture4_ee720_channel_pulse_model/auto/images/ab7ca49f6bcce26c32b02196f99f8d4ab374f7b0ef3ca446dd3ac4cf2367c0a4.jpg)

• PAM4 modulation is more sensitive to residual ISI

## Multi-Level PAM Challenges

Receiver complexity increases considerably

3x input comparators (2-bit ADC)

Input signal is no longer self-referenced at OV differential

Need to generate reference threshold levels, which wil be dependent on channel loss and TX equalization

● CDR can display extra jiter due to multiple "zero crossing" times

• Smaller eyes are more sensitive to cross-talk due to maximum transitions

• Advanced equalization (DFE) can allow NRZ signaling to have comparable (or better) performance even with >9.5dB loss per octave

## Modulation Take-Away Points

● Loss-slope guidelines are a good place to start in consideration of alternate modulation schemes

● More advanced modulation trades-off receiver complexity versus equalization complexity

• Advanced modulation challenges

Peak TX power limitations

Setting RX comparator thresholds and controlling offsets

• CDR complexity

• Crosstalk sensitivity (PAM-4)

● Need link analysis tools that consider voltage, timing, and crosstalk noise to choose best modulation scheme for a given channel

## Next Time

## Link Circuits

• Termination structures

·Drivers

• Receivers