---
layout: post
title:      "ECEN 720 : H ig h-Speed Li n ks Ci rcu its a nd Systems Spri ng 2023"
date:       2026-04-18 16:38:11
author:     "Bert"
tags:
  - CDR
  - Lecture
  - Mineru
---
Lectu re 1 2 : CD Rs

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/6a69fe8cb048a4c2b65e07f06eafc1a099c489027c71d23952c52c7ce5dc3522.jpg)

Sa m Pa lermo Ana log & M ixed -Sig na l Center Texas A&M U n iversity

## An nou ncements

• Project Prel i m i na ry Report d ue Apr 1 8

• Project Fi na l Report d ue May 2

## Agenda

• CDR overview

• CDR phase detectors

• Si ng le- loop a na log PLL- based CDR

• Dua l - loop CDRs

• Phase i nterpolators

• C D R j itte r p ro pe rti es

## Em bedded Clock I/O Ci rcu its

## Multi-Channel Serial Link System

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/d81f133cd5c775d4ecd84591c7471b5dfa2dec0468ad0e7b47df4483f4585b1a.jpg)

## • TX PLL

## • TX Cl ock D i stri butio n

## CDR

• Per-cha n nel PLL- based

• Dua l - loop w/ G loba l PLL &

• Loca l D LL/PI

• Loca l Phase- Rotator PLLs

• G loba l PLL req u i res RX cl ock d i stri b utio n to i nd ivid ua l cha n nels

## Clock a nd Data Recovery

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/09626394f51bfd6e458647f31aa825df1413435847d9eca6334c9a7fa227d4f4.jpg)

• A clock a nd data recovery system (CD R) prod uces the clocks to sa m ple i ncom i ng data

• The clock(s) m ust have a n effective freq uency eq ua l to the i ncom i ng d ata rate

1 0G H z for 1 0G b/s data rate

O R, m u lti ple clocks spaced at 1 00 ps

Add itiona l clocks may be used for phase detection

• Sa m pl i ng clocks shou ld have sufficient ti m i ng ma rg i n to ach ieve the d es i red b it-e rro r- rate ( B E R)

• C D R s h o u l d exh i b it s m a l l effective j itte r

## Em bedded Clocki ng (CDR)

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/f1935cf1b7d8076d103640693aef0a89b7142896e39ac3cd04f65b0b1ee6eb2b.jpg)

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/9409e26a8d5e558e6739791c6fd9e129f9a37fc9eacaa71ec67b70849de72245.jpg)

• Clock freq uency a nd opti m u m phase position a re extracted from i ncom i ng data

• Phase detection conti n uously ru n n i ng

• J itter tracki ng l i m ited by CD R ba ndwidth

• With tech nology sca l i ng we ca n ma ke CDRs with h ig her ba ndwidths a nd the j itter tracki ng adva ntages of sou rce synch ronous systems is d i m i n ished

• Possi ble CDR i m plementations

• Sta nd -a lone PLL

• “ Dua l - loop” a rch itectu re with a PLL or D LL a nd phase i nterpolators ( PI)

• Phase- rotator PLL

## Agenda

• CDR overview

• CDR phase detectors

• Si ng le- loop a na log PLL- based CDR

• Dua l - loop CDRs

• Phase i nterpolators

• C D R j itte r p ro pe rti es

## CDR Phase Detectors

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/4a886e5f1ea2947459ff1451701b08d556b4543aa7beecd0e87d2f2f516ad077.jpg)

• A pri ma ry d ifference between CDRs a nd PLLs is that the i ncom i ng data sig na l is not period ic l i ke the i ncom i ng reference clock of a PLL

• A CDR phase detector m ust operate properly with m issi ng tra nsition edges i n the i n put data seq uence

## CDR Phase Detectors

• CDR phase detectors com pa re the phase between the i n put data a nd the recovered clock sa m pl i ng th is data a nd provides i nformation to adj ust the sa m pl i ng clocks’ phase

• Phase detectors ca n be l i nea r or non - l i nea r

• Li nea r phase detectors provide both sig n a nd mag n itude i nformation rega rd i ng the sa m pl i ng phase error • Hogge

• Non- l i nea r phase detectors provide on ly sig n i nformation rega rd i ng the sa m pl i ng phase error

• Alexa nder or 2x-Oversa m pled or Ba ng - Ba ng

• Oversa m pl i ng ( > 2)

• Ba ud - Rate

## Hogge Phase Detector

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/00331ac52217fcbb14346ede682e61504376e22be76800b3e6a9a96e8bc749ad.jpg)

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/03c13a84812fb64a63f21ba8202ecf146c104b7e49823fc7453a578f8188d05e.jpg)

