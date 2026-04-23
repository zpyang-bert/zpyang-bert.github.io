---
layout: post
title:      "ECEN 720 : H ig h-Speed Li n ks Ci rcu its a nd Systems Spri ng 2023"
date:       2026-04-18 16:59:45
author:     "Bert"
tags:
  - Lecture
  - Mineru
---
Lectu re 1 : I ntrod uction

![](images/c277572f4a06c70699b950fdcc388349d453d391df09a711c3b6aac1d36f01d0.jpg)

Sa m Pa lermo Ana log & M ixed -Sig na l Center Texas A&M U n iversity

## Class Topics

• System a nd desig n issues releva nt to h ig h -speed e l ectri ca l (a n d o pti ca l ) si g n a l i n g

• Cha n nel properties

Model i ng, measu rements, com m u n ication tech n iq ues

• H ig h -Speed l i n k ci rcu its

Drivers, receivers, eq ua l izers, ti m i ng systems

• Li n k system desig n

Model i ng a nd performa nce metrics

• Li n k system exa m ples

## Ad m i n i strative

## • I n stru cto r :

• Sa m Pa lermo

• 3 1 5 E WEB, 845-4 1 14, spa lermo@ta m u . ed u

• Office hou rs : M 8 : 30AM - 1 0 : 00AM R 4 : 00 PM -5 : 30 PM

## • Lectu res

• TR 9 : 3 5AM - 1 0 : 50AM, ZACH 36 1

• Videos posted on Ca nvas

• La b : M 1 2 : 40 PM -3 : 30 PM ZACH 1 27

• La b beg i ns on Ja n ua ry 30

## • Class web page

https ://people . eng r.ta m u . ed u/spa lermo/ecen 720 . htm l

• Wi l l u se Ca nvas for tu rn i ng i n assig n ments

## Cl a ss M ate ri a l

## • Textbook: Class Notes a nd Tech n ica l Pa pers

## • Key References

• Digital Systems Engineering, W. Da l ly a nd J . Pou lton, Ca m bridge U n iversity Press, 1 998 .

• Advanced Signal Integrity for High-Speed Digital Designs, S. H . Ha l l a nd H . L. Heck, Joh n Wi ley & Sons, 2009 .

• High-Speed Digital Design: A Handbook of Black Magic, H . Joh nson & M . G ra ha m, Prentice Ha l l , 1 993 .

• Design of Integrated Circuits for Optical Communications, B. Razavi, M cG raw- H i l l , 2003 .

## • Class notes

Wi l l post on l i ne before class

## G rad i ng

## • Exa ms (50%)

Two m idterm exa ms (25% each)

## Homework & La bs (25%)

La bs ( Prela b + Report) a nd homeworks weig hted eq ua l ly

• Col la boration is a l lowed, but i ndependent si m u lations a nd write- u ps

Need to setu p CADE NCE si m u lation envi ron ment

• Tu rn i n via Ca nvas

No late homework/la bs wi l l be g raded

## • Fi n a l P roj ect ( 2 5 % )

G rou ps of 1 -3 students

Report a nd PowerPoi nt presentation req u i red

## Prereq u isites

• Th is is a ci rcu its AN D systems class

• C i rc u its

ECEN474/704 or a pprova l of i nstructor

Basic knowledge of CM OS gates, flops, etc…

• Ci rcu it si m u lation experience ( H SPICE, Spectre)

## • Systems

Basic knowledge of s- a nd z-tra nsforms

• Basic d ig ita l com m u n ication knowledge

MATLAB experience

## Si m u lation Tools

• M atl a b

ADS (Statistica l BE R l i n k a na lysis)

• Cadence

90n m CMOS device models

• Ca n use other tech nology models if they a re a 90n m or more adva nced CMOS node

• Other tool s, schematic, layout, etc … a re o pti o n a l

## H ig h-Speed Seria l I/O

• Fou nd i n a ppl ications ra ng i ng from h ig h -end com puti ng systems to sma rt mobi le devices

Typica l processor platform

