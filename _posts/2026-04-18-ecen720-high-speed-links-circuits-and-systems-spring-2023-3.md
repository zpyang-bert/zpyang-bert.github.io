---
layout: post
title:      "ECEN720: High-Speed Links Circuits and Systems Spring 2023"
date:       2026-04-18 17:13:37
author:     "Bert"
tags:
  - Channel
  - Lecture
  - Mineru
---
Lecture 2: Channel Components, Wires, & Transmission Lines

![](/img/mineru_output/lecture2_ee720_channels/auto/images/58d8c6073b3e6e4094888ac9cfea1f92959a472b9d3a0410b57a721d87504861.jpg)

Sam Palermo Analog & Mixed-Signal Center Texas A&M University

## Announcements

● Homework 1 due today

● Lab

Prelab 1 due Jan 30

• Lab 1 report and Prelab 2 due Feb 6

• TA Tong Liu

liut@tamu.edu

Office Hours M 10AM-12PM, WEB 160

## • Reference Material Posted on Website

TDR theory application note

S-parameter notes

## Agenda

● Channel Components

• IC Packages, PCBs, connectors, vias, PCB Traces

● Wire Models

Resistance, capacitance, inductance

Transmission Lines

Propagation constant

• Characteristic impedance

● Loss

·Reflections

• Termination examples

Differential transmission lines

## Channel Components

![](/img/mineru_output/lecture2_ee720_channels/auto/images/ea86c7e1082ffe8f2437ae6725392db4f9d696dbbbb103248470038603f4d8b1.jpg)

## IC Packages

• Package style depends on application and pin count

<table><tr><td rowspan=1 colspan=1>Package Type</td><td rowspan=1 colspan=1>Pin Count</td></tr><tr><td rowspan=1 colspan=1>Small Outline Package (SOP)</td><td rowspan=1 colspan=1>8-56</td></tr><tr><td rowspan=1 colspan=1>Quad Flat Package (QFP)</td><td rowspan=1 colspan=1>64-304</td></tr><tr><td rowspan=1 colspan=1>Plastic Ball Grid Array (PBGA)</td><td rowspan=1 colspan=1>256-420</td></tr><tr><td rowspan=1 colspan=1>Enhanced Ball Grid Array (EBGA)</td><td rowspan=1 colspan=1>352 -896</td></tr><tr><td rowspan=1 colspan=1>Flip Chip Ball Grid Array (FC-BGA)</td><td rowspan=1 colspan=1>1089 - 2116</td></tr></table>

• Packaging technology hasn't been able to increase pin count at same rate as on-chip aggregate bandwidth

• Leads to I/O constrained designs and higher data rate per pin

![](/img/mineru_output/lecture2_ee720_channels/auto/images/ac17dc424870af1c1459548e5db7ad27c83ac09111bd84e1a0193a92c9a7f004.jpg)

[Package Images - Fujitsu]

## IC Package Examples

● Wirebonding is most common die attach method

● Flip-chip packaging allows for more efficient heat removal

● 2D solder ball array on chip allows for more signals and lower signal and supply impedance

Standard Wirebond Package  
![](/img/mineru_output/lecture2_ee720_channels/auto/images/cded7848e65c8330acf887d6ad4f9fb744452c19326700b4a653803a5cdfdad3.jpg)

Flip-Chip/Wirebond Package  
![](/img/mineru_output/lecture2_ee720_channels/auto/images/37da625904561886ea083c1e6924b7bf404c01ec41481f175ac766c46873fcf6.jpg)

Flip-Chip/Solder Ball Package  
![](/img/mineru_output/lecture2_ee720_channels/auto/images/1311a65d66186f6f76a0fb806045ce1f78d1e7eba869ed74024290b438473d8d.jpg)  
[Package Images - Fujitsu]

## IC Package Model

![](/img/mineru_output/lecture2_ee720_channels/auto/images/eec46d9bbc4eaa9ea0b851fa03d88e928193719ebf90d553a4d5bef05e7069dd.jpg)

## IC Package Model Comparisons

![](/img/mineru_output/lecture2_ee720_channels/auto/images/cf1828c406c0939a9b134dedb8974bca8cc2293609ecf45e1c57f3509ba7023b.jpg)  
[Intel]

FCB packaging allows for much less chip interface impedance

