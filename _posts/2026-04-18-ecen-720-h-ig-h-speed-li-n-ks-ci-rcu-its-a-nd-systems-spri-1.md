---
layout: post
title:      "ECEN 720 : H ig h-Speed Li n ks Ci rcu its a nd Systems Spri ng 2023"
date:       2026-04-18 21:29:11
author:     "Bert"
tags:
  - Lecture
  - Mineru
  - RX
---
Lectu re 8 : RX FI R, CTLE, DFE, & Ada ptive Eq .

![](images/bba043e49c7218136079e95a21da8983d372f31a4d6c4597e04ced4d4855e50a.jpg)

Sa m Pa lermo Ana log & M ixed -Sig na l Center Texas A&M U n iversity

## An nou ncements

• La b 5 Report a nd Prela b 6 d ue Ma r 27

Eq ua l ization overview a nd ci rcu its pa pers a re posted on the website

## Agenda

RX FI R eq ua l ization

• RX CTLE eq ua l ization

• RX DFE eq ua l ization

Eq ua l ization ada ptation tech n iq ues

• Adva nced mod u lation/other tech n iq ues

## Li n k with Eq ua l ization

![](images/1840d8313172536d92439ec49b5104d1b52d527ba097dfb5a630f7f0f5aa90e5.jpg)

## TX FI R Eq ua l ization

• TX FI R fi lte r p re-d i sto rts tra n s m itted p u l se i n o rd e r to i nve rt c h a n n e l d istortion at the cost of atten uated tra nsm it sig na l (de-em phasis)

![](images/70bb56f9f913436575267b2792a39e8d8519ffbf7231c8dd6eaf9ffe553f413e.jpg)

![](images/82f1e56b4777ec8ffccb7c3322a8e2a86841b87160ca707397d00133032b6741.jpg)

![](images/7b125ada23e03bae4d9df4575610f4e7f5a12b299b39c6e37cc6d85ccb341863.jpg)

![](images/0bbbae1a1b62ac187add45256986fa959cd79b4a24d744ed58343c3c59df4d28.jpg)

![](images/e54b7afb6517e7fa3555971504035120768bc2e3a1eefc97e9619b94d8a59432.jpg)

![](images/4db710ec194e6ebf045c323840cf4b1dfcb02eb44c3fa538c4d5d11150215edb.jpg)

## RX FI R Eq ua l ization

## • Delay a na log i n put sig na l a nd m u lti ply by eq ua l ization coefficie nts

## • Pros

• With sufficient dyna m ic ra nge, ca n a m pl ify h ig h freq uency content ( rath e r th a n atte n u ate l ow freq uencies)

• Ca n ca ncel ISI i n pre-cu rsor a nd beyond fi lter spa n

• Fi lter ta p coefficients ca n be ada ptively tu ned without a ny back-cha n nel

## • Cons

Am pl ifies noise/crossta l k

I m plementation of a na log delays

• Ta p precision

![](images/9286f6730d4dd51bd068288069b6b487a4c09ea6483c5436616068fc97406b28.jpg)

## RX Eq ua l ization Noise En ha ncement

• Li nea r RX eq ua l izers don ’t d iscri m i nate between sig na l , noise, a nd cross-ta l k

• Wh i l e s i g n a l -to-d i sto rti o n ( I SI ) rati o i s i m p roved , S N R rema i ns u ncha nged

![](images/1a22335f184bf6aee786d353974cf7c005b3652d64cf7a74a05faa23b9586e5d.jpg)

## Ana log RX FI R Eq ua l ization Exa m ple

• 5-ta p eq ua l izer with ta p spaci ng of $\mathsf T _ { \mathsf { b } } / 2$

![](images/9bbb65883c0307c3258fa3b8dda20fcaf6c59a43aba4b093e8eb531643abb068.jpg)

3 rd-o rd e r d e l ay ce l l

![](images/3c40896c98b26d5a0f28b4d0429ab0659dd4c314368ed9686854b446143d5e75.jpg)  
Floating Inductor Emulator and Active Load

1 G b/s experi menta l resu lts

![](images/01c3f80999e18301a2778964c526da5c81c95436fadbc74cc44caa1364dd581f.jpg)  
Before Equalizer: 23meters