• Li nea r phase detector

• With a data tra nsition a nd assu m i ng a fu l l - rate clock

• The late sig na l prod uces a sig na l whose pu l se width is proportiona l to the phase d ifference between the i ncom i ng data a nd the sa m pl i ng clock

• A Tb/2 reference sig na l is prod uced with a Tb/2 delay

• If th e cl ock i s sa m p l i n g ea rly, th e l ate sig na l wi l l be sho rte r tha n Tb/2 a nd vice-versa

## Hogge Phase Detector

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/dbcd9c38cd886f804679d9009a9acac5a58ed7f202ce005c095715fe82aa8cf5.jpg)

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/7c086345765fbb1dace4101b3bba52db33cc9e5011b0d80e35aedea2a02d7ea9.jpg)

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/10f9f185fea3ed6414a94023102f605c5887c41ed6856ae42f1c5424961e6b7a.jpg)

• Fo r p h a se tra n sfe r 0 ra d i s w . r . t opti ma l Tb/2 () spaci ng between sa m pl i ng clock a nd data

• $\Phi _ { \mathrm { e } } = \Phi _ { \mathrm { i n } } - \Phi _ { \mathrm { c l k } } - \pi$

• TD is the tra nsition density – no tra nsitions no i nformation

• A va l ue of 0 . 5 ca n be assu med for ra ndom data

## PLL- Based CDR with a Hogge PD

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/e710d10e5d38b334c32be219a5e5c00f210fd73c0ba0ab1c667ba330e6f5d594.jpg)

• XO R outputs ca n d i rectly d rive the cha rge pu m p

• Need a relatively h ig h-speed cha rge pu m p

## Alexa nder (2x-Oversa m pled) Phase Detector

• Most com mon ly used CDR phase detector

• Non- l i nea r ( Bi na ry) “ Ba ng - Ba ng ” PD • On ly provides sig n i nformation of phase e rro r ( n ot m a g n itu d e)

• Phase detector uses 2 data sa m ples a nd one “edge” sa m ple

• Data tra nsition necessa ry

$$
D _ { n } \oplus D _ { n + 1 }
$$

• If “edge” sa m ple is sa me as second b it (o r d iffe re nt fro m fi rst) , th e n th e clock is sa m pl i ng “ late”

$$
E _ { n } \oplus D _ { n }
$$

• If “ed g e” sa m p l e i s sa m e a s fi rst b it (o r d iffe re nt fro m seco n d ) , th e n th e clock is sa m pl i ng “ea rly”

$$
E _ { n } \oplus D _ { n + 1 }
$$

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/d2448eb6c8b4c8cf711ed0c92cafb97a3df57403c36535d241893c1cbdd8fdc4.jpg)

## Alexa nder Phase Detector Cha racteristic ( N o N o i se)

( Late – Ea rly)

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/a179c476f2c870a1169155b0c0a004084c48fa6f92c483eab5085cc53b13c9b2.jpg)

• Phase detector on ly outputs phase error sig n i nformation i n the form of a late O R ea rly pu lse whose width doesn ’t va ry

Phase detector ga i n is idea l ly i nfi n ite at zero phase error

• Fi n ite g a i n wi l l be p rese nt with n o i se, c l oc k j itte r, sa m p l e r m eta sta b i l ity, I SI

## Alexa nder Phase Detector Cha racteristic (With N o i se)

• Tota l tra nsfer cha racteristic is the convol ution of the idea l PD tra nsfer cha racteristic a nd the noise PDF

• N oise l i nea rizes the phase detector over a phase reg ion correspond i ng to the pea k-to- pea k j itte r

$$
K _ { _ { P D } } \approx \frac { 2 } { J _ { _ { P P } } } ( T D )
$$

• TD i s th e tra n siti o n d e n sity – no tra n sitio n s, no i nfo rmatio n

• A va l ue of 0 . 5 ca n be assu med for ra ndom data

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/a64d858695de3de96f893057059d83589bc68da9529780e273ae9f620e368fe0.jpg)

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/ca804fe7b381edd72d5778854b382b272553ea3f9be1327aa69aa9b1a3d0db74.jpg)

## M uel ler- M u l ler Ba ud - Rate Phase Detector

• Ba ud - rate phase detector on ly req u i res one sa m ple cl ock pe r sym bo l ( b it)

• M uel ler- M u l ler phase detector com mon ly used

