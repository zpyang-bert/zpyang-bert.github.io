---
layout: post
title:      "ECEN 720 : H ig h-Speed Li n ks Ci rcu its a nd Systems Spri ng 2023"
date:       2026-04-18 20:36:32
author:     "Bert"
tags:
  - Lecture
  - Mineru
  - RX
---
Lectu re 6 : RX Ci rcu its

![](images/9d018f21c021a9533b082710183ff2aea1ac8b7f4568ef3463eb10c197c0452a.jpg)

Sa m Pa lermo Ana log & M ixed -Sig na l Center Texas A&M U n iversity

## An nou ncements

• La b 4 report a nd Prela b 5 d ue Ma r 6

• Exa m 1 Ma r 7

• Covers materia l th roug h Lectu re 6

Previous yea rs’ exa m 1 s a re posted on the website for reference

• Sa m pler a nd com pa rator pa pers a re posted on the website

## O utl i n e

• Receiver pa ra meters

• T-coi l s at RX exa m ples

• Ana log front-end

• Clocked com pa rators

• Se n sitivity & offset co rrecti o n

• Dem u lti plexi ng

• PAM4 RX exa m ple

## H ig h -Speed Electrica l Li n k System

![](images/5b8e9bb3536ca35362a1d3133909c41b25903d42af0ec88329ecd2a876ea1315.jpg)

TX data D[n] XD[n+1]D[n+2] D[n+3]   
TX clk   
RX clk

## Receiver Pa ra meters

• RX sensitivity, offsets i n voltage a nd ti me doma i n , a nd a pertu re ti me a re i m porta nt pa ra meters

• M i n i m u m eye width is determ i ned by a pertu re ti me pl us pea k-to- pea k ti m i n g j itte r

• M i n i m u m eye heig ht is determ i ned by sensitivity pl u s pea k-to- pea k voltage offset

![](images/228171cb869f02a1eb83879b750bae51d5fd275f6f80dbe7c38e4c89a1c4ee5d.jpg)

## RX Block Diag ra m

![](images/aadea2468104ddce6a4e806d4e0aa80d41446322dfbb076da597fae04d30777a.jpg)

• RX m ust sa m ple the sig na l with h ig h ti m i ng precision a nd resolve i n p ut d ata to l og i c l eve l s with h i g h se n sitivity

• I n put pre-a m p ca n i m prove sig na l ga i n a nd i m prove i n put referred noise

• Ca n a l so be u sed for eq ua l ization , offset correction , a nd fix sa m pler com mon-mode

M ust provide ga i n at h ig h- ba ndwidth correspond i ng to fu l l data rate

• Com pa rator ca n be i m plemented with static a m pl ifiers or clocked regenerative a m pl ifiers

Clocked regenerative a m pl ifiers a re more power efficient for h ig h ga i n

• Decoder used for adva nced mod u lation ( PAM4, Duo- bi na ry)

## O utl i n e

• Receiver pa ra meters

• T-coi l s at RX exa m ples

• Ana log front-end

• Clocked com pa rators

• Se n sitivity & offset co rrecti o n

• Dem u lti plexi ng

• PAM4 RX exa m ple

## 56G b/s PAM4 I n put Network

## [ Pisati ISSCC 20 19]

![](images/7d601788fde7ecbd1cbe8721f0db0c8e5269feb9a073a7a12405c87cbce1558f.jpg)

• T-coi l isolates ESD a nd i n put stage ca pacita nce

• Sh u nt pea ki ng with term i nation network provides ba ndwidth extension

## 1 00G b/s PAM4 I n put Network

![](images/9976e3b04b2833b80f6f551acb24964bcdb164f5bd51d226e92cc4b1c45f6764.jpg)

• Bridged T-coi l isolates ES D a nd provides fu rther ba ndwidth extension

• Series pea ki ng isolates i n put stage ca pacita nce

## O utl i n e

• Receiver pa ra meters

• T-coi l s at RX exa m ples

• Ana l og front-end

• Clocked com pa rators

• Se n sitivity & offset co rrecti o n

• Dem u lti plexi ng

• PAM4 RX exa m ple

## Ana log Front- End (AFE)

[ Pisati ISSCC 20 19]

![](images/25d483d4b0e386f0e102305302dbc7cdf12bd385bd0b81c7aff02aec6ea255d2.jpg)  
Analog Front End  
Input termination

![](images/68c2de6eb0f80fbcb8660ad4ac4548a0883e95e56a655deb38044e2a284cd1ab.jpg)  
stage 1

![](images/118ee6913b3b82280189ab493a8c8331d20fca57ea09211fe9da7660ce0cdbc6.jpg)  
stage 2

![](images/a5156230aff1d3e8b2b093dcf8fa67d63a6ddc73f6a60b38f151d988eff6340c.jpg)

• AFE provides eq ua l ization (CTLE) a nd ga i n stages (VGA) to opti m ize the sig na l for sym bol detection (m ixed -sig na l RX) or q ua ntization (ADC- based RX)

• Sh ri n ki ng su pply voltages ma ke it d ifficu lt to efficiently ach ieve ga i n

## RX Stati c D iffe re nti a l Am p l ifi e rs

• D iffe re nti a l i n p ut a m p l ifi e rs ofte n u sed as i n put stage i n h ig h performa nce seria l l i n ks

Rejects com mon- mode noise

• Sets i n put com mon- mode for preced i ng com pa rator

• I n p ut sta g e type ( n o r p) ofte n set by term i nation scheme

• H ig h ga i n- ba ndwidth prod uct necessa ry to a m pl ify fu l l data rate s i g n a l

• Offset correction a nd eq ua l ization ca n be merged i nto th e i n p ut a m p l ifi e r

![](images/b39aea35b000521f642e285333e6d3b2551239534d4e3247106d27307f2f247f.jpg)

$$
A _ { \nu } = g _ { m 1 } \big ( R _ { L } \| r _ { o 1 } \big ) \approx g _ { m 1 } R _ { L }
$$

![](images/19938d8ba0e002eaf08fb9dc919dffeab6da6d3c882304de65b51bd4eb271fe4.jpg)

