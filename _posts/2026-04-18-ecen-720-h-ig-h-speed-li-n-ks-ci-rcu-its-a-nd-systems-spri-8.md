---
layout: post
title:      "ECEN 720 : H ig h-Speed Li n ks Ci rcu its a nd Systems Spri ng 2023"
date:       2026-04-18 21:16:42
author:     "Bert"
tags:
  - Clocking
  - Lecture
  - Mineru
  - PLL
---
## Lectu re 1 1 : Clocki ng Arch itectu res & PLLs

![](images/d3b35ef917f0b27814d357e4971775d6e17baa3adcf3c73923869b8339d688d8.jpg)

Sa m Pa lermo Ana log & M ixed -Sig na l Center Texas A&M U n iversity

## An nou ncements

• Project Prel i m i na ry Report d ue Apr 1 8

• Project Fi na l Report d ue May 2

## Agenda

## • Clocki ng Arch itectu res

• PLLs

• M od e l i n g

• N oi se tra n sfe r fu n ctio n s

## References

• H ig h -speed l i n k clocki ng tutoria l pa per, PLL a na lysis pa per, a nd PLL thesis posted on website

• Posted PLL models i n project section

• Website has add itiona l l i n ks on PLL a nd j itte r tuto ri a l s

M ajority of today’s PLL materia l comes fro m Fi sch ette tuto ria l a n d M . M a n su ri ’s Ph D thesis ( UCLA)

## H ig h -Speed Electrica l Li n k System

![](images/9605065472e6483adecd0ae28c238a2d39f926fabc773113dd57fc67aabfdc01.jpg)

## Clocki ng Term i nology

![](images/e2bcd386d2ebad740c245d10e032072767fe6c275f005c02b8c1b33d58545157.jpg)  
phase recovery

![](images/b09427d8014be26270bf4812f738888ef053c29bf39e3252b76fc4f156dcf986.jpg)

magic box & buffer  
![](images/b30d0d31df95d87a883e8b01e63b94d8603c00289b52477432bf3c1e2cc56b61.jpg)

![](images/c7a12c1590202fd337a658ed07965819cbc135619de023c04856e5742fca2662.jpg)

## Synch ronous

Every ch i p gets sa me freq uency AN D phase

Used i n low-speed busses

## Mesochronous

Sa me freq uency, but u n known phase

Req u i res phase recovery ci rcu itry

Ca n d o with o r with o ut fu l l C D R

• Used i n fast memories, i nterna l system i nterfaces, MAC/Packet i nterfaces

## Plesiochronous

• Al most the sa me freq uency, resu lti ng i n slowly d rifti n g p ha se

• Req u i res CDR

Widely used i n h ig h-speed l i n ks

## Asynch ronous

N o cl ocks at a l l

Req uest/acknowledge ha ndsha ke proced u re

Used i n em beddded systems, U n ix, Li n ux

## I/O Clocki ng Arch itectu res

• Th ree basic I/O a rch itectu res

• Com mon Clock (Synch ronous)

Forwa rd Clock (Sou rce Synch ronous)

Em bedded Clock (Clock Recovery)

• These I/O a rch itectu res a re used for va ryi ng a ppl ications th at req u i re d iffe re nt l eve l s of I/O ba n dwi dth

• A processor may have one or a l l of these I/O types

• Often the sa me ci rcu itry ca n be used to em u late d ifferent I/O schemes for desig n reu se

## Com mon Clock I/O Arch itectu re

## [ Kra uter ]

![](images/1405d8e72f2f6f8e07f770060c0a39b348a6d1602220d216bbbf3a5569c1379b.jpg)

• Com mon i n orig i na l com puter systems

• Synch ronous system by desig n (no active deskew)

• Com mon bus clock controls ch i p-to-ch i p tra nsfers

• Req u i res eq ua l length routes to ch i ps to m i n i m ize clock skew

• Data rates typica l ly l i m ited to \~ 1 00 M b/s

## Com mon Clock I/O Cycle Ti me

Cycle time to meet setup time

![](images/e46aa5b744fcd149da1618cd64d460140e1772c024b890df27841f6d3e6e2b91.jpg)

## Com mon Clock I/O Li m itations

Difficu lt to control clock skew a nd propagation delay

• Need to have tig ht control of a bsol ute delay to meet a g iven cycl e ti m e

• Sensitive to delay va riations i n on -ch i p ci rcu its a nd boa rd ro utes

• Ha rd to com pensate for delay va riations d ue to low correlation between on-ch i p a nd off-ch i p delays

• Wh i le com mon ly used i n on -ch i p com m u n ication, offers l i m ited speed i n I/O a ppl ications

## Forwa rd Clock I/O Arch itectu re

Multi-Channel Serial Link System

## RX Data Channels

![](images/2f3ef31dfa1d5a9200b1144479668d37820279b5bc63eea5371e9f9bd43f2f77.jpg)

• Com mon h ig h-speed reference clock is forwa rded from TX ch i p to RX ch i p

• Mesoch ronous system

• Used i n processor- memory i nterfaces a nd m u lti - processor com m u n ication

• I n te l Q PI

• Hypertra nsport

• Req u i res one extra clock cha n nel

• “Coherent” clocki ng a l lows lowto- h i g h freq u e n cy j itte r tra cki n g

• Need good clock receive a m pl ifier as the forwa rded clock is atten uated by the cha n nel

## Forwa rd Clock I/O Li m itations

Multi-Channel Serial Link System  
![](images/079d9eed83639e47a69f28f5ae25ab137a9a63d15768a8fa27a6a501635d6ad7.jpg)

• Clock skew ca n l i m ited forwa rd clock I/O performa nce

• Driver strength a nd load i ng m ismatches

• I ntercon nect length m ismatches

## • Low pass cha n nel ca uses j itter a m p l ifi cati o n

• Duty-Cycle va riations of forwa rded clock

## Forwa rd Clock I/O De-Skew

Multi-Channel Serial Link System  
![](images/16b30c33734d1602b9dd5aac435a3c6add23bd7a05d9182519a290501c230fbd.jpg)

• Per-cha n nel de-skew a l lows for sig n ifica nt data rate i ncreases

• Sa m ple clock adj usted to center clock on the i ncom i ng data eye

• I m plementations

• Delay- Locked Loop a nd Phase I nte rpo l ato rs

• I njection - Locked Osci l lators

## • Phase Acq u isition ca n be

• BER based – no add itiona l i n put phase sa m plers

• Phase detector based i m plemented with add itiona l i n put phase sa m plers period ica l ly powered on

## Forwa rd Cl ock I/O Ci rcu its

## Multi-Channel Serial Link System

![](images/86362dae372b920f97930390d0dd8c9de404da3f3fe3a17145e4b113165c5ee2.jpg)

• TX PLL

• TX Clock Distri bution

• Repl ica TX Clock Driver

• Cha n nel

• Forwa rd Clock Am pl ifier

• RX Clock Distri bution

• De-Skew Ci rcu it

• D LL/ PI

• I njection - Locked Osci l lator

## Em bedded Clock I/O Arch itectu re

Multi-Channel Serial Link System  
![](images/eca46b0ba40133a5d378e6bf77d674e7b1de39abaff17b44ef145fe20da037e6.jpg)

• Ca n be used i n mesoch ronous or plesioch ronou s systems

• Clock freq uency a nd opti m u m phase position a re extracted from i ncom i ng data strea m

• Phase detection conti n uously ru n n i ng

• CDR I m plementations

• Per-cha n nel PLL- based

• Dua l - loop w/ G loba l PLL &

• Loca l D LL/PI

• Loca l Phase- Rotator PLLs

## Em bedded Clock I/O Li m itations

![](images/05fddc3dcdab784d39f0bea7571094dd12a1102788d97485875041367924d9f7.jpg)

## • J itte r tra c ki n g l i m ited by CDR ba ndwidth

• Tech nology sca l i ng a l lows CD Rs with h ig her ba ndwidths wh ich ca n ach ieve h ig her freq uency j itte r tra c ki n g

## • Genera l ly more ha rdwa re tha n forwa rd clock i m plementations

• Extra i n put phase sa m plers

## Em bedded Clock I/O Ci rcu its

## Multi-Channel Serial Link System

![](images/9aa1884ca7c07d2c5c051a5e900dd15a6f0cf6ff7d1546d31cb8124abe13302e.jpg)

## • TX PLL

## • TX Cl ock D i stri butio n

## • CDR

• Per-cha n nel PLL- based

• Dua l - loop w/ G loba l PLL &

• Loca l D LL/PI

• Loca l Phase- Rotator PLLs

• G loba l PLL req u i res RX cl ock d i stri b utio n to i nd ivid ua l cha n nels

## Xi l i nx 0 . 5-3 2G b/s Tra nsceiver Clocki ng

![](images/2f788f5350220632d8d8b7c3ef91a89f299c285746671bc6dfd517e6d577e65b.jpg)

<table><tr><td rowspan=1 colspan=1>Technology</td><td rowspan=1 colspan=1>CMOS 16nm FinFET</td></tr><tr><td rowspan=1 colspan=1>Power Supply (Vave, Vavt, Vaux)</td><td rowspan=1 colspan=1>0.9 V, 1. 2V, 1.8 V</td></tr><tr><td rowspan=1 colspan=1>Frequency range</td><td rowspan=1 colspan=1>500 Mb/s – 32.75 Gb/s</td></tr><tr><td rowspan=1 colspan=1>Transceiver Quad area</td><td rowspan=1 colspan=1>2.625 mm × 2.218 mm</td></tr><tr><td rowspan=1 colspan=1>LC PLL range</td><td rowspan=1 colspan=1>8-16.375 GHz</td></tr><tr><td rowspan=1 colspan=1>Ring PLL range</td><td rowspan=1 colspan=1>2-6.25 GHz</td></tr><tr><td rowspan=1 colspan=1>TX PRBS7 jitter at 32.75Gb/s</td><td rowspan=1 colspan=1>TJ: 5.39 ps, RJ: 190 fs</td></tr><tr><td rowspan=1 colspan=1>32.75Gb/s RX JTOL @ 30MHz@ 100MHz</td><td rowspan=1 colspan=1>0.45 UI0.6 UI</td></tr><tr><td rowspan=1 colspan=1>Channel loss at 32.75Gb/s</td><td rowspan=1 colspan=1>30 dB</td></tr><tr><td rowspan=1 colspan=1>Measured BER at 32.75Gb/s</td><td rowspan=1 colspan=1>&lt; 10-15</td></tr><tr><td rowspan=1 colspan=1>Power at 32.75Gb/s with DFE</td><td rowspan=1 colspan=1>577mW/ch (17.6pJ/b)</td></tr></table>

[U pad hyaya VLSI 20 16 ]

• LC- PLL with 2 LC-VCOs used to cover h ig h data rates (8-3 2G b/s)

• Ri ng - PLL u sed for lower data rates

• CM L clock d istri bution with active i nd uctive loads used fo r l ow j itte r

## PLLs

## • PLL model i ng