• Attem pti ng to eq ua l ize the a m pl itude of sa m ples ta ken before a nd after a pu lse

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/67ab651ea4ab2ab2633177ae1067594f168707695536355392e0b45f47f1e068.jpg)

Locked Condition: $h ( \tau _ { k } { - } T _ { b } ) { = } h ( \tau _ { k } { + } T _ { b } )$ Early Clock: $h ( \tau _ { k } { - } T _ { b } ) { < } h ( \tau _ { k } { + } T _ { b } )$ Late Clock: $h ( \tau _ { k } { - } T _ { b } ) > h ( \tau _ { k } { + } T _ { b } )$

## M uel ler- M u l ler Ba ud - Rate Phase Detector

MM-PD is measuring the effective

$$
h _ { 1 } - h _ { - 1 }
$$

which can be computed by

$$
E [ y _ { k } \cdot d _ { k - 1 } ] - E [ y _ { k } \cdot d _ { k + 1 } ]
$$

• If th i s i s pos itive, th e n the effective post-cu rsor I SI i s too h i g h a n d we a re sa m pl i ng too ea rly

• If th i s i s n eg ative, th e n th e effective p re-cu rso r ISI i s too h i g h a n d we a re sa m pl i ng too late

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/b69c4932bc980bbf714866cb39c6b17d4ceebe28b3fa2dfe7c03f577587a9341.jpg)

Locked Condition: $h ( \tau _ { k } { - } T _ { b } ) { = } h ( \tau _ { k } { + } T _ { b } )$ Early Clock: $h ( \tau _ { k } { - } T _ { b } ) { < } h ( \tau _ { k } { + } T _ { b } )$ Late Clock: $h ( \tau _ { k } { - } T _ { b } ) > h ( \tau _ { k } { + } T _ { b } )$

## M uel ler- M u l ler Ba ud - Rate Phase Detector

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/45e17267d31dfd745afbf26e453e6c76fdbd1c6723740350316cf1b71b93b438.jpg)  
[Spag na ISSCC 20 10]

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/ac53994c82720cbf07366bf02932b4354f30742af32b783a90c0baee3acbbcfb.jpg)

Com pa ri ng the cu rrent sa m ple versus the desi red reference l evel $( \mathsf { e } _ { \mathsf { n } } )$ a nd correlati ng that with the a ppropriate data sa m ple $( { \mathsf { d } } _ { \mathsf { n } } )$ g ives pre/post-cu rsor i nformation

• Th is req u i res add itiona l error sa m plers $\boldsymbol { \mathsf { w } } /$ | VRE F | th reshold s

• $\mathsf { e } _ { \mathsf { n } }$ g ives ${ \sf d } _ { { \sf n } - 1 }$ post-cu rsor $( \mathsf { h } _ { 1 } )$ i nfo rm ati o n

• $\Theta _ { \mathsf { n } - 1 }$ g ive ${ \sf d } _ { \sf n }$ pre-cu rsor $( \mathsf { h } _ { - 1 } )$ i nformation

## M uel ler- M u l ler Ba ud - Rate Phase Detector

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/26b12f9534c086079560c24ba1e3d12752bf0ba0c3afb96c4b779247c7a6b547.jpg)

<table><tr><td rowspan=1 colspan=1>dj</td><td rowspan=1 colspan=1> ${ \underline { { \mathbf { d } } } } _ { \mathbf { j } \cdot 1 }$ </td><td rowspan=1 colspan=1>ej</td><td rowspan=1 colspan=1> $\underline { { \pmb { \mathrm { e } } _ { \mathrm { j } - 1 } } }$ </td><td rowspan=1 colspan=1> $\underline { { \boldsymbol { \Phi } _ { \mathsf { e r r } _ { \mathrm { i } } } } }$ </td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1>LATE</td></tr><tr><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1>LATE</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>EARLY</td></tr><tr><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>-1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>EARLY</td></tr><tr><td rowspan=1 colspan=4>All other cases</td><td rowspan=1 colspan=1>HOLD</td></tr></table>

[Spag na ISSCC 20 10]  
![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/584b936491f04e7ef7a58a87e4caebc508a24c1965a471136ae95a6fba4b892d.jpg)

• Si m p l ified M M - PD on ly considers tra nsition patterns

If consecutive error sa m ples a re d iffe re nt, p h a se e rro r pola rity is g iven by ej

## Agenda

• CDR overview

• CDR phase detectors

• Si ng le- loop a na log PLL- based CDR

• Dua l - loop CDRs

• Phase i nterpolators

• C D R j itte r p ro pe rti es