![](images/60e14ebf21c58521817e7d90ba588ea5ceff8f86e462b994b0835f3a65e9f00e.jpg)  
After Equalizer: 23meters  
D . Herna ndez-Ga rd u no a nd J . Si lva- Ma rti nez, “A CMOS 1 G b/s 5-Ta p Tra nsversa l Eq ua l izer based on 3rd-Order Delay Cel ls, " ISSCC, 2007 .

## Dig ita l RX FI R Eq ua l ization

• Dig itize the i n put sig na l with h ig h -speed low/med i u m resol ution ADC a nd perform eq ua l ization i n d ig ita l doma i n

D i g ita l d e l ays, m u lti p l i e rs, a d d e rs

Li m ited to ADC resol ution

• Power ca n be h ig h d ue to very fast ADC a nd d ig ita l fi lters

![](images/2f23302605317ec5609fe6e2bf404f3bc7b6246e347f898c3cf29fa06bd78500.jpg)

## Dig ita l RX FI R Eq ua l ization Exa m ple

![](images/306c0d3a67e4b0425e5662d3f6952c33f60cc060426d95f153485e01eb595a21.jpg)

• 1 2 . 5GS/s 4 . 5- bit Flash ADC i n 65 n m CMOS [Harwood ISSCC 2007 ]

2-ta p FFE & 5-ta p DFE

• XCVR power (i nc . TX) = 330mW, Ana log = 245 mW, Dig ita l = 85 mW

## Agenda

• RX FI R eq ua l ization

RX CTLE eq ua l ization

• RX DFE eq ua l ization

Eq ua l ization ada ptation tech n iq ues

• Adva nced mod u lation/other tech n iq ues

## Li n k with Eq ua l ization

![](images/a2e3827d775cb11dc638db0a1d1ef7828388b753cc8bd7c878950fd8de062271.jpg)

## RX Conti n uous-Ti me Li nea r Eq ua l izer (CTLE)

• Passive R-C (or L) ca n i m plement h ig h - pass tra nsfer fu nction to com pensate for cha n nel loss

• Ca ncel both precu rsor a nd long -ta i l I SI

• Ca n be pu rely passive or com bi ned with a n a m p l ifi e r to p rovi d e g a i n

![](images/7fed00200fdaf8264b54f3d9dd6916614475f57e20b63470987fbe90d4dcc2a9.jpg)

![](images/80f1a47d7c62123ba3536864edf9498e17f6a888ca8b8c7ba54e9982e33fc309.jpg)

![](images/371b10e12d1f08652f9028a66018a84014da400d15eeff8a06e930aa97d93ba1.jpg)

## Passive CTLE

Passive structu res offer excel lent l i nea rity, but no ga i n at Nyq u ist freq uency

![](images/54786ce625bec8d125a8ebf5be94edbaac1e3ec1f8b22fd3341e43acd993bdec.jpg)

$$
H ( s ) = \frac { R _ { 2 } } { R _ { 1 } + R _ { 2 } } \frac { 1 + R _ { 1 } C _ { 1 } s } { 1 + \frac { R _ { 1 } R _ { 2 } } { R _ { 1 } + R _ { 2 } } ( C _ { 1 } + C _ { 2 } ) s }
$$

$$
\omega _ { z } = \frac { 1 } { R _ { 1 } C _ { 1 } } , \quad \omega _ { \mathbf { p } } = \frac { 1 } { \frac { R _ { 1 } R _ { 2 } } { R _ { 1 } + R _ { 2 } } ( C _ { 1 } + C _ { 2 } ) }
$$

$$
\mathbf { D C } \mathbf { g a i n } = \frac { R _ { 2 } } { R _ { 1 } + R _ { 2 } } , \mathbf { H F } \mathbf { g a i n } = \frac { C _ { 1 } } { C _ { 1 } + C _ { 2 } }
$$

$$
\mathbf { P e a k i n g } = { \frac { \mathbf { H F \underbrace { g a i n } _ { } } } { \mathbf { D C \underbrace { g a i n } _ { } } } } = { \frac { \omega _ { p } } { \omega _ { z } } } = { \frac { R _ { 1 } + R _ { 2 } } { R _ { 2 } } } { \frac { C _ { 1 } } { C _ { 1 } + C _ { 2 } } }
$$

## Active CTLE

• I n p ut a m p l ifi e r with RC degeneration ca n provide freq uency pea ki ng with ga i n at Nyq u ist freq uency