• PLL noise tra nsfer fu nctions

## PLL Block Diag ra m

![](images/6699e9da808118ca2b3e022a1ddcf94fdcb46b3c24d81b2e1d753535695fc59e.jpg)

• A phase- locked loop ( PLL) is a negative feed back system where a n osci l lator-generated sig na l is phase AN D freq uency locked to a reference sig na l

## PLL Appl ications

## • PLLs a ppl ications

## Freq uency synthesis

• M u lti plyi ng a 1 00 M Hz reference clock to 1 0G Hz

## Skew ca ncel lation

• Phase a l ig n i ng a n i nterna l clock to a n I/O clock

## • Clock recovery

Extract from i ncom i ng data strea m the clock freq uency a nd opti m u m phase of h ig h-speed sa m pl i ng clocks

## Mod u lation/De- mod u lation

Wi reless systems

• Spread -spectru m clocki ng

## Forwa rd Cl ock I/O Ci rcu its

## Multi-Channel Serial Link System

![](images/dfe37dc448faf733d88ff1e4e72d019f47915268db02ca90c71e2907852b00fe.jpg)

• TX PLL

• TX Clock Distri bution

• Repl ica TX Clock Driver

• Cha n nel

• Forwa rd Clock Am pl ifier

• RX Clock Distri bution

• De-Skew Ci rcu it

• D LL/ PI

• I njection - Locked Osci l lator

## Em bedded Clock I/O Ci rcu its

## Multi-Channel Serial Link System

![](images/18e312fb8f952a7df8d1fd8459704bd37dec2557deae6207d10acd5f4aec2a37.jpg)

## • TX PLL

## • TX Cl ock D i stri butio n

## • CDR

• Per-cha n nel PLL- based

• Dua l - loop w/ G loba l PLL &

• Loca l D LL/PI

• Loca l Phase- Rotator PLLs

• G loba l PLL req u i res RX cl ock d i stri b utio n to i nd ivid ua l cha n nels

## PLL Desig n Cha l lenges

• Boa rd - level reference clock freq uencies don ’t sca le often • 1 56M Hz is a com mon freq uency

• RX CDR ba ndwidth is ha rd to sca le with PAM4 sig na l i ng a nd ADC- based front-ends

• Typica l ly 2-4M Hz

• PLL ba ndwidth m u st be kept less tha n 1 0 M Hz for sta bi l ity a n d to fi lte r refe re n ce j itte r

• VCO phase noise at low-freq uency offsets d ue to fl icker noise m ust be su ppressed

32. 75Gbps Transceiver PLL Simulated Jitter Numbers
<table><tr><td rowspan=1 colspan=1>Receiver Type</td><td rowspan=1 colspan=1>PLL PN @1MHz</td><td rowspan=1 colspan=1>CDR BW</td><td rowspan=1 colspan=1>RJ</td><td rowspan=1 colspan=1>RJ in UI</td></tr><tr><td rowspan=1 colspan=1>Analog based RX</td><td rowspan=1 colspan=1>-92.4dBc/Hz</td><td rowspan=1 colspan=1>12.7MHz</td><td rowspan=1 colspan=1>160.7fs</td><td rowspan=1 colspan=1>5.26mUI</td></tr><tr><td rowspan=1 colspan=1>ADC based RX</td><td rowspan=1 colspan=1>-92.4dBc/Hz</td><td rowspan=1 colspan=1>2MHz</td><td rowspan=1 colspan=1>407fs</td><td rowspan=1 colspan=1>13.3mUI</td></tr></table>

## [Tu rker ISSCC 20 1 9 ]

## Cha rge Pu m p PLL

![](images/a11e060c64ba1170f58adff9e3418d4e015ccf5120036d3cae36f27ed6f84371.jpg)

• Cha rge pu m p PLL is a com mon i m plementation

• Type-2 (2 i nteg rators) a l lows for idea l ly zero phase error between the i n put a nd feed back phase

• Req u i res a sta b i l i z i n g ze ro th at i s rea l i zed with th e fi lte r res i sto r

• A seconda ry ca pacitor ${ \mathsf C } _ { 2 }$ i s ofte n a d d ed fo r a d d iti o n a l fi lte ri n g to red uce reference spu rs

• M odeled as a th i rd -order system

## Li nea r PLL Model

![](images/ccef6ddd1eca1561fef307552a7aae852ec91689b52a11819b4501426010d1e4.jpg)

• Phase is the key va ria ble of i nterest

Output phase response to a sti m u l us i njected at a g iven poi nt i n the loop

• Phase error response is a l so i nformative

• Li nea r “sma l l -sig na l ” a na lysis is u sefu l for u ndersta nd PLL dyna m ics if

PLL is locked (or nea r lock)

• I n put phase deviation a m pl itude is sma l l enoug h to ma i nta i n operation i n lock ra nge

## U ndersta nd i ng PLL Freq uency Response

Input phase response

![](images/621a40f4e3731718270ea1f0bb114f8c0326aa49d178b8dab6985f385c906726.jpg)  
VCO output phase response

![](images/41a1889a50cb027ece22f6b2c3a808648aff90dad18bd9c7a082ca637767a4e0.jpg)

• Freq uency doma i n a na lysis ca n tel l us how wel l the PLL tracks the i n put phase as it cha nges at a certa i n freq uency

• PLL tra nsfer fu nction is d ifferent depend i ng on wh ich poi nt i n the loop the output is respond i ng to

## Li nea r PLL Model

![](images/80031b71c161205c0bd7111c7d5555c2a2123a390b809f094c9d22079f55bc6c.jpg)

For Cha rge Pu m p PLL :

$$
K _ { P D } = \frac { I _ { C P } } { 2 \pi }
$$

$$
F ( s ) = { \frac { \left( { \frac { 1 } { C _ { 2 } } } \right) \left( s + { \frac { 1 } { R C _ { 1 } } } \right) } { s \left( s + { \frac { C _ { 1 } + C _ { 2 } } { R C _ { 1 } C _ { 2 } } } \right) } }
$$

$$
H ( s ) = \frac { \phi _ { o u t } ( s ) } { \phi _ { i n } ( s ) } = \frac { \frac { K _ { P D } K _ { V C O } } { C _ { 2 } } \left( s + \frac { 1 } { R C _ { 1 } } \right) } { s ^ { 3 } + \left( \frac { C _ { 1 } + C _ { 2 } } { R C _ { 1 } C _ { 2 } } \right) s ^ { 2 } + \left( \frac { K _ { P D } K _ { V C O } } { N C _ { 2 } } \right) s + \frac { K _ { P D } K _ { V C O } } { N R C _ { 1 } C _ { 2 } } }
$$

## 14G Hz PLL Closed - Loop Tra nsfer Fu nction

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Fref</td><td rowspan=1 colspan=1>156.25MHz</td></tr><tr><td rowspan=1 colspan=1>N</td><td rowspan=1 colspan=1>90</td></tr><tr><td rowspan=1 colspan=1>Fvco</td><td rowspan=1 colspan=1>14GHz</td></tr><tr><td rowspan=1 colspan=1> $\mathsf { f } _ { \mathsf { u } }$ </td><td rowspan=1 colspan=1>2MHz</td></tr><tr><td rowspan=1 colspan=1> $\Phi _ { \mathrm { m } }$ </td><td rowspan=1 colspan=1> $6 0 ^ { \circ }$ </td></tr><tr><td rowspan=1 colspan=1> $\mathsf { f } _ { 3 \mathsf { d B } }$ </td><td rowspan=1 colspan=1>3.1MHz</td></tr><tr><td rowspan=1 colspan=1>Kvco</td><td rowspan=1 colspan=1>2π*1GHz/V</td></tr><tr><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>4kΩ</td></tr><tr><td rowspan=1 colspan=1> ${ \mathsf { C } } _ { \uparrow }$ </td><td rowspan=1 colspan=1>74pF</td></tr><tr><td rowspan=1 colspan=1> ${ \sf C } _ { 2 }$ </td><td rowspan=1 colspan=1>5.8pF</td></tr><tr><td rowspan=1 colspan=1> $\boldsymbol { \mathrm { I } } _ { \mathtt { C P } }$ </td><td rowspan=1 colspan=1>310uA</td></tr></table>

![](images/828eb9c569174821be1c2b691c916839edceb93339b5c9ba2d8f3d2936d6d307.jpg)

$$
H ( s ) = \frac { \phi _ { o u t } ( s ) } { \phi _ { i n } ( s ) } = \frac { \frac { K _ { P D } K _ { V C O } } { C _ { 2 } } \left( s + \frac { 1 } { R C _ { 1 } } \right) } { s ^ { 3 } + \left( \frac { C _ { 1 } + C _ { 2 } } { R C _ { 1 } C _ { 2 } } \right) s ^ { 2 } + \left( \frac { K _ { P D } K _ { V C O } } { N C _ { 2 } } \right) s + \frac { K _ { P D } K _ { V C O } } { N R C _ { 1 } C _ { 2 } } }
$$

## Com mon PLL Noise Sou rces

![](images/55f238ad9c91ad842a9631a79fc3ed4e38ef03c11166d3432d960492590c2fec.jpg)

$$
\begin{array} { r l } & { S _ { \phi _ { o u t } } ^ { \phi _ { i n } } = S _ { \phi _ { i n } } | N T F _ { I N } ( s ) | ^ { 2 } } \\ & { S _ { \phi _ { o u t } } ^ { i c p } = S _ { i _ { C } } | N T F _ { C P } ( s ) | ^ { 2 } } \\ & { \quad S _ { \phi _ { o u t } } ^ { v _ { R } } = S _ { v _ { R } } | N T F _ { R } ( s ) | ^ { 2 } } \\ & { \quad S _ { \phi _ { o u t } } ^ { \phi _ { V C O } } = S _ { \phi _ { V C o } } | N T F _ { V C O } ( s ) | ^ { 2 } } \\ & { S _ { \phi _ { o u t } } ^ { T o t a l } = S _ { \phi _ { o u t } } ^ { i c _ { D } } + S _ { \phi _ { o u t } } ^ { i c _ { D } } + S _ { \phi _ { o u t } } ^ { \phi _ { V C O } } } \end{array}
$$

## Noise Tra nsfer Fu nctions

$$
N T F _ { I N } ( s ) = \frac { \phi _ { o u t } ( s ) } { \phi _ { i n } ( s ) } = \frac { ( N ) L G ( s ) } { 1 + L G ( s ) }
$$

$$
N T F _ { C P } ( s ) = \frac { \phi _ { o u t } ( s ) } { i _ { C P } ( s ) } = \frac { \left( \frac { N } { K _ { P D } } \right) L G ( s ) } { 1 + L G ( s ) }
$$

$$
N T F _ { R } ( s ) = \frac { \phi _ { o u t } ( s ) } { v _ { R } ( s ) } = \frac { \frac { K _ { V C O } } { s } } { 1 + L G ( s ) }
$$

