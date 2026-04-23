---
layout: post
title:      "Analysis and Application of Digital Signal Processing Algorithms for Intelligent Optical Coherent Transceivers in Multiband Systems"
date:       2026-04-18 22:00:39
author:     "Bert"
tags:
  - DSP
  - Mineru
  - Optical
---
vorgelegt von M. Sc. Matheus Ribeiro Sena

an der Fakultät IV - Elektrotechnik und Informatik der Technischen Universität Berlin zur Erlangung des akademischen Grades Doktor der Ingenieurwissenschaften -Dr.-Ing.- genehmigte Dissertation

Promotionsausschuss:

Vorsitzender: Prof. Dr.-Ing. Lars Zimmermann

Gutachter: Prof. Dr.-Ing. Ronald Freund

Gutachter: Prof. Dr.-Ing. Norbert Hanik

Gutachter: Prof. Sergei K. Turitsyn

Tag der wissenschaftlichen Aussprache: 17. November 2023

Berlin 2024

## Zusammenfassung

Im Laufe der letzten Jahrzehnte hat die Welt eine zunehmende Abhängigkeit vom Internet für Kommunikation, Unterhaltung und E-Commerce erfahren. Mit Milliarden Nutzern weltweit ist die Notwendigkeit verbesserter Netzinfrastrukturen, die in der Lage sind, die stetig wachsenden High-Bandwidth-Dienste zu unterstützen, zu einem wichtigen Faktor geworden, der die Zukunftsfähigkeit des Internets bestimmen wird. Da der Großteil des heutigen Datentrafcs über Glasfaserkabel übertragen wird, ist die Realisierung innovativer Ansätze zur Steigerung der Kapazität von Glasfasernetzwerken ein entscheidender Schritt, um denjenigen Herausforderungen zu begegnen, die die Zukunft des Internets gefährden könnten. Eine Alternative zur Erkundung der Kapazität der bereits verlegten Glasfaserkabel besteht darin, mehrere optische Bänder des Telekom-Spektrums, die sogenannte Multiband (MB)-Technologie, zu nutzen. Dennoch erfordert eine erfolgreiche Implementierung des MB-Ansatzes in Glasfasernetzwerken immer noch die Lösung einer Reihe von Fragestellungen, etwa die Entwicklung von MB-fähigen Geräten, die Schafung von Schätzungs- und Bewältigungsmechanismen bei komponentenabhängigen Wellenlängenverzerrungen sowie die efziente überwachung von MB-Netzwerken.

Diese Arbeit diskutiert zwei Anwendungen für optische MB-Netzwerke unter Verwendung von optischen kohärenten Transceivern, genauer gesagt auf Grundlage der digitalen Signalverarbeitung (DSP) von Sendern (Tx) und Empfängern (Rx). Moderne kohärente Transceiver sind mit leistungsstarken Tx- und Rx-DSP-Modulen ausgestattet, sodass Algorithmen mit einer Vielzahl von Funktionen implementiert werden können, die für die Realisierung von MB-Systemen entscheidend sind. In diesem Zusammenhang beginnt diese Arbeit mit einer Diskussion über den Einfuss von wellenlängenbasierten komponenteninduzierten Verzerrungen auf die Designspezifkationen für MB-optische Sender, die auf Indiumphosphid (InP)- Technologie basieren, was in der Folge die Entwicklung von Tx-DSP-Algorithmen rechtfertigt. Bei dieser Diskussion liegt ein besonderer Schwerpunkt auf der Modellierung von optischen Dual-Polarisations-(DP) In-Phase-(I)-Quadratur-(Q)-Modulatoren, die aus InP-Multimode-Interferenz-(MMI)-Kopplern aufgebaut sind. Es werden simulative Analysen verwendet, um den Einfuss wellenlängenabhängiger komponenteninduzierter Verzerrungen in optischen kohärenten Sendern zu bemessen. In dieser Studie wird festgestellt, dass die Optimierung des MMI-Designs zu optischen Modulatoren führen kann, die in etwa 95% des optischen Spektrums von 1260-1620 nm (O+E+S+C+L-Band) optische Signal-Rausch-Verhältnis (OSNR)-Strafen unter 0.5 dB (back-to-back) aufweisen.

