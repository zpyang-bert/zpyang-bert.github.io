---
layout: post
title:      "ECEN 720 : H ig h-Speed Li n ks Ci rcu its a nd Systems Spri ng 2023"
date:       2026-04-18 17:56:58
author:     "Bert"
tags:
  - Lecture
  - Mineru
  - TX
  - Termination
---
Lectu re 5 : Term i nation , TX Driver, & M u lti plexer Ci rcu its

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/6a247d1e675367035c44ad28812163a9a67fb714e6b87c27c87e6eef759a5ac6.jpg)

Sa m Pa lermo Ana log & M ixed -Sig na l Center Texas A&M U n iversity

## An nou ncements

• La b 3 report a nd Prela b 4 d ue Feb 20

• Read i ng

• Pa pers posted on voltage- mode d rivers a nd h ig ho rd e r TX m u lti p l exe r ci rcu its

## Agenda

• Te rm i n ati o n Ci rcu its

• TX D rive r Ci rcu its

• TX ci rcu it speed l i m itati o n s

• Cl ock d i stri b uti o n

M u lti plexi ng tech n iq ues

## H ig h -Speed Electrica l Li n k System

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/243f6c8bb7bf42a5d84176690f3b7b6294b24305886f2446b51fd6cc1349f4c0.jpg)

TX data D[n] D[n+1]D[n+2]D[n+3]   
TX clk   
RX clk

## Term i nation

• Off-ch i p vs on -ch i p

• Se ri es vs pa ra l l e l

• DC vs AC Cou pl i ng

• Te rm i n ati o n ci rcu its

## Off-Ch i p vs On-Ch i p Term i nation

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/67ef173b18a7bfcef9351fbc20617627d8f873ce8748ee279393012cd491ff4a.jpg)  
(a) Extermal Terminator

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/c5dbf32608468251f962191ccbfd8e9bba8dd9c35a37ec057e9cf7754a00e802.jpg)

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/53e9578744843b405e56a097b1b4afbfacad7a180a40e37ee47fab3a58059cc5.jpg)

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/071ad2145a0bcc8c762dec7a41f7eff797b3d70d73a577d613ec55a7d894a7f2.jpg)

Package pa rasitics act as a n u nterm i nated stu b wh ich sends reflections back onto the l i ne

• On-ch i p term i nation ma kes package i nd ucta nce pa rt of tra n s m i ssi o n l i n e

## Series vs Pa ra l lel Term i nation

Series Termination

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/e7f95a04769ad12e90883efff1e77f58edff83b453d86316e9ab923f11c93c1f.jpg)

Pa ra l lel Term i nation

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/7b163c818c429a200483672e90fa78f2c94b72c430de131a3bf2e50443f59e91.jpg)

Dou ble Termination

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/4d2a9ce52bdefba3365ff7220f8d5b26abbbfb1222e95abb991037f5601671fa.jpg)

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/35ba1b66a71b49c904200091cb6a38422eea1f46c8bf7d73876b347c5df6844c.jpg)

• Low i m peda nce voltage- mode d river typica l ly em ploys se ri es te rm i n ati o n

H ig h i m peda nce cu rrent- mode d river typica l ly em ploys pa ra l l e l te rm i n ati o n

• Dou ble term i nation yield s best sig na l q ua l ity

• Done i n majority of h ig h performa nce seria l l i n ks

## AC vs DC Cou pled Term i nation

• DC cou pl i ng a l lows for u ncoded data

• RX com mon-mode set by tra n s m itte r s i g n a l l e v e l

• AC cou pl i ng a l lows for i ndependent RX com mon-mode level

• Now cha n nel has low freq uency cut-off

• Data m ust be coded

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/cc4cc327e375194c345e6815379a1e0412b233b33146ece38c9a1baee6a802ad.jpg)

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/9fa9a488d2e48d00014ffc74b09783cc90f84839cf7fc6ea314e468b24ad33fb.jpg)

## Passive Term i nation

• Choice of i nteg rated resistors i nvolves trade-offs i n ma n ufactu ri ng steps, sheet resista nce, pa rasitic ca pacita nce, l i nea rity, a nd ES D tolera nce

• I nteg rated passive term i nation resistors a re typica l ly rea l ized with u n sa l icid ed po ly, d iffu sio n , o r n -we l l resi sto rs

• Poly resistors a re typica l ly u sed d ue to l i nea rity a nd tig hter tolera nces, but they typica l ly va ry +/-30% over process a nd tem peratu re

Resistor Options (90nm CMOS)
<table><tr><td rowspan=1 colspan=1>Resistor</td><td rowspan=1 colspan=1>Poly</td><td rowspan=1 colspan=1>N-diffusion</td><td rowspan=1 colspan=1>N-well</td></tr><tr><td rowspan=1 colspan=1>Sheet R (2/sq)</td><td rowspan=1 colspan=1>90±10</td><td rowspan=1 colspan=1>300±50</td><td rowspan=1 colspan=1>450±200</td></tr><tr><td rowspan=1 colspan=1>VC1(V-1)</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>10-3</td><td rowspan=1 colspan=1>8x10-3</td></tr><tr><td rowspan=1 colspan=1>Parasitic Cap</td><td rowspan=1 colspan=1>2-3fF/um2(min L poly)</td><td rowspan=1 colspan=1>0.9fF/um2 (area),0.04fF/um (perimeter)</td><td rowspan=1 colspan=1>0.2fF/um² (area),0.7fF/um (perimeter)</td></tr></table>

