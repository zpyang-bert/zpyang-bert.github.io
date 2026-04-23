---
layout: post
title:      "ECEN 720 : H ig h-Speed Li n ks Ci rcu its a nd Systems Spri ng 2023"
date:       2026-04-18 22:34:08
author:     "Bert"
tags:
  - Lecture
  - Mineru
  - Noise
---
Lectu re 9 : Noise Sou rces

![](images/31853f0618e32f718a767a5b6b334a73bd54d28aec5d414bf7c308ab261213e3.jpg)

Sa m Pa lermo Ana log & M ixed -Sig na l Center Texas A&M U n iversity

## An nou ncements

• La b 5 Report & Prela b 6 d ue Ma r 27

• Stateye theory pa per posted on website

## Noise i n H ig h-Speed Li n k Systems

![](images/f4ba928889e728a3c8c06bbebb8108ad3d5cd0cfd0df508aeab791f25ea6097b.jpg)

## • M u lti ple noise sou rces ca n deg rade l i n k ti m i ng a nd a m pl itude ma rg i n

## Noise Sou rce Overview

## • Com mon “ noise” sou rces

Power su pply noise

Receiver offset

• Crossta l k

I nter-sym bol i nterference

• Ra ndom noise

## • Power su pply noise

• Switch i ng cu rrent th roug h fi n ite su pply i m peda nce ca uses su pply voltage d rops th at va ry with ti m e a n d physica l location

## • Receive r offset

• Ca used by ra ndom device m ismatches

## • Crossta l k

• O ne sig na l (agg ressor) i nte rfe ri n g with a n oth e r s i g n a l (vi cti m )

On -ch i p cou pl i ng (ca pacitive)

Off-c h i p co u p l i n g (t- l i n e)

• Nea r-end

Fa r-end

## I nter-sym bol i nterference

• Sig na l d ispersion ca u ses s i g n a l to i nte rfe re with itse l f

## • Ra ndom noise

Therma l & shot noise

Clock j itter com ponents

## Bou nded a nd Statistica l Noise Sou rces

## • Bou nded or deterministic noise sou rces

• Have theoretica l ly pred icta ble va l ues with defi ned worst-case bou nds

• Al l ows fo r s i m p l e ( b ut pessi m istic) worst-case a na lysis

• Exa m ples

• Crossta l k to sma l l cha n nel cou nt

• I S I

• Rece ive r offset

## Statistica l or random noise sou rces

Treat noise as a ra ndom process • Sou rce may be psuedo- ra ndom

Often cha racterized w/ Ga u ssia n stats

RM S va l ue

Proba bi l ity density fu nction ( PD F)

• Exa m ples

\- Therma l noise

Clock j itter com ponents

• Crossta l k to la rge cha n nel cou nt

## • U ndersta nd i ng whether noise sou rce is bou nded or ra ndom is critica l to accu rate l i n k performa nce esti mation

## Proportiona l a nd I ndependent Noise Sou rces

## • Some noise is proportional to sig na l swi ng

• Crossta l k

• Si m u lta neous switch i ng power su pply noise

• I SI

• Some noise is independent to sig na l swi ng

RX offset

Non-IO power su pply noise

• Ca n overpower th is noise

## • Ca n ’t overpower th is noise

La rger sig na l = more noise

$$
\underset { \ b { \mathscr { n } } } { V } = \underset { \ b { \mathscr { n } } } { K } \underset { \ b { \mathscr { n } } } { V } + \underset { \ b { N } } { V } ,
$$

Tota l noise

Proportiona l noise consta nt

Independent noise

Sig na l swi ng

## Com mon Noise Sou rces

• Power su pply noise

Receiver offset

• Crossta l k

• I nter-sym bol i nterference

• Ra ndom noise

## Power Su pply Noise

![](images/4f3966f8897af697aa391a851b9fae0562373868f117ba2bdb1e233c2484c9cb.jpg)  
[Hodges ]

• Ci rcu its d raw cu rrent from the VD D su pply nets a nd retu rn cu rre nt to th e G N D n ets

• Su pply networks have fi n ite i m peda nce

• Ti me-va ryi ng (switch i ng) cu rrents i nd uce va riations on the su pply voltage

• Su pply noise a ci rcu it sees depend s on its location i n su pply d istri bution network