$$
N T F _ { V C O } ( s ) = \frac { \phi _ { o u t } ( s ) } { \phi _ { V C O } ( s ) } = \frac { 1 } { 1 + L G ( s ) }
$$

![](images/b3d4f14a26466d38e6812594c3193b61512fc3922e9f0dfa5a2318c8ee0ae055.jpg)

• I n put reference a nd cha rge pu m p noise is low- pass fi ltered

• Loop fi lter noise (VCO i n put noise) is ba nd - pass fi ltered

• VCO output phase noise is h ig h - pass fi ltered

## PLL Phase N oise & J itter

![](images/97f99567f63ee51e6501c208530bbb63ba904329d0e82796eb23f00ac4656d31.jpg)

## [Tu rker ISSCC 20 18]

<table><tr><td></td><td>同</td><td>同]</td><td>[5]</td><td>(同]</td><td>This Work</td></tr><tr><td>PLL Avchitecture</td><td>iteger N, SSPD based</td><td>FracN, SSPD DPLL</td><td>F</td><td>SPD based Ineger N,</td><td>Integer N, CP based</td></tr><tr><td>VCO</td><td>LC</td><td>LC</td><td>LC</td><td>LC</td><td>LC</td></tr><tr><td>Techndogy</td><td>180nm</td><td>28nm</td><td>14nmFinFET</td><td>16nm FinFET</td><td>16nm FinFET</td></tr><tr><td>Referonce Freqg(MHz)</td><td>5.25</td><td>40</td><td>26</td><td>450</td><td>500</td></tr><tr><td>Frequency Range (GHz)</td><td>221</td><td>27-4.3</td><td>5.38</td><td>9.18</td><td>7.4-14</td></tr><tr><td>Measumert Foguncy (GHz)</td><td>2.21</td><td>5.82</td><td>269</td><td>18</td><td>6.25</td></tr><tr><td>Phase Noise @100kH2 (dBoH2)</td><td>(@200KHt) .125</td><td>-105.5</td><td>-113.6</td><td>104.1 (@200KHz)</td><td>.120</td></tr><tr><td>Phase Nose @1MH2 (dBoHz)</td><td>(from fgure) -125</td><td>-115.4</td><td>.122.45</td><td>-107.3</td><td>.123.2</td></tr><tr><td>Phase Noise @100KH2 (nommalzed to 1GHz)</td><td>(@200kHt) 131.9</td><td>-120.8</td><td>.1222</td><td>(@200KHz) 129.2</td><td>.135.9</td></tr><tr><td>Phase Nose 1MH2</td><td>-131.9</td><td>-130.7</td><td>- 131</td><td>.132.4</td><td>-139.1</td></tr><tr><td>RAMS Jter (t)</td><td>160 (10k- 100M)</td><td>159 (10k −40M)</td><td>(10k − 10M) 137</td><td>(1k − 100M) 164</td><td>(10k-10M) 53.6</td></tr><tr><td>Referonoe Spur(Bc)</td><td>-56</td><td>-78</td><td>-87.6</td><td>NA</td><td>.75.5*</td></tr><tr><td>Power (mi)</td><td>2.5</td><td>8.2</td><td>13.4</td><td>29.2</td><td>45</td></tr><tr><td>Area (mm)</td><td>02</td><td>0.3</td><td>0.257</td><td>0.39</td><td>0.35</td></tr><tr><td>FOM(dB)</td><td>NA *including DAC, masured at 1.052GH2 DAC oput</td><td>-243.4</td><td>NA</td><td>-239.3</td><td>-246.8</td></tr></table>

• PLL ti me-doma i n j itter is obta i ned by i nteg rati ng the output phase noise

• We ca n model a n i nd ivid ua l noise sou rce’s contri bution

$$
\sigma _ { j , T o t a l } ^ { 2 } = \frac { 2 } { \omega _ { 0 } ^ { 2 } } \int _ { f _ { s t a r t } } ^ { f _ { s t o p } } S _ { \phi _ { o u t } } ^ { T o t a l } ( f ) d f
$$

$$
\sigma _ { j , i } ^ { 2 } = \frac { 2 } { \omega _ { 0 } ^ { 2 } } \int _ { f _ { s t a r t } } ^ { f _ { s t o p } } S _ { i } ( f ) | N T F _ { i } ( f ) | ^ { 2 } d f
$$

RM S J itte r $\sigma _ { j } = \sqrt { \sigma _ { j , T o t a l } ^ { 2 } }$

$$
\sigma _ { j , T o t a l } ^ { 2 } = \sum _ { i } \sigma _ { j , i } ^ { 2 }
$$

## Wi re l i ne Tra n sceiver J itter M od e l i ng

![](images/c1bdc13e95d7b32d69d3bb7d6cac1b8e6cff7f9269832814fe72749c18f1e8db.jpg)

![](images/153b6a369ca4ef2f35c52a2fa963a0367eb5b6838adddb20042e5f2d19b8311f.jpg)

• Relative j itter (dyna m ic phase error) between the RX CDR-generated sa m pl i ng clock a nd i n put data sets the system ti m i ng ma rg i n

• Th is CD R h ig h - pass response provides add itiona l fi lteri ng

Modeled as a 4M Hz $1 ^ { \mathsf { s t } _ { - } }$ order response (I EEE 802 . 3 & OI F-CEI)

$$
\sigma _ { j S Y S , i } ^ { 2 } = \frac { 2 } { \omega _ { 0 } ^ { 2 } } \int _ { 0 } ^ { \frac { f _ { 0 } } { 2 } } S _ { i } ( f ) | N T F _ { i } ( f ) | ^ { 2 } | C D R ( f ) | ^ { 2 } d f
$$

## I n put Reference Noise

Si l icon La bs U ltra Low J itter Crysta l Osci l lator

![](images/74d742e7dc29d9e25ec07c9284e3ac562bfae8a116d49999ec07dd44f1e1efa9.jpg)  
Phase Noise at 156. 26M Hz

![](images/c986f9ea2474b78220afefe2e92cc60fb5f86cdf3b8087c3abcd28d2b66202aa.jpg)  
• Refe re n ce j itte r $\sigma _ { \mathrm { j , i n } } = 2 2 6 \mathsf { f s } _ { \mathrm { r m s } }$ ( 1 0 kHz – 1 0 M Hz)

## I n put Reference Noise

$$
N T F _ { I N } ( s ) = \frac { \frac { K _ { P D } K _ { V C O } } { C _ { 2 } } \left( s + \frac { 1 } { R C _ { 1 } } \right) } { s ^ { 3 } + \left( \frac { C _ { 1 } + C _ { 2 } } { R C _ { 1 } C _ { 2 } } \right) s ^ { 2 } + \left( \frac { K _ { P D } K _ { V C O } } { N C _ { 2 } } \right) s + \frac { K _ { P D } K _ { V C O } } { N R C _ { 1 } C _ { 2 } } }
$$

![](images/a763df1062618cc67bd69523744c272cb9df795c31309b4168b9efffb8a78a7f.jpg)

![](images/0da1a170128366bba14b4566e6a3330c3de3c21bd1e8ac560d36b04260e2016e.jpg)

• Afte r P LL : $\sigma _ { \mathrm { j , i n } } = 2 1 7 \mathsf { f s } _ { \mathrm { r m s } }$ ( 1 0 kHz – 1 0 M Hz)

• I ncl u d i ng CD R : $\sigma _ { \mathrm { j , i n } } = 4 5 \mathsf { f s } _ { \mathrm { r m s } }$ ( 1 00 Hz – 7G Hz)

## Cha rge Pu m p Noise

![](images/edc73337ba878669a2dc1b1f60304d9b42ec977801e884d632ac469ab590622e.jpg)

![](images/c118254787b89102e1e66a2b709b3932808eae1d84aad70ef57e257ed4fe4747.jpg)

$$
S _ { i _ { C P } } = \frac { T _ { r s t } } { T _ { r e f } } \left( S _ { i _ { n , M P } } + S _ { i _ { n , M N } } \right)
$$

![](images/8da2503588d71cdbc96344e1254b50701df76feeaec0fe1df8ed81f134e57f26.jpg)

• Cha rge pu m p noise cu rrent is i njected i nto the loop fi lter d u ri ng the PFD reset ti me

• Trade-off between cha rge pu m p noise contri bution a nd deadzone robustness

• Tra nsistor fl icker noise ca n contri bute sig n ifica ntly to PLL i n- ba nd phase noise

## Cha rge Pu m p Noise

$$
N T F _ { C P } ( s ) = { \frac { { \frac { K _ { V C O } } { C _ { 2 } } } \left( s + { \frac { 1 } { R C _ { 1 } } } \right) } { s ^ { 3 } + \left( { \frac { C _ { 1 } + C _ { 2 } } { R C _ { 1 } C _ { 2 } } } \right) s ^ { 2 } + \left( { \frac { K _ { P D } K _ { V C O } } { N C _ { 2 } } } \right) s + { \frac { K _ { P D } K _ { V C O } } { N R C _ { 1 } C _ { 2 } } } } }
$$

![](images/66d5224412301013fbd615298fd767ede6e47a07c33ad9502c4bf500e71e25f6.jpg)

![](images/1acd6d2d5200c0a404f74ba3c33e6774f68584a8016c3adb5e03f76ba9c4f538.jpg)

• Afte r P LL : $\sigma _ { \mathrm { j , \mathsf { C P } } } = 2 0 5 \mathsf { f s } _ { \mathrm { r m s } }$ ( 1 0 kHz – 1 0 M Hz)

• I ncl u d i ng CD R : $\sigma _ { \mathrm { j , C P } } = 5 2 \mathsf { f s } _ { \mathrm { r m s } }$ ( 1 00 Hz – 7G Hz)

## Loop Fi lter R N oise

![](images/a0717a98a570b97fb1a384872da7b6442c0149ac674c0e62711165b8ca8906ce.jpg)

![](images/84523217f66ed726d2fe073380a2343e0e19f172a1c8c9db7731abf7f9fb1d8b.jpg)

• Tra d e-off betwee n resi sto r n o i se, l oo p fi lte r ca pacitor size, a nd cha rge pu m p noise

• S m a l l e r res i sto r res u lts i n l a rg e r ca pa cito rs ( h i g h e r a rea ) a nd la rger cha rge pu m p cu rrent (h ig her $\mathsf { S } _ { \mathsf { i C P } } )$

## Loop Fi lter R N oise

$$
N T F _ { R } ( s ) = \frac { K _ { V C O } s \left( s + \frac { C _ { 1 } + C _ { 2 } } { R C _ { 1 } C _ { 2 } } \right) } { s ^ { 3 } + \left( \frac { C _ { 1 } + C _ { 2 } } { R C _ { 1 } C _ { 2 } } \right) s ^ { 2 } + \left( \frac { K _ { P D } K _ { V C O } } { N C _ { 2 } } \right) s + \frac { K _ { P D } K _ { V C O } } { N R C _ { 1 } C _ { 2 } } }
$$

![](images/9ab7a22716c86244d7ec0063926e7842f47494fcb2d18fcc4c04abd2d3d91472.jpg)