## Active Term i nation

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/155c91a7de079b9b4fb8c86ebb2243422139c01b7c3fdffa1a42808b8b5f6ee1.jpg)  
(a) Triode

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/62ebe4cea39271d2a621c3c29819f92fcff80b852e4958a7ebf4afaad5dcc62f.jpg)  
(b) Two-Element

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/d1a0c014a2834e0c37ad076dc27dd5591178e3eb3412c6c89b9f2e466696c7d8.jpg)  
(c) Pass Gate

• Tra nsistors m ust be used for term i nation i n CM OS processes wh ich don ’t provide resistors

• Triode-biased FET works wel l for low-swi ng ( < 500 mV)

• Add i ng a d iode con nected FET i ncreases l i nea r ra nge

• Pass-gate structu re a l lows for d iffe re nti a l te rm i n ati o n

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/96ae42b6ee7992f024fdda67acc5dc47dac9e3f3554de6a625439e8b5b187b35.jpg)  
[ Da l l y ]

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/98037e144a5400adb6f85b676a9a44193a3262e45eceac6207aafe4ba5e4f379.jpg)

## Adj usta ble Term i nation

• FET resista nce is a fu n cti o n of g ate overd rive

$$
R _ { F E T } = \frac { 1 } { \mu C _ { o x } ( W / L ) ( V _ { G S } - V _ { t } ) }
$$

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/9b84ab2b5f2f171bda3a7ee383d35116a097c3366e349f60761a0b40e2394a07.jpg)

• La rge va ria nce i n FET th reshold voltage req u i res adj u sta ble term i nation structu res

• Ca l i bration ca n be done with a n a na log control vo ltag e or th rou g h d ig ita l “tri m m i ng ”

• Ana log control red uces $\mathsf { V } _ { \mathsf { G S } }$ a nd l i nea r ra nge

• D i g ita l co ntro l i s g e n e ra l ly p refe rred

## Term i nation Dig ita l Control Loop

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/db30a4c4d33bbd5ce877b08219413b7c9866549bfb3e6bf0c44cd6e911135d29.jpg)

• Off-ch i p precision resistor is u sed as reference

• O n -ch i p te rm i n ati o n i s va ri ed u nti l vo lta g es a re with i n a n LSB

Dither fi lter typica l ly u sed to avoid voltage noise

• Control loop may be sha red a mong severa l l i n ks, but with i ncreased na nometer CMOS va riation per-cha n nel ca l i bration may be necessa ry

## H ig h -Speed Electrica l Li n k System

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/387196dbf3b1c5047cce313f41208e05edf55bcc16274a59e3788cea79b85969.jpg)

## TX D rive r Ci rc u its

• Si ng le-ended vs d ifferentia l sig na l i ng

• Control led -i m peda nce cu rrent & voltagemode d rivers

Swi ng en ha ncement tech n iq ues

• I m peda nce control

• Pad ba ndwidth extension

S l ew- rate co ntro l

## Si ng le- Ended Sig na l i ng

• Fi n ite su pply i m peda nce ca u ses sig n ifica nt Si m u lta neous Switch i ng Output (SSO) noise (xta l k)

• N ecessitates la rge a mou nts of decou pl i ng ca pacita nce for su ppl ies a nd reference voltage

• Deca p l i m its I/O a rea more th at ci rcu itry

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/663255cecd88b99059e7c0bcee191f755aa1b0afafca27f14e8a68030dc82d44.jpg)

## D iffe re nti a l S i g n a l i n g

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/bcc1d77b8051af552d31927dcff23651fa1f61ba2573cf0a06978780a936caad.jpg)

• A d ifference between voltage or cu rrent is sent between two l i n es

• Req u i res 2x sig na l l i nes relative to si ng le-ended sig na l i ng , b ut l ess retu rn p i n s

• Adva ntages

Sig na l is self- referenced

• Ca n ach ieve twice the sig na l swi ng

Rejects com mon- mode noise

Retu rn cu rrent is idea l ly on ly DC

## TX D rive r Ci rc u its

• Si ng le-ended vs d ifferentia l sig na l i ng

• Control led -i m peda nce cu rrent & voltagemode d rivers

Swi ng en ha ncement tech n iq ues

• I m peda nce control

• Pad ba ndwidth extension

S l ew- rate co ntro l

## Control led -I m peda nce Drivers

• Sig na l i nteg rity considerations ( m i n . reflections) req u i res 50 Ω d river output i m peda nce

• To prod uce a n output d rive voltage

• Cu rrent- mode d rivers use Norton-eq u iva lent pa ra l lel term i nation Easier to control output i m peda nce

• Voltage- mode d rivers use Theven i n-eq u iva lent series te rm i n ati o n

• Pote ntia l ly ½ to ¼ th e cu rre nt fo r a g ive n outp ut swi n g

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/272212c84d0cc43c60be9200acd46d2fafedbad4c32b8e3c998a707d1b517306.jpg)  
Current-Mode

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/91f883117f7e6d9df865b903fa63dd88f8a372ecf6969cf0cc60909e9f473c77.jpg)  
Voltage-Mode

## Push - Pu l l Cu rrent- Mode Driver

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/92a123731e6aa70d172238fd75edd9ca4c846ded2aa2a5a28ecd4193f29ff190.jpg)

• Used i n Low-Voltage Differentia l Sig na ls ( LVDS) sta nda rd

• D rive r cu rre nt i s i d ea l ly co n sta nt, resu lti n g i n l ow d I/dt n o i se

• Dua l cu rrent sou rces a l low for good PSRR, but head room ca n be a problem i n low-voltage tech nolog ies

