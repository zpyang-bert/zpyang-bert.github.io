---
layout: post
title:      "ECEN720: High-Speed Links Circuits and Systems Spring 2023"
date:       2026-04-18 21:10:08
author:     "Bert"
tags:
  - Lecture
  - Mineru
  - TX
---
## Lecture 7: Equalization Introduction & TX FIR Eq

![](images/cd4133802cefbe2bb4750008ca5ad28843f570d1d223248348d16f440c4589fc.jpg)

Sam Palermo Analog & Mixed-Signal Center Texas A&M University

## Announcements

● Lab 4 Report and Prelab 5 due Mar 10

● Exam 1 Mar 7

• Covers material through Lecture 6

• Previous years' exam 1s are posted on the website for reference

● Equalization overview and circuits papers are posted on the website

## Agenda

## ● Equalization theory and circuits

Equalization overview

Equalization implementations

TXFIR

•RX FIR

·RX CTLE

·RX DFE

## • TX FIR Equalization

FIR fiter in time and frequency domain

MMSE Coefficient Selection

Circuit Topologies

Equalization overview paper posted on website

## High-Speed Electrical Link System

![](images/2dd96105c5c054ea03393f52f2b9ed54b74f0529e40e3add5811de0c412e7fdc.jpg)

![](images/c3fda610c2e966581bde69d38a36d8b1c7086b2bbdd8040ae46b36071d51d669.jpg)

## Link with Equalization

![](images/5810698e8bd4f5d01c4461d8d0a0fa467e5a5e3344758d54bfe541db34f0da89.jpg)

## Channel Performance Impact

![](images/724cd2a42090990e206dc2d80b9cbc585be19b3c9c19e58a92c51a4bd7d5bb94.jpg)

![](images/5da32185a1d9eea1144d619a40d4c850fec60153b43c38111e3a7230d2c88cd2.jpg)

![](images/88287050a0c3af21f486dcdbc181b70148c36f0645dbc4d6857cc47a560d4baa.jpg)

![](images/390a9996021c9f6df625073ba730d23bb7f18cc084779590e8ed65badb710a74.jpg)

![](images/5e564609983f72b2138057eae3cb3fca939ca85d94aea172d3bd4043cebd46b1.jpg)

## Channel Performance Impact

![](images/1cf14511fa2691d8a9656eee528a27e0ef8da8d6713fe428f5af90d3d2552c23.jpg)

![](images/7a1a5c18ac10051439ded4185aa9857ca5b1a6e5fb75a364910924b3e612654c.jpg)

![](images/9b9bdc31e27b98021a55129b7b0f9f5998fd05657d93995c40ff50bf90c7ff45.jpg)

![](images/e0ddeb3fff3ebb60eaa1f03a58109b56f921af64b5cc379b67d35e2af3c642dd.jpg)

![](images/182e19c36c44df1c2a34d913ebefbc5df33f37991a83a323cf07ce78a8a05b63.jpg)

## Channel Equalization

Equalization goal is to flatten the frequency response out to the Nyquist Frequency and remove time-domain ISI

![](images/227a5a7dddff4d71ab48b51898bef8b523c281787d3c217f1967ac9e2e3e0066.jpg)

## TX FIR Equalization

TX FIR filter pre-distorts transmitted pulse in order to invert channel distortion at the cost of attenuated transmit signal (de-emphasis)

![](images/0501aa8ffab3cbcce91fe8891a62bb41137ad5cbb413c4e16e6777824b7501f0.jpg)  
"A Low Power 10Gb/s Serial Link Transmitter in 90-nm CMOS," A. Rylyakov et al., CSICS 2005

## 6Gb/s TX FIR Equalization Example

![](images/cf482ab0b9732b603faa8477a2b79a0568ad4b6511526e4a424307abaa110ebb.jpg)

6Gb/s Pulse Responses  
![](images/da5f5354cb4c510f382175aa702082cf045318fdddd073f9117276ede4109dcb.jpg)