![](images/8dbd79e3211159a859a9216f70efcaf3f666edb9912bf8b80fc0deb5ac6e2d56.jpg)

• Afte r P LL : $\sigma _ { \mathrm { j } , \mathsf { R } } = 1 2 8 \mathsf { f s } _ { \mathsf { r m s } }$ ( 1 0 kHz – 1 0 M Hz)

• I ncl u d i ng CD R : $\sigma _ { \mathrm { j } , \mathsf { R } } = 8 1 \mathsf { f s } _ { \mathsf { r m s } }$ ( 1 00 Hz – 7G Hz)

## VCO Noise

![](images/75a68e0e9610334b5447a3b81964171ff191ee95519ecb7b0b4d719d76a0f8a4.jpg)

![](images/f032438482f2891cbcf20da0906fdc7d25d00cf4115a9ee8c0d488255c4055d2.jpg)

• LC-VCO phase noise sou rces

Fi n ite ta n k q u a l ity fa cto r

• Cross-cou pled pa i r

• Ta i l cu rrent sou rce

## VCO Noise

$$
N T F _ { V C O } ( s ) = { \cfrac { s ^ { 2 } \left( s + { \cfrac { C _ { 1 } + C _ { 2 } } { R C _ { 1 } C _ { 2 } } } \right) } { s ^ { 3 } + \left( { \cfrac { C _ { 1 } + C _ { 2 } } { R C _ { 1 } C _ { 2 } } } \right) s ^ { 2 } + \left( { \cfrac { K _ { P D } K _ { V C O } } { N C _ { 2 } } } \right) s + { \cfrac { K _ { P D } K _ { V C O } } { N R C _ { 1 } C _ { 2 } } } } }
$$

![](images/e5a36fc6291d235993baffdd910d47af99e9506c1ac756697f0a359a9b137882.jpg)

![](images/5ca4c50569f29e1c704c068763c263c762612c20fbabaab879838636695aa07e.jpg)

• After PLL : $\sigma _ { \mathrm { j } , \mathsf { v c o } } = 2 5 7 \mathsf { f s } _ { \mathsf { r m s } }$ ( 1 0 kHz – 1 0 M Hz)

• I ncl ud i ng CDR: $\sigma _ { \mathrm { j } , \mathsf { R } } = 1 2 5 \mathsf { f s } _ { \mathrm { r m s } }$ ( 1 00 Hz – 7G Hz)

## Tota l N oise

![](images/80f95edbaf6632a04d4dd7dcc0dec57907f6680f728b9a7b511796349bafb931.jpg)

![](images/14742b8ce179a76872375e05a423a9c7cc251f62ff90a908deeebae6fcdf209b.jpg)

• After PLL : $\sigma _ { \mathrm { j , 7 o t a l } } = 4 1 4 \mathsf { f } s _ { \mathrm { r m s } } \left( 1 0 \mathsf { k H z } - 1 0 \mathsf { M } \mathsf { H } z \right)$

Reference clock a nd cha rge pu m p noise dom i nates at low freq uency

VCO dom i nates nea r loop ba ndwidth a nd h ig her

I ncl ud i ng CDR: $\sigma _ { \mathrm { j , \tau o t a l } } = 1 6 4 \mathsf { f } s _ { \mathrm { r m s } } \left( 1 0 0 \mathsf { H z } - 7 \mathsf { G H z } \right)$

Now VCO noise clea rly dom i nates tota l

Loop resistor noise is a la rger percentage

## PLL Noise Tra nsfer Fu nction Ta ke-Away Poi nts

The way a PLL sha pes phase noise depends on where the noise is i ntrod uced i n the loop

• Opti m izi ng the loop ba ndwidth for one noise sou rce may en ha nce other noise sou rces

• Genera l ly, the PLL low- pass sha pes i n put phase noise, ba nd - pass sha pes VCO i n put voltage noise, a nd h ig h- pass sha pes VCO/clock buffer output phase noise

## Osci l l ato r N o i se

![](images/706431ae2aca4a88c7f83e87268b5f553d2b6b39d216bd45815ecd93a4e16313.jpg)

![](images/f97dcd53dc4c146a2260ea3ebf6c25d084a08e4b80b2805415caa311c1e72f1f.jpg)

## Osci l lator Phase Noise M odel

![](images/8bae54a9522988cbe12dc3e60ec6105ca8b4f04df96184d5e56611ac2ca39249.jpg)

$$
L ( f ) { = } 1 0 \log \left( { \frac { \mathrm { N o i s e S p e c t r a l D e n s i t y } } { \mathrm { C a r r i e r P o w e r } } } \right) \left( \mathbf { d B c } / \mathbf { H z } \right)
$$

Leeson ’s Model : $L ( \Delta f ) = 1 0 \log \left( \frac { 2 F k T } { P _ { s i g } } \left( 1 + \left( \frac { 1 } { 2 Q } \frac { f _ { o } } { \Delta f } \right) ^ { 2 } \right) \left( 1 + \frac { \Delta f _ { _ { 1 / f ^ { 3 } } } } { \left| \Delta f \right| } \right) \right)$

• For i m proved model see Haj i m i ri pa pers

## Open - Loop VCO J itter

![](images/5506805f760e9605393faf371deed1e07774d3f72658566a5b2195a62c00fc20.jpg)

• M easu re d istri bution of clock th reshold crossi ng s

• P l ot   a s a fu n cti o n of d e l ay $\Delta \mathsf { T }$

## Open - Loop VCO J itter

![](images/35d4b4ae85ea71b96c9d3519a64a909567666accbc780fa7b6385c99cca239a4.jpg)  
J itte r   i s p ro po rti o n a l to sq rt( T)

•  i s VCO ti m e d o m a i n fi g u re of m e rit

## VCO i n Closed - Loop PLL J itter

![](images/58772257440ac3101fc4f4c5b811413df750b49259348dc8a941a5b061aa576f.jpg)  
• PLL l i m its   for delays longer tha n loop ba ndwidth $\tau _ { \mathrm { L } }$

$$
\tau _ { L } = 1 / 2 \mathcal { \eta } _ { L }
$$

## Ref Cl k- Referenced vs Self- Referenced

![](images/acce3761356b7bab3ba05dee69a013348dbdd5935c3da6642557ad5b4a1b5864.jpg)

![](images/044adc859694c569d55aa6a4ec006de6be6535370a2106881c1b9da8912ccff7.jpg)

![](images/253df331c09648ba6c9e80a7e635eab5b82bdea14915806725470652c868fc02.jpg)

• Ge n e ra l ly, we ca re a bo ut th e j itte r w . r . t . th e ref. c l oc k $( \sigma _ { \mathsf { x } } )$

• However, may be easier to measu re w. r.t. delayed version of output cl k

• Due to noise on both edges, th is wi l l be i ncreased by a sq rt(2) factor relative to th e refe re n ce c l oc k- refe rred j itte r 49

## Converti ng Phase N oise to J itter

![](images/c0b2b00815d13c3e11146668134b345a7a7b59fff06375fa0ada9333f4117749.jpg)

• RM S j itte r fo r $\Delta \mathsf { T }$ accu m u lation $\sigma _ { \Delta T } ^ { 2 } = \frac { 8 } { \omega _ { o } ^ { 2 } } \int _ { 0 } ^ { \infty } S _ { \phi } ( f ) s i n ^ { 2 } ( \pi f \Delta T ) d f$

• As $\Delta \mathsf { T }$ g oes to  ∞ $\sigma _ { T } ^ { 2 } = \frac { 2 } { \omega _ { o } ^ { 2 } } R _ { \phi } \left( 0 \right) = \frac { 2 } { \omega _ { o } ^ { 2 } } \int \ d S _ { \phi } \left( f \right) d f$

• Actua l i nteg ration ra nge depends on a ppl ication ba ndwidth • $\mathsf { f } _ { \mathsf { m i n } }$ set by assu med CDR tracki ng ba ndwidth

• $\mathsf { f } _ { \mathsf { m a x } }$ set by Nyq u ist freq uency $( \mathsf { f } _ { 0 } / 2 )$

• Most exact a pproach

$$
\sigma _ { T } ^ { 2 } = \frac { 2 } { \omega _ { o } ^ { 2 } } \begin{array} { c } { { f _ { 0 } } } \\ { { 2 } } \\ { { \omega _ { \phi } ^ { 2 } \left( f \right) \left| H _ { s y s } \left( f \right) \right| ^ { 2 } d f } } \end{array}
$$

where $\left| H _ { s y s } \left( f \right) \right| ^ { 2 }$ i s the system j itter trans fer function

## Ti me Doma i n Model

• Ti me doma i n models ca ptu res the d iscrete-ti me operation of the PLL a rch itectu res

I nteraction between cha rge pu m p a nd loop fi lter

Cycle sl i ppi ng behavior

• Al lows model i ng of non - l i nea r control systems

Dyna m ic loop ba ndwidth control

Automatic freq uency ba nd selection

Potentia l i m plementation tools

• Matla b Si m u l i n k

• CppSi m

• Cadence

## Si m u l i n k Model

PLL FREQUENCY SYNTHESIZER MODEL  
![](images/9d696cec30d557727e8cbb287c02b4b57f59e3a2d250bf1534205aa23407436e.jpg)

PFD  
![](images/775abbb652244bcc5c920a613573627aa294e32baeb885e5dbfd242fa1aee916.jpg)

![](images/430fc04d8776162ca7d91ed351d926c9fcceb276cee6741339052a5bf903718b.jpg)

## Freq uency Step w/ Si m u l i n k Model

VCO control voltage response to i n put freq uency step

KVCO = 2 \* 1G Hz/V (LC Osc)  
![](images/6d3083d93885cf92d4df0d71fdf2c1720981919e0af84e0392a685d2d4869df0.jpg)

$v _ { \mathrm { v c o } } { = } 2 \pi ^ { * }$ 10G Hz/V (Ri ng Osc)  
![](images/d2b4aebe3765ca2fe928f1b2288b5775b3b92faaa3a7fad189dd9bcfe1663031.jpg)  
• Voltage spi kes d ue to cha rge pu m p cu rrent d rivi ng loop fi lter resistor

• Cycle sl i ppi ng occu rs d u ri ng lock acq u isition d ue to la rge i n itia l freq uency d ifference

## CppSi m Model

![](images/f3b9540efafa52fe54b1d4bb9982028363cc7aaa1c28b75bae37ebbe7b8bb12c.jpg)

## [ Perrott/ Men i nger]

![](images/55ea0095c933e934844a3ec33a703a2b4704be3ba7de3085fb9707dd2eeb4d0c.jpg)

https : //cppsi m . com/

• C+ + based a l lows for ra pid si m u lation of adva nced a rch itectu res

• Ma ny usefu l bu i ld i ng blocks i ncl uded

![](images/abfdf7966b7346939377810b88c35a1dbf87b43ab0a488823cd5483863b2c9a4.jpg)