• Differentia l pea k-to- pea k RX swi ng is  I R with dou ble term i nation

## Cu rrent- Mode Log ic (CM L) Driver

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/7ccd262a6c8fd004073d68d2c94c09cc08ce5d6fdeec81850db5eda79d3c1397.jpg)

• Used i n most h ig h performa nce seria l l i n ks

• Low voltage operation relative to push - pu l l d river

H ig h output com mon - mode keeps cu rrent sou rce satu rated

• Ca n use DC or AC cou pl i ng

AC cou pl i ng req u i res data cod i ng

• D iffe re nti a l p p RX swi n g i s $\pm \mathrm { I R } / 2$ with dou ble term i nation

## Cu rrent- Mode Cu rrent Levels

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/5f1bcc1ff5fd4c7666760bdfdf485439eb79fd868d36a2b46c3a389473192704.jpg)

$$
V _ { d , 1 } = ( I / 2 ) R
$$

$$
V _ { d , 0 } = - ( I / 2 ) R
$$

$$
V _ { d , p p } = I R
$$

$$
\pmb { I } = \frac { V _ { d , p p } } { R }
$$

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/345a1b11ce5ce47d2b800bd78293a7ff8d6c8c5656857264a974c4a7003d9a6d.jpg)

$$
V _ { d , 1 } = ( I / 4 ) ( 2 R )
$$

$$
V _ { d , 0 } = - ( I / 4 ) ( 2 R )
$$

$$
V _ { d , p p } = I R
$$

$$
\pmb { I } = \frac { V _ { d , p p } } { R }
$$

## Voltage- Mode Cu rrent Levels

Sing le- Ended Termination

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/bb8c29b3e1c3e007aa9f7f124712aca9d867e5b284d01ffa4ecc5276a55b24c1.jpg)

$$
V _ { d , 1 } = \left( V _ { s } / 2 \right)
$$

$$
V _ { d , 0 } = - \big ( V _ { s } / 2 \big )
$$

$$
V _ { d , p p } = V _ { s }
$$

$$
I = \left( V _ { s } / 2 R \right)
$$

$$
\pmb { I } = \frac { V _ { d , p p } } { 2 R }
$$

Differentia l Term i nation

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/3ea6111e898958d168e9738f0d95b11ebe58ea3f35f86cba48f3e72a9d1ab890.jpg)

$$
V _ { d , 1 } = \left( V _ { s } / 2 \right)
$$

$$
V _ { d , 0 } = - \big ( V _ { s } / 2 \big )
$$

$$
V _ { d , p p } = V _ { s }
$$

$$
I = \left( V _ { s } / 4 R \right)
$$

$$
\pmb { I } = \frac { V _ { d , p p } } { 4 R }
$$

## Cu rrent- Mode vs Voltage- Mode Su m ma ry

<table><tr><td rowspan=1 colspan=1>Driver/Termination</td><td rowspan=1 colspan=1>Current Level</td><td rowspan=1 colspan=1>Normalized Current Level</td></tr><tr><td rowspan=1 colspan=1>Current-Mode/SE</td><td rowspan=1 colspan=1> $\underline { { \mathsf { V } _ { \mathrm { d } , \mathsf { p p } } / Z _ { 0 } } }$ </td><td rowspan=1 colspan=1>1x</td></tr><tr><td rowspan=1 colspan=1>Current-Mode/Diff</td><td rowspan=1 colspan=1> $\underline { { \mathsf { V } _ { \mathrm { d } , \mathsf { p p } } / Z _ { 0 } } }$ </td><td rowspan=1 colspan=1>1x</td></tr><tr><td rowspan=1 colspan=1>Voltage-Mode/SE</td><td rowspan=1 colspan=1> $\mathsf { V } _ { \mathsf { d } , \mathsf { p p } } / 2 \mathsf { Z } _ { 0 }$ </td><td rowspan=1 colspan=1>0.5x</td></tr><tr><td rowspan=1 colspan=1>Voltage-Mode/Diff</td><td rowspan=1 colspan=1> $\mathsf { V } _ { \mathsf { d } , \mathsf { p p } } / 4 \mathsf { Z } _ { 0 }$ </td><td rowspan=1 colspan=1>0.25x</td></tr></table>

• An idea l voltage- mode d river with d ifferentia l RX term i nation ena bles a potential 4x red uction i n d river power

• Actual d river power levels a lso depend on

• Output i m peda nce control

Pre-d river power

Eq ua l ization i m plementation

## Voltage- Mode Drivers

• Voltage- mode d river i m plementation depends on output swi ng req u i rements

• For low-swi ng $( < 4 0 0 { - } 5 0 0 \mathsf { m V p } )$ , a n a l l N M OS d rive r i s su ita b l e

• For h ig h -swi ng , CM OS d river is u sed

Low-Swing Voltage-Mode Driver

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/23e14745ecf49d42454f73af6f5a5a51a3b099d6e0f51df4b1c846efe9cc348d.jpg)

$$
V _ { s } < { \frac { 4 } { 3 } } \big ( V D D - V _ { t 1 } - V _ { O D 1 } \big ) \ ( \mathrm { D i f f . T e r m } )
$$

$$
V _ { \it s } < 2 \big ( V D D - V _ { \it t 1 } - V _ { \it O D 1 } \big ) \mathrm { ~ ( S E ~ T e r m ) }
$$

H ig h-Swing Voltage- Mode Driver

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/ee8e8d857a077fab1eb88ee00c6253d8e81552d82142e0ea1435022ed1655007.jpg)

