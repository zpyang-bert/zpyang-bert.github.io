---
layout: post
title:      "LPO serdes oDSP"
date:       2026-04-21 12:01:24
author:     "Bert"
tags:
  - DSP
  - Fundamentals
  - Paper
  - SerDes
---

Linear Drive enables Green All-Optical
Connectivity for Datacenters
Sponsored by IPEC
March 21, 2023

2

Agenda:
Part 1 (60 minutes):

Part 2 (60 minutes):

•

Welcome message from IPEC

•

Macom

•

Nvidia

•

Ranovus

•

Meta

•

Nubis Communications

•

Huawei

•

Arista

•

Serialink Systems

•

Source Photonics

•

Q&A and Discussion – 10 min

•

Q&A and Discussion - 20 min

QUARTERLY MARKET UPDATE | DECEMBER 18, 2019

LINEAR DRIVE WEBINAR l MARCH 2023

Open ·Unified ·Equality ·Innovation

Dr. Zhang Hua

Chair, IPEC Marketing & Education Committee

Who we are …
Our Members

41 members including the network operators, Internet service providers, system

IPEC
International

manufacturers, chip/module/component vendors, and research institutes, etc.

Our Mission
Open

Unify

Photonics &
Electronics

Committee

Equality

Innovation

Key Projects and Progresses

2020.10
• Initiated the 800G 500 m
and 2 km project

2021.12

2022.12

• Initiated the Mobile Fronthaul 50G
(MFH50) project

• Initiated the 800G interoperability
standards project

• Determined the objectives of the
800G Gen1 10 km project

2022.6

2021.8

• Initiated the optical network
intelligent O&M project

• Initiated the 100T+ OIO
research project

2022.4

Linear Drive
Technologies

• Initiated the OIO PELS project

2021.4
2022.1

• Initiated the 400G interoperability
standards project

2020

2023

2021

• Initiated the 100 Gbit/s BIDI project

2022

2023
Coming Soon …

400GE Interoperability Test SPEC

800GE IA Draft 2.0

September 2022, Released

December 2022，Released

MFH50 White Paper
OIO White Paper
800G Test SPEC.

……

Linear Drive Technology
Linear drive technology , as a new topic that has attracted wide attention in the industry.

Will linear drive technology be an effective method for reducing system power consumption?

Digital Signal Evolution
Host

CDR

oDSP
O/E

energy efficiency.

✓ CDR/DSP-based architectures still face
thermal issues.

oDSP
O/E

1. Bring optical components closer to ASIC chips
2. Significantly reduce per-bit costs and improving

Pluggable Optics
VSR

VSR

ASIC

XSR+

Host

ASIC

XSR+

Nowadays

OIO (OBO/NPO/CPO) OE

✓ Evolution from Pluggable to Optical
Input/Output (OIO)

Analogue Signal Evolution
Host

Linear Transceiver

✓ Introduction of the Linear Transceiver
technology for applying pluggable optics
and OIO optics.
1. Lower power consumption

ASIC oDSP

O/E

2. Lower latency

3. Lower costs`

Build a Booming Optoelectronic Ecosystem
03/2023
Linear Drive Enables Green All-Optical Connectivity for DCs
07/2022
Together with LightCounting
Next-Generation Fronthaul Optical Technical Directions

02/2022
Together with CIOE and EPIC
Research on the 100T+ CPO/OIO technology

09/2021
Shenzhen World Exhibition & Convention Center
International Standards and Industry Development Summit

06/2021
Together with CIOE and EPIC
Hosted a global academic webinar in the
photoelectron field

Thanks

WHY IS LINEAR DRIVE IMPORTANT?
CRAIG THOMPSON, NVIDIA
MARCH 21ST 2023

Challenges from System Perspective
Growing gap between memory demand and supply

 A Supply & Demand problem
 Scale-Out as we Scale-Up
 Create larger native GPU
Domains (hundreds to
thousands)
 Cluster sizes growing from
10’s racks to 100’s racks
 -> 10’s meters to 100’s
meters

 Provide ‘enough’ bandwidth
between all GPUs to keep
them fully utilized

Challenges from System Perspective
Growing gap between FLOPS demand and supply

DATA CENTER NETWORK

Emerging AI/ML Clusters

MoR and EoR Switches
All-to-All connectivity
Placed further away if
rack-power limited

NDR IB or 400GbE
•Up to 4Tb/s per server
•100’s meters

H100 Server
8x H100 GPUs
24TB/s memory BW

GPU-GPU FABRIC

3.6Tb/s per GPU
28.8Tb/s for 8x GPUs
256 GPUs per cluster
10’s meters (cluster scaling)

WHY IS LINEAR DRIVE IMPORTANT?
4Tb/s
100s meters
1000s GPUs

28.8Tb/s
10s meters
256 GPUs

WHY IS LINEAR DRIVE IMPORTANT?
4Tb/s
100s meters
1000s GPUs

GPU SERVER POWER
 4.0Tb/s per GPU = 40W per GPU for retimers
 x32 GPUs per rack = 1,280W
 Allocate power to GPUs = 10-15% cluster
performance benefit
 or power savings where rack-power limited

 PCIe card also limits module power to ~10W
 Goal is <4W multimode, <8W singlemode for
800G interface

28.8Tb/s
10s meters
256 GPUs

WHY IS LINEAR DRIVE IMPORTANT?
4Tb/s
100s meters
1000s GPUs

GPU SERVER POWER
LATENCY ON GPU-GPU FABRIC
 28.8Tb/s across 8 GPUs
 Latency limits reach or throughput
 Extend to switch next
 Pluggable when we can; CPO when we must

28.8Tb/s
10s meters
256 GPUs

DEMONSTRATION OF NVIDIA 100G SERDES AND LINEAR, NON-RETIMED OPTICS

Summary:
• AI/ML clusters are driving new applications of optical
interconnect
• Interconnect power, power density and latency are limiting
factors in AI/ML performance scaling
• NVIDIA is investing in linear, non-retimed technology to
alleviate these limitations
• Initial testing and demonstrations of the technology show
that it is feasible with DSP-based SERDES

Perspective on Linear Direct Drive Pluggable Optics

Janet Chen, Ph.D.
Technical Sourcing

Growing Power Allocation for Networking
DC Power Utilization

Network Traffic

~10X

& Cost/BW

Network

Other

IT

IT Other

Machine-to-User
Machine-to-Machine

• Networking is consuming a higher proportion of the data center power budget
• Technology innovation to enable a downward shift of the curve

Interconnect solutions for DC networks
Optics in Meta DC

Power
(pJ/bit)

Switch
Capacity

Host
Interface

Fabric PMD

12.8T

25G
NRZ

100G CWDM4

25.6T

50G
PAM4

200G FR4

51.2T

100G
PAM4

400G FR4

102.4T

200G
PAM4

800G FR4*

CPO

DSP-based FR4
DSP-based FR4 Lite

E.g. Link budget
relax for 500m
Linear Drive
(DSP-free)
Linear FR4 Lite

POR today

Pluggable

Tighter E/O
integration

< 2m (intra rack)
< 500m (intra DC fabric)
< 3km (intra DC region)

DAC

Cost ($/Gbps)

Challenges & Opportunities
Retimed Pluggable
Power
Cost
Latency
Product Maturity
Serviceability
Late Binding Commitment
Link Performance
Link Accountability
Interoperable Ecosystem

Linear-Drive Pluggable

Linear-Drive CPO

Perspective on Linear Drive Pluggable Optics
Opportunities

●
●
●

Power and cost
Staying pluggable: serviceability, flexibility, and can leverage proven
optics technology and manufacturing process
Pave the way for non-retimed CPO

Challenges
●
●
●

Robustness and Interoperability: TBD
Reduced link performance accountability
Scalability:
○ Standardization of TP1a & TP4 spec and testing methodology
○ Ecosystem and avoid vendor lock-in
○ Backward compatibility
○ 200G/lane?

Summary
●

Ever growing network demand calls for accelerating improvements in power and cost
efficiencies

●

Linear drive pluggable optics potentially strikes the balance between benefits and risks
○
○

●

Clear values in reducing power, cost and staying pluggable form factor
Challenges on robustness, interoperability, and scalability are yet to be addressed

Requires industry-wide efforts to achieve the needed robustness and scaling
○ We need a broad and robust solution to apply it widely at scale
○ Collaborate to build the ecosystem - time is of the essence!

Thank you

System Modeling of Linear Transceivers:
Challenges and Opportunities for
Link Performance Analysis

Aleksey Tyshchenko, Ph.D.
22 March 2023
1

Outline
• Historical perspective: how did we get here?
• Challenges of linear drive (non-retimed) link modeling
• Path towards simulation-based standard definition

2

Historical Perspective: How Did We Get Here?
Host

Host

• Two hosts in a data center (DC) need to communicate over a reliable link at high data rates
• Both hosts process information in electrical domain

3

Historical Perspective: How Did We Get Here?
Host

Host
TX

Host

Host
RX

• Two hosts in a data center (DC) need to communicate over a reliable link at high data rates
• Both hosts process information in electrical domain
• Add a transmitter (TX) and a receiver (RX) to the hosts

4

Historical Perspective: How Did We Get Here?
Host

Host
TX

Electrical Channel

Host

Host
RX

• Two hosts in a data center (DC) need to communicate over a reliable link at high data rates
• Both hosts process information in electrical domain
• Add a transmitter (TX) and a receiver (RX) to the hosts
• Connect the hosts over an electrical channel
• However…

5

Historical Perspective: How Did We Get Here?
Host

Host
TX

Electrical Channel

Host

Host
RX

• Two hosts in a data center (DC) need to communicate over a reliable link at high data rates
• Both hosts process information in electrical domain
• Add a transmitter (TX) and a receiver (RX) to the hosts
• Connect the hosts over an electrical channel
• However, with growing data rate demands, electrical channels cannot scale efficiently
• What is the next best alternative?

6

Historical Perspective: How Did We Get Here?
Host

Optical Fiber

Host

Host
TX

Host
RX

• Use low-loss high-bandwidth optical fiber to transmit data over required distances
• However…

7

Historical Perspective: How Did We Get Here?
Host

Host
TX

Electro-Optical Module

Optical Fiber

Opto-Electrical Module

Host

Host
RX

• Use low-loss high-bandwidth optical fiber to transmit data over required distances
• However, electrical signals need to be converted to optical, and then back to electrical
• Electro-optical (EO) and opto-electrical (OE) modules take care of this conversion

8

Historical Perspective: How Did We Get Here?
Host

Host
TX

Electro-Optical Module

Module
RX

Optical Fiber

Opto-Electrical Module

Host

Host
RX

• Use low-loss high-bandwidth optical fiber to transmit data over required distances
• However, electrical signals need to be converted to optical, and then back to electrical
• Electro-optical (EO) and opto-electrical (OE) modules take care of this conversion
• First, host transfers data to EO module over electrical link, and the module restores this data

9

Historical Perspective: How Did We Get Here?
Host

Host
TX

Electro-Optical Module

Module
RX

DRV
E to O

Optical Fiber

Opto-Electrical Module

Host

Host
RX

• Use low-loss high-bandwidth optical fiber to transmit data over required distances
• However, electrical signals need to be converted to optical, and then back to electrical
• Electro-optical (EO) and opto-electrical (OE) modules take care of this conversion
• First, host transfers data to EO module over electrical link, and the module restores this data
• Next, EO module uses restored data to drive electro-optical converter and to send the data

10

Historical Perspective: How Did We Get Here?
Host

Host
TX

Electro-Optical Module

Module
RX

Optical Fiber

Opto-Electrical Module

DRV

TIA
E to O

O to E

Host

Host
RX

• Use low-loss high-bandwidth optical fiber to transmit data over required distances
• However, electrical signals need to be converted to optical, and then back to electrical
• Electro-optical (EO) and opto-electrical (OE) modules take care of this conversion
• First, host transfers data to EO module over electrical link, and the module restores this data
• Next, EO module uses restored data to drive electro-optical converter and to send the data
• Then, OE module converts received optical signal to electrical, prepares it for data recovery

11

Historical Perspective: How Did We Get Here?
Host

Host
TX

Electro-Optical Module

Module
RX

Optical Fiber

Opto-Electrical Module

DRV

TIA
E to O

O to E

Module
TX

Host

Host
RX

• Use low-loss high-bandwidth optical fiber to transmit data over required distances
• However, electrical signals need to be converted to optical, and then back to electrical
• Electro-optical (EO) and opto-electrical (OE) modules take care of this conversion
• First, host transfers data to EO module over electrical link, and the module restores this data
• Next, EO module uses restored data to drive electro-optical converter and to send the data
• Then, OE module converts received optical signal to electrical, prepares it for data recovery
• Finally, OE module restores digital data, and sends it to far end host over an electrical link
12

Electrical and Optical Domains of a Serial Link
Electrical Domain

Host
TX

Module
RX

Optical Domain

Electrical Domain

DRV

TIA
E to O

O to E

Module
TX

Host
RX

• This topology breaks the serial link system into three domains
• Near-end electrical domain to bring data from source host TX to E-to-O converter
• Optical domain to facilitate long-range low-loss data transfer
• Far-end electrical domain to bring data from O-to-E converter to destination host

13

Electrical and Optical Standard Components
Electrical Standard

Host
TX

Module
RX

Optical Standard

DRV

Electrical Standard

TIA
E to O

O to E

Module
TX

Host
RX

• This also facilitates a convenient standard partitioning to electrical and optical parts
• Electrical standards define “chip-to-module” interfaces
• Optical standards define “optical links”
• Internal parts of EO and OE modules are not exposed, and therefore are not standardized
• Different tools are used to define electrical and optical standards

14

Is This Approach Scalable?
High Power Penalty

Host
TX

Module
RX

High Power Penalty

DRV

TIA
E to O

O to E

Module
TX

Host
RX

• Data recovery (re-timing) inside module RX & module TX comes at high power penalty
• Modules do not consume digital data, they only transduce data
• Data recovery (re-timing) facilitates data transfer between electrical and optical domains
• Re-timing is a non-linear operation: samplers that recover data symbols are non-linear
• With explosive growth of the number of ports in DC’s, every bit of power matters
• Is this approach sustainable? Is it sufficiently “green”?
• Can we do better?
15

Do We Really Need to Re-Time and Restore Digital Data?
Lower Power

Host
TX

EQ

Lower Power

DRV

TIA
E to O

O to E

DRV

Host
RX

• If modules do not consume data, why do we need to restore digital data?
• Can we support EO and OE conversion without restoring digital data?
• Let’s keep only the essential functionality: equalization and electrical driver
• This eliminates non-linear digital data recovery!
• Simpler functionality leads to lower power consumption
• Since we removed non-linear data recovery, let’s call this topology “linear” or “linear drive”
• Unfortunately, this is a very misleading link name…
16

Linear Drive (Non-Retimed) EOE Link Challenges
Host

Host
TX

Module

EQ

Optical Fiber

Module

DRV

TIA
E to O

Host

DRV

O to E

Host
RX

• Good news: from data centers’ point of views, the link topology remains unchanged
• Hosts interact with modules, while modules enable data transfer over optical fiber

17

Linear Drive (Non-Retimed) EOE Link Challenges
Electrical Domain

Host
TX

EQ

Optical Domain

Electrical Domain

DRV

TIA
E to O

DRV

O to E

Host
RX

• Good news: from data centers’ point of views, the link topology remains unchanged
• Hosts interact with modules, while modules enable data transfer over optical fiber
• We still have three well-defined link domains: electrical, optical, and electrical
• However…

18

Linear Drive (Non-Retimed) EOE Link Challenges
Electrical Impairments

Host
TX

EQ

+

Optical Impairments

DRV

+

TIA
E to O

Electrical Impairments

DRV

O to E

Host
RX

• Good news: from data centers’ point of views, the link topology remains unchanged
• Hosts interact with modules, while modules enable data transfer over optical fiber
• We still have three well-defined link domains: electrical, optical, and electrical
• However, lack of re-timers leads to compounding of E, O, E impairments
• Neither electrical, nor optical standard definition approaches are practical here

19

Linear Drive (Non-Retimed) EOE Link Challenges
Single End-to-End Opto-Electrical Standard

Host
TX

EQ

DRV

TIA
E to O

O to E

DRV

Host
RX

• Good news: from data centers’ point of views, the link topology remains unchanged
• Hosts interact with modules, while modules enable data transfer over optical fiber
• We still have three well-defined link domains: electrical, optical, and electrical
• However, lack of re-timers leads to compounding of E, O, E impairments
• Neither electrical, nor optical standard definition approaches are practical here
• A single, end-to-end, opto-electrical link standard is required
• How can we define this standard if optical components add non-linear impairments?
20

Linear Drive (Non-Retimed) EOE Link Challenges
How do we model end-to-end link to drive the standard development?

Host
TX

EQ

DRV

TIA
E to O

O to E

DRV

Host
RX

• Simulation-based definition is essential for a successful standard
• This topology mixes mostly linear electrical and non-linear optical modeling methodologies
• Neither electrical, nor optical methodologies are sufficient by themselves
• What can we do to help define linear drive (non-retimed) serial link standards?

21

End-to-End Linear Drive (Non-Retimed) Link Modeling
SeriaLink

Host
TX

EQ

DRV

TIA
E to O

O to E

DRV

Host
RX

• SeriaLink Systems has a parametric TX model: reflects non-linear effects in time domain

22

Parametric TX Model
Data Source

FFE

DAC

Pulse Shaping

Non-linearity

Launch Amp
A

tr

Clock Source

R_LM

SNR_TX

Noise Source

• We can enable/disable impairments
• Our starting point is 112 Gb/s long reach (LR) reference transmitter
• The model generates a representative transient TX waveform
23

End-to-End Linear Drive (Non-Retimed) Link Modeling
SeriaLink

Host
TX

SeriaLink

EQ

DRV

TIA
E to O

O to E

DRV

Host
RX

• SeriaLink Systems has a parametric TX model: reflects non-linear effects in time domain
• SeriaLink Systems has three flavors of parametric RX models
• Analog-centric RX
• ADC-based RX
• ADC-based RX with MLSE

24

Analog-Centric
(Sampler
Based,
Analog)
RX
channel IBIS
AMI
term

CTLE

1:64

DFE

FFE

VCO
off die

custom design

CDR

Legend
DREC

analog
analog/digital
digital
decision point

• This RX flavor would be the most abstract modeling approach
• We can use both FFE or DFE to equalize the signal
• However, this would not be representative of actual architectures
• Also, exploring MLSE impact with this approach would be misleading

25

ADC-Based RX
channel

IBIS

AMI

CTLE

ADC
CKREC

term

VCO
off die

4:64

S-param

÷ 16

DREC

DFE

CDR

CTRL

custom design

112 Gbit/s PAM4
56 GBaud/s
fN = 28 GHz

FFE

synthesized RTL
4 x 14 GS/s
5 bits/S
fCK = 14 GHz

Legend
analog
ADC
digital
decision point

64 samples in parallel
5 bits/S
fCK = 875 MHz

• This RX architecture would be the most adequate for this work

26

ADC-Based RX with MLSE

CTLE

ADC
CKREC

term

VCO
off die

4:64

S-param

÷ 16

MLSE

DREC

CDR

CTRL

custom design

112 Gbit/s PAM4
56 GBaud/s
fN = 28 GHz

FFE

synthesized RTL
4 x 14 GS/s
5 bits/S
fCK = 14 GHz

Legend
analog
ADC
digital

64 samples in parallel
5 bits/S
fCK = 875 MHz

• This RX architecture allows us to evaluate the MLSE trade-offs
• MLSE replaces DFE, clock recovery taps off before MLSE
27

End-to-End Linear Drive (Non-Retimed) Link Modeling
SeriaLink

Host
TX

S-Params

S-Params

EQ

DRV

TIA
E to O

O to E

DRV

SeriaLink

Host
RX

• SeriaLink Systems has a parametric TX model: reflects non-linear effects in time domain
• SeriaLink Systems has three flavors of parametric RX models
• Analog-centric RX
• ADC-based RX
• ADC-based RX with MLSE

• Electrical channel is a passive, linear system captured in the form of S-parameter network

28

End-to-End Linear Drive (Non-Retimed) Link Modeling
SeriaLink

Host
TX

S-Params

Partner 1

EQ

DRV

S-Params

TIA
E to O

O to E

DRV

SeriaLink

Host
RX

• SeriaLink Systems has a parametric TX model: reflects non-linear effects in time domain
• SeriaLink Systems has three flavors of parametric RX models
• Analog-centric RX
• ADC-based RX
• ADC-based RX with MLSE

• Electrical channel is a passive, linear system captured in the form of S-parameter network
• Working with Partner 1 to reflect time domain, parametric, behavioral optical link model

29

End-to-End Linear Drive (Non-Retimed) Link Modeling
SeriaLink

Host
TX

S-Params

Partner 2

EQ

Partner 1

DRV

TIA
E to O

O to E

Partner 2 S-Params

SeriaLink

DRV

Host
RX

• SeriaLink Systems has a parametric TX model: reflects non-linear effects in time domain
• SeriaLink Systems has three flavors of parametric RX models
• Analog-centric RX
• ADC-based RX
• ADC-based RX with MLSE

• Electrical channel is a passive, linear system captured in the form of S-parameter network
• Working with Partner 1 to reflect time domain, parametric, behavioral optical link model
• Working with Partner 2 to reflect behavioral models of EQ and DRV components
• This completes a parametric, time domain, behavioral model of the end-to-end link!
30

Performance Analysis
• SNR, BER at host RX
• Sample distributions though ADC-based host RX
• Eye diagrams where applicable
• We leverage simulated SNR to estimate link performance
• Once we get the whole link model working, we can explore system sensitivities
• We intend to use this link model to drive standard definition
• We are open to working with other partners on optical components

31

Linear Drive Enables Green All-Optical
Connectivity for Datacenters
Ryan Latchman
MACOM

Agenda

> Today’s Revolution

> Historical Evolutions when electrical interface
matches optical interface
> Host Interface Comparison & IEEE context
> Going Green in the Data Center

2

Today’s Revolution
(2023)
Source: Sunil Priyadarshi (Intel)

OSFP 800G Module

Electrical Interface

Other
TIA 5%
0%
10%

Driver
18%

DSP
49%

Retimed (DSP)

DSP Functionality consumes
~50% of SMF Modules

Laser
18%

OSFP 800G Module
Other
TIA 5%
0%
10%
Driver
18%
Laser
18%

DSP
49%

Linear

Material Power Savings
from removing DSP
(~50% reduction of power
for SMF modules)

3

A Historical View of Transceiver Evolution
(~2007)

XFP 10G Module

Electrical Interface

Retimed

SFP+ 10G Module
Limiting
(and smaller form factor)

PMD Interfaces
Maintained

4

53GBAUD Host Electrical Interfaces:
I/O Relative Power

~16dB

LR
Tx

ASIC

DSP

DR

VSR I/O+
LR I/O

TIA

LR
Rx

Optical
Module

100%
I/O Power = 2*(LR I/O) + 1* VSR I/O
=~12pJ/bit

~10dB
ASIC

Optical Interface requires LR I/O for
signal recovery
Pluggable modules leverage VSR
electrical Interfaces

Traditional Pluggable

LR
Tx

ASIC Power Consumption similar
across architectures (ASIC support
multiple configurations including
Passive Copper e.g. LR I/O)

DSP

DR

XSR I/O +
LR I/O

TIA

Optical
Chiplet

~80%
I/O Power = 2*(LR I/O) + 1* XSR I/O
=~10pJ/bit

LR
Rx

DSP requirements for Optical Interface
remain LR I/O, XSR interface saves
power in CPO chiplet at the expense of
channel loss support
ASIC remains LR I/O capable due to
multi-configuration use

Retimed CPO/NPO
LR
Tx

ASIC

~11dB

DR
Linear
TIA
Linear

LR
Rx

Linear Drive Pluggable / Linear CPO

Optical
Module

~45%
I/O Power = 1*(LR I/O) + 1* Linear I/O
=~5pJ/bit

Removal of DSP from module saves
material power consumption, latency,
and cost
Linear TIA/Driver functionality common
and therefore does not materially add
to power consumption when leveraging
Linear Interface
CEI-112G-Linear channel loss support
in alignment with passive copper5

ASIC Integration as seen at OFC’23

> Both Pluggable & recent CPO architectures are integrating DSP functionality in ASICs as a
primary power savings path***
• Revolution is well underway

> Pluggable Linear Drive supports historical benefits of pluggable while enabling power, cost,
and latency reductions
• Multiple Pluggable PMD types including SMF, MMF, Active Copper, Passive Copper

• Field Serviceability
• Traditional supply chain / manufacturing techniques
• At least 4 different module vendors had linear pluggable modules on the OFC’23 show floor
***
https://www.macom.com/updates/news/2023/macom-to-demonstrate-100g-lane-high-speed-optical-link-with-line
https://www.arista.com/en/company/news/press-release/17020-pr-20230228
https://www.broadcom.com/blog/broadcoms-persistent-cadence-copackaged-optics-innovation
https://blogs.cisco.com/sp/cisco-demonstrates-co-packaged-optics-cpo-system-at-ofc-2023
6

Optical Linear Drive in IEEE Context

> Linear Drive -> PMD Service Interface
> Often optical evaluation starts & ends electrically

7

MACOM PURE DRIVE™ Example

> MACOM offers Linear TIAs and Drivers supporting Linear Drive Optical applications
• SMF and MMF
• ACC linear copper equalizers as well

8

Going Green in the Datacenter

Green Optical
Connectivity
For Data
Centers

Reducing
Power
Consumption

Multiple PMDs
& Optimal
Partitioning of
Functionality

Pluggable
Linear Drive

9

23-11.3a A framework for developing non-retimed optical links
Jeff Hutchins / Ranovus
21 March 2023
21 March 2023
2023 LightCounting Linear Drive Webinar

A framework for developing non-retimed optical links

1

A framework for developing non-retimed optical links
q Motivation
q Types of non-retimed links
q Non-retimed applications
q Compliance requirements for non-retimed links
q Modeling performance of non-retimed optical links
q What is achievable with non-retimed links
q Summary
21 March 2023
2023 LightCounting Linear Drive Webinar

A framework for developing non-retimed optical links

2

Motivation
There has been significant interest in links with non-retimed interfaces for a variety of reasons:
q Reduced power consumption

Non-Retimed Optics Saves Power

q Improved density for co-packaging applications
q Reduced latency for latency sensitive applications

However, there are multiple different applications
for non-retimed links :
q Front panel pluggables
q Near packaged modules
q Co-packaged engines
q Die to die electrical links

We will examine the various applications and types of non-retimed links
21 March 2023
2023 LightCounting Linear Drive Webinar

A framework for developing non-retimed optical links

OFC2023 Panel - Optics in Future AI Systems:
Interconnects, Switching and Processing

3

A framework for developing non-retimed optical links
q Motivation
q Types of non-retimed links
q Non-retimed applications
q Compliance requirements for non-retimed links
q Modeling performance of non-retimed optical links
q What is achievable with non-retimed links
q Summary
21 March 2023
2023 LightCounting Linear Drive Webinar

A framework for developing non-retimed optical links

4

What is a Non-retimed interface?
Retimed pluggable

Socketed ASIC
ASIC

MR/LR SerDes

Pluggable Optics (retimed)
Electrical channel to the front panel equalized by the SerDes

ASIC Substrate / RDL

RDL

Host PCB (high performance material)
Co-packaged ASIC
ASIC

XSR SerDes

Retimed optical engine

Co-packaged using XSR (retimed)

E àO
Engine Substrate

XSR supports ~50mm (10dB) reach across substrate

Co-Packaged Assembly Substrate

Host PCB
Co-packaged (non-retimed)
Co-packaged ASIC
ASIC

LR SerDes

Non-retimed optical engine
DRV

E àO

Electrical channel to the OE equalized by the SerDes

Engine Substrate

Co-Packaged Assembly Substrate

Host PCB
21 March 2023
2023 LightCounting Linear Drive Webinar

A framework for developing non-retimed optical links

5

What is a Non-retimed interface?
Retimed pluggable

Socketed ASIC
ASIC

MR/LR SerDes

Pluggable Optics (retimed)
Electrical channel to the front panel equalized by the SerDes

ASIC Substrate / RDL

RDL

Host PCB (high performance material)
Co-packaged ASIC
ASIC

XSR SerDes

Co-packaged using XSR (retimed)

Retimed optical engine
E àO
Engine Substrate

XSR supports ~50mm (10dB) reach across substrate

Co-Packaged Assembly Substrate

Host PCB
SerDes equalizes entire link
Co-packaged ASIC
ASIC

LR SerDes

Non-retimed optical engine
DRV

Co-packaged (non-retimed)
Non-retimed optical engine

E àO

E àO

Engine Substrate

Engine Substrate

Co-Packaged Assembly Substrate

Co-packaged ASIC
LR SerDes

ASIC

Co-Packaged Assembly Substrate

Host PCB
21 March 2023
2023 LightCounting Linear Drive Webinar

DRV

Host PCB
A framework for developing non-retimed optical links

6

Some types of non-retimed & partially retimed links
Retimed*
MR Rx

ASIC
MR Tx

CDR
DSP
CDR

Non-Retimed – Host Tx Predistortion

Partially Retimed*
TIA

LR Rx

AGC

LR Rx

TIA

ASIC
DRV

XSR Tx

LR Rx

AGC

TIA

CDR

LR Tx
(α, β)

DRV

LR Tx

CTLE

DRV

Swing defined by IC technology (~0.8-1.0V)
Objective: OE independent specification

LR Tx

DRV

Non-Retimed – Engine Tx Predistortion
LR Rx

TIA

ASIC

ASIC

CTLE

Non-linearity compensation in SerDes

Non-Retimed – Direct Drive*
LR Rx

TIA

ASIC

OE Tx retiming increases margin
Non-Retimed – Linearly Amplified Drive*

AGC

ASIC
LR Tx

DRV

AGC

TIA

CTLE
+Nonlinear

DRV

Non-linearity compensation in OE

Swing defined by modulator technology

There are a variety of non-retimed alternatives to traditional retimed links
(*)

21 March 2023
2023 LightCounting Linear Drive Webinar

A framework for developing non-retimed optical links

Reference: OIF-Co-Packaging-FD-01.0 – Co-Packaging Framework Document

7

A framework for developing non-retimed optical links
q Motivation
q Types of non-retimed links
q Non-retimed applications
q Compliance requirements for non-retimed links
q Modeling performance of non-retimed optical links
q What is achievable with non-retimed links
q Summary
21 March 2023
2023 LightCounting Linear Drive Webinar

A framework for developing non-retimed optical links

8

What non-retimed channels should be supported?
Package ASIC
ASIC Substrate / RDL

Electrical Channel

Electrical Interface Configurations

Engine Die

Higher Loss
RDL

Host PCB

• Pluggable / On Board
ASIC Package + PCB Trace + Engine Attach
(traditional interface)

Engine Die

Packages ASIC
RDL

• Near-Packaged Interface
ASIC Package + Package Trace + Engine Attach
(reduced loss channel with a packaged ASIC)

RDL

HDI

Host PCB
Engine Die

Package
ASIC

RDL

Co-Packaged Assembly Substrate

Host PCB

socketed or
soldered

• Co-Packaged Interface
ASIC bump + Package Trace + Engine Attach
(short low loss channel with a flipped ASIC)
Lower Loss

Non-retimed links can be used in a wide variety of configurations
21 March 2023
2023 LightCounting Linear Drive Webinar

A framework for developing non-retimed optical links

9

What are the components of possible non-retimed links?
Data Rate
100G
200G
Wide I/Fs
Others?

Non-retimed
link
application

Electrical Channel
XSR: 10dB + link + 10dB
Front Panel Pluggable
Others?

Is a Standard possible?
Or must be designed as a
system?

Traffic Characteristics
Ethernet (w/FEC)
Low latency (e.g. PCIe)
Others?

Interoperability
Full (IMDD, coherent),
limited, or single vendor

The application space for non-retimed links consists of a large number of factors
Targeting specific applications will enable a well optimized solution
21 March 2023
2023 LightCounting Linear Drive Webinar

A framework for developing non-retimed optical links

10

A framework for developing non-retimed optical links
q Motivation
q Types of non-retimed links
q Non-retimed applications
q Compliance requirements for non-retimed links
q Modeling performance of non-retimed optical links
q What is achievable with non-retimed links
q Summary
21 March 2023
2023 LightCounting Linear Drive Webinar

A framework for developing non-retimed optical links

11

Compliance requirements for non-retimed links
Channel

Linear Amp
TP1

Non-linear
EàO

Link
TP2

OàE

Linear Amp

Compliance test points should be defined to ensure interoperability
q Between host and non-retimed module (TP1, TP4)
q Between various vendors and non-retimed EàO technologies (TP1-TP2, TP3-TP4)
Various EàO technologies have differing characteristics
q Consider the impact of non-linearity differences between EMLs, MZMs, VCSELs, etc.
q Consider the impact of packaging on IL (discrete, hybrid integration, monolithic integration)
q Consider the impact of IL from different placements (CPO, NPO, close proximity, front panel)
q Consider the impact of different non-retimed configurations (linearly amplified vs predistortion)
Increased margin is required to support interoperability as more technologies and
configurations are included

Compliance test points need to be defined to enable
interoperability for various technologies and packaging
21 March 2023
2023 LightCounting Linear Drive Webinar

Channel

TP3

A framework for developing non-retimed optical links

Host Rx

TP4
Applications
Defined Electrical Channels

Host Tx

CPO

10dB

NPO

13dB

Front
Panel
Full
Half
Nonretimed retimed
retimed
Retiming Implementation

12

A framework for developing non-retimed optical links
q Motivation
q Types of non-retimed links
q Non-retimed applications
q Compliance requirements for non-retimed links
q Modeling performance of non-retimed optical links
q What is achievable with non-retimed links
q Summary
21 March 2023
2023 LightCounting Linear Drive Webinar

A framework for developing non-retimed optical links

13

Broadly, there are two common questions
Can a particular non-retimed link work with a standard SerDes feature set (say LR)?

Can a particular non-retimed link work with a reduced power SerDes?
That is, what features need to be added or removed from a SerDes to enable a particular non-retimed link

21 March 2023
2023 LightCounting Linear Drive Webinar

A framework for developing non-retimed optical links

14

Accurate modeling of a non-retimed end-to-end link
Co-packaged (non-retimed)
Analog Optical Engine
MR/LR SerDes

Analog Optical Engine
MR/LR SerDes

Substrate

ASIC

Substrate

≤ 2km

Co-Packaged Assembly Substrate

ASIC

Co-Packaged Assembly Substrate

Host PCB

q
q
q

Host PCB

Tx SerDes (bare die)
Electrical Channel + LGA
Optical Engine Tx

q
q
q

q

Rx SerDes (bare die)
Electrical Channel + LGA
Optical Engine Rx

Fiber Model

Full end-to-end model including fiber should include all non-linearities and noise sources
21 March 2023
2023 LightCounting Linear Drive Webinar

A framework for developing non-retimed optical links

15

Dealing with inherent non-linearities of EàO conversion
Rx Non-linear Slicer Level Adjustment

Tx Non-linear Predistortion

+1+β

Rx Slicer Threshold

+3

β

+1
-1+α
-1

α

-3

Rx OMA

Tx FIR optimization coupled with adjusting levels for predistortion to improve the Tx optical eye linearity with parameters
(α, β)

Rx runs in adaptive mode for CTLE/AGC, FFE, and DFE

Non-linear predistortion can compensate for EàO non-linearities (EML, VCSEL, MZM, MRM, etc.)
21 March 2023
2023 LightCounting Linear Drive Webinar

A framework for developing non-retimed optical links

16

Impact of Tx Non-linear Predistortion

§ Impact on the end-to-end link performance
o

VS.

The “worst” PAM4 eye would dominate the
BER performance.

o

A more balanced PAM4 eye can reduce the
overall BER by a factor of 10.

The improved eye linearity has a
marked impact on BER

21 March 2023
2023 LightCounting Linear Drive Webinar

A framework for developing non-retimed optical links

17

An End-to-End optical link analysis
Analysis Example

SerDes
ASIC

ASIC Substrate / RDL

Optimizing a SerDes feature for a particular non-retimed link
q

3 tap Tx FFE, Rx CTLE, 1 tap DFE, 32 tap FFE

PCB C2C Trace (on Tx side and on Rx side)

Samtec 12dB IL channel (IEEE802.3 contribution)
“Channel Models for 100 Gb/s, 200Gb/s, 400 Gb/s C2C AUI”
(https://www.ieee802.org/3/ck/public/tools/index.html)

q

Engine

Engine
RDL

ASIC

ASIC Substrate / RDL

RDL

Host PCB

Host PCB

BER for Selected SerDes Features

LR SerDes used in a non-retimed link
•

q

End to End Link Channel

End to End simulation performed

Includes O-E, fiber, and E-O characteristics
Channel: 12dB + link + 12dB
Includes all effects such as non-linearities and noise sources

End-to-end simulation highlights the utility of various
SerDes features enabling optimization
21 March 2023
2023 LightCounting Linear Drive Webinar

LR SerDes

2e-8

LR SerDes+ Tx
non-linear
predistortion

2.9e-9

LR SerDes with
Rx DFE Disabled

6.3e-8

LR SerDes with
Rx CTLE Disabled

1.3e-7

LR SerDes with
Rx FFE Disabled

A framework for developing non-retimed optical links

1.5e-2
18

A framework for developing non-retimed optical links
q Motivation
q Types of non-retimed links
q Non-retimed applications
q Compliance requirements for non-retimed links
q Modeling performance of non-retimed optical links
q What is achievable with non-retimed links
q Summary
21 March 2023
2023 LightCounting Linear Drive Webinar

A framework for developing non-retimed optical links

19

What can be achieved with non-retimed implementations?
Retimed pluggable

Socketed ASIC
ASIC

Pluggable Optics (retimed)

15 pJ/b

MR/LR SerDes

ASIC Substrate / RDL

RDL

Host PCB (high performance material)

CDR
DSP

TIA

CDR

DRV

100G-DR8

Co-packaged (non-retimed)
Co-packaged ASIC
ASIC

LR SerDes

5 pJ/b

Non-retimed optical engine
DRV

E àO

Engine Substrate
AGC

TIA

Co-Packaged Assembly Substrate

Host PCB

DRV

A non-retimed solution offers significant power savings
21 March 2023
2023 LightCounting Linear Drive Webinar

A framework for developing non-retimed optical links

100G-DR8
20

Summary
There has been significant interest in links with non-retimed interfaces for a variety of reasons:
Reduced power consumption
q Improved density for co-packaging applications
q Reduced latency for latency sensitive applications
q

However, there are multiple different applications for non-retimed links and different configurations
For example, linearly amplified drive vs non-linear drive, pluggable optics vs co-packaging, non-retimed vs partially retimed
q Important to clearly define the specific configurations of interest
q

Compliance test points need to be defined to enable interoperability for various technologies and packaging
q

For example, the degree of interoperability: single vendor vs multi-vendor, single vs multiple technologies, packaging and IL differences

An opportunity exists to improving the performance of non-retimed links by optimizing the components
q

Tuning SerDes or optical engine elements to maximize power savings and maximize margins

Non-retimed links provide many advantages such as reducing power, but the specific configurations must be clearly defined
21 March 2023
2023 LightCounting Linear Drive Webinar

A framework for developing non-retimed optical links

21

Thank You!
RANOVUS Odin™

Multi Terabit platform for optical interconnect
21 March 2023
2023 LightCounting Linear Drive Webinar

A framework for developing non-retimed optical links

22

Linear Pluggable Optics
For 100G and 200G
Peter Winzer
Laurent Alloin, Son Le, and Pete Pupalaikis
March 21, 2023

Why Linear Pluggable Optics (LPOs)
Compute/Switch Box

Host
ASIC

LR
SerDes

MR SerDes O-DSP

Laser

Laser

Direct-Attach Cable (DAC)

0 W, 1 m

OE

Retimed Pluggable Optics

15 W, 2 km

OE

Linear Pluggable Optics

6 W, 2 km
*powers are for 800G

Advanced ASICs embed powerful SerDes to drive Direct-Attach Cables (DACs)
• Not much power savings by “powering down” LR SerDes to MR/VSR

Advanced Optical Engines (OEs) that “look like copper” can be driven by LR SerDes
è Halves pluggable optics power consumption
© Nubis Communications, 2023

2

Making Optics Look Like Copper
Copper

Optical

Electrical trace

Modulator, Driver, TIA

Electrical connectors

Opto-electronic components

Quantization, Jitter, Thermal

Thermal, Shot, RIN

Amplitude nonlinearities

–

Modulator, Driver, TIA

Time nonlinearities

–

Modulator

Nonlinear fiber impairments

–

CD, MPI, FWM

Bandwidth limitations
RF reflections
Noise

Linear
optics
minimiz
es these
issues

Unequal

Skew
Equal

Sampling point
mazzini_3bs_01_0914
© Nubis Communications, 2023

lyubomirsky_3db_01_1020

Sampling point
Nubis XT1600TM, measured at 106 Gbps
3

Making Optics Look Like Copper
•
•
•
•

Low-swing linear drivers and linear optical modulators
Linear optical receivers
Single-wavelength better than WDM
Very careful co-design of optics and electronics
NubisSim™ : End-to-End Design and Sign-off Tool
•
•

Accurately simulates full E-O-E channel
Sophisticated linear & nonlinear component models

Inputs
Actual device perf, layouts, channel models

© Nubis Communications, 2023

Outputs
waveforms, link budgets, error-rates

4

9” PCB Chip-to-Module Channel @ 100G
Compute/Switch Box

Host
ASIC

Compute/Switch Box

LR
SerDes
100G

LR
SerDes
100G

8 dB

2.5 dB
Laser

4 dB

1.5 dB

16 dB

(C2M, IEEE 802.3ck)

OE

2 km
DR+

OE

Host
ASIC

8 dB

2.5 dB
Laser

1.5 dB

4 dB

16 dB

(C2M, IEEE 802.3ck)

è Use 20 dB channel loss for margin
© Nubis Communications, 2023

5

Simulations With 20-dB Channel Loss @ 100G
20 dB
LR
SerDes
Tx IBISAMI

Customer
Channel

Connector +
Module
Snp
Termination

Driver
Snp

Driver
NL

Modulator
snp

Mod
NL

Fiber
CD, DGD, att,…

LR
Serdes
Rx IBISAMI

Customer
Channel

Connector +
Module
Snp
Termination

TIA
NL

TIA
snp

PD

20 dB
© Nubis Communications, 2023

6

Simulations With 20-dB Channel Loss @ 100G: TX
20 dB
LR
SerDes
Tx IBISAMI

Customer
Channel

Connector +
Module
Snp
Termination

Driver
Snp

Driver
NL

Modulator
snp

Mod
NL

ER = 3.9 dB, TDECQ 2.35
dB
© Nubis Communications, 2023

7

Simulations With 20-dB Channel Loss @ 100G: RX

BER = 3e-6

LR
Serdes
Rx IBISAMI

OMA = -3.3 dBm

Customer
Channel

Connector +
Module
Snp
Termination

TIA
NL

TIA
snp

PD

20 dB
© Nubis Communications, 2023

8

Linear Pluggable Optics: Scaling to 200G
Compute/Switch Box

Host
ASIC

LR
SerDes
200G

9 dB

4.0 dB
Laser

9.5 dB

2.0 dB

OE

è 40 – 50 dB SerDes reqmt for LPO
(w/o margin)
è Very challenging w/ existing
box arch.
(resolved by VLC, next slide)

25 dB (PCB)
20 dB (Twinax)
Loss numbers after https://www.ieee802.org/3/B400G/public/21_08/kocsis_b400g_01a_210826.pdf
Loss numbers after http://parallaxgroup.com/media/bg/2/designcon2013.pdf
© Nubis Communications, 2023

9

Vertical Line Card (VLC) Scales LPO to 200G
Switch

Pluggables

VLC (w/ PCB)

SerDes for LPO

100 Tbps

8 x 200G (OSFP) (x64)
16 x 200G (OSFP-XD) (x32)
16 x 200G (LPO Plugs) (x32)

20 dB
18 dB
14 dB

40 dB
36 dB
28 dB

200 Tbps

16 x 200G (LPO Plugs) (x64)

15 dB

30 dB

100T à 64 x OSFP

VLC à
© Nubis Communications, 2023

100T à 32 x OSFP-XD

•
•
•
•

100T à 32 x LPO Plug

200T à 64 x LPO Plug

Shorter PCB traces (9” à 2” – 5”)
Lower-loss connectors (2 dB, 4 dB à 1 dB)
Lower losses inside module (4 dB à 2 dB)
Enables LPO paradigm scaling 50T à 100T à 200T
10

Conclusions
• Linear Pluggable Optics save 50% of I/O power
• Feasible at 100G/lane using today’s SerDes and box arch
− Standardization, interoperability, link training open issues

• LPOs extend to 200G/lane using Vertical Line Card systems
− LPO-optimized pluggable form factors bring further benefits

© Nubis Communications, 2023

11

Thank You

Linear Drive Pluggable Optics (LPO)
Andreas Bechtolsheim
Arista Networks

Linear Drive Pluggable Optics Modules
1. Linear Drive means no DSP or CDR in Module
Just a linear driver to drive electro-optical modulator

2. Requires high-performance switch SERDES
And careful motherboard signal integrity design

3. Achieves same power ef ciency as direct drive CPO
While retaining the many advantages of pluggable optics modules

fi

Compared to the latest DSP Optics, Linear Drive Optics
reduce optics power by up to 50%, switch power by 25%

Why Now? Three Key Ingredients
1. Digital DSP based Switch SERDES
Capable of dealing with both electrical and optical channel

2. 100G SERDES speed matches 100G Optical Lambda
Optics with di erent Serdes/Lambda speeds requires gearbox

3. High Bandwidth Linear Drives and TIAs
High bandwidth is key to deliver the lowest BER

ff

Linear Drive works only with high-performance SerDes
and a high-quality electrical and optical channel design

DSP or Linear Drive
Optics

Electrical

Lambda

Implementation

400G

8x50G

4x100G

DSP/Gearbox

800G

8x100G

8x100G

LD or DSP

800G

8x100G

4x200G

DSP/Gearbox

1600G

8x200G

8x200G

LD or DSP

Linear Drive is not applicable to 400G optics (8x50G) with
100G Lambda, or 800G optics (8x100G) with 200G Lambda

Linear Drive Optics Modules
TFLN
SiPh
VCSEL
Modules provided by Eoptolink

Linear Drive works with any type of optics technology

Pre-FEC BER with Ethernet Traf c

fi

Measurements with Silicon Photonics Module

800G Pluggable Optics Power Evolution
12

15 pJ/Bit

SiPh

TFLN

VCSEL

12 pJ/Bit
9

Power measured with
Pluggable Optics Modules

10 pJ/Bit
pJ/Bit Calculated at 100G
All Power is typical at 3.3V

8 pJ/Bit
6

6.3 pJ/Bit
5 pJ/Bit

3

0
100G 5nm DSP

100G LD

Switch Power Savings with LD SiPh Optics
Switch

Switch

Fans+CPU

Optics

51.2T

-25%

51.2T-LD

102.4T

-25%

102.4T-LD
0

500

1000

1500

2000

2500 [W]

51.2T Power measured, 102.4T power projected
8

LPO and Direct Drive CPO Comparison
Form Factor

LPO

CPO

CPO Delta

DSP

N/A

N/A

Same

Linear Driver

Required

N/A

Lower Power

External Laser

N/A

Required

Higher Power

New EOM Tech

Supported

Not POR

Higher Power

Voltage Rail

3.3V

Device Voltage

Adjust for voltage

Projected Power

8 pJ/Bit SiPh
5 pJ/Bit VCSEL

7 pJ/Bit SiPh @ 0.8V
VCSEL N/A

Basically Same
for SiPh
9

The Problems Pluggable Optics Solve
1. Support any Type of Optics, Mix and Match
SR, DR, FR, ZR, AOC, Copper Cables

2. Support Multiple Optics Technologies
DML, EML, Silicon Photonics, VCSEL, TFLN, etc.

3. Enable Large Multi-vendor Ecosystem
All existing high-speed optics module vendors

4. Easy Serviceability in Case of Failure
Each module can be individually hot-swapped

5. Disaggregated Business Model
No margin stacking on optics

✓
✓
✓
✓
✓

Linear Drive Pluggable Summary
1. Same power as CPO in a Pluggable Form Factor
While retaining all the advantages of Pluggable Modules

2. Signi cant cost reduction compared to DSP Optics
DSP is the most expensive part in an optics module

3. Requires careful system design to achieve low BER
SerDes performance and electrical signal integrity is key

fi

LPO is the lowest risk way to reduce optics power and cost
while retaining all advantages of pluggable optics modules

Thank You

The Perspectives of Linear Optical
Pluggables for AI/ML Clusters
Frank Chang, Ph.D
Source Photonics
March 23, 2023
IPEC Webinar, “Linear Enable Green All-Optical Connectivity for Datacenters”, 2023.3.23
On behalf of Source Photonics and IPEC

Key Linear Drive discussion points
From Module Vendor Perspective
1

What drives the demand?

2

How linear play over CPO/NPO?

3

How to make “DSP free” happen?

4

How linear optics will be applied?

5

How to handle multi-vendor interop?

6

Upcoming Optics – 200G/Lambda

Slide no. 1

SourceConfidential
Photonics Confidential
and Proprietary
Source Photonics
and Proprietary

Facebook

Power Efficient is Key for Al Clusters
Major OFC/OCP Take-aways
► Al/ML clusters - a big driver for network bandwidth
► Today’s GPU drive 2x400G, later upgradable to 2x800G.

► Data center switching power comes increasingly from optical interconnects
► Linear drive can promise >25% total system power savings.

51.2T Power measured
102.4T power projected

Source: OFC’23 plenary
(with updates by Andy)
Slide no. 2

SourceConfidential
Photonics Confidential
and Proprietary
Source Photonics
and Proprietary

Why STOP using CPO/NPO for saving power?
CPO claim to reduce switch power by 30-40%

CPO

Pluggables

►

Lower power

►

Reliability

►

Lower latency

►

Manufacturability

►

High integration

►

Serviceability

►

Sipho focus

►

Leverage high BW optics

Lower cost
Linear Optical Pluggables
Source: OIF
Slide no. 3

SourceConfidential
Photonics Confidential
and Proprietary
Source Photonics
and Proprietary

Transceiver Power Consumptions (400 vs 800G)
400G & 800G optics modules with 100 Gb/s electrical lane ecosystem
400G DR4/FR4 at ~8W
HT (70℃) Power Consumption Composition Breakdown
1.0%

8.0%

800G DR8/FR8 at <13-14W
HT (70℃) Power Consumption Composition Breakdown

1.0%

1.0%

15.0%

2.0%
10.0%

10.0%

12.0%

15.0%

60.0%
65.0%

8x100G QSFP-DD800

4x100G QSFP56-DD
TEC

Laser

DSP

TIA

MCU

Other

Rough estimation with 7nm DSP
Slide no. 4

TEC

Laser

DSP

TIA

MCU

Other

Rough estimation with 5nm DSP

SourceConfidential
Photonics Confidential
and Proprietary
Source Photonics
and Proprietary

Transceiver Power Consumptions (800G vs. 1.6T)
Next 800G & 1.6T optics with the 200 Gb/s electrical/optical lane ecosystem
800G DR4/FR4 at ~11~12W

1.6T (8x200G) DR8/2xFR4 at <22W

Power Consumption Composition Breakdown HT
(70℃)

Power Consumption Composition Breakdown HT
(70℃)

1.0%

3.0%

7.0%

9.0%
10.0%

9.2%

12.8%

0.9%

8.9%
8.6%

800G scalable to 1.6T
200G/  Gen1 DSP
70.0%

59.6%

200G/  Gen2 DSP

4x200G QSFP-DD800

8x200G OSFP1600/QSFP-DD
TEC

Laser

DSP

TIA

MCU

Other

TEC

Rough estimation with 5nm DSP
Slide no. 5

Laser

DSP

TIA

MCU

Rough estimation with 3nm DSP
SourceConfidential
Photonics Confidential
and Proprietary
Source Photonics
and Proprietary

Other

How “DSP free” work?
Retimed Interface
400G QSFP112

10G XFP
4X
CDR
(EQ)

Driver TOSA
TIA

800G OSFP/QSFP-DD

ROSA

Driver
DSP/ (4:4) TOSA
4X100G
CDR
TIA
(4:4) (4:4) ROSA

Linear Drive Interface (eliminate DSP/CDR power and cost)
400G QSFP112
10G SFP+

Slide no. 6

4X

Driver TOSA

Driver/EQ
TOSA
(4:4)

TIA/LA ROSA

TIA/EQ
(4:4)

DSP/
CDR
(8:8)

Driver
(8:8) TOSA
8X100G
TIA
(8:8)

800G OSFP/QSFP-DD
Driver /EQ
(8:8)

4X100G
ROSA

SourceConfidential
Photonics Confidential
and Proprietary
Source Photonics
and Proprietary

ROSA

TOSA
8X100G

TIA/EQ
(8:8)

ROSA

High–speed 224Gb/s PAM4 EMLs

DC & RF probing station

RF testing PNA

f3dB ~65 GHz

Plus other high BW new materials:
- TFLN, BTO, Polymer MZM etc
- VCSELs

Slide no. 7

SourceConfidential
Photonics Confidential
and Proprietary
Source Photonics
and Proprietary

Explore linear module Line/Host I/O
Electrical input

TP2 Optical Eye

TECQ 3.6dB

TP1

TP4

TP4 Elec. Eye after O/E
TP3 stressed optical signal

Slide no. 8

SourceConfidential
Photonics Confidential
and Proprietary
Source Photonics
and Proprietary

Explore Linear Module Link Performance

TECQ 3.6dB

Slide no. 9

SourceConfidential
Photonics Confidential
and Proprietary
Source Photonics
and Proprietary

Channel model simulation

TECQ 3.6dB

Insertion Loss
Impulse after FFE

Impulse

RL incls PCB loss
Slide no. 10

SourceConfidential
Photonics Confidential
and Proprietary
Source Photonics
and Proprietary

OIF CEI Linear Interop Demo – It Works!

This interoperability demo consists of a 112G Linear test board receiving and converting an optical signal across single mode fiber being
transmitted by a remote-laser-source-driven optical engine to an electrical signal via PD+TIA. The electrical signal is then sent to a BERT which
integrates receive FFE functionality and achieves a link BER exceeding standard requirements. There is no discrete DSP in the Rx path before the
BERT, saving module power and cost.
SourceConfidential
Photonics Confidential
and Proprietary
Source Photonics
and Proprietary

THANK YOU!

Office locations
West Hills, CA

San Jose

Taiwan

8521 Fallbrook Avenue, Suite 200,

1731 Technology Drive, Suite 530

9F, No 81, Shui Lee Rd.

West Hills, CA 91304

San Jose, CA 95110

Hsinchu, Taiwan, R.O.C.

Tel: +1 (818) 773-9044

Tel: +1 (818) 773-9044

Tel: 886-3-5169222
Fax: 886-3-5169213

Fax: +1 (818) 773-0261

Shenzhen

Chengdu

Jintan

Building #2 & 5, West Export

#6 Building, No. 1036 Chenfeng Road,

2/F, EYANG Building, No.3 of Qimin Rd,

Processing Zone, No. 8 Kexin Road,

Jintan Development Zone,

Langshan 2nd Street, Hi-Tech Industrial

Hi-Tech Zone, Chengdu, 611731, China

Changzhou City, Jiangsu Province,

Park North, Nanshan District, Shenzhen,

Tel : (86) 28-87958788

China

518057, China

Fax: (86) 28-87958787

Tel : (86) 519-82999666

Tel : (86) 755-86139096
Fax: (86) 755-86139080

Wuhan
Room 902, Huigu Space-time Building,
No. 8 Senlin Road. East Lake High-tech
Development Zone, Wuhan, Hubei
Province, China
Tel : (86) 27-87592132

India
#54, 3rd Floor, 13th Main, 17th Cross,

Macau
2/A1, No. 369 Avenue

Section 6, HSR Layout,

Keng Ou, Commercial Building

Bangalore 560 101, India

2nd Floor, A1 Macau, China

Tel: +91-97400-12929

www.sourcephotonics.com