![](images/dc450069b2a87b4a0908724cd68a14aafef36caaf98b601a38633b183ce82a3b.jpg)

## Cadence Veri log-A Model

![](images/148096f000b07e2a5dccdc1924b79a33e1d8626f7d5ace8cdbaee51bca3b7751.jpg)

module vco\_advanced\_backup (in, out);   
parameter Emin = 13.5625G;   
else inst\_freq =((v(in)−vmin) + (Emax−Emin)/(vnax−Vnin)) + Emin :

![](images/60f30f39bb15b9b61b439f88bac1ebade47e41038e2093de477ba8c1a34da59f.jpg)

## Next Ti me

## • CDRs

The fol lowi ng sl ides provide more deta i l s on PLL ci rcu its . Th is 620 materia l may u sefu l for the project, but won ’t be covered i n d eta i l on Exa m 2 .

## PLL Loop Ga i n

![](images/1489bfba96c605d8f7c2ba3c9341ebe6bc6b3283ab1d54122a21075bcf1e0bd4.jpg)

$$
L G ( s ) = \frac { K _ { P D } F ( s ) K _ { V C O } } { N s } = \frac { K _ { P D } K _ { V C O } \left( s + \frac { 1 } { R _ { 1 } C _ { 1 } } \right) } { N C _ { 2 } s ^ { 2 } \left( s + \frac { C _ { 1 } + C _ { 2 } } { R _ { 1 } C _ { 1 } C _ { 2 } } \right) }
$$

$$
\omega _ { z } = \frac { 1 } { R _ { 1 } C _ { 1 } } , \qquad \omega _ { p 1 } = \omega _ { p 2 } = 0 , \qquad \omega _ { p 3 } = \frac { C _ { 1 } + C _ { 2 } } { R _ { 1 } C _ { 1 } C _ { 2 } }
$$

## Loop Ga i n Response

![](images/dd6ef4e8ac4feaf099e90ec260a2246fb857b753ba2f0371e62d1875b5391b2f.jpg)

$$
\omega _ { p 1 } = \omega _ { p 2 } = 0
$$

$$
\omega _ { z } = \frac { 1 } { R _ { 1 } C _ { 1 } }
$$

$$
\omega _ { p 3 } = \frac { C _ { 1 } + C _ { 2 } } { R _ { 1 } C _ { 1 } C _ { 2 } }
$$

$$
\Phi _ { m } = \tan ^ { - 1 } \left( \frac { \omega _ { u } } { \omega _ { z } } \right) - \tan ^ { - 1 } \left( \frac { \omega _ { u } } { \omega _ { p 3 } } \right)
$$

## Desig n Proced u re for Max $\Phi _ { \mathsf { m } }$

![](images/309b8de44c579b8c965ce94708d42e051df3551c66539ece80b54442a4a25fce.jpg)

PLL Specs
<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Fref</td><td rowspan=1 colspan=1>156.25MHz</td></tr><tr><td rowspan=1 colspan=1>N</td><td rowspan=1 colspan=1>90</td></tr><tr><td rowspan=1 colspan=1>Fvco</td><td rowspan=1 colspan=1>14GHz</td></tr><tr><td rowspan=1 colspan=1> $^ { 4 }$ </td><td rowspan=1 colspan=1>2MHz</td></tr><tr><td rowspan=1 colspan=1> $\infty$ </td><td rowspan=1 colspan=1> $6 0 ^ { \circ }$ </td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Kvco</td><td rowspan=1 colspan=1> $2 \pi ^ { * } 1 \mathsf { G H z } N$ </td></tr><tr><td rowspan=1 colspan=1>R</td><td rowspan=1 colspan=1>??</td></tr><tr><td rowspan=1 colspan=1> ${ \mathsf { C } } _ { 1 }$ </td><td rowspan=1 colspan=1>??</td></tr><tr><td rowspan=1 colspan=1> $\mathsf { C } _ { 2 }$ </td><td rowspan=1 colspan=1>??</td></tr><tr><td rowspan=1 colspan=1> $\boldsymbol { \mathrm { I } } _ { \mathtt { C P } }$ </td><td rowspan=1 colspan=1>??</td></tr></table>

• Desig n proced u re maxi m izes phase ma rg i n for a g iven $\mathsf { f } _ { \mathsf { u } }$ a nd $\Phi _ { \mathsf { m } }$ specification [ Ha n u mol u TCAS 1 2004]

## Desig n Proced u re for Max $\Phi _ { \mathsf { m } }$

1 . Set l oo p fi lte r ca pa cito r rati o ba sed o n $\Phi _ { \mathsf { m } }$

$$
K _ { C } = \frac { C _ { 1 } } { C _ { 2 } } = 2 \left( t a n ^ { 2 } ( \Phi _ { m } ) + t a n ( \Phi _ { m } ) \sqrt { t a n ^ { 2 } ( \Phi _ { m } ) + 1 } \right)
$$

$$
\Phi _ { m } = 6 0 ^ { \circ }  K _ { C } = 1 2 . 9
$$

2 . Set loop fi lter va l ues based on $\mathfrak { O } _ { \mathsf { U } }$ & with R set fo r l ow n o i se

$$
\omega _ { z } = \frac { \omega _ { u } } { \sqrt { 1 + K _ { C } } }
$$

$$
C _ { 1 } = \frac { 1 } { \omega _ { z } R } , \ C _ { 2 } = \frac { C _ { 1 } } { K _ { C } }
$$

$$
\omega _ { u } = 2 \pi * 2 M H z \to \omega _ { z } = 2 \pi * 5 3 6 k H z
$$

$$
\mathrm { S e t } R = 4 k \Omega  C _ { 1 } = 7 4 p F \& C _ { 2 } = 5 . 8 p F
$$

3 . Set $\mathtt { I _ { c p } }$ to ach ieve req u i red loop ga i n

$$
I _ { c p } = \frac { \mathrm { N } C _ { 2 } \omega _ { u } ^ { 2 } } { K _ { V C O } } \sqrt { \frac { \omega _ { p 3 } ^ { 2 } + \omega _ { u } ^ { 2 } } { \omega _ { z } ^ { 2 } + \omega _ { u } ^ { 2 } } }
$$

$$
\omega _ { p 3 } = 2 \pi * 7 . 4 5 M H z \to I _ { c p } = 3 1 0 \mu A
$$

## Si m u lated Responses

![](images/5dd454064e408764da88a35d532a1042fa2e33635e1439459c5a2f11e34b0bdc.jpg)

![](images/ba90d563e515280c7c356ad87a14be9f4a3fb381e29f4ef9e19370491a57f367.jpg)

• Desig n ach ieves $f _ { \mathrm { u } } { = } 2 M H z$ a n d $\Phi _ { \mathrm { m } } = 6 0 ^ { \circ }$

• Closed loop response has $\mathsf { f } _ { 3 \mathrm { d } \mathsf { B } } { = } 3 . 1 \mathsf { M } \mathsf { H } z$

## Cha rge- Pu m p PLL Ci rcu its

• Phase Detector

• Cha rge- Pu m p

• Loo p Fi lte r

• VCO

• D ivi d e r

![](images/bada3cde0ef3442c2fc2284d14e20dbc5058c4d462d3af4c75a0499d564f9226.jpg)

## Phase Detector

![](images/95d2a2daa8ab0492f2ed4a37a8c4ecf99f01707908662c9d26ac0a6809299d50.jpg)

![](images/dd6e22c3f3bd0c4dd4f6e65d9a4178dba74fc8126825e86faa2ea28157ded2f5.jpg)  
avg ?? ௘ ?? ൌ ??௉஽ Δ??

• Detects phase d ifference between feed back clock a nd reference clock

• Th e l oo p fi lte r wi l l fi lte r th e p h a se d etecto r o utp ut, th us to cha racterize phase detector ga i n, extract average output voltage

![](images/b383b7a81fa84c8cd72173a2d0eceba1f7267f1ed19a50d08069347884091a51.jpg)

• The $K _ { \mathsf { P D } }$ factor ca n cha nge depend i ng on the specific phase detector ci rcu it

$K _ { \scriptscriptstyle P D }$ units are V/rad when used with  a dimension - le s s filter

$K _ { \scriptscriptstyle P D }$ units are rad (averaged) or A/rad when combined with the charge - pump-1

## Ana log M u lti pl ier Phase Detector

$$
\begin{array} { r l } & { \mathcal { A } _ { 1 } \cos \omega _ { 1 } t \xrightarrow [ ] { \mathcal { A } _ { 1 } \cos \omega _ { 1 } d _ { 2 } } \mathrm { c o s } [ ( \omega _ { 1 } + \omega _ { 2 } ) t + \Delta \phi ] + \frac { \alpha d _ { 1 } d _ { 2 } } { 2 } \cos [ ( \omega _ { 1 } - \omega _ { 2 } ) t - \Delta \phi ] } \\ & { \mathcal { A } _ { 2 } \cos ( \omega _ { 2 } t + \Delta \phi ) \xrightarrow [ \mathrm { ~ \alpha ~ } ] { \mathcal { A } _ { 1 } \sin \operatorname { s e r } g \sin } \mathrm { g a i n } } \end{array}
$$

• I f ${ \mathfrak { o } } _ { 1 } { = } { \mathfrak { o } } _ { 2 }$ a nd fi lteri ng out h ig h -freq uency term

$$
\overline { { y ( t ) } } = \frac { \alpha A _ { 1 } A _ { 2 } } { 2 } \cos { \Delta \phi }
$$

• Nea r $\Delta \phi$ l ock reg i o n of  /2 : ${ \overline { { y ( t ) } } } \approx { \frac { \alpha A _ { 1 } A _ { 2 } } { 2 } } { \left( { \frac { \pi } { 2 } } - \Delta \phi \right) }$

![](images/a0b58f8def87408771b4dd5abbc94adb6a0fd4a17209d96cf4f34224904ad58d.jpg)

## XOR Phase Detector

![](images/2d6c9658d822d9ac4a2caa6ebf4dee04434c326239e9cc76c045b51f588b67dc.jpg)

![](images/1db4252a2cbeae00487bcf3f4e12038e4c8c13b33afbd09eb7581cadc1def64d.jpg)

![](images/da80ce2190d266032e4318dcb9ddf17f8ac61278081dcc69232c926733aee3e3.jpg)

![](images/5392260cf1f2b50943b5324f45be93a98c3d4e6b61c6fe13fef66f8a7498253f.jpg)

![](images/fa4f8bef8904f1f5a5e8c4d6535d90f5d41dae10b811aee0bbd7e8aa8d9d7c28.jpg)  
[ Razavi ]

• Assu m i ng log ic $1 = " + 1 "$ a nd $0 { = } " { \bf - } 1 ^ { \prime \prime }$ the XOR PD wi l l lock when the average output is 0

• Ge n e ra l ly, $\pi / 2$ is a sta ble lock poi nt a nd $- \pi / 2$ i s a m eta sta b l e po i nt

• Sensitive to clock d uty cycle

## XOR Phase Detector