• Processor-to-memory : DDR4

• Processor-to- peri phera l : PCIe & USB

• Storage : SATA

• Network: LAN

## M obi le systems

• DSI : D i s p l ay Se ri a l I nte rfa ce

• CSI : Ca m e ra Se ri a l I nte rfa ce

• U n i PRO : M I PI U n iversa l Protocol

## AM D EPYC Rome Platform

![](images/59ea2918623000b6f88d3da5b6e758218c291bdf417b629567705fa2e98f3af8.jpg)

![](images/ddd5073908c137b713aa4d87b862dfdd9fe3f13fe57a0544396d56526d672485.jpg)

## Data Center Li n ks

## • Different i ntercon nect tech nolog ies a re used to spa n va rious d ista nces

## E l ectri ca l I/O

• Ch i p-to- mod u le

• I ntra - ra c k

## • O pti ca l I/O

TO R switch to edge switch

Futu re i ntra - ra c k

![](images/cd6e5ce5b20bbcc5df28e21c84bc777499900590ba203b50733bd46f28846510.jpg)  
[G iga l ig ht]

## I ncreasi ng I/O Ba ndwidth Dema nd

![](images/8a81b1f7e6f8ea32981198f993cac2202c7ef9bff1e8c9ac8738e80520cf68fa.jpg)

![](images/b00ada016f84071b447f6c3c8649627638b3d98821c442429b3268370e25a3d5.jpg)  
[Zhou Opt. Fi ber Tech . 20 17]

• Agg ressive sca l i ng of I/O data rates is req u i red for data centers a nd H PC systems

• PAM4 mod u lation offers h ig her spectra l efficiency a nd is com mon ly used i n electrica l I/Os operati ng a bove 50Gb/s

## H ig h -Speed Electrica l Li n k System

![](images/4a2f284bc0d760439e3a920e9e6af6eafaedf7c45721ffb98b0057105b100730.jpg)

## Electrica l Backpla ne Cha n nel

![](images/9b35d63f382b1504bc7cb3498c0462677da485b6b5c6891f3e1d22a2afffce8e.jpg)

• Freq uency dependent loss Dispersion & reflections

• Co-cha n nel i nterference Fa r-end ( FEXT) & nea r-end ( N EXT) crossta l k

## Cha n nel Performa nce I m pact

![](images/2b1b49849c6670d7ddd7e880f8ad04a79883efb39205d49f058c5c7422d7ba84.jpg)

![](images/b288789c458e40f2ab572766aa547bda1a16b1d7b7f08d3e02cfd37c3a4ffd1d.jpg)

![](images/f7c6a0ff5ffbe5c9dc8aa3da09ff33fdca8b433c8104c1f80256fb09a9669bba.jpg)

![](images/1caf2a8c0182075c3038771cf8eb0bb69c74a74f8c662ba54731a5af477323d7.jpg)

![](images/5760bbf8118bdb8e06a1f0c09e1215ab4454c3b5ab69971c361ca8e0c022ed97.jpg)

## Cha n nel Performa nce I m pact

![](images/8bbe181e7fae18701a0fbf38a1dc3ea1a114a59e4fd7c9bb5a9b12433dacc5c3.jpg)

![](images/9b14d4020e2e7d137b1b57f294b57cc06cc25dcdf926d454eccf4b0859f93e2e.jpg)

![](images/21249cc8ad63d57bb04d2794efe0f654664ea5bc10694181d2a43f2c2af1b272.jpg)

![](images/915bc788e4df622fbe7e1024dda47d486fe57c745ddc105bc7ae3252a46b88bd.jpg)

![](images/37f85f2620107442ce594465c937ceab928bae023a706bd59e1e090b62f66e27.jpg)

# A 1 0G b/s 5-tap D FE / 4-Tap F FE Transceiver i n 90n m C MOS Tech nology

