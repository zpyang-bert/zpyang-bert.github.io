---
layout: post
title:      "ECEN720: High-Speed Links Circuits and Systems Spring 2023"
date:       2026-04-18 16:27:33
author:     "Bert"
tags:
  - Jitter
  - Lecture
  - Mineru
---
Lecture 10: Jitter

![](/img/mineru_output/lecture10_ee720_jitter/auto/images/660cc234d2f3281c2340a3e0786cc0a092ebcfaf29118203b67d492b0a043fef.jpg)

Sam Palermo Analog & Mixed-Signal Center Texas A&M University

## Announcements

## ● Lab 6 Report due Apr 3

## ● Reference Material

Jitter application notes posted on website

Majority of today's material from Hall reference

## Agenda

● Jitter Definitions

● Jitter Categories

● Dual Dirac Jitter Model

● System Jitter Budgeting

## Eye Diagram and Spec Mask

• Links must have margin in both the voltage AND timing domain for proper operation

For independent design (interoperability) of TX and RX, a spec eye mask is used

Eye at RX sampler

![](/img/mineru_output/lecture10_ee720_jitter/auto/images/92243255509fbe946a64a9a9d13921b682b10f149b3d6c3b926b13eddcb5cc96.jpg)  
RX clock timing noise - or jitter (random noise only here)

## Jitter Definitions

• Jitter can be defined as "the short-term variation of a signal with respect to its ideal position in time"

• Jitter measurements

·Period Jitter $( \mathsf { 1 } _ { \mathsf { P E R } } )$

• Time difference between measured period and ideal period

Cycle to Cycle Jitter $( \mathsf { J } _ { \mathsf { C C } } )$

• Time difference between two adjacent clock periods

Important for budgeting on-chip digital circuits cycle time

Accumulated Jitter $( \mathsf { J } _ { \mathsf { A C } } )$

• Time difference between measured clock and ideal trigger clock

Jitter measurement most relative to high-speed link systems

## Jitter Statistical Parameters

## • Mean Value

Can be interpreted as a fixed timing offset or "skew"

• Generally not important, as usually can corrected for

## ● RMS Jitter

Useful for characterizing random component of jitter

## ● Peak-to-Peak Jitter

● Function of both deterministic (bounded) and random (unbounded) jitter components

• Must be quoted at a given BER to account for random (unbounded) jitter

## Jitter Calculation Examples

![](/img/mineru_output/lecture10_ee720_jitter/auto/images/8afe6347bb65727dd72d6e588f0eb9ed4bdaf50a4d82986ab962f706e8f2dcaa.jpg)

<table><tr><td rowspan=1 colspan=1>n</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>Mean</td><td rowspan=1 colspan=1>RMS</td><td rowspan=1 colspan=1>PP</td></tr><tr><td rowspan=1 colspan=1> $\frac { ] _ { P E R } } { P E R }$ </td><td rowspan=1 colspan=1>-0.06</td><td rowspan=1 colspan=1>0.02</td><td rowspan=1 colspan=1>-0.06</td><td rowspan=1 colspan=1>0.12</td><td rowspan=1 colspan=1>0.005</td><td rowspan=1 colspan=1>0.085</td><td rowspan=1 colspan=1>0.18</td></tr><tr><td rowspan=1 colspan=1> $\underline { { \mathsf { J } _ { \mathsf { C C } } } }$ </td><td rowspan=1 colspan=1>0.08</td><td rowspan=1 colspan=1>-0.08</td><td rowspan=1 colspan=1>0.18</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>0.06</td><td rowspan=1 colspan=1>0.131</td><td rowspan=1 colspan=1>0.26</td></tr><tr><td rowspan=1 colspan=1> $\mathsf { J } _ { \mathsf { A C } }$ </td><td rowspan=1 colspan=1>-0.07</td><td rowspan=1 colspan=1>-0.05</td><td rowspan=1 colspan=1>-0.11</td><td rowspan=1 colspan=1>0.01</td><td rowspan=1 colspan=1>-0.055</td><td rowspan=1 colspan=1>0.05</td><td rowspan=1 colspan=1>0.12</td></tr></table>

$] _ { P E R }$ = time difference between measured period and ideal period  
$\mathsf { J } _ { \mathsf { C C } }$ = time difference between two adjacent clock periods  
$\mathsf { J } _ { \mathsf { A C } }$ = time difference between measured clock and ideal trigger clock

## Jitter Histogram

![](/img/mineru_output/lecture10_ee720_jitter/auto/images/b3048c3c5df4274264cba9086bd18d8c04fb75fa8fe456fe764f62976ec050f3.jpg)

• Used to extract the jitter PDF

• Consists of both deterministic and random components

• Need to decompose these components to accurately estimate jitter at a given BER