![](images/629d6c450d73d4a977188f5d26588ec94eee60614e387daa978fcb30cf9a854b.jpg)

![](images/423b71df372cb283ab398bfe55c30f2b83ab25db32d6aef0e02ba01e487e856c.jpg)

Width is sa me for both leading and lagging phase difference!

$$
W = - \biggl ( \frac { \Phi _ { \sf r e f } - \Phi _ { \sf d i v } } { \pi } \biggr ) \top / 2
$$

$$
W = \bigg ( \frac { \Phi _ { \mathsf { r e f } } - \Phi _ { \mathsf { d i v } } } { \pi } \bigg ) \top / 2
$$

[ Perrott ]

![](images/758a282935f1cf972cca2993b5c83ab5c99deed7b4f3a3ef21b864cfb16717bd.jpg)

## Cycle Sl i ppi ng

• If there is a freq uency d ifference between the i n put reference a nd PLL feed back sig na ls the phase detector ca n j u m p between reg ions of d ifferent ga i n

PLL is no longer acti ng as a l i nea r system

![](images/3079bf027124892057dd0daa749bdfcd7d5bcbad1695148f1ba279d881b35518.jpg)

## Cycle Sl i ppi ng

Synthesizer Response To Divider Step  
![](images/bd93f03ed5f38c7d20e3bf05afeb4e3a34e1fed696abb6a7c041430d71856e70.jpg)

![](images/964ad272f54fea3c6d5dc53f08bd01f15747dff7b7b79358ebb3fce2f508b3c7.jpg)  
• If freq uency d ifference is too la rge the PLL may not lock

## Phase Freq uency Detector ( PFD)

![](images/1abff0f21f0cd98a70ccbc9ba446ac88fb96ef23951f83e0dda96a5f9e60be28.jpg)

• Phase Freq uency Detector a l lows for wide freq uency locki ng ra nge, potentia l ly enti re VCO tu n i ng ra nge

• 3-stage operation w/ U P & D N outputs

• Risi ng edge-triggered resu lts i n d uty cycle i nsensitivity

![](images/64f89aa5de46cbcaa883dc4ad5edb2a68d5ff9f6f46a44acc9a0b760b1646ff3.jpg)

![](images/87e5209c15aa0311cd8486b46df6084c97de7c504f6a8a333636669cb5861fc1.jpg)

## Averaged PFD Tra nsfer Cha racteristic

U P= 1 & DN = - 1

![](images/408c07d605f764169e4145c8eca965cad0b59321c6febc77570cc9dd5d6f2500.jpg)

![](images/38dc18031d2532bba06d48f25462bbcf181914004e0a66a834d5598169b8c43c.jpg)

• Consta nt slope a nd pola rity asym metry a bout zero phase a l lows for wide freq uency ra nge operation

• The averaged PFD ga i n is $1 / ( 2 \pi )$ with u n its of $\mathsf { r a d } ^ { - 1 }$

## Phase Detector

![](images/68ad60cc8dfd92c4a4544585bfa82189da7676bd63cf74c0e62c7a878664a12b.jpg)

• Detects phase d ifference between feed back clock a nd reference clock

• Th e l oo p fi lte r wi l l fi lte r th e p h a se d etecto r o utp ut, th u s to ch a ra cte ri ze phase detector ga i n, extract average output voltage (or cu rrent for cha rge- pu m p PLLs)

## PFD Deadzone

![](images/52c4346d8d9d506e27e39153e83d414c24d33f63a84b3a9a5e0fe0a4e05604c4.jpg)

![](images/c9a1ddfa75f7681eb971e85c17fc0f9a32d37dc6283acc35e6d4bb33902d13cb.jpg)

• If p h a se e rro r i s s m a l l , th e n s h o rt output pu lses a re prod uced by PFD

• Ca n not effectively propagate these pu lses to switch cha rge pu m p

• Resu lts i n phase detector “dead zone” wh ich ca uses low loop ga i n a nd i ncreased j itter

![](images/1e8840bb58567913e78cfff89e4deb3e12bd4f7a0a18de6c7891a7abe44c01da.jpg)

## PFD Operation w/ Reset Delay

• Sol ution is to add delay i n PFD reset path to force a m i n i m u m U P a nd DN pu lse length

• I n locked state both U P a nd D N cu rrent sou rces a re on for ${ \sf T } _ { \sf r s t } ,$ b ut i d ea l ly n o n et cu rre nt i s d e l ive red to l oo p fi lte r

![](images/23902bfd970301854f3a350c9f3bb8952ee291d80d441c57d821a07e8be65466.jpg)

![](images/e289fe1dea9c960b9bc1b749d3e2d2ab1120de9055b6ab54f041900cdabe1b67.jpg)

## Problems Nea r 2 

• PFD ca n not react to i n put risi ng edges d u ri ng reset

• Th is ca n resu lt i n the next risi ng edge d rivi ng the loop i n the wrong d i rection

• Reset delay ca n i ncrease acq u isition ti me a nd sets a max PFD operati ng freq uency

![](images/3f94c70ba5bf2fdd0395c45ed27dddad564eb840363faaae317f42e35312882e.jpg)

![](images/00b01fc7d3b72f5b64c4d2df8c351b9053bd0964b85a9369cf524bcdc39379f8.jpg)

![](images/8fb91b0fda68e057c7fd8ba4e3d7ae048e2a4fd3a667b830e494ad75a77017fc.jpg)

## PFD Tra nsfer Cha racteristic w/ Reset Delay

![](images/4d0fafa80980204f60fb24206bee6a54aaf4747be3e79bd25b7d453541a36fcd.jpg)

PFD reset delay generates wrong freq uency i nformation

• If th is becomes a la rge percentage of the reference cycle, then the PFD ca n fa i l to acq u i re freq uency lock

$$
 \frac { \mathsf { M a x } \ : T _ { r s t } = \frac { T _ { r e f } } { 2 } } { \mathsf { M a x } \ : \mathsf { P F D } \ : \mathsf { F r e q u e n c y } = \frac { 1 } { 2 T _ { r s t } } } \Bigg |
$$

## Cha rge- Pu m p PLL Ci rcu its

• Phase Detector

• Cha rge- Pu m p

• Loo p Fi lte r

• VCO

• D ivi d e r

![](images/a6a95de724bf8e32d54d550d325205d31e204e71dc261ed6d344b0e004ddfee4.jpg)

## Cha rge Pu m p

![](images/ffad68ea79e24bac19d1119f0716fc58b46c400f91400c45c9c5c98835c8a723.jpg)

• Converts PFD output sig na l s to cha rge

• Cha rge is proportiona l to PFD pu l se widths

Un - Averaged Charge - Pump Gain $= I _ { { \scriptscriptstyle C P } }$  Amp s

Averaged Charge $\mathrm { - P u m p G a i n } = { \frac { I _ { C P } } { 2 \pi } } \left( { \frac { \mathrm { A m p s } } { \mathrm { r a d } } } \right)$

Total PFD & Charge - Pump Gain    CPI 2  rad Amps  

This gain can vary if a different phase detector is used

## Si m ple Cha rge Pu m p

![](images/1db97df57151bd8fe12645d55d0691dd1ea9c581e826335d63a8c22550e419ec.jpg)

• Issues

• Skew between U PB a nd DN control sig na ls

Match i ng of U P/D N cu rrent sou rces

• Clock feedth roug h a nd cha rge i njection from switches onto $\mathsf { V } _ { \mathsf { c t r l } }$

Cha rge sha ri ng between cu rrent sou rce d ra i n nodes’ ca pacita nce a nd $\mathsf { V } _ { \mathsf { c t r l } }$

## Si m ple Cha rge Pu m p Skew Com pensation

![](images/5f5f8f199d176ca50ca06454b5640fe516e6a7891b475c4bbfd0bac531b52158.jpg)

3/ 2 I nverter Path  
![](images/83afc5e23e5f69ce9a7b0d8be1d573b344407d5ac11b715df08a66739170d70e.jpg)

• Add i ng a tra nsm ission gate i n the D N sig na l path hel ps to eq ua l ize the delay with the U PB sig na l for better overla p between the U P a nd D N cu rrent sou rces

• Poor match i ng of U PB a nd $\mathsf { D N } _ { \Delta }$ edge rates

• Uti l i z i n g a 3 - i nve rte r U P path a nd a 2-i nverter DN path with a h ig her fa nout provides good match i ng of both delay a nd edge rates

## Cha rge Pu m p M ismatch

![](images/9ed74ef78c2f37b80f2220c41e649982e134c445b83d68a731df2cfbe4899a59.jpg)

Idea l locked cond ition, but CP m ismatch

![](images/05e562ded5f40897e45d54125c5bae9f58d1ff6b3f9c95f0614342ea017b93b5.jpg)

• P LL wi l l l oc k with stati c p h a se e rro r if there is a cha rge pu m p m ismatch

• Extra “ ri pp l e” on $\mathsf { V } _ { \mathsf { c t r l } }$

• Resu lts i n freq uency doma i n spu rs at the reference clock freq uency offset fro m th e ca rri e r

Actua l locked cond ition w/ CP m ismatch

![](images/1d25f91d824322fe0cc321d2b80e2977051c45459584e32685bb34644ebbddb0.jpg)

$$
I _ { U P } = I _ { C P } - \frac { \Delta I } { 2 }
$$

$$
I _ { D N } = I _ { C P } + \frac { \Delta I } { 2 }
$$

$$
I _ { U P } ( T _ { o s } ) = \Delta I ( T _ { r s t } )
$$

$$
T _ { o s } = \frac { \Delta I ( T _ { r s t } ) } { I _ { C P } - \frac { \Delta I } { 2 } }
$$

$$
\phi _ { o s } = 2 \pi \left( \frac { \Delta I } { I _ { C P } - \frac { \Delta I } { 2 } } \right) \left( \frac { T _ { r s t } } { T _ { r e f } } \right)
$$

## Cha rge Pu m p w/ I m proved Match i ng

![](images/12265eb4be92dce6aca1c2f48e862af52a9ce898801fc8c6c8b2eee6bf32c1ca.jpg)  
[You ng JSSC 1992 ]

• Pa ra l lel path keeps cu rrent sou rces a lways on

• Am pl ifier keeps cu rrent sou rce $\mathsf { V } _ { \mathsf { D } \mathsf { S } }$ voltages consta nt resu lti ng i n red uced tra nsient cu rrent m ismatch (cha rge sha ri ng)

## Dig ita l Lea kage Com pensation

• Cha rge pu m p off-state lea kage ca uses PLL to l oc k with stati c p h a se e rro r

• Com pensated by add itiona l d ig ita l ly-control led cha rge pu m p cu rrent pu lses

• TDC detects phase error between i n put reference clock a nd feed back clock

![](images/fc706231ccc487abd44c0d5f2ffdd846b1bcad7efd472f37aeb134ae52b146b1.jpg)

![](images/4890893e320d13699200e727a467739ebcd4b22a73065ce32016cf40f0263e0b.jpg)