## Ana log PLL- based CDR

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/dc2eb5c283d56e850de65ceb512c0951b691ccbe6b7aa2deefa0d0dce6a94aed.jpg)

$$
\frac { \phi _ { o u t } } { \phi _ { i n } } = \frac { s \cdot K _ { P } \cdot K _ { P D } \cdot K _ { V C O } + K _ { i } \cdot K _ { P D } \cdot K _ { V C O } } { s ^ { 2 } + s \cdot K _ { P } \cdot K _ { P D } \cdot K _ { V C O } + K _ { i } \cdot K _ { P D } \cdot K _ { V C O } }
$$

$$
K _ { \scriptscriptstyle P } = I _ { c } \cdot R \qquad K _ { \scriptscriptstyle i } = \frac { I _ { c } } { C } \qquad \omega _ { \scriptscriptstyle n } = \sqrt { K _ { \scriptscriptstyle i } \cdot K _ { \scriptscriptstyle P D } \cdot K _ { \scriptscriptstyle V C O } } \quad \zeta = \frac { K _ { \scriptscriptstyle P } } { K _ { \scriptscriptstyle i } } \cdot \frac { \omega _ { \scriptscriptstyle n } } { 2 }
$$

## Ana log PLL- based CDR

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/00bfecc2eb2bb97ebde2d9e486fa9264cb4e11943f6eabb0ca20e6e5d6e9c1ed.jpg)

• CDR “ ba ndwidth ” wi l l va ry with i n put phase va riation a m pl itude with a non - l i nea r phase detector

• Fi na l performa nce verification shou ld be done with a ti me-doma i n non- l i nea r model

## 56G b/s PAM4 Ana log PLL-based CDR

• Q u a rte r- rate a rch itectu re

• 3 data sa m plers for PAM4 detection

• 1 edge sa m pler for CD R a nd DFE ada ptation

• 1 e rro r sa m p l e r fo r th res h o l d ada ptation

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/9e148407a5ee719829ce69fbe589b99b94d415f8acc4b87f067f2e4f598501b4.jpg)  
[ Roshan-Zamir JSSC 20 19]

## 56G b/s PAM4 Ana log PLL-based CDR

• PLL- based CDR to red uce power consu m ption

• Ba ng - ba ng phase detector works on sym metric PAM4 tra n s iti o n s to m i n i m ize detection e rro rs

• Pa ra l l e l ch a rg e pu m ps m i n i m ize log ic a nd loop delay

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/b00c763df17a2d2c7ae23d41f4108d4d9936e8272a3fd905b9e7fac37b7eeca9.jpg)

[ Roshan-Zamir JSSC 20 19]

## 56G b/s PAM4 Ana log PLL-based CDR

• LC-VCO w/ add itiona l sou rce LC fi lte r i m p roves phase noise

• 8- phase q ua rter-rate cl ock

• CM L d ivid e r

• 2X oversa m pl i ng clock

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/67f7fccaf77e172599adab4b2b2eb000e8d82fb8f455b1bb91fd327e99801d34.jpg)

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/bc9808ac0ce22c46c57a939fe2acbeb104c77b5b522d6e936adcea51da5997cc.jpg)

## [ Roshan-Zamir JSSC 20 19]

Channel 2.

## Agenda

• CDR overview

• CDR phase detectors

• Si ng le- loop a na log PLL- based CDR

Dua l - loop CDRs

• Phase i nterpolators

• C D R j itte r p ro pe rti es

## Si ng le- Loop CDR Issues

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/61295daf9321afbb15cae8c47d5cf2e7f71a9d3d8b00febad3c535af7e4140a0.jpg)

• Phase detectors have l i m ited freq uency acq u isition ra nge

Resu lts i n l o n g l ock ti m es o r n ot l ocki n g at a l l

Ca n potentia l ly lock to ha rmon ics of correct clock freq uency

• VCO freq uency ra nge va riation with process, voltage, a nd tem peratu re ca n exceed PLL lock ra nge if on ly a phase detector is em ployed

## Phase I nterpolator ( PI) Based CDR

• Freq uency synthesis loop ca n be a g loba l PLL

• Ca n be d iffi cu lt to d istri bute m u lti ple phases long d ista nce

• Need to preserve phase spaci ng

• Clock d istri bution power i ncreases with phase n u m ber

• If CDR needs more tha n 4 phases consider loca l phase generation

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/ba73668ae8e960b025498c3e9e7b14aa71e8c8d2b54190da99447b1f2a66ff62.jpg)

## DLL Loca l Phase Generation

• O n ly d iffe re nti a l c l ock i s d istri buted from g loba l PLL

