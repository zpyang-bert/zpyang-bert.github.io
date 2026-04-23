---
layout: post
title:      "ECEN 720 : H ig h-Speed Li n ks Ci rcu its a nd Systems Spri ng 2023"
date:       2026-04-18 16:48:57
author:     "Bert"
tags:
  - Lecture
  - Mineru
---
## Lectu re 14 : Clock Distri bution Tech n iq ues

![](images/0d51c7fc0790c8cdb39be6ac9237d00f146781def3c1d310fac62ec378996726.jpg)

Sa m Pa lermo Ana log & M ixed -Sig na l Center Texas A&M U n iversity

## An nou ncements

• Exa m 2 Apr 25

Focuses on materia l from Lectu res 7- 14

• Previous yea rs’ Exa m 2s a re posted on the website for reference

• Project Fi na l Report d ue May 2

Project Presentations May 4 ( 1 2 : 30 PM -2 : 30 PM )

## Agenda

Wi re Sca l i n g

• Cl ock D i stri b uti o n

• CM L2CMOS Converters

• M u lti- Phase Generation

• M u lti- Phase Ca l i bration

## Cl ock Di stri bution i n Seria l I/O System s

![](images/0709d18eebd209a828bc19170f68b20838cb2438193d3c17d92caea573b860a6.jpg)

## • On -d ie g loba l clock d istri bution is necessa ry i n m u lti -cha n nel em bedded a nd fowa rded clock seria l l i n k systems

## VLSI I ntercon nect (Wi res)

Loose pitch + thick metal on upper layers

• High speed global wires

• Low resistance power grid

Tight pitch on lower layers

• Maximum density for local interconnects

[ Boh r ISSCC 2009]

![](images/1b099c367496c95d1bd8029a3f6e632f392df0f86d820be65edf9f42171c9691.jpg)

<table><tr><td>Pitch (nm)</td><td></td></tr><tr><td>M8</td><td>810</td></tr><tr><td>M7</td><td>560</td></tr><tr><td>M6</td><td>360</td></tr><tr><td>M5</td><td>280</td></tr><tr><td>M4</td><td>240</td></tr><tr><td>M3</td><td>160</td></tr><tr><td>M2</td><td>160</td></tr><tr><td>M1</td><td>160</td></tr></table>

## Wi re Sca l i n g

Node “N”

Node “N + 1” ( id ea l sca l i ng )

![](images/1fc3a68e5f26a627dc49a34978a7e7bdcc3da58b2819522fd772c248c1d420fc.jpg)  
Node “N + 1” (actua l sca l i ng)  
[ Ho]

![](images/cf2ff8c56724b197360f51ee579bebcfbd81dfeef0c973bee3f56059d5772572.jpg)

![](images/3269ec9234518ccac32c6809b4cd6e86f613ec397b1828708e2fc4efaa5594b1.jpg)

• Idea l ly, we sca le everyth i ng by 0 . 7x when we move to a more adva nced tech nology node for $_ { 2 x }$ d e n sity

• Resu lts i n $_ { 2 x }$ wi re resista nce, wh ich d ra matica l ly i ncreases wi re RC delay To com pensate resista nce wi res get ta l ler

• Ca p g rows at a sma l ler pace with sca l i ng

Ta l ler wi res i ncrease sidewa l l ca p

I m proved (low- k) d ielectrics hel p red uce ca p

## Wi re Sca l i n g - De l ay

![](images/42c70de306cb1b52a2e2d5cc8ccf5ce253a499902890a0eb5aac9a3e4a42e7dc.jpg)  
[ Ho Proc. IE E E 200 1 ]

## • G loba l on-ch i p wi re RC delay becomes ma ny ( 1 00 + ) gate delays (if d riven w/ one l u m ped d river)

## Li m ited Wi re Ba ndwidth

![](images/b93c88fef105173966d38e9964fda2a548f59ef990c81ffd155fe7e6c3cdc921.jpg)

• G l o ba l o n -ch i p wi re ba ndwidth is m uch worse tha n ch i pto-ch i p cha n nels

• RC-dom i nated onch i p wi res vs ( R) LC-dom i nated off-ch i p wi res

## Agenda

• Wi re Sca l i n g

• Clock Distri bution

• CM L2CMOS Converters

• M u lti- Phase Generation

• M u lti- Phase Ca l i bration

## Cascaded Clock Buffers

[ Ki m ISSCC 20 19 ]