![](images/b9d8a2162e386d26c076f2b2cd6a84e5ac02d4a7baf8abf9f6f0b678824cda9b.jpg)  
Two pulse digital leakage compensation for leakage from supply

## Cha rge Pu m p w/ Reversed Switches

## • Swa ppi ng switches red uces cha rge i njection

• MOS ca ps ( Md 1 -4) provide extra clock feedth roug h ca ncel lation

• H el per tra nsistors Mx a nd My q u i ckly tu rn -off cu rre nt sou rces

• Du m my bra nch hel ps to match PFD load i ng

• H el ps with cha rge i nj ectio n , but cha rg e s h a ri n g i s sti l l a n i ss u e

![](images/db40a1fd80579572a33b24913bac7cb0558a18adf2624d57d972009840f42acc.jpg)  
[Ing i no JSSC 200 1 ]

## Cha rge- Pu m p PLL Ci rcu its

• Phase Detector

• Cha rge- Pu m p

• Loo p Fi lte r

• VCO

• D ivi d e r

![](images/be9d6cbab3317346abd50991f63ed481dcecbd02a5d4c751a67ae023500474af.jpg)

## Cha rge Pu m p PLL Passive PI Loop Fi lter

![](images/fcc90cfbf004e9f25654eb38515075bfd4b51894fef876e4ab4ad0fc79590f22.jpg)

• Si m ple passive fi lter is most com mon ly u sed

• I nteg rates low-freq uency phase errors onto C 1 to set average freq uency

• Resistor ( proportiona l ga i n ) isolates phase correction from freq uency co rrectio n

• Pri ma ry ca pacitor C 1 affects PLL ba ndwidth

• Zero freq uency affects PLL sta bi l ity

• Resistor add s therma l noise wh ich is ba nd - pass fi ltered by PLL

## Loop Fi lter Tra nsfer Fu nction

• Neg lecti ng seconda ry ca pacitor, ${ \mathsf C } _ { 2 }$

$$
F ( s ) = \frac { V _ { c } \left( s \right) } { I _ { e } \left( s \right) } = \frac { R \left( s + \frac { 1 } { R C _ { 1 } } \right) } { s }
$$

![](images/f2aebf2477850f7c9d3f3674b0287689d0bf2bde8edf6579e9549102df03199c.jpg)

## Loop Fi lter Tra nsfer Fu nction

• With seconda ry ca pacitor, ${ \mathsf C } _ { 2 }$

$$
Z ( s ) = { \cfrac { { \cfrac { 1 } { C _ { 2 } } } ^ { \left( s + { \cfrac { 1 } { R C _ { 1 } } } \right) } } { s ^ { 2 } + { \cfrac { s { \cfrac { \left( C _ { 1 } + C _ { 2 } \right) } { R C _ { 1 } C _ { 2 } } } } { R C _ { 1 } C _ { 2 } } } } }
$$

![](images/316666529fe7cd26b3a5a32e084262b0bf5344896df33bda5e8527addc941c6e.jpg)

## Why have C2?

• Seconda ry ca pacitor smoothes control voltage ri pple

• Ca n ’t ma ke too big or loop wi l l go u nsta ble

$\mathsf C _ { 2 } < \mathsf C _ { 1 } / 1 0$ fo r sta b i l ity

• $\mathsf C _ { 2 } > \mathsf C _ { 1 } / 5 0$ fo r l ow j itte r

![](images/e2dad48e26cb1dc37ab6bbd3989e5d581e6598a3ab3174f440676b3630c43641.jpg)

## Loop Fi lter Ca pacitors

• To m i n i m ize a rea, we wou ld l i ke to use h ig hest density ca ps

• Th i n oxide MOS ca p gate lea kage ca n be a n issue

• S i m i l a r to a d d i n g a n o n - l i n ea r pa ra l l e l res i sto r to th e ca pa cito r

Lea kage is voltage a nd tem peratu re dependent

• Wi l l resu lt i n excess phase noise a nd spu rs

• Meta l ca ps or th ick oxide ca ps a re a better choice • Tra d e-off i s a rea

• Meta l ca p density ca n be < 1/ 1 0 th i n oxide ca ps

• Fi lter ca p freq uency response ca n be relatively low, as PLL loop ba ndwidths a re typica l ly 1 -50 M Hz

## Cha rge- Pu m p PLL Ci rcu its

• Phase Detector

• Cha rge- Pu m p

• Loo p Fi lte r

• VCO

• D ivi d e r

![](images/f6ca76960d66d099a2bf6091cfa1200c2bbf47551dbdd50bb0a885b5b0b3d47a.jpg)

## Voltage-Control led Osci l lator

$$
\mathbf { v } _ { \mathrm { c t r l } } ( \mathbf { t } ) \longrightarrow \boxed { \begin{array} { r l } \end{array} } \boxed { \begin{array} { r l } \end{array} } \boxed { \begin{array} { r l } \end{array} } \boxed { \begin{array} { r l } \end{array} }
$$

![](images/9aa4eca626fa45f8e41f923ddb6cf3e881dd8af8108ccd9b70109761f16639f4.jpg)

$$
\omega _ { o u t } ( t ) = \omega _ { 0 } + \Delta \omega _ { o u t } ( t ) = \omega _ { 0 } + K _ { V C O } v _ { c t r l } ( t )
$$

• Ti me-doma i n phase relationsh i p

$$
\begin{array} { c } { \displaystyle \phi _ { o u t } ( t ) = \int \Delta \omega _ { o u t } ( t ) d t = \int K _ { V C O } v _ { c t r l } ( t ) d t } \\ { \displaystyle K _ { V C O } \mathrm { u n i t s ~ a r e } \frac { \mathrm { r a d } } { { \bf s } \cdot { \bf V } } } \\ { \displaystyle \frac { 2 \pi \big ( { \bf { \mathrm { 1 } } } { \bf M } { \bf H } { \bf { z } } \big ) } { { \bf V } } = 2 \pi \times 1 0 ^ { 6 } \frac { \mathrm { r a d } } { { \bf s } \cdot { \bf V } } } \end{array} ,
$$

Laplace Domain Model

$$
v _ { \mathrm { c t r l } } ( \bf t ) \longrightarrow [ \begin{array} { l } { \underbrace { K _ { v c o } } _ { \mathbb { S } } } \\ { \rule { 0.25 ex } { 5 ex } } \end{array} ]  \phi _ { \mathrm { o u t } } ( \bf t )
$$

## Voltage-Control led Osci l lators (VCO)

## • Ri n g Osci l l ato r

Easy to i nteg rate

• Wide tu n i ng ra nge (5x)

H ig her phase noise

![](images/f19ae41b953ac10637cfaf1106c6e410eefd782d1e0eff68d169d02a6a9c4714.jpg)

## • LC Osci l l ato r

La rge a rea

Na rrow tu n i ng ra nge (20-30%)

Lower phase noise

![](images/0b4981f412e13461f4188cc9d3c18818753e8db6640da624f50459ef4056750b.jpg)

## Ba rkha u sen ’s Osci l lation Criteria

![](images/88eda4d8cb3b4b8e5207b6083c631461533c9ebc06c5a7f32fb2a138702c0e38.jpg)

Closed - loop tra nsfer fu nction : $\frac { H ( j \omega ) } { 1 - H ( j \omega ) }$

• Su sta i ned osci l lation occu rs if $H ( j \omega ) = 1$

• 2 co n d iti o n s :

• Ga i n = 1 at osci l lation freq uency $\mathfrak { O } _ { 0 }$

• Tota l phase sh ift a rou nd loop is $\boldsymbol { \mathsf { n 3 6 0 ^ { \circ } } }$ at osci l lation freq uency $\mathfrak { O } _ { 0 }$

## Ri ng Osci l lator Exa m ple

![](images/f7f1189236db06eca914aca2d40afac10db7f292198071908a6b329718e41f04.jpg)

$$
H ( s ) = - \frac { A _ { 0 } ^ { 4 } } { \left( 1 + \frac { s } { \omega _ { o } } \right) ^ { 4 } }
$$

Phase Condition: $\begin{array} { r } { \tan ^ { - 1 } ( \frac { \omega _ { o s c } } { \omega _ { o } } ) = 4 5 ^ { \circ }  \sqrt { \omega _ { o s c } = \omega _ { o } = \frac { 1 } { R C } } } \end{array}$

Gain Condition: $\begin{array} { r } { \frac { A _ { 0 } ^ { 4 } } { [ \sqrt { 1 + ( \frac { \omega _ { O S C } } { \omega _ { O } } ) ^ { 2 } } ] ^ { 4 } } = 1  A _ { 0 } = \sqrt { 2 } = g _ { m 1 } R } \end{array}$

## LC Osci l lator Exa m ple

![](images/5945682101b4f9aebb3a1477fefe21c30dcd50ac813df3f14358255b51efec61.jpg)

• Osci l lation phase sh ift cond ition satisfied at the freq uency when the LC (a nd R) ta n k load d isplays a pu rely rea l i m peda nce, i . e . $0 ^ { \circ }$ phase sh ift

LC tank impedance

$$
Z _ { e q } ( s ) = { \frac { R _ { s } + L _ { 1 } s } { 1 + L _ { 1 } C _ { 1 } s ^ { 2 } + R _ { s } C _ { 1 } s } }
$$

$$
\left| Z _ { e q } \left( s = j \omega \right) \right| ^ { 2 } = \frac { R _ { S } ^ { 2 } + L _ { 1 } ^ { 2 } \omega ^ { 2 } } { \left( 1 - L _ { 1 } C _ { 1 } \omega ^ { 2 } \right) ^ { 2 } + R _ { S } ^ { 2 } C _ { 1 } ^ { 2 } \omega ^ { 2 } }
$$

## LC Osci l lator Exa m ple

![](images/8e751c5d35c2faeacc133a18afb6e4a54464fbe49de680519bf6e7a24eb7d62e.jpg)

• Tra nsform i ng the series loss resi sto r of th e i n d u cto r to a n eq u iva lent pa ra l lel resista nce

![](images/49aab2c16cd00c41dbf81d0195c0a197d181d47c514cf812259b1c1bb1564df2.jpg)

$$
L _ { P } = L _ { 1 } \Biggl ( 1 + { \frac { R _ { S } ^ { 2 } } { L _ { 1 } ^ { 2 } \omega ^ { 2 } } } \Biggr ) , C _ { P } = C _ { 1 } , R _ { P } \approx { \frac { L _ { 1 } ^ { 2 } \omega ^ { 2 } } { R _ { s } } }
$$

![](images/36409ea83b0e55c9c00d005f074ebe9f7ad122a770016b2231b09a605e03b79b.jpg)

![](images/1780b4a1f7a8a00429eb219ccbaea45b7a672eab9342d2c90e511619d849d02b.jpg)

$$
\omega _ { 1 } = { \frac { 1 } { \sqrt { L _ { P } C _ { P } } } }
$$

[ Razavi ]

## LC Osci l lator Exa m ple