<table><tr><td rowspan=3 colspan=1>Electrical Parameter</td><td rowspan=1 colspan=3>Wirebond Package Type</td><td rowspan=1 colspan=2>Flip-chip Package Type</td></tr><tr><td rowspan=2 colspan=1>CPGA</td><td rowspan=2 colspan=1>PPGA</td><td></td><td></td><td></td></tr><tr><td rowspan=1 colspan=1>IPDCA</td><td rowspan=1 colspan=1>OLGA</td><td rowspan=1 colspan=1>FC.PGA</td></tr><tr><td rowspan=1 colspan=1>Bondwire/Die bump R (mohms)</td><td rowspan=1 colspan=1>126 -165</td><td rowspan=1 colspan=1>136 -188</td><td rowspan=1 colspan=1>114 -158</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>0.06</td></tr><tr><td rowspan=1 colspan=1>Bondwire/Die bumpL (nH)</td><td rowspan=1 colspan=1>2.3 -4.1</td><td rowspan=1 colspan=1>2.5 -4.6</td><td rowspan=1 colspan=1>2.1 -4.1</td><td rowspan=1 colspan=1>0.02</td><td rowspan=1 colspan=1>0.013</td></tr><tr><td rowspan=1 colspan=1>Trace R (moniis/cm)</td><td rowspan=1 colspan=1>1200</td><td></td><td></td><td rowspan=1 colspan=1>500</td><td rowspan=1 colspan=1>120</td></tr><tr><td rowspan=1 colspan=1>Trace L (nH/cm)</td><td rowspan=1 colspan=1>4.32</td><td rowspan=1 colspan=1>3.42</td><td rowspan=1 colspan=1>3.42</td><td rowspan=1 colspan=1>3.07</td><td rowspan=1 colspan=1>2.329</td></tr><tr><td rowspan=1 colspan=1>Trace C (pF/cm)</td><td rowspan=1 colspan=1>2.47</td><td rowspan=1 colspan=1>1.53</td><td rowspan=1 colspan=1>1.53</td><td rowspan=1 colspan=1>1.66</td><td rowspan=1 colspan=1>1.707</td></tr><tr><td rowspan=1 colspan=1>Trace Z_0 (ohms)</td><td rowspan=1 colspan=1>42</td><td rowspan=1 colspan=1>47</td><td rowspan=1 colspan=1>47</td><td rowspan=1 colspan=1>43</td><td rowspan=1 colspan=1>38.5</td></tr><tr><td rowspan=1 colspan=1>Pin/Land R (mohms)</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>20</td></tr><tr><td rowspan=1 colspan=1>Pin/Land L (nH)</td><td rowspan=1 colspan=1>4.5</td><td rowspan=1 colspan=1>4.5</td><td rowspan=1 colspan=1>4.0</td><td rowspan=1 colspan=1>0.75</td><td rowspan=1 colspan=1>2.9</td></tr><tr><td rowspan=1 colspan=1>Plating Trace R (mohms/cm)</td><td rowspan=1 colspan=1>1200</td><td rowspan=1 colspan=1>66</td><td rowspan=1 colspan=1>66</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>N/A</td></tr><tr><td rowspan=1 colspan=1>Plating Trace L (nH/cm)</td><td rowspan=1 colspan=1>4.32</td><td rowspan=1 colspan=1>3.42</td><td rowspan=1 colspan=1>3.42</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>N/A</td></tr><tr><td rowspan=1 colspan=1>Plating Trace C (pF/cm)</td><td rowspan=1 colspan=1>2.47</td><td rowspan=1 colspan=1>1.53</td><td rowspan=1 colspan=1>1.53</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>N/A</td></tr><tr><td rowspan=1 colspan=1>Plating Trace Z_0 (ohms)</td><td rowspan=1 colspan=1>42</td><td rowspan=1 colspan=1>47</td><td rowspan=1 colspan=1>47</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>N/A</td></tr><tr><td rowspan=1 colspan=1>Trace Length Range (mm)</td><td rowspan=1 colspan=1>8.83 -26.25</td><td rowspan=1 colspan=1>6.60 -42.64</td><td rowspan=1 colspan=1>4.41-22.24</td><td rowspan=1 colspan=1>3.0- 18.0</td><td rowspan=1 colspan=1>10.0 -42.6</td></tr><tr><td rowspan=1 colspan=1>Plating Trace Length Range (mm)</td><td rowspan=1 colspan=1>1.91-10.50</td><td rowspan=1 colspan=1>1.91-16.46</td><td rowspan=1 colspan=1>0.930-8.03</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>N/A</td></tr></table>

## Printed Circuit Boards

● Components soldered on top (and bottom)

● Typical boards have 4-8 signal layers and an equal number of power and ground planes

● Backplanes can have over 30 layers

![](/img/mineru_output/lecture2_ee720_channels/auto/images/165e3da869f2de7184dbad46f08cff73263d246b961db79e101f2c2b84c75aa3.jpg)

## PCB Stackup

• Signals typically on top and bottom layers

● GND/Power plane pairs and signal layer pairs alternate in board interior

• Typical copper trace thickness

"0.5oz' (17.5um) for signal layers

"1oz' (35um) for power planes

![](/img/mineru_output/lecture2_ee720_channels/auto/images/d34b5bdcfcfbe32a19da9f240dcd73ad5e29674354871e1a640e61917f22f58a.jpg)  
[Dally]

## Connectors

● Connectors are used to transfer signals from board-to-board

● Typical differential pair density between 16-32 pairs/10mm

![](/img/mineru_output/lecture2_ee720_channels/auto/images/16c22b13c4362fcc7cd1061dd507f417309ec832e75907aa3a6c1001b90edb3d.jpg)

## Connectors

Important to maintain proper differential impedance through connector

• Crosstalk can be an issue in the connectors

![](/img/mineru_output/lecture2_ee720_channels/auto/images/9af45342dd9a94709ecb1d6c304b43402128e1668fefdcb4f0de70bdd1b95b52.jpg)

![](/img/mineru_output/lecture2_ee720_channels/auto/images/40cf81275b04157846f5a019d2de781b61cfcf3883479684edd126a5fb93ae6e.jpg)