$$
V _ { s } > \left| V _ { t 1 } \right| + V _ { O D 1 }
$$

## TX D rive r Ci rc u its

• Si ng le-ended vs d ifferentia l sig na l i ng

• Control led -i m peda nce cu rrent & voltagemode d rivers

• Swi ng en ha ncement tech n iq ues

• I m peda nce control

• Pad ba ndwidth extension

S l ew- rate co ntro l

## H ig h -Swi ng Tra nsm itter Li nea rity

• Tra nsm it swi ng s $\geq 1 \mathsf { V } _ { \mathsf { p p d } }$ a re often needed to su pport operation over h ig h - loss cha n nel s

• Red uctions i n su pply voltages ma ke ach ievi ng th i s swi n g with h i g h l i n ea rity d iffi cu lt

• Th i s i s pa rti c u l a rly i m po rta nt with PAM 4 mod u lation

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/1818c204e85ffbfdc09ff3edbb5254d7e98a713061fcda65da9ce79993ebe0b9.jpg)

$$
\mathrm { R L M } = 3 \frac { \mathrm { V _ { m i n } } } { \mathrm { V _ { p k \mathrm { - p k } } } }
$$

## Pa ra l lel Bleeder Cu rrent Sou rce

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/3bc5013de43de042eb7a38f74b9bccc83df0345e4e2bbae367e798cdcf027424.jpg)

• Pa ra l lel th ick-oxide bleeder cu rrent sou rce from 1 . 8V su pply ra ises output com mon mode

• Ach ieves $> 1 . 2 \mathsf { V } _ { \mathsf { p p d } }$ swi ng i n a 1 6n m Fi n FET process

## CM L Driver w/ H ig her Output Stage Su pply

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/17ab1a819d57f1551b1b8fa293c617f1e26e008a5f7197ae7dd5c1b3acdf3211.jpg)

H ig her output stage su pply

• Sou rce voltage of switch PM OS tra nsistors rema i ns nea r 1V fo r 1 0 n m re l i a b i l ity

• ${ \tt > } 1 \tt V _ { \tt p p d }$ swi ng

## Ta i l - Less Cu rrent- M ode Driver

## [Steffan ISSCC 20 17]

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/ecc04f8bb0538e72c5d5cd3ad43652ba301c36f9dd0c47cc09be0f8aceac7dd6.jpg)

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/3ca349c284c400fbbb054c7d2da0bb6f74f609acc7f26fdb94f89d4dbf7ad18f.jpg)

• Botto m tra n si sto r d rive n by fu l l - rate se ri a l i zed d ata

• Repl ica - bias network sets output stage cascode tra nsistors’ gate voltage to ach ieve the desi red output swi ng

• Ach ieves $1 . 2 \mathsf { V } _ { \mathsf { p p d } }$ output swi ng with 94% RLM

## Voltage- Mode Driver w/ Leve l -Sh ifti n g Pred rive r

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/3566f3deb70a8ef033d836621645194a55ba2d8d5edbc99d4c69d0c6da578582.jpg)

56.25Gbps  
![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/d42ebdfce6ff9ac54c3d4cbe11dffee6dbdcee30f6fa7820630386f316ff7d02.jpg)  
Package+PCB loss is \~3dB, FIR applied to open eye  
RLM = 98.5, SNDR = 37dB, SNR\_ISI = 37.7dB

• Pred river uses a 0 . 85V su pply to d rive the N MOS a nd a level sh ifted 0 . 1 5V G N D to d rive the PMOS

• Ach ieves $1 \mathsf { V } _ { \mathsf { p p d } }$ output swi ng i n 7n m CMOS

## Hybrid Voltage- Mode Driver w/ Pa ra l lel Cu rrent- Mode Seg ments

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/2976fdfdc418d5cda7ee9c593f6d4ecdc51a14a7641ad90fe0ef3e3bf9d800b0.jpg)

• Pa ra l lel cu rrent- mode output stage provides swi ng en ha ncement

• Ach ieves $1 . 2 \mathsf { V } _ { \mathsf { p p d } }$ output swi ng i n 40n m CMOS

## PAM4 Hybrid Voltage- Mode Driver w/ Pa ra l lel Push- Pu l l Cu rrent- Mode Seg ments

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/2a8c3665de616db8da2e0d64d765991542a7ecc29f33060e4cd66963666996ee.jpg)

• Pa ra l lel push - pu l l cu rrent sou rces d riven by the M SB & LSB a l low for a h ig h-swi ng PAM4 i m plementation

• Ach ieves $1 . 3 \mathsf { V } _ { \mathsf { p p d } }$ output swi ng i n 1V 28n m CMOS with > 94% RLM

## TX D rive r Ci rc u its

• Si ng le-ended vs d ifferentia l sig na l i ng

• Control led -i m peda nce cu rrent & voltagemode d rivers

Swi ng en ha ncement tech n iq ues

I m peda nce control

• Pad ba ndwidth extension

S l ew- rate co ntro l

## G loba l Resistor Ca l i bration

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/2e52aa9ff2aba1f63da19c0645078d43434b2264a28a5c16aa7de60a3d82c2da.jpg)

• Off-ch i p precision resistor is u sed as reference

• On -ch i p term i nation is va ried u nti l voltages a re with i n a n LSB Dither fi lter typica l ly u sed to avoid voltage noise

• I n cu rrent- mode d rivers, th is code is u sed for the nom i na l l oa d setti n g

## Low-Swi ng VM Driver I m peda nce Control

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/291d96d0accf66943a5603e9f37e1f6f9b0a2f85ab1e74d9680159669c582f59.jpg)