Durch den Betrieb im nichtlinearen Bereich kann die Leistung optischer kohärenter Sender mit der Verwendung von Volterra-basierten nichtlinearen digitalen Vorverzerrungs(DPD)- Schemata weiter verbessert werden. Die Gestaltung von DPD-Filtern ist jedoch eine anspruchsvolle Aufgabe, und da von MB-Efekten eine wellenlängenabhängige Abhängigkeit erwartet wird, müssen zusätzliche Funktionen entwickelt werden, um die Anpassungsfähigkeit an das Tx-DSP zu gewährleisten. Dadurch kann das Tx-DSP seinen Betrieb selbstständig auf Verzerrungen in mehreren optischen Bändern abstimmen. In diesem Sinne wird ein Tx-DSP-Ansatz verwendet, der auf der Bayesianischen Optimierung (BO) basiert, um das Design von Volterra-DPD-Filtern zu optimieren. Dieser Ansatz wird in mehreren übertragungsszenarien getestet und verifziert. Bei diesem Ansatz optimiert die BO die Länge der Speichertaps in einer Volterra-Reihe, die zur Synthese von DPD-Filtern verwendet wird. Einer der beobachteten Vorteile nach Verwendung der BO ist die Reduzierung der Konvergenzgeschwindigkeit der Systemidentifkation um 46% im Vergleich zu einem benchmarkgestützten Ansatz. Zusammen mit der Verwendung von Memory-Polynomials-Filtern kann der BO-basierte DPD zu einer Reduzierung der Filterkomplexität um etwa 75% im Vergleich zu Volterra-DPD-Filtern führen, ohne dabei wesentliche Leistungseinbußen in einem optischen Back-to-Back-Setup zu verursachen. Schließlich wird dieses Schema getestet, um die Leistung eines traditionellen C-Band-Senders im S+C+L-Band zu verbessern, wobei die Optimierung der Speichertapverteilung für den DPD-Filter über BO einen Gewinn von etwa 0.4 dB im Q-Faktor über 40 km Einmodenfaser liefert. Diese Anwendung deckt somit den ersten vorgeschlagenen Anwendungsbereich ab, nämlich die Entwicklung von Tx-DSP für MB-Systeme.

Schließlich wird der zweite vorgeschlagene Anwendungsbereich, nämlich ein Rx-DSP für die MB-optische Kommunikation, durch die Demonstration eines räumlich aufgelösten und wellenlängenweisen überwachungsschemas erreicht, um die MB-Eigenschaften von C+L-Bandoptischen Verstärkern abzuschätzen und Fehler zu identifzieren, die während des MB-Betriebs auftreten können. Bei dieser Analyse wird eine Link-Tomographie, d.h. eine Schätzung der optischen Leistung des Kanals in Abhängigkeit von Entfernung und Wellenlänge, erstellt und in einer umfangreichen experimentellen Untersuchung verwendet, bei der das spektrale Gewinnprofl von optischen Verstärkern, die über 280 km Glasfaser bereitgestellt sind, aus dem Rx-DSP vorhergesagt werden kann. Die in dieser Arbeit aufgezeigten Ergebnisse zeigen, dass sub-dB-Fehler (maximal 0.6 dB) erzielt werden können, wenn der Gewinn aus der Link-Tomographie mit einer Back-to-Back-Charakterisierung verglichen wird, die mit einem optischen Spektrumanalysator durchgeführt wurde. Schließlich wird die Link-Tomographie auf neuartige Weise eingesetzt, um häufg auftretende Verstärkungsanomalien wie Verstärkungskippungen und schmalbandigen Verstärkungskompressionen, die durch den spektralen Lochbrennefekt verursacht werden, darstellen zu können. Dies ergänzt die zweite vorgeschlagene Anwendung für diese Dissertation, die eine praktische Nutzung des Rx-DSP für MB-Systeme darbieten will.

## Abstract

Over the past decades, the world has experienced an increasing reliance on Internet for communication, entertainment, and e-commerce. And with billions of users spread across the globe, the necessity for enhanced network infrastructures capable to support the ever growing high-bandwidth services has become an important aspect that will determine the survivability of the Internet in the future. As most of today’s data trafc is transferred over optical fber cables, the realization of innovative approaches to increase capacity of optical networks is a vital step to tackle the challenges that may undermine Internet’s future. One alternative to explore the capacity of the already deployed optical fber cables is by means of utilizing Yet, a successful implementation of the MB approach in optical networks still requires thesolution of a series of questions, such as the development of MB-capable devices, the creation of mechanisms that can estimate and cope with component wavelength-dependent distortions,and how to efciently monitor MB networks. This thesis discusses two applications for optical MB networks using optical coherent transceivers, or more specifcally, transmitter (Tx) and receiver (Rx) based digital signal processing (DSP). Since modern coherent transceivers are embedded with powerful Tx- and Rx-DSP modules, algorithms can be implemented such to fulfll a wide range of functions that are crucial for the realization of MB systems. In that context, this work starts debating the infuence of wavelength-based component-induced distortions on the design specifcations for MB optical transmitters based on Indium Phosphide (InP) technology, which later justifes the development of Tx-DSP algorithms. In this discussion, a signifcant focus is given to the modeling of optical dual-polarization (DP) in-phase (I) quadrature (Q) modulators, which are built from InP multi-mode interference (MMI) couplers. Some simulative analysis are utilized to quantify the impact of wavelength-dependent component-induced distortions in optical coherent transmitters. In this study, it is observed that the optimization of MMI design can lead to optical modulators yielding optical signal-to-noise ratio (OSNR) penalties under 0.5 dB (back-to-back) in approximately 95% of the optical spectrum from 1260 - 1620 nm (O+E+S+C+L-band). When operated in nonlinear regime, the performance of optical coherent transmitters can be further improved with the utilization of Volterra-based nonlinear digital pre-distortion (DPD) schemes. Yet, the design of DPD flters is a challenging task and since MB efects are expected to be wavelength-dependent, additional features must be developed such to ofer adaptability to the Tx-DSP. Then, the Tx-DSP can self-tune its operation to account for distortions in multiple optical bands. In this sense, a Tx-DSP approach based on using Bayesian optimization (BO) to optimize the design of Volterra DPD flters is used and verifed in several transmission