![](/img/mineru_output/lecture2_ee720_channels/auto/images/8912bdd1279b4ed2e1794c0ce1b0737d83937897d6dee886d4db434c862056d7.jpg)

<table><tr><td colspan="2">TX/RX Nolse % (Victim E4F4)</td></tr><tr><td>Edge Rate</td><td>Nolse</td></tr><tr><td>50ps</td><td>1.9%</td></tr><tr><td>100ps</td><td>1.1%</td></tr></table>

## Vias

## • Used to connect PCB layers

• Made by drilling a hole through the board which is plated with copper

Pads connect to signal layers/traces

• Clearance holes avoid power planes

• Expensive in terms of signal density and integrity

• Consume multiple trace tracks

• Typically lower impedance and create "stubs"

![](/img/mineru_output/lecture2_ee720_channels/auto/images/8e5b9d6b4487c4c88bd184e315d945edc48de84017fa8d65f3ac4d1d75c8ec03.jpg)  
[Dally]

## Impact of Via Stubs at Connectors

![](/img/mineru_output/lecture2_ee720_channels/auto/images/866794173e429ad0636dd1a88d26abae104e57583afa8fe3832d9d155a84074d.jpg)

![](/img/mineru_output/lecture2_ee720_channels/auto/images/ee9fe31addd9b0bf06e30998a888cabcf00f356871dba02083365b54cf7f183d.jpg)  
Legacy BP has default straight vias

• Creates severe nulls which kills signal integrity

Refined BP has expensive backdrilled vias

## PCB Trace Configurations

● Microstrips are signal traces on PCB outer surfaces

• Trace is not enclosed and susceptible to cross-talk

● Striplines are sandwiched between two parallel ground planes

Has increased isolation

![](/img/mineru_output/lecture2_ee720_channels/auto/images/6f46a2579393947b3c7f7216a00a37e8b9b529a6418736ef8ce584602b98137f.jpg)  
Stripline

![](/img/mineru_output/lecture2_ee720_channels/auto/images/8cfa69e1de46e79a63c291cf19cb5a2cd41f8ac2ba1b6b4c81447315374da502.jpg)  
[Johnson]

## Wire Models

• Resistance

● Capacitance

• Inductance

● Transmission line theory

## Wire Resistance

● Wire resistance is determined by material resistivity, p, and geometry

• Causes signal loss and propagation delay

![](/img/mineru_output/lecture2_ee720_channels/auto/images/7bc50c15f5208a770c7ed0158a78237b14e51f96b5afd1cec80dbf78b7cd4d3b.jpg)

$$
R = \frac { \rho l } { A } = \frac { \rho l } { w h }
$$

![](/img/mineru_output/lecture2_ee720_channels/auto/images/1168ab252afe6217c1fa1fd7fd163bc88197bf4101b20d753d6e3f747990fef1.jpg)

$$
R = \frac { \rho l } { A } = \frac { \rho l } { \pi ^ { 2 } }
$$

<table><tr><td>TABLE 3-1 Resistivity of Common Conductive Materials</td></tr><tr><td>Material Symbol  $\rho ( \boldsymbol { \Omega } - \mathbf { m } )$ </td></tr><tr><td>Silver Ag  $1 . 6 \times 1 0 ^ { - 8 }$  Copper Cu  $1 . 7 \times 1 0 ^ { - 8 }$  Gold Au  $2 . 2 \times 1 0 ^ { - 8 }$  Aluminum A1  $2 . 7 \times 1 0 ^ { - 8 }$  Tungsten W  $5 . 5 \times 1 0 ^ { - 8 }$ </td></tr></table>

[Dally]

## Wire Capacitance

● Wire capacitance is determined by dielectric permittivity, $\varepsilon ,$ and geometry

● Best to use lowest $\mathfrak { E } _ { \mathfrak { r } }$

Lower capacitance

Higher propagation velocity

![](/img/mineru_output/lecture2_ee720_channels/auto/images/4ec073f88cb5b57cf1885d64c6db0290f4c21ff2d43ad86600427bdb377bb9ba.jpg)  
Parallel Plate

![](/img/mineru_output/lecture2_ee720_channels/auto/images/c9d952dd6de2abd0008128841b598f650b0f5af1abd5b07b283206326da36837.jpg)  
Coaxial

![](/img/mineru_output/lecture2_ee720_channels/auto/images/0425b7250ecab2fe126ba21b6f65813c9d1216ae2d0f5b3d644d77c0b05a47aa.jpg)  
Wire Pair

$$
C = \frac { w \varepsilon } { s }
$$

$$
C = { \frac { 2 \pi \varepsilon } { \log \left( r _ { 2 } / r _ { 1 } \right) } }
$$

$$
C = { \frac { \pi \varepsilon } { \log ( s / r ) } }
$$

<table><tr><td>TABLE 3-2 Permittivity of Some Typical Insulators</td></tr><tr><td>Material Br</td></tr><tr><td>Air 1 Teflon 2 Polyimide 3 Silicon dioxide 3.9 Glass-epoxy (PC board) 4 Alumina 10 Silicon 11.7</td></tr></table>

![](/img/mineru_output/lecture2_ee720_channels/auto/images/50f71e9b161830c10acc77cbb7190412357046474481b436f2892de27e7d9440.jpg)  
[Dally]  
Rectangle over ground