• Delay- Locked Loop ( DLL) loca l ly generates the m u lti ple clock phases for the phase i nterpolators

• DLL ca n be per-cha n nel or sha red by a sma l l n u m ber (4)

• Sa me a rch itectu re ca n be used i n a forwa rded -clock system

• Replace freq uency synthesis PLL with forwa rded -clock sig na l s

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/725dd36b5e6026f75f1799144bad096792d08b7e76e5d7fccae15d8ac16d5010.jpg)

## Phase Rotator PLL

• Phase i nterpolators ca n be expensive i n terms of power a nd a rea

• Phase rotator PLL places one i nterpolator i n PLL feed back to adj ust a l l VCO output phases si m u lta neously

• Now freq uency synthesis a nd phase recovery loops a re cou pled

• Need PLL ba ndwidth g reater tha n phase loop

• U sefu l i n fi lte ri n g VCO n o i se

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/73916e4b6090277082e1dbbb19fff8f74b087471e4d07e5bffdb78d15ac51bae.jpg)

## Agenda

• CDR overview

• CDR phase detectors

• Si ng le- loop a na log PLL- based CDR

• Dua l - loop CDRs

• Phase i nterpolators

• C D R j itte r p ro pe rti es

## Phase I nterpolators

• Phase i nterpolators rea l ize d ig ita l -to- phase conversion ( D PC)

• Prod uce a n output clock that a weig hted su m of two i n put clock phases

Com mon ci rcu it structu res

• Ta i l cu rrent su m mation i nte rpo l ati o n

Voltage- mode i nterpolation

• I nterpolator code ma ppi ng tech n iq ues

• Si n usoida l

• Li n ea r

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/fb4b5e58baba1b9c2c346c8a79b366ff063b74d6312e319152b688a34741d0aa.jpg)

## Si n usoida l Phase I nterpolation

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/4acc2b1116bcf81f852c9cf30eec0560ca9a357769d24088740b1e745d671bdb.jpg)

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/dd2388e05e609eb1bbafd0e4142f9291d8ab0a22dd36a96a3349ab0a790b67a8.jpg)

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/31fbe96bb7a8f381bed049c001ac55289da209fa7edf357cabf854fc7aaad26d.jpg)

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/db72d602b26d1427139220f1b613865d40180c03dc5570a05e40256ed684c686.jpg)

$$
X _ { Q } = A \sin ( \omega t - \pi / 2 ) = - A \cos ( \omega t )
$$

• Arbitra ry phase sh ift ca n be generated with l i nea r su m mation of I/Q clock sig na l

$$
\begin{array} { l } { { Y = A \sin ( \omega t - \phi ) } } \\ { { \ } } \\ { { = A \cos ( \phi ) { \sin ( \omega t ) } - A \sin ( \phi ) { \cos ( \omega t ) } \quad \left( 0 \leq \phi \leq \displaystyle \frac { \pi } { 2 } \right) } } \\ { { \ } } \\ { { = { \cos ( \phi ) } { X _ { I } } + { \sin ( \phi ) } { X _ { Q } } = a _ { 1 } { X _ { I } } + a _ { 2 } { X _ { Q } } } } \end{array}
$$

$$
Y = A \sin ( \omega t - \phi ) = a _ { 1 } X _ { 1 } + a _ { 2 } X _ { Q }
$$

where $a _ { 1 } = \cos ( \phi )$ and $a _ { 2 } = \sin ( \phi )$

$$
a _ { 1 } ^ { 2 } + a _ { 2 } ^ { 2 } = 1
$$

## Si n usoida l vs Li nea r Phase I nterpolation

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/8281d4ffa25c0504cba05632f06ceb32244d8b027f38b940b3c9bdec0648d4cf.jpg)

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/1c56dc1ddf426fc1cbdf6d16bc34e348854335f9161db0f4e54f08edc9e8bf11.jpg)

• It ca n be d iffi cu lt to g e n e rate a ci rcu it th at i m p l e m e nts si n usoida l weig hti ng

$$
a _ { 1 } ^ { 2 } + a _ { 2 } ^ { 2 } = 1
$$

• I n p ra cti ce, a l i n ea r we i g hti n g is often u sed

$$
a _ { 1 } + a _ { 2 } = 1
$$

Sinusoidal vs Linear Interpolation Weighting

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/5163ddfa306760824f3438ff3423e4cef61474513e90104e7b0b5727346c5ff7.jpg)

## Phase I nterpolator Model

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/64e383ec88e371b9c9847fc60e180555671bbf8fcf52832295c4c39159da5b4b.jpg)

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/7c7f38f7df93705d051afed504d290ecce62a83996f2dcfa5faddf0f39db8f59.jpg)