scenarios. In this approach, the BO tunes the length of memory taps in a Volterra series used for the the synthetization of DPD flters. One of the benefts observed after utilizing the BO is the reduction of 46% in the convergence speed of the system identifcation, when this method is compared against a benchmarked approach. Additionally, in conjunction with the use of memory polynomials flters, the BO-based DPD can lead to a flter complexity reduction of approximately 75% in comparison to Volterra DPD flters without any signifcant performance loss in an optical back-to-back setup. Finally, this scheme is tested to improve performance of a traditional C-band transmitter in S+C+L-band, where the optimization of the memory tap distribution for the DPD flter via BO yields a gain of approximately 0.4 dB in Q-factor over 40 km of single mode fber. This application, then, covers the frst proposed scope, which is the development of Tx-DSP for MB systems.

At last, the second proposed scope, i.e., a Rx-DSP for MB optical communication, is achieved with the demonstration of a spatially-resolved and wavelength-wise monitoring scheme to estimate MB properties of C+L-band optical amplifers and identify faults that may occur in MB operation. In this analysis, a link tomography, i.e., an estimation of the channel’s optical power with respect to distance and wavelength, is constructed and used in an extensive experimental investigation where the spectral gain profle of optical amplifers deployed over 280 km of optical fber can be predicted from the Rx-DSP. The results reported in this work show that sub-dB errors (maximum 0.6 dB) can be achieved when comparing the gain extraction from the link tomography against a back-to-back characterization realized through an optical spectrum analyzer. At last, the link tomography is employed in a novel manner by delivering a visualization of common amplifcation anomalies such as gain tilts and narrowband gain compressions caused by spectral hole burning efect. This complements the second proposed application for this thesis, which intends to ofer a practical use of the Rx-DSP for MB systems.

## Acknowledgements

I would like to express my deepest appreciation to Dr.-Ing. Johannes Karl Fischer for providing me the opportunity to work on this captivating topic with a high level of creative freedom and for the valuable advisory support. Over the course of three years, I learned with him how to properly analyze and present my scientifc results in publications and at conferences in the feld of optical communications. I also dedicate many thanks to Dr. Behnam Shariati, who generously shared knowledge and expertise during our daily interactions. Additionally, this endeavor would not have been possible without the supportive assistance of Prof. Dr.-Ing. Ronald Freund, who took time to review this work and my publications, thus suggesting valuable improvements.

I also extend my thanks to the colleagues I met at Fraunhofer Heinrich Hertz Institute (HHI), including Dr. M. Sezer Ercılınç, Dr.-Ing. Pablo Wilke, Dr.-Ing. Felix Frey, Dr.-Ing. Isaac Sackey, with whom I had productive discussions, either during lunch time, meetings or business trips. In particular, I owe my special thanks to Dipl.-Ing. Robert Emmerich. His assistance and counsels with the laboratory activities helped me to rapidly develop the experimental knowledge necessary for the success of my research.

In the familiar environment, I am extremely thankful to my parents, Gabriel and Vera, for their love, and encouragement throughout the journey of completing this PhD. Their unwavering belief in me and their willingness to listen to my concerns and fears during this time have been a stable source of strength and motivation. Moreover, their constant support has been very meaningful to me and played a crucial role in my academic and personal growth. I also want to thank my sisters, Rafaela and Gabrielle, my aunts, Gabriela and Tila, and my great friend Pedro Jorge. They have always been there for me, ofering a listening ear and a helping hand whenever I needed it. Your encouragement and advice have been invaluable, and I am grateful to have you present in my life. Finally, I want to thank my wife, Camila, for her love and patience during this long process of concluding the PhD. Her love and patience have strengthened me, and I could not have completed this project without her. From the late-night calls to the most stressful moments with paper submissions, Camila has always been there for me.

To conclude, I would like to thank Tatiana Kilina, the Fraunhofer HHI, and all others who have been directly or indirectly involved in the coordination and organization of the wideband optical networks (WON) project.

## Table of Contents