![](images/af98c31a83ba5fb7662f9bf2f991b4e14eec514a992a7804869eb24750edd9f4.jpg)

## Loop Gain

![](images/df8f8805cd6991823d0aec5804b0159fcf48303b7a9950365e93e89080ba5b28.jpg)

![](images/e34a537e32a1917072c1b6e96266d4dd22cc68c9a769cefcefeb3c7249ffc050.jpg)

• Phase cond ition satisfied at $\omega _ { 1 } = \frac { 1 } { \sqrt { L _ { P } C _ { P } } }$

$\blacktriangledown _ { \circ } \bar { \mathbf { \Psi } }$ • Ga i n cond ition satisfied when $\left( g _ { m } R _ { P } \right) ^ { 2 } \ge 1$

• Ca n a l so vi ew th i s ci rcu it a s a pa ra l l e l com bi nation of a ta n k with loss resista nce $2 \mathsf { R } _ { \mathsf { P } }$ a nd negative resista nce of $2 / 9 _ { \mathrm { m } }$

• Osci l lation is satisfied when

$$
{ \frac { 1 } { g _ { m } } } \leq R _ { P }
$$

## Su pply-Tu ned Ri ng Osci l lator

![](images/5b15a242cd829be1b94a5fb2dbeebf729688813138d05ef114598e2b1004364e.jpg)

$$
T _ { V C O } = 2 n T _ { D } \approx \frac { 2 n C _ { s t a g e } } { \beta \left( V _ { c } - V _ { t h } \right) }
$$

[Sid i ropou los VLSI 2000 ]

$$
K _ { _ { V C O } } = \frac { \hat { \sigma } f _ { _ { V C O } } } { \hat { \sigma } V _ { c } } = \frac { \beta } { 2 n C _ { s t a g e } }
$$

## Cu rrent-Sta rved Ri ng Osci l lator

![](images/bc2b8ea969f35f328b6940e94db0ae0a85fac9af3708597ae5868af41ff6ca04.jpg)  
Current - starved VcO.

## Ca pacitive-Tu ned Ri ng Osci l lator

![](images/2d92d93da61bfe3a67ce4fff5d7c0b3ad97c1839afcd98de13dd692359a31d37.jpg)

## Sym metric Load Ri ng Osci l lator

VCO Replica-Feedback Bias Generator

![](images/a4693030a7deaaefcf33e21a7c61d76b5ef7c857c245df77f1a289242c63870d.jpg)  
Buffer Stage

![](images/b8f209ddbe41d0c10b97a0a92928531492ead1e5c9e5ef1674d126879fa38bb4.jpg)  
[ Ma neatis JSSC 1 996 & 2003]

![](images/4675892c71098f2b80222d81339688c9bbc95f7e7ab61e8c151063353bb237cc.jpg)  
11-Stage Ring Oscillator

![](images/e04c7493561932192e35dccd010e7b2ed566a4644fa99969eec31ede249c76d5.jpg)

![](images/2f0676adcc67466c3d6d869000941b6fd73dbdf7b2a10df166fffaa23e0b5a6b.jpg)

![](images/6765f9acb3e887a22a9fc36a8e1deb66cf69615eb4135ee8029aa45525f561b6.jpg)

• Sym metric load provides freq uency tu n i ng at excel lent su pply noise rejection

• See Ma neatis pa pers for self- biased tech n iq ues to obta i n consta nt da m pi ng factor a nd loop ba ndwidth (% of ref cl k)

## LC Osci l l ato r

• A va ria ble ca pacitor (va ra cto r) i s ofte n u sed to adj ust osci l lation freq uency

• Tota l ca pacita nce i ncl udes both tu n i ng ca pacita nce a nd fixed ca pacita nces wh ich red uce the tu n i ng ra nge

$$
\omega _ { o s c } = \frac { 1 } { \sqrt { L _ { P } C _ { P } } } = \frac { 1 } { \sqrt { L _ { P } \big ( C _ { t u n e } + C _ { f u x e d } \big ) } }
$$

![](images/38e70a7b56fbd9dcffbd00e410c79ed3660fe74641c21432a9964ee5882b2304.jpg)

## Va ractors

• pn j u nction va ractor

Avoid forwa rd bias reg ion to prevent osci l lator non l i nea rity

![](images/59d286b2dca2b38943baa0928189877506f5975ac8e4bd22edb678b5ae5dc0cc.jpg)

• MOS va ractor

Psubstrate

![](images/36d98392f7a26e7ac76c5335db99fa6d4d0c38e2cdd3dbe11bcbbfb34b133b25.jpg)  
[ Perrott]

• Accu m u lation- mode devices have better Q tha n i nversion- mode

![](images/717e9464ed60a1103536570b8a2d9c81796ffe50e14f3ea1e283c136d09fe0f0.jpg)

![](images/0a0fa4d02e52d5381c97205e7f77b982517805ebb2640a79e4e93434d9bba752.jpg)  
[Razavi]

## Cha rge- Pu m p PLL Ci rcu its

• Phase Detector

• Cha rge- Pu m p

• Loo p Fi lte r

• VCO

• Divider

![](images/749242601386d1db6ce3ca593b08d991da2a9a12375a43d1dcf9d0cf65c7b3e1.jpg)

## Loop Divider

$$
\phi _ { \mathrm { o u t } } ( \mathrm { t } )  [ \begin{array} { l } { { \begin{array} { r } { 1 } \end{array} } } \\ { { \begin{array} { r } { N } \end{array} } } \end{array} ]  \phi _ { \mathrm { f b } } ( \mathrm { t } )
$$

$\phi _ { \mathrm { o u t } } ( \mathbf { t } )$

![](images/44d2856ff2120ccdb1cbc866770f794c01580049906d9a8c32e061bb8b465fd1.jpg)

• Ti me-doma i n model

$$
\omega _ { \mathcal { I } b } ( t ) = \frac { 1 } { N } \omega _ { o u t } ( t )
$$

$$
\phi _ { _ { f b } } ( t ) = \int \frac { 1 } { N } \omega _ { o u t } ( t ) \mathrm { d t } = \frac { 1 } { N } \phi _ { o u t } ( t )
$$

• Th e l oo p d ivi d e r i s d i mension - less i n the PLL l i nea r mod e l

## Basic Divide- by-2

![](images/9e8117259ecea1d61a275d9a331088d037c6abb0890dec0ac2203e3734e040e2.jpg)

• Divide- by-2 ca n be rea l ized by a fl i p-fl i p i n “ negative feed back”

• Divider shou ld operate correctly u p to the maxi m u m output clock freq uency of i nterest PLUS some ma rg i n

![](images/e9f0282728cd3934dae4f0b206aae37535528d41f100fa4f87620fde6f9be6ca.jpg)

## Divide- by-2 with TSPC FF

## True Si ng le Phase Clock Fl i p- Flop

![](images/3c297c8acb7cb648398bce2cc91a1cb26b9e897b4ff34285d8ecd75efabc1450.jpg)

• Adva ntages

Divider Eq u iva lent Ci rcu it Note : output i nverter not i n left schematic

![](images/6d13f5909af27b2d7e0280c2d04f018108b9e918a0c8ba51604e0217dd86e64f.jpg)

![](images/74ea36e1b48e912a23868bb46d8b30671cb91164e261ba72034e6440774a29bd.jpg)

Reasona bly fast, com pact size, a nd no static power

Req u i res on ly one phase of the clock

## • Disadva ntages

Sig na l needs to propagate th roug h th ree gates per i n put cycle

Need fu l l swi ng CMOS i n puts

• Dyna m ic fl i p-flop ca n fa i l at low freq uency (test mode) d ue to lea kage, as va rious nodes a re floati ng d u ri ng d ifferent CLK phases & output states

• Ex : Q\_ba r is floati ng d u ri ng when CLK is low

## Divide- by-2 with CM L FF

![](images/372ba83a55ec666c646d671c7bb3ea93b1da984f1fd3eae3d35f5b0a2591b0bb.jpg)

• Adva ntages

Sig na l on ly propagates th roug h two CM L gates per i n put cycle

Accepts CM L i n put levels

• Disadva ntages

La rger size a nd d issi pates static power

Req u i res d iffe re nti a l i n p ut

N eed ta i l cu rrent biasi ng

• Add itiona l speed u p ( > 50%) ca n be ach ieved with sh u nt pea ki ng i nd uctors

## Bi n a ry D ivi d e rs : Asynch ronous vs Synch ronous

Asynchronous Divider  
![](images/24e1ab49c662b3c953f29f449067d32b323f80db6e320d41b00cdef8d8b6917c.jpg)

## • Adva ntages

• Each stage ru ns at lower freq uency, resu lti ng i n red uced power

• Red uced h ig h freq uency clock load i ng

## • Disadva ntage

J itte r a ccu m u l ati o n

## Synchronous Divider

![](images/7ae4dced17562d2fb5d127910e390dd8e549a69f2a2475f5fe1a3f5b14a053f1.jpg)

## • Adva ntage

Red u ced j itter

## • Disadva ntage

• Al l fl i p-fl o ps wo rk at m axi m u m freq uency, resu lti ng i n h ig h power

• La rge load i ng on h ig h freq uency clock

## J itter i n Asynch ronous vs Synch ronous Dividers

![](images/4ea78cac1ca82c7d6d074bbf94d75450b94f1a8f40aedb273d287dd4b33c01e4.jpg)

Synchronous

![](images/93bc99988808e4eb8b959d16644729a3380e8e0ae094c1187ab19d4c55c33a97.jpg)

• J itter accu m u lates with the clock-to-Q delays th roug h th e d ivi d e r

• Extra d ivider delay ca n a lso deg rade PLL phase ma rg i n

• Divider output is “sa m pl ed ” with h ig h freq uency clock

• J itte r o n d ivi d e r c l ock i s s i m i l a r to VCO o utp ut

• M i n i ma l d ivider delay

## Dua l Mod u l us Presca lers

![](images/3c03725cb93343c0f0a313c87335b9b47cb1862735afd61de2909db123491e96.jpg)

![](images/a33c5b2bda68c23fc187caa8e503a51456a9644e218ccd2c67cc38b19633cc40.jpg)  
• Fo r / 1 5, fi rst p resca l e r ci rcu it d ivid es by 3 o n ce a n d 4 th ree ti m es d u ri ng the 1 5 cycles

## I njection- Locked Freq uency Dividers

## LC-osci l lator type (/ 2)

![](images/0ab85a4b43ec1f99e30f25818aefa10eab0ecba1587b023602d85f5d9d1dc6b7.jpg)  
[Verma JSSC 2003, Rategh JSSC 1999]

Ri ng -osci l lator type (/ 3)

![](images/2e77d29cbd4d93b5d0f8f51042c3d148249653fe85df72c40331a6a9408cf783.jpg)  
[ Lo CICC 2009 ]

• Su perha rmon ic i njection - locked osci l lators (I LOs) ca n rea l ize freq uency d ividers

• Faster a nd lower power tha n fl i p-flop based d ividers

I njection locki ng ra nge ca n be l i m ited