## Power Routi ng

Bad – Block B wi l l experience excessive su pply noise

![](images/c8fe97029a48f0f742109114ac5c7ce3db2cc5acc15d61451f5bc373fe9403a7.jpg)  
Even Better – Block A & B wi l l expe ri e n ce s i m i l a r su pply noise

![](images/1e7ebbfcc57a037b5f8ae36d138940425cb49ebea5474336d71917810f25ac99.jpg)

Bette r – B l ock B wi l l expe rie n ce 1/2 su pply noise, but at the cost of dou ble the power routi ng th roug h blocks

![](images/f57c2e3df299ca5aa9c2ce1208d5b19e1e9215522ef21c38afb8f84315d5874c.jpg)  
Best – Block A & B a re more isolated

![](images/7d30d98b717e05486e3a04e4e602eb9165134df76285ae5f2f50173bc2ffa629.jpg)

## Su pply I nd uced Delay Va riation

• Su pply noise ca n i nd uce va riations i n ci rcu it delay

Resu lts i n determ i n istic j itter on clocks $\&$ data sig na l s

![](images/3712cfd87d81f8bd77f36326f04087d42b767957879f4630c1e371d21f1e0de3.jpg)

$$
t _ { _ { P H L } } = \frac { C _ { L } \left( V D D / 2 \right) } { I _ { D S A T N } } = \frac { C _ { L } \left( V D D / 2 \right) } { \left( \frac { W _ { N } \nu _ { s a t } C _ { o x } \left( V D D - V _ { _ { T N } } \right) ^ { 2 } } { V D D - V _ { _ { T N } } + E _ { c N } L _ { _ { N } } } \right) ^ { \approx } } \frac { C _ { L } V D D } { 2 W _ { N } \nu _ { s a t } C _ { o x } \left( V D D - V _ { _ { T N } } \right) }
$$

$$
\mathbf { D e l a y } \propto { \frac { V D D } { { V D D } - V _ { _ { T N } } } } \approx \propto V D D
$$

• CMOS delay is a pproxi mately d i rectly proportiona l to VDD

M o re d e l ay res u lts i n m o re d ete rm i n i sti c j itte r

## Si m u lta neous Switch i ng Noise

• Fi n ite su pply i m peda nce ca u ses sig n ifica nt Si m u lta neous Switch i ng Output (SSO) noise (xta l k)

• SSO noise is proportiona l to n u m ber of outputs switch i n g , n , a n d i nve rse ly p ro po rti o n a l to s i g n a l tra n s iti o n ti m e, $\mathfrak { t } _ { \mathfrak { r } }$

$$
V _ { _ { N } } = L { \frac { i } { t _ { r } } } { = } n { \frac { L V _ { s } } { Z _ { 0 } t _ { r } } }
$$

![](images/0e431c14c327cddf055d25c9afc376970f041188caff19f2be7a28a94ecb5232.jpg)

## Com mon Noise Sou rces

• Power su pply noise

• Receiver offset

• Crossta l k

• I nter-sym bol i nterference

• Ra ndom noise

## Receiver I n put Referred Offset

![](images/63a93ada54d9a773d13cb041c9d2d1e1076caea43c8b7446a089b8d8b9176384.jpg)

• Th e i n p ut refe rred offset i s p ri m a ri ly a fu n cti o n of $\mathsf { V } _ { \mathtt { t h } }$ m ismatch a nd a wea ker fu nction of   (mobi l ity) m ismatch

$$
\sigma _ { { } _ { V _ { t } } } = { \frac { A _ { { } _ { V _ { t } } } } { \sqrt { W L } } } , \quad \sigma _ { { } _ { \Delta \beta / \beta } } = { \frac { A _ { \beta } } { \sqrt { W L } } }
$$

## Receiver I n put Referred Offset

$$
\sigma _ { { } _ { V _ { t } } } = { \frac { A _ { { } _ { V _ { t } } } } { \sqrt { W L } } } , \quad \sigma _ { { } _ { \Delta \beta / \beta } } = { \frac { A _ { \beta } } { \sqrt { W L } } }
$$

• To red uce i n put offset $2 \times ,$ we need to i ncrease a rea 4x

Not practica l d ue to excessive a rea a nd power consu m ption