Title Page i   
Zusammenfassung iii   
Abstract v   
List of Figures xiii   
Abbreviations xi1 Introduction1.1 Beyond WDM systems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 Optical MB systems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3 Cognitive optical networks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.4 Scope of this thesis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.5 Author’s bibliography . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . List of Tables xvii   
Abbreviations x   
1 Introduction 1   
1.1 Beyond WDM systems 1   
1.2 Optical MB systems 2   
1.3 3   
4   
5   
2 Fundamentals 7   
2.1 Optical coherent transmission 7   
2.2 Optical coherent transceivers 8   
2.2.1 Transceiver specifcations 9   
2.2.1.1 Packaging . . 9   
2.2.1.2 DSP embedding 11   
2.2.2 Transceiver anatomy 11   
2.2.2.1 Transmitter DSP (Tx-DSP) 11   
2.2.2.2 Digital-to-analog converter (DAC) 12   
2.2.2.3 Driver amplifer (DA) 13   
2.2.2.4 Modulator 14   
2.2.2.5 Receiver frontend 16   
2.2.2.6 Analogue-to-digital converter (ADC) 16   
2.2.2.7 Rx-DSP 17   
2.3 Conclusion and outlooks 21   
3 Design of MB Transmitters 23   
3.0.1 Performance metrics 23   
3.0.2 Device technology 24   
3.0.2.1 Lithium Niobate (LiNbO3) 24   
3.0.2.2 Silicon Photonics . 25   
3.0.2.3 Indium Phosphide (InP) 25   
3.1 InP-based multimode interference (MMI) couplers 26   
3.1.1 Self-imaging principle 27   
3.1.2 Splitting ratio . 30   
3.1.3 Insertion loss 32   
3.1.4 Wavelength dependency of SR and IL 33   
3.2 System-level performance 35   
3.3 Conclusion 40   
4 Digital Predistortion for MB Optical Transmitters 41   
4.1 Volterra-based system identifcation (SI) 42   
4.1.1 Mathematical background . 42   
4.1.2 Kernel coefcient estimation 43   
4.2 Bayesian optimization . 43   
4.2.1 Hyperparameter tuning problem 43   
4.2.2 Surrogate function 44   
4.2.3 Acquisition function 45   
orithm 45   
4.3 47   
4.4 Digital pre-distortion 49   
4.5 51   
51   
4.5.2 Performance evaluation 52   
4.5.2.1 Diferent driver amplifer (DA) gains . 53   
4.5.2.2 Diferent symbol rates . 55   
4.5.2.3 Diferent modulation formats 55   
4.5.2.4 Performance with memory polynomial flters 56   
4.6 Experimental validation II . . 58   
4.6.1 Linear vs. nonlinear DPD in S-band 59   
4.6.2 BO for Volterra and MP-based DPD in S+C+L-band 60   
4.6.3 Conclusion . . 61   
5 DSP for Link Tomography in MB Systems 63   
5.1 Rx-based DSP for optical performance monitoring (OPM) 64   
5.2 Fundamentals of light propagation in optical fbers 65   
5.2.1 System identifcation of optical fber links 65   
5.2.2 Digital backpropagation 66   
5.2.3 Problem formulation 68   
5.2.4 Implications to the problem formulation 68   
5.3 In-situ power profle estimator (PPE) for longitudinal power estimation 69   
5.4 Link tomography . 72   
5.4.1 Simulative investigations . . 73   
5.4.2 Experimental validation I 78   
5.4.2.1 Spectral gain estimation . 78   
5.4.2.2 Anomaly detection . 83   
5.4.3 Experimental validation II . 85   
5.5 Conclusion 87   
6 Conclusions and Outlook 9 1   
References 93

## List of Figures