![](images/92f84df5dbedcd810582be5179358b6f04b049557a3433aca0bad461eaf75766.jpg)

• Tota l output j itter i n freq uency doma i n ca n be obta i ned from per-stage JTFs a nd phase noise ( PN )

## Cl ock Buffe r J itte r Tra n sfe r Fu n cti o n

## [ Kim ISSCC 20 19]

![](images/946f0d74fbed6639a82cde99963fc34b7c479667fb07592b9fc8fa1273314d7c.jpg)

![](images/84c8b4fea95043fed5cdc0c1a92c8ab44880bffbc92d18632a417cd72ceb0a95.jpg)

• S i g n ifi ca nt j itte r a m p l ifi cati o n at 28G H z i n th e c l ock d i stri b uti o n ch a i n

• M otivates most 1 1 2G b/s systems to u se a q ua rter- rate clocki ng scheme with 14G Hz clocks

• Quad ratu re phase spaci ng a nd d uty cycle correction is necessa ry for u n iform output eyes

## 14G Hz Quad ratu re Clock Distri bution

![](images/5cdf1029416d808ecfa486290fe2b57fcbbed722667025ee10f0d1c5e2c5ec77.jpg)

• PLL output phase noise is m u lti pl ied by clock d istri bution JTF

• C D R fi lte r ( h i g h - pa ss) i s a p p l i ed to g et th e u ntra cked effective TX j itte r

[ Kim ISSCC 20 19]  
![](images/b52bf668d3222099555dcadb4f796e2580d5388f5f35d7783a855e15e4ed20d3.jpg)  
208fsrms w/ 3M Hz CDR BW $\yen 123,456,789$ w/ 10M Hz CDR BW

## Clock Distri bution Reg u lation

![](images/dc67a2bfc7a7911d875b7f1460cc011008c8cd520922bdbf39dc11075b7bff66.jpg)  
[Tu rker ISSCC 20 1 9 ]

## H uawei 60G b/s PAM4 Clock Distri bution

![](images/042a93a77a6171c524b3b4335162cfd1121139014bb412ffaadf205741b52d29.jpg)  
[ LaCroix ISSCC 20 19]

![](images/bff27c34afbad877d4081c83a504f4415b3750231ec2d520360fc7211cb792c5.jpg)

• Wideba nd ½- rate si ng le-ended clock d istri bution (2- 1 6G Hz)

• 2 i ndependent data rates possi ble per 4- la ne macro

• LDO- powered CMOS i nverter- based d istri bution

M eta l sh ield a rou nd d istri bution wi res to lower crossta l k

## Med iatek 56G b/s PAM4 Clock Distri bution

![](images/ce3d910cd47516c48a0958aed883b8bcceb7c93c93b75e59a87d43de0be0d638.jpg)  
[G. Li, ASSCC 2015]

• Tu ned sta nd i ng -wave clock d istri bution

• Two sh u nt i nd uctors placed i n the m idd le set bou nda ry cond itions for the tra nsm ission l i ne a nd tu ne nea rly eq ua l a m pl itude at the d rop poi nts

## I nd uctive- Loaded Clock Distri bution

[Shibasaki ISSCC 20 16]

![](images/850feb71e72394a67fed5bcbc9bfaeb19e0c18fa5f9d62089ccce72cb2ed107c.jpg)

![](images/1148e56f2b4afdfbef0aa62311b2a8461a63e1015a5571eb4ad65ba410658822.jpg)  
28GHz clock path

2-stage na rrow- ba nd buffer d rives 2- la ne 2 : 1 M UXs a nd d ivider

• M i n i ma l length 28G Hz clock path

## Active-I nd uctor- Based Clock Distri bution

![](images/7b665f115a9f9ea0f3ebb83f277ee92080cc6d60b92908c9140ba73822e31a73.jpg)  
[ Upadhyaya ISSCC 20 18]

Active Ind uctor CM L Load

![](images/2abd71b075b33b105cbb1fd97809a5595d13e13e4cbd47400958bf40d92b29ee.jpg)

## Agenda

• Wi re Sca l i n g

• Cl ock D i stri b uti o n

• CM L2CMOS Converters

• M u lti- Phase Generation

• M u lti- Phase Ca l i bration

## CM L2CMOS Converter ( 1 )

[ Balamurugan JSSC 2008]

![](images/7b783378ba1845dd08b7158c56143d25720893b9f86e1f569f1830615dc665bd.jpg)