6Gb/s Pulse Responses  
![](images/85bdd63e8999889714d33418bb1a44a9f4274b6956b2a0d375717d36d43f10c3.jpg)

## ● Pros

Simple to implement

• Can cancel ISI in precursor and beyond filter span

Doesn't amplify noise

• Can achieve 5-6bit resolution

## ● Cons

Attenuates low frequency content due to peak-power limitation

Need a "back-channel" to tune filter taps

![](images/58dfb40d0b1b49149a8a333180de6fecb5d4d39380d179fbc8aa68cea2f00527.jpg)

![](images/2c5148453553011da1dce05ca18fff8644a5d2768f420b0a5fa6b7dde7a8b64f.jpg)

## RX Equalization #1: RX FIR

![](images/c6c8e0729656bec920e39bb50a162d78317c5e7ef1282c6414504edf0a6a6b73.jpg)

## ● Pros

With sufficient dynamic range, can amplify high frequency content (rather than attenuate low frequencies)

• Can cancel ISI in pre-cursor and beyond filter span

• Filter tap coefficients can be adaptively tuned without any back-channel

## ● Cons

Amplifies noise/crosstalk

Implementation of analog delays

Tap precision

Eye-Pattern Diagrams at 1Gb/s on CAT5e\*  
![](images/402cc46602e836f4e2d7f98034e74e52ab4d1a0e84f75919bd043bd0f183c020.jpg)  
Before Equalizer: 23meters  
Ater Equalizer: 23meters

## RX Equalization #2: RX CTLE

![](images/4694f9f1144cc83b8d553007ec0eafe4c699a4e34926a7e36fd51443d8308f8d.jpg)

![](images/1fc63a9d23da49499ef3c621d6133f3eaffcbdb04fddd32d6661e43814e7e786.jpg)

## ● Pros

Provides gain and equalization with low power and area overhead

Can cancel both precursor and long-tail ISI

## ● Cons

Generally limited to 1st order compensation

Amplifies noise/crosstalk

PVT sensitivity

Can be hard to tune

![](images/8374c5c3b10a65ee3ec7ab0871d671ed186fe9a1fa374770fb7a0c04663b2b83.jpg)

![](images/b10cd001fcf6ed4ccec8c6ca811a9596e178990c01a43a43b4b5b229d566643f.jpg)

## RX Equalization #3: RX DFE

![](images/d0a6c4ee93c5b31c655589792e47311355ae56ac617b29e7c0f7784e756558a3.jpg)

![](images/a3db1b44bd2d255115843f8c7698eb208259c7c962ae0c9c615ed68eff56363c.jpg)

## ● Pros

No noise and crosstalk amplification

Filter tap coefficients can be adaptively tuned without any backchannel

## ● Cons

• Cannot cancel precursor ISI

• Critical feedback timing path

Timing of ISI subtraction complicates CDR phase detection

![](images/e57a9c818cc8ee729e904089b92871e07443a75ef6d9fd03907d377116f3e510.jpg)

![](images/8bea855e6eaa67ef08b814de7ab9a4ee24c652ced64fabb52dbbd062c463794b.jpg)

## Equalization Effectiveness

![](images/06b05fa724039df6e27ce0f7de5368fc81aebf225b7b3ea2dd03c2d7a2f0be78.jpg)  
Some observations:

![](images/cce0204980d3ee5e2bfbeb7952abe91b03f4a34d6a9cccbe8ba37b27dfaef5e4.jpg)

Big initial performance boost with 2-tap TX eq.

With only TX eq., not much difference between 2 to 4-tap

• RX equalization, particularly DFE, allows for further performance improvement

Caution – hard to build fast DFEs due to critical timing path

## Link with Equalization

![](images/14c9a4390797b29874cedf5b9535bc6e4359907bddbdb477a5a51d2d8e3e96fc.jpg)