1.1 Optical MB spectrum and throughput records in SMF using WDM MB systems. 2   
2.1 Generic block diagram of a p2p coherent transmission system setup. 8   
2.2 Diagram of the transceiver form factor evolution. 9   
2.3 Picture of an Acacia CFP2-DCO transceiver, illustration of a stacked component   
design, generic block diagram of an optical coherent transceiver. 10   
2.4 Representation of a 3-bit (N = 3) DAC nominal response, and actual nonlinear   
ft curves of the DAC’s response. 13   
2.5 Schematic of a MZM, and feld transfer function of a MZM. 14   
2.6 Structure of an IQ modulator. . 15   
2.7 Block diagram of the adaptive 2x2 MIMO time-domain equalizer. 18   
3.1 Schematic of a MZM and its functional elements, and light intensity distribution   
for a 2x2 MMI. 27   
3.2 Two-dimensional representation of a step-index multimode waveguide, and   
example of amplitude-normalized lateral feld profles corresponding to the frst   
9 guided modes in a step-index multimode waveguide. 27   
3.3 Representation of a multimode waveguide. When the input feld $\Psi ( y , 0 )$ is fed   
to the waveguide, a mirrored single image is replicated at $3 L _ { \pi }$ , a direct single   
image at $2 ( 3 L _ { \pi } )$ , and two-fold images at $\scriptstyle { \frac { 3 L _ { \pi } } { 2 } }$ and $\scriptstyle { \frac { 3 ( 3 L _ { \pi } ) } { 2 } }$ 29   
3.4 Schematic of a 2x2 MMI. 30   
3.5 Schematics of a 2x2 MMI with two active input signals and a 1x2 MMI. 32   
3.6 Simulated splitting ratio of a 2x2 MMI vs. wavelength for four diferent lengths,   
widths and access waveguide widths. . 34   
3.7 Simulated insertion loss of a 2x2 MMI vs. wavelength for four diferent lengths,   
widths and access waveguide widths. . 34   
3.8 Simulation setup for the b2b evaluation of the transmitter based on the four   
types of InP MMI designs. . 35   
3.9 OSNR penalty as a function of the wavelength for four diferent modulator   
designs tested on a 32 GBd DP-4QAM signal. Recovered constellation diagram   
for x-polarization when the modulator design based on the InP MMI 1 is   
evaluated at a) 1.55 µm (C-band), b) 1.40 µm (E-band), and c) 1.30 µm   
(O-band) (OSNR = 12.75 dB). 36   
3.10 Recovered constellation diagram for x-polarization when the modulator design   
based on the InP MMI 3 is evaluated at a) 1.30 µm (O-band), b) 1.40 µm   
(E-band), c) 1.50 µm (S-band), d) 1.55 µm (C-band), and d) 1.60 µm (L-band)   
(OSNR = 12.75 dB). . 37   
3.11 Per-band and total spectrum availability as function of the 2x2 MMI design   
and modulation format (DP-4QAM). . . 38   
3.12 OSNR penalty as a function of the wavelength for four diferent modulator   
designs tested on a 32 GBd DP-16QAM signal. Recovered constellation diagram   
for x-polarization when the modulator design based on the InP MMI 1 is   
evaluated at a) 1.55 µm (C-band), b) 1.40 µm (E-band), and c) 1.30 µm   
(O-band) (OSNR = 19.70 dB). 38   
3.13 Per-band and total spectrum availability as function of the 2x2 MMI design   
and modulation format (DP-16QAM). 39   
4.1 Implementation of the BO algorithm for maximization of the objective function f. 46   
4.2 Initialization of the surrogate model with n = 5 observations. a, c, e, g) Updated   
surrogate function for i = 1, 2, 3, 4, respectively. b, d, f, h) Acquisition function   
for i = 1, 2, 3, 4, respectively. . . 46   
4.3   
identifcation error eSI . . 47   
4.4   
of a 5th-order synthetic flter. 49   
4.5   
approach. . 50   
4.6 Conceptual block diagram of the DPD, and block diagram of the ILA for   
synthetization of the DPD flter. 50   
4.7 Experimental setup, and block diagram for validation of the DPD hyperparameters. 51   
4.8 Identifcation error for diferent DA gains with respect to flter complexity MC   
when Bayesian-based SI is performed. . . 54   
4.9 BER validation (at fxed OSNR = 44.9 dB) for diferent DA gains $( g _ { 1 } < g _ { 2 } < g _ { 3 } )$   
as function of the flter complexity MC. 54   
4.10 BER validation (at fxed OSNR = 44.9 dB) for diferent symbol rates (64 and   
80 GBd) as function of the flter complexity MC. . 55   
4.11 BER validation (at fxed OSNR = 44.9 dB) for modulation formats (DP-64QAM   
and DP-256QAM) as function of the flter complexity MC. 56   
4.12 BER curves obtained for DP-64QAM signal at 64 and 80 GBd when Volterra   
and MP DPD flters are benchmarked. . . . . 57   
4.13 Filter complexity reduction of 75% can be achieved by using MP DPD flters. . 57   
4.14 Experimental setup investigated in the second validation. 58   
4.15 BER curves for fxed OSNR = 32.5 dB when Type I and Type II DPD flters   
are used in the S-band. . 60   
4.16 Q-factor curves for OSNR = 32.5 dB when Type I, III and IV DPD flters are   
investigated in the S+C+L-band. . 60   
5.1 Setup utilized to explain the concept of the link tomography, and block diagram   
of the in-situ PPE algorithm used in this work. 70   
5.2 Figure to explain the concept of a networkwide link tomography. 72   
5.3 Simulative analysis for validation of the in-situ PPE. . 74   
5.4 Output of the in-situ PPE when the gain of in-line amplifer 2 (highlighted in   
red in the link schematic) is attenuated by 1 and 2 dB (black and red curve,   
respectively). . 75   
5.5 Output of the in-situ PPE when four launch power regimes, i.e., 0, 4, 8 and 12   
dBm, are evaluated. 76   
5.6 Output of the in-situ PPE and spectrum for a C-band single-channel and   
C+L-band multi-channel transmission. . . . . . 77   
5.7 a) Longitudinal power profle (blue curve) and span-wise linear fts (red curves)   
used to estimate the gain $G _ { i }$ (for a fxed wavelength) of the i-th in-line amplifer,   
scheme to perform the b2b validation of the in-line amplifer gain, and example   
of input and output spectra, when the channel’s central wavelength is 1585 nm. 79   
5.8 Link tomography for the estimation of the spectral gain profle. . 80   
5.9 Comparison between gain spectrum obtained from OSA and from link   
tomography for the in-line EDFAs. 81   
5.10 a) The estimated gain spectrum of the AUT 1 in the operation mode, where no   
link manipulation is performed to maintain constant input power at the input of   
the AUT, a method for detecting anomalies, such as gain tilt and narrowband   
gain compression due to SHB, in the AUT 1, a map that indicates the presence   
and types of faults, such as gain tilt and narrowband gain compression, and a   
comparison of the gain spectra of the AUT 1 under normal conditions and with   
emulated gain tilts. . . 83   
5.11 Result of the anomaly indicator when a weak and strong tilt are emulated (for   
C-band) on the in-line EDFA 1 by adding a wavelength-dependent attenuation   
profle. . 85   
5.12 The proposed anomaly detection method is applied to visualize a 5-dB   
narrowband gain compression at 1582.5 nm, simulating the efect of the SHB   
on the L-band. 85   
5.13 Setup used in the Experiment II, where a multi-channel analysis is performed   
to detect tilt evolution caused by the optical amplifers. 86   
5.14 Link tomography obtained in Experiment II (multi-channel analysis). 87   
5.15 Power peak curves obtained from the link tomography obtained at b) input   
of the OLS, and output of the in-line EDFA c) 1, d) 2 and e) 3 link, when   
compared against spectrum from an OSA. 88