• I nte rpo l ati o n l i n ea rity i s a fu n cti o n of the phase spaci ng, $\Delta \ t ,$ to output ti me consta nt, ${ \mathsf { R C } } ,$ rati o

• I m po rta nt th at i nte rpo l ato r o utp ut ti me consta nt is not too sma l l (fa st) fo r p h a se m ixi n g q u a l ity

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/f7520f8cbc6ca42fc4235978e7d93c9691762e9bec7f2e076014ce095816bc44.jpg)

w/ idea l step i n puts (worst case)  
![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/71a5da3a6bb28110847a8d24d2c34f14a4b73598a3be0595fcc18d7a06d38134.jpg)

## Phase I nterpolator Model

w/ idea l step i n puts

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/bfa464a0c5a4b57cd6dfc3a0e7df3eb049601e8a08380275618f03e3cfccc349.jpg)  
w/ idea l step i n puts :

w/ fi n ite i n put tra nsition ti me  
![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/17d8ce35b6c000bb2b7f6dba91f2d131c6f3ad63071082221db39cd64d016b07.jpg)

Spice si m u lation  
![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/59926a6b5fdfd30024f0cf45409ee58d6d13d407db233275fd6d08c32596e8db.jpg)

$$
\begin{array} { r l } & { V _ { o } ( t ) = { V _ { c c } } + R \cdot I \cdot \left[ \left( 1 - \alpha \right) \cdot u ( t ) \cdot \left( { e ^ { - \frac { t } { R C } } - 1 } \right) + \alpha \cdot u ( t - \Delta t ) \cdot \left( { e ^ { - \frac { t - \Delta t } { R C } } - 1 } \right) \right] } \end{array}
$$

w/ fi n ite i n put tra nsition ti me :

$$
\begin{array} { l } { { { \bf \Delta } ^ { \prime } } _ { v _ { o } } ( t ) ~ = ~ V _ { c c } + ( 1 - \alpha ) \cdot \frac { { \bf \Delta } _ { m a x } \cdot t } { \Delta t } \cdot R \cdot \alpha \cdot \left[ u ( t ) - u ( t - \Delta t ) \right] \cdot \left( e ^ { - \frac { t } { R C } } - 1 \right) + \alpha E _ { \mathrm { ~ m a x } } \cdot t } \end{array}
$$

$$
\alpha \cdot \frac { I _ { m a x } \cdot t } { \tau _ { r } } \cdot R \cdot \left[ u ( t - \Delta t ) - u ( t - 3 \Delta t ) \right] \cdot \left( e ^ { - \frac { t - \Delta t } { R C } } - 1 \right) .
$$

For more deta i ls see D. Wei n lader’s Sta nford Ph D thesis

## Ta i l -Cu rrent Su m mation PI

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/793622c0f822ff2d03ec3555a885e2dbcddad489364896ef11055b3985b7abf1.jpg)

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/84d72fa5efcc4f65cf47c818d7edc53541afca883d67bad5cda0e8a79d8eaf26.jpg)

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/7cda476344903ac121e42cf5b2f832d792a1e2180ab0c9e339de15943e8c7f6c.jpg)

• Co ntro l of I/Q po l a rity a l l ows fo r fu l l 3 60  p h a se rotati o n with phase step determ i ned by resol ution of weig hti ng DAC

• For l i nea rity over a wide freq uency ra nge, i m porta nt to co ntro l eith e r i n p ut o r o utp ut ti m e co n sta nt (sl ew rate)

## Voltage- Mode Su m mation PI

## [Joshi VLSI Sym p 2009]

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/214a4b0706de2d4630703d5cf3c31a787b87a251a69baef7a49d2fd8fe67486c.jpg)

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/eb8d5be40f690b10d37f0df774f9964e4c05f2a2bc0af297a54810a7aaf4a9b3.jpg)

• For l i nea rity over a wide freq uency ra nge, i m porta nt to co ntro l eith e r i n p ut o r o utp ut ti m e co n sta nt (sl ew rate)

## Delay- Locked Loop ( DLL)

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/5a6d0c7702a507ece9fbdbf79c97b548826ef4ae3e62ec8506042387e7cdf8ec.jpg)

• DLLs lock delay of a voltage-control led delay l i ne (VCDL)

• Typica l ly lock the delay to 1 or ½ i n put clock cycles If locki ng to ½ clock cycle the D LL is sensitive to clock d uty cycle