$$
C = \frac { w \varepsilon } { s } + \frac { 2 \pi \varepsilon } { \log \left( 4 s / h \right) }
$$

## Wire Inductance

● Wire inductance is determined by material permeability, u, and closed-loop geometry

● For wire in homogeneous medium

$$
C L = \varepsilon \mu
$$

● Generally $\mu { = } \mu _ { \mathrm { 0 } } { = } 4 \pi { \times } 1 0 ^ { - 7 } \mathrm { H / m }$

## Wire Models

• Model Types

• Ideal

Lumped C, R, L

RC transmission line

LC transmission line

中 RLGC transmission line

$$
R C L i n e ^ { - M } \frac { I } { I }
$$

$$
\cos \sin \frac { - m } { \frac { I } { J } }
$$

$$
\frac { - M - m } { R L 6 } = \frac { 1 } { 2 } = \frac { 3 } { 5 }
$$

Condition for LC or RLGC model (vs RC) $f _ { 0 } \geq \frac { R } { 2 \pi L }$

<table><tr><td rowspan=1 colspan=1>Wire</td><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>L</td><td rowspan=1 colspan=1>C</td><td rowspan=1 colspan=1>&gt;f (LC wire)</td></tr><tr><td rowspan=1 colspan=1>AWG24 Twisted Pair</td><td rowspan=1 colspan=1>0.082/m</td><td rowspan=1 colspan=1>400nH/m</td><td rowspan=1 colspan=1>40pF/m</td><td rowspan=1 colspan=1>32kHz</td></tr><tr><td rowspan=1 colspan=1>PCB Trace</td><td rowspan=1 colspan=1>52/m</td><td rowspan=1 colspan=1>300nH/m</td><td rowspan=1 colspan=1>100pF/m</td><td rowspan=1 colspan=1>2.7MHz</td></tr><tr><td rowspan=1 colspan=1>On-Chip Min. Width M6(0.18μm CMOS node)</td><td rowspan=1 colspan=1>40k2/m</td><td rowspan=1 colspan=1>4μH/m</td><td rowspan=1 colspan=1>300pF/m</td><td rowspan=1 colspan=1>1.6GHz</td></tr></table>

## RLGC Transmission Line Model

![](/img/mineru_output/lecture2_ee720_channels/auto/images/14e517aa236a297245ffbbcd1d61a3239067d295501f7e77f393e8a1a05160fd.jpg)

As dx →0

$$
\frac { \partial V ( x , t ) } { \partial x } = - R I ( x , t ) - L \frac { \partial I ( x , t ) } { \partial t }
$$

$$
\frac { \partial I ( x , t ) } { \partial x } { = } - G V ( x , t ) { - } C \frac { \partial V ( x , t ) } { \partial t }
$$

(1)

(2)

General Transmission Line Equations

## Time-Harmonic Transmission Line Eqs.

Assuming a traveling sinusoidal wave with angular frequency, ω

$$
\frac { d V \big ( x \big ) } { d x } = - \big ( R + j \omega L \big ) I \big ( x \big )\tag{3}
$$

$$
{ \frac { d I ( x ) } { d x } } = - ( G + j \omega C ) V ( x )
$$

(4)

Differentiating (3) and plugging in (4) (and vice versa)

$$
{ \frac { d ^ { 2 } V { \bigl ( } x { \bigr ) } } { d x ^ { 2 } } } = \gamma ^ { 2 } V { \bigl ( } x { \bigr ) }
$$

(5)

$$
{ \frac { d ^ { 2 } I ( x ) } { d x ^ { 2 } } } { = } \gamma ^ { 2 } I ( x )
$$

(6)

Time-Harmonic Transmission Line Equations

where $\gamma$ is the propagation constant

$$
\sqrt { \gamma = \alpha + j \beta = \sqrt { \big ( R + j \omega L \big ) \big ( G + j \omega C \big ) } \left( \mathrm { m } ^ { - 1 } \right) } \big |
$$

## Transmission Line Propagation Constant

• Solutions to the Time-Harmonic Line Equations:

$$
V ( x ) = V _ { f } \left( x \right) + V _ { r } \left( x \right) = V _ { f 0 } e ^ { - \pi x } + V _ { r 0 } e ^ { \jmath x }
$$

$$
I ( x ) = I _ { _ { f } } ( x ) + I _ { _ { r } } ( x ) = I _ { _ { f 0 } } e ^ { - \jmath x } + I _ { _ { r 0 } } e ^ { \jmath x }
$$

where

$$
\sqrt { \gamma = \alpha + j \beta = \sqrt { \big ( R + j \omega L \big ) \big ( G + j \omega C \big ) } \left( \mathrm { m } ^ { - 1 } \right) }
$$

What does the propagation constant tell us?

Real part (α) determines attenuation/distance (Np/m)

Imaginary part (β) determines phase shift/distance (rad/m)

Signal phase velocity

$$
\boxed { \upsilon = \omega / \beta \pmod { s } }
$$

## Transmission Line Impedance, $Z _ { 0 }$

• For an infinitely long line, the voltage/current ratio is $Z _ { 0 }$

From time-harmonic transmission line eqs. (3) and (4)