• Potentia l ly l i m ited by g a i n - ba ndwidth of a m p l ifier

• Am pl ifier m ust be desig ned fo r i n p ut l i n ea r ra n g e

• Often TX eq . provides some low freq uency atten uation

• Sensitive to PVT va riations a nd ca n be ha rd to tu ne

• Ge n e ra l ly l i m ited to 1 st-o rd e r com pensation

![](images/f705a88170ab5f76857273e9411dbe326c6853550b18b1892554ceda5c87b768.jpg)  
[Gondi JSSC 2007]

![](images/381ddfd72d4e4b4dde8e6396a9557a8272af383302cac82eceb89f628a9ab529.jpg)

$$
H ( s ) = \frac { g _ { m } } { C _ { p } } \frac { s + \displaystyle \frac { 1 } { R _ { s } C _ { s } } } { \displaystyle \left( s + \frac { 1 + g _ { m } R _ { s } / 2 } { R _ { s } C _ { s } } \right) \left( s + \frac { 1 } { R _ { D } C _ { p } } \right) }
$$

$$
\omega _ { z } = \frac { 1 } { R _ { s } C _ { s } } , \omega _ { \mathbf { p } 1 } = \frac { 1 + g _ { m } R _ { s } / 2 } { R _ { s } C _ { s } } , \omega _ { \mathbf { p } 2 } = \frac { 1 } { R _ { D } C _ { p } }
$$

$\mathbf { D C } \mathbf { g a i n } = \frac { g _ { m } R _ { D } } { 1 + g _ { m } R _ { S } / 2 } ,$ , Ideal peak ${ \bf g a i n } = { g _ { m } } R _ { D }$

$$
\mathrm { I d e a l ~ P e a k i n g } = \frac { \mathrm { I d e a l ~ p e a k ~ g a i n } } { \mathrm { D C ~ g a i n } } = \frac { \omega _ { p 1 } } { \omega _ { z } } = 1 + g _ { m } R _ { s } / 2
$$

## Active CTLE Exa m ple

![](images/4fd1ba55d12b06f1459316d3a561a85f3f77703ddda4de181385cbcc080877fe.jpg)

![](images/e98ef6a97d1767ebc07afb4384254fa08b818ebc304220a2c4d492a3cd96d3b3.jpg)

![](images/3bb624a2911794c62ad1e5705a9328a8a9fc1f19fb30af8251665d688515f44f.jpg)

![](images/94a6badca2f506f20ec128cc59192d45e627f9cb8bd3ed42e10ea46612281056.jpg)

## Active CTLE Tu n i ng

• Tu ne degeneration resistor a nd ca pacitor to adj ust zero freq uency a nd $1 ^ { \mathsf { s t } }$ pole wh ich sets pea ki ng a nd DC ga i n

• I ncreasi ng ${ \sf C } _ { \sf S }$ moves zero a nd $1 ^ { \mathsf { s t } }$ pole to a lower freq uency w/o i m pacti ng (idea l) pea ki ng

• I ncreasi ng ${ \sf R } _ { \sf S }$ moves zero to lower freq uency a nd i ncreases pea ki ng (lowers DC ga i n)

M i n i ma l i m pact on $1 ^ { \mathsf { s t } }$ pole

![](images/4d3c92324eabe8df58b8d4be40d0386c98e8cf789dfbd3a36fc1d92eacb86982.jpg)

$$
\omega _ { z } = \frac { 1 } { R _ { s } C _ { s } } , \omega _ { \mathbf { p } 1 } = \frac { 1 + g _ { m } R _ { s } / 2 } { R _ { s } C _ { s } }
$$

## Agenda

• RX FI R eq ua l ization

• RX CTLE eq ua l ization

RX DFE eq ua l ization

Eq ua l ization ada ptation tech n iq ues

• Adva nced mod u lation/other tech n iq ues

## Li n k with Eq ua l ization

![](images/e227c0f230dd8b21f3fa1d5ff87f8d4d14e8cb80aa4e2a4abffe4112a855946e.jpg)

## RX Decision Feed back Eq ua l ization ( DFE)

• DFE is a non - l i nea r eq ua l izer

• Sl icer ma kes a sym bol d eci si o n , i . e . q ua ntizes i n put