• DLL does not self-generate the output clock, on ly delays the i n put clock

## Voltage-Control led Delay Li ne

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/ab98596ec8d70abe26cb8a65a8c1aa22bf166aae05d39cbd677ffe7b17b35c30.jpg)  
[Sid i ropou los]

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/ba8ca3537a24ebe58d33c69aff5174e910ffa3b3091adb42f1ecbfbd5b2031f3.jpg)

## DLL Delay Tra nsfer Fu nction

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/bb27474d15bf44a9097299f5e0c8443d3bc75614ad94e6447abd820688da196c.jpg)

$$
\begin{array} { c } { { D _ { O } ( s ) = ( D _ { I } ( s ) - D _ { O } ( s ) ) \cdot F _ { \mathrm { R E F } } \cdot \frac { I _ { C H } } { s C _ { 1 } } \cdot K _ { D L } } } \\ { { \displaystyle \frac { D _ { O } ( s ) } { D _ { I } ( s ) } = \frac { 1 } { 1 + s / \omega _ { N } } } } \\ { { \omega _ { N } = I _ { C H } \cdot K _ { D L } \cdot F _ { \mathrm { R E F } } \cdot \frac { 1 } { C _ { 1 } } } } \end{array}
$$

• Fi rst-order loop as delay l i ne doesn ’t i ntrod uce a ( low-freq uency) pole

• The delay between reference a nd feed back sig na l is low- pass fi ltered

• U ncond itiona l ly sta ble as long as conti n uous-ti me a pproxi mation holds, i . e . $\mathrm { { c o } _ { \mathrm { { n } } } { < } \mathrm { { c o } _ { \mathrm { { r e f } } } / 1 0 } }$

## Agenda

• CDR overview

• CDR phase detectors

• Si ng le- loop a na log PLL- based CDR

• Dua l - loop CDRs

• Phase i nterpolators

• C D R j itte r p ro pe rti es

• J itte r tra n sfe r

• J itte r g e n e rati o n

• J itte r to l e ra n ce

## C D R J itte r M od e l

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/5d293c3149cd5e8e9746915b20b057ea0e92e7db0606c65b25756afdfcfef8ef.jpg)

$$
\frac { \phi _ { o u t } } { \phi _ { i n } } = \frac { s \cdot K _ { P } \cdot K _ { P D } \cdot K _ { V C O } + K _ { i } \cdot K _ { P D } \cdot K _ { V C O } } { s ^ { 2 } + s \cdot K _ { P } \cdot K _ { P D } \cdot K _ { V C O } + K _ { i } \cdot K _ { P D } \cdot K _ { V C O } }
$$

$$
K _ { \scriptscriptstyle P } = I _ { c } \cdot R \qquad K _ { \scriptscriptstyle i } = \frac { I _ { c } } { C } \qquad \omega _ { \scriptscriptstyle n } = \sqrt { K _ { \scriptscriptstyle i } \cdot K _ { \scriptscriptstyle P D } \cdot K _ { \scriptscriptstyle V C O } } \quad \zeta = \frac { K _ { \scriptscriptstyle P } } { K _ { \scriptscriptstyle i } } \cdot \frac { \omega _ { \scriptscriptstyle n } } { 2 }
$$

## J itte r Tra n sfe r

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/d0d6eef12eb9bd4e838a4c9762dd00f0e8c91225a579044b1474a2a5dc8d19b5.jpg)

• J itte r tra n sfe r i s h ow m u c h i n p ut j itte r “tra n sfe rs” to th e o utp ut

• If the PLL has a ny pea ki ng i n the phase tra nsfer fu nction , th is j itter ca n actua l ly be a m pl ified

$$
\frac { \phi _ { o u t } } { \phi _ { i n } } = \frac { s \cdot K _ { P } \cdot K _ { P D } \cdot K _ { V C O } + K _ { i } \cdot K _ { P D } \cdot K _ { V C O } } { s ^ { 2 } + s \cdot K _ { P } \cdot K _ { P D } \cdot K _ { V C O } + K _ { i } \cdot K _ { P D } \cdot K _ { V C O } }
$$

## J itter Tra nsfer M easu rement

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/5dba3f6a69d1970a73545739170180f21c1a6196295fc68a760caf7bd5094fd0.jpg)

## J itte r Tra n sfe r S pecifi cati o n

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/e0364a185ec7519ad4b672d2b583eb926d1615b565029337bb2f2ec97c2e7a04.jpg)