$$
\boxed { Z _ { 0 } = \frac { V \big ( x \big ) } { I \big ( x \big ) } = \sqrt { \frac { R + j \omega L } { G + j \omega C } } \big ( \Omega \big ) }
$$

● Driving a line terminated by $Z _ { 0 }$ is the same as driving an infinitely long line

$$
] \equiv _ { 0 } = \underbrace { \frac { \hbar d x - \hbar \omega } { c d x } } _ { \langle c d x \rangle = 1 } \equiv _ { 0 }
$$

ally]

## Lossless LC Transmission Lines

● If $\scriptstyle \mathsf { R d x } = \mathsf { G d x } = 0$

$$
\gamma = \alpha + j \beta = j \omega \sqrt { L C }
$$

$$
\alpha = 0
$$

$$
\beta = \omega \sqrt { L C }
$$

• Waves propagate $w / 0$ distortion

Velocity and impedance independent of frequency

Impedance is purely real

$$
\begin{array} { l } { \displaystyle { \boxed { D = \frac { \omega } { \beta } = \frac { 1 } { \sqrt { L C } } } } } \\ { \displaystyle { \vphantom { \sum _ { 0 } } } } \\ { \displaystyle { \vphantom { \sum _ { 0 } } } } \end{array}
$$

![](/img/mineru_output/lecture2_ee720_channels/auto/images/dac53168db3f7e14ec498ec319b0ab9dfe59d8fc8dc5549862e19dd6cd4b2d51.jpg)

![](/img/mineru_output/lecture2_ee720_channels/auto/images/0dadbfb9afd093e4009f12c76a4dd314fe23b244777d98d45decda8aab243a1a.jpg)

## Low-Loss LRC Transmission Lines

If R/oL and G/ωC << 1

● Behave similar to ideal LC transmission line, but ..

• Experience resistive and dielectric loss

• Frequency dependent propagation velocity results in dispersion

Fast step, followed by slow DC tail

$$
\gamma = \alpha + j \beta = \sqrt { \big ( R + j \omega L \big ) \big ( G + j \omega C \big ) }
$$

$$
\cong j \omega { \sqrt { L C } } { \left( 1 - j { \frac { R C + G L } { \omega L C } } \right) } ^ { \frac { 1 } { 2 } }
$$

$$
\cong \frac { R } { 2 Z _ { 0 } } + \frac { G Z _ { 0 } } { 2 } + j \omega \sqrt { L C } \Biggl [ 1 + \frac { 1 } { 8 } \Biggl ( \frac { R } { \omega L } \Biggr ) ^ { 2 } + \frac { 1 } { 8 } \Biggl ( \frac { G } { \omega C } \Biggr ) ^ { 2 } \Biggr ]
$$

$$
= \alpha _ { R } + \alpha _ { D } + j \beta
$$

R Resistive Loss = Dielectric Loss

$$
\beta \cong \omega \sqrt { L C } \Bigg [ 1 + \frac { 1 } { 8 } \Bigg ( \frac { R } { \omega L } \Bigg ) ^ { 2 } + \frac { 1 } { 8 } \Bigg ( \frac { G } { \omega C } \Bigg ) ^ { 2 } \Bigg ]
$$

$$
{ \sqrt { \upsilon \cong \left( { \sqrt { L C } } { \Biggl [ } 1 + { \frac { 1 } { 8 } } { \Biggl ( } { \frac { R } { \omega L } } { \Biggr ) } ^ { 2 } + { \frac { 1 } { 8 } } { \Biggl ( } { \frac { G } { \omega C } } { \Biggr ) } ^ { 2 } { \Biggr ] } \right) ^ { - 1 } } }
$$

## Frequency-Dependent Loss Mechanisms

● The resistive $( a _ { \mathsf { R } } )$ and dielectric $( \alpha _ { \mathsf { D } } )$ loss terms cause a signal propagating down a transmissionline to become attenuated with distance

![](/img/mineru_output/lecture2_ee720_channels/auto/images/795562e5e41ec80202919f23f5b0b7aa06e62cd42d6f85d41dbe71f8b9e6db51.jpg)

• Resistive loss term is due to conductor skin effect

● Dielectric loss term is due to dielectric absorption

Both terms increase with frequency, although at different rates

## Skin Effect (Resistive Loss)

• High-frequency current density falls off exponentially from conductor surface

● Skin depth, $\delta ,$ is where current falls by $\mathsf { e } ^ { - 1 }$ relative to ful conductor

• Decreases proportional to sqrt(frequency)

● Relevant at critical frequency $\boldsymbol { \mathsf { f } } _ { \mathsf { s } }$ where skin depth equals half conductor height (or radius)

● Above $\boldsymbol { \mathsf { f } } _ { \mathsf { s } }$ resistance/loss increases proportional to sqrt(frequency)

![](/img/mineru_output/lecture2_ee720_channels/auto/images/3150b4d9aa9dce335b91f6a406048716d87a69ee0149183d179712ba2ff4d3a9.jpg)  
[Dally]

$$
J = e ^ { - \frac { d } { \delta } } \qquad \delta = ( \eta / \mu \sigma ) ^ { - \frac { 1 } { 2 } }
$$

For rectangular conductor:

$$
f _ { s } = { \frac { \rho } { \pi \mu \left( { \frac { h } { 2 } } \right) ^ { 2 } } }
$$