## Jitter Categories

![](/img/mineru_output/lecture10_ee720_jitter/auto/images/c715de8251502ced9cf50d4c658371f9512b268f683c9fa6cad308f9ac8755f4.jpg)

## Random Jitter (RJ)

Unbounded and modeled with a gaussian distribution

Assumed to have zero mean value

• Characterized by the rms value, $\sigma _ { \mathsf { R } }$

Peak-to-peak value must be quoted at a given BER

Originates from device noise

Thermal, shot, flicker noise

![](/img/mineru_output/lecture10_ee720_jitter/auto/images/62b96e8e52c2c71c427402f99225153b16239ef466985d08147c756426dff1f3.jpg)

## Deterministic Jitter (DJ)

• Bounded with a peak-to-peak value that can be predicted

● Caused by transmission-line losses, duty-cycle distortion, spreadspectrum clocking, crosstalk

● Categories

Sinusoidal Jiter (SJ or PJ)

Data Dependent Jitter (DDJ)

• Intersymbol Interference (ISI)

Duty Cycle Distortion (DCD)

• Bounded Uncoirrelated Jitter (BUJ)

![](/img/mineru_output/lecture10_ee720_jitter/auto/images/122eb05832f18c8faaab6cb38f0adc913eaca8a8f3d800d4f0f817b4e57f7e76.jpg)

## Sinusoidal or Periodic Jitter (SJ or PJ)

Repeats at a fixed frequency due to modulating effects

• Spread spectrum clocking

PLL reference clock feedthrough

Can be decomposed into a Fourier series of sinusoids

$$
S J ( t ) { = } \sum _ { i } { A _ { i } \cos ( \omega _ { i } t + \theta _ { i } ) }
$$

The jitter produced by an individual sinusoid is

![](/img/mineru_output/lecture10_ee720_jitter/auto/images/1e681b5dba8353ef78d487b839e49b3ce33407a1ba6c799af040d252a9e479fa.jpg)

## Data Dependent Jitter (DDJ)

Data dependent jitter is correlated with either the transmitted data pattern or aggressor (crosstalk) data patterns

● Caused by phenomena such as phase errors in serialization clocks, channel filtering, and crosstalk

● Categories

• Duty Cycle Distortion (DCD)

Intersymbol Interference (ISI)

Bounded Uncorrelated Jitter (BUJ)

## Duty Cycle Distortion (DCD)

● Caused by duty cycle errors in TX serialization clocks and rise/faill delay mismatches in postserialization buffers

● Resultant PDF from a peak-to-peak duty cycle distortion $( \alpha _ { \sf D C D } )$ is the sum of two delta functions

$$
P D F _ { _ { D C D } } ( t ) = \frac { 1 } { 2 } \Bigg [ \delta \Bigg ( t - \frac { \alpha _ { D C D } } { 2 } \Bigg ) + \delta \Bigg ( t + \frac { \alpha _ { D C D } } { 2 } \Bigg ) \Bigg ]
$$

![](/img/mineru_output/lecture10_ee720_jitter/auto/images/a08858652825acbabb698385ed3ac0931a4721da16044ed3596ee447de0dce42.jpg)

## Intersymbol Interference (ISI)

● Caused by channel loss, dispersion, and reflections

● Equalization can improve ISI jitter

![](/img/mineru_output/lecture10_ee720_jitter/auto/images/bcefd367f31502387131ecff5514f1f1331820bcbc67372b6d16710abfc23bda.jpg)

## Bounded Uncorrelated Jitter (BUJ)

Not aligned in time with the data stream

● Most common source is crosstalk

● Classified as uncorrelated due to being correlated to the aggressor signals and not the victim signal or data stream

● While uncorrelated, still a bounded source with a quantifiable peak-to-peak value

## Total Jitter (TJ)

The total jiter PDF is produced by convolving the random and deterministic jitter PDFs

$$
\begin{array} { c } { { P D F _ { \scriptscriptstyle { J T } } ( t ) = P D F _ { \scriptscriptstyle { R J } } ( t ) ^ { * } P D F _ { \scriptscriptstyle { D J } } ( t ) } } \\ { { { \bf w h e r e } P D F _ { \scriptscriptstyle { D J } } ( t ) = P D F _ { \scriptscriptstyle { S J } } ( t ) ^ { * } P D F _ { \scriptscriptstyle { D C D } } ( t ) ^ { * } P D F _ { \scriptscriptstyle { I S I } } ( t ) ^ { * } P D F _ { \scriptscriptstyle { B U J } } ( t ) } } \end{array}
$$

![](/img/mineru_output/lecture10_ee720_jitter/auto/images/d1b28c1a34cb85d4e6f3369f9f6b7af4dc16cb29680ae43d3d2cf32fbe3fa9e7.jpg)