• Offset correction necessa ry to efficiently ach ieve good sensitivity

• Idea l ly the offset “A” coefficients a re g iven by the desig n kit a nd M onte Ca rlo is performed to extract offset sig ma

If not, here a re some com mon va l ues :

• $\mathsf { A } _ { \mathsf { V } \mathrm { t } } = 1 \mathsf { m } \mathsf { V } \mu \mathsf { m }$ per n m of $\mathfrak { t } _ { \mathfrak { o x } }$

• For ou r defa u lt 90n m tech nology, $\mathsf { t } _ { \mathsf { o x } } { = } 2 . 8 \mathsf { n m } \to \mathsf { A } _ { \mathsf { v t } } { \sim } 2 . 8 \mathsf { m V } \mathsf { \mu m }$

• $\mathsf { \pmb { A } } _ { \beta }$ is genera l ly nea r $2 \% \mu \mathrm { m }$

## Com mon Noise Sou rces

• Power su pply noise

• Receiver offset

• Crossta l k

• I nter-sym bol i nterference

Ra ndom noise

## Crossta l k

• Crossta l k is noise i nd uced by one sig na l (agg ressor) that i nte rfe res with a n oth e r s i g n a l (vi cti m )

## • M a i n crossta l k sou rces

• Cou pl i ng between on-ch i p (ca pacitive) wi res

Cou pl i ng between off-ch i p (t- l i ne/cha n nel ) wi res

Sig na l retu rn cou pl i ng

## • Crossta l k is a proportiona l noise sou rce

• Ca n not be red uced by sca l i ng sig na l levels

• Add ressed by usi ng proper sig na l conventions, i m provi ng cha n nel a nd su pply network, a nd usi ng good ci rcu it desig n a nd layout tech n iq ues

## Crossta l k to Ca pacitive Li nes

On -ch i p wi res have sig n ifica nt ca pacita nce to adjacent wi res both on sa me meta l layer a nd adjacent vertica l layers

• Fl oati n g vi cti m

Exa m ples : Sa m ple- nodes, dom i no log ic

When agg ressor switches

• Sig na l gets cou pled to victi m via a ca pacitive voltage d ivider

• S i g n a l i s n ot resto red

$$
\Delta V _ { _ B } = k _ { c } \Delta V _ { _ A }
$$

$$
k _ { c } = \frac { C _ { C } } { C _ { C } + C _ { O } }
$$

[ Da l l y ]

## Crossta l k to Driven Ca pacitive Li nes

• Crossta l k to a d rive n l i ne wi l l decay away with a ti m e-co n sta nt

$$
\tau _ { x c } = R _ { o } \big ( C _ { c } + C _ { o } \big )
$$

• Pea k crossta l k is i nversely proportiona l to agg ressor tra nsition ti m es, $\sf { t } _ { r } ,$ a nd d rive strength $( 1 / \mathsf { R } _ { 0 } )$

![](images/544d1e32e0a06e357cc94e39f65cf15ce6c914026d1ce8d71a782f35871f2ada.jpg)

![](images/47cd7e45884dbd361772c1b5e73c07f61e6099f092735ed97716b7f8412cccea.jpg)

Ideal Unit Step :

$$
\Delta V _ { _ { B } } ( t ) = k _ { c } \exp \biggl ( - \frac { t } { \tau _ { _ { x c } } } \biggr )
$$

Step with Finite Rise Time, $t _ { r }$ :