• A l i nea r reg u lator sets the output stage su pply, $\mathsf { V } _ { \mathsf { s } }$

• Term i nation is i m plemented by output N MOS tra nsistors

• To com pensate for PVT a nd va ryi ng output swi ng levels, the pre-d rive su pply is adj usted with a feed back loop

• The top a nd bottom output stage tra nsistors need to be sized d iffe re ntl $\mathsf { y } ,$ as they see a d ifferent $\mathsf { V } _ { \mathsf { O D } }$

## 4 : 1 Output M u lti plexi ng Voltage- Mode TX

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/cbf75e2bbd5145b413b92d016602046b50701574e942cf9cdbbcddfb53926719.jpg)

• I m peda nce control is ach ieved i ndependent of th e p re-d rive r su p p ly by add i ng add itiona l u p/down a na log - control led N MOS tra n s i sto rs

## • Leve l -s h ifti n g p re-d rive r a l l ows fo r s m a l l e r output tra nsistors

## Low-Swi ng Voltage- Mode Driver Ana log I m peda nce Control

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/cff38818e8ac09378832365381cbc3443ba5d0a47183400c7ccf86b91be9e4f5.jpg)

• Repl ica g loba l i m peda nce control loop provides a na log gate voltages to the add itiona l top/bottom tra nsistors to set the pu l l - u p/down i m peda nce

## H ig h-Swi ng Voltage- Mode Driver I m peda nce Control

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/ff75c241169f2a2a3f386585cfb822696a676eabf757e896d1ff7559f95ddd9c.jpg)

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/eed5df3d0ae9c867dde8c7890af82b08e333f2c264282d4b723227fcf2c2c280.jpg)

• Passive resistors + tra nsistors’ triode resista nce

Output i m peda nce wi l l cha nge d ue to process va riation

• Ca uses reflection a nd level m ismatch

## H ig h-Swi ng Voltage- Mode Driver I m peda nce Control

• Eq ua l ization control by setti ng the n u m ber of seg ments con nected to each ta p

• Term i nation control by setti ng the tota l n u m ber of ena bled seg ments

• Disadva ntages :

Tra n si sto r sta cki n g i n fu l l - rate path

• Extra a rea d ue to red u nda nt seg ments

• Extra power consu m ption beca use pre-d river shou ld be sized to d rive maxi m u m load

Sensitive to P/N skew va riations

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/44f5d183e66d77d87e6c6c1b549a7feaf501b03bacaaac4f52be0cb5e0be0dcc.jpg)

## H ig h-Swi ng Voltage- Mode Driver Hybrid I m peda nce Control Scheme

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/d7d5c5c5e9a175aaa784cd244ed6f607f52d8a4d784ec41c51968a8fa9a1250c.jpg)  
75 to 85 d rive r s l i ces (1 0 prog ram mable s l ices with NAN D and N O R as p re-d rive r)

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/769fc73b5c5f3dc6104d02a73fcdcb0729fb50d224e7e560a68634b878cea137.jpg)

• Prog ra m ma ble n u m ber of d river sl ices provides coa rse i m peda nce control to com pensate for resistor va riations

• Ana log i m peda nce loop provides fi ne i m peda nce control to com pensate for N MOS/PMOS va riations

• M easu red d ifferentia l mode retu rn loss meets key protocol s com posite retu rn loss mask

## TX D rive r Ci rc u its

• Si ng le-ended vs d ifferentia l sig na l i ng

• Control led -i m peda nce cu rrent & voltagemode d rivers

Swi ng en ha ncement tech n iq ues

• I m peda nce control

• Pad ba ndwidth extension

S l ew- rate co ntro l

## Output Pad Network Cha l lenges

• M eeti ng retu rn loss $( \mathsf { S } _ { 1 1 } )$ spec

• < - 7d B at Nyq u i st

• Maxi m izi ng ba ndwidth with sma l l g rou p delay

Su pport ESD

• Ba la nce output network size versus performa nce

## T-Coi l Output Stage

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/64cce7ed63c203e57661295636985ff5cbc7fd1e69dfd469ff1e39a15257cf23.jpg)

• Output T-coi l between d river a nd pad a l lows for spl itti ng of d river, ESD, a nd pad ca pacita nce

• Provides sig n ifica nt ba ndwidth en ha ncement a nd i m proved retu rn loss

## T-Coi l Eq uations

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/0572e252818ecc68bac4f3f6b9970ae8d1b1f5cc7db39a51cc4b58abd2314f3b.jpg)

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/21df4cd8008b70112d34014de8400ba2c7323bbb4c76b68498e60d143c778429.jpg)

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/a1e1ee0f9d64428788849055544bed483031f266ad248ade2c8aac4ac1ce532d.jpg)

$$
Z _ { \mathrm { T x , o u t } } ^ { \prime } = \frac { Z _ { T } \cdot Z _ { 3 } + Z _ { 1 } \cdot Z _ { 3 } + Z _ { 1 } \cdot Z _ { 2 } + Z _ { 2 } \cdot Z _ { 3 } + Z _ { 2 } \cdot Z _ { T } } { Z _ { 1 } + Z _ { 3 } + Z _ { T } }
$$

[ Kossel JSSC 2008]

(4)

(6)

$$
Z _ { 1 } = { \frac { ( L _ { a } + M ) \cdot s + R _ { a } } { D ( s ) } }\tag{7}
$$

$$
Z _ { 2 } = { \frac { ( L _ { b } + M ) \cdot s + R _ { b } } { D ( s ) } }
$$