## Jitter and Bit Error Rate

● Jitter consists of both deterministic and random components

Total jitter must be quoted at a given BER

● At $\mathsf { B E R = 1 0 ^ { - 1 2 } }$ jitter \~1675ps and eye width margin \~200ps

● System can potentially achieve BEI $\mathtt { \lambda } = 1 0 ^ { - 1 8 }$ before being jitter limited

![](/img/mineru_output/lecture10_ee720_jitter/auto/images/786b484165a941571dce17df00d0e446d2723f72b82a59935e30e22613f9d0bb.jpg)

![](/img/mineru_output/lecture10_ee720_jitter/auto/images/b29f352b597cc13089112fd05915b7d3ee37c9ac6c41acbc22c9280590a4104f.jpg)

## Dual Dirac Jitter Model

• For system-level jitter budgets, the dual Dirac model approximates the complex total jitter PDF and allows for the budgeting of deterministic and random jitter components

$$
R J ( t ) = \frac { 1 } { \sqrt { 2 \pi } \sigma _ { R J } } e ^ { \frac { - t ^ { 2 } } { 2 \sigma _ { R J } ^ { 2 } } }
$$

$$
 D J \left( t \right) = \frac { \delta \left( t - D J _ { \delta \delta } / 2 \right) } { 2 } + \frac { \delta \left( t + D J _ { \delta \delta } / 2 \right) } { 2 }
$$

$$
J T ( t ) = R J ( t ) ^ { * } D J ( t ) = \frac { 1 } { 2 \sqrt { 2 \pi } \sigma _ { _ { R J } } } \Biggl [ e ^ { - \frac { t - D J _ { \delta \delta } / 2 } { 2 \sigma _ { _ { R J } } ^ { 2 } } } + e ^ { - \frac { t + D J _ { \delta \delta } / 2 } { 2 \sigma _ { _ { R J } } ^ { 2 } } } \Biggr ]
$$

![](/img/mineru_output/lecture10_ee720_jitter/auto/images/10f3299b1fc2ffd4390a69898fa68002b22781cae3f6bf0463362218b9b06485.jpg)

![](/img/mineru_output/lecture10_ee720_jitter/auto/images/7e3c87dd8e527186ee759dde821a6475ad79943a95e220077b66016b0f94a676.jpg)

![](/img/mineru_output/lecture10_ee720_jitter/auto/images/09cacc434e18d6e104b45524dddf7e29df54fbbd0905c9c86d91ffc9f3fa8eb8.jpg)

## Dual Dirac Jitter Model

Jitter at a given BER is computed considering both leading and trailing edges

![](/img/mineru_output/lecture10_ee720_jitter/auto/images/44fdfb6296d1810dbbfa5ebe94969f7a09f24d969d3d0b8e9e97e5111ff0657d.jpg)

## Dual Dirac Jitter Model Example

● Plot measured jitter PDF vs Q-scale

$$
Q _ { B E R } \big ( B E R \big ) = \sqrt { 2 } e r f ^ { - 1 } \Bigg ( 1 { - } \frac { B E R } { \rho _ { T } } \Bigg )
$$

where $\rho _ { \mathbf { T } }$ is the transition density, typically 0.5

● Tails are used to extract $\sigma _ { \mathsf { R } } \mathsf { 1 }$

● Extrapolate to Q(0) to extract separation of dual-Dirac delta functions

![](/img/mineru_output/lecture10_ee720_jitter/auto/images/67898ef8a13bc259e3ed8f3810823482cb2a22b83b8cd6ddbeae3fefffd030ad.jpg)

![](/img/mineru_output/lecture10_ee720_jitter/auto/images/48b3fd4da922157198fa6745b3736ef3eff9bdf54fad1dd0314371a69db49d1f.jpg)  
DJ s = Extracted seperation of dual - Dirac delta functions  
DJp = Actual deterministic jitter peak - to - peak value

## Dual Dirac Jitter Model Example

![](/img/mineru_output/lecture10_ee720_jitter/auto/images/1b93f0cbdf8cbc9ec6d50a7811cf498a83aa41a56acd24f5c86495b421b0a706.jpg)

## Extracted dual Dirac model matches well with measured jitter PDF

## System Jitter Budget

For a system to achieve a minimum BER performance

$$
U I \geq D J _ { \delta \delta } ( s y s ) + Q _ { B E R } \sigma _ { R M S } ( s y s )
$$

● The convolution of the individual deterministic jitter components is approximated by linear addition of the terms

$$
D J _ { _ { \delta \delta } } ( s y s ) \mathrm { = } \sum _ { i } D J _ { _ { \delta \delta } } ( i )
$$

● The convolution of the individual random jitter components results in a root-sum-of-squares system rms value