$$
\Delta V _ { _ { B } } ( t ) = \left\{ \begin{array} { c c } { \displaystyle k _ { c } \left( \frac { \tau _ { _ { x c } } } { t _ { r } } \right) \left[ 1 - \exp \left( - \frac { t } { \tau _ { _ { x c } } } \right) \right] } & { \mathrm { i f ~ } t < t _ { r } } \\ { \displaystyle k _ { c } \left( \frac { \tau _ { _ { x c } } } { t _ { r } } \right) \left[ \exp \left( - \frac { t - t _ { r } } { \tau _ { _ { x c } } } \right) - \exp \left( - \frac { t } { \tau _ { _ { x c } } } \right) \right] } & { \mathrm { i f ~ } t \geq t _ { r } } \end{array} \right.
$$

## Ca pacitive Crossta l k Delay I m pact

• Agg ressor tra nsition i ng nea r victi m tra nsition ca n mod u late the victi m ’s effective load ca pacita nce

• Th is mod u lates the victi m sig na l ’s delay, resu lti ng i n d ete rm i n i sti c j itte r

![](images/cdb31030c77834c14db5791e5472cd68dbb51a3d67d716dc5653e6e156cd08e1.jpg)

Aggressor Static : $C _ { L } = C _ { g n d } + C _ { C }$

Aggressor Switching Same Way : $C _ { L } = C _ { g n d }$

Aggressor Switching Opposite Way : $C _ { L } = C _ { g n d } + 2 C _ { C }$

## M itigati ng Ca pacitive (O n -Ch i p) Crossta l k

• Adjacent vertica l meta l layers shou ld be routed perpend icu la r ( Ma n hatta n routi ng)

• Li m it maxi m u m pa ra l lel routi ng d ista nce

• Avoid floati ng sig na l s a nd u se keeper tra nsistors with dyna m ic log ic

• M axi m ize sig na l tra n sitio n ti m e

Tra d e-off with j itte r se n s itivity

• Fo r d iffe re ntia l si g n a l s, pe riod i ca l ly “twi st” ro uti n g to m a ke cross-ta l k com mon - mode

• Sepa rate sensitive sig na l s

• Use sh ield wi res

• Cou ple DC sig na ls to a ppropriate su pply

## Tra nsm ission Li ne Crossta l k

• 2 cou pled l i nes :

![](images/63bbc16b29c27b25f19cbaedd2a3b1abc6a48bb27362b0a28c8a14c2cf27cc4b.jpg)

• Tra nsient voltage sig na l on A is cou pled to B ca pacitively

$$
{ \frac { d V _ { _ { B } } ( x , t ) } { d t } } = k _ { _ { c x } } { \frac { d V _ { _ { A } } ( x , t ) } { d t } } \quad { \mathrm { ~ w h e r e ~ } } \quad \left[ k _ { _ { c x } } = { \frac { C _ { c } } { C _ { s } + C _ { c } } } \right]
$$

• Ca pacitive cou pl i ng sends ha lf the cou pled energy i n each d i rection with eq u a l po l a rity

## Tra nsm ission Li ne Crossta l k

• 2 cou pled l i nes :

![](images/8f97381de2346cbb0f05a4983f447bce75b3f7b12dc621b913421a9a1d20c366.jpg)

• Tra nsient cu rrent sig na l on A is cou pled to B th roug h m utua l i nd ucta nce

$$
\begin{array} { c } { \displaystyle \frac { \partial I _ { _ { A } } ( { \boldsymbol { x } } , t ) } { \partial t } = - \frac { \partial V _ { _ { A } } ( { \boldsymbol { x } } , t ) } { L \partial { \boldsymbol x } } } \\ { \displaystyle \frac { d V _ { _ { B } } ( { \boldsymbol { x } } , t ) } { d x } = - M \frac { d I _ { _ { A } } ( { \boldsymbol { x } } , t ) } { d t } = \frac { M } { L } \bigg [ \frac { d V _ { _ { A } } ( { \boldsymbol { x } } , t ) } { d x } \bigg ] = k _ { l x } \frac { d V _ { _ { A } } ( { \boldsymbol { x } } , t ) } { d x } ~ \mathrm { w h e r e } ~ \left[ k _ { l x } = \frac { M } { L } \right] } \end{array}
$$

• I nd uctive cou pl i ng sends ha lf the cou pled energy i n each d i rection with a negative forwa rd travel i ng wave a nd a positive reverse travel i ng wave

## Nea r- a nd Fa r- End Crossta l k

## [ H a l l ]

![](images/d7202d6016acc1e3953ddf5bb4e6e0a920204699a2e6375478357da95e2d3b00.jpg)

![](images/8e3c7b66cdcad807181c42ddf064472b24d21c3d39b7038de960c6c8c8226a8e.jpg)

(b)  
![](images/189388d440a19539c6e6d343bae27bc9e66fbb71d0a64e6b98e5f2ad93db89eb.jpg)

![](images/2637462256713c3527f1caf89e8926b9cdf25b7630895b2738b1a401d53bd143.jpg)  
Figure 4-22 Summary of propagation of forward- and backward-coupled noise: (a) ini- ) imi-tinl wave launch; (b) halfway down the line; (c) one full trip down the line; (d) round ound trip.