$$
R \left( f \right) = R _ { D C } \left( \frac { f } { f _ { s } } \right) ^ { \frac { 1 } { 2 } }
$$

$$
\boxed { \alpha _ { R } = \frac { R _ { D C } } { 2 Z _ { 0 } } \Bigg ( \frac { f } { f _ { s } } \Bigg ) ^ { \frac { 1 } { 2 } } }
$$

## Skin Effect (Resistive Loss)

$$
R _ { D C } = 7 \Omega / m , \ f _ { s } = 4 3 M H z
$$

$$
R _ { D C } = 0 . 0 8 \Omega / m , \ f _ { s } = 6 7 k H z
$$

$$
\boxed { \alpha _ { R } = \frac { R _ { D C } } { 2 Z _ { 0 } } \Bigg ( \frac { f } { f _ { s } } \Bigg ) ^ { \frac { 1 } { 2 } } }
$$

![](/img/mineru_output/lecture2_ee720_channels/auto/images/f32abf5b6c6bf30e0202f2c81ec7c9c12e24c6f577db491958b268c7bd83485a.jpg)

![](/img/mineru_output/lecture2_ee720_channels/auto/images/dac694c55010cb767b75af460d2acdd99fb0131c39eef091409ac86ef98474f6.jpg)

## Dielectric Absorption (Loss)

● An alternating electric field causes dielectric atoms to rotate and absorb signal energy in the form of heat

● Dielectric loss is expressed in terms of the loss tangent

● Loss increases directly proportional to frequency

$$
\tan \delta _ { D } = { \frac { G } { \omega C } }
$$

<table><tr><td>TABLE 3-4 Electrical Properties of PC Board Dielectrics</td></tr><tr><td>Material 8r tan δD</td></tr><tr><td>Woven glass, epoxy resin(&quot;FR-4&quot;) 4.7 0.035 Woven glass,polyimide resin 4.4 0.025 Woven glass, polyphenylene oxide resin (GETEK) 3.9 0.010 Woven glass, PTFEresin(Tefon) 2.55 0.005</td></tr></table>

$$
\begin{array} { c }  \displaystyle { \boxed { \alpha _ { D } = \frac { G Z _ { 0 } } { 2 } = \frac { 2 \pi f C \tan \delta _ { D } \sqrt { L / C } } { 2 } } } \\ { \displaystyle { = \pi f \tan \delta _ { D } \sqrt { L C } } } \end{array}
$$

## Total Wire Loss

![](/img/mineru_output/lecture2_ee720_channels/auto/images/667216a82d31878a64af32f4bc61ff1f1b4a0efd07582c7f95976af5a9ec3634.jpg)

## Advanced Board Dielectrics

![](/img/mineru_output/lecture2_ee720_channels/auto/images/91b4b741e27d800d3ba138f3e284379931bc8c0104b316e91acd54d986b97274.jpg)  
• Tachyon 25dB loss is 15.6"  
• PTFE (Teflon) 25dB loss is $2 2 . 7 ^ { \prime \prime }$  
• Cabled interconnects can support \~1.5m

## Cabled Backplane

![](/img/mineru_output/lecture2_ee720_channels/auto/images/186854a2703bb116dfe4255d2a3be71c785f89a458532c5dc085e85b7e4ff1c3.jpg)

● Cabled backplane with short daughter cards can support \~1m distances at 224Gb/s

## Reflections & Telegrapher's Eq.

![](/img/mineru_output/lecture2_ee720_channels/auto/images/169bb383a45af3eda8c393a07927f25c5cb38bc59d64b8e61fd65ee583c9ed67.jpg)

![](/img/mineru_output/lecture2_ee720_channels/auto/images/9f749719e81ae701b45ed8e3cf7c3c675ef8660e4d5230bbad78a1483d9ee8ac.jpg)

• With a Thevenin-equivalent model of the line:

Termination Current: $I _ { \mathrm { { } } } = \frac { 2 V _ { i } } { Z _ { 0 } + Z _ { T } }$ minotion.

• KCL at Termination:

$$
I _ { f } = { \frac { V _ { i } } { Z _ { 0 } } } , I _ { r } = I _ { f } - I _ { T }
$$

$$
I _ { r } = \frac { V _ { i } } { Z _ { 0 } } - \frac { 2 V _ { i } } { Z _ { r } + Z _ { 0 } }
$$

$$
I _ { r } = \frac { V _ { i } } { Z _ { 0 } } \Biggl ( \frac { Z _ { r } - Z _ { 0 } } { Z _ { r } + Z _ { 0 } } \Biggr )
$$

Telegrapher's Equation or Reflection Coefficient

$$
\boxed { k _ { r } = \frac { I _ { r } } { I _ { f } } = \frac { V _ { r } } { V _ { i } } = \frac { Z _ { T } - Z _ { 0 } } { Z _ { T } + Z _ { 0 } } }
$$

## Termination Examples - Ideal

![](/img/mineru_output/lecture2_ee720_channels/auto/images/9a84d59c2775aa7ddc0298bd7c2d7dab158313bec8859d33baef9459d3820f2f.jpg)

$$
V _ { _ i } = 1 V \left( \frac { 5 0 } { 5 0 + 5 0 } \right) = 0 . 5 V
$$