## Low-Voltage G m -TIA Am pl ification

![](images/21f2c36711821adda08279e637dc7b32fe361ad4eebf187bed7a05a604242468.jpg)

• Two-stage topology consisti ng of a n i n put tra nscond ucta nce (G m) stage fol lowed by a n output tra nsi m peda nce (TIA) stage a l lows for low-voltage operation

Both N MOS a nd PMOS tra nscond ucta nce ca n be uti l ized

• TIA sta g e a l l ows fo r i m p roved g a i n with bette r l i n ea rity, a s mostly sig na l cu rrent passes th roug h $\mathsf { R } _ { \mathsf { F } }$

## eSi l icon 56G b/s PAM4 CTLE G m-Stage

• I n put AC-cou p l i ng for opti ma l com mon-mode to uti l ize both N MOS a nd PMOS Gm

• RC degeneration at ma i n i n put tra nsistors’ sou rces provides h ig h-freq uency pea ki ng

• Add itiona l tu na ble bias resistor at the N MOS i n put provides a n add itiona l zero for low-freq uency cha n nel com pensation

• Ga i n control ach ieved th roug h bias prog ra m ma bi l ity

[ Pisati ISSCC 20 19]

![](images/79ea8a472c586de3819c9e0e712dde5d7ca83c26e0f961d969a603a223f236e4.jpg)

## eSi l icon 56G b/s PAM4 CTLE TIA-Stage

• I nverter- based ga i n stage with feed back resistor

• Su pply noise rejection ach ieved with a repl ica - bias reg u lated power su pply

• As mostly sig na l cu rrent flows th roug h RF, good l i n ea rity i s a ch i eved with h ig h sig na l swi ng

[ Pisati ISSCC 20 19]

![](images/94101701c92ba36225b16b6754691fde6896853163472cf99c165ec8a7d098da.jpg)

## I nverter- Based Desig n

![](images/f47b15ef052bd898a796bc20ec572f3a909acd76136f073bd65d98ec66afc96e.jpg)

• I nverter- based desig n a l lows for both N MOS a nd PMOS tra nscond ucta nce

• Cel l s ca n a l so be u sed as resistive a nd active- i nd uctor load s

## 56G b/s I nverter- Based CTLE Repl ica Bias Loop

![](images/61d87a665270a29082b2523d2c8fa0b9e4eecfb69aca8cc79e8253c74dbdad12.jpg)  
• Repl ica - biasi ng with ri ng osci l lator- based process mon itor

## O utl i n e

• Receiver pa ra meters

• T-coi l s at RX exa m ples

• Ana log front-end

• Clocked com pa rators

• Se n sitivity & offset co rrecti o n

• Dem u lti plexi ng

• PAM4 RX exa m ple

## RX Clocked Com pa rators

• Al so ca l led regenerative a m pl ifier, sense-a m pl ifier, fl i p-fl o p, l atc h

• Sa m ples the conti n uous i n put at clock edges a nd reso lves th e d iffe re nti a l to a b i n a ry 0 o r 1

![](images/fdc57ecd53cd8d1af2da3ad31aa665c8b0488d0a3d7a86aaa21d50839790fad7.jpg)

## I m porta nt Com pa rator Cha racteristics

• Offset a nd hysteresis

• Sa m pl i ng a pertu re, ti m i ng resol ution , u ncerta i nty wi ndow

• Regeneration ga i n, voltage sensitivity, m eta sta b i l ity

• Ra ndom decision errors, i n put- referred noise

## Dyna m ic Com pa rator Ci rcu its

![](images/eb0ab4e1db6ad5e65a5baf5fa906603a57865278a7efeeeaf29ce9abf98abf89.jpg)  
Strong-Arm Latch

![](images/3e83d65d54950c2a2254709423857f46549af63e76bd7071be7fff22d810c159.jpg)  
CM L Latch

• To fo rm a fl i p-fl o p

After strong -a rm latch, cascade a n R-S latch

After CM L latch cascade a nother CM L latch

• Strong -Arm fl i p-flop has the adva ntage of no static power d issi pation a nd fu l l CM OS output level s

## StrongARM Latch Operation [J . Ki m TCAS 1 2009 ]

![](images/d653188c88eec7bce7c58aabbe8b889c0d44e5e701f952809b555dfbd769dc6b.jpg)

![](images/f6dc1c7238b4d629f969d25ebd40e59514266ba9ee8b301a549ee4eb013c2d89.jpg)

• 4 operati ng phases : reset, sa m pl i ng , regeneration, a nd decision

## StrongARM Latch Operation – Sa m pl i ng Phase [J . Ki m TCAS 1 2009 ]

• Sa m pl i ng phase sta rts when cl k goes h ig h, $\mathfrak { t } _ { 0 } ,$ a nd ends when PM OS tra nsistors tu rn on, $\mathfrak { t } _ { 1 }$

• M 1 pa i r d ischa rges $\mathsf { X } / \mathsf { X } ^ { \prime }$

• M 2 pa i r d ischa rges out+/-

$$
\begin{array} { r l } & { \frac { \nu _ { o u t } \left( s \right) } { \nu _ { i n } \left( s \right) } = \frac { g _ { m 1 } g _ { m 2 } } { s C _ { o u t } C _ { x } \left( s + \frac { g _ { m 2 } \left( C _ { o u t } - C _ { x } \right) } { C _ { o u t } C _ { x } } \right) } } \\ & { \phantom { m m m m m m } \cong \frac { g _ { m 1 } g _ { m 2 } } { s ^ { 2 } C _ { o u t } C _ { x } } = \frac { 1 } { s ^ { 2 } \tau _ { s 1 } \tau _ { s 2 } } } \\ & { \mathrm { w h e r e } \tau _ { s 1 } = C _ { x } / g _ { m 1 } \tau _ { s 2 } \equiv C _ { o u t } / g _ { m 2 } } \end{array}
$$

![](images/3262a261ee70d251067b0eb537a8bd9c1dc558616ca8c17fcc09154d59534787.jpg)

## StrongARM Latch Operation – Regeneration [J . Ki m TCAS 1 2009 ]

• Regeneration phase sta rts when PMOS tra nsistors tu rn on , $\mathsf { t } _ { 1 } ,$ u nti l decision ti m e, $\mathfrak { t } _ { 2 }$

• Assu m e M 1 i s i n l i n ea r reg ion a nd ci rcu it no longer sensitive to ${ \mathsf { v } } _ { \mathsf { i n } }$

• Cross-cou pled i nverters a m pl ify sig na l s via positivefeed back:

$$
\boxed { \begin{array} { c } { G _ { R } = \exp \left( \frac { t _ { 2 } - t _ { 1 } } { \tau _ { R } } \right) } \\ { \tau _ { R } = C _ { o u t } / \left( g _ { m 2 , r } + g _ { m 3 , r } \right) } \end{array} }
$$

![](images/170fbf1dabe4cd9ba4d5efe201cb0633c7570c81591fe1872ba1df9e35ff3b32.jpg)

![](images/7163e490ee4a0303888f8e51ae8a252fd93c1b9358f2ba8760f91375c92ebcd2.jpg)

![](images/f0b1ebd8e564ef5f71a2730425f39038151c39d44f4ea34968e64137dc346f9e.jpg)

## StrongARM Latch Operation – Diff. Output [J . Ki m TCAS 1 2009]

![](images/d06d0d5a33f1ed1cdfa4aa42932170812e9727cfb20bd0dcfc26130a08fed4d3.jpg)

## Conventiona l RS Latch

• RS latch holds output data d u ri ng latch precha rge phase

• Conventiona l RS latch ri s i n g o utp ut tra n s iti o n s fi rst, fo l l owed by fa l l i n g tra n s iti o n

![](images/b6f6debd4eefe96e0149e9a154e7db287efcd7b65365bde882ef59847242f1c2.jpg)

## Opti m ized RS Latch

• O pti m izi n g RS l atch fo r sym m etric pu l l - u p a nd pu l l -down paths a l lows for considera ble speed - u p

• D u ri ng eva l u atio n , l a rg e d river tra n si sto rs a re a ctivated to cha nge output data a nd the keeper path is d isa bled

• Du ri ng pre-cha rge, la rge d river tra nsistors a re tri -stated a nd sma l l keeper cross-cou pled i nverter activated to hold data [ N i kol ic JSSC 2000 ]

![](images/d1c1b1b1704feef52b381e631f12da92bc19fdfeb52efe3edf312b12a2b39dc3.jpg)

Driver BranchesEvaluation Mode (Clock H ig h)

Keeper BranchesHold/ Precharge Mode (Clock Low)

## Delay I m provement w/ Opti m ized RS Latch

[ N i kol ic JSSC 2000 ]  
![](images/f886a898ffdbf301668d98f8042adcf98fedf022339737036a36f136b8d9ab6b.jpg)  
• Strong -Arm fl i p-flop delay i m proves by close to a factor of two  
• Has better delay performa nce tha n other adva nced fl i p-flop topolog ies

## Sa m pler Ana lysis

• Sa m pler a na lysis provides i nsig ht i nto com pa rator operation

[Joha nsson JSSC 1998 ]

input

![](images/e8f8d878d38dd3809483488a4d7e1825669b8ff314349ade8cc149dab18c8a7c.jpg)

![](images/4b02c6e398cf8d2f1bfe411222d5521cdd3f8ff8f480758ea85659bd3b7f9f50.jpg)  
h    sampling fúnction  
aperture time (aperture window width)

$$
\nu _ { s a m p l e } = \int \displaylimits _ { - \infty } ^ { \infty } \nu _ { i n } ( \tau ) h ( \tau ) d \tau
$$

sampling clock

aperture delay

aperture jitter (aperture uncertainty)

• Switch ca n be modeled as a device wh ich determ i nes a weig hted average over ti me of the i n put sig na l

The weig hti ng fu nction is ca l led the sa m pl i ng fu nction

## Sa m pl i ng Fu nction Properties

• Sa m pl i ng fu nction shou ld (idea l ly) i nteg rate to 1

$$
\int _ { - \infty } ^ { \infty } h ( \tau ) d \tau = 1
$$

• Idea l sa m pl i ng fu nction is a delta fu nction

Sa m pled va l ue is on ly a fu nction of exact sa m pl i ng ti me

$$
\begin{array} { c c } { { \displaystyle { \bigtimes } } } & { { } } \\ { { \mathrm { i d e a l } h ( \bar { \tau } ) = \delta ( t ) } } & { { \displaystyle { \big T } } } \\ { { \qquad \quad \longmapsto \tau } } \end{array} \qquad \nu _ { s a m p l e } = \int _ { - \infty } ^ { \infty } \nu _ { i n } ( \bar { \tau } ) h ( \bar { \tau } ) d \tau
$$

## Sa m pl i ng Fu nction Exa m ple

• Pra ctica l sa m p l i n g fu n ctio n wi l l weig ht th e i n p ut sig na l nea r the nom i na l sa m pl i ng ti me

![](images/fc1e80d95a2ad08a725942ce3e7b4109a998c3cd1ae5a224bb37641362a0a1e7.jpg)

$$
\nu _ { s a m p l e } = \int \nu _ { i n } ( \tau ) h ( \tau ) d \tau
$$

## Sa m pler Freq uency Response

• Fou rier tra nsform of the sa m pl i ng fu nction yield s the sa m pler freq uency response

• Sa m pler ba ndwidth is a fu nction of sa m ple clock tra n s iti o n ti m e

![](images/e2159bc088b7d8ed35b53e784f3a8df347cc03246ece82a9475f885e34d44d59.jpg)

$$
F . T . \{ h ( - \tau ) \}
$$

![](images/03149a7998fd6e492a710b8aa825e8529b257fb39a2432b27671f29123b77275.jpg)

## Sa m pler Apertu re Ti me

• Ape rtu re ti m e i s d efi n ed a s th e width of th e S F pea k were a certa i n percentage (80%) of the sensitivity is confi ned h(τ)

$$
w _ { 8 0 } = t _ { 9 0 } - t _ { 1 0 }
$$

$$
0 . 1 = \intop _ { - \infty } ^ { t _ { 1 0 } } h ( \tau ) d \tau
$$

$$
0 . 9 = \int _ { - \infty } ^ { t _ { 9 0 } } h ( \tau ) d \tau
$$

![](images/7d687379fbd0408c01e67ca222b9281c656b10e3ec3e5b82600b7cc0d1e8d6bf.jpg)

## Clocked Com pa rator LTV Model

$$
V _ { _ { k } } { = } V _ { _ { o } } ( t _ { o b s } { + } k T )
$$

![](images/a882ed268701d6c42692cebf16b0e391f8f6d26c1b56f84a1cc295f01ea9d866.jpg)

LTV small signal model

![](images/8ab86ba24a2286d3c2aa3a05401ff628f652977a7eb2ebab21c1f302f1b4b7c5.jpg)

[J . Ki m ]

• Com pa rator ca n be viewed as a noisy non l i nea r fi lter fol lowed by a n idea l sa m pler a nd sl icer (com pa rator)

• Sma l l -sig na l com pa rator response ca n be modeled with a n I S F $\boldsymbol { \Gamma } ( \tau ) = h ( t , \tau )$

## Clocked Com pa rator ISF

Com pa rator IS F is a su bset of a ti me-va ryi ng i m pu l se

response $h ( t , \tau )$ for LTV systems :

$$
y ( t ) = \int _ { - \infty } ^ { \infty } h ( t , \tau ) \cdot x ( \tau ) d \tau
$$

![](images/5d1d0f7e7bce1cf62c483fbc50020e0ca6f5f033fabf6703096605f8e2f46815.jpg)  
Fig. 1. LTV system is characterized either with time-varying impulse response h(t, π) or with time-varying transfer function H (jω; ).

• $h ( t , \tau ) \colon$ syste m res po n se at  t to a u n it i m p u l se a rrivi n g at  

• I S F $\varGamma ( \tau ) = h ( t _ { o b s } \tau )$

For com pa rators, $t _ { o b s }$ is before decision is made

• Output voltage of com pa rator

$$
\nu _ { o } ( t _ { o b s } ) = \int _ { - \infty } ^ { \infty } \nu _ { i } ( \tau ) \cdot \Gamma ( \tau ) d \tau
$$

• Com pa rator decision

$$
D _ { k } = \mathrm { s g n } { \left( \nu _ { k } \right) } = \mathrm { s g n } { \left( \nu _ { o } { \left( t _ { o b s } + k T \right) } \right) } = \mathrm { s g n } { \left( \int _ { - \infty } ^ { \infty } \nu _ { i } \left( \tau \right) \cdot \Gamma \left( \tau \right) d \tau \right) }
$$

## Clocked Com pa rator ISF

![](images/a1ff6ff7e7637d062d31c976d0e5be4c837a0ba0236d640b1009fd7d32cd4ef0.jpg)

• IS F is defi ned with respect to $\mathsf { t } _ { \mathsf { o b s } } ,$ o r the decision ti me

• The com pa rator provides the most g a i n d u ri ng the sa m pl i ng phase

[J . Ki m ]

## Clocked Com pa rator ISF

IS F shows sa m pl i ng a pertu re or ti m i ng resol ution

• I n freq uency doma i n, it shows sa m pl i ng ga i n a nd ba ndwidth

![](images/bb75a2c77d1aeaccaa6f99b2164c665f9968f3199fc656bd66fb449885c58675.jpg)

![](images/be86af0b7592406fab861619b6bcd7b3cdd8adea3a7489f1d98735c50a5a7e09.jpg)

## Cha racterizi ng Com pa rator ISF

## [Jeerad it VLSI 2008 ]

1. Find Metastable $V _ { \mathrm { m s } } ( \tau ) = V _ { \mathrm { { o s } } } ( \tau  \infty , \tau )$ such that V(out+) = V(out-)

![](images/ef9aac940dbddb66e845bc86745a117bf124e5501ab396becaa3c0bed4536cc7.jpg)

![](images/2a8870cdd1471e807d68d38cf61f2b4c51498c165d6e7b77f6f7f148c208144c.jpg)

3. Derive ISF

![](images/35f89521d07fee6605d466e70a96625f2d516fdff015ceb9de8a47fcc947ae0b.jpg)

• For more deta i l s, see

![](images/05ac64ce64afb584f11f8db44e1b179d62f73d9903338b9aeb9eb29d6c128f3f.jpg)

![](images/150d5ab81d24e269d4fa8d3bf03af0663c78173e1f7a2412a72166361f5f1352.jpg)

http ://www. ece .ta m u . ed u/\~spa lermo/ecen689/ECEN 720 la b4 20 1 7 . pdf

## Com pa rison of SA & CM L Com pa rator ( 1 )

[Jeerad it VLSI 2008 ]

VDD effect on StrongARM ISF

![](images/68f4ea77843d94284cb1f29fe89af9dc3075f21fb7fb2c9dfd7ce6e91689b466.jpg)

![](images/df896065226d431ebbfeed82a0760ffaf49f7bc47bef0f4a322bf2f540d654aa.jpg)

## Com pa rison of SA & CM L Com pa rator (2)

## [Jeerad it VLSI 2008 ]

Sampling Gain vs Input Size  
![](images/d4e044d28a707e8a3b12ddec0429a3997b857ca2deafe3548c5605f0fd3899f0.jpg)

![](images/227c2f79f08d5211419ba97a43fa08dcbd392bf9455c9fb84d279ca05c21108a.jpg)

• CM L latch has h ig her sa m pl i ng ga i n with sma l l i n put pa i r

StrongARM latch has h ig her sa m pl i ng ba ndwidth

• For CM L latch i ncreasi ng i n put pa i r a l so d i rectly i ncreases output ca pacita nce

• For SA latch i ncreasi ng i n put pa i r resu lts i n tra nscond ucta nce i ncreasi ng faster tha n ca pacita nce

## Low-Voltage SA – Sch i n kel ISSCC 2007

![](images/d243a573d5b02fa4fac6af503e4d05330aa0264f4c1de2fe18f2af5143db1c96.jpg)

• Does req u i re cl k & cl k b

H ow sensitive is it to skew?

## Low-Voltage SA – Sch i n kel ISSCC 2007

![](images/4a8be7f2d3087da434633a16cbb3f7819164f8156707efed75217b9065ad4c24.jpg)

![](images/29a690cac34d8afbfb8f6859d0f1fa503c5dc089d05e723506ce2a2c0a6f0a4d.jpg)

## Low-Voltage SA – Sch i n kel ISSCC 2007

![](images/225190589284fb78dde1b853403a76f15ab033416e6a6c7255bb04abf7158bff.jpg)  
90nm CMOs simulations. $\Delta \lor \mathsf { i n } = 5 0 \mathsf { m V } .$  
Circuits designed for equal off set $\sigma _ { \mathrm { { o s } } } = 1 0 \mathrm { { m V } }$ at $\mathsf { V } _ { \mathsf { c m } } \mathsf { = } 1 . 1 \mathsf { V }$

## Low-Voltage SA – Gol l TCAS2 2009

![](images/6d1d4896e4991941c634b9af12045477acd51d710d25a27f871c35e2994ea423.jpg)

![](images/467438e9531bec6872863b4d8fc56399b46ee4f675f4d44c504c4a1baa5c7e7b.jpg)

• Si m i la r stacki ng to conventiona l SA latch

• However, now P0 a nd P 1 a re i n itia l ly on d u ri ng eva l uation wh ich speeds u p operation at lower voltages

• Does req u i re cl k & cl k b

H ow sensitive is it to skew?

## Low-Voltage SA – Gol l TCAS2 2009

![](images/17ae373017395906bc2d8b52ea47771b0153a585c03be49753f505fd1cbce715.jpg)

## Cha rge-Steeri ng Latch

F i rst Stag e (faste r)

![](images/d2707188c0c2eaf770da055d0b26b88bda4413136f582de6965eb922211a2d59.jpg)  
Second Stage (fast)

![](images/f039c52e625138cc5c0bfd85aab07de440172bf357f26bdd639053426f60915a.jpg)

![](images/bed29ae3bf89862609d95bef54b702e7ff47584aa2054571768604366f4dfb91.jpg)  
[C h iang 20 1 3 VLSI , Bai 20 1 4 ISSCC]

 Fi rst stage has sma l l a pertu re ti me, but both outputs d ischa rge to G N D

 Second stage has sma l l delay, provides ga i n, a nd latches the d iffe re nti a l o utp ut

 On ly req u i res one clock phase

 Ga i n i s l i m ited

## Cha rge-Steeri ng Latch Head room at Low-VDD

Reset Phase

![](images/511126ed511c8a22c30a85f76ddece1707eeb3d83647a128f2fb6d947e25779f.jpg)

![](images/8b9a1c6fb573e7fd6cb98722e3ff4b14222a712bed2e01fa6df1fc655d06370d.jpg)

• O n ly one effective tra nsistor stack

Maxi m izes $9 m$ of a ctive tra n si sto rs

Al lows for low-voltage operation

## Cha rge-Steeri ng Latch w/ Com mon- Mode Restore

[Bai 20 1 4 ISSCC]

![](images/ce20fdbd979404e54f4b1270d608b5ed979a2d4f0d6d5489bb9d1df4ca0ea254.jpg)

• Differentia l output swi ng is proportiona l to output voltage com mon-mode $( \mathsf { V } _ { \mathsf { C M } } )$ d ro p

• However, excessive $V _ { \mathsf { C M } }$ d rop ca n l i m it su bseq uent stages’ speed

• Add ition of PM OS ca pacitors a l lows for la rger overa l l ga i n

## 65 n m Cha rge-Steeri ng Latch Performa nce

![](images/489dc0c32db3b4bb065007f3b169d38e64aff43bc6c3fcff203eb9fc73b97caa.jpg)

![](images/d8b89a5d0fe802349add4ed7f34b6e155b5e38b910da051e16e046db2903aca2.jpg)

• Sa m pl i ng a pertu re is \~ 1 7 ps ( post- l ayo ut)

Latch has a ga i n > 2

• Al so possi ble to config u re the structu re as a fast sa m ple-a nd - h o l d (S/ H )

## Cha rge-Steeri ng Latch w/ Regeneration

![](images/871726bcfc9ae92f588c35ee2f6cef89b24fdfd01d14012c58a952b4dde58a1b.jpg)

![](images/804db95c0dbee5820fde56b398dcc09af36c105fe2be659fc5d8f2969c5165a3.jpg)

 Add ition of sma l l M p3/M n 3 regeneration stage i n pa ra l lel with second stage output provides a fu l l -swi ng output

 Regeneration cu rrent set with a n N M OS tra nsistor

 On ly req u i res one clock phase

 Overa l l , sma l ler delay relative to other low-voltage regenerative com pa rators (Sch i n kel latch)

• Uti l ized i n a 3 2G b/s PAM4 DFE receiver [ El had idy 20 1 5 VLSI]

## O utl i n e

• Receiver pa ra meters

• T-coi l s at RX exa m ples

• Ana log front-end

• Clocked com pa rators

• Se n sitivity & offset co rrectio n

• Dem u lti plexi ng

• PAM4 RX exa m ple

## RX Se n sitivity

RX se n sitivity i s a fu n cti o n of th e i n p ut refe rred n o i se, offset, a nd m i n i m u m latch resol ution voltage

$$
\nu _ { S } ^ { p p } = 2 \nu _ { n } ^ { r m s } \sqrt { S N R } + \nu _ { \mathrm { m i n } } + \nu _ { o f f s e t ^ { \ast } }
$$

• Ga ussia n (u n bou nded) i n put referred noise comes from i n put a m pl ifiers, com pa rators, a nd term i nation

• A m i n i m u m sig na l -to- noi se ratio (S N R) i s req u i red fo r a g iven bite rro r- rate ( B E R)

$$
\mathbf { F o r \ B E R } = \mathbf { 1 0 } ^ { - 1 2 } \left( \sqrt { \mathbf { S N R } } = 7 \right)
$$

• M i n i m u m latch resol ution voltage comes from hysteresis, fi n ite regeneration ga i n, a nd bou nded noise sou rces

$$
\mathbf { T y p i c a l } \nu _ { \mathbf { m i n } } < 5 m V
$$

• I n p ut offset i s d u e to ci rcu it m i s m atch ( p ri m a ri ly $\mathsf { V } _ { \mathtt { t h } }$ m ismatch) & is most sig n ifica nt com ponent if u ncorrected

## Front- End Noise

![](images/2b9c98ed9d513c179e8b47017088f9b25cc32619898759c0cbededf7bcd20ff5.jpg)  
Output Noise Power Spectrum: $V _ { n , F E } ^ { 2 } = | H ( f ) | ^ { 2 } \cdot V _ { n , i n } ^ { 2 } ( f )$

Integrating this noise spectrum over the decision circuit bandwidth $B W _ { D }$ gives the total noise power experienced by the decision circuit

$$
\overline { { v _ { n , F E } ^ { 2 } } } = \int _ { 0 } ^ { B W _ { D } } | H ( f ) | ^ { 2 } \cdot V _ { n , i n } ^ { 2 } ( f ) d f
$$

• N ote that si nce $H ( f )$ genera l ly rol l s-off q u ickly, the exact u pper bou nd is n ot too criti ca l a n d co u l d be set to a ve ry h i g h va l u e ( i nfi n ity) 5 3

## 56G b/s Front- End Output Noise Exa m ple

![](images/70a64f087784c8290dd475fa53d4a6965e01f7ad620f9d371c61aef920611ee1.jpg)

![](images/4b4f5c24430fc345ae89b3ebdff8a0c8ab8ceefb499826eda147bec71125e346.jpg)  
TX= 3-ta p, RX= 14-ta p FFE & 1-ta p DFE

![](images/5bf148407456c5fb3a49236243896459e6b096d90cb5aebddf0942c691510e67.jpg)

• Iterati ng front-end config u ration ( DC ga i n, pea ki ng, ba ndwidth) to com pensate for a 37d B cha n nel

• Wh i le front-end ISI is red uced with h ig her ba ndwidth a nd pea ki ng, the rms noise a lso g rows

• The opti m u m ba ndwidth is genera l ly nea r or sl ig htly h ig her tha n the Nyq u ist freq uency

## Com pa rator Noise

![](images/c0384aaf0abedf44d4018de05bfefbe100a724d3fa39266c23e915c2ba8bd74b.jpg)

• Device noise ca uses ra ndom decisions even with zero i n put s i g n a l

• Noise va ria nce ca n be fou nd by fitti n g o utp ut to a Ga u ssi a n CD F as the i n put is swept a nd tra nsient noise is ena bled

• Noise ca n a lso be si m u lated with PSS+ PAC+ PNOISE, but req u i res post processi ng to fi nd IS F from sideba nd tra nsfer fu nction [ Ki m TCAS-I 2009]

## Com pa rator Metasta bi l ity

![](images/dd1db2aa14a1678854b6e03f63875d272f73cec949138f4017bb0978759852f1.jpg)

![](images/db6a80465a2c234092a10cb39fc9b1ba6feb045e675f20575a507bb1dcf4801d.jpg)

![](images/31fed6d6159bcb0fb296aaeebee42d81baeaf196dced3c1287b156b1e36a4e03.jpg)

$$
t _ { r e g } { \sim } \tau _ { c o m p } \ln \left( \frac { V _ { D D } } { V _ { i n } } \right)
$$

• Com pa rator eva l uation ti me g rows proportiona l to $\mathsf { I n } ( \mathsf { V } _ { \mathsf { i n } } { } ^ { - 1 } )$

• M etasta bi l ity occu rs when the i n put is too sma l l a nd the com pa rator doesn ’t have sufficient ti me to fu l ly eva l uate

• Th is metasta bi l ity wi ndow is a major com ponent of the com pa rator $\mathsf { V } _ { \mathsf { m i n } }$

## RX Se n sitivity & Offset Co rrectio n

• RX se n sitivity i s a fu n cti o n of th e i n p ut refe rred n o i se, offset, a nd m i n latch resol ution voltage

$\nu _ { S } ^ { p p } = 2 \nu _ { n } ^ { r m s } \sqrt { S N R } + \nu _ { \mathrm { m i n } } + \nu _ { o f f s e t ^ { \ast } }$ Typical Values : $\nu _ { n } ^ { r m s } = 1 m V _ { r m s } , \nu _ { \mathbf { m i n } } + \nu _ { o f f s e t ^ { * } } < 6 m V$

For $\mathbf { B E R } = \mathbf { 1 0 } ^ { - 1 2 } ( \sqrt { \mathbf { S N R } } = 7 ) \Rightarrow \nu _ { s } ^ { p p } = 2 0 m V _ { p p }$

• Ci rcu itry i s req u i red to red u ce i n p ut offset fro m a potentia l ly la rge u ncorrected va l ue ( > 50mV) to nea r 1 mV

![](images/95d99e8fcad0b7181a4293d40857a454b97ca8639c362fd775560228355f5f77.jpg)

## Com pa rator Offset

![](images/26d1c276b02e972c0414cab12dc5c92e9bd307e0185d85dd5b35f57652e54428.jpg)

• Th e i n p ut refe rred offset i s p ri m a ri ly a fu nction of Vth m ismatch a nd a wea ker fu n cti o n of   ( m o b i l ity) m i s m atch

$$
\sigma _ { { } _ { V _ { t } } } = { \frac { A _ { { } _ { V _ { t } } } } { \sqrt { W L } } } , \quad \sigma _ { { } _ { \Delta \beta / \beta } } = { \frac { A _ { \beta } } { \sqrt { W L } } }
$$

![](images/88f0f3e3da6eabf28360ac5a8253dbc2ae3136258c6389e0e3916077af0ec60b.jpg)

• To red uce i n put offset $2 \times ,$ we need to i ncrease a rea 4x

• Not practica l d ue to excessive a rea a nd power consu m ption

• Offset correction necessa ry to efficiently ach ieve good sensitivity

## Offset Correction Ra nge & Resol ution

• Genera l ly ci rcu its a re desig ned to ha nd le a m i n i m u m va riation ra nge of $\pm 3 \sigma$ fo r 99 . 7 % yi e l d

• Exa m ple : I n put d ifferentia l tra nsistors $\mathsf { W } { = } 4 \mu \ m , \mathsf { L } { = } 1 5 0 \ n \ m$

$$
\sigma _ { { \nu } _ { t } } = \frac { A _ { { \nu } _ { t } } } { \sqrt { W L } } = \frac { 2 . 8 m V \mu m } { \sqrt { 4 . \mu m \cdot 1 5 0 n m } } = 3 . 6 m V , \quad \sigma _ { { \Delta \beta } / \beta } = \frac { A _ { \beta } } { \sqrt { W L } } = \frac { 2 ^ { 9 } \circ \mu m } { \sqrt { 4 \mu m \cdot 1 5 0 n m } } = 2 . 6 ^ { \circ } \circ \frac { 1 } { 2 . 0 8 \cdot 1 0 8 } = 4 . 6 ^ { \circ } \sigma _ { \Delta \beta }
$$

• If we assu me (opti m istica l ly) that the i n put offset is on ly dom i nated by the i n put pa i r $\mathsf { V } _ { \mathrm { t } }$ m ismatch, we wou ld need to desig n offset co rrecti o n ci rcu itry with a ra n g e of a bo ut   1 1 mV

• If we wa nt to ca ncel with i n 1 mV we wou ld need a n offset ca ncel lation resol ution of 5 bits, resu lti ng i n a worst-case offset of

$$
1 L S B = { \frac { \mathbf { O f f s e t } \mathbf { C o r r e c t i o n R a n g e } } { 2 ^ { \mathbf { R e s o l u t i o n } } - 1 } } = { \frac { 2 2 m V } { 2 ^ { 5 } - 1 } } = 0 . 6 5 m V
$$

## Cu rrent- Mode Offset Correction Exa m ple

• D iffe re nti a l cu rre nt i nj ected i nto i n put a m pl ifier load to i nd uce a n i n p ut- refe rred offset th at ca n ca ncel the i n herent a m p l ifier offset

• Ca n be made with extended ra nge to perform l i n k ma rg i n i ng

• Passi ng a consta nt a mou nt of tota l offset cu rre nt fo r a l l th e offset setti ng s a l lows for consta nt output com mon- mode level

• Offset correction performed bot at i n p ut a m p l ifi e r a n d i n i nd ivid ua l receiver seg ments of the 2-way i nterleaved a rch itectu re

![](images/2c1d5479c25ffc6bfea4964b96e098c455f425fe07f926ba6fe8215a18763f28.jpg)

## Ca pacitive Offset Correction Exa m ple

• A ca pacitive i m ba la nce i n the sense-a m pl ifier i nterna l nodes i nd uces a n i n put- referred offset

• Pre-cha rges i nterna l nodes to a l low m o re i nteg rati o n ti m e fo r m o re i ncreased offset ra nge

• Add itiona l ca pacita nce does i ncrease sense-a m p a pertu re ti me

• Offset i s tri m m ed by sh o rti n g i n puts to a com mon- mode voltage a nd adj usti ng setti ngs u nti l a n even d istri bution of “ 1 ”s a nd “0”s a re observed

• Offset correction setti ng s ca n be sensitive to i n put com mon- mode

![](images/47bf4149b923aca1f5eac9deb3b12d94cdc07e1a4df9bbc213560b1001057389.jpg)

![](images/9a90b697012949924cf5d647f3fba4be10eea485736d3e37392cfcd7754b6694.jpg)

## O utl i n e

• Receiver pa ra meters

• T-coi l s at RX exa m ples

• Ana log front-end

• Clocked com pa rators

• Se n sitivity & offset co rrecti o n

• Dem u lti plexi ng

• PAM4 RX exa m ple

## Dem u lti plexi ng RX

• De m u lti p l exi n g a l l ows fo r lower clock freq uency re l ative to d ata rate

• G ives extra regeneration a nd pre-cha rge ti me i n com pa rators

• Need precise phase spaci ng , but not as sensitive to d uty-cycle as TX m u lti plexi ng

![](images/5662551e28086e77f258e1f7af2f903f5f0c2f73512e8536f0ddfb9bd9bd5159.jpg)

## 1 : 4 Dem u lti plexi ng RX Exa m ple

![](images/5a64cb8d550f6c02f05e88de03db78d23dd7cb35d03e440b544a5fc787cd638b.jpg)

![](images/8add0eb3711faa69c7823b9f7a0a8873324fcd3b611c1a14dcc538e614774240.jpg)

• I ncreased dem u lti plexi ng a l lows for h ig her data rate at the cost of i ncreased i n put or pre-a m p load ca pacita nce

• H ig her m u lti plexi ng factor more sensitive to phase offsets i n deg rees

## Low-Voltage Seria l I/O Tra nsceiver

![](images/57ea5aac56d2e53dbb1937dd847f0301a09e0ab23ae00e01c499ddc25f39a475.jpg)

# • Uti l i zes a h i g h TX o utp ut m u lti p l exi n g (4 : 1 ) a n d RX i n p ut m u lti p l exi n g ( 1 : 8) fa cto r fo r low-voltage operation

Y. - H . Song, R. Ba i, P . Ch ia ng, a nd S . Pa lermo, “A 0 .47-0 . 66 pJ/b it, 4 . 8-8G b/s I/O Tra nsceiver i n 65n m-C M OS , ” I EEE JSSC, vol . 48, no . 5, pp . 1 276- 1 289, May 20 1 3 .

## 1 : 8 I n put De- M u lti pl exi ng RX

![](images/fa45b9bc9c5bbd7495651fd7e6bb1bc400cb1616555a94a33a0deb6660187ee6.jpg)

• 1 : 8 i n put de- m u lti plexi ng a l lows i n put com pa rators to operate at low voltages

• I nj ecti o n - l ocked -osci l l ato r i s u sed fo r effi ci e nt m u lti- phase clock generation a nd de-skew

Y. - H . Song, R. Ba i, P . Ch ia ng, a nd S . Pa lermo, “A 0 .47-0 . 66 pJ/b it, 4 . 8-8G b/s I/O Tra nsceiver i n 65n m-C M OS , ” I EEE JSSC, vol . 48, no . 5, pp . 1 276- 1 289, May 20 1 3 .

## 0 . 47-0 . 66 pJ/ bit, 4 . 8-8G b/s G P 65 n m CMOS Prototype

![](images/76886b2395e741ed4cf3c3e68a651333d6bb46e3f96444b401518d29f12da784.jpg)

## Testi ng with 20cm FR-4 Cha n nel

![](images/93e5761aa1707bc0a7a77b54c1e2fd46dd6aa95e076dded2395ccc576a4f5f9f.jpg)

![](images/a30048e7d8dad65b0e8e14fea1eee29851338baa017ad915d025a8b67a5014b0.jpg)

<table><tr><td colspan="2">TX Power Breakdown (6.4Gb/s at 0.65V)</td></tr><tr><td>LDO &amp; Output Driver (150mVp)</td><td>793uV</td></tr><tr><td>Serializer.Pre-drivers, Clocking</td><td>933uV</td></tr><tr><td>Global Impedance Control (amortized across 9 TX)</td><td>193uW</td></tr><tr><td>TX Energy Efficieney</td><td>0.3pJb</td></tr><tr><td colspan="2">RX Power Breakdown (6.4Gb/s at 0.65V)</td></tr><tr><td>CTLE, Quantizers, ILRO</td><td>1.07mW</td></tr><tr><td>Clock Distribution</td><td>38uW</td></tr><tr><td>RX Energy Efficieney</td><td>0.17pJb</td></tr><tr><td>Total Energy Efficiency</td><td>0.47pJ/b</td></tr></table>

## • Opti ma l 0 . 47pJ/b energy efficiency ach ieved at 6 . 4G b/s

At l ow d ata rates, l ess a m o rti zati o n of stati c cu rre nt

At h ig h d ata rates, h ig h e r vo lta g e req u i red fo r se ria l izatio n ti m i n g

Y. - H . Song, R. Ba i, P . Ch ia ng, a nd S . Pa lermo, “A 0 .47-0 . 66 pJ/b it, 4 . 8-8G b/s I/O Tra nsceiver i n 65n m-C M OS , ” I EEE JSSC, vol . 48, no . 5, pp . 1 276- 1 289, May 20 1 3 .

## O utl i n e

• Receiver pa ra meters

• T-coi l s at RX exa m ples

• Ana log front-end

• Clocked com pa rators

• Se n sitivity & offset co rrecti o n

• Dem u lti plexi ng

• PAM4 RX exa m ple

## PAM4 RX Exa m ple

![](images/428ebd30f71aacc232d440827f5d3d47314a2495c667a8c5fe18991d14035c99.jpg)

• 2 b flash ADC (3 com pa rators) for PAM4 sym bol decisions

• Swept error sa m pler for PAM4 th reshold ada ptation

• Edge sa m plers provide i nformation for CDR & eq ua l ization ada pt

• CTLE & DFE ca ncel ISI

## PAM4 Sl icer Th reshold Ada ptation

![](images/beb1bd4f87d94bceef7d3ff29dd007727be9508ebfe37d9892a9c193289019da.jpg)

• Fu l ly ada ptive backg rou nd ca l i b rati o n to pos ito n s l i ce rs i n the m idd le of the PAM4 eyes

• E rror sa m pl er tracks eyes edges a nd fi nd s heig hts

![](images/6ec305bd0746a61432a0587b84b5c3f9950526ae0227f687c28af5ee3f11627b.jpg)  
[ Roshan Zamir JSSC 20 19]

## PAM4 Sl icer Th reshold Ada ptation

![](images/773246108d07188156ecf255760aa2f88d2331dd9354bf66b21475daa203c402.jpg)

## 56Gb/s PAM4 RX Test Setu p

![](images/eea95417fff3c3d32692311b45ab7c90077eb8f5a5f69ab1b6e3b42a41863c5d.jpg)

## 56G b/s PAM4 RX Measu red Resu lts

## G P 65nm Prototype

![](images/6f50933bbbf81dfc57d4c33856543cb7b5a2afac1080850e53e6f089624c0b90.jpg)  
• 20 . 8d B cha n nel  
Equalization Adaptation

![](images/9a685f9e19200a713e59068c766ff748bd706e1c5831d854be558a020409f15e.jpg)

Threshold Adaptation  
![](images/7ed9f1189cc36bfb1940c998f3bc3ba06ede5a16d5a0be9d161d2ab8f84a5bcc.jpg)  
• 4 . 6 pJ/ b

![](images/141df403908dd28ef63a7449c7a9d902b2ae4a4291dc06eaf4f99d79d3200cb5.jpg)

![](images/e7893ff783409e7713a0aaa2d39a30346b407e92d36421c94a6db7a728ebc0ab.jpg)

![](images/fa2c33383cde5f7657d8a9e43264bc407710dcfe83d20bfa9399c5bf48242f14.jpg)

## RX Ta ke-Away Poi nts

• AFE provides eq ua l ization a nd ga i n stages to opti m ize the sig na l for sym bol detection ( m ixed -sig na l RX) or q ua ntization (ADC- based RX)

• G m -TIA a nd i nverter- based front-ends a l low for h ig her ga i n with sh ri n ki ng su pply voltages

• Ach ievi ng good RX sensitivity req u i res ca refu l front-end noise a na lysis a nd sa m pler offset correction

• H ig her i n put stage dem u lti plexi ng relaxes clock freq uencies at the cost of front-end load i ng a nd clock phase generation

• PAM4 receivers req u i re extra th reshold ada ptation

## Next Ti me

Eq ua l ization theory a nd ci rcu its

Eq ua l ization overview

Eq ua l ization i m plementations

• TX FI R

• RX FI R

• RX CTLE

• RX D FE

Setti n g coefficie nts

Eq ua l ization effectiveness

Alternate/futu re a pproaches