## List of Tables

5.1 Summary of relevant works concerning Rx-DSP OPM approaches. 65

## Abbreviations

ACO analog coherent optics 11   
ADC analog-to-digital converter 8   
ASE amplifed spontaneous emission 75   
ASIC application specifc integrated circuit 8   
AUT amplifer under test 79   
AWG arbitrary waveform generator 52   
AWGN additive white Gaussian noise 35   
b2b back-to-back 5   
BER bit-error ratio 35   
BO Bayesian optimization 42   
BPF bandpass flter 86   
BPS blind phase search 20   
CD chromatic dispersion 17   
CDC chromatic dispersion compensator 69   
CFP C form-factor pluggable 9   
CMA constant modulus algorithm 19   
CRF coherent receiver frontend 36   
CUT channel under test 86   
CW continuous wave 14   
DA driver amplifer 7   
DAC digital-to-analog converter 7   
DAEQ data-aided equalizer 69   
DBP digital backpropagation 64   
DC direct current 26   
DCO digital coherent optics 11   
DD-LMS directed-decision least mean-square algo  
rithm 19   
DFA doped fber amplifer 3   
DP dual-polarization 5   
DPD digital pre-distortion 5   
EDFA Erbium-doped amplifer 53   
EI expected improvement 45   
FEC forward-error correction 4   
FFT fast Fourier transform 20   
FIR fnite-impulse response 19   
GBIC gigabit interface converter 9   
GP Gaussian process 44   
GVD group velocity dispersion 17   
HS hypothesis space 44   
HT hyperparameter tuning 44   
I in-phase 5   
IL insertion loss 30   
ILA indirect learning architecture 50   
IM/DD intensity modulation / direct detection 9   
InGaAlAs Indium-Galium-Aluminium-Arsenide 26   
InP Indium-Phosphide 5   
ISI intersymbol interference 12   
LO local oscillator 16   
LS least-squares 43   
LSB least signifcant bit 13   
MB multiband 2   
MF matched flter 69   
MIMO multi-input multi-output 1   
MMI multi-mode interference 5   
MOS metal-oxide-semiconductor 11   
MP memory polynomial 56   
MSA multi-source agreement 9   
MZM Mach-Zehnder Modulator 14   
NL nonlinear 70   
NLPR nonlinear phase rotation 64   
NLSE nonlinear Schrödinger equation 66   
NMSE normalized mean squared error 47   
OLS open line system 69   
OMFT optical multi-format transmitter 52   
OPM optical performance monitoring 63   
OSA optical spectrum analyzer 79   
OSNR optical signal-to-noise ratio 35   
OTDR optical time-domain refectometer 64   
p2p point-to-point 7   
PIC photonic integrated chips 11   
PPE power profle estimator 63   
PSK phase shift-keying 20

Q Quadrature 5

QAM quadrature amplitude modulation 5

QSFP-DD quad small form-factor pluggable - double density 9

RF radio frequency 11

RLS recursive least-squares 50

RRC root-raised cosine 36

RTO real-time oscilloscope 52

Rx receiver 8

SDM spatial-division multiplexing 1

SFP small form-factor pluggable 9

SH sample-and-hold 16

SHB spectral hole burning 64

SMF single mode fber 2

SNR signal-to-noise ratio 20

SOA semiconductor optical amplifer 3

SPM self-phase modulation 76

SR splitting ratio 30

SRS stimulated Raman scattering 2

SSC spot-size converter 26

SSFM split-step Fourier method 66

SUT system under test 43

Tx transmitter 7

VHDL very high speed integrated circuit hardware description language 12

VOA variable optical attenuator 53