$$
k _ { r T } = \frac { 5 0 - 5 0 } { 5 0 + 5 0 } = 0
$$

$$
k _ { r S } = \frac { 5 0 - 5 0 } { 5 0 + 5 0 } = 0
$$

$$
\ R _ { 5 } = 5 0 \Omega
$$

$$
\mathbf { Z } _ { 0 } = 5 0 \Omega , \mathbf { t } _ { \mathrm { d } } = 1 \mathsf { n } s
$$

$$
\mathtt { R } _ { \mathsf { T } } = 5 \mathsf { \mathbf { 0 } } \Omega
$$

![](/img/mineru_output/lecture2_ee720_channels/auto/images/3b4647db7530e4dc402f58d83f0bb73f33feb9b91a47776c431b283bc0fa855b.jpg)

## Termination Examples - Open

![](/img/mineru_output/lecture2_ee720_channels/auto/images/27930af3109f1bf6e14b9c6c6b1ac0ccd863ff6203bb5f5334c92549bc1d2a74.jpg)

$$
V _ { _ i } = 1 V \left( \frac { 5 0 } { 5 0 + 5 0 } \right) = 0 . 5 V
$$

$$
k _ { r T } = \frac { \infty - 5 0 } { \infty + 5 0 } = + 1
$$

$$
k _ { r S } = \frac { 5 0 - 5 0 } { 5 0 + 5 0 } = 0
$$

$$
\ R _ { 5 } = 5 0 \Omega
$$

$$
\mathbf { Z } _ { 0 } = 5 0 \Omega , \mathbf { t } _ { \mathrm { d } } = 1 \mathsf { n } s
$$

$$
\mathbb { R } _ { \tau } \sim \infty \left( { \bf 1 } { \bf M } \Omega \right)
$$

![](/img/mineru_output/lecture2_ee720_channels/auto/images/e8140b30ae01db8fbc5ea99aa12bd2015e9394910a092448a035e2d092f50776.jpg)

## Termination Examples - Short

![](/img/mineru_output/lecture2_ee720_channels/auto/images/c8ded89119016e62537141f878ec9f5aa3fa6d7330e80b7819a6da4d47fc4926.jpg)

$$
\begin{array} { l } { \displaystyle { V _ { i } = 1 V \left( \frac { 5 0 } { 5 0 + 5 0 } \right) = 0 . 5 V } } \\ { \displaystyle { k _ { r T } = \frac { 0 - 5 0 } { 0 + 5 0 } = - 1 } } \\ { \displaystyle { k _ { r S } = \frac { 5 0 - 5 0 } { 5 0 + 5 0 } = 0 } } \end{array}
$$

$$
\begin{array} { l } { { \sf R } _ { S } = 5 0 \Omega } \\ { { \sf Z } _ { 0 } = 5 0 \Omega , { \sf t } _ { \mathrm { d } } = 1 \mathsf { n } s } \\ { { \sf R } _ { \mathsf { T } } = 0 \Omega } \end{array}
$$

![](/img/mineru_output/lecture2_ee720_channels/auto/images/a75c84c3109c233ffea59be7d3f57ce84546cf604d97acc6a84b3114e7b780b2.jpg)

## Arbitrary Termination Example

![](/img/mineru_output/lecture2_ee720_channels/auto/images/250b15f6bb0d18b76356c77474172147bc2a7898b8edcc61ed07d62f20af2509.jpg)

$$
V _ { _ { i } } = 1 V \left( { \frac { 5 0 } { 4 0 0 + 5 0 } } \right) = 0 . 1 1 1 V
$$

$$
k _ { r T } = \frac { 6 0 0 - 5 0 } { 6 0 0 + 5 0 } = 0 . 8 4 6
$$

$$
k _ { r S } = \frac { 4 0 0 - 5 0 } { 4 0 0 + 5 0 } = 0 . 7 7 8
$$

$$
\mathsf { R } _ { \mathsf { S } } = \mathsf { 4 0 0 } \Omega
$$

$$
\mathbf { Z } _ { 0 } = 5 0 \Omega , \mathbf { t } _ { \mathrm { d } } = 1 \mathsf { n } s
$$

$$
\aleph _ { \tilde { \tau } } = 6 0 0 \Omega
$$

![](/img/mineru_output/lecture2_ee720_channels/auto/images/fb0ad80e377d546ad1a2b431a85b3a98160d3f6428e1758dbac7f32752c369e9.jpg)

## Lattice Diagram

![](/img/mineru_output/lecture2_ee720_channels/auto/images/514411beceacbe2a11a21f58eb6714645947f82a009546ca3a80d90771f5ee4d.jpg)

$$
\begin{array} { l } { { \sf R } _ { S } = 4 0 0 \Omega } \\ { \quad \displaystyle \boldsymbol { \mathsf { Z } } _ { 0 } = 5 0 \Omega , \ : \boldsymbol { \mathsf { t } } _ { \mathrm { d } } = 1 \mathsf { n } s } \\ { \quad \displaystyle { \sf R } _ { \mathsf { T } } = 6 0 0 \Omega } \end{array}
$$

![](/img/mineru_output/lecture2_ee720_channels/auto/images/513e1dffac7daa446e27c3f16ab72beef2613e1dae46b75fdc0b7de381c23ce6.jpg)