• Differentia l i n put stage fol lowed by h ig h -swi ng output stage

• Ca n be sensitive to power-su pply noise a nd red uce j itte r be n efits of l ow-swi n g d i stri b utio n tech n iq u es

• Often req u i re some type of d uty-cycle control

## CM L2CMOS Converter (2)

[ Kossel JSSC 2008]

• AC-cou pled self- biased i nverter i n put stages a nd cross-cou pled buffer stages ca n hel p i m prove d uty cycle performa nce

![](images/135b086ff54562a7c2eafdc67be74b89a3d7f30d61a9f619a48e9252c84a5d28.jpg)

## Agenda

• Wi re Sca l i n g

• Cl ock D i stri b uti o n

• CM L2CMOS Converters

M u lti- Phase Generation

• M u lti- Phase Ca l i bration

## I LO- Based M u lti- Phase Clock Generation

![](images/708425bcf2115874e9680c86ae01aa92e88fcc26bbc711b6317b3e2419480fe0.jpg)

• I LO generates m u lti ple output phases from d ifferentia l i njected clock

• Coa rse freq uency tu n i ng loop ensu res that the I LO wi l l lock

• Fi ne q uad ratu re- locked loop m i n i m izes phase error

## I BM 1 00G b/s PAM4 QDLL Phase Generation

![](images/08c09ad07555ae0ed642b064e52dcce6b28833875ceadf8749e9a238421d55b6.jpg)

## Agenda

• Wi re Sca l i n g

• Cl ock D i stri b uti o n

• CM L2CMOS Converters

• M u lti- Phase Generation

M u lti- Phase Ca l i bration

## Clock Error Ca l i bration Loop

![](images/4f219bd5dc19c6688cff34849226dfbff381bcc01742e7810e51d58b41ba18d9.jpg)

## Asynch ronous Sa m pl i ng Error Detection

![](images/0563c1170e113a05748bf16440633770e7b580367c085d513a0033f5df3a53b1.jpg)

![](images/fbd84eb4230262b4bb79e9585d7f5a76a3b3124146bc0b648c32970f08a4e75c.jpg)

![](images/fff1ebd9b37d0a30054af2d90ae7d36cb5cde0271315a2919d852f9ccbcce2ca.jpg)

Asynch ronous VCO sa m ples fi na l ¼ - rate clocks

• Duty cycle error m i n i m ized w/ eq ua l P/N cou nt

• Quad ratu re error m i n i m ized w/ eq ua l $\mathtt { I P ^ { * } Q P / Q P ^ { * } I N }$ cou nt

## Backg rou nd Quad ratu re Clock Ca l i bration

![](images/2271d9930be79bf82faaba3c88cbc33cef922ba230ea0288d96acb82d5e88f28.jpg)

• Duty cycle error detected by low- pass fi lteri ng clocks

• IQ m ismatch is detected by mon itori ng output d uty cycle of repl ica m ux

• I nformation is used to control i ndependent I/Q VCDLs

## 1 28G b/s PAM4 TX Clock Generation

[Toprak-Deniz ISSCC 2018]

![](images/7753b3ccc3c9d89b0565d2018d02080cb5a69f6ed444c8760e940d77854e8dfa.jpg)

• DCC with cu rre nt i nj ecti o n b uffe rs

• Q EC with d iffe re nti a l offset vo lta g e i n h a lf- rate C M L d ivi d e r

## DCC w/ I nverter Tri p Poi nt Adj u stment

• Clocks a re AC-cou pled to i n p ut i nve rte rs th at a re b i a sed at th e tri p po i nt with feed back resistors

• $\mathrm { I _ { D C } }$ i nj ected at i nve rte r i n p ut s h ifts tri p po i nt a n d output d uty cycle

• Monoton ic control ach ieved with pu l l - u p/down d iodes

• $\mathsf { R } _ { \mathsf { D C } }$ ca n a lso be adj usted to cha nge tu n i ng ra nge

![](images/4b5c4c7e3d3bd8672f9ade36e6f0fbffafae1b723ed093aae0750bc7184457d7.jpg)

## Clock Generation & Distri bution Ta ke-Away Poi nts

• Low- noise clock d istri bution is necessa ry i n h ig h - performa nce seria l l i n ks

J itte r a m p l ifi cati o n m u st be avo i d ed i n m u lti - la ne clock d istri bution

• Efficient m u lti - phase generation a nd ca l i bration is necessa ry for ¼ - rate front-end s