$$
Z _ { 3 } = \frac { v _ { 4 } s ^ { 4 } + v _ { 3 } s ^ { 3 } + v _ { 2 } s ^ { 2 } + v _ { 1 } s + 1 } { u _ { 3 } s ^ { 3 } + u _ { 2 } s ^ { 2 } + u _ { 1 } s }\tag{8}
$$

$$
Z _ { T } = \frac { R _ { \mathrm { T x } } } { 1 + s R _ { \mathrm { T x } } C _ { T } } .\tag{9}
$$

$$
Z _ { \mathrm { T x , o u t } } = \frac { Z _ { \mathrm { T x , o u t } } ^ { \prime } } { 1 + s C _ { P } Z _ { \mathrm { T x , o u t } } ^ { \prime } } .
$$

Output Reflection Factor

$$
r = \frac { Z _ { \mathrm { T x , o u t } } - 5 0 \Omega } { Z _ { \mathrm { T x , o u t } } + 5 0 \Omega }\tag{10}
$$

<table><tr><td rowspan=1 colspan=4>Parameters: $L _ { \mathrm { a } } = 3 6 0$ pH, Lb = 240 pH, k = 0.4, M = 118 pH, Cb = 15 fF, Ct = 600 fF, $C _ { \mathrm { p } } = 7 0$ fF, $R _ { \mathrm { T x } } = R _ { \mathrm { R x } } = 5 0 \Omega$ </td></tr><tr><td rowspan=1 colspan=4> $\begin{array} { r } { { \cal D } ( s ) = C _ { b } \big ( L _ { a } + L _ { b } + 2 M \big ) \cdot s ^ { 2 } + C _ { b } \big ( R _ { a } + R _ { b } \big ) \cdot s + 1 } \end{array}$ </td></tr><tr><td rowspan=1 colspan=1> $\overline { { \nu _ { 1 } = C _ { b } \big ( R _ { a } + R _ { b } \big ) } }$ </td><td rowspan=1 colspan=1> $\overline { { \nu _ { 2 } = R _ { a } R _ { b } C _ { b } C _ { e } + C _ { b } \big ( L _ { a } + L _ { b } + 2 M \big ) - M C _ { e } } }$ </td><td rowspan=1 colspan=1> $\overline { { \nu _ { 3 } = C _ { b } C _ { e } \left( L _ { a } R _ { b } + L _ { b } R _ { a } \right) } }$ </td><td rowspan=1 colspan=1> $\overline { { { \nu _ { 4 } = C _ { b } C _ { e } \big ( L _ { a } L _ { b } - M ^ { 2 } \big ) } } }$ </td></tr><tr><td rowspan=1 colspan=1> $u _ { 1 } = C _ { e }$ </td><td rowspan=1 colspan=1> $\overline { { u _ { 2 } = C _ { b } C _ { e } \big ( R _ { a } + R _ { b } \big ) } }$ </td><td rowspan=1 colspan=2> $\overline { { u _ { 3 } = C _ { b } C _ { e } \big ( L _ { a } + L _ { b } + 2 M \big ) } }$ </td></tr></table>

## T-Coi l Wi ri ng & I m provement

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/df4e5b1aab327e908f42ce3a64955fbf1848e2bdb614f2c8a8da6afd789aaf61.jpg)  
g.22.a ssiDDie) SOI CMOS SST transmiter [7] with ESD. Simulated return loss curves: (e): HFSS EM model; (f) mathematical model.

## • A hel ica l wi ri ng scheme red uces the vertica l pa rasitic fri ng i ng ca pacita nce between layers a nd i m proves self- resona nce freq uency 4 5 45

## Dou ble T-Coi l Output Ba ndwidth Extension

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/13153a6ae180b623db425857083cdd29ca8608e30bd1f5d138be273b483425e7.jpg)

• Dou ble T-coi l structu re a l lows se pa ratio n of te rm i natio n ca pacita nce

• En ha nces ba ndwidth by 1 . 5X

[Steffan ISSCC 20 17]

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/06172fc902f7d3f63a7f703d95ca6fdc8aff445fcd92e881c54cfe6f064d7adc.jpg)

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/2ffd0e01cf33de237e33d14bb1e9bf50659b2d8199a8fe239d7e57c87c433281.jpg)

## -Coi l Output Ba ndwidth Extension

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/bf1f1013a3800c56bd50ada43024ad02ae3fb1af6953e29c9a3f1e7ca034f6ad.jpg)

• Output -coi l provides add itiona l term i nation ca pacita nce sepa ration

• Provides add itiona l ba ndwidth extension at the cost of sl ig htly deg raded retu rn loss

## -Coi l Output Ba ndwidth Extension

## Response at TX Pad

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/c9c94b2c7b86d69a1f6478bfc3cb691d7237cb253bdcae4816dd3c48e4ec8cc1.jpg)

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/4c7ddec293440a21a4202c900ad1801fdebd96fd4b4c1bb67d50677939ca7324.jpg)  
[ Kim ISSCC 20 19]

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/139d8103d0b7aa9fcc48c6f71af5c359a18ba354e492d8324864d7f2b76b438c.jpg)  
Response after 20d B channel

• 1 -2d B ba ndwidth pea ki ng resu lts i n sl ig htly deg raded retu rn l oss, b ut a bette r p u l se response over a low- pass cha n nel

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/fc9eb28317d98692f21bd2c07a6cb0694953e31861568b6929c3de7bf777582f.jpg)

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/ada6df976974ff8e7cf6d9ca81b7dc6383f257ffd08a22df4001018034193095.jpg)