![](images/7ca916ffaeee7010e04ac0144f561d85e3b7d36788554513395536dafa493086.jpg)

• N ea r-end crossta l k ( N EXT) is i m med iately observed sta rti ng at the agg ressor tra nsition ti me a nd conti n u i ng for a rou nd -tri p delay

• Due to the ca pacitive a nd i nd uctive cou pl i ng terms havi ng the sa me pola rity, the N EXT sig na l wi l l have the sa me pola rity as the agg ressor

• Fa r-end crossta l k ( FEXT) propagates a long the victi m cha n nel with the i ncident sig na l a nd is on ly observed once

• Due to the ca pacitive a nd i nd uctive cou pl i ng terms havi ng the opposite pola rity, the FEXT sig na l ca n have either pola rity, a nd i n a homogeneous med i u m (stri pl i ne) ca ncel out

## Nea r- a nd Fa r- End Crossta l k

![](images/d1f98bc7d13c448ab43084fe75dd3770a02a76d034541e3d70eb999e23a834a8.jpg)

Reverse Cou pl i ng Coefficient ${ \sf k } _ { \sf r x }$ ( N EXT)

Forwa rd Cou pl i ng Coefficient $\mathsf { k } _ { \mathsf { f x } }$ ( FEXT)

$$
\begin{array} { c } { \boxed { k _ { r x } = \frac { \left( k _ { c x } + k _ { l x } \right) } { 4 } } } \\ { k _ { f x } = \frac { \left( k _ { c x } - k _ { l x } \right) } { 2 } } \end{array}
$$

For derivation of ${ \sf k } _ { \sf r x }$ a nd ${ \sf k } _ { \sf f x } ,$ see D a l l y 6 . 3 . 2 . 3

## Off-Ch i p Crossta l k

 Occu rs mostly i n package a nd boa rd - to- boa rd con nectors

 FEXT is atten uated by cha n nel response a nd has ba nd - pass cha racteristic

 N EXT d i rectly cou ples i nto vi cti m a n d h a s h ig h - pass cha racteristic

![](images/1431f3f938463582aec81188af9b801834f229e777910ef476f9bb0bdbc648ba.jpg)

![](images/b22cb2d300b147f75c085fead3632972d195df2fe49f7592132bd535684439e7.jpg)

## Sig na l Retu rn Crossta l k

• Sha red retu rn path with fi n ite i m peda nce

• Retu rn cu rrents i nd uce crossta l k occu rs a mong sig na l s

![](images/06bee899f791f31651f40c3c6c5bb4a9a71971187b7b9b2ddfdf4e64567b8476.jpg)

![](images/983ed82a2c30725effae440661f592cab77c6c9ba56cc062f1efcacbdf094d59.jpg)

Return Cro s stalk Voltage : $V _ { x r } = \Delta V \frac { Z _ { R } } { Z _ { 0 } } = k _ { x r } \Delta V$

## Com mon Noise Sou rces

• Power su pply noise

• Receiver offset

• Crossta l k

• I nte r-sym bo l i nte rfe re n ce

Ra ndom noise

## I nte r- Sym bo l I nte rfe re n ce ( I SI )

• Previou s bits resid ua l state ca n d i sto rt th e cu rre nt b it, res u lti n g i n i nte r-sym bo l i nte rfe re n ce (ISI)

$$
y ^ { ( d _ { k } ) } ( t ) = c ^ { ( d _ { k } ) } ( t ) * h ( t )
$$

$$
\mathsf { y } ^ { ( 1 ) } ( \mathsf { t } )
$$

![](images/22d7882dedd72ad4a29da012f3346cbe5156f7d41ae7c2949e47cfd27f87fc61.jpg)

$$
\mathsf { y } ^ { ( 0 ) } ( \mathsf { t } ) = - \mathsf { 1 } ^ { \ast } \mathsf { y } ^ { ( 1 ) } ( \mathsf { t } )
$$

## Pea k Distortion Ana lysis Exa m ple

![](images/1ad93f77c5dd1785f56304ba4ebf632ce51e2bef0f6e7f8da717b8350c32175f.jpg)