## Channel Equalization

Equalization goal is to flatten the frequency response out to the Nyquist Frequency and remove time-domain ISI

![](images/52d3e0f0ceef7286f273a9abd3d7a936ecaffe5d0e3e35db3c83d999f2dd4ee9.jpg)

## TX FIR Equalization – Time Domain

For 10Gbps : $\begin{array} { r } { W \big ( z \big ) = - 0 . 1 3 1 + 0 . 5 9 5 z ^ { - 1 } - 0 . 2 7 4 z ^ { - 2 } } \end{array}$

![](images/821374cedbc42bc887af0f202f9949b3f37bcea4add88762307876aceaed4285.jpg)  
Low Frequency Response (Sum Taps)

$$
\left[ \ldots \quad 1 \quad 1 \quad 1 \quad \ldots \right] * \left[ - 0 . 1 3 1 \quad 0 . 5 9 5 \quad - 0 . 2 7 4 \right] = \left[ \ldots \quad 0 . 1 9 0 \quad 0 . 1 9 0 \quad 0 . 1 9 0 \quad 0 . 1 9 0 \quad \ldots \right] * \left[ 0 . 1 9 0 \quad 0 . 1 9 0 \quad \ldots \right] * \left[ 0 . 1 9 0 \quad 0 . 1 9 0 \quad \ldots \right] * \left[ 0 . 1 9 0 \quad 0 . 1 9 0 \quad \ldots \right] * \left[ 0 . 1 9 0 \quad 0 . 1 9 0 \quad \ldots \right] \quad .
$$

Nyquist Frequency Response (Sum Taps w/ Alternating Polarity) $\left[ \ldots - 1 \quad 1 \quad - 1 \quad \ldots \right] * \left[ - 0 . 1 3 1 \quad 0 . 5 9 5 \quad - 0 . 2 7 4 \right] = \left[ \ldots \quad 1 \quad - 1 \quad 1 \quad \ldots \right]$

![](images/628a72b257ae7365cc9557488ec1ae34c8ea1417ccc682d85c1e93daad5231cd.jpg)

![](images/4b1b38ac6c304b652fc63bf78e8425f4795978c585be8f022efd1fe85141ede7.jpg)

## TX FIR Equalization – Freq. Domain

For 10Gbps : $\begin{array} { r } { W \big ( z \big ) = - 0 . 1 3 1 + 0 . 5 9 5 z ^ { - 1 } - 0 . 2 7 4 z ^ { - 2 } } \end{array}$

![](images/208a74037d62d059f3727ff3012b6a78c7d5a1c010e2cb47268c8cc07e6094b0.jpg)

$$
\begin{array} { r } { W \left( z \right) = - 0 . 1 3 1 + 0 . 5 9 5 z ^ { - 1 } - 0 . 2 7 4 z ^ { - 2 } } \end{array}
$$

![](images/83d6ad4b216d5e037cdc7a92f1cdb0a95a25b950e9cb3373500fbbf69de8868b.jpg)

$$
\mathbf { w } / \ z = e ^ { j 2 \pi f T _ { s } } = \cos ( 2 \pi f T _ { s } ) + j \sin ( 2 \pi f T _ { s } )
$$

Low Frequency Response (f = 0)

$$
z = \cos ( 0 ) + j \sin ( 0 ) = 1 \Rightarrow W \big ( f = 0 \big ) = 0 . 1 9 0 \Rightarrow - 1 4 . 4 d B
$$

Nyquist Frequency Response $\left( f = \frac { 1 } { 2 T _ { s } } \right)$

$$
z = \cos ( \pi ) + j \sin ( \pi ) = - 1 \Rightarrow W \left( f = { \frac { 1 } { 2 T _ { s } } } \right) = - 1 \Rightarrow 0 d B
$$

● Equalizer has 14.4dB of frequency peaking

Note: Ts=Tb=100ps