M ou n i r M eg h e l l i , Se rgey Rylov, J oh n B u lzacch e l l i , Wooge u n Rh ee , Al exa nd er Rylya kov, H erschel Ai nspa n , Ben Parker, M ichael Bea kes , Ai ch i n Ch u ng , Troy Beu kema , Petar Pepelj ugoski , Le i S ha n , You ng Kwa rk, S u d h i r Gowd a a nd Da n F ried ma n

I B M T . J . Watson Resea rch Ce nte r, Yorktown H e ig hts , NY

## Transm iss ion C han nel I m pai rments

![](images/ae56529f78bf34aae42b9b32463cf521f589cd055718254e16f91ed4812e00cc.jpg)

![](images/ec49dd803a49964ffc58170750370dfe9d459f54d89fd1fa2e6ac199406f6ca7.jpg)

## 1 0G b/s SerDes Mai n Featu res

 Tx with 1 baud-spaced 4-ta p F F E

 Rx with 5-tap adaptive D F E and d ig ital clock recovery

 LC-VCO based P L L for low noise clock generation

 90 n m CM OS tech nology

## Tra ns m itte r Arch itectu re

## Key Featu res :

\- H a lf- rate C M L d es i g n

\- 4 -ta p F F E

\- Ta p p o l a ri ty co n t ro l

\- E S D p rotecti o n

\- 70 mW (24 mA mai n tap , no F F E )

<table><tr><td rowspan=1 colspan=1>FFE Taps</td><td rowspan=1 colspan=1>Full Scale</td><td rowspan=1 colspan=1>DAC bits</td></tr><tr><td rowspan=1 colspan=1>Pre-cursor</td><td rowspan=1 colspan=1>25%</td><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=1 colspan=1>Cursor</td><td rowspan=1 colspan=1>100%</td><td rowspan=1 colspan=1>6</td></tr><tr><td rowspan=1 colspan=1>1st Post-cursor</td><td rowspan=1 colspan=1>50%</td><td rowspan=1 colspan=1>5</td></tr><tr><td rowspan=1 colspan=1>2nd Post-cursor</td><td rowspan=1 colspan=1>25%</td><td rowspan=1 colspan=1>4</td></tr></table>

![](images/76468bc04c68ea0af0bcac0ae531be36ffd389814d6f649d2fd1ee758c01c7c0.jpg)  
“A Low Powe r 1 0G b/s Se ria l Li n k Tra ns m itte r i n 90-n m C M OS” A. Rylyakov et al . , CS I CS 2005 1

## Tx Output Eye D iag ram @ 1 0G b/s

No F FE, 24mA on mai n tap

![](images/163284f8943f2f01cc626fb8ff435f032a9c582db636631d6f2ce0db3f6ce17d.jpg)

F F E 4= [0 , 8 5% , - 1 5% , 0 , 0]

![](images/034d3e4dbefe221152e7f2ea27ddf060bed05e52cf46148f0ebf4d432e9b0460.jpg)

## Receiver Arch itectu re

![](images/19e0ebd9c692307e37a7623bfde5d7da79b87b5874d1426a8d231b4182a32b19.jpg)

\- 5-ta p conti n u ously ad a ptive D F E

\- Va ri a b l e g a i n a m p l i fi e r

\- D i g i ta l C D R

\- ES D protection ( H B M & C D M )

\- 1 30 mW (with D F E a nd C D R log i c)

## D FE Approach

![](images/e0f3045f6d38ca7d2a5a3705fc6569395f28830048fa0005f34e8e740d9d90eb.jpg)

<table><tr><td rowspan=1 colspan=1>DFE Taps</td><td rowspan=1 colspan=1>Resolution</td></tr><tr><td rowspan=1 colspan=1>H1</td><td rowspan=1 colspan=1>6 bits</td></tr><tr><td rowspan=1 colspan=1>H2</td><td rowspan=1 colspan=1>5 bits</td></tr><tr><td rowspan=1 colspan=1>H3, H4, H5</td><td rowspan=1 colspan=1>4 bits</td></tr></table>

## Key Featu res :

\- H a lf-rate D F E with H 1 specu l ation a nd dynam ic H2-H 5 feed back al lows 2 U I for s ett l i n g