## TX D rive r Ci rc u its

• Si ng le-ended vs d ifferentia l sig na l i ng

• Control led -i m peda nce cu rrent & voltagemode d rivers

Swi ng en ha ncement tech n iq ues

• I m peda nce control

• Pad ba ndwidth extension

• Slew- rate control

## TX Driver Slew Rate Control

• Output tra nsition ti mes shou ld be control led

• Too sl ow •

• Li m its max data rate

• Too fa st

Ca n excite resona nt ci rcu its, resu lti ng i n ISI d ue to ri ng i ng

Ca use excessive crossta l k

## • Slew rate control red uces reflections a nd crossta l k

## Slew Rate Control w/ Seg mented Driver

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/ef1e911cb537cb0164d4aa39862468707f8698990c4cc8c0674ed9071bb96d71.jpg)

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/5826976dd4fce070606e8eb13d909dc97f757d02a8a05b4ea726cd3526154304.jpg)

• Slew rate control ca n be i m plemented with a seg mented o utp ut d rive r

• Seg ments tu rn-on ti me a re spaced by $1 / \mathsf { n }$ of d esi red tra n s iti o n ti m e

• Pred river tra nsition ti me shou ld a l so be control led

## Cu rrent- Mode Driver Exa m ple

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/a25b6458242618e909456b806b0df88be182e7ae8c8da67a5e8f53de6863b00a.jpg)

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/2a8b9afe3fc046d7a23c9be3279b1b6fb277db24fbe727976c954145542a937c.jpg)  
A:(46.9446p 3.28265m) delta: (88.991p 586.674u) B：（135.936b 3.86933m) sloe:6.59251M

## Voltage- Mode Driver Exa m ple

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/49aacff96beb178a9833d146450d0bc8ce039677d0df18571707db8ed2f4fdc7.jpg)

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/e2865c08d0ca3dc1353d946b7b948072f9103c47733a6e0f2dac74ed0872267e.jpg)

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/fc06bde1e47eda261700efcff39b4d0981e07439c77a33098d14c4a6211fcde5.jpg)  
deltc (89.4286p 476.868u) slope:B.33063M

## TX Ci rcu it Speed Li m itations

• H ig h -speed l i n ks ca n be l i m ited by both the cha n nel a n d th e ci rcu its

• Clock generation a nd d istri bution is key ci rcu it ba ndwidth bottleneck

• M u lti p l exi n g ci rcu itry a l so l i m its m axi m u m d ata rate

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/cbd537fbc6bf7346d15b968653793d75edbab27604f0f8a6fed110eb993f9ed3.jpg)

## TX M u lti p l exer – Fu l l Rate

• Tree-m ux a rch itectu re with cascaded 2 : 1 stages often used

• Fu l l - rate a rc h itectu re relaxes clock d utycyc l e, b ut l i m its m ax d ata rate

• Need to generate a nd d istri bute h ig h -speed clock

• Need to desig n h ig hspeed fl i p-flop

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/4c4b1782fae1a2bf1714b8671f7c48991dad0384ab331b0a086c8675f5c686a6.jpg)

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/0662fbbc814dfc3d885d17b2144160dc4d28734d058d65a4148d9e96783d0042.jpg)

## TX M u lti plexer – Fu l l Rate Exa m ple

• CM L log ic someti mes u sed i n last stages

• M i n i m ize CM L to save power

• 1 0G b/s i n 0 . 1 8 m CM OS

• 1 30mW ! !

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/c4b3080737868edb747e0ad8462da3fb10c6c5b2401d4d4c15b8e3e368d174f2.jpg)

## TX M u lti p l exer – H a lf Rate

• Ha lf- rate a rch itectu re el i m i nates h ig h-speed c l ock a n d fl i p-fl o p

• Output eye is sensitive to clock d uty cycle

• Critica l path no longer has fl i p-fl o p setu p ti m e

• Fi n a l m ux co ntro l i s swa pped to prevent output g l itches

• Ca n a l so d o th i s i n preced i ng stages for better ti m i ng ma rg i n

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/0ce7ffd4f396a4a7a0f5165f0994f36a8f4c9bc246ffb683c136db0aa5787a03.jpg)

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/91bb14375d7b903d341dab6d781aeb34aa516b8a5e69d619915b1e20cb0dd236.jpg)

## Clock Distri bution Speed Li m itations

• Max clock freq uency that ca n be efficiently d istri buted i s l i m ited by cl ock b uffe rs a bi l ity to propagate na rrow pu l ses

• C M OS b uffe rs a re l i m ited to a m i n clock period nea r 8 FO4 i nverter delays

• About 4G Hz i n typica l 90n m CMOS

• Fu l l - rate a rc h itectu re l i m ited to th i s d ata rate i n G b/s

## • N eed a faster clock   u se fa ste r cl ock b uffe rs

• CM L

• CM L w/ i nd uctive pea ki ng

$\pmb { \mathrm { t } } _ { \mathtt { F O 4 } }$ in 90nm \~ 30ps  
![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/fe54df87b1fef576e706fa6dbf24fe221aa67be22b53430b9fb4dd6fe15db5c9.jpg)

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/e2165db2a5d7c6a0a15ad9b4e46cac38f9c8509b9c38775c11b2fe0da6bf657f.jpg)  
\*C . - K. Ya ng, “ Desig n of H ig h -Speed Seria l Li n ks i n CM OS, " 1 998 .

## M u lti plexi ng Tech n iq ues – ½ Rate