<table><tr><td rowspan=1 colspan=1>Data Rate</td><td rowspan=1 colspan=1> $\mathbf { f } _ { \mathsf { c } } [ \mathbf { k H z } ]$ </td><td rowspan=1 colspan=1>P[dB]</td></tr><tr><td rowspan=1 colspan=1>155 Mb</td><td rowspan=1 colspan=1>130</td><td rowspan=1 colspan=1>0.1</td></tr><tr><td rowspan=1 colspan=1>622 Mb</td><td rowspan=1 colspan=1>500</td><td rowspan=1 colspan=1>0.1</td></tr><tr><td rowspan=1 colspan=1>2.488 Gb</td><td rowspan=1 colspan=1>2000</td><td rowspan=1 colspan=1>0.1</td></tr></table>

This specification is intended to control jitter peaking in long repeater chains

## J itte r Ge n e rati o n

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/b32d976dc1b6bd5abfd3a9bd6c8fd804d65b061acb4ab67ff75fd0ec4f80f253.jpg)

• J itter generation is how m uch j itter the CD R “generates”

Assu med to be dom i nated by VCO

• Assu m es j itte r-free se ri a l d ata i n p ut

VCO Phase Noise : $H _ { n _ { t e c o } } ( s ) = \frac { \phi _ { o u t } } { \phi _ { n _ { t e c o } } } = \frac { s ^ { 2 } } { s ^ { 2 } + \left( \displaystyle \frac { K _ { L o o p } } { N } \right) R C s + \displaystyle \frac { K _ { L o o p } } { N } } = \frac { s ^ { 2 } } { s ^ { 2 } + 2 \zeta \omega _ { n } s + \omega _ { n } ^ { 2 } }$

For CDR, N shou ld be 1

## J itte r Ge n e rati o n

H ig h- Pass Tra nsfer Fu nction

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/34bb2fae87e84df471bf0794c62bfe3b56eca1b8d0c4afca4e9df4824aef56e1.jpg)

• SO N ET specification :

J itter accu m u lates u p to ti me   1/ PLL ba ndwidth

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/0cb1495772d02b86b77e885c95b21da0cf493995c4b009418382eda06d41ffec.jpg)

rm s o utp ut j itte r  ≤ 0 . 0 1 U I

## J itte r To l e ra n ce

• H ow m uch si n u soida l j itter ca n the CD R “tolerate” a nd sti l l ach ieve a g iven BER? [Shei khol esla m i ]

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/547f82ec3c147783fbfbc45e98ebc3740c17ed45f5b9d9a4fb6c7ca914c6f8b7.jpg)

Maximu m tolerable $\phi _ { \tt e }$

$$
\phi _ { e } \left( s \right) = \left( 1 - \frac { \phi _ { o u t } \left( s \right) } { \phi _ { i n } \left( s \right) } \right) \phi _ { n . i n } \left( s \right) \leq \frac { \mathrm { T i m i n g ~ M a r g i n } } { 2 }
$$

$$
J T O L ( s ) = 2 \phi _ { n . i n } ( s ) = { \frac { T M } { \left( 1 - { \frac { \phi _ { o u t } ( s ) } { \phi _ { i n } ( s ) } } \right) } }
$$

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/24f3d90ededb21e5a9c7961ac8b7fb30cc263bd7e428032312ade510bac9f0a8.jpg)

## J itter Tolera nce Measu rement

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/c551df869962b178a6f3c3ce934c0c4399e1ee21819c007a44da0983b1cc37a5.jpg)

• Ra ndom a nd si n usoida l j itter a re added by mod u lati ng the BERT clock

• Determ i n istic j itter is added by passi ng the data th roug h the cha n nel

• For a g iven freq uency, si n u soida l j itter a m pl itude is i ncreased u nti l the m i n i m u m accepta ble BER $( 1 0 ^ { - 1 2 } )$ is recorded

## J itter Tolera nce Measu rement

![](/img/mineru_output/lecture12_ee720_cdrs/auto/images/78036494c3259f39c40d2dc39c858b31b1227f071854783dd8cbc05e5ccbfd64.jpg)

## CDR Ta ke-Away Poi nts

CDRs extract the proper clock freq uency a nd phase position to sa m ple the i ncom i ng data sym bols

• Specia l ized phase detectors su ited for ra ndom data sym bols a re req u i red

• Dua l - loop CDRs a re often used to both opti m ize j itter performa nce a nd provide robust freq uency acq u isition

• J itte r to l e ra n ce i s a n i m po rta nt C D R m etri c th at i s i m proved with i ncreased loop ba ndwidth

## Next Ti me

• Forwa rded -Clock Deskew Ci rcu its

• Clock Distri bution Tech n iq ues