$$
\begin{array} { c } { { y _ { 0 } ^ { ( 1 ) } ( t ) = 0 . 5 4 0 } } \\ { { \displaystyle \sum _ { k = - \infty } ^ { \infty } y ^ { ( 1 ) } \big ( t - k T \big ) _ { | y ( t - k T ) \times 0 } = - 0 . 0 0 7 } } \\ { { \displaystyle \sum _ { k = - \infty } ^ { \infty } y ^ { ( 1 ) } \big ( t - k T \big ) _ { | y ( t - k T ) \times 0 } = 0 . 3 8 9 } } \\ { { \displaystyle k \approx 0 } } \\ { { s ( t ) = 2 \big ( 0 . 5 4 0 - 0 . 0 0 7 - 0 . 3 8 9 \big ) = 0 . 2 8 8 } } \end{array}
$$

![](images/2fbc2521511ebabaac3d741c9c69c57c9724feca3e037b41adc51c65165d1862.jpg)

![](images/759cdbd7688ad6c9fd941900257b1c80e3e5209e52764f9f454ea12a7de09325.jpg)

## Worst-Case Eye vs Ra ndom Data Eye

![](images/185bad70d7df9c490ca45ba3bf6825649c9622337d141ef7be35ec33623c87e1.jpg)  
• Worst-case data pattern ca n occu r at very low proba bi l ity !

• Consideri ng worst-case is too pessi m istic

## Constructi ng ISI Proba bi l ity Density Fu nction ( PDF)

• Usi ng ISI proba bi l ity density fu nction wi l l yield a more accu rate BER performa nce esti mate

• I n order to construct the tota l ISI PDF, need to convolve a l l of the i nd ivid ua l ISI term PD Fs together • 50% proba bi l ity of “ 1 ” sym bol ISI a nd “ - 1 ” sym bo l ISI

![](images/3623001e03be6d4429ab970f785e325b6d4f7cc6021e567679d05d67024e142c.jpg)

![](images/3b364403f5b14476a7b473e1400681efc37a57bf9f655628420abf6be7728b48.jpg)

![](images/c8a447f0f5327d2b3b3859dd795847f314ed966954a05125a1e652c08822cdd6.jpg)

![](images/ca68f15e3034902a56280d7d099ca2e597e73646627beaa41662b4666b2ce5cc.jpg)

## Convolvi ng I nd ivid ua l ISI PDFs Together

![](images/46996814dba4297955cd41af18e40b6162bedb2b64fe70d521f5b214df773091.jpg)

![](images/0c2d9f1a308771f21d82050bdead0b5d825cfc845cb8d8542a7e1723d206b2f2.jpg)

![](images/bcf6fad0981cc70acc2c2b1a9f38a61dafac05cfc6bd805b5828a080709974fe.jpg)

![](images/604dd74698f12c84645e07d683c04cb7234d5c8f0a07207a45f5698d4474a71f.jpg)

![](images/b71e8a9248b4043d8a653a58784b77912ba2ec86987a81b650c5a142bd7cd397.jpg)

![](images/01f4a15ac24df4fa206e6fbb9e2bfca211ebaa21b3405257c21a9e5474aa79f7.jpg)  
Keep goi ng u nti l a l l i nd ivid ua l PDFs convolved together

## Com plete ISI PDF

![](images/7fbf55171a9d2dbd8a5cd94e9c749de9c75a131316baed937870520d42f335b0.jpg)

## Cu rsor PD F – Data 1

![](images/c27ac65de2ec63d1243237e342ad2db458cfcebf4279744ef358864c6a4a3f87.jpg)

![](images/86cdea662a2ab156a2a636c48d3739e450b8b53331050bc418da8c97ebf1e414.jpg)

![](images/70dabdddb66b243abd747955fca9773bcde42deeea9e6a591da5f540d8ceaf16.jpg)

## • Data 1 PD F is centered a bout the cu rsor va l ue a nd va ries from a maxi m u m positive va l ue to the worst-case va l ue pred icted by PDA

• Th is worst-case va l ue occu rs at a low proba bi l ity !

## Cu rsor Cu m u lative Distri bution Fu nction (CD F)

• Fo r a g ive n offset, wh at i s th e p ro ba b i l ity of a Data 1 error?