• Fu l l - rate a rc h itectu re i s l i m ited by maxi m u m clock freq uency to 8 FO4 ${ \sf T } _ { \sf b }$

• To i ncrease data rates e l i m i n ate fi n a l reti m i n g a n d u se m u lti ple phases of a slower clock to m ux data

• H a lf- rate a rch itectu re u ses 2 clock phases sepa rated by $1 8 0 ^ { \circ }$ to m ux data

• Al l ows fo r $4 F O 4 T _ { \mathsf { b } }$

• $1 8 0 ^ { \circ }$ phase spaci ng (d uty cycle) criti ca l fo r u n ifo rm o utp ut eye

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/38e283c67cd065e3e834dfdd62a242a23361d8a4474acf427a957d30180a7b91.jpg)

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/59f7d51da2c6de59c2bce0e6f56ff9d739451e611398a146db55318511665caa.jpg)

## 2 : 1 CMOS M ux

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/f2e50b7d5af717d6c22bc5f319aaf9c64bfdd4db20d23bd8573837c9c2ebc12a.jpg)

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/ccbceb6bbf10b343496b5cdc655538bd31fbb8cdf696434696894b5d0526092b.jpg)

2 : 1 CMOS m ux a ble to propagate a m i n i m u m pu lse nea r   
2FO4 ${ \sf T } _ { \sf b }$

• H oweve r, with a ½ - rate a rc h itectu re sti l l l i m ited by clock d istri bution to 4FO4 ${ \sf T } _ { \sf b }$

8G b/s i n typica l 90 n m

## 2 : 1 CM L M ux

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/0c69d3c823e82e0ab774c39364273f5aab7bde8dd3dad0065f16835a2f54946a.jpg)

• CM L m ux ca n ach ieve h ig her speeds d ue to red uced se lf- l oa d i n g fa cto r

• Cost is h ig her power consu m ption that is i ndependent of data rate (stati c cu rre nt)

## I ncreasi ng M u lti plexi ng Factor – ¼ Rate

• I ncrease m u lti plexi ng fa cto r to a l l ow fo r l owe r freq uency clock d i stri b uti o n

• ¼ - rate a rc h itectu re

• 4- phase clock d istri bution spaced at $90 \textdegree$ a l l ows fo r 2FO4 Tb

• 90  phase spaci ng a nd d uty cyc l e c riti ca l fo r u n ifo rm output eye

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/802e8a0e83bfdc4f3ef94960d162c75a7ef3726131ddcb24ec8c1bc3183b7288.jpg)

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/d673cb2d064d1e12f5e0ab9027d4d946f4264d1384557ea2c4a796781c42aef6.jpg)

## I ncreasi ng M u lti plexi ng Factor – M ux Speed

• H ig her fa n - i n m uxes ru n slower d ue to i ncreased ca p at m ux node

## • ¼ - rate a rc h itectu re

• 4 : 1 CMOS m ux ca n potentia l ly ach ieve 2 FO4 ${ \sf T } _ { \sf b }$ with l ow fa n o ut

An agg ressive CMOS-style desig n has potentia l for 1 6G b/s i n typica l 90 n m CMOS

## • 1/8- rate a rch itectu re

8- phase clock d istri bution spaced at $4 5 ^ { \circ }$ a l lows for 1 FO4 Tb

• No way a CMOS m ux ca n ach ieve t h i s ! !

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/43f59f93179f32d6b77e2b99b00820c946a356b2a0100e9819eb98312e2ac5ca.jpg)

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/a88d4b41fc0ab1a948a41bd2d9fc655be3aa3587332e5a1965964f12c8618c23.jpg)

## H ig h -Order Cu rrent- Mode Output- M u lti plexed

• 8 : 1 cu rrent- mode m ux d i rectly at output pad

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/5edbc5692c2677e9149652196e386eeea220178eaed06bee3f472f2c1a49796e.jpg)

• M a kes sense if output ti me consta nt sma l ler tha n on -ch i p ti me consta nt

\*C . - K. Ya ng, “ Desig n of H ig h-Speed Seria l Li n ks i n CMOS, " 1 998 .

Very sensitive to clock phase spaci ng

$$
\tau _ { o u t } = 2 5 \Omega \times C _ { o u t }
$$

Ya ng ach ieved 6G b/s i n 0 . 3 5 m CMOS

Eq u iva lent to 33G b/s i n 90n m CMOS (now cha n nel ( n ot c i rc u it) l i m ited )

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/aa338e3a5d294af6884527fbf3ad89a7246c8fc758a72fae503531abeb33fdec.jpg)

## Cu rrent- Mode I n put- M u lti plexed

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/b10bfad4a6d48841c729acf286bf6fb9401ab2f96c96b2ae285a32986492db42.jpg)

![](/img/mineru_output/lecture5_ee720_termination_txdriver/auto/images/d3625cc44773318cb2de87dbbfa03eb6781ca3b2cc7db557a9c4fbe04e5606e3.jpg)

• Red uces output ca pacita nce relative to output- m u lti plexed d rive r

Easier to i m plement TX eq ua l ization

• N ot sensitive to output stage cu rrent m ismatches

• Red uces power d ue to each m ux stage not havi ng to be si zed to d e l ive r fu l l o utp ut cu rre nt

## Next Ti me

Receiver Ci rcu its

• RX pa ra meters

• RX stati c a m p l ifi e rs

• Clocked com pa rators

• C i rc u i ts

Cha racterization tech n iq ues

• I nteg rati n g rece ive rs

• RX se n s itivity

• Offset co rrecti o n