• Attenuates DC at -14.4dB and passes Nyquist frequency at 0dB

## TX FIR Coefficient Selection

● One approach to set the TX FIR coefficients is a Minimum Mean-Square Error (MMSE) Algorithm

$$
a _ { k } = [ \sum \limits _ { w _ { k } } ^ { T X E q . } w _ { k } ]  [ \sum \limits _ { h _ { k } } ^ { C h a n n e l } \ ]  y _ { k }
$$

channel output vector, y

Rows = k+n+l-2

where k = channel pulse model length

TX Eq "w" Matrix

Rows = n+l-1 where n = tap number Columns = l = input symbol number

$$
\left[ \begin{array} { c } { { y ( 0 ) } } \\ { { y ( 1 ) } } \\ { { \cdots } } \\ { { y ( l + n + k - 3 ) } } \end{array} \right] = \left[ \begin{array} { c c c c c c c c c } { { h ( 0 ) } } & { { 0 } } & { { 0 } } & { { \ldots } } & { { 0 } } & { { 0 } } & { { { \top } w ( 0 ) } } & { { 0 } } & { { \ldots } } & { { 0 } } & { { 0 } } \\ { { h ( 1 ) } } & { { h ( 0 ) } } & { { 0 } } & { { \ldots } } & { { 0 } } & { { 0 } } & { { { \top } w ( 1 ) } } & { { w ( 0 ) } } & { { 0 } } & { { \ldots } } & { { 0 } } & { { 0 } } \\ { { \ldots } } & { { \ldots } } & { { \ldots } } & { { \ldots } } & { { \ldots } } & { { \ldots } } & { { \ldots } } & { { \ldots } } & { { \ldots } } & { { \ldots } } & { { \ldots } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { \ldots } } & { { h ( k - 1 ) } } & { { h ( k - 2 ) } } & { { 0 } } & { { 0 } } & { { 0 } } & { { \ldots } } & { { w ( n - 1 ) } } & { { w ( n - 2 ) } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { \ldots } } & { { 0 } } & { { h ( k - 1 ) } } & { { 0 } } & { { 0 } } & { { 0 } } & { { \ldots } } & { { 0 } } & { { w ( n - 1 ) } } \end{array} \right] \left[ \begin{array} { c } { { c ( 0 ) } } \\ { { c ( 1 ) } } \\ { { \ldots } } \\ { { \cdots } } \\ { { c ( l - 1 ) } } \end{array} \right] .
$$

Channel "h" Matrix

e input symbols, c

## TX FIR Coefficient Selection

• Total system

$$
[ \begin{array} { c } { { y ( 0 ) } } \\ { { y ( 1 ) } } \\ { { \cdots } } \\ { { y ( l + n + k - 3 ) } } \end{array} ] = [ \begin{array} { c c c c c c c c } { { h ( 0 ) } } & { { 0 } } & { { 0 } } & { { \ldots } } & { { 0 } } & { { 0 } } & { { 0 } } & { { \ldots } } & { { 0 } } & { { 0 } } \\ { { h ( 1 ) } } & { { h ( 0 ) } } & { { 0 } } & { { \ldots } } & { { 0 } } & { { 0 } } & { { 0 } } & { { \ldots } } & { { 0 } } & { { 0 } } \\ { { \ldots } } & { { \ldots } } & { { \ldots } } & { { \ldots } } & { { \ldots } } & { { \ldots } } & { { \ldots } } & { { \ldots } } & { { \ldots } } & { { \ldots } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { \ldots } } & { { h ( k - 1 ) } } & { { h ( k - 2 ) } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { \ldots } } & { { 0 } } & { { h ( k - 1 ) } } & { { 0 } } & { { 0 } } & { { \ldots } } & { { 0 } } & { { u ( n - 1 ) } } \end{array} ] \ldots c ( l ) ] \ldots [ \begin{array} { c } { { \sigma ( 0 ) } } \\ { { \sigma ( 1 ) } } \\ { { \ldots } } \\ { { \sigma ( l - 1 ) } } \\ { { \sigma ( l + n + k - 1 ) } } \end{array} ] .
$$