• Data 1 e rro r p ro ba b i l ity fo r a g ive n offset i s eq u a l to the Data 1 CDF

$$
B E R ( X ) = \int _ { - \infty } ^ { X } ( P D F ) d x
$$

![](images/12a0e6252c575434a0b84cf80b4bad6997775d2e769aefb2b750563490c08c07.jpg)

![](images/7b5485923f47055d647eedcff5b66cc32b65bdf2fbaf4fcf9abf4c740f6f286b.jpg)

## Com bi n i ng Cu rsor CDFs

![](images/480271f7db666320f7decc829d02e0b3d3e2c513ef198c7bb6c88e50433996f2.jpg)

![](images/a4a8da9b0bfcfe6eb8f1bdbd9a5eb2d561c2cee522c0df5f470f256b7ac2fa27.jpg)

![](images/2b55271079cc7b91b4ca850276fb0aa42da91533809e162a3c135259fa05a35a.jpg)

## B it- E rro r- Rate ( B E R) D i stri b uti o n Eye

• Statistica l BE R a na lysis tool s u se th is tech n iq ue to accou nt for ISI d istri bution a nd a l so other noise sou rces

Exa m ple from Stateye

Note : Different cha n nel & data rate from previou s sl ides

![](images/131aaa8be69140dca1eb5992c9f1d44b90e4814b867e0c0b869cde8222f8e6a7.jpg)

## Com mon Noise Sou rces

• Power su pply noise

• Receiver offset

• Crossta l k

• I nter-sym bol i nterference

• Ra ndom noise

## Ra ndom Noise

• Ra ndom noise is u n bou nded a nd modeled stati sti ca l ly

Exa m ple : Ci rcu it therma l a nd shot noise

• Modeled as a conti n uous ra ndom va ria ble descri bed by

• Proba bi l ity density fu nction ( PD F)

• M ea n , 

Sta nda rd deviation, 

$$
P D F = P _ { n } ( x ) , \mu _ { n } = \intop _ { - \infty } ^ { \infty } x P _ { n } ( x ) d x , \sigma _ { n } ^ { 2 } = \intop _ { - \infty } ^ { \infty } ( x - \mu _ { n } ) ^ { 2 } P _ { n } ( x ) d x
$$

## Ga u ssia n Distri bution

• Ga u ssia n d istri bution is norma l ly assu med for ra ndom noise La rger sig ma va l ue resu lts i n i ncreased d istri bution spread

$$
P _ { n } ( x ) = { \frac { 1 } { \sqrt { 2 \pi } \sigma } } e ^ { - { \frac { ( x - \mu _ { n } ) ^ { 2 } } { 2 \sigma ^ { 2 } } } }
$$

![](images/524b6e09eeeb2695e091750f202171fa70ae77cda63ea82e4fbea44293e1c6c9.jpg)

Gaussian PDFs  
![](images/2c4ce05becbeac5dfbd88b44045b47c0570a85970deecdcfb0cee384b703538e.jpg)

## Sig na l with Added Ga ussia n Noise

![](images/4eb47ef5e1d4a920efd37bf662886e37a5a9cb8d002c3d9e5ab33c31e2d794af.jpg)

![](images/95a12693f7f9d7c15aa25ea8366aeaaebe54b938b68a00d0958198ed52666cab.jpg)

## • Fi n ite proba bi l ity of noise pu sh i ng sig na l pa st th resh o l d to yi e l d a n e rro r

## Cu m u lative Distri bution Fu nction (CDF)

• The CDF tel ls what i s th e p ro ba b i l ity that the noise sig na l is less tha n or eq ua l to a certa i n va l ue

![](images/5dea58c913f86a47d07d46c2cb09ff8d7fa65e8575579620644dcdfd02fd5e99.jpg)

$$
\Phi _ { n } ( x ) = \int _ { u = - \infty } ^ { x } P _ { n } ( u ) d u = \int _ { u = - \infty } ^ { x } \frac { 1 } { \sqrt { 2 \pi } \sigma } e ^ { - \frac { ( u - \mu _ { n } ) ^ { 2 } } { 2 \sigma ^ { 2 } } } d u
$$

## Error a nd Com pl i menta ry Error Fu nctions

• E rro r Fu n cti o n :