VoD video-on-demand 1

WDM wavelength-division multiplexing 1

WSS wavelength selective switch 4

XPM cross-phase modulation 76

## Introduction

## 1.1 Beyond WDM systems

As of January 2021, an approximate number of 4.66 billion Internet users has been estimated worldwide (59% of the global population) [1]. In spite of the relatively disseminated Internet penetration across the globe, the increasing demand for data-hungry applications has required enhanced network infrastructures capable to support high-bandwidth services. Online video-ondemand (VoD) platforms for the consumption of movies and series, for example, have sparked a rise in Internet throughput in the past decade to meet the urge of consumers for uninterrupted streams and smooth browsing experiences [2, 3]. Additionally, the recent events related to the 2020 COVID-19 pandemic have just shown how dependent on connectivity the modern society is for work, education, social activities, and entertainment [4]. In this new age of remote interactions, optical networks play a fundamental role in providing reliable Internet operation since 95% of the Internet data trafc is transferred over optical fber cables [5]. Therefore, one of the main concerns for network operators is the realization of innovative approaches that increase the achievable capacity of commercial wavelength-division multiplexing (WDM) systems, while avoiding trafc congestion.

The success of such innovative solutions highly depends on how efciently the fve physical properties of light (time, quadrature, polarization, space and frequency) are utilized to modulate/multiplex data [6]. For instance, the spatial property, embodied in the light spatial modes, can be used to parallelize transmission via multiple physical propagation media (e.g., multiple cores in a single fber [7]), and scale capacity with respect to single-core transmission [8]. Such an aggregation scheme is technically known as spatial-division multiplexing (SDM) and has been claimed as a promising alternative to override the capacity crunch [9]. Nevertheless, implementation issues, namely, (1) hardware update (e.g., multi-input multi-output (MIMO) digital signal processing (DSP) modules [10], SDM amplifers [11]) and (2) fber deployment costs [12], still stand as major challenges for the successful commerical operation of SDM systems. Bearing in mind the business-limiting aspects imposed by (2), ongoing eforts concentrate on the realization of solutions that can spectrally extend the already existing

WDM infrastructure towards new optical transmission bands. These multiband (MB) systems provide a cost-efective exploitation of the full transmission window of single-mode fibers (SMF)s, i.e., approximately 40 THz of bandwidth, and can be considered as a near-term solution to cope with the rapid trafc growth [13].

## 1.2 Optical MB systems

In fber-based optical communications, transmission can be mainly performed in the fber low-loss region (1260 - 1625 nm), which has been conventionally named as “low-loss” due to the fact that within this wavelength interval the standard propagation media ofer the minimum attenuation. This region consists of the O- (1260 - 1360 nm), E- (1360 - 1460 nm), S- (1460 - 1530 nm), C- (1530 - 1560) and L-band (1560 - 1625 nm), as depicted in Figure 1.1.a). Yet, despite the broad range of the telecom optical spectrum (∼360 nm), conventional transmission systems are still predominantly carried out over C+L-band. However, nowadays a trend towards the extension of the conventional transmission window (C+L-band) to enable WDM systems for operation in MB regime, i.e., harnessing O-, E-, and/or S-band, is already noticeable. This trend can be better visualized when considering the amount of ongoing eforts to explore these additional bands as means of increasing the capacity (e.g., throughput1) in SMFs. Figure 1.1.b), for instance, summarizes the recent progresses [14, 15, 16, 17, 18, 19, 20] quantifed by record breaks in throughput by using C+L- and S+C+L-band WDM systems as a function of the propagation distance, with the maximum capacity achieving 206.1 Tbit/s in one single fber [14]. One of the main reasons for this growing interest in MB systems is the possibility to maximize the return on investment of already deployed optical infrastructure, which in contrast to other competitive solutions (e.g., SDM), can greatly reduce deployment costs [21]. Obviously, the MB option still presents numerous challenges, as discussed below.

![](/img/mineru_output/DSP_Algorithms_Intelligent_Optical_Coherent_Transceivers_RibeiroSena_24p/auto/images/e216ef4365cf700468ccd1cfc3c4c7eed20d23036450b283bb31a6cc7f7613fa.jpg)

![](/img/mineru_output/DSP_Algorithms_Intelligent_Optical_Coherent_Transceivers_RibeiroSena_24p/auto/images/4f4ed497c3d89717ac4f9387e4128a4f846e8fbe47d854a999e41ff6f8e87975.jpg)  
Figure 1.1: a) Optical MB spectrum. b) Throughput records in SMF using WDM MB systems.