• I SI i s th e n d i rectly su btracted from the i ncom i ng sig na l via a feed ba ck FI R fi lte r

$$
z _ { k } = y _ { k } - w _ { 1 } d _ { k - 1 } . . . - w _ { n - 1 } d _ { k - ( n - 1 ) } - w _ { n } d _ { k - n }
$$

![](images/a4fc8a3c9f813bbaa71b9aad4103a975b9c3d328efaffe0784c33a6d15a57d8b.jpg)

## RX Decision Feed back Eq ua l ization ( DFE)

## • Pros

• Ca n boost h ig h freq uency content without noise a nd crossta l k a m pl ification

• Fi lter ta p coefficients ca n be ada ptively tu ned without a ny back-cha n nel

## • Cons

Ca n not ca ncel pre-cu rsor ISI

• Cha nce for error propagation Low i n p ra cti ca l l i n ks ( B E R= 1 0- 1 2 )

• Critica l feed back ti m i ng path

• Ti m i n g of ISI su btra cti o n com pl icates CDR phase detection

![](images/cb04f131392f142f0f20badfb44a9087f98746bcd981cb7febf27151f9c9d2d2.jpg)

![](images/1f90f4c010d9908a7a1122c60a061c27b74d7501079615206bff155d21cecf10.jpg)

## DFE Exa m ple

• If on ly D FE eq ua l ization, D FE ta p coefficients shou ld eq ua l the u neq ua l ized cha n nel pu lse response va l ues $[ \mathsf { a } _ { 1 } \mathsf { a } _ { 2 } \dots \mathsf { a } _ { \mathsf { n } } ]$

• With other eq ua l ization, D FE ta p coefficients shou ld eq ua l the pre- DFE pu lse response va l ues

D F E p rovi d es fl exi b i l ity i n th e o pti m i zati o n of oth e r eq u a l ize r ci rcu its

i . e . , you ca n opti m ize a TX eq ua l izer without ca ri ng a bout the ISI terms that the DFE wi l l ta ke ca re of

$$
[ \mathsf { w } _ { 1 } \mathsf { w } _ { 2 } ] { = } [ \mathsf { a } _ { 1 } \mathsf { a } _ { 2 } ]
$$

![](images/233f34daf339dfbc91596ed9669e02c0a33d0486ab61b6be1b047bde4593cb8c.jpg)

![](images/ee317d7dd14d2b5cb873818215674f11a6505df8543700fd8973a149e88fe717.jpg)

![](images/4581fd04cfc3b723f8825aa64abd9f476916dbf7f9708eb73fa52add209536fa.jpg)

6Gb/s Eye - Refined BP Channel w/ RX DFE Eq  
![](images/e03f13ca7d5e18bfbe7fe0c739dd884679b1641606eecba22724bc11a458e1f9.jpg)

## Di rect Feed back DFE Exa m ple (TI)

## • 6 . 25G b/s 4-ta p DFE

½ rate a rc h itectu re

Ada ptive ta p a lgorith m

• Cl oses ti m i n g o n 1 st ta p i n ½ U I fo r convergence of both ada ptive eq ua l ization ta p va l ues a nd CDR

![](images/4022b351ce0d57b5361f97fef48aa90b4e9554b1e8a3a8f013bd66a1b428263c.jpg)

Feed back tap mux  
![](images/412973e6363797a565b2443f001dd940b66ceafa0ff341aed91a3875bac5ba9c.jpg)

## Di rect Feed back D FE Critica l Path

![](images/dbb1c85caa0c0c6a5976e4f4e43b814db3f8f510e93c3cfae639cba58e380434.jpg)

M ust resolve data a nd feed back i n 1 bit period • TI desig n actua l ly does th is i n ½ U I for CD R

## DFE Loop U n rol l i ng

![](images/e6547c54f00ce590cf79b53609a56b224518c161009b987ca8f79e9b1edaa939.jpg)

• I nstead of feed i ng back a nd s u btra cti n g I SI i n 1 U I

![](images/1ef1e95ddb9e53fd5790b8cacec47ada6d9890c07fc1400ac453bbeabd35f97f.jpg)

• U n rol l loop a nd pre-com pute 2 poss i b i l iti es ( 1 -ta p D F E) with adj u sta ble sl icer th reshold

![](images/d4ca9f9e564fd01f4222d3410da57c67d3393947bf06ca9497ca534d82ef3d14.jpg)