## Termination Reflection Patterns

![](/img/mineru_output/lecture2_ee720_channels/auto/images/08437306d083fa30d5324fd6ef6dcfe6ce8c1d1494174033ad005e012c43ad06.jpg)

![](/img/mineru_output/lecture2_ee720_channels/auto/images/6e96bbd17e99efc7b1e2c60a12668f43b340c030d853505edc3e7fe768a2d853.jpg)

## Termination Schemes

## No Termination

• Little to absorb line energy

● Can generate oscillating waveform

• Line must be very short relative to signal transition time

• $n = 4 - 6$

Limited off-chip use

## • Source Termination

Source output takes 2 steps up

• Used in moderate speed pointto-point connections

![](/img/mineru_output/lecture2_ee720_channels/auto/images/31a023c4a86938b60ed762eaf67557fb02b62065ddffad25901794280ffac5e2.jpg)

$$
t _ { r } > n T _ { r o u n d - t r i p } = 2 n l \sqrt { L C }
$$

![](/img/mineru_output/lecture2_ee720_channels/auto/images/05a116c6229401abc6ddbbcb87ef72a1098532c6cd87b44f5634f2f3ab5e5738.jpg)

## Termination Schemes

## • Receiver Termination

No reflection from receiver

• Watch out for intermediate impedance discontinuities

•Little to absorb reflections at driver

## • Double Termination

• Best configuration for min reflections

Reflections absorbed at both driver and receiver

● Get half the swing relative to single termination

• Most common termination scheme for high performance serial links

![](/img/mineru_output/lecture2_ee720_channels/auto/images/8b2508eb978bd0ce9b413fd3d1f885169feda02963e25ce425d055c381a31ff4.jpg)

![](/img/mineru_output/lecture2_ee720_channels/auto/images/bb2118acaf044666c9b39354052a4b856c640d11365d8958cbb5571413bc4580.jpg)

## Differential Signaling

● Differential signaling advantages

Self-referenced

• Common-mode noise rejection

Increased signal swing

Reduced selfinduced power-supply noise

● Requires 2x the number of signaling pins relative to single-ended signaling

But, smaller ratio of supply/signal (return) pins

• Total pin overhead is typically 1.3-1.8x (vs 2x)

## Odd & Even Modes

![](/img/mineru_output/lecture2_ee720_channels/auto/images/7a95853a3ef67af0753b6e033441852d192f0df5af423dee68311c51d47f7be4.jpg)

![](/img/mineru_output/lecture2_ee720_channels/auto/images/04a8048d6e7f7453858d6f0f74bc75dca9adc0201a158805aade49a88ed55014.jpg)  
[Hall]

![](/img/mineru_output/lecture2_ee720_channels/auto/images/05ae51ba2c8c65e6c7c223987c0625eca2ab8ec1a17a13ab5ab0331728d6eef6.jpg)

![](/img/mineru_output/lecture2_ee720_channels/auto/images/5b6c004f2df7291e14d70856bc4a123e1c559bbbd7d886bbe1cf7a7e1c715cc0.jpg)

Even mode

• When equal voltages drive both lines, only one mode propagates called even more

● Odd mode

• When equal in magnitude, but out of phase, voltages drive both lines, only one mode propagates called odd mode

● For a differential pair (odd mode), a virtual reference plane exists between the conductors that provides a continuous return current path

Electric field is perpendicular to the virtual plane

Magnetic field is tangent to the virtual plane

## Balanced Transmission Lines

● Even (common) mode excitation

• Effective ${ \mathsf C } = { \mathsf C } _ { \mathsf C }$

• Effective $\mathsf { L } = \mathsf { L } + \mathsf { M }$

● Odd (differential) mode excitation

Effective $\mathsf { C } = \mathsf { C } _ { \mathsf { C } } + 2 \mathsf { C } _ { \mathsf { d } }$

Effective $\mathsf { L } = \mathsf { L } - \mathsf { M }$

$$
\boxed { Z _ { D I F F } = 2 Z _ { o d d } , \quad Z _ { C M } = \frac { Z _ { e v e n } } { 2 } }
$$

![](/img/mineru_output/lecture2_ee720_channels/auto/images/affe19bb8752a0d7eb6e10380517b357b5abfb4aded4c0c7520ebfb8eeccda82.jpg)  
(a) Model of a Balanced Line

$$
\boxed { \begin{array} { l } { \displaystyle { \overline { { Z _ { e v e n } } } = \overline { { { \left( { \frac { L + M } { C _ { c } } } \right) } ^ { \vee 2 } } } } } \\ { \displaystyle { \overline { { Z _ { o d d } } } = \overline { { { \left( { \frac { L - M } { C _ { c } + 2 C _ { d } } } \right) } ^ { \vee 2 } } } } } \end{array} }
$$

## PI-Termination

![](/img/mineru_output/lecture2_ee720_channels/auto/images/17b8840da9e47a6b620f464f1f78747138578b402d9ebafd72c6b158eb95e2e9.jpg)

## T-Termination

![](/img/mineru_output/lecture2_ee720_channels/auto/images/56e7635f2d8b675c9f475949c0aaec3ad075949eb0b142966b38a33143b964e7.jpg)

## Next Time

● Channel modeling

· Time domain reflectometer (TDR)

Network analysis