$$
e r f ( x ) = \frac { 2 } { \sqrt { \pi } } \int _ { u = 0 } ^ { x } \exp { \left( - u ^ { 2 } \right) } d u
$$

• Relationsh i p between norma l           212 1 xx e rf C D F (0, 1 ) a n d E rro r Fu n cti o n :

• The com plementa ry error $\begin{array} { c } { { Q ( x ) { = } 1 { - } \Phi ( x ) { = } \displaystyle \frac { 1 } { 2 } \Biggl [ 1 { - } e r f \Biggl ( \displaystyle \frac { x } { { \sqrt 2 } } \Biggr ) \Biggr ] } } \\ { { { } } } \\ { { { } = \displaystyle \frac { 1 } { 2 } e r f c \Biggl ( \displaystyle \frac { x } { \sqrt 2 } \Biggr ) } } \end{array}$   
fu nction g ives the proba bi l ity   
that the noise wi l l exceed a   
g iven va l ue

$$
Q _ { \mu \sigma } ( x ) { = } { = } { \frac { 1 } { 2 } } e r f c { \left( { \frac { x - \mu } { \sigma { \sqrt { 2 } } } } \right) }
$$

## B it E rro r Rate ( B E R)

• U si n g e rfc to p red ict B E R :

![](images/77979f0de26d09474e029e42432971c69fee061f927a7ba5866443465df90bd2.jpg)

• Need a sym bol of a bout $7 \sigma$ fo r B E R= 1 0- 1 2

• Pea k-to- pea k va l ue wi l l be $2 { \tt x }$ th i s

## N oise Sou rce Classifications

• Determ i n i ng whether noise sou rce is

Proportiona l vs I ndependent

• Bou nded vs Statistica l

• is i m porta nt i n noise budgeti ng

Proportional Independent
<table><tr><td rowspan=2 colspan=1>papunog</td><td rowspan=1 colspan=1>Residual ISICrosstalk</td><td rowspan=1 colspan=1>RX OffsetRX SensitivityPower SupplyNoise</td></tr><tr><td rowspan=1 colspan=1>Large-ChannelCrosstalk</td><td rowspan=1 colspan=1>Random Noise</td></tr></table>

## Noise Budget Exa m ple

• Pea k TX d ifferentia l swi ng of $4 0 0 \mathrm { \textmu m V _ { p p d } }$ eq ua l ized down 1 0d B • $\pm 2 0 0 \mathrm { m V }  \pm 6 3 \mathrm { m V }$

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1> $\kappa _ { \mathfrak { n } }$ </td><td rowspan=1 colspan=1>RMS</td><td rowspan=1 colspan=1>Value $( \mathsf { B E R } { = } \mathbf { 1 0 } ^ { - 1 2 } )$ </td></tr><tr><td rowspan=1 colspan=1>Peak DifferentialSwing</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.4V</td></tr><tr><td rowspan=1 colspan=1>RX Offset +Sensitivity</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>5mV</td></tr><tr><td rowspan=1 colspan=1>Power SupplyNoise</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>5mV</td></tr><tr><td rowspan=1 colspan=1>Residual ISI</td><td rowspan=1 colspan=1>0.05</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>20mV</td></tr><tr><td rowspan=1 colspan=1>Crosstalk</td><td rowspan=1 colspan=1>0.05</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>20mV</td></tr><tr><td rowspan=1 colspan=1>Random Noise</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1mV</td><td rowspan=1 colspan=1>14mV</td></tr><tr><td rowspan=1 colspan=1>Attenuation</td><td rowspan=1 colspan=1> $1 0 \mathsf { d } \mathsf { B } = 0 . 6 8 4$ </td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.274V</td></tr><tr><td rowspan=1 colspan=1>Total Noise</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.338V</td></tr><tr><td rowspan=1 colspan=1>Differential EyeHeight Margin</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>62mV</td></tr></table>

![](images/caf668aece016d3361306f5cddbe0f46d7bbcc9240396c70f17951792a6daa21.jpg)

• Conservative a na lysis

• Assu mes a l l d istri butions com bi ne at worst-case

• Better tech n iq ue is to u se statistica l BE R l i n k si m u lators

## Next Ti me

• Ti m i ng Noise

• BER Ana lysis Tech n iq ues