\- D F E algorith m maxi m izes vertical eye ope n i ng at the d ata sl i ci ng i nsta nt

\- Offs et a dj u stm e n t at a l l th e s l i ce r i n p u ts

## CDR Loop

![](images/1df4c0c1cb6681681a1d437e2a8c6289818a81359ef51c3dd89496247a8d48e6.jpg)

## Key Featu res :

\- F u l l y d i g i ta l l o o p

\- Ca n ha nd l e u p to +/- 4000 p p m

freq u e n cy offset

\- I nd e pe nd e nt I , Q control

![](images/43c4b04c43ac7768ff78e1275f908c1b2de8fa7b7c1cc527403be6692748bc51.jpg)

## C h i p-to-C h i p Li n k Experi ments

![](images/1a635ffdae0d5dddd528c7e69e4769c694dbd923e0e39bbe77933afce6c22651.jpg)

<table><tr><td rowspan=1 colspan=1>TraceLength</td><td rowspan=1 colspan=1>5GHz losses(Tx module + boardtrace + Rx module)</td><td rowspan=1 colspan=1>Number of vias3.8mm via stub /1.8mm via stub /1.8mm via through</td></tr><tr><td rowspan=1 colspan=1>10&quot;(#1)</td><td rowspan=1 colspan=1>12dB</td><td rowspan=1 colspan=1>2/010</td></tr><tr><td rowspan=1 colspan=1>10&quot;(#2)</td><td rowspan=1 colspan=1>10dB</td><td rowspan=1 colspan=1>0/2/0</td></tr><tr><td rowspan=1 colspan=1>15&quot;</td><td rowspan=1 colspan=1>25dB</td><td rowspan=1 colspan=1>41210</td></tr><tr><td rowspan=1 colspan=1>20&quot;</td><td rowspan=1 colspan=1>15dB</td><td rowspan=1 colspan=1>01012</td></tr></table>

## C h i p-to-C h i p Measu rement Resu lts

![](images/1be25630a851b1870cac35dc34e7a4074e4a385ecd865c619ae08bfd9ced5e2c.jpg)  
Li n k[Meg hel l i (I B M) ISSCC 2006]

## Prel i m i na ry Sched u le

<table><tr><td rowspan=1 colspan=1>Topic</td><td rowspan=1 colspan=1>Week</td></tr><tr><td rowspan=1 colspan=1>I.      Channels</td><td rowspan=4 colspan=1>Week 1-7</td></tr><tr><td rowspan=1 colspan=1>II.      Communication Techniques</td></tr><tr><td rowspan=1 colspan=1>III.    Equalizers</td></tr><tr><td rowspan=1 colspan=1>IV.    Transmitter/Receiver Circuits</td></tr><tr><td rowspan=1 colspan=1>First Exam</td><td rowspan=1 colspan=1>March 7</td></tr><tr><td rowspan=1 colspan=1>V.     Equalizer Circuits</td><td rowspan=5 colspan=1>Week 8-14</td></tr><tr><td rowspan=1 colspan=1>VI.    Clocking Circuits</td></tr><tr><td rowspan=1 colspan=1>VII.   Clocking Systems</td></tr><tr><td rowspan=1 colspan=1>VIII.  Link Modeling</td></tr><tr><td rowspan=1 colspan=1>IX.    Link Examples</td></tr><tr><td rowspan=1 colspan=1>Second Exam</td><td rowspan=1 colspan=1>April 25</td></tr><tr><td rowspan=1 colspan=1>Project Report Due</td><td rowspan=1 colspan=1>May2</td></tr><tr><td rowspan=1 colspan=1>Project Presentations</td><td rowspan=1 colspan=1>May 4 (12:30PM – 2:30PM)</td></tr></table>

• Dates may cha nge with reasona ble notice

## Next Ti me

## • Cha n nels

• Com ponents

• Ch i p packages, PCBs, Wi res, Con nectors

• M od e l i n g

• Wi res, Tra nsm ission Li nes