In such a novel MB transmission scenario, fber- and component-induced efects need to be better understood and their impairments adequately addressed. The stimulated Raman scattering (SRS), for example, is an important MB nonlinear process present in optical fbers when high-frequency channels amplify low-frequency channels in the optical spectrum [22]. For transmission over conventional C-band systems, the SRS can be most of the time neglected. Nevertheless, with the progressive rise of commercial C+L-band systems, a demand for accurate channel models [23] that can predict the impact of such nonlinear efects has become a key enabler to improve the management of network resources (e.g., spectrum, route [24]) and properties (e.g., power [25]). Another important aspect to secure a successful migration from today’s C-band based optical networks to a MB scenario heavily relies on the development of novel MB optical devices. Amplifers [16] and flters [26] must be designed such to provide the best performance for each band. In that regard, signifcant progress has been lately achieved in the context of amplifcation technologies, e.g., rare earth components (Erbium-, Thulium-, Neodymium-, Praseodymium-doped fiber amplifers (DFA) [21]), Bismuth-DFA [27], Raman [28] and semiconductor optical amplifers (SOA) [19]. As for transceivers, which is the focus of this work, the three most prominent solutions are based on Lithium Niobate $\left( \mathrm { L i N b O _ { 3 } } \right)$ [29], Silicon Photonics [30] and III-V semiconductor materials (e.g., Indium Phosphide [31]). Despite the multiple benefts that these materials can ofer to the transceiver design, which is later approached in this thesis, wavelength-dependent impairments of linear [32] or non-linear [33] nature can provoke uneven performance across their operational spectrum. In order to mitigate such efects and relax device design specifcations, DSP algorithms play an important role as they are a cheap solution to counter-balance component-induced distortions [34]. This strategy can reduce the cost-per-bit of MB network implementation and help the short-term deployment of MB technologies.

Besides mitigating transmission efects, DSP algorithms can also serve for monitoring purposes in MB networks. This is possible because fundamental properties of the deployed optical fber and in-line devices can be extracted from the processing of the digitized signal samples [35], i.e., at the transceiver level. Thus, by aggregating the information from multiple transceivers, one can estimate link characteristics in the wavelength domain as well as in the spatial domain and create indicators of the health of network elements across complex networkwide topologies [36]. With these indicators, network operators are able to map unknown portions of the infrastructure and locate faults without need of expensive measurement equipment.

Enabling DSP algorithms to mitigate and sense component-induced and wavelengthdependent efects of optical coherent systems is a frst step towards the establishment of cognitive optical networks. In these networks, systems will be able to “... perceive current conditions, and then plan, decide, and act...” [37]. To better understand the benefts of cognition in the context of optical communications, the following discussion is provided.

## 1.3 Cognitive optical networks

The concept of cognitive/autonomous systems was frst described by IBM in 2001 and its essence consists of freeing system administrators from the details of operation and maintenance to provide services that run at optimal performance 24/7 [38]. Particularly, a cognitive network is any network that can confgure, monitor and maintain itself with minimal or no human intervention. These networks have gained importance over the past years because of their self-management capabilities, which means that they can [39]:

• seamlessly adjust their component confgurations (self-confguration),

• continually improve their performance (self-optimization),

• automatically detect and repair problems (self-healing),

• act to anticipate and prevent system failures (self-protection).

From a business perspective, cognitive networks are an attractive tool for operators because they yield economic gains in at least three diferent ways.

1. To avoid loss of revenue from service downtime. Due to network suboptimal management caused by human intervention, resource shortage, especially during “trafc peak hours,” can cause periods of service unavailability (downtime) and directly impact revenue. Self-optimization impedes that cognitive networks reach such a degree of resource depletion and consequently makes operation more robust to failure.

2. To reduce people-related costs. Expenses associated with staf, working facilities and training activities can be drastically minimized, given that typical network teams in charge of planning and provisioning tasks may be at least partially replaced by systems that realize self-confguration.

3. To reduce fault-related costs. By preventing failures (self-protection) and assertively identifying the fault location/reason (self-healing), operators can reduce maintenance routines and minimize costs.

In the feld of optical communications, cognition has been explored because of its key role in efciently handling and jointly optimizing the massive plurality of the underlying physical layer parameters (e.g., modulation format, power level, wavelength) and network layer parameters (e.g., bandwidth, lightpath, latency). This consequently leads to optimal end-to-end confgurations that would be impossible to achieve via manual intervention from a human-based network administration. A few successful examples of cognitive mechanisms in the optical layer are: gain automation in optical amplifers [40]; failure detection and identifcation based on spectrum monitoring for reconfguration of intermediate wavelength selective switches (WSS)s [41]; modulation format [42] and forward-error correction (FEC) scheme adaptation [43].

When it concerns the enabling of cognitive mechanisms in optical networks, transceivers are key elements. In charge of the generation and reception of the optical signal, transceivers have the capability to adapt transmission parameters, such as modulation formats, FEC coding schemes and spectral aggregation. Additionally, transceivers can behave as monitoring devices, permitting the estimation of network properties and sensing of disrupting events. These features, i.e., adaptability and monitoring open opportunities to incorporate network automation in multiple fronts.

## 1.4 Scope of this thesis

In this thesis, the previously introduced topics, i.e., optical MB systems and cognitive optical networks, are merged and studied in the design and application of intelligent DSP algorithms.