$$
\sigma _ { { \scriptscriptstyle R M S } } ( s y s ) = \sqrt { \sum _ { i } \sigma _ { { \scriptscriptstyle R M S } } ^ { 2 } ( i ) }
$$

## Jitter Budget Example – PCI Express System

![](/img/mineru_output/lecture10_ee720_jitter/auto/images/63181947de52f6be1c0f7b4a8a29c0c1599ab95c6970ddf51dc9639640667e01.jpg)

## Jitter Budget Example – PCI Express System

$$
D J _ { \delta \delta } ( s y s ) = D J _ { \delta \delta } ( T X ) + D J _ { \delta \delta } ( c h a n n e l ) + D J _ { \delta \delta } ( R X ) + D J _ { \delta \delta } ( c l o c k )
$$

$$
\sigma _ { R M S } \left( s y s \right) = \sqrt { \sigma _ { R M S } ^ { 2 } \left( T X \right) + \sigma _ { R M S } ^ { 2 } \left( c h a n n e l \right) + \sigma _ { R M S } ^ { 2 } \left( R X \right) + \sigma _ { R M S } ^ { 2 } \left( c l o c k \right) }
$$

TABLE 13-2. PCI Express 2.5-Gb/s Jitter Budget at $1 0 ^ { - 1 2 }$ BER
<table><tr><td>Component</td><td>Term</td><td> $\sigma _ { \mathrm { R J } } ~ ( \mathrm { p s } )$ </td><td> $\mathrm { D J } _ { \delta \delta } \ ( \mathrm { p s } )$ </td><td>TJ (ps)</td></tr><tr><td>Reference clock</td><td> $\mathrm { { T J } _ { \ c l o c k } }$ </td><td>4.7</td><td>41.9</td><td>108</td></tr><tr><td>Transmitter</td><td> $\mathrm { ~ T J ~ } _ { \mathrm { T X } }$ </td><td>2.8</td><td>60.6</td><td>100</td></tr><tr><td>Channel</td><td> $\mathrm { { T J } _ { \ c h a n n e l } }$ </td><td>0</td><td>90</td><td>90</td></tr><tr><td>Receiver</td><td>TJ Rx</td><td>2.8</td><td>120.6</td><td>147→160</td></tr><tr><td>Linear TJ RSS TJ</td><td></td><td></td><td></td><td>458</td></tr><tr><td></td><td> $6 . { \overset { \cdot } { 1 5 } } * 1 4 . 0 6 9 = 8 6 . 5$ </td><td></td><td>313.1</td><td>399.6</td></tr><tr><td colspan="5">TABLE 13-1.  $\varrho _ { \mathrm { B E R } }$  as a Function of the Bit Error Rate</td></tr><tr><td>BER</td><td>QBER</td><td>QBER</td><td>BER</td><td>QBER</td></tr><tr><td> $1 \times 1 0 ^ { - 3 }$ </td><td>6.180</td><td>12.723</td><td> $1 \times 1 0 ^ { - 1 7 }$ </td><td>16.987</td></tr><tr><td> $1 \times 1 0 ^ { - 4 }$ </td><td>7.438</td><td> $1 \times 1 0 ^ { - 1 0 } ^  $  1 x10-11 13.412</td><td> $1 \times 1 0 ^ { - 1 8 }$ </td><td>17.514</td></tr><tr><td> $1 \times 1 0 ^ { - 5 }$ </td><td>8.530</td><td> $\subset 1 \times 1 0 ^ { - 1 2 }$  14.069</td><td> $1 \times 1 0 ^ { - 1 9 }$ </td><td>18.026</td></tr><tr><td> $1 \times 1 0 ^ { - 6 }$ </td><td>9.507</td><td> $1 \times 1 0 ^ { - * }$ </td><td> $1 \times 1 0 ^ { - 2 0 }$ </td><td>18.524</td></tr><tr><td> $1 \times 1 0 ^ { - 7 }$ </td><td>10.399</td><td>14.698  $1 \times 1 0 ^ { - 1 4 }$  15.301</td><td> $1 \times 1 0 ^ { - 2 1 }$ </td><td>19.010</td></tr><tr><td> $1 \times 1 0 ^ { - 8 }$ </td><td>11.224</td><td> $1 \times 1 0 ^ { - 1 5 }$  15.882</td><td> $1 \times 1 0 ^ { - 2 2 }$ </td><td>19.484</td></tr><tr><td> $1 \times 1 0 ^ { - 9 }$ </td><td>11.996</td><td> $1 \times 1 0 ^ { - 1 6 }$  16.444</td><td> $7 . 7 \times 1 0 ^ { - 2 4 }$ </td><td>20.000</td></tr></table>

## Next Time

● Clocking Architectures