Multiplying input symbols by TX Eq., ${ \mathsf { w c } } { = } { \mathsf { w } } ^ { * } { \mathsf { C } }$

$$
\left[ \begin{array} { c } { { y ( 0 ) } } \\ { { y ( 1 ) } } \\ { { \cdots } } \\ { { y ( l + n + k - 3 ) } } \end{array} \right] = \left[ \begin{array} { c c c c c c } { { h ( 0 ) } } & { { 0 } } & { { 0 } } & { { \ldots } } & { { 0 } } & { { 0 } } \\ { { h ( 1 ) } } & { { h ( 0 ) } } & { { 0 } } & { { \ldots } } & { { 0 } } & { { 0 } } \\ { { \ldots } } & { { \ldots } } & { { \ldots } } & { { \ldots } } & { { \ldots } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { \ldots } } & { { h ( k - 1 ) } } & { { h ( k - 2 ) } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { \ldots } } & { { 0 } } & { { h ( k - 1 ) } } \end{array} \right] \left[ \begin{array} { c } { { w c ( 0 ) } } \\ { { w c ( 1 ) } } \\ { { \cdots } } \\ { { w c ( n + l - 1 ) } } \end{array} \right]
$$

• We desire the output vector, y, to be ISI free

$$
y _ { _ { d e s } } = \left\{ \begin{array} { l l } { y _ { _ { d e s } } { \left( n \right) } { = } 1 , n { = } \mathbf { C h a n n e l \ p r e - c u r s o r s a m p l e \# + E q \ p r e c u r s o r t a p \# + 1 } } \\ { y _ { _ { d e s } } { \left( n \right) } { = } 0 , n { \neq } \mathbf { C h a n n e l \ p r e - c u r s o r s a m p l e \# + E q \ p r e c u r s o r t a p \# + 1 } } \end{array} \right.
$$

## Lone-Pulse Equalization Example

● With lone-pulse equalization, e=1 input symbols, i.e. c=[1]

![](images/c60ae9599fc534e3b179c0b778a6de82e3c7109e20676258fdd59b1bc312470c.jpg)

Channel precursor samples

$$
\Upsilon _ { \mathrm { d e s } } ( 5 + 1 + 1 = 7 ) { = } 1
$$

Channel pulse matrix H with 5 precursor samples and 10 post-cursor samples, 3 columns for 3 eq taps

$$
\begin{array} { r l } { \frac { d } { d t } } & { \mathrm { h e a r a n g } } \\ { \frac { d } { d t } } & { \mathrm { h e a r a n g \ : ~ i m e a n \ : ~ } \ : \ : \ : } \\ { \frac { d } { d t } } & { \mathrm { l o a r a n g \ : ~ a t e a n a n \ : ~ } \ : \ : } \\ { \frac { d } { d t } } & { \mathrm { l o a r a n g \ : ~ a t e a n a n i t } } \\ { \frac { d } { d t } } & { \mathrm { l o a r a n g \ : ~ a t e a n a n i t } } \\ { \frac { d } { d t } } & { \mathrm { l o a r a n g \ : ~ a t e a n a n i t } } \\ { \frac { d } { d t } } & { \mathrm { l o a r a n g \ : ~ a t e a n a n i t } } \\ { \frac { d } { d t } } & { \mathrm { l o a r a n g \ : ~ a t e a n a n i t } } \\ { \frac { d } { d t } } & { \mathrm { l o a r a n g \ : ~ a t e a n a n i t } } \\ { \frac { d } { d t } } & { \mathrm { l o a r a n g \ : ~ a t e a n a n i t } } \\ { \frac { d } { d t } } & { \mathrm { l o a r a n g \ : ~ a t e a n a n i t } } \\ { \frac { d } { d t } } & { \mathrm { l o a r a n g \ : ~ a t e a n a n i t } } \\ { \frac { d } { d t } } & { \mathrm { l o a r a n g \ : ~ a t e a n a n i t } } \\ { \frac { d } { d t } } & { \mathrm { l o a r a n g \ : ~ a t e a n a n i t } } \\ { \frac { d } { d t } } & { \mathrm { l o a r a n g \ : ~ a t e a n a n i t } } \\ { \frac { d } { d t } } & { \mathrm { l o a r a n g \ : ~ a t e a n a n i t } } \\ { \frac { d } { d t } } & { \mathrm { l o a r a n g \ : ~ a t e a n a n i t } } \\ { \frac { d } { d t } } & { \mathrm { l o a r a n g \ : ~ a t e a n a n i t } } \\ { \frac { d } { d t } } & { \mathrm { l o a r a n g \ : ~ a t e a n a n i t } } \\ { \frac { d } { d t } } & { \mathrm { l o a r a n g \ : ~ a t e a n a n i t } } \\ { \frac { d } { d t } } & { \mathrm { l o a r a n g \ : ~ a t e a n a n i t } } \\  \end{array}
$$

## TX FIR Coefficient Selection

We can calculate the error w.r.t. a desired output

$E = Y - Y _ { d e s } = H W _ { c } - Y _ { d e s } = H W - Y _ { d e s }$ with pulse input

● Computing the error matrix norm²

$$
\left\| E \right\| ^ { 2 } = W ^ { T } H ^ { T } H W - 2 Y _ { d e s } ^ { T } H W + Y _ { d e s } ^ { T } Y _ { d e s }
$$

Differentiating this w.r.t. tap matrix taps to find taps which yield minimum error norm²

$$
\frac { d } { d W } \big \| E \big \| ^ { 2 } = 2 W ^ { T } H ^ { T } H - 2 Y _ { d e s } ^ { T } H = 0
$$

$$
\boldsymbol { W } ^ { T } \boldsymbol { H } ^ { T } \boldsymbol { H } = Y _ { d e s } ^ { T } \boldsymbol { H }
$$

Solving for optimum TX Eq taps, W

$$
\boxed { W _ { l s } = \left( H ^ { T } H \right) ^ { - 1 } H ^ { T } Y _ { d e s } }
$$

● This will yield a W matrix to produce a value of $" 1 "$ at the output cursor, i.e. an FIR filter with gain

• Need to normalize by the total abs(tap) sum for TX FIR realization

$$
\boxed { W _ { l s n o r m } \big ( n \big ) = \frac { W _ { l s } \big ( n \big ) } { \displaystyle \sum _ { i = 1 } ^ { n } \big | W _ { l s } \big ( n \big ) \big | } }
$$

## TX FIR Tap Resolution

• Using the above MMSE algorithm for the Refined Server Channel at 10Gb/s 17" Refined Server 10Gb/s Pulse Respc

$$
W _ { l s } = \left[ { \begin{array} { l } { - 0 . 8 1 8 0 } \\ { 0 . 7 2 4 5 } \\ { 0 . 5 9 4 9 } \\ { - 1 . 7 1 8 4 } \end{array} } \right] ^ { - 0 . 8 1 8 0 } { \bmod { \underline { { 1 } } } } \psi _ { l s n o r m } = { \left[ { \begin{array} { l } { - 0 . 1 3 0 7 } \\ { 0 . 5 9 4 9 } \\ { 0 . 5 9 4 9 } \\ { - 0 . 2 7 4 5 } \end{array} } \right] }
$$

$$
\begin{array} { c } { { W \big ( z \big ) = - 0 . 1 3 1 + 0 . 5 9 5 z ^ { - 1 } - 0 . 2 7 4 z ^ { - 2 } } } \\ { { \big [ 1 p r e \quad m a i n \quad 1 p o s t \big ] } } \\ { { \big [ - 0 . 1 3 1 \quad 0 . 5 9 5 \quad - 0 . 2 7 4 \big ] } } \end{array}
$$

![](images/bd150ce18a6cd516936d70690a97036b865e8d4b4b338ebb6f2b5ee89ca30e12.jpg)

Generally, TX DAC resolution is limited to between 4 to 6bits

Mapping these equalization coefficients with this resolution may impact performance

## TX FIR Circuit Architectures

• Direct FIR vs Segmented DAC

Direct FIR

Parallel output drivers for output taps

• Each parallel driver must be sized to handle its potential maximum current

Lower power & complexity

Higher output capacitance

## Segmented DAC

• Minimum sized output transistors to handle peak output current

Lowest output capacitance

Most power & complexity

Need mapping table (RAM)

Very flexible in equalization

Direct FIR

![](images/f3f6cb3cad5a38dd5a266c8e5f6662a09bd239934c2c5893bb5beeeb67b81646.jpg)  
Segmented DAC

![](images/0904c75b6bd638d07dcc9dd2c0da1d11cfdf3cd01d2323b0d9e35462371cf60e.jpg)

## Direct FIR Equalization

![](images/f9700d52c9934340db35a37f7261832db35112003b37b86396ffe66ce6b7baf2.jpg)

## Segmented DAC Example

![](images/c63a5449a58cabc07062112b131f7fdf446b9642b9dccac46ba1f00e15049f8e.jpg)  
For this 4-bit pattern, send this 6-bit number Combining taps in digital domain, not at output  
Sized only to deliver maximum total current  
4 filtered bits (parallel) at 6-bit resolution  
[Casper IsscC 2006]

## Voltage-Mode TX FIR Driver #1

![](images/faca4cb67fb774d322d5ae041e1afc068ac5f227ae10038529eaa4e0c79c04f0.jpg)  
[Wong JssC 2004]

![](images/75a95b5906a8c7ce7bcfab5d7c0b1400831029b9fcf3b1db5af5f7eb29d49133.jpg)  
[Sredojevic JssC 2011]

● FIR equalization is typically more difficult to implement in voltage-mode drivers due to the series impedance

● An output voltage divider with a GND shunting path can realize the different voltage levels required by the FIR equalizer and also maintain impedance control

Drawbacks to this approach

• Output segmentation requires significant pre-dive logic whose complexity grows with equalization tap resolution

Time-varying current draw from the VREF supply

## Voltage-Mode TX FIR Driver #2

![](images/2d677f20a64cc7aa1c9414ccb88c81130428452f6823a8c3a90dbb46fd0de430.jpg)

![](images/2fe438991302f8d1fa32a20cf23eca028c1cb2864c2c50e7b9d1091b1369c5d0.jpg)  
[Sredojevic JssC 2011]

• Adding a channel shunting path can realize the different voltage levels required by the FIR equalizer, maintain impedance control, and produce a constant current draw from the VREF supply

• The major drawback to this approach is even more complex output segmentation pre-drive logic

## Hybrid Voltage-Mode Driver with Current-Mode Equalization

![](images/15250cf76cfb3651f4f01e8e7c14b75d805d5b1b919cd7527ba890329c034e38.jpg)

![](images/1934ce8ba6d8139ddf4bf2598ba47fd96f3928287a066e117381a485f3f38be8.jpg)  
(a)

![](images/e2eaafd587f59fb10e228bd314a2a0e7583beeb60662b7d1a01bd378a9c99f77.jpg)  
Fig. 7. 4.8-Gbit/s eye diagrams with a channel that has 6-dB 1oss at 2.4 GHz. (a) Without equalization. (b) With equalization.

● A hybrid voltage-mode driver with current-mode equalization provides the advantages of both drivers

• The main driver tap is voltage-mode, which allows for reduced current for a given voltage swing

● High-resolution pre-emphasis equalization taps at minimum pre-drive complexity are possible with parallel current-mode drivers

• Does have some dynamic current variation, but is less than the original VM TX FIR #1

## Impedance Modulated Equalization

• Signaling power reduces as de-emphasis increases

• Transition bits have 50Ω impedance

• Longer run length data has higher impedance

Segmented Implementation [2]

![](images/c87ebb15d476b3e7f6ec0ab3739b75a090c5b8a9755373b543b9c268ddd65cc5.jpg)

[2] R. Sredojevic, et al., JSSC 2011

![](images/3a86fe1f8753e5241d751c7d382ddffdf90db47c0f93e6db5157ef1fc99fe171.jpg)

## Impedance Modulated Equalization

• Signaling power reduces as de-emphasis increases

• Transition bits have 50Ω impedance

• Longer run length data has higher impedance

Segmented Implementation [2]

![](images/f4cd6b2068abe6057dc8ea89e1b3e721bd1a37589118e77323eb8b6ebe023e32.jpg)

[2] R. Sredojevic, et al., JSSC 2011

![](images/64a3419b625ce812e4a574f2731ae8a048cdf9ed1185df67663dbc56543f2843.jpg)

## Relative Equalization Performance

• Relative equalization performance depends on the channel

Channels with significant reflections (middle-trace backplane) can have >20% extra residual ISI

• Well-controlled impedance channels (single-board CPW) display almost identical performance

![](images/d159d7e465b3d43c9b7a0f7432894662896e229bce881019ddec6464fa43d7d1.jpg)  
10Gb/s Residual ISI w/ 2-tap EQ

![](images/5b1ad41440a37ca0f18789f6035b31ddb657c4bf298375e11c21db954f6b4f33.jpg)  
26.5: An 8-to-16Gb/s 0.65-to-1.05pJ/b 2-Tap Impedance-Modulated Voltage-Mode Transmitter with Fast Power-State Transitioning in 65nm CMOS'

## Equalization Tap Control

• Segmented pre-driver and output driver significantly increases dynamic power consumption with increased equalization resolution

Segmented Implementation [2]

![](images/93d138cbc45d279bb4344c40944b164ff114fcc5db96fecf8f0302447b8501ef.jpg)

[2] R. Sredojevic, et al., JSSC 2011

Proposed non-segmented Implementation

![](images/db3628602b6da68c5b35cd2f8dfcffcfbfdb385b02c7681ac528357c2a29a677.jpg)

## TX Output Driver w/Analog Control

Global impedance modulation/control lops and voltage regulator allows for power amortization

![](images/bd8f2e2aa70f1d8e436a68e54714f47702fcfdd9fdf7eae3dbbc036bfbbc5870.jpg)

## Impedance Modulated EQ Mode

• Maximum transmitter output swing during a transition bit

![](images/cf900e58d4667d4fce36def06961847931057284cc3a208679c0ce99578c5a63.jpg)

![](images/0d64662e46586fc47ec313b237c56d95c171b3a60caa564dde04bf1ecf0cb877.jpg)  
26.5: An 8-to-16Gb/s 0.65-to-1.05pJ/b 2-Tap Impedance-Modulated Voltage-Mode Transmitter with Fast Power-State Transitioning in 65nm CMOS

## Impedance Modulated EQ Mode

• De-emphasis transmitter output swing (Analog control) for run-length > 1 F AAIID VREGO VzranlID

![](images/9f3d532024515ccbd555f24f9ea2cfb13ac2f5a3451f0ff1d9180f51cd0be7d1.jpg)

![](images/3c44d0cc9c5805d8a40f8a954ec6de61bac8cf8fd53b0a3fb20b17b5f031a6ea.jpg)

## Next Time

● RX FIR

● RX CTLE

● RX DFE

• Alternate/Future Approaches