• With i ncreasi ng ta p n u m ber, com pa rator n u m ber g rows as $2 ^ { \# \tt t a p s }$

$$
\tilde { d } _ { k } = \left\{ \begin{array} { l l } { \mathrm { s g n } \big ( y _ { k } - w _ { 1 } \big ) \ " \mathbf { i f } ^ { \prime \prime } \ \tilde { d } _ { k - 1 } = 1 } \\ { \mathrm { s g n } \big ( y _ { k } + w _ { 1 } \big ) \ \cdots \mathbf { i f } ^ { \prime \prime } \ \tilde { d } _ { k - 1 } = - 1 } \end{array} \right.
$$

## DFE Resistive- Load Su m mer

![](images/790f82ca3c776ccf42046c1afa2e9e84fffa52548f5b3ec5db42c4fa7e748b7d.jpg)

• Su m mer performa nce is critica l for D FE operation

• Su m mer m ust settle with i n a certa i n level of accu racy ( > 9 5 % ) fo r ISI ca n ce l l ati o n

• Trade-off between su m mer output swi ng a nd settl i ng ti me

• Ca n resu lt i n la rge bias cu rrents for i n put a nd ta ps

## DFE I nteg rati ng Su m mer

![](images/bb0eec15ccb35ecdb0f4448988880cc9ad206a399b1daae46e68098e6cf21727.jpg)  
• I nteg rati ng cu rrent onto load ca pacita nces el i m i nates RC settl i ng ti me

• Si nce $\Delta \mathsf { T } / { \mathsf { C } } > \mathsf { R } ,$ bias cu rrent ca n be red uced for a g iven output swi ng Typica l ly a 3x bias cu rrent red uction

## Dig ita l RX FI R & DFE Eq ua l ization Exa m ple

![](images/487a57195b53e19b922ee04e6d10e522b2ba3da5bce106921c8d95a7054c6c13.jpg)

• 1 2 . 5GS/s 4 . 5- bit Flash ADC i n 65 n m CMOS [Harwood ISSCC 2007 ]

2-ta p FFE & 5-ta p DFE

• XCVR power (i nc . TX) = 330mW, Ana log = 245 mW, Dig ita l = 85 mW

## DFE with Feed back FI R Fi lter

![](images/9edd9a4f9d8250261cfca0748c08a5b6cc2288e3f42de09a7bdcfc12ce4d89b6.jpg)

• D F E with 2 -ta p FI R fi lte r i n feed ba c k wi l l on ly ca ncel ISI of the fi rst two post-cu rsors

## “Smooth ” Cha n nel

![](images/2fbe68b85a4285c26f6422f41cf313fca192fc4c4d4aa2e06001a997612750d9.jpg)

![](images/a4da65d47210db8f80fa7a13bebdce7c559e998738ab7a3eedbc9e5aabafe2c6.jpg)

• A DFE with FI R feed back req u i res ma ny ta ps to ca ncel ISI

• Smooth cha n nel long -ta i l ISI ca n be a pproxi mated as exponentia l ly decayi ng

• Exa m ples i ncl ude on -ch i p wi res a nd si l icon ca rrier wi res

## DFE with II R Feed back

## [ Li u ISSCC 2009 ]

![](images/f27fd50a15cb87c582f72a0f3148f23005c9fd317837d12983a18e2f5ed9b23e.jpg)

![](images/1bdf6b1f8f4add449c48652ff77b583734d8d7c4d5dc082e70e7b7174475bf97.jpg)

• La rge $1 ^ { \mathsf { s t } }$ post-cu rsor H 1 is ca nceled with norma l FI R feed back ta p

• S m ooth l o n g ta i l ISI fro m $2 ^ { \mathsf { n d } }$ post-cu rsor a nd beyond is ca nceled with low- pass II R feed back fi lter

• Note : cha n nel needs to be smooth (not ma ny reflections) i n order for th is a pproach to work wel l 3 1

## DFE with II R Feed back RX Arch itectu re

![](images/dd86fdba04c232a2d7789b3524c14ac5b79feec30b8eea4a3605180ffb244060.jpg)

## Merged Su m mer & Pa rtia l Sl icer

![](images/7db5b06a219f076b9b116726ec062baf353bdd3142565d0d65f0ebb2c3418700.jpg)

• I nteg rati ng su m mer with regeneration PMOS devices to rea l i ze pa rti a l s l i ce r o pe rati o n

## M e rg ed M ux & I I R Fi lte r

![](images/2cc0cce9608b7c34f690582e2e43b8e55becd1d41218381ad926eaf9c3457b23.jpg)

• Low- pass response (ti me consta nt) i m plemented by ${ \sf R } _ { \sf D }$ a nd $C _ { \mathsf { D } }$

Am pl itude control led by ${ \sf R } _ { \sf D }$ a nd $I _ { \mathsf { D } }$

• 2 U I delay i m plemented th roug h m ux to beg i n ca ncel lation at ${ 2 ^ { \mathsf { n d } } }$ post-cu rsor

## Agenda

• RX FI R eq ua l ization

• RX CTLE eq ua l ization

• RX DFE eq ua l ization

• Eq ua l ization ada ptation tech n iq ues

• Adva nced mod u lation/other tech n iq ues

## Setti ng Eq ua l izer Va l ues

• Si m plest a pproach to setti ng eq ua l izer va l ues (ta p weig hts, po l es, ze ros) i s to fix th e m fo r a specific syste m

• Choose opti ma l va l ues based on la b measu rements

• Sensitive to ma n ufactu ri ng a nd envi ron ment va riations

• An ada ptive tu n i ng a pproach a l lows the opti m ization of the eq ua l izers for va ryi ng cha n nels, envi ron menta l cond itions, a nd data rates

I m porta nt issues with ada ptive eq ua l ization

Extracti ng eq ua l ization correction (error) sig na l s

Ada ptation a lgorith m a nd ha rdwa re overhead

• Com m u n icati ng the correction i nformation to the eq ua l izer ci rcu it

## TX FI R Ada ptation Error Extraction

• Wh i le we a re ada pti ng the TX FI R, we need to measu re the response at the receiver i n put

• Eq u a l ize r a d a ptatio n (e rro r) i nformation is often obta i ned by com pa ri ng the receiver i n put versu s the desi red sym bol levels, d Lev

• Th is necessitates add itiona l sa m plers at the receiver with prog ra m ma ble th reshold levels

![](images/c71ddd50c0c7dba85690ed341f251a9781bda8e45bc369d99dd314449d07230d.jpg)  
Initial eye

![](images/df5d9a96671bc4898fc826c37b890bf8c50196071b85e85ae239bc3cef8ed467.jpg)

![](images/a792110aee7da90327d834a6c7778de5bac6cb7150cc8909753379c8f71c1c14.jpg)

## TX FI R Ada ptation Algorith m

• The sig n -sig n LM S a lgorith m is often used to ada pt eq ua l ization ta ps d ue to i m plementation s i m p l i c i ty

$$
w _ { n + 1 } ^ { k } = w _ { n } ^ { k } + \Delta _ { w } \mathrm { s i g n } ( d _ { n - k } ) \mathrm { s i g n } ( e _ { n } )
$$

w n ktap co efficients , time instant, tap index,    $d _ { n } = \operatorname { r e c e i v e d d a t a }$

e dLeverror with respect to desired data level,

• As the desi red data level is a fu n cti o n of th e tra n s m itte r swi n g a nd cha n nel loss, the desi red data level is not necessa ri ly known a nd shou ld a lso be ada pted

$$
d L e \nu _ { { } _ { n + 1 } } = d L e \nu _ { { } _ { n } } - \Delta _ { d L e \nu } \mathrm { s i g n } ( e _ { n } )
$$

![](images/85c0e4f3b52a85ab290cc21c8f339e276f8223c923fedc00702c0936e2ad28ca.jpg)

![](images/7cf26f854cd7d83b249790e62056f834c332508f0dba65f9922eb3ffa9ff7aa6.jpg)

## TX FI R Com mon- Mode Back-Cha n nel

• I n order to com m u n icate FI R ta p u pdate i nformation back to the TX, a back-cha n nel is necessa ry

• One option is to use low data rate (\~ 1 0 M b/s) com mon - mode sig na l i ng from the RX to TX on the sa me d ifferentia l cha n nel

![](images/97d06257286b8fce8a664c3ea3d328bd5cce62334ecacaad939689a4316e230b.jpg)

## TX FI R Data Encoder Back-Cha n nel

• Another option is to use a h ig h-speed TX cha n nel on the RX side that com m u n icates data back to the TX u nder ada ptation

• Flexi bi l ity i n data encod i ng (8 B 1 0 B/Q) a l lows low data rate ta p ada ptation i nformation to be tra nsm itted back without data rate overhead

![](images/96a30d56ade7991113f9c519b215aa429b3bd40c7992c903d21f884cec116a0e.jpg)  
[Stonick JSSC 2003 ]

## CTLE Tu n i ng with PSD Measu rement

• One a pproach to CTLE tu n i ng is to com pa re low-freq uency a nd h ig h-freq uency spectru m content of ra ndom data

• For idea l ra ndom data, there is a pred icta ble ratio between the low-freq uency power a nd h ig h-freq uency power

• The error between these power com ponents ca n be used i n a servo loop to tu ne the CTLE

![](images/3a30653a834a09a397dac738fd93ef3d9cfe6b163725a217e87711d9e31612e9.jpg)

$$
s _ { x } ( f ) { = } T _ { b } \Bigg [ \frac { { \sin ( \pi f T _ { b } ) } } { { \pi } f T _ { b } } \Bigg ] ^ { 2 }
$$

$$
\int _ { 0 } ^ { f _ { m } } s _ { x } \big ( f \big ) d f = \int _ { f _ { m } } ^ { \infty } s _ { x } ( f ) d f = \frac { 1 } { 4 }
$$

where $f _ { m } \approx \frac { 0 . 2 8 } { T _ { b } }$

![](images/bf475c894259d23d040ddf0a26904575115e39e06523b23050fe9c73d4de4963.jpg)  
Power Detector

## CTLE Tu n i ng w/ Output Am pl itude Measu rement

• CTLE tu n i ng ca n a lso be done by com pa ri ng low-freq uency a nd h ig hfreq uency average a m pl itude

• Approxi mati ng the eq ua l ized data as a si ne wave, a pred icta ble ratio exists between the low freq uency average a nd h ig h-freq uency average

• Eq ua l izer setti ngs a re adj usted u nti l the h ig h freq uency pea k-to- pea k swi ng matches the low-freq uency pea k-to- pea k swi ng

![](images/06f324ba32f681b3b3f3d44b92ea98fccc2dcc7103b3bcb46eee307d8c9f2f63.jpg)

![](images/f3317517127be0c1b3c36db1bfe82780a81570dae11a2340fc4aecf7cd0ba40f.jpg)

## CTLE Tu n i ng w/ Data Edge Distri bution Mon itori ng

• The width a nd sha pe of the data edge d istri bution ca n be used to rel ia bly ca l i brate a n eq ua l izer

• By oversa m pl i ng the data bits with su b- period accu racy, th is i nformation ca n be obta i ned

• Objective is to maxi m ize eye open i ng, or eq u iva lently m i n i m izi ng the sta nda rd deviation of the edge d istri bution

![](images/53de97ed2e7793db18ca7c9acf45e0b6645b3e3354d0350c37991b898600bd90.jpg)

![](images/91cbb84ee66e929670c587a3bf9c9b302fc1fe68ae0ac041cbcff24bd28012cd.jpg)

![](images/6561cbff3531ac19b02ae6895bcc0fb0c3cb5be4b2763e4a3d8bb6d4da668d9f.jpg)

![](images/5a8aa529b5b8647c5fa0e8fff9112eb710e0d6e536f3d354e0482e5ebc1a85b4.jpg)

![](images/5cc11cd318a88dd668c95477302fc94218f53cb87da7568ed5433f4d90310ccd.jpg)

![](images/69e9c88de93c5c1acb5800dcb3835339333723c04b4524f9a6b551246cc7aff8.jpg)

![](images/fe63f0d832eea9ed8f2aa6d387b6c116f0cbff8834ad4ddb496a481435434d2b.jpg)

![](images/cefda6c1b0a5f55d51ae60015d3d31c96afb9dc3a5b4e8a2f486f2fa76a7641a.jpg)

![](images/311eee54e9bc3f648009b913f67fc7c72646e175966ca61afa1b55d348aed906.jpg)

![](images/685eb6da9c7d50748003b2b14b6da3ff5d2cc59268e0af84b025dd3b5684e3f4.jpg)  
[Gerfers JSSC 2008]

## DFE Tu n i ng – FI R Feed back

![](images/3f9645249f8a393bf384710c3714bc2c6045b91eb28de7073e7e16452c0aab16.jpg)

![](images/7bb3cd67c749f2521653183e4a23c4542bc78d71b3948a63270df6a419aaf281.jpg)

![](images/5bf740652a9349a7591a653175db92022c63d651bde4f078d793eff65cba2ea4.jpg)

![](images/cc2049bd18f7943ea2c6026fefef7ede93465dd823a255b97ea40225faa40ae7.jpg)

![](images/e401603d99be1839db2018887a80b8b44f38ae6f36a4f56ed7a9f367c4cd8b51.jpg)

• 2x oversa m pl i ng the eq ua l ized sig na l at the edges ca n be used to extract i nformation to ada pt a DFE a nd d rive a CDR loop

Sig n-sig n LM S a lgorith m used to ada pt DFE ta p va l ues

## DFE Tu n i ng – II R Feed back

![](images/d5c5202ffdfcd2e9d4d235dcd12b12bb91009b2c6640f20179885e67ade2a6af.jpg)

![](images/d4360397d90fd0b6c30c28f2c3d30b3ecc885f5c27ebbc844923b1ff8bb3ea4d.jpg)  
RC time constant control → Equivalent tap number

![](images/f1bde0c4f059ad1151ed34c1c42d8f99aeabf1b7d2c4ece3966872da10c6673f.jpg)  
Amplitude control → Equivalent tap weight

![](images/05fe0135ea8c387a58c01c607c85c6eed4bf63074d017574c51e4a3b6a353bac.jpg)

<table><tr><td rowspan=2 colspan=1>Case 1 $\mathsf { D } 2 , \mathsf { D } 1 , \mathsf { D } 0 = 1 1 0$ </td><td></td><td></td></tr><tr><td rowspan=1 colspan=1> $1 5 1 0 < 0$ </td><td rowspan=1 colspan=1>Decreases amplitude</td></tr><tr><td rowspan=2 colspan=1>Case 2 $\scriptstyle \mathsf { D 3 } , \mathsf { D 2 } , \mathsf { D 1 } , \mathsf { D 0 } = 1 1 1 0$ </td><td rowspan=1 colspan=1> $1 S 1 _ { E 0 } > 0$ </td><td rowspan=1 colspan=1>Increases time constant</td></tr><tr><td rowspan=1 colspan=1> $1 5 1 _ { \mathrm { E 0 } } < 0$ </td><td rowspan=1 colspan=1>Decreases time constant</td></tr></table>

Y. Hidaka, et al., Isscc07

## Agenda

• RX FI R eq ua l ization

• RX CTLE eq ua l ization

• RX DFE eq ua l ization

Eq ua l ization ada ptation tech n iq ues

• Adva nced mod u lation/other tech n iq ues

## Adva nced Mod u lation

I n o rd e r to re m ove I SI , we atte m pt to eq ua l ize or flatten the cha n nel response out to the Nyq u ist freq uency

• For less freq uency-dependent loss, move the Nyq u ist freq uency to a lower va l ue via more adva nce mod u lation

• 4- PAM (o r h i g h e r)

• Duo- bi na ry

• Refe r to l ectu re 4 fo r m o re d eta i l s

## M u lti -to ne Sig na l i ng

![](images/cfefbbb715d2208b2142184520458a532b5933a7a82d4cd0beb9c5b82c90c80d.jpg)  
56G b/ s tota l i n 1 5 ba nds

![](images/5523e9ada5bc36b8be2894e4301b5b77b9cb124ca3fa1fcf160ca4d5e52be53e.jpg)  
[Kim ISSCC 2019]

• I nstead eq ua l izi ng out to baseba nd Nyq u ist freq uency

• Divide the cha n nel i nto ba nds with less freq uency-dependent loss

• Shou ld resu lt i n less eq ua l ization com plexity for each su b- ba nd

• Req u i res u p/down-conversion

• Discrete M u lti-tone used i n DSL modems with very cha l leng i ng cha n nels

Lower data rates a l low for h ig h performa nce DSP

Recently seei ng th is i n some h ig h-speed l i n k resea rch prototypes

## Next Ti me

• Li n k Noise a nd BER Ana lysis