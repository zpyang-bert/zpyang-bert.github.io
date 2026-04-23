---
layout: post
title:      "lecture13 ee720 fwd clk deskew"
date:       2026-04-18 20:13:32
author:     "Bert"
tags:
  - Lecture
  - Mineru
---

## ECEN 720 : H ig h-Speed Li n ks Ci rcu its a nd Systems Spri ng 2023

## Lectu re 1 3 : Forwa rded Clock Deskew Ci rcu its



Sa m Pa lermo Ana log & M ixed -Sig na l Center Texas A&M U n iversity

## An nou ncements

• Project Prel i m i na ry Report d ue today

• Exa m 2 Apr 25

Focuses on materia l from Lectu res 7- 14

• Previous yea rs’ Exa m 2s a re posted on the website for reference

• Project Fi na l Report d ue May 2

Project Presentations May 4 ( 1 2 : 30 PM -2 : 30 PM )

## Agenda

• Forwa rded Clock I/O Overview

• Data & Clock Skew Performa nce I m pact

• J itter I m pu l se Respo n se a nd J itter Tra n sfer Fu nction

• Forwa rded Clock Deskew Arch itectu res

• P LL/ PI

• D LL/ PI

• I LO

• Fu nda menta l, Su per- Ha rmon ic, Su b- Ha rmon ic

## Forwa rded Clock I/O Arch itectu re

Multi-Channel Serial Link System

## RX Data Channels



• Com mon h ig h-speed reference clock is forwa rded from TX ch i p to RX ch i p

• Mesoch ronous system

• Used i n processor- memory i nterfaces a nd m u lti - processor com m u n ication

• I n te l Q PI

• Hypertra nsport

• Req u i res one extra clock cha n nel

• “Coherent” clocki ng a l lows lowto- h i g h freq u e n cy j itte r tra cki n g

• Need good clock receive a m pl ifier as the forwa rded clock is atten uated by the cha n nel

## Forwa rded Clock I/O Li m itations

Multi-Channel Serial Link System  


• Clock skew ca n l i m ited forwa rd clock I/O performa nce

• Driver strength a nd load i ng m ismatches

• I ntercon nect length m ismatches

## • Low pass cha n nel ca uses j itter a m p l ifi cati o n

• Duty-Cycle va riations of forwa rded clock

## Forwa rded Clock I/O De-Skew

Multi-Channel Serial Link System  


• Per-cha n nel de-skew a l lows for sig n ifica nt data rate i ncreases

• Sa m ple clock adj usted to center clock on the i ncom i ng data eye

• I m plementations

• Delay- Locked Loop a nd Phase I nte rpo l ato rs

• I njection - Locked Osci l lators

## • Phase Acq u isition ca n be

• BER based – no add itiona l i n put phase sa m plers

• Phase detector based i m plemented with add itiona l i n put phase sa m plers period ica l ly powered on

## Forwa rded Clock I/O Ci rcu its

## Multi-Channel Serial Link System



• TX PLL

• TX Clock Distri bution

• Repl ica TX Clock Driver

• Cha n nel

• Forwa rd Clock Am pl ifier

• RX Clock Distri bution

• De-Skew Ci rcu it

• P LL/ PI

• D LL/ PI

• I njection - Locked Osci l lator

## Data & Clock Skew Performa nce I m pact

H ig h speed forwa rded clock a l l ows j itte r tra c ki n g between clock a nd data

•Clock to data skew ca uses that h ig h freq uency clock a nd data j itters become out of phase on the receiver



## I m pa ct of Cl ock to Data S kew o n J itte r Tracki ng

J itter Freq uency = 1 00 M Hz  


$$
J _ { D } = J _ { P } \sin { ( 2 \pi f _ { j } U I \cdot n ) }
$$

skew of mUI between data and clock

$$
J _ { C } = J _ { P } \sin { ( 2 \pi f _ { j } U I \cdot n + 2 m \pi f _ { j } U I ) }
$$

$$
J _ { d i f f } = J _ { D } - J _ { C }
$$

U I = 1 00 ps

Assu m i ng 5 U I skew i n th is exa m ple

## I m pa ct of Cl ock to Data S kew o n J itte r Tracki ng

J itter Freq uency = 200 M Hz  






## I m pa ct of Cl ock to Data S kew o n J itte r Tracki ng

  
The clock skew fl i ps the j itter phase of clock faster for h ig her freq uency j itte r a n d res u lts i n h i g h e r d iffe re nti a l j itte r

## I m pact of Clock to Data Skew o n J itte r Tra cki n g

• Ass u m i n g i nfi n ite j itte r tracki ng ba ndwidth (JTB)

• For a g iven skew, as the j itter freq uency i ncreases th e d iffe re nti a l j itte r i ncreases a nd become a maxi m u m of 2X

• Fo r a g ive n j itte r freq u e n cy, at a skew of $1 / ( 6 \mathsf { f } _ { \mathrm { j } } )$ th e   
system wi l l have a   
d iffe re nti a l j itte r g reate r   
tha n 1





## O pti m u m J itte r Tra cki n g fo r 200 M H z j itte r

• Li m it the JTB by atten uati ng the clock j itter usi ng a m pl itude response of low pass fu nction with pole freq uency = JTB

$J _ { C } = J _ { P } ^ { \prime } \sin \left( 2 \pi f _ { j } U I \cdot n + 2 m \pi f _ { j } U I \right)$

• $\begin{array} { r } { J _ { P } ^ { \prime } = J _ { P } | \frac { 1 } { 1 + \frac { j f _ { j } } { J T B } } | } \end{array}$

I n 1 0G b/s system , U I = 1 00 ps

Control la bl e JTB over 70 - 800 M Hz is desi red



## J itte r I m p u l se Respo n se(J I R) a n d J itte r Tra n sfe r Fu nction (JTF) Ana lysis Method

• J I R : test th e syste m respo n se o n j itte r

• JTF : rati o of o utp ut to i n p ut j itte r a s a fu n cti o n of freq u e n cy, DTFT of JIR

Extraction of J I R i n ½ rate system where both clock edges a re usi ng



Idea l clock waveform su peri m posed with clock i ncorporati ng j itter i m pu l se sti m u l u s

Output clock waveforms usi ng idea l clock versu s j itter i m pu l se clock

J itter i m pu l se response

• A clock system ’s effect on a n i n put j itter seq uence ca n be eva l uated by convolvi ng the j itter seq uence with the j itter i m pu lse response

## Fi lter/Am pl ifier Freq uency Response & J itter Tra nsfer Response



• Low- pass freq uency response ( b u ffe r, d i stri b uti o n i nte rco n n ect) i s s i m i l a r to a h i g h - pa ss j itte r fi lte r

• H i g h freq u e n cy j itte r i s a m p l ifi ed

• H ig h- pass freq uency response (AC co u p l i n g ca p) i s s i m i l a r to a n a l l - pa ss j itte r fi lte r, exce pt fo r Nyq u i st- rate j itte r (d uty cyc l e e rro r)

• Ba nd - pass freq uency response ( ba n d - pa ss fi lte r) i s s i m i l a r to a l ow- pa ss j itte r fi lte r with th e center freq uency a l ig ned with the fu nda menta l clock freq uency

## J itte r Am p l ifi cati o n

• Low- pass freq uency response ( buffer, d istri bution i nte rco n n ect) i s s i m i l a r to a h i g h - pa ss j itte r fi lte r

• H ig h freq u e n cy j itte r i s a m p l ified a s it p ro pa g ates across the cha n nel





## PLL or DLL/PI Forwa rded Clock Deskew

• TX clock is forwa rded a long a n i ndependent cha n nel to the RX ch i p where it is d istri buted to the RX cha n nels



• The PLL or DLL locks onto the forwa rded clock a nd serves as a m u lti - phase g e n e rato r a n d a j itte r fi lte r

• The PI m ixes the phases to prod uce sa m pl i ng clocks at th e o pti ma l p ha se fo r maxi m u m ti m i ng ma rg i n or BER

## PLL/PI Forwa rded Clock Deskew Exa m ple

  
[ Prete ISSCC 2006]

## • Fu l ly buffered DI M M tra nsceiver

## PLL/PI Forwa rded Clock Deskew Exa m ple

## • P LL l ow- pa ss j itte r tra n sfe r c h a ra cte ri sti c fi lte rs h i g h freq u e n cy j itte r

Des i red fo r u n co rre l ated j itte r

N ot d esi red fo r co rre l ated h ig h freq u e n cy j itte r



## • PLL d isadva ntages

• J itter accu m u l ation i n VCO

• Sta b i l ity

3:0> • More a rea a nd com plex tha n DLL i m plementations

## DLL/PI Forwa rded Clock Deskew Exa m ple

## • D LL d isplays a n a l l - pass j itter tra nsfer fu nction

Des i red fo r co rre l ated j itte r

N ot d es i red fo r u n co rre l ated j itte r



## • DLL adva ntages

N o j itter accu m u l atio n

I n herently sta ble

• Si m pler a nd less a rea tha n PLL

## • Fi n ite ba ndwidth of DLL rded d e l ay l i n e ca n res u lt i n ock j itte r a m p l ifi cati o n

## I njection Locki ng i n LC Ta n ks

a ) a fre e - ru n n i n g os c i l l ato r cons isti ng of a n id ea l positive feed back a m pl ifier a nd a n LC ta n k;

b ) we i n s e rt a p h as e s h i ft i n the loop . We know th is wi l l ca use th e osci l l ation   
freq u e n cy to s h ift s i n ce th e loop ga i n has to   
have exactly 2 π p hase s h ift (o r m u l t i p l e s ) .

  
(a)

  
(b)



  
(d)

## Phase Sh ift for I njected Sig na l

• Assu me th e osci l l ator “locks” onto th e i nj ected cu rre nt a nd osci l l ates at th e sa me freq u e n cy.

• S i n ce th e l ocki n g s i g n a l i s n ot i n g e n e ra l at th e reson a nt ce nte r freq u e n cy, th e ta n k i ntrod u ces a p hase s h ift

• I n o rd e r fo r t h e os c i l l ato r l o o p g a i n to b e e q u a l to u n ity with ze ro p h ase s h ift, th e s u m of th e cu rre nt of th e tra n s i sto r a n d th e i nj ected cu rre nts m ust have th e p rope r p hase s h ift to com pe nsate for th e ta n k p hase s h ift.



Source: [Razavi]

## I njection Locked Osci l lator Phasors

$\phi _ { 0 } =$ Tank impedance phase shift

Phase shift between inj ected clock and output signal



N ote that th e freq u e n cy of th e i nj ection s ig n a l d ete rm i n es th e extra p hase s h ift $\Phi _ { 0 }$ of th e ta n k. Th is is fixed by th e freq u e n cy offset.

 Th e cu rre nt from th e tra ns istor is fed by th e ta n k voltage , wh i ch by d efi n ition th e ta n k cu rre nt ti mes th e ta n k i m ped a n ce , wh i ch i ntrod u ces $\Phi _ { 0 }$ betwee n th e ta n k cu rre nt/voltage .

 Th e a ng l e betwee n th e i nj ected cu rre nt a nd th e osci l l ator cu rre nt  θ m ust be su ch that th e i r su m a l ig ns with th e ta n k cu rre nt.

## I njection Geometry

$$
\begin{array} { r } { \sin \phi _ { 0 } = \frac { B } { I _ { t a n k } } } \\ { \cos ( \pi / 2 - \theta ) = \sin ( \theta ) = \frac { B } { I _ { t n j } } } \\ { \sin \phi _ { 0 } = \frac { I _ { \mathrm { i n j } } } { I _ { t a n k } } \sin ( \theta ) } \\  \sin \phi _ { 0 } = \frac { I _ { \mathrm { i n j } } \sin ( \theta ) } { \left| I _ { 0 \mathrm { e } } e ^ { j \theta } + I _ { \mathrm { i n j } } \right| } = \frac { I _ { \mathrm { i n j } } \sin ( \theta ) } { \sqrt { I _ { 0 \mathrm { e } } + I _ { \mathrm { i n j } } ^ { 2 } + 2 \cos \theta I _ { \mathrm { o n } } I _ { i n j } } } \sqrt { \displaystyle \sum _ { I _ { 0 \mathrm { i n j } } } ^ { I _ { \mathrm { o n } } } \int _ { I _ { 0 \mathrm { i n j } } } ^ { I _ { \mathrm { o n } } } \int _ { I _ { 0 \mathrm { i n j } } } ^ { I _ { \mathrm { o n } } } \int _ { I _ { 0 \mathrm { i n j } } } ^ { I _ { \mathrm { o n } } } \int _ { I _ { 0 \mathrm { i n j } } } ^ { I _ { \mathrm { o n } } } \int _ { I _ { 0 \mathrm { i n j } } } ^ { I _ { \mathrm { o n } } } \int _ { I _ { 0 \mathrm { i n j } } } ^ { I _ { \mathrm { o n } } } \int _ { I _ { 0 \mathrm { i n j } } } ^ { I _ { \mathrm { o n } } } \mathrm { d } I _ { 0 \mathrm { i n j } } } \end{array}
$$

Th e geometry of th e p rob l e m i m pl i es th e fol lowi ng constra i nts on th e i nj ected cu rre nt a m pl itu d e re l ative to th e osci l l ation a m pl itu d e .

## Locki ng Ra nge

$$
\begin{array} { l } { \sin \phi _ { \mathrm { 0 } } = \displaystyle \frac { I _ { i n j } } { I _ { T } } \sin \theta = \frac { I _ { i n j } \sin \theta } { \sqrt { I _ { o s c } ^ { 2 } + I _ { i n j } ^ { 2 } + 2 I _ { o s c } I _ { i n j } \cos \theta } } } \\ { \Rightarrow \sin \phi _ { \mathrm { 0 , m a x } } = \frac { I _ { i n j } } { I _ { o s c } } , i f . \cos \theta = - \frac { I _ { i n j } } { I _ { o s c } } } \end{array}
$$

A s e co n d ‐ o rd e r p a ra l l e l ta n k co n s i st i n g of L . C, R p ex h i b i ts a p h a s e s h i ft of :

$$
\begin{array} { l } { { \displaystyle { \phi _ { 0 } = \frac { \pi } { 2 } - \tan ^ { - 1 } ( \frac { L \cdot \omega } { R _ { p } } \cdot \frac { \omega _ { 0 } ^ { 2 } } { \omega _ { 0 } ^ { 2 } - \omega ^ { 2 } } ) } } } \\ { { \displaystyle { : \omega _ { 0 } ^ { 2 } - \omega ^ { 2 } \approx 2 \omega _ { 0 } ( \omega _ { 0 } - \omega ) , \frac { L \cdot \omega } { R _ { p } } = \frac { 1 } { Q } , \frac { \pi } { 2 } - \tan ^ { - 1 } ( x ) = \tan ^ { - 1 } ( x ^ { - 1 } ) } } } \\ { { \displaystyle { : \tan \phi _ { 0 } \approx \frac { 2 Q } { \omega _ { 0 } } ( \omega _ { 0 } - \omega ) } } } \\ { { \displaystyle { \mathrm { : t a n ~ } \phi _ { 0 } = \frac { I _ { i n f } } { I _ { T } } , I _ { T } = \sqrt { I _ { a c } ^ { 2 } - I _ { i n f } ^ { 2 } } } } } \end{array}
$$

  
Sou rce : Razavi

At the edge of the lock ra nge , the i nj ected cu rre nt is orthogon a l to th e ta n k cu rre nt.

The p hase a ng l e betwee n the i nj ected cu rre nt a nd the osci l l ator is $9 0 ^ { \circ } + \Phi _ { 0 , \operatorname* { m a x } }$

## Locki ng Ra nge

$$
\begin{array} { r l } & { \Theta \xrightarrow { I _ { \mathcal { N } } } \frac { \mathcal { Z } _ { \omega } } { I _ { \mathcal { N } } } \le \frac { 2 Q } { \omega _ { \delta } } ( \omega _ { \delta } - \omega ) } \\ & { \xrightarrow { I _ { \mathcal { N } _ { \omega } } } - \frac { I _ { \mathcal { N } _ { \omega } } } { I _ { \mathcal { N } } } - \frac { I _ { \mathcal { N } _ { \omega } } } { I _ { \mathcal { N } _ { \omega } } } \xrightarrow { I _ { \mathcal { N } _ { \omega } } } - \frac { 1 } { \sqrt { 1 - \frac { I _ { \mathcal { N } _ { \omega } } ^ { 2 } } { I _ { \mathcal { N } _ { \omega } } ^ { 2 } } } } } \\ & { \xrightarrow { I _ { \mathcal { N } _ { \omega } } } - \frac { 1 } { \sqrt { 1 - \frac { I _ { \mathcal { N } _ { \omega } } ^ { 2 } } { I _ { \mathcal { N } _ { \omega } } ^ { 2 } } } } \xrightarrow { \infty } \frac { 2 Q } { \omega _ { \delta } } ( \omega _ { \delta } - \omega ) } \\ & { \Rightarrow \omega _ { 0 } - \omega _ { \delta } \sim \frac { 2 Q } { 2 Q } \xrightarrow { I _ { \mathcal { N } _ { \omega } } } \frac { 1 } { I _ { \mathcal { N } _ { \omega } } } \xrightarrow { I _ { \mathcal { N } _ { \omega } } } \frac { 1 } { \sqrt { 1 - \frac { I _ { \mathcal { N } _ { \omega } } ^ { 2 } } { I _ { \mathcal { N } _ { \omega } } ^ { 2 } } } } } \end{array}
$$

$$
I _ { i n j } < < I _ { o s c }
$$

$$
\omega _ { { \scriptscriptstyle \Delta } , L } = \omega _ { 0 } - \omega _ { i n j } \approx \frac { \omega _ { 0 } } { 2 Q } \cdot \frac { I _ { i n j } } { I _ { o s c } }
$$

$$
\begin{array} { l } { { W h e n : \omega _ { \scriptscriptstyle 0 } = 1 0 G H z , Q = 5 , K = \frac { I _ { i n j } } { I _ { o s c } } = 0 . 1 } } \\ { { \Rightarrow \omega _ { \scriptscriptstyle \Delta , L } \approx 1 0 0 M H z } } \end{array}
$$

Locki ng ra nge is i nversely proportiona l to osci l lator Q

## D i g ita l Co ntro l l ed Osci l l ato r ( DCO) with I nj ecti o n Loc ki n g



  
S h e khar, S u d i p et a l , “Strong I nj ection Locki ng i n Low-Q LC Osci l l ators : M od e l i ng a nd Ap pl i cation i n a Forwa rd ed-Clocked I/O Receiver” , I E E E J SSC , 2009 .

Th e d ig ita l ly control l ed switch-ca pacitor ba n k tu n es th e free-ru n n i ng freq u e n cy of DCO to adj ust the p hase of the forwa rd ed clock a nd a lso com pensate for PVT.

## Ri ng Osci l lator I LO Exa m ple



## Ri ng Osci l lator I LO Exa m ple





## I LO J itte r Tra n sfe r

• I LOs have a fi rst-order low- pass $J T F _ { _ { I N P U T } } = \frac { 1 } { 1 + \displaystyle \frac { s } { \omega _ { P } } }$   
fi lte r fu n cti o n to i n p ut ( i nj ecti o n   
c l oc k) j itte r

• I LOs have a fi rst-order h ig h - pass fi lte r fu n cti o n to VCO j itte r

$$
\begin{array} { c } { { \displaystyle { J T F _ { \scriptscriptstyle { V C O } } = \frac { \displaystyle { \frac { s } { \omega _ { P } } } } { 1 + \frac { s } { \omega _ { P } } } } } } \end{array}
$$

where $\omega _ { \mathrm { { P } } }$ i s the j itter tracking bandwidth : $\omega _ { \mathrm { p } } = \sqrt { \frac { K ^ { 2 } } { A ^ { 2 } } - \Delta \omega ^ { 2 } }$

For a parallel RLC resonant tank : $A = \frac { 2 Q } { \omega _ { o } }$

$\Delta \omega$ is a function of the desired de - skew phase : $\theta _ { \mathrm { s s } } \approx \mathrm { s i n } ^ { - 1 } \bigg ( \frac { A } { K } \Delta \omega \bigg )$

## I LO J itte r Tra n sfe r



$$
J T F _ { _ { I N P U T } } = \frac { 1 } { 1 + \displaystyle \frac { s } { \omega _ { P } } }
$$

$$
\omega _ { \mathrm { p } } = \sqrt { \frac { K ^ { 2 } } { \boldsymbol { A } ^ { 2 } } - \Delta \omega ^ { 2 } }
$$

$$
\theta _ { \mathrm { s s } } \approx \mathrm { s i n } ^ { - 1 } \bigg ( \frac { A } { K } \Delta \omega \bigg )
$$

[ Hossain JSSC 2009]

• I LO j itter tra nsfer ba ndwidth decreases as the osci l l ato r i s l ocked fu rth e r fro m th e free- ru n n i n g freq uency, $\mathfrak { O } _ { 0 } ,$ to o bta i n a l a rg e r p h a se s h ift $\theta _ { s s }$

## I LO J itte r Tra n sfe r



$$
J T F _ { _ { I N P U T } } = \frac { 1 } { 1 + \displaystyle \frac { s } { \omega _ { P } } }
$$

$$
\omega _ { \mathrm { p } } = \sqrt { \frac { K ^ { 2 } } { \boldsymbol { A } ^ { 2 } } - \Delta \omega ^ { 2 } }
$$

$$
\theta _ { \mathrm { s s } } \approx \mathrm { s i n } ^ { - 1 } \bigg ( \frac { A } { K } \Delta \omega \bigg )
$$

[ Hossain JSSC 2009]

• I LO j itte r tra n sfe r ba n dwidth i n crea ses with i nj ecti o n stre n gth

## I LO J itte r Tra n sfe r



$$
J T F _ { _ { I N P U T } } = \frac { 1 } { 1 + \displaystyle \frac { s } { \omega _ { P } } }
$$

$$
\omega _ { \mathrm { p } } = \sqrt { \frac { K ^ { 2 } } { \boldsymbol { A } ^ { 2 } } - \Delta \omega ^ { 2 } }
$$

$$
\theta _ { \mathrm { s s } } \approx \mathrm { s i n } ^ { - 1 } \bigg ( \frac { A } { K } \Delta \omega \bigg )
$$

[ Hossain JSSC 2009]

• I LO j itte r tra n sfe r ba n dwidth i n crea ses with i nj ecti o n stre n gth

## I LO Phase N oise Fi lteri ng

$$
S _ { o u t } = \left| J T F _ { i n p u t } \right| ^ { 2 } S _ { i n j } + \left| J T F _ { V C O } \right| ^ { 2 } S _ { V C O }
$$

$$
S _ { o u t }  { \left( \omega _ { j i t t e r } \right) } = \frac { \omega _ { P } ^ { 2 } S _ { i n j } + \omega ^ { 2 } S _ { V C O } } { \omega _ { P } ^ { 2 } + \omega ^ { 2 } } = \frac { \left( \displaystyle \frac { K } { A } \right) ^ { 2 } \cos ^ { 2 } { \theta _ { s s } } S _ { i n j } + \omega ^ { 2 } S _ { V C O } } { \left( \displaystyle \frac { K } { A } \right) ^ { 2 } \cos ^ { 2 } { \theta _ { s s } } + \omega ^ { 2 } }
$$



• U p to j itte r tra c ki n g ba ndwidth, I LO output phase noise is dom i nated by i njection clock

Ca n be better tha n VCO

• JTB depends on desi red de-skew phase

• At h ig h freq uencies, VCO phase noise dom i nates

## Ri ng Osci l lator Su per- Ha rmon ic I LO Exa m ple

• Potentia l system a ppl ication

• ½ rate TX forwa rd s clock to ¼ rate RX



$$
f _ { o s c } = m f _ { i n j }
$$

H ere m  0 . 5

[ Hossain JSSC 2009]

## Su per- Ha rmon ic I LO Phase Noise Fi lteri ng



• Low freq uency phase n o i se i s a ctu a l ly bette r th a n i nj ecti o n osci l l ato r by $\mathsf { m } ^ { 2 }$

$$
S _ { o u t } \big ( \omega _ { j i t t e r } \big ) = \frac { m ^ { 2 } \bigg ( \displaystyle \frac { K } { A } \bigg ) ^ { 2 } \cos ^ { 2 } m \theta _ { s s } S _ { i n j } + \omega ^ { 2 } S _ { V C O } } { \bigg ( \displaystyle \frac { K } { A } \bigg ) ^ { 2 } \cos ^ { 2 } m \theta _ { s s } + \omega ^ { 2 } }
$$

![](/img/mineru_output/lecture13_ee720_fwd_clk_deskew/auto/images/01cce1a82ec801cfb077dff7c2cd687c4279d6c6700a9a4248740fdf743a2ec3.jpg)

## Ri ng Osci l lator Su b- Ha rmon ic I LO Exa m ple w/ Clock Sig na l I njection

• Forwa rd i ng a lower speed clock avoids j itter a m pl ification over low- pass cha n nel

• Su b- Ha rmon ic i nj ecti o n with c l oc k sig na l ca n ca use si g n ifi ca nt I LO a m pl itude va riations a nd su b- ha rmon ic spu riou s tones



## Ri ng Osci l lator Su b- Ha rmon ic I LO Exa m ple w/ Pu lse Tra i n Sig na l I njection

• Forwa rd i ng a pu l se tra i n sig na l red uces a m pl itude va riations a nd I LO spu rious tones

• Adj u sti ng pu l se width, d, cha nges effective i nj ecti o n strength a nd ca n be u sed to adj u st j itte r tra c ki n g ba ndwidth



## Effective I njection Strength of Pu l se Tra i n



Injection strength of ${ \mathsf { n } } _ { \mathsf { t h } }$ harmonic → $K _ { n } = { \frac { 4 A } { N T } } \mathrm { s i n } \Bigg ( { \frac { n \pi d } { N T } } \Bigg )$

[ Hossain ISSCC 20 10]



• Wider pu lse sepa ration (lower freq uency su bha rmon ics) red uces effective i njection strength

## Adj usti ng J itter Tracki ng Ba ndwidth w/ Pu l se Tra i n Sig na l





• Wider pu lse sepa ration (lower freq uency su b- ha rmon ics) red uces effective i njection strength a nd resu lts i n lower j itte r tra c ki n g ba n d wi dth

• Red uci ng pu lse width, d, for a g iven spaci ng red uces effective i nj ecti o n stre n gth a n d res u lts i n l owe r j itte r tracki ng ba ndwidth

## Phase Drifts with I LO- Based Clocki ng



• Voltage a nd tem peratu re va riations ca n ca use the TX/RX I LOs’ free ru n n i ng freq uency to cha nge, a nd th us the p ha se re l atio n sh i p ca n d rift with ti m e

## Low-Overhead CDR w/I LO- Based De-Skew



• I ntrod uci ng a low-overhead CDR i nto a forwa rded -clock system a l lows tracki ng of low-freq uency phase d rifts, wh i le m a i nta i n i n g co rre l ated j itte r tra c ki n g

## M u lti - Phase E rrors at Low VD D



## Edge- Rotati ng 5/4X Su b- Rate CDR



• An add itiona l period ica l ly rotati ng edge sa m pler provides the 4-eye phase i nformation to CD R l og ic

• Al lows tracki ng of phase d rift a n d o pti m i zati o n of each sa m pler ti m i ng ma rg i n

## 14Gb/s G P 65 n m CMOS Prototype

## Tracking Non-U niform Eyes





## Correlated J itter Tolera nce



<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[2]</td><td rowspan=1 colspan=1>[3]</td><td rowspan=1 colspan=1>[4]</td><td rowspan=1 colspan=1>This Work</td></tr><tr><td rowspan=1 colspan=1>VDD, Process</td><td rowspan=1 colspan=1>1.0V/65nm</td><td rowspan=1 colspan=1>1.25V/90mm</td><td rowspan=1 colspan=1>1.08V/32mm</td><td rowspan=1 colspan=1>0.8V/65mm</td></tr><tr><td rowspan=1 colspan=1>Data Rate</td><td rowspan=1 colspan=1>6.4Gb/s</td><td rowspan=1 colspan=1>8Gb/s</td><td rowspan=1 colspan=1>16Gb/s</td><td rowspan=1 colspan=1>14Gb/s</td></tr><tr><td rowspan=1 colspan=1>Clock Rate</td><td rowspan=1 colspan=1>3.2GHz</td><td rowspan=1 colspan=1>2GHz</td><td rowspan=1 colspan=1>4GHz</td><td rowspan=1 colspan=1>3.5GHz</td></tr><tr><td rowspan=1 colspan=1>Clock Arch.</td><td rowspan=1 colspan=1>FC</td><td rowspan=1 colspan=1>Embedded</td><td rowspan=1 colspan=1>FC</td><td rowspan=1 colspan=1>FC</td></tr><tr><td rowspan=1 colspan=1>Multi-phase Gen.</td><td rowspan=1 colspan=1>PLL/PI</td><td rowspan=1 colspan=1>DLL</td><td rowspan=1 colspan=1>ILO/PI</td><td rowspan=1 colspan=1>ILO/PI</td></tr><tr><td rowspan=1 colspan=1>RX FOM*(Excludes PLL)</td><td rowspan=1 colspan=1>3.9pJ/bit*</td><td rowspan=1 colspan=1>1.59pJ/bit*</td><td rowspan=1 colspan=1>1.02pJ/bit</td><td rowspan=1 colspan=1>0.56pJ/bit</td></tr></table>

U ncorrelated J itter Tolera nce  


## O pti m u m J itte r Tra cki n g fo r 200 M H z j itte r

• Li m it the JTB by atten uati ng the clock j itter usi ng a m pl itude response of low pass fu nction with pole freq uency = JTB

• $J _ { C } = J _ { P } ^ { \prime } \sin \left( 2 \pi f _ { j } U I \cdot n + 2 m \pi f _ { j } U I \right)$

• $\begin{array} { r } { J _ { P } ^ { \prime } = J _ { P } | \frac { 1 } { 1 + \frac { j f _ { j } } { J T B } } | } \end{array}$

$$
\begin{array} { l } { \displaystyle \mathrm { I n \ 1 0 G b / s \ s y s t e m } , } \\ { \displaystyle \mathrm { U I } = 1 0 0 \mathsf { p s } } \end{array}
$$

Objective : I m plement o pti m a l JTB th at yi e l d s m i n i m u m d iffe re nti a l j itte r

Control la bl e JTB over 70 - 800 M Hz is desi red



## U ndersta nd i ng of J itter Red uction usi ng Ba nd pass Fi lteri ng

• Ti me Doma i n J ittery Clock Expression :

$$
c ( t ) = A c o s ( 2 \pi f _ { c } t + \beta s i n 2 \pi f _ { m } t )
$$

$\beta$ : phase noise a m pl itude; $f _ { m }$ : J itte r freq u e n cy

• Freq uency Doma i n J ittery Clock Expression :

$$
C ( f ) \approx \frac { A } { 2 } \delta ( f - f _ { c } ) - \frac { \beta A } { 4 } [ \delta ( f - f _ { L } ) - \delta ( f - f _ { H } ) ]
$$





## U ndersta nd i ng of J itter Red uction usi ng Ba nd pass Fi lteri ng

• The spectru m of received clock after fi lteri ng

$$
\begin{array} { r } { S ( f ) = \frac { \alpha _ { c } A } { 2 } \delta ( f - f _ { c } ) - \frac { \beta A } { 4 } [ \alpha _ { L } \delta ( f - f _ { L } ) - \alpha _ { H } \delta ( f - f _ { H } ) ] } \end{array}
$$

$\alpha _ { \mathrm { c } } , \alpha _ { \mathrm { L } }$ a nd $\alpha _ { \mathrm { H } }$ a re the ga i n of the ba nd pass fu nction at $\mathrm { f } _ { \mathrm { c } } , \mathrm { f } _ { \mathrm { L } }$ a n ${ \mathsf { d f } } _ { \mathrm { H } }$

• Received clock expression i n ti me doma i n :

$$
s ( t ) = A _ { r } c o s ( 2 \pi f _ { c } t + \beta _ { r } s i n 2 \pi f _ { m } t )
$$

• Phase noise a m pl itude of the received clock

$$
\beta _ { r } \approx ( \frac { \alpha _ { L } + \alpha _ { H } } { 2 \alpha _ { c } } ) \beta
$$

• For typica l ba nd pass fi lteri ng , $\alpha _ { \mathrm { c } } \geq$ 1 a nd $\alpha _ { \mathrm { L } } = \alpha _ { \mathrm { H } } < \alpha _ { \mathrm { c } }$ . Th u s, $\beta _ { \mathrm { r } } <$ β a nd the j itter of the tra nsm itted clock is red uced by ba nd pass fi l te ri n g

## U ndersta nd i ng of J itter Red uction usi ng Ba nd pass Fi lteri ng

• Ba nd pass fu nction is sym metrica l a nd center at $\mathrm { f } _ { \mathrm { c } } ,$ th e tra n sfe r fu nction ca n be expressed as a low- pass fu nction with respect to the freq uency offset from $\mathrm { f } _ { \mathrm { c } } ,$

$$
H \big ( j 2 \pi ( f _ { c } - f ) \big ) = H \big ( j 2 \pi ( f _ { c } + f ) \big ) = \frac { | H ( j 2 \pi f _ { c } ) | } { 1 + \frac { j f } { f _ { p } } }
$$

?? : the offset freq uency from $f _ { c } ; \mathrm { \Delta B W _ { 3 d B } }$ : ba ndwidth of ba nd pass fi lter

$$
f _ { p } = ( 1 / 2 ) B W _ { 3 d B }
$$

• JTF of ba n d pa ss fi lte ri n g :

$$
J T F _ { B P } ( j 2 \pi f ) = \frac { \beta _ { r } } { \beta } ( j 2 \pi f ) = \frac { H \big ( j 2 \pi ( f _ { c } - f ) \big ) + H \big ( j 2 \pi ( f _ { c } + f ) \big ) } { 2 H ( j 2 \pi f _ { c } ) } = \frac { 1 } { 1 + \frac { j f } { f _ { p } } }
$$

## Ana lysis of Ba nd pass J itter Fi lteri ng Based on J I R a nd JTF



  
• Tra n s m itted j itte r exh i b its l ow- pa ss tra n sfe r cha racteristic th roug h ba nd - pass cha n nel

• Received h ig h freq uency u ncorrelated j itter ca n be red uced by a ba nd pass fi lter

## O pti m u m J itter Tracki n g with Ba nd pass Fi l te ri n g

• H ig h e r Q of ba n d pa ss fi lte ri n g , sma l l e r ba n dwidth , h ig h e r j itte r fi l te ri n g

$$
\begin{array} { c } { { J T F _ { B P } ( j 2 \pi f ) = \displaystyle { \frac { 1 } { 1 + \frac { j f } { f _ { p } } } } } } \\ { { f _ { p } = ( 1 / 2 ) B W _ { 3 d B } } } \end{array}
$$



## O pti m u m J itter Tracki n g with Ba nd pass Fi l te ri n g

• Apply J I R a nd JTF a na lysis to q ua ntify the i m pact of Q on JTB of 5G Hz clock, U I = 1 00 ps



Q tu n i ng ra nge over 3 -30 provides JTB ra nge over 97 – 790 M Hz

To ach ieve JTB of 70 M Hz to opti m ize j itte r tra c ki n g with 1 0 U I clock skew, h ig her Q is req u i red .

## Ba nd pass Fi lter for Forwa rded -Clocks

SW1..SW4





## Ba n d pa ss Fi lte r J itte r Fi lte ri n g

  
Fig. 20 Simulated impact of the proposed bandpass flter cireuit on random jitter

  
Fig, 21 Simulated impact of the proposed andpas flter circuit on DCD

  
Fig, 22 Simulated impact of the proposed bandpass fiter cireuit on a sinusoidal jiter component

• Ba n d pa ss fi lte r i s effective i n fi lte ri n g h i g h -freq u e n cy j itte r

• Low- m axi m u m Q of th e fi lte r (Q = 2 . 6) l i m its tu n i n g to low-freq uency j itter tracki ng ba ndwidths

Li m ited by the passive i nd uctor Q

## Next Ti me

• Clock Distri bution Tech n iq ues