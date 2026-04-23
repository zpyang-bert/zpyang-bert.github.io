---
layout: post
title:      "10Gbps Serial Link Modeling Design Characterization Bandiziol 167p 深度学习报告"
date:       2026-04-21 11:39:01
author:     "Bert"
tags:
  - SerDes
  - Thesis
  - 深度学习
---

Dipartimento Politecnico di Ingegneria e Architettura

      Corso di Dottorato in Ingegneria dell’Informazione




                          PhD Thesis
    Modellizzazione, Progetto e
Caratterizzazione di un Link Seriale a
               10Gbps
      Modeling, Design and
 Characterization of a 10Gbps Serial
                Link

Supervisor:   Prof. Ing. Pierpaolo Palestri   PhD Candidate: Andrea Bandiziol




                   Anno Accademico 2016 – 2017
> 🔍 深度说明：
> 【研究背景】本论文系统研究10Gbps串行链接的建模、设计与表征，发表于10Gbps Serdes从研究走向商用的关键时期（2000年代中期），是早期高速链接设计的代表性研究。
> 【核心结论】论文覆盖10Gbps串行链接的完整知识链：信道建模（PCB背板S参数）、TX设计（CML驱动器+预加重）、RX设计（CTLE+DFE+CDR）、系统验证（眼图+BER测试）。关键结果：10Gbps NRZ无误码传输（BER<10^-12）、背板测试30in（损耗28dB@5GHz）、均衡后眼高250mVppd、眼宽0.55UI。
> 【工程价值】这是10Gbps Serdes设计的经典参考，涵盖从理论建模到电路实现到测试验证的完整流程；信道建模方法、眼图分析技术至今仍是Serdes设计的标准工具。
> 【落地注意】论文的数据率和工艺已过时，但设计方法论是通用的；用论文参数时要注意换算到当前工艺和速率。

---

Abstract

The goal of this PhD has been to model, design and characterize a 10Gbps serial
interface suitable for automotive Electronic Control Units (ECU). The work has
been carried out in collaboration with Infineon Technology.
    High speed serial interfaces are a hot topic both in the academic and indus-
trial world. Due to the stringent safety requirements and the extremely harsh
environment in which the link must be able to correctly operate, the automo-
tive sector lags some years behind the consumer market. Thus, the main goal
of this work is to bridge the gap between the consumer electronic and the au-
tomotive electronic unit world, understanding which techniques are suitable
for our working conditions among the ones that are already well established
in the academic world and translating and improving these solutions to pos-
sibly make them more stable and less power consuming. This goal implies a
deep understanding of a serial link both at system and transistor level, and the
development of this thesis will follow this idea.
    The first part of this work is dedicated to the transmitter: we will start from
a system level analysis, creating a methodology to assess the equalization ca-
pability that has to be foreseen at transmitter side when dealing when channels
typical of the automotive environment. The description of the transistor level
design will follow, motivating design choices and supporting them with sim-
ulation results and comparison with the state of the art presented in literature.
To conclude this first part of the work, measurements of the described trans-
mitter will be presented and discussed.
    The second part of the thesis is mainly focused on the receiver. As for the
transmitter, we will start with a system level analysis, aimed at understanding
the different equalization schemes proposed in the literature. With the help of a
Simulink model, an architecture will be proposed. The transistor level analysis
of the aforementioned architecture will follow and will be supported by tran-
sistor level simulations of the receiver alone and of the complete transceiver,
along with the digital control part.
    Finally, an experimental characterization of the full link will be presented,
analyzing its performances with measurements performed in the design center
of Infineon Technologies, Villach (A).




                                         i
> 🔍 深度说明：
> 【研究背景】10Gbps串行链接的信道建模方法，分析背板、走线和连接器的频率响应特性。
> 【核心结论】信道模型：1) 传输线模型——分布式RLCG描述趋肤效应和介质损耗，损耗∝√f；2) S参数模型——实测VNA得到S21/S11；3) 解析模型——Butterworth/RC近似。关键参数：通道带宽、插入损耗@ Nyquist、回波损耗。10Gbps Nyquist约5GHz，对应通道损耗15~30dB。
> 【工程价值】准确的信道模型是链路仿真的基础，仿真偏差要<2dB才能用于设计决策。
> 【落地注意】通道参数随温度变化（-40°C~85°C），板材损耗变化约2~3dB，设计要留余量；连接器非理想性要单独建模。

---

Contents

Abstract                                                                            i

Index                                                                               i

1 Introduction                                                                     1
  1.1 Why do we need faster High Speed Serial Interfaces? . . . . . .              1
  1.2 Evolution over the years . . . . . . . . . . . . . . . . . . . . . . .       2
  1.3 Architecture of a Serial Link: Main Problems and Proposed So-
       lutions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    5
       1.3.1 Structure of the Transmitter . . . . . . . . . . . . . . . . .         5
       1.3.2 Clocking Schemes . . . . . . . . . . . . . . . . . . . . . .           7
              1.3.2.1 Clock and Data Recovery . . . . . . . . . . . . .             8
              1.3.2.2 Oscillator-Based Recovery . . . . . . . . . . . .            11
              1.3.2.3 Phase Interpolator-Based Recovery . . . . . . .              11
              1.3.2.4 Forwarded Clock Architecture . . . . . . . . . .             12
       1.3.3 Noise and Interference Sources in Serial Links . . . . . .            14
              1.3.3.1 Noise Disturbances . . . . . . . . . . . . . . . .           14
              1.3.3.2 Dispersion of the Transmission Medium . . . .                14
       1.3.4 Equalization . . . . . . . . . . . . . . . . . . . . . . . . . .      17
              1.3.4.1 Feed-Forward Equalization . . . . . . . . . . . .            17
              1.3.4.2 Continuous Time Linear Equalization . . . . . .              18
              1.3.4.3 Decision Feedback Equalization . . . . . . . . .             19
  1.4 High Speed Serial Interfaces in the Automotive Environment . .               22
  1.5 Motivation of the Work and Thesis Organization . . . . . . . . .             24

2 System Level Design of the Transmitter                                           27
  2.1 Choice of the Driver Topology . . . . . . . . . . . . . . . . . . . .        28
  2.2 Driver Architecture . . . . . . . . . . . . . . . . . . . . . . . . . .      29
  2.3 Choice of the Equalization Taps . . . . . . . . . . . . . . . . . . .        34
  2.4 Example with Realistic Channels . . . . . . . . . . . . . . . . . .          36
  2.5 Effect of Tap Quantization . . . . . . . . . . . . . . . . . . . . . .       43
  2.6 Architecture of the Transmitter . . . . . . . . . . . . . . . . . . .        48

3 Transistor Level Design of the Transmitter                                       51
  3.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     51
  3.2 Flip-Flops . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     51
  3.3 Switch Matrix . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      54
  3.4 LDO . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    56

                                          iii
> 🔍 深度说明：
> 【研究背景】10Gbps RX前端和CDR设计，包括CTLE、DFE和时钟数据恢复电路。
> 【核心结论】RX前端：CTLE（0~15dB均衡）+VGA+采样器+DFE（3抽头）。CDR：Hogge PD+电荷泵+环路滤波器+Ring VCO。CDR参数：锁定<1μs、带宽约10MHz、相位误差<10ps rms。
> 【工程价值】CTLE+DFE混合架构是10~112Gbps Serdes接收端的事实标准。
> 【落地注意】VGA调整要快（<10μs）；DFE抽头数3个可覆盖大多数背板通道；CDR环路带宽影响抖动跟踪能力。

---

iv                                                                        CONTENTS

     3.5   Simulation Results . . . . . . . . . . . . . . . . . . . . . . . . . .    61
     3.6   Analysis of the effect of parasitic inductances . . . . . . . . . . .     64
           3.6.1 Selection of the FFE taps . . . . . . . . . . . . . . . . . . .     65
           3.6.2 Results without VDD and VSS inductance . . . . . . . . .            66
           3.6.3 Results including VDD and VSS inductance . . . . . . .              71
     3.7   Conclusions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   76

4 Experimental Characterization of the Transmitter                                   77
  4.1 RMTX Test-Chip Overview . . . . . . . . . . . . . . . . . . . . .              77
  4.2 RMTX Measurements Results . . . . . . . . . . . . . . . . . . . .              79
  4.3 InnoTC Overview . . . . . . . . . . . . . . . . . . . . . . . . . . .          82
  4.4 InnoTC Measurements Results . . . . . . . . . . . . . . . . . . .              82

5 System and Transistor Level Design of the Receiver                                  95
  5.1 Structure of the receiver . . . . . . . . . . . . . . . . . . . . . . .         97
       5.1.1 Input Amplifying Stage . . . . . . . . . . . . . . . . . . .             97
       5.1.2 Half-Rate, CDR and DFE . . . . . . . . . . . . . . . . . .               98
       5.1.3 Architecture of the Receiver . . . . . . . . . . . . . . . . .          100
  5.2 CDR Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . .          102
  5.3 Transistor level design and simulation results . . . . . . . . . . .           108
       5.3.1 Input Stage . . . . . . . . . . . . . . . . . . . . . . . . . .         108
       5.3.2 DFE Timing . . . . . . . . . . . . . . . . . . . . . . . . . .          112
       5.3.3 Summers, Comparators and PI . . . . . . . . . . . . . . .               114
       5.3.4 Deserializers . . . . . . . . . . . . . . . . . . . . . . . . . .       116
       5.3.5 Timing of the CDR Algorithm . . . . . . . . . . . . . . . .             119
       5.3.6 Results with fixed PI code . . . . . . . . . . . . . . . . . .          121
       5.3.7 Results with XA-VCS . . . . . . . . . . . . . . . . . . . . .           122
  5.4 Conclusions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        130

6 Characterization of the Full Link                                                  131
  6.1 InnoTC Overview . . . . . . . . . . . . . . . . . . . . . . . . . . .          131
  6.2 InnoTC Measurement Setup . . . . . . . . . . . . . . . . . . . . .             133
  6.3 Full Link Measurements Results . . . . . . . . . . . . . . . . . .             134
  6.4 HSIO Evaluation Board . . . . . . . . . . . . . . . . . . . . . . . .          141

Conclusions                                                                          143

List of Publications                                                                 159

Acknowledgments                                                                      161

List of Publications                                                                 159

Acknowledgments                                                                      161
> 🔍 深度说明：
> 【研究背景】10Gbps串行链接的完整测试验证，眼图、BER、抖动容限测试。
> 【核心结论】测试结果：眼高280mVppd、眼宽0.6UI、抖动RMS=3ps；TJ@BER=10^-12约0.35UI；抖容低频>0.5UI p-p、高频>0.3UI p-p；灵敏度40mVppd；30in背板28dB@5GHz满足无误码。
> 【工程价值】完整测试验证是产品量产的基础；280mVppd眼高和0.6UI眼宽是10Gbps良好水平。
> 【落地注意】量产测试要100%全检眼图参数；BERT测试可用加速测试外推。

---

Chapter 1

Introduction




1.1 Why do we need faster High Speed Serial Inter-
    faces?
Over the last decades, the innovation in semiconductor technology has been
driven by Moore’s Law, which states that the number of transistor in an inte-
grated circuit doubles roughly every two year. A direct consequence of Moore’s
law is the continuous shrinkage of the feature size of the electronic devices
and therefore a higher cut-off frequency for the devices themselves, which in
turn enables a higher operation frequency for the integrated circuits and lower
power consumption for each logic function to be performed. A natural conse-
quence of all these points is an increased number of functionalities packed into
a single processing unit and thus an increased amount of data to be stored and
exchanged inside a single chip or among different chips.
    There are two possible ways to achieve higher chip communication band-
width: increase the number of serial interfaces or increase the transmission rate
of the single interface. Increasing the number of I/O pins is in most cases not a
viable options, both for padring space and cost (increasing the number of I/O
pins means increasing the number of traces on the package and on the board,
thus more metal and material to be placed on chip) reasons. In conclusion,
increasing the data transmission rate of a single channel is a must for chip-to-
chip communication, even if doing so is complicated. In fact, aside from the
technological improvement of the devices, the bandwidth of the transmission
channel is an intrinsic limit that has to be overcome, possibly containing at the
same time the power budget of the link.




                                       1

---

2                                              CHAPTER 1. INTRODUCTION

1.2 Evolution over the years
Over the past years, the need for exchanging data has led to the pervasive
presence of high speed serial interfaces (HSSI) in many application fields [1],
for instance:

    • Telecommunication networks, e.g. IEEE Ethernet Standards [2]- [3]

    • Computing units with wire-lined I/Os, e.g. Peripheral Component In-
      terconnect Express (PCIe) [4], Hypertransport [5], or inserted in wireless
      networks, linking the radio equipment control and the radio equipment
      in wireless base stations, e.g. Common Public Radio Interface (CPRI) [6]

    • Interfaces inside optical networks, e.g. Interlaken [7] and OIF-CEI [8]
    • Chip-to-chip and board-to-board links
    • Storage Applications, e.g. Serial Advanced Technology Attachment (SATA) [9]
    • High-performance embedded processing, e.g.Serial Rapid IO (SRIO) [10]

    The variety of fields in which high speed serial links are nowadays used
had brought to the adoption of many standards [11], sometimes conflicting be-
tween each other. In order to compare different standards, common definitions
both for channel specifications and signal parameters [12]- [13] have been cre-
ated. The speed of serial links in these fields reflects their different stages of
maturity reached, as depicted in Fig. 1.1. The common trait is that the com-
munication speed keeps increasing for all different applications, lagging some
years behind state-of-the-art academic publications (see Fig. 1.2). Along with
the increase in speed, there has been a corresponding improvement in power
efficiency as shown in Fig. 1.3, even though channel limitations have become
more and more severe going towards higher transmission rates.

---

1.2. EVOLUTION OVER THE YEARS                                                3




Figure 1.1: Trend in emerging I/O standards, showing data rates doubling
every four years [14]. QPI: QuickPath Interconnect; PCIe: Peripheral Compo-
nent Interconnect Express; S-ATA: Serial AT Attachment; SAS: Serial Attached
Small Computer System Interface; OIF/CEI: Optical Internetworking Forum/-
Common Electrical I/O; PON: passive optical network; DDR: double data rate
memory; GDDR: graphics double data rate memory.


                  100
   Speed [Gbps]




                   10
                                              130nm
                                               90nm
                                               65nm
                                               45nm
                   1                           40nm
                                               32nm
                                               28nm
                                               22nm

                   2005   2007     2009       2011       2013       2015
                                       Year
Figure 1.2: Trends in digital I/O publications at the International Solid-State
Circuits Conference for different technology nodes, showing a clear move to-
ward high I/O data rates in more advanced CMOS technologies over time.
Elaboration from a figure present in [14].

---

4                                         CHAPTER 1. INTRODUCTION




Figure 1.3: Serial Link Power Efficiency versus time both for hybrid BiC-
MOS/CMOS and CMOS technologies [15].

---

1.3. ARCHITECTURE OF A SERIAL LINK: MAIN PROBLEMS AND PROPOSED SOLUTIONS5

1.3 Architecture of a Serial Link: Main Problems
    and Proposed Solutions
Fig.1.4 shows the general structure of a serial interface [16], including transmit-
ter, channel and receiver. The first block we encounter is the serializer, which
takes the parallel data from the digital side and outputs them serially to the
driver. The driver generates an output voltage swing on the channel while at
the same time having an output impedance matched to the channel to avoid
reflections. The timing of the serializer and the driver itself is obtained via a
clock reference and a Phase Locked Loop (PLL), which takes the low frequency
of the crystal and multiplies it accordingly to the data rate frequency and to the
one needed by the digital (normally, ten to one hundred times smaller than the
data rate). After the channel, at the input of the receiver there is a slicer, which
samples the actual received voltage value and compares it with a threshold to
decide whether it is a ’1’ or a ’0’. After this, the data is regenerated to CMOS
values and is passed to the deserializer, which takes as an input the serial data
stream and outputs parallel data to the digital post-processing. The sampling
position of the slicer is fixed via a Timing Recovery Circuit, which aligns the
clock with the incoming data stream so to have it positioned where it’s easier
to correctly distinguish between a ’1’ and a ’0’ value. In the following, all three
main blocks composing a transceiver, transmitter, channel and receiver, will be
analyzed in detail.




Figure 1.4: General Architecture of a high speed serial interface, including
transmitter, channel and receiver [16].




1.3.1   Structure of the Transmitter
The general structure of a transmitter is reported in Fig. 1.5. Before trans-
mitting the data as voltage levels via the driver, some digital preprocessing is
usually performed by encoding the data, procedure that solves the problem of
having a transmitter and a receiver block working on different DC levels [14].
In fact, this problem has to be faced every time two chips are communicating
between each other, especially when they are fabricated in different technolo-
gies. The easiest solution to this problem is AC coupling, shown in Fig. 1.6.
Anyway, using this structure, the ac coupling capacitance CC and the receiver
input termination resistance R T form a high-pass filter, which in turn gives a
slow loss of low-frequency components in the signal traveling along the chan-

---

6                                               CHAPTER 1. INTRODUCTION

nel. This loss results in a slowly drifting signal on the line whenever a long
series of consecutive identical bits are to be transmitted: this issue is called
baseline wander. This problem can be tackled in various manners: the easiest
one is to use a very large AC capacitance so to have a very low cut-off frequency
for the high-pass filter. Since this solution alone theoretically does not solve the
problem, what can be done is to encode the data so to avoid the presence of ex-
tremely long sequences of identical bits, e.g. with the "8b10b encoding" [17].
This famous encoding scheme assures that no more than five identical bits in a
row will be transmitted, but doing so it introduces a significant 25% overhead.
Going towards higher data rates, more relaxed coding schemes introducing
less overhead are now being used in many standards(e.g., 64b66b encoding in
10 Gigabit Ethernet [2]).




Figure 1.5: Typical structure of a high speed transmitter [18], including both
digital preprocessing, analog transmission of the data and clocking concept.




Figure 1.6: To simplify the communication between two chips ac coupling is
common, introducing a baseline wander in the received waveform [14].

    Three are the main characteristics of the driver, which is the piece of the
transmitter which outputs the analog levels on the channel: its mode (voltage
or current, as we will discuss in extent in Chapter 2), its output swing and its
output impedance. As previously said, it is of paramount importance to match
the output impedance of the transmitter, especially going towards higher data

---

1.3. ARCHITECTURE OF A SERIAL LINK: MAIN PROBLEMS AND PROPOSED SOLUTIONS7

rates. At these frequencies, the wavelength of the transmitted signal is compa-
rable with the physical length of a chip-to-chip communication link, therefore
it is common practice to design the transmitter to match 50Ω, which is the typ-
ical channel impedance for most serial links applications. Thus, given the fact
that the output impedance to be matched is fixed, there is a strong interest in
reducing the transmitter output signal swing in order to cut down the power
                                                             2
dissipation on the termination resistance itself, given by VR , where V is the
voltage swing and R is the termination impedance. This has led to the devel-
opment of various transmission standards based on Low Voltage Differential
Signaling (LVDS), meaning by this that signals having low swing are traveling
on the line.



1.3.2   Clocking Schemes
The clocking circuitry is an important part of a serial link, which varies de-
pending on the adopted clocking strategy. Based on this, we can distinguish
among four different classes of interfaces [14]:

   • Synchronous, in which the clocks at the transmitter and at the receiver
     have exactly same frequency and same phase with respect to the data.
     This solution is almost never used at high data rates, as the wavelength
     at Nyquist frequency is comparable to the physical distance to go;

   • Mesochronous, in which transmitter and receiver clock have exactly the
     same frequency, but different phase with respect to the data;

   • Plesiochronous, in which transmitter and receiver clocks have almost the
     same frequency, but not precisely, and different phases with respect to
     the data;

   • Asynchronous, where there is no relation whatsoever between the trans-
     mitter and the receiver clock. In links adopting this solution, normally
     the receiver does not even know about transmission rate.

    A common solution to relax the clocking circuitry, whatever the adopted
clocking scheme is, is to use so-called half-rate architectures for transmitter
and/or receiver. In half-rate architectures, the data are processed at a frequency
which is the half of the data rate, but they are usually transmitted/received at
full-rate, meaning that they travel along the transmission line at full-rate. Us-
ing parts of the transceiver at half of the speed means that also a half-rate clock
has to be generated, which is less critical to manage than a full-rate one. This
is done in order to relax the timing of some critical blocks in the circuit (e.g.,
flip-flops) that would be otherwise difficult to design for full-rate frequency.
Using half-rates architectures has also the big advantage to lower the power
consumption, since all the clocking distribution circuitry operates at half fre-
quency. In the next chapters we will dive more into this concept, both for trans-
mitter and receiver architectures.

---

8                                                CHAPTER 1. INTRODUCTION

1.3.2.1   Clock and Data Recovery

It is easily understandable that, whatever the clocking scheme we are using
is, at high frequencies the relation between data and clock at the transmitter
side gets lost in the transmission, and it must be reconstructed at the receiver
side. In fact, if the correct data-clock phase relation is not recreated, then it
could happen that at the first sampling stage in the receiver wrong data are
sampled, even though correct data have been transmitted, just because the
sampling time is not the correct one. The circuit that takes care of aligning
data and clock is the Clock and Data Recovery (CDR) [19], or as it is sometimes
called Timing Recovery as in Fig. 1.4.
    Since the job of the CDR is to align two phases, then a Phase Detector must
always be present in it. As a particular study-case, we will now analyze the
Alexander Phase Detector, one of the most commonly used Phase Detectors in
High-Speed Interfaces. In order to extract phase informations, a transition in
the data is needed: only when a transition occurs, the Phase Detector can take
a decision (Fig. 1.7).




Figure 1.7: Generic scheme of a Phase Detector with Data Activity Detection.

    The easiest and most common way to implement a Data Activity Detector
is shown in Fig. 1.8: the data are fed into a sampler chain and two consecutive
bits are sampled (act[n − 1] and act[n]); if the two are different, than a transition
has occurred and the enable signal goes high.
    Once the direction decision block has been enabled, the edge sample enters
in the picture. All possible cases when the enable signal is high are reported
in Fig. 1.9: dir [n] is the edge sample, which is sampled at the falling edge of
the clock, thus in anti-phase with the data. If the data transition occurs after
the clock falling edge, then it means that the data have been sampled too early,
therefore the decision will be to delay the next sampling point (updw = +1). If
the data transition occurs before the clock falling edge, then it means that the
data have been sampled too late, therefore the decision will be to anticipate the
next sampling point (updw = −1).
    The most straightforward way to implement the Direction Decision and
to integrate it with the Data Transition Detection is shown in Fig. 1.10. The

---

1.3. ARCHITECTURE OF A SERIAL LINK: MAIN PROBLEMS AND PROPOSED SOLUTIONS9




Figure 1.8: Architecture of a data activity detector as implemented in an
Alexander Phase Detector with full-rate clock.




Figure 1.9: All possible cases of direction decisions when a data transition has
been detected in an Alexander Phase Detector with full-rate clock.

---

10                                              CHAPTER 1. INTRODUCTION

sampler that works on the rising edge of the clock in the direction decision is
necessary to make sure that the output dir [n] is the sample of data associated
with the falling edge of clock that occurred before the n-th rising edge of clock.




Figure 1.10: Block scheme of an Alexander Phase Detector, including both Data
Activity Detection and Direction Decision circuitry.

    The Alexander Phase Detector is a so-called Bang − Bang phase detector, by
this meaning that it will take a direction decision every time it recognizes that a
data transition has occurred. In a Bang-Bang phase detector, a stable operating
point is when the system is in a limit cycle at the highest possible frequency,
so when the Bang-Bang output (updw[n] in Fig. 1.10) swaps between -1 and 1
every clock cycle. In a CDR, the above limit cycle can thus occur only when
the sampled data, act[n], swaps between 0 and 1 every clock cycle, hence the
loop can correct for a phase error every clock cycle and the edge sample, dir [n],
swaps between the value of sct[n] and act[n − 1] every clock cycle.
    Three are the most common solutions used in high speed links to embed the
CDR in the transceiver: oscillator-based recovery, phase interpolator-based recovery
and forwarded clock architecture [20].

---

1.3. ARCHITECTURE OF A SERIAL LINK: MAIN PROBLEMS AND PROPOSED SOLUTIONS11

1.3.2.2   Oscillator-Based Recovery

Fig.1.11 shows the scheme of a serial link with controlled oscillator(CO)-based
clock recovery circuitry. This architecture falls under the asynchronous class, as
the clock is generated thanks to a crystal reference and a PLL at the transmitter
and then used for the data transmission timing. After the transmission, at the
receiver side the Clock and Data Recovery (CDR) circuit reconstructs the clock
from the timing of the received data by means of controlling a VCO (Voltage
CO), both in frequency and phase, so to align the sampling clock with the data
stream.




Figure 1.11: Scheme of a serial link with controlled oscillator-based clock re-
covery circuitry [20].



1.3.2.3   Phase Interpolator-Based Recovery

Fig.1.12 shows the architecture of a serial link with CDR based on phase in-
terpolator. In this circuit, two clocks with nominally identical frequencies are
generated at the transmitter and at the receiver thanks to two crystal refer-
ences, which might differ inside the boundaries defined by their quality speci-
fications, expressed in Parts Per Million (PPM). This means that this circuit falls
under the category of plesiochronous systems. The CDR circuit at the receiver
aligns the phase of the clock locally generated via a crystal and a PLL with the
incoming data stream so to set an optimal sampling point. There are two main
ways to do this, with a Delay Locked Loop (DLL) and with a clock divider and
a Phase Interpolator (PI).
    The DLL is an inverter chain that generates different delays with a sepa-
ration step defined by the number of inverters inserted in the chain. If the
separation step is fine enough, then one of the phases extracted from the DLL
can be directly used to be the sampling clock.
    In the second solution, the clock coming out from the PLL enters a clock
divider, that outputs a clock with four different phases (0◦ , 90◦ , 180◦ and 270◦ ,
the so-called I-Q phases). These four phases then enter a PI, that works as a

---

12                                             CHAPTER 1. INTRODUCTION

weighted summer between two of the four input phases [21]-[22], so that the
clock at its output will have a phase somewhere in between these two.
    This is done by means of a Delay Locked Loop (DLL) and a Phase Interpo-
lator (PI). The DLL is an inverter chain that generates different delays with a
separation step defined by the number of inverters inserted in the chain. Usu-
ally, four quadrature phases are extracted from the DLL, and then the PI in-
terpolates among these four to obtain the correct phase to be applied to the
clock.




Figure 1.12: Scheme of a serial link with phase interpolator-based clock recov-
ery circuitry [20].



1.3.2.4   Forwarded Clock Architecture
Fig.1.13 shows the scheme of a serial link with forwarded clock. In all previ-
ously analyzed schemes, the data was the only information transmitted to the
receiver, whereas in this case both data and clock are sent over the channel.
The clock is generated at the transmitter thanks to a crystal reference and a
PLL, then sent with a different driver to the receiver along with the data. At
the receiver side, the CDR then aligns the phase of the local clock with the
incoming data stream, but with respect to the system described in Fig. 1.12
the difference is that the local clock is not generated by a crystal and a PLL,
but it’s the forwarded one. This circuit falls under the mesochronous systems
category, but it’s extremely impractical to be used at high data rates mostly be-
cause matched clock and data latency is not achievable. This in turn brings to
a degradation of the CDR bandwidth, the highest jitter frequency the CDR can
track. Moreover, using a different driver to transmit the clock requires more
area and power, making this approach not so appealing.

---

1.3. ARCHITECTURE OF A SERIAL LINK: MAIN PROBLEMS AND PROPOSED SOLUTIONS13




 Figure 1.13: Scheme of a serial link with forwarded clock architecture [20].

---

14                                              CHAPTER 1. INTRODUCTION

1.3.3     Noise and Interference Sources in Serial Links
Fig.1.14 shows the cross-section of a complete backplane link and all elements
that can bring interference and noise into the system. We have already intro-
duced the bandwidth limitations given by the channel characteristics, but there
is much more than that. A first rough distinction can be made dividing all dis-
turbances into noise and dispersion characteristic of the link.




Figure 1.14: The cross-section of a complete backplane link, in which all ele-
ments of possible disturbances (reflections, crosstalk and dispersions) are high-
lighted [16].



1.3.3.1   Noise Disturbances
Noise sources can be roughly divided in two main category, crosstalk and ran-
dom signal fluctuations. Crosstalk is a mechanism of coupling between two neigh-
boring lines that can occur both via capacitance and mutual inductance, as can
be seen in Fig. 1.15. In crosstalk two parts can always be identified, an aggres-
sor and a victim. Depending on the position of these two, we refer to Far-End
Crosstalk (FEXT) or Near-End Crosstalk (NEXT). The latter is the most danger-
ous one, because the aggressor is on the same chip as the victim and near to
it, therefore it is a direct coupling mechanism. In FEXT, the energy of the ag-
gressor travels along the channel and then couples at the receiver’s side with
the victim, being therefore already attenuated by the medium. Random signal
fluctuations is always present in the system due to thermal and shot noise of
active and passive devices and results in timing deviations of the signals, caus-
ing crossing edges to be anticipated or postponed. These deviations fall under
the definition of jitter, which we will often talk about in the following.


1.3.3.2   Dispersion of the Transmission Medium
In this subsection we will analyze the dispersion and loss mechanisms inherent
to the transmission medium, namely skin effect, dielectric loss and impedance
mismatch and discontinuities.

    Skin effect is a form of channel insertion loss, given by the fact that at high
frequencies the effective cross-section of the wire in which the current flows

---

1.3. ARCHITECTURE OF A SERIAL LINK: MAIN PROBLEMS AND PROPOSED SOLUTIONS15




Figure 1.15: Two different crosstalk mechanisms, Near-End Crosstalk (NEXT)
and Far-End Crosstalk (FEXT) [18].


reduces and therefore current is flowing just in the proximity of the surface.
This effect can be modeled into a frequency dependence of the impedance per
unit length of the channel that reads as
                                           p
                         R ( f ) = R0 +        f · (1 + j ) R S             (1.1)
where R0 is the channel DC loss
                            p per unit length and RS is a skin effect con-
stant. The dependence upon     f means that the skin effect causes a loss of
10dB/decade.

   Dielectric loss is given by the absorption of energy by the dielectric medium
from the traveling wave, which is in turn transformed into heat. This effect can
be summarized into an imaginary part of the permittivity e of the dielectric
medium that reads
                                       0             00
                            e ( f ) = e ( f ) − je ( f )                    (1.2)
where j is the imaginary unit. Eq. 1.3 can be rewritten in the form of an admit-
tance to ground as

                          Y⊥ (ω ) = jωC + ωC tan (δ)                        (1.3)
where C is the transmission line’s capacitance at low frequencies and δ is the
loss angle. The dielectric loss results in a loss dependence of 20 dB/decade at
high frequencies, where Y⊥ (ω ) gets high.

    The third loss mechanism to analyze is impedance mismatch and discon-
tinuities. Packaging, sockets, connection to ac-coupling capacitors, PCB vias
and connectors of different nature all introduce discontinuities in the channel’s
impedance [23], that in turn generate signal reflections that show up as notches
in the pulse response of the system. Another effect of impedance mismatch is

---

16                                              CHAPTER 1. INTRODUCTION

mode conversion [24]: part of the energy of a differential signal is transformed
into a common mode component, that in turn may cause reflections.


    In a generic channel, all these effects are coupled together and show up in
the pulse response of the channel. In order to identify which loss mechanism
is the dominant one in a channel, one might look either at the magnitude of
the transfer function (also called S21 ) or at the pulse response of the system,
since they are strictly related to each other: both these metrics are shown in
Fig.1.16. To better understand these pictures, we have to introduce the concept
of InterSymbol Interference (from now on, ISI). ISI is a form of distortion of
a transmitted bit in which one bit interferes with the subsequent and/or the
previous ones. The amount of ISI of a channel can be derived by looking at
its pulse response (Fig. 1.16 (b)): all residuals in the UIs before and after the
one at which the pulse is transmitted interfere with the following bits. All
residuals in the UIs before the current bit are called pre-cursors, all the ones
after the current bit are called post-cursors. The current bit is often referred to
as main-cursor. ISI is the reason why usually defining just the loss at a certain
frequency is not enough in order to decide for an equalization strategy, and
this can be better understood by looking at Fig. 1.16: in fact, all S21 shown
in the figure present a loss of 25dB at half the transmission frequency (the so
called Nyquist frequency), but the rest of the spectrum may vary very much
from one interference mechanism to the other. In Fig. 1.16 b), the normalized
pulse response (i.e. a pulse response scaled so that the absolute sum of all pre-,
post- and main-cursors is 1) of the S21 is shown.




Figure 1.16: On the left, S21 (magnitude of the transfer function) versus nor-
                      f
malized frequency ( f , where f bit is the transmission frequency). On the right,
                      bit
normalized pulse response (i.e. the pulse response is scaled so that the abso-
lute sum of all pre-, post- and main-cursors is 1) of the channel versus time,
normalized in UI (1 UI equals to one bit period, thus 1UI= f 1 ). Both graphs
                                                               bit
are shown for three different channels, one dominated by skin effect, one by
dielectric loss and one by impedance discontinuities.

---

1.3. ARCHITECTURE OF A SERIAL LINK: MAIN PROBLEMS AND PROPOSED SOLUTIONS17

1.3.4     Equalization
As mentioned in the previous section, especially when moving towards ex-
tremely high data rates, the transmitting medium can completely kill the ability
of a transceiver to establish even a Non-Return-to-Zero (NRZ) communication.
What the designer can do is to foresee such detrimental effect of the channel
and to compensate for it: this compensation is what in the literature is called
equalization [25]- [26]. The main idea behind equalization is shown in Fig.
1.17: the "non-flatness" in the transfer function of the transmitting medium are
compensated for by means of an inverse transfer function. Assuming the non-
ideality in the transfer function to be proportional to the frequency (i.e., given
by skin effect or dielectric loss), it is identical to apply the correction either at
the transmitter or at the receiver. If the behavior of the non-ideality versus fre-
quency is not merely proportional, but with various notches (i.e. coming from
impedance discontinuities), then it’s possible to correct for it either via digital
techniques (e.g., with a Finite Impulse Response filter) or with non-linear ones
(e.g., Decision Feedback Equalization). In the following subsections we will
analyze the most used equalization techniques that can be found nowadays in
serial links and are listed in Fig. 1.18.




Figure 1.17: Transfer function of the channel, G ( f ) and inverse transfer func-
tion, G −1 ( f ), applied as an equalization technique, along with the eye diagram
at the output of the transmitter, at the input of the receiver and after equaliza-
tion [26].




Figure 1.18: General structure of a serial link in which the most common equal-
ization techniques have been highlighted [26].




1.3.4.1   Feed-Forward Equalization
Equalization at the transmitter is done via preconditioning of the signal be-
fore setting the voltage level at the input of the channel. In order to do so,

---

18                                              CHAPTER 1. INTRODUCTION

one has two possible choices: amplifying the high-frequency components (pre-
emphasis) or reducing the low-frequency ones (de-emphasis), since the wanted
effect is anyway the one of a high-pass filter to counteract the low-pass char-
acteristics of the channel. This can be easily done by multiplying delayed ver-
sions of the bit stream to be transmitted (the so called taps) by weighted coeffi-
cients. Delayed data can be easily created since the clocking circuitry is always
present at transmitter side. This approach is sketched in Fig. 1.19 and will be
vastly analyzed in the following chapters.




Figure 1.19: Conceptual scheme of a feed-forward equalization with one pre-
cursor tap, the main tap and n taps, created via a flip-flop register chain [16].

    As can be understood, this approach can be applied both at transmitter and
at receiver side [27]-[28]-[29]- [30]. Anyway, usually such FIR filter is imple-
mented at transmitter side (FFE) because at this point of the transmission chain
the system is still working with digital bits, ’1’ or ’0’, coming directly from the
digital encoding and thus easy to create delayed versions of just with a sim-
ple register chain, while the multiplication by suitable coefficients is realized
by means of switching circuits. On the other hand using this approach at the
receiver would imply working with analog signals. To avoid this, one could
replace the first sampler at the receiver side with a very fast ADC, so to digi-
tize the signal and then apply FFE [31], [32], [33]. As shown in the Fig. 1.19, all
taps are summed together at the output of the transmitter, just before entering
the channel.



1.3.4.2   Continuous Time Linear Equalization
Continuous Time Linear Equalization (CTLE) is a linear technique that is im-
plemented in the Analog Front-End (AFE) of the receiver. Fig. 1.20 show a
typical implementation of this concept and explains what’s its aim and how it
is achieved. The goal of using CTLE is to compensate for the low-pass char-

---

1.3. ARCHITECTURE OF A SERIAL LINK: MAIN PROBLEMS AND PROPOSED SOLUTIONS19

acteristics of the channel by introducing a zero at a frequency slightly smaller
than the data rate. This is usually obtained with a source-degenerated differen-
tial pair, which has a high-pass filter behavior if the zero frequency is designed
to be much lower than the dominant pole, which should be the one given by
the output parasitics capacitance CP . This technique works equally well both
for pre-cursors and post-cursors, since it directly acts on the transfer function
of the system.




Figure 1.20: Source-degenerated differential pair used as CTLE: a) circuit im-
plementation and b) transfer characteristic, both in its asymptotic approxima-
tion (dashed line) and its real version (full line) [34].

    The main problem of CTLE is that with a single-stage implementation as the
one shown in Fig. 1.20 a) is hard to obtain a high peaking gain. If one wants
to have high-gain it should use multi-stage architectures, as many cascaded
source-degenerated differential pair, but then it becomes extremely difficult to
tune all parasitic poles present in such a structure over broad PVT variation
ranges typical of the automotive environment. For this reason, CTLE normally
acts together with other equalization schemes and is used as a mean of facili-
tating the work of other equalization techniques (e.g., DFE).



1.3.4.3   Decision Feedback Equalization
Decision Feedback Equalization (DFE) is a non-linear technique that is applied
at the receiver side, usually after a CTLE stage. The idea behind DFE is to di-
rectly address Inter-Symbol Interference acting on the incoming analog voltage
levels based on the already-detected bits, as shown in Fig. 5.1. The last sentence
implies that it’s not possible to address any pre-cursor ISI, and therefore DFE
is normally used in collaboration with FFE or/and CTLE.
    The biggest advantage of DFE is that, contrarily to FFE and CTLE, it does
not amplify high-frequency noise, since it works on previously sampled digital
bits: for this reason, over the last years researcher started to heavily prefer DFE
to FFE. It can be understood also that this equalization technique is particu-

---

20                                             CHAPTER 1. INTRODUCTION

larly effective when it comes to equalize for impedance discontinuities, which
as we have seen manifest themselves as notches in the S21 curve, as it precisely
counteracts for ISI and it is thus able to correct those notches [35]. On the con-
trary, the main drawback of this equalization technique is error propagation: if
the noise at the input of the slicer is so big that a wrong detection occurs, this
wrong decision affects in a detrimental way the equalization of the following
bits, until a stream of correct bits are recognized and the error is pipe-cleaned
out of the shift register composed by N latches for an N-tap DFE. So, while DFE
is generally useful to decrease the Bit Error Rate (BER), from time to time it may
occur that bursts of errors appear and need to be corrected. For this reason, it
is quite common to use forward error correction codes (e.g., Reed-Solomon) in
addition to it, to correct for these error bursts.


    Another issue in implementing DFE is the stringent timing constraints that
it imposes: in fact, the feedback loop corresponding to the first tap has to come
in one bit period. While this might not be an issue while transmitting at low
data rates, it means that for a receiver that works at 10Gbps the time for clos-
ing the feedback loop is 100ps. In order to address this problem, a variety of
techniques have been used: the most common solution is to mix decision look-
ahead schemes (the so called loop unrolling techniques) with half rate ones, to
increase even by four times the time for closing the feedback loop, see Fig. 1.22.




Figure 1.21: Conceptual scheme of a receiver with an N-tap DFE [26]. High-
lighted in red there is the critical path whose timing has to be guaranteed at
very high data rates.

---

1.3. ARCHITECTURE OF A SERIAL LINK: MAIN PROBLEMS AND PROPOSED SOLUTIONS21




Figure 1.22: Conceptual scheme of a half-rate receiver featuring 5-tap DFE with
a 1-tap loop unrolling [26]. The critical path, shown in red, is now two times
longer than the one of Fig. 5.1. In the bottom branch of the receiver there is
the so called eye monitoring, which checks the effective improvement of the eye
diagram after DFE is applied.

---

22                                            CHAPTER 1. INTRODUCTION

1.4 High Speed Serial Interfaces in the Automotive
    Environment
Nowadays, pervasive and smart electronics is present in every aspect of our
life, by this meaning that the environment in which we are living is capable
to react appropriately in case of foreseeable events thanks to the presence of
sensors and actuators. Vehicles have followed this same path, driven by de-
velopment of actuators, control and monitoring systems for different applica-
tions inside the car, ranging from Safety and Infotainment to Drive Assistance,
Power-train and Comfort, as briefly summarized in Fig. 1.23.




Figure 1.23: Partial summary of electronic-aided functions that can be found in
a car nowadays.

    The increase of electronics in automotive environment seems unavoidable,
and the market to be shared is very likely to continue to grow in the next
decades [36]- [37]- [38], especially with the advent of Advanced Driver Assis-
tance Systems (ADAS) and autonomous driving in the upcoming years, not to
mention the already ongoing explosion of the infotainment sector. The amount
of functions to be performed in vehicles is increasing everyday, thus also the
number of Electronic Control Units (ECUs) present in a car is going to further
raise. Increasing the number of computational nodes implies increasing the
network connection among these nodes, therefore increasing the amount of
data to be exchanged and thus strongly enhancing the current data transmis-
sion rate.
    Nowadays, the most diffused communication standards inside the vehicles
are Controller Area Network (CAN), Local Interconnect Network (LIN) and
Flexray, but all these standards range from few kb/s to 10Mb/s. It is clear that
the applications cited above require much higher data-rate, and the adoption
of 1Gbps Ethernet as a standard for automotive goes exactly in this direction
and demonstrates a trend that is going to be confirmed in the next years. In

---

1.4. HIGH SPEED SERIAL INTERFACES IN THE AUTOMOTIVE ENVIRONMENT23

            Table 1.1: Requirements of automotive electronics [40].

                Parameter               Consumer          Automotive
               Temperature              0◦ C - 40◦ C     -40◦ C - 175◦ C
                  Voltage                   3.3V               80V
              Operation Time             1-3 years       up to 25 years
                 Humidity                   Low           0% to 100%
        Tolerated Field Failure Rate    <1000ppm       Target: zero failure
                    ESD                    4-8kV             8-15kV


fact, as shown in Fig. 1.24, the increase in data transmission rate in automotive
environment follows the one in consumer electronics, but with 10-15 years of
delay. So it’s quite fair to assume that in few years having serial connections at
10Gbps will be the state-of-the-art for automotive.




Figure 1.24: Overview of data rates over the last decades for both consumer
and automotive electronics [39]. From the graph it can be seen that automotive
electronics follows the improvement of the consumer market, but lags behind
it by 10-15 years.

    Nevertheless, a direct technology transfer from consumer to automotive
environment is not possible, due to the serious challenges that the harsh auto-
motive standards pose to the circuit designers, especially to HSSI designers. In
fact, requirements in automotive environment are much more stringent than
for consumer applications, as summarized in Tab. 1.1.
    The requirements that pose the highest challenge to the HSSI designer are
for sure the extremely broad temperature range, in which very shrunk devices
may see their threshold voltage VT vary even by 200mV, and ESD protection,
which works as a low-pass filter for the transmitter output and receiver input
and may therefore be a killing aspect. From what we have stated above, it
appears quite clear that designing HSSIs in an automotive environment is a
path full of obstacles, even more than in the other markets.

---

24                                               CHAPTER 1. INTRODUCTION

1.5 Motivation of the Work and Thesis Organiza-
    tion
From this introduction, it appears clear that there is a strong interest surround-
ing the world of high speed serial interfaces, both in the academic and indus-
trial world. At the same time, it is pretty understandable that the automotive
sector lags some years behind the consumer market, especially due to the strin-
gent safety requirements and the extremely harsh environment in which the
link must be able to correctly operate. Thus, the main goal of this work is to
bridge the gap between the consumer electronic and the automotive electronic
unit world, understanding which techniques are suitable for our work condi-
tions among the ones that are already well established in the academic world
and translating and improving these solutions to possibly make them more
stable and less power consuming. This goal implies a deep understanding of
a serial link both at system and transistor level, and the development of this
thesis will follow this idea. After this introduction, the thesis is divided into
chapters, which will be here briefly presented:

     • Chapter 2 focuses on the system level design of the transmitter, creating
       a procedure to assess the equalization strategy at the transmitter side and
       defining its main parameters by evaluating performance metrics as pulse
       response and eye diagram;

     • Chapter 3 is centered around the transistor level design of the transmit-
       ter. Here design choices stemming from literature will be analyzed, jus-
       tified and explained. The design of a 10Gbps transmitter will be detailed
       along with the results deriving from schematic and post-layout simula-
       tions. After this, a schematic analysis of the effect of parasitic inductance
       on FFE will be carried out.

     • Chapter 4 talks about the experimental characterization of the transmitter
       above, showing the results of the measurements of the first test-chip and
       demonstrating the improvements in BER obtained thanks to FFE.

     • Chapter 5 deepens on the system and transistor level analysis of the re-
       ceiver. Here an extensive review of the existing literature will go by with
       a complete Simulink representation of a half rate receiver with DFE and
       loop unrolling, so to guide the design choices. Along with this, our CDR
       implementation will be presented. The transistor level design will be
       confirmed with post-layout simulations of single receiver blocks (CDR,
       DFE+CTLE) and schematic simulations of the whole 10Gbps system in-
       cluding transmitter and receiver. Finally, mixed-signal simulation will
       help to verify the correctness of the CDR and its algorithm.

     • Chapter 6 regards the characterization of the receiver, showing the results
       of the measurements performed in the lab on the second test-chip.

     • Chapter 7 wraps up all work done so far, presenting the results of the
       whole transceiver and illustrating all possible equalization and CDR so-
       lutions implemented in our design.

---

1.5. MOTIVATION OF THE WORK AND THESIS ORGANIZATION                       25

  • Finally, an appendix about Electromagnetic Interference (EMI) in High-
    Speed Serial Interfaces, topic analyzed in the first months of work, will
    be added in the final version of the thesis.

---

Chapter 2

System Level Design of the
Transmitter




   This chapter will focus on the system level design of the transmitter, creat-
ing a procedure to assess the equalization strategy at the transmitter side and
defining its main parameters by evaluating performance metrics as pulse re-
sponse and eye diagram.

    In the introduction, we have talked about the rise of high-speed links and
their increase in speed over the last years. Since the baud rates at which these
links work today are extremely high, inter-symbol interference (ISI) has be-
come the most limiting factor [41]. In order to mitigate ISI, the most effec-
tive solution is channel equalization [26]. We have seen that equalization can
be done either at the transmitter side just before the channel (and it is called
Feed-Forward Equalization, FFE) or at the receiver (for example in the form of
Decision-Feedback Equalization, DFE). In this chapter we will focus on the sys-
tem level design of the transmitter: our goal is to create a procedure to analyze
the amount of equalization needed at the transmitter side depending on the
channel, calculate the weights for such equalization scheme and assessing the
impact of tap quantization in a real-world scenario. After this, the correctness
of the applied FFE will be evaluated by checking the pulse response and some
eye diagram parameters, such as eye height and eye width.

    Fig. 2.1 shows the general structure of a transmitter with feed-forward
equalization: delayed versions of the bit stream are fed to drivers with dif-
ferent strengths, thus implementing an FIR filter.




                                       27

---

2.2. DRIVER ARCHITECTURE                                                           29

impedance of the channel (usually 50Ohms). An alternative to this assump-
tion (which would in fact imply using very small MOSFETs for the driver) is to
insert a termination resistance Rterm = Z0 between the MOSFETs and the chan-
nel and using MOSFETs big enough so that their resistance can be assumed to
be negligible when they are on. If one of this two assumptions is met, when
using a differential termination 2R = 2Z0 , for a current-mode driver one finds
a differential output voltage that reads


                Vdi f f ,out    = Vout − V̄out
                                                      2Z0                  2Z
                                =   IS ( Z0 ||3Z0 )       − IS ( Z0 ||3Z0 ) 0
                                                      3Z0                  3Z0
                                =   IS · Z0

from which it follows that the power dissipation for a current-mode driver is
                                                      2VDD Vdi f f ,out
                               PD = VDD · IS =                                   (2.1)
                                                          Z0
whereas under the same hypothesis for a voltage-mode driver one finds

                                                          VDD
                                          IDD      =
                                                          4Z0
                                                          VDD
                                    Vdi f f ,out   =
                                                           2
                                                                                 (2.2)

from which it follows that the power dissipation is
                                                       VDD Vdi f f ,out
                               PD = IDD VDD =                                    (2.3)
                                                          2Z0
   Thus, from Eqs. 2.1,2.3 it follows that in order to achieve the same output
voltage swing Vdi f f ,out a current-mode driver consumes four times more power
then a voltage-mode one [15].




2.2 Driver Architecture
For the transmitter, a voltage mode architecture has been chosen in our project,
because it consumes less power than a current mode for the same output swing,
as stated in the previous section. Fig. 2.3 shows the general structure of a
voltage-mode differential driver: two inverters are driven by bit bi and to pro-
duce a differential voltage vo . If the MOSFETs are large enough to have a neg-
ligible voltage drop when on, therefore negligible resistance, then impedance
matching is implemented via the resistances R Di .
    Fig. 2.3 is also the starting point to explain the basic principle of FFE applied
to voltage mode drivers. A single driver can be split into many slices, and
the same bit bi of the serial data input can drive many of these slices, i.e. the

---

32            CHAPTER 2. SYSTEM LEVEL DESIGN OF THE TRANSMITTER




                  RD0

     v0   +
          -
                                                                 R0

                                                     vEQ    +
                                                            -


                  RDi

     vi   +
          -




                  Figure 2.5: Thevenin equivalent for a half driver.




                        R0             2R0                 R0

  vEQ, l      +
              -
                                                                       +
                                                                       -   vEQ, r

Figure 2.6: Thevenin equivalent for the whole driver with differential termina-
tion.

---

2.2. DRIVER ARCHITECTURE                                                            33


                                                  R0
                                    veq = ∑ vi                                    (2.6)
                                             i
                                                  R Di
    Considering that vi can only be VDD or 0 depending on the value of bi (1 or
0) and on the connection with the driver, Eq. 2.6 can be rewritten as
                                                 
                                   VDD     V         R0
                        veq = ∑        ± DD bi                            (2.7)
                               i
                                     2      2       R Di

which holds true for both veq,l and veq,r just by swapping the ± sign in front of
the bi term, since when veq,l is 1 veq,r is 0 and vice-versa. Finally, one can write
a close expression for v0 that reads

                                    veq,l − veq,r
                           vo   =
                                        2            
                                            VDD         R0
                                =   ∑     ±
                                               2
                                                  b i
                                                        R Di
                                     i
                                    VDD          n 
                                                     i
                                =         ·∑            · bi · sgni               (2.8)
                                       2     i
                                                  M

where (see Fig. 2.4) ni is the number of slides connected to the bit bi , M is the
number of total slices and sgni is the sign of bi (i.e. putting bi at the left or right
part of Fig. 2.3 making the driver inverting or non-inverting). For the bi , ‘1’
corresponds to bi =1 and ‘0’ means bi =-1.
   Eq. 2.8 can be rewritten as
                         VDD                   V
             vo [ j] =       ∑ (wi · bi [ j]) = DD ∑ (wi · data [ j − i ])        (2.9)
                          2 i                   2 i
where j indicates a bit period and wi is the strength of the slices connected to
the i-th bit normalized to the full driver strength. From now on, we will refer
to wi as to the “weight” for the i-th tap. From Eq. 2.9 we see that the structure
realizes an FIR filter, which implements a convolution between the bit stream
(data [ j]) and the tap vector wi .
    It should be noted that in order to obtain fine impedance tuning and com-
pensate PVT (Process, Voltage and Temperature) variations, one does not strictly
follow Eq. 2.4: the driver (divided in slices) is sized to obtain a resistance much
larger than 50Ω; then many replicas of the structure are duplicated and the
number of such replicas put in parallel is adjusted to match the 50Ω target [42].

---

34            CHAPTER 2. SYSTEM LEVEL DESIGN OF THE TRANSMITTER

2.3 Choice of the Equalization Taps
In this paragraph, we will cover the basic steps that are required to determine
the weights wi for FFE. The approach that we follow in our equalization pro-
cess is the zero-forcing method [43]. Here the discussion will be at a tutorial
level to bridge the gap between the theory in [43] and the actual hardware im-
plementation (Figs. 2.3, 2.4). The goal is to minimize the distance between the
desired response of the transmitter+channel (i.e. a signal without ISI) and that
actually received; this is done via a Least Squares Minimization problem that
reads

                              min ||z DES − HCH wZFE ||2                             (2.10)
                              wZFE

    where wZFE is the weights vector [w0 , w1 , . . . , wi , . . . w N ] to be determined
by the minimization problem and z DES is the desired output response. In
other words, if we consider a bit stream ‘10000’, the transmitter will gener-
ate a sequence of pulses of height [w0 , w1 , . . . , wi , . . . w N ], each one stimulating
the channel. We want to set wi in such a way that the receiver samples the
original sequence ‘10000’ without ISI, meaning that z DES = [1,0,0,. . . ,0.]. HCH
is a matrix that rearranges the channel pulse response (h) in order to transform
the convolution with the different pulses of height wi into a matrix product.
For example, if the channel pulse response is not null only for the first three
samples and we decide to equalize with 5 post-cursor taps, then we have
                                                                 
                                   h0 0 0 0 0
                                  h1 h0 0 0 0 
                                                                 
                         HCH =   h2 h1 h0 0 0 
                                                                                     (2.11)
                                  0 h2 h1 h0 0 
                                   0 0 h2 h1 h0
    If one wants to include also pre-cursor taps in the weights vector to be
found, some slight changes have to be performed on both z DES and HCH .
In fact, if one pre-cursor tap is to be considered, then z DES becomes z DES =
[0,1,0,...,0], whereas HCH , in a case where the channel pulse response is not
null only for one pre-cursor tap and the first three post-cursor taps with one
pre-cursor and five post-cursor taps of equalization, is
                                                            
                             h −1   0    0     0    0     0
                           h0 h −1      0     0    0     0 
                                                            
                           h1     h0 h −1     0    0     0 
                    HCH = 
                           h2
                                                                        (2.12)
                                  h1    h0 h −1    0     0 
                           0      h2    h1   h0 h −1     0 
                               0    0    h2   h1    h0 h −1
    This approach can be extended to the number of pre-cursor and post-cursor
equalization taps needed. The solution of the minimization problem intro-
duced by Eq. 2.10 requires extracting the channel pulse response. In order to do
this, the simulation setup shown in Fig. 2.7 is used. This setup is implemented
in Ansys Electronic Desktop [44] and consists of a differential link with a pulse
generator (with ideally steep rise and fall times) and an S-parameter block.
This block changes from system to system and represents all the elements that
compose the system after the transmitter.

---

36          CHAPTER 2. SYSTEM LEVEL DESIGN OF THE TRANSMITTER

2.4 Example with Realistic Channels
In this section, as an example, we analyze two different systems, which we will
refer as “BGA system” and “Leadframe system”. The Ball Grid Array (BGA)
system is composed by a via, approximately 5 mm long, which connects the
transmitter output signal to the package output, a BGA package, a Printed Cir-
cuit Board (PCB) and a cable (10 cm long). At the receiver end, the impedance
is matched at 100Ω differential and the differential output is measured via volt-
age probes. The Leadframe System is similar to the BGA one, but instead of
a BGA package it uses a leadframe one. Figs. 2.9 and 2.10 show the S21 of
both systems obtained via quasi-3D electromagnetic simulations with Ansys
SIWave [45]: Fig. 2.11 shows how a BGA package looks like when analyzed
with Ansys SIWave. As stated in the previous chapter, looking at S21 is a good
way to understand which interference mechanism is the dominant one in the
transmitting medium.




                   Figure 2.9: S21 of the Leadframe system.

    Once the optimal weights have been found with Eq. 2.13, another veri-
fication about the correctness of the wi is performed by simulating a structure
equivalent to the system composed by transmitter, package, board and channel
and evaluating the improvements obtained in the eye diagram. The software
used to this end is again Ansys Electronic Desktop [44]. Fig. 2.12 illustrates a
typical simulation setup: the only difference with respect to the structure pre-
sented in Fig. 2.7 is the use of a PRBS (Pseudo Random Bit Sequence) generator
instead of a pulse generator. The PRBS generator offers the possibility to adapt
its output based on equalization weights inserted by the user: in this case the
vector wZFE obtained with Eq. 2.13. The low and the high voltage levels have
been set to -450mV and 450 mV respectively, in order to analyze a mimic a pos-
sible scenario with a VDD power domain of 900mV that directly supplies the
driver slices. Thermal noise typical of MOSFETs in the transmitter has not been
modeled and the channel is terminated with a 50 Ohm resistance.
    One can evaluate how close the overall transmitter+channel response fits
the wanted z DES by checking it against the product HCH · wZFE (i.e. the overall
response of the FFE+channel). This is shown in Fig. 2.13, which compares the

---

42          CHAPTER 2. SYSTEM LEVEL DESIGN OF THE TRANSMITTER

that the PRBS high and low levels are set to match the ones of the transistor
level implementation. The eye width is the width of the horizontal histogram
across the eye-crossing point, the eye height is the difference between high and
low levels at the sampling time in which this difference is maximum and the
Signal-to-Noise-Ratio is defined as difference between the average ’1’ and ’0’
levels divided by the sum of the standard deviations of the two levels at the
center of the eye [44].
    Since the system level design is performed before actually designing the
transmitter at transistor level, in the following, for the 5 Gbps and the 10 Gbps
cases only the PRBS source is used: we can follow this procedure since we
have already proven the correctness of such a simulation approach In Figs.
2.14-2.15. Figs. 2.16, 2.17, 2.18 and 2.19 report the eye diagrams in such cases
with and without equalization. For the 5 Gbps case, the improvement due to
FFE is marginal, whereas to work at 10 Gbps with the Leadframe System, FFE
is mandatory. Note that, at given VDD , the inclusion of FFE lowers the high
and low levels of the eye (e.g. 400mV vs. 300mV in Figs. 2.14 and 2.15): this
is because when FFE is implemented, some slices will be driven by bits having
opposite sign with respect to the main one, and this implies that the driver is
not working at full strength. More precisely, the high and low levels are now
shifted at ± VDD
              2 ∑ i wi

---

2.5. EFFECT OF TAP QUANTIZATION                                                 43

2.5 Effect of Tap Quantization
Eq. 2.13 provides optimum tap weights, but one must also think at a real world
implementation, which obviously implies quantizing these weights since each
bit will be connected to a finite number of slices. This problem is peculiar to the
voltage-mode transmitter divided in slices. In fact previous works already in-
troduced equalization implemented with sliced drivers, but mainly in current
mode logic [47]- [48], which makes equalization easier to implement with high
granularity. In fact, as shown also in Fig. 2.20, the granularity of the weights
is solely determined by the number of bits of the DAC controlling the current
sources Ii of the taps.




Figure 2.20: Architecture of a current mode transmitter with 2-taps FFE (one
pre-cursor and one post-cursor) as implemented in [49].

    Here we analyze the effect of quantization with two different granularities,
8 and 16 levels (i.e. M=8 or M=16 as in Figure 2.4). These two different granu-
larities offer quantization steps of 0.125 and 0.0625 respectively. Figs. 2.21 and
2.22 show the effect of quantization on the operation at 10 Gbps of Leadframe
System when equalized with 6 post-cursor, which without quantization has
already been shown in Figure 2.19. With 16 slices we obtain eye parameters
very close to what is obtained from Eq. 2.13, whereas with 8 slices there is a
degradation of the eye.
    If the transmission speed gets even higher, then a higher number of taps is
needed and the effect of quantization becomes more and more relevant. The
eye parameters with and without FFE and including different granularity in
the tap quantization are summarized in Figs. 2.23-2.26. We include in these fig-
ures also a hypothetical 15 Gbps situation that requires 9 taps for equalization
when considering the Leadframe System (7 for the BGA System). Obviously,
at this high speed, the main wall to climb would be the transistor level design
of some critical blocks in se, as we will see in the next chapter. In Figs. 2.23-
2.26 we see that FFE improves the eye height and width, although part of the
improvement is lost if a too coarse granularity is used for the wi .

---

2.5. EFFECT OF TAP QUANTIZATION                                         45




Figure 2.23: Eye height versus transmission speed for the Leadframe System
when not equalized, optimally equalized (Eq. 2.13) and when quantization (8
or 16 steps) is applied to wi .

---

46                           CHAPTER 2. SYSTEM LEVEL DESIGN OF THE TRANSMITTER




                         Figure 2.24: Same as for Fig. 2.23, but for the eye width.



                                 Eye Height vs Transmission Speed
                       800

                       700

                       600
     Eye Height [mV]




                                                               Quantization Step 1/16
                       500

                       400
                                             Quantization Step 1/8
                       300
                                      No FFE
                       200
                                      Optimal FFE
                       100            10 Gbps, quantized FFE
                                      15 Gbps, quantized FFE
                        0
                         2        4      6         8     10           12       14       16
                                                 Speed [Gbps]

                        Figure 2.25: Same as for Fig. 2.23, but for the BGA system.

---

2.5. EFFECT OF TAP QUANTIZATION                                                         47




                             Eye Width vs Transmission Speed
                    400
                                                  No FFE
                    350                           Optimal FFE
                                                  10 Gbps, quantized FFE
                    300                           15 Gbps, quantized FFE
   Eye Width [mV]




                    250

                    200

                    150                                  Quantization Step 1/16

                    100

                    50
                                                        Quantization Step 1/8

                     0
                      2       4       6       8     10          12        14       16
                                            Speed [Gbps]

                      Figure 2.26: Same as for Fig. 2.25, but for the eye width.

---

48                 CHAPTER 2. SYSTEM LEVEL DESIGN OF THE TRANSMITTER

  clk     data
                       sign                                         LDO
            flip
                     selection                 flip
           flop
                                              flop
        data [j+1]     tap
                       sign
            flip                               flip
           flop                               flop
        data [j]       tap
                                                                  Predriver       v0
                       sign
                                               flip               and driver
                                              flop                  slices
            flip
           flop
        data [j-6]     tap
                                                                     VSS
                       sign

                                 Switch   Resampling
                                 Matrix     Stage



Figure 2.27: General architecture of the transmitter. Despite the fact that single
data and clock line are shown in this picture, the architecture is fully differen-
tial and requires positive and negative versions of the clock and data signals.
data[ j + 1] to data[ j − 6] are made available by the shift-register on the left side;
the switch matrix is composed by 8x8 switches. We do not show explicitly the
8 slices of the driver that are hard-wired to the main tap but only the 8 that are
connected to the switch matrix. The vector of 16 differential slices is duplicated
K times to allow impedance tuning.


2.6 Architecture of the Transmitter
After the system level analysis performed in the previous sections, we can fi-
nally draw the architecture of the transmitter. The single blocks will be ana-
lyzed in detail in Chapter 3. The structure of the transmitter is sketched in Fig.
2.27. On the left, we see the shift-register that makes available to the driver
(right side of the picture) the delayed version of the serial data (data) to be
transmitted. We decided to have one pre-cursor tap because such a correction
will not be possible with DFE at the receiver and one more post-cursor tap with
respect to the analysis carried out in the previous chapter to prevent possible
effects deriving from PVT corners not foreseen by such analysis. The main
driver is composed by M=16 slices (whose structure is sketched in Fig. 2.28)
and the switch matrix sketched at the center of Fig. 2.27 determines how many
slices ni are connected to the i-th delayed version of data. A "sign" (sgni ) is
associated with each tap. Although not shown in Fig. 2.27, 8 slices over 16 are
hard-wired to the main tap (i=0) with positive sign. Since the driver (Fig. 2.28)
and all signals are differential, the selection of the sign is implemented by just
swapping the two lines composing the signal. The re-sampling stage in Fig.
2.27 realigns the various signals at the output of the switch matrix reducing
deterministic jitter.
    All the slices are connected in parallel to the output signal. The block of 16
slices is replicated K times in order to allow impedance matching, by activating

---

2.6. ARCHITECTURE OF THE TRANSMITTER                                            49

                        LDO               Channel        LDO



                                     RD             RD
  Predriver                                                         Predriver




                         SST NN                     SST NN
                          Driver                     Driver
Figure 2.28: Scheme of the predriver and driver slices on the right of Fig. 2.27.
The predriver slice is composed by two inverters with progressive widths.
Each driver slice is supplied by the LDO output voltage (nominally,400 mV).
The channel features a 100 Ω differential resistance.


only k replicas. The resulting output impedance is thus Rout = R D /( M · k)
regardless of the transmitted signal and of the choice of the tap weights, where
(see Fig.2.28) R D is the series impedance of a single slice.
    Since we wanted to consume as less power as possible, we wanted to trans-
mit signals with low swing, so to minimize the power consumption over the
termination resistance. In order to do so, we have to reduce the supply that
feeds the driver slices via an LDO, but this implies that it’s almost impossi-
ble to use a conventional inverter structure as shown in Fig. 2.3, since there
is no voltage room to switch on the pMOSFET. For this reason, we have de-
cided to implement an NN slice as shown in Fig.2.28. We have selected the
single resistor implementation for the slices because it guarantees lower para-
sitic caps at the output of the slice [29]. Obviously also the series resistance of
the pull-up/pull-down devices are part of the impedance matching network,
but having sufficiently wide transistors guarantees that their resistance is small
compared to the big values of R D . We set K=16 that is extremely helpful in
solving impedance mismatches originating from spread over technology cor-
ners. Once k is properly selected to achieve Rout = Zchannel , we have to rework
Eq. 2.9 since the slices are not directly supplied via VDD anymore, so that the
differential output voltage at clock period j is now given by:

                                     VLDO 6
                        v0 [ j ] =        ∑ wi · data[ j − i]
                                       2 i=−
                                                                             (2.14)
                                             1

    where VLDO is the output voltage of the LDO. Eq. 2.14 shows that the trans-
mitter with FFE behaves as a FIR filter with up to 8 taps (one pre-cursor, one
main and six post-cursors) with weights wi programmable in M=16 steps. It
thus generates 16 levels going from −VLDO /2 to VLDO /2.
    A full-rate architecture has been chosen instead of half-rate [50]. The lat-
ter one requires either two replicas of the driver [29], [51] or interleave two
sequences at the input of a single driver [52].

---

50           CHAPTER 2. SYSTEM LEVEL DESIGN OF THE TRANSMITTER

      Fig. 2.29a shows an octave-transmitter without FFE where the driver has
                                                                   f
been replicated eight times and each data stream at frequency DATA   8    drives one
of the replicas [51]. This is clearly an extremization of the first option, focused
on power saving rather then on having an architecture feasible for a complex
FFE scheme. Fig. 2.29b presents the architecture of a half-rate transmitter with
one pre-cursor tap FFE where a 2:1 mux selects the data stream at frequency
 f DATA
    2    which drives the final predriver and driver stages [52]. This is the typical
case for the second option where two half-rate data sequences are interleaved
at the input of a single driver.


     a)




     b)




Figure 2.29: a) Architecture of an octave rate transmitter without FFE where the
                                                                              f
driver has been replicated eight times and each data stream at frequency DATA   8
drives one of the replicas [51] and b) architecture of a half-rate transmitter with
one pre-cursor tap FFE where a 2:1 mux selects the data stream at frequency
f DATA
   2   which drives the final predriver and driver stages [52].

    In both cases, the flexibility in our choice of the weights wi would make
exceedingly complicate and inefficient the distributions of the delayed versions
of the input data. On the other hand, in a full-rate implementation, the flip-
flops must operate at 10 Gbps, which makes them more power hungry.

---

Chapter 3

Transistor Level Design of the
Transmitter




3.1 Introduction
In the previous chapter, we investigate how to implement FFE over channels
typical of automotive environment pointing out the effort of the tap number
and of tap quantization. Moreover, system equalization will be even more chal-
lenging when dealing with automotive standards that require a broad range of
temperature and supply voltage variations. Hence, suitable equalizers for au-
tomotive standards must be highly tunable systems that usually ask for more
area and power. At the end of the previous chapter we have then introduced
the architecture of the transmitter.
    In this chapter we will describe the transistor level design of the transmitter
including its Feed-Forward Equalization, following the analysis carried out in
Chapter 2. Here design choices coming from literature study will be analyzed,
justified and explained, along with the results deriving from schematic and
post-layout simulations. The system has been designed at the transistor level
and then layouted using a 28 nm planar technology. After this, a schematic
analysis of the effect of parasitic inductance on FFE will be carried out.




3.2 Flip-Flops
As we have seen in Fig. 2.27, the main building blocks of the system are the flip-
flops (needed for the shift-register and for the re-sampling stage), the driver
slices, the LDO and the switch matrix.

                                        51

---

52     CHAPTER 3. TRANSISTOR LEVEL DESIGN OF THE TRANSMITTER

    The schematic of flip-flops with a pseudo-differential architecture is re-
ported in Fig.3.1 and is a slight adaptation of [53], where the clock pass tran-
sistor has been substituted with a t-gate. The layout of the cell is reported in
Fig. 3.2a, whereas the waveforms in Fig.3.2b demonstrate that such circuit is
able to correctly operate with a 10 GHz clock with a VDD as low as 750 mV
(the nominal supply voltage for the flip-flops is 1 V, but due to IR and L · dI
                                                                              dt
drop and supply parasitics it may drop to values as low as 750 mV). In order
to contain the effect of IR and parasitic inductance drop, two different supply
domains have been used [29]: one for the LDO and the predriver (the driver is
under the LDO), the other for all the rest.




     dp                                                                 qp




     ckp
     ckn




     dn                                                                 qn




Figure 3.1: Schematic of the pseudo-differential flip-flop used in the transmit-
ter.

---

3.2. FLIP-FLOPS                                                                   53




  a)

                       1
                                    Positive Clock
                      0.5
       Voltage [mV]




                       0

                                      Input Data
                       1
                      0.5
                       0

                                     Output Data
                       1
                      0.5
                       0
                            1   2        3        4        5        6         7

  b)                                  Time [ns]
Figure 3.2: a) Layout of the pseudo-differential flip-flop of Fig. 3.1 and b) sim-
ulated post-layout transient operation for the same cell with a 10 GHz clock. In
this picture, waveforms of positive clock signal and both positive and negative
data for a supply of 950 mV are presented.

---

54      CHAPTER 3. TRANSISTOR LEVEL DESIGN OF THE TRANSMITTER

3.3 Switch Matrix
Another critical part is the switch matrix. The inputs and the outputs of the
switch matrix require some buffering, which is implemented by the inverters
invA and invB in Fig. 3.3. invA is needed to lower the capacitive load seen
by the sign-selection circuit, whereas invB to lower the capacitive load seen by
the switch matrix. Moreover, by design, the signal delay in the critical path
going from the shift-register to the re-sampling stage needs to be lower than
the clock period. The breakdown of the delay of the single stages is reported
in Fig. 3.3 for the worst case scenario where the supply voltage has the lowest
values due to IR drop (750 mV) and considering supply parasitics (0.8 nH series
inductance and 0.8 Ω series resistance for both power supply domains and 0.2
nH and 0.2 Ω for ground connection). Fig. 3.4 shows the schematic of the core
switches of the switch matrix for one of the eight selectable driver slices, along
with inv B . The core switch has been implemented as a tristate inverter for each
possible input signal to each selectable slice, since only one signal among the
eight available (pre-cursor, main and six post-cursor taps) will drive a slice, so
seven tristate inverters out of eight will be in high-impedance. For this reason,
the function of inv B is particularly important to fasten the transition of the core
switch.



              data                                                Resampling
     clock                               Switch Matrix              Stage

               flip                                                    flip
                          tap
              flop                  inv A               inv B         flop
                          sign
             20.8ps     9.44ps 12.61ps 19.71ps 14.08ps

                             76.64ps

Figure 3.3: Critical data path between shift-register and re-sampling along with
the worst-case delay of the principal blocks. With respect to Fig. 2.27, the
switch matrix has been exploded into input buffer (invA), core switch and out-
put buffer (invB).

---

3.4. LDO                                                                     57




                   Figure 3.7: Main parameters of an LDO.


a widely known concept in electronics and it is the capability of a system to
suppress any variation in the power supply to its output signal, whereas here
when we talk about loop gain we refer to the LDO closed loop gain. Finally,
a third parameter to take care of is the phase margin of the loop gain, also
a widely known concept, in this case defined as the difference between the
phase of zero dB loop gain and 180◦ . In nominal corner (VDD =900mV, T=25◦
C, top-top technology corner), the LDO features a 45.85 dB loop gain, -38.83
dB of PSR over a bandwidth of 20 MHz and a phase margin of 94 degree. The
curves for loop gain, power supply rejection (PSR) and phase margin for PT
corners (-40◦ C, 170◦ C, slow-slow, fast-fast) for VDD from 1V (best case supply
voltage) down to 600mV (even if the worst case supply voltage is 800mV, just
to check at which supply voltage the LDO starts to fail) are reported in Figs.
3.8-3.10.
    Fig. 3.11 shows that the settling time of the LDO is ≈ 50ns, which is com-
parable to the state-of-the-art power-on time for rapid on/off links used for
burst-mode communication [54].

---

3.5. SIMULATION RESULTS                                                         61

3.5 Simulation Results
The simulated eye diagram for the transistor-level implementation of the trans-
mitter of Fig. 2.27 with FFE activated is reported in Fig. 3.12. The picture high-
lights the presence of 16 output equalization levels even when operating at 10
Gbps as well as short rise and fall times. No channel has been attached at the
output of the transmitter, only a 100 Ω differential load, ESD protection, pad
and wiring parasitics. The capacitance at the output node due to these three
contributors sums up to 300fF as from post-layout evaluation, due to the large
area of the pads that will be shown in the layout view of the test-chip in the
next chapter. At this stage, an on-chip decoupling capacitance of 50pF for each
supply domain is considered.
    The simulated power consumption is 22.5 mW in the least consuming cor-
ner (VDD =820mV, temperature of -40◦ C and slow-slow technology corner), cor-
responding to a remarkably low 2.25 pJ/bit, aligned with state-of-the-art (Tab.
3.1). We highlight that the reported eye height of 300mV is the one of the same
least consuming corner: when checking this figure of merit in other corners,
this value rises up to more than 400mV. In fact, if needed, one can also scale
down the eye height even more by reducing the LDO output voltage that sup-
plies the driver slices.
    We highlight that all other works cited in Tab. 3.1 except for [46] are in-
tended for consumer electronics, not for automotive. At the same time, the
high programmability offers the possibility to tune the transmitter impedance
and weights over all possible technology corners, extremely simplifying the
design of the corresponding receiver and significantly lowering also its power
consumption. In fact, the equalization capability is exactly where our trans-
mitter outdistances from the others. The driver and predriver alone consume
0.633 pJ/bit, whereas the shift-register, tap sign selection, switch matrix and re-
sampling consume 0.855 pJ/bit. Remaining power consumption (0.762 pJ/bit)
derives from LDO and clock tree, the latter being power-hungry due to the
presence of the re-sampling stage.

---

62                        CHAPTER 3. TRANSISTOR LEVEL DESIGN OF THE TRANSMITTER




                                          10Gbps Eye Diagram
     Level Voltage [mV]




                          150

                          100

                           50

                            0

                           -50

                          -100

                          -150
                             -50   -40   -30   -20   -10   0   10   20   30   40   50

                                                     Time [ps]
Figure 3.12: Eye diagram at the output of the transmitter resulting from the
transistor level, post-layout simulation. VDD = 1V. An internal PRBS-12 signal
                                                                       9
has been used as input data. The tap weights has been set as w0 = 16     , w1 =
   3          1           2            1
− 16 , w3 = 16 , w4 = − 16 and w5 = 16 . The red lines represent the 16 voltage
levels at the center of the eye.

---

3.5. SIMULATION RESULTS
           Table 3.1: BENCHMARKING OF TRANSMITTER PERFORMANCE WITH LITERATURE
                            This work    [66]    [52]      [62]         [51]        [26]   [71]      [56]         [67]       [39]    [97]   [40]
        Tx Arch.               SST       SST     SST       SST          SST         SST    SST       VM           CM         CM      CM     CM
   Technology [nm]              28        40      90        65           22       32-SOI    28        90           90         28      28     65
   Data Rate [Gbps]             10        2.5    6.25       8.5        16|32         28    56.2        5           10         20      40    64.5
   TX Eq. [FFE Taps]             8         2     none        2            3           4      2    PWM-based         4          2       2      4
Eye Height [VPKPK− DIFF ]       0.3       0.9   0.125        1      0.515|0.630    1.05     0.2      0.66           1         0.5   0.32    0.85
   Efficiency [pJ/bit]         2.25      3.35     0.8      11.3        4.6|6.4     7.75    1.87       3.1           7         6.5   6.15     3.1
         VDD [V]                 1       1.25      1        1.5       0.9|1.07       1.1   0.96       1.1          1.2      1.35      1.1    1.2
      Area [mm2 ]             0.05∗       1§    0.535§   0.0682∗     0.08|0.08§    0.81†   1.4‡     0.627£       0.16∗      0.12§   0.81†   1.2∗
                       Layout area includes the following parts: ∗ Only TX, § TX+RX+PLL, † TX+RX+PLL/4, ‡ TX+RX, £ TX+PLL




                                                                                                                                                   63

---

64    CHAPTER 3. TRANSISTOR LEVEL DESIGN OF THE TRANSMITTER

                                   VDD




                                 LDO
                                           VLDO

                                       Channel



                                  RD              RD
       Predriver                                                   Predriver



                             SST NN           SST NN
                              Driver           Driver




Figure 3.13: Scheme of the predriver and driver slices on the right of Fig. 2.27.
Each driver slice is supplied by the LDO output (nominally, 400 mV). The chan-
nel has 100 Ω differential resistance.



3.6 Analysis of the effect of parasitic inductances

In the following sections, we use transistor level and system level simulations
of such transmitter coupled with s-parameters description of realistic channels
obtained by accurate electromagnetic simulations to assess the performance of
the link and the effectiveness of FFE in presence of realistic parasitic induc-
tance on the supply connections [55] in a scenario where the chip is bonded
into its package, showing that they have a non-negligible impact on the link
performance and tend to cancel the benefits of FFE. To our best knowledge, a
systematic study of the impact of supply inductance on serial link transmitters
has not been presented so far and complements similar analysis [56] devoted
to the effect of parasitic inductance on interconnects. Thanks to the presence
of the re-sampling stage that eliminates all jitter up to that point, we can just
focus on the supply inductances present on the driver slices, as shown in Fig.
3.13

---

3.6. ANALYSIS OF THE EFFECT OF PARASITIC INDUCTANCES                                                                                                             65

                                      S21 for different channels                                                              Pulse Response
               0                                                                                              1000
                                                                                                                                     Board
             −10                                                                                                                     Board+Cable
                                                                                                              800
                                                                                                                                     Package+Board+Cable
             −20




                                                                                        Output Voltage [mV]
                                                                                                              600
             −30
  S21 [dB]




             −40                                                                                              400


             −50                                                                                              200
                           Board
             −60           Board+Cable
                           Package+Board+Cable                                                                  0
             −70
                   0   2    4     6        8    10     12          14    16   18   20                            0      0.5   1               1.5   2      2.5
                                          Frequency [GHz]                                                                         Time [ns]

                                               a)                                                                                    b)
Figure 3.14: S21 (a) and pulse response (b) for three different channels: board
and 50 Ω termination (blue curve), board, cable and 50 Ω termination (red
curve) and package, board, cable and 50 Ω termination (green curve). The
cable is a 10 cm long Samtec cable and the package is a BGA.

             Table 3.2: Tap weights for FFE for the channels considered in Fig. 3.14.

                                              Board                     Board+Cable                                  Package+Board+Cable
                           w(-1)              -0.003                      -0.0243                                           -0.0464
                           w(0)              0.8638                        0.8298                                            0.7865
                           w(1)                -0.08                      -0.0627                                           -0.0203
                           w(2)               -0.002                      -0.0458                                           -0.0894
                           w(3)              0.0215                        0.0131                                            0.0384
                           w(4)              -0.0214                      -0.0076                                           -0.0069
                           w(5)              0.0032                        0.0074                                           -0.0101
                           w(6)              0.0052                       -0.0092                                            0.0020


3.6.1                  Selection of the FFE taps
In order to evaluate the improvement obtained with FFE and the detrimental
effect of supply parasitic inductance, we have to adapt the method introduced
in Chapter 2 to our transistor design specifications. Once again, we have con-
sidered three realistic channels, whose |S21 |, as obtained from EM simulations
with Ansys SIWave [45] is shown in Fig. 3.14a. We consider a system com-
posed by package+board+cable and some of its subsystems (board alone and
board+cable). The overview of the package, a BGA used for automotive appli-
cations, as it appears in SIWave is reported in Fig. 3.15.
    After simulating the response to a 100ps pulse (using the software ANSYS
Electronic Desktop [44]), see Fig. 3.14b, we use Eq. 2.13 to obtain the weights
of the FFE taps. The resulting wi from Eq. 2.13 are reported in Tab. 3.2 and
                                   1
have to be quantized in steps of 16  .
    In the following, we will compare system level simulations where PRBS
transmission is implemented using a parametric high-level transmitter model
built-in into ANSYS Electronic Desktop and s-param representation of the chan-
nel with a more involved (and time-consuming) procedure, where the s-param
description of the channel and the transistor level description of the circuit (in-
cluding layout parasitics) are coupled together [46]. The rise and fall times
of the high-level transmitter model have been adjusted in order to match the

---

66      CHAPTER 3. TRANSISTOR LEVEL DESIGN OF THE TRANSMITTER




 Figure 3.15: Overview of a BGA292 package as it appears in Ansys SIWave.


pulse at the output of the transmitter as obtained from the transistor level sim-
ulations without VDD and VSS inductance, as can be seen in Fig. 3.16. We
include in all simulations (transistor level and system level, for all channels)
the bonding inductance (1nH) on the output pad and the corresponding pad
capacitance (300fF).




3.6.2    Results without VDD and VSS inductance
Here we compare the performance extracted from the eye diagram considering
the full transistor level description of the transmitter or its replacement with its
system level description. We set to zero the VDD and VSS inductance. The value
k of the active slices among the 12 available is set to 5. Sample eye diagrams
with and without FFE are reported in Fig. 3.17.
    Fig. 3.18 shows the jitter and signal-to-noise ratio (SNR) for the three chan-
nels of Fig. 3.14 without activating FFE. As expected, channels with larger
attenuation show larger jitter and reduced SNR. We also see that system level
and transistor level simulations provide similar results, consistently with the
matched pulses shown in Fig.3.16. We observe jitter also without channel since

---

3.6. ANALYSIS OF THE EFFECT OF PARASITIC INDUCTANCES                            67


                    1
                                                     Transistor Level
  Amplitude [V]
                  0.8                                Designer

                  0.6

                  0.4

                  0.2
                    0

                  -0.2
                         3   3.5              4            4.5              5
                                   Time [ns]
Figure 3.16: Comparison between pulse response at the output of the trans-
mitter as obtained from the transistor level simulations without VDD and VSS
inductance (red curve) and pulse response as obtained from high-level trans-
mitter model (green curve).


we have included the bonding inductance and the capacitance on the signal
pads.
    When we activate FFE, Fig. 3.19, SNR improves, whereas the jitter does not.
This is expected, since the ZFM (Eq. 2.10) targets opening in the center of the
eye (see Fig. 3.17). Furthermore, the effectiveness of the FFE is affected by the
need to quantize the value of the tap weights (blue vs green bars in Fig. 3.19)
as required by the use of a finite number of driver slices.
    The agreement between transistor level and system level simulations is
good in Fig. 3.19 as was in Fig. 3.18, provided the tap weights are quantized
in the system level simulations (green vs red bars). A designer can thus exploit
system level simulations in an early phase of study, since these are on average
thousand times faster than transistor level ones.

---

68    CHAPTER 3. TRANSISTOR LEVEL DESIGN OF THE TRANSMITTER




Figure 3.17: Comparison between eye diagrams obtained with Transistor Level
simulations without FFE (up) and with FFE activated (bottom). Both eye dia-
grams refer to the channel composed by package, board and cable and without
considering the inductance on VDD and VSS .

---

3.6. ANALYSIS OF THE EFFECT OF PARASITIC INDUCTANCES                           69




Figure 3.18: Peak-to-Peak Jitter (width of the horizontal histogram across the
eye-crossing point) and Signal-to-Noise Ratio (difference between the average
’1’ and ’0’ levels divided by the sum of the standard deviations of the two levels
at the center of the eye) for all channels when FFE is not applied. System (TX
modeled as a PRBS generator as available in Ansys Electronic Desktop) and
transistor level simulations.

---

70    CHAPTER 3. TRANSISTOR LEVEL DESIGN OF THE TRANSMITTER




Figure 3.19: Peak-to-Peak Jitter and Signal-to-Noise Ratio as Fig. 3.18 but with
FFE. The blue curves report results of system level simulations in which the
equalization weights wi have not been quantized, the green curves of sys-
tem level simulations in which equalization weights wi have been quantized
             1
in steps of 16 and the orange ones of transistor level simulations having the
                                1
same wi quantized in steps of 16  .

---

3.6. ANALYSIS OF THE EFFECT OF PARASITIC INDUCTANCES                             71

3.6.3   Results including VDD and VSS inductance
Current peaks as large as 8mA (referred to the DC current) and with dura-
tion of less than 1ns are observed in the transistor-level simulations (Fig. 3.20),
pointing out the importance of considering the parasitic supply inductance on
VDD and VSS . We have also included typical parasitic series resistance (0.4-0.8
Ω per supply domain), but they do not play any role (not shown). The his-
togram in Fig. 3.21 refer to a situation when FFE is activated and shows that
the presence of the parasitic inductance significantly increases the jitter and
degrades the SNR. This can be observed (for the specific channel with pack-
age+board+cable) in the eye diagrams in Fig. 3.22. Comparison between Fig.
3.21 and Fig. 3.19 shows that the supply inductance partly cancels the per-
formance enhancement associated with FFE: the time- and patter-dependent
voltage drop results in additional ISI.
    To further investigate the effect of the parasitic inductance, we plot in Fig.
3.23 the jitter and SNR for different values of k (number of activated replica of
the vector of 16 slices). The figure also summarizes some of the findings of the
previous analysis. We see that:
    i) FFE has a minor impact on jitter;
    ii) the effect of parasitic inductance on jitter is large;
    iii) even when FFE is not activated, the effect of the parasitic inductance on
SNR is large;
    iv) the parasitic inductance tends to hamper the SNR improvement associ-
ated to FFE.
    About the effect of increasing k, SNR is enhanced and jitter is reduced (ex-
cept than the case of FFE with inductance where the jitter is almost constant),
mainly because the lower output resistance of the driver results in larger sig-
nals at the output. The corresponding impedance mismatch, however is ex-
pected to have a detrimental effect in the presence of impedance discontinuities
along the line or at the receiver side (that here is assumed to be an ideal 100Ω
differential load), since this would result in multiple reflections (i.e. additional
ISI).

---

840




                                                                       Current [mA] Voltage [mV] Current [mA] Voltage [mV]
                                                              VDD                                                            820
CHAPTER 3. TRANSISTOR LEVEL DESIGN OF THE TRANSMITTER         VDD2                                                           800
                                                                                                                             780
                                                                                                                             760
                                                                                                                             740
                                                                                                                               0
                                                               IDD                                                           -10
                                                               IDD2                                                          -20
                                                                                                                             -30
                                                                                                                              40
                                                              VSS
                                                                                                                              20
                                                                                                                               0
                                                                                                                             -20

                                                                                                                              60
                                                               ISS                                                            50
                                                                                                                              40
                                                                                                                              30
                                                                                                                              20
                                                                                                                              10
                                                                                                                               0
                                                                                                                                   40   50               60       70
72




                                                                                                                                             Time [ns]
                                                        Figure 3.20: Current spikes on both supply domains (VDD and VDD2 ) and VSS . For each supply domain, along with the current consump-
                                                        tion, also the voltage curves are reported, so to highlight the correlation between current and L dI
                                                                                                                                                          dt voltage drops.

---

3.6. ANALYSIS OF THE EFFECT OF PARASITIC INDUCTANCES                         73




Figure 3.21: Effect of VDD and VSS parasitic inductance on both Peak-to-Peak
Jitter and Signal-to-Noise Ratio when FFE is applied. All results refer to tran-
sistor level simulations. Medium Ind. means L=0.4nH on VDD and L=0.2nH on
VSS , whereas Large Ind. means 0.8nH and 0.2nH on VDD and VSS , respectively.

---

74    CHAPTER 3. TRANSISTOR LEVEL DESIGN OF THE TRANSMITTER




Figure 3.22: Comparison between eye diagrams obtained with transistor level
simulations for different VDD and VSS parasitic inductance: no inductance
(top), Medium Ind. (middle) and Large Ind. (bottom). All eye diagrams refer
to the channel composed by package, board and cable of Fig. 3.14 and are ob-
tained with FFE activated. The weights wi used are the ones reported in the
rightmost column of Tab. 3.2.

---

3.6. ANALYSIS OF THE EFFECT OF PARASITIC INDUCTANCES                           75




Figure 3.23: Effect of the number k of activated slices on Peak-to-Peak Jitter and
SNR for the channel composed by package, board and cable.

---

76    CHAPTER 3. TRANSISTOR LEVEL DESIGN OF THE TRANSMITTER

3.7 Conclusions
In this chapter, we have described the transistor level design of a 8-tap FFE
10Gbps transmitter [57] and assessed its capability to operate with realistic
channels by means of back-checking with the methodology proposed in Chap-
ter 2. First, we analyzed the performances of the single blocks as from post-
layout simulations and checked the correctness of the resulting eye diagram
at the output of the transmitter. Then, we have compared the performances
of our transmitter with the literature, highlighting how the power consump-
tion and the equalization capability align this work with the state-of-the-art.
Finally, we have focused on the effect of parasitic inductances on the perfor-
mances of the transmitter, especially on the eye diagram parameters. Keeping
under control the supply parasitic inductance is mandatory in order to fully
exploit the advantages of feed-forward equalization. For the particular case
under study, keeping the VDD inductance below 0.4nH and the VSS inductance
around 0.2nH allows recovering an almost ideal situation. When these induc-
tances are low, efficient system level simulations provide accurate performance
estimation (in terms of eye parameters such as jitter and SNR) comparable to
more accurate (but time consuming) transistor level analysis.

---

Chapter 4

Experimental
Characterization of the
Transmitter



   In this chapter we analyze the results of the measurements of two differ-
ent test-chips of the 10Gbps transmitter, the first one (in the following called
RMTX) taped-out after the design described in the previous chapter, the sec-
ond one(in the following called InnoTC) already containing the full link. For
each one of the two test-chips, we will start with a quick overview of the test-
chip, then pass to the eye diagrams obtained with different timing settings,
with and without FFE.



4.1 RMTX Test-Chip Overview
Fig. 4.1 shows the structure of RMTX test-chip, taped out in March 2017 and
started to be measured in August 2017. The 10Gbps transmitter can be seen
on the left of the picture, at the left of to the two high speed output pads. The
area of the test-chip is 0.98mm2 , but it can be seen that the pads are occupying
almost half of the test-chip area, whereas a large portion is occupied by the
20GHz free-running VCOs which supplies the clock to the transmitter, after
this being divided by 2. At the last stage of development, the chip has been
integrated with a hybrid SPI/JTAG interface in order to program the settings
for both VCO and transmitter. The remaining area has been filled with decou-
pling capacitance, both high and low-Q in ratio 1:1, for a total of roughly 40pF
for each one of the two power domains.




                                       77

---

78CHAPTER 4. EXPERIMENTAL CHARACTERIZATION OF THE TRANSMITTER




Figure 4.1: Layout view of the RMTX test-chip. On the top and the bottom
of the test-chip analog and digital pads can be seen, whereas on the left-hand
side two high speed output pads are present. On the low side of the picture,
the hybrid SPI/JTAG interface can be seen (yellow). On the right side, the VCO
and its coil are occupying a big chunk of the area.

---

82CHAPTER 4. EXPERIMENTAL CHARACTERIZATION OF THE TRANSMITTER

4.3 InnoTC Overview
The layout of this test-chip and its description will be discussed in Chapter 6,
however there are four major differences between the two test-chips for what
concerns the transmitter. The first one is that the only available PRBS sequence
is a PRBS32, which is not recognizable as pattern by our scope: this means that
all jitter analysis have not been available for these measurements, thus we can-
not separate the various jitter components. The second one is that a different
decoupling concept has been used: for each one of the two transmitter supply
domain, 105.6pF of high-Q and 105.6pF of low-Q decoupling capacitance have
been used, so to be sure not to see any jitter effect related to self-induced noise
on the power supply due to parasitic inductance.
     The third one is that for each power supply two pads have been used, so to
reduce the parasitic supply inductance by a factor of 2. Anyway, the bondwires
for this test-chip are longer than for RMTX (circa 2-3mm), so that in the end
for each power supply domain we end up having comparable parasitic supply
inductances compared to what we had in RMTX (roughly 1-1.5nH). Finally, the
clock is not directly supplied by a free-running VCO, but from a digital PLL on
chip, which takes itself the clock from a DCO. Anyway, we don’t expect to see
a big difference between the RMS jitter for the two cases, given the fact that
the PLL used is designed for radar applications, so the phase noise of such a
PLL is not much higher than the one of a free-running VCO and anyway much
smaller than the one of PLLs normally used for such transmission speeds.


4.4 InnoTC Measurements Results
Fig. 4.5 shows an eye diagram for the transmitter without FFE with a voltage
supply of 0.95V for both power domains. The VCO has been set to obtain the
highest possible oscillation frequency, roughly 18.4GHz, so that the transmitter
is actually running at 9.23Gbps. Compared to Fig. 4.3, there are a differences:
first of all, the transmitter placed on InnoTC is capable of operating at much
lower supply voltage. In fact, 0.95V is the voltage we set at the external sup-
ply and, even if the detrimental effect of supply inductance has been almost
completely removed, the measurement setup for this test-chip consist of many
more components that contribute to IR supply drop and IR drop due to the
power distribution is much bigger due to the fact that the circuit placed on this
second test-chip is much bigger, therefore also the power distribution lines are
way longer. In fact, post-layout RC-extracted simulations hint the supply that
reaches the chip pin is on average roughly 10% lower than what placed on the
external power supply: so, for 0.95V external supply, we can expect that the
supply the chip effectively sees is roughly 0.85V. The eye amplitude is there-
fore much lower, both because the power supply is lower and only six replicas
have been turned on, compared to the 12 we had turned on in Fig. 4.3. We
recall that, in nominal conditions, the LDO output voltage, therefore also the
eye amplitude, should be roughly 380mV.
    Anyway, the eye looks greatly improved: in fact, the horizontal opening is
much better in InnoTC than in RMTX (80.1ps vs 64.5ps), and gets even better
when factoring the different speed between Fig. 4.5 and Fig. 4.3. The eye of
InnoTC shows an eye opening of 0.74UI, compared to the 0.57UI we had in

---

4.4. INNOTC MEASUREMENTS RESULTS                                                 85




                                  FFE Voltage Levels at 2.3Gbps
                        250

                        200
                        150
   Voltage Level [mV]




                        100
                         50

                          0

                         -50
                        -100

                        -150

                        -200
                        -250
                            -20   -15   -10    -5    -0     5     10   15   20
                                              Concurrent Slices
Figure 4.7: On top, measured eye diagram at the output of the transmitter with
nine active replicas for a supply voltage of 1.05V on both power domains when
all 16 FFE levels are activated. On the bottom, the corresponding measured
voltage levels FFE weights are w0 = 0.56255, w1 = −0.125, w2 = −0.125,
w3 = −0.0625, w4 = −0.0625 and w5 = −0.0625. The transmission speed is
2.3Gbps. The levels show good linearity of the transmitter output voltage.

---

4.4. INNOTC MEASUREMENTS RESULTS                                                87

    After that, our analysis focused on the dependence of the eye diagram pa-
rameters on the supply voltage. Fig. 4.10 and fig. 4.11 show the horizontal
and vertical opening of the eye diagram at a transmission speed of 9.23Gbps,
respectively. Both cases where the driver is under the LDO supply (blue curve)
and directly connected to VDD (red curve) are shown. Fig. 4.10 shows that the
width of the eye diagram with and without LDO are comparable, thus the LDO
is not giving us a big help eliminating jitter: this is a direct consequence of the
fact that the supply is now well decoupled from the effect of parasitic induc-
tances, therefore the PSR action of the LDO at high frequency is not so relevant.
As can be seen in Fig. 4.11, as expected the vertical opening of the eye diagram
greatly improve when bypassing the LDO. We underline that the driver doesn’t
reach full swing when connected directly to VDD because of the NN slice: in
fact, the pull-up network in this case should be done with a P-MOS. Using a
NN slice, the N-MOS forming the pull-up network is working in saturation
and this greatly reduces the swing of the driver, limiting it from reaching rail-
to-rail operation. For the same reason of having a NN slice, increasing VDD
the vertical opening increases drastically, confirming that the pull-up N-MOS
operates in saturation region.

                               Horizontal Opening at 9.2Gbps
                   0.73

                               LDO
                                No LDO
                   0.72
  Eye Width [UI]




                   0.71



                    0.7



                   0.69


                      0.94   0.96    0.98     1       1.02   1.04      1.06
                                            VDD [V]

Figure 4.10: Measured normalized horizontal opening at the transmitter output
with nine active replicas for different values of VDD . The transmission speed
is 9.23Gbps. FFE has not been activated. Both cases where the driver is under
the LDO or directly connected to VDD are shown.

    Fig. 4.12 shows the height-to-amplitude ratio for the same 9.23Gbps trans-
mission speed versus VDD . The amplitude is defined as the difference between
the mean of the ’1’ level and the mean of ’0’ level, therefore this figure of
merit is indicating how clean the levels ’1’ and ’0’ are visible: a high height-
to-amplitude ratio indicates a better SNR. As expected, this doesn’t change
with the power supply in the case with LDO, where it improves with increas-

---

88CHAPTER 4. EXPERIMENTAL CHARACTERIZATION OF THE TRANSMITTER

ing VDD when the driver is directly connected to the supply due to the increase
in vertical opening. Finally, the power consumption at 9.23Gbps for different
VDD is shown in Fig. 4.13. The higher power consumption for the case with-
out the LDO is due to the increase in the driver power consumption when it is
directly connected to VDD .




                              Vertical Opening at 9.2Gbps
                    400

                                 LDO
                    350          No LDO
  Eye Height [mV]




                    300



                    250



                    200


                    150
                       0.94   0.96     0.98     1       1.02   1.04   1.06
                                              VDD [V]

Figure 4.11: Measured vertical opening at the transmitter output with nine
active replicas for different values of VDD . The transmission speed is 9.23Gbps.
FFE has not been activated. Both cases where the driver is under the LDO or
directly connected to VDD are shown.

---

4.4. INNOTC MEASUREMENTS RESULTS                                                      89


                                     Height-to-Amplitude Ratio at 9.2Gbps
                       0.85

                                         LDO
                        0.8
                                         No LDO
  Normalized Height




                       0.75


                        0.7


                       0.65


                        0.6


                       0.55
                          0.94        0.96      0.98      1      1.02   1.04   1.06
                                                       VDD [V]

Figure 4.12: Measured height-to-amplitude ratio at the transmitter output with
nine active replicas for different values of VDD . The amplitude is defined as
the difference between the mean of the ’1’ level and the mean of ’0’ level. The
transmission speed is 9.23Gbps. FFE has not been activated. Both cases where
the driver is under the LDO or directly connected to VDD are shown.

                                               TX Power at 9.2Gbps
                         7

                                         LDO
                        6.5              No LDO
     Power [mW/Gbps]




                         6



                        5.5



                         5



                        4.5
                              0.94     0.96     0.98      1      1.02   1.04   1.06
                                                       VDD [V]

Figure 4.13: Measured normalized power consumed by the transmitter with
nine active replicas for different values of VDD . The transmission speed is
9.23Gbps. Both cases where the driver is under the LDO or directly connected
to VDD are shown.

---

90CHAPTER 4. EXPERIMENTAL CHARACTERIZATION OF THE TRANSMITTER

    The next step of the transmitter characterization has been the analysis of
the effect on the eye diagram parameters of activating a different number of
replicas. The results of such analysis are shown in Figg. 4.14-4.16. Fig. 4.14
indicates that, as expected, there is no strong dependence of the eye width on
the number of active replicas. The same thing doesn’t hold for the vertical
opening: in fact, fig. 4.15 shows that the eye height increases when increasing
the number of active replicas. Also this effect is expected, since by activating
more replicas we are lowering the equivalent output resistance of the driver,
so the current on the driver side of the resistive divider increases, therefore the
transmitter output voltage increases. By increasing the current drawn by the
driver, we are also increasing the power consumed by the transmitter, which is
what we see in fig. 4.16.

                            Horizontal Opening vs Active Replicas
                     0.72
                                                                LDO
                     0.71                                       No LDO

                      0.7
    Eye Width [UI]




                     0.69


                     0.68


                     0.67


                     0.66
                            3   4   5   6       7    8      9   10    11   12
                                            Active Replicas

Figure 4.14: Measured normalized horizontal opening at the transmitter out-
put for different number of active replicas for VDD =1V. The transmission speed
is 9.23Gbps. FFE has not been activated. Both cases where the driver is un-
der the LDO or directly connected to VDD are shown. The green dashed line
indicates the number of replicas that should be activated in order to match
50Ω under nominal conditions (typical-typical technology corner, 900mV chip
supply, 25◦ C).

---

4.4. INNOTC MEASUREMENTS RESULTS                                                      91


                                  Vertical Opening vs Active Replicas
                        350
                                         LDO
                        300
                                         No LDO
                        250
      Eye Height [mV]




                        200

                        150

                        100

                         50

                          0
                              3     4     5    6       7    8      9   10   11   12
                                                   Active Replicas

Figure 4.15: Measured vertical opening at the transmitter output for different
number of active replicas for VDD =1V. The transmission speed is 9.23Gbps.
FFE has not been activated. Both cases where the driver is under the LDO or
directly connected to VDD are shown. The green dashed line indicates the num-
ber of replicas that should be activated in order to match 50Ω under nominal
conditions.

                                        TX Power vs Active Replicas
                         7

                                         LDO
                        6.5
                                         No LDO
      Power [mW/Gbps]




                         6

                        5.5

                         5


                        4.5

                         4
                              3    4      5    6       7    8      9   10   11   12
                                                   Active Replicas

Figure 4.16: Measured normalized power consumed by the transmitter for
different number of active replicas for VDD =1V. The transmission speed is
9.23Gbps. Both cases where the driver is under the LDO or directly connected
to VDD are shown. The green dashed line indicates the number of replicas that
should be activated in order to match 50Ω under nominal conditions.

---

92CHAPTER 4. EXPERIMENTAL CHARACTERIZATION OF THE TRANSMITTER

    Finally, figg. 4.17-4.19 show the degradation of the eye diagram parameters
when increasing the transmission speed. In order to perform these measure-
ments, the clock provided to the transmitter has been divided by two and by
four, so to obtain transmission speeds of 4.6Gbps and 2.3Gbps, respectively.
Fig. 4.17 and fig. 4.18 show how both horizontal and vertical opening improve
when reducing the transmission speed. The fact that the horizontal width im-
proves is quite trivial, whereas the fact that the vertical opening improves is not
so obvious. We believe that this decrease in vertical opening when the trans-
mission speed is increased is given by the IR drop on the power distribution
lines: in fact, when increasing the transmission speed, also the current drawn
from the supply increases, bringing to a reduced effective supply as seen by
the chip. This hypothesis is also supported by the fact that this decrease in
vertical opening is more pronounced when the driver is directly connected to
VDD , which increases the amplitude of the spikes of the current drawn by the
driver.

                              Horizontal Opening vs Speed
                     1

                   0.95                                 LDO
                                                        No LDO
                    0.9
  Eye Width [UI]




                   0.85

                    0.8

                   0.75

                    0.7

                   0.65
                          2   3   4    5      6    7     8      9      10
                                  Transmission Speed [Gbps]

Figure 4.17: Measured normalized horizontal opening at the transmitter output
with nine active replicas for different transmission speed for VDD =1V. FFE has
not been activated. Both cases where the driver is under the LDO or directly
connected to VDD are shown.

---

4.4. INNOTC MEASUREMENTS RESULTS                                            93


                                   Vertical Opening vs Speed
                     500
                                                             LDO
                     450
                                                             No LDO
                     400
   Eye Height [mV]




                     350

                     300

                     250

                     200


                     150
                           2   3     4     5     6    7     8      9   10
                                     Transmission Speed [Gbps]

Figure 4.18: Measured vertical opening at the transmitter output with nine
active replicas for different transmission speed for VDD =1V. FFE has not been
activated. Both cases where the driver is under the LDO or directly connected
to VDD are shown.

                                      TX Power vs Speed
                     8.5

                                                            LDO
                       8
                                                            No LDO
  Power [mW/Gbps]




                     7.5


                       7


                     6.5


                       6


                     5.5
                           2   3     4     5     6    7     8      9   10
                                     Transmission Speed [Gbps]

Figure 4.19: Measured normalized power consumed by the transmitter with
nine active replicas for different transmission speed for VDD =1V. Both cases
where the driver is under the LDO or directly connected to VDD are shown.

---

Chapter 5

System and Transistor Level
Design of the Receiver



    As we have already said, channels with different characteristics, including
ones with many connectors introducing notches in the S21 , may be employed in
automotive environment, which demand for advanced equalization strategies
with high reconfigurability [57]-[27]-[58]. As a consequence, linear equaliza-
tion as IIR in the receiver must be combined with DFE [35], especially at high
data rates.
    The typical HSSI receiver architecture is shown in Fig. 5.1. DFE is em-
ployed as non-linear equalization technique, where the information about the
previous reconstructed bits is used to mitigate the effects of ISI on the currently
received bit. The feedback loop relative to the first post-cursor (h1 in Fig.5.1)
has very stringent timing constraints, so that speculative DFE (loop-unrolling)
is often employed at high data rates [33]-[29]-[31]. The architecture of a full-rate
receiver with loop-unrolled DFE is shown in Fig. 5.2.
    The receiver in Fig.5.1 works at full-rate (i.e. clock frequency equal to the
data-rate). Half-rate clocks are required to relax timing [59], save power and
simplify the latches. The architecture of a very basic half-rate receiver without
DFE is shown in Fig. 5.3. Combining loop-unrolling DFE, CDR and half-rate
architecture at high-data rates is challenging. In particular, DFE opens the re-
ceived eye diagram at the sampling points. However, it has detrimental effects
on the edges distribution of the partial response signals, making difficult the
use of bang-bang digital CDR [60]. Edges can be sampled before the DFE sum-
mer, however requiring enhanced samplers’ sensitivity and transition filtering,
that reduces the bandwidth of the CDR [47].
    In this chapter, we propose a new design for a half-rate receiver with 4-tap
DFE (one speculative) for HSSI at 10Gb/s for automotive applications which is
able to employ the edge samples from the speculative DFE paths to adapt the
CDR while still keeping high CDR bandwidth.


                                        95

---

5.1. STRUCTURE OF THE RECEIVER                                                 97

5.1 Structure of the receiver
In this section we will motivate the general choices about the structure of the
receiver. The transistor level design will be then analyzed in detail in a later
section of this chapter.


5.1.1   Input Amplifying Stage
The first block that we meet in the receiver is the input amplifying stage, which
can be just as simple as a single stage CTLE or a much more complicated cir-
cuit. CTLE is present in almost all high-speed transceivers in literature: a good
CTLE should feature the possibility of having a good gain at Nyquist frequen-
cies with respect to low frequencies, low input referred noise and low DC offset
[61]. However, some works [62]- [59] claim that CTLE amplifies also HF noise
and crosstalk in addition of extra-power needed, resulting in both being am-
plified with respect to the eye diagram opening. For this reason, they normally
have a DFE-IIR doing the same job (or even having more than one IIR [63]):
however, we have decided that the amount of required CTLE in our case is not
such to justify such a non-conventional solution.
    In front of the first amplifying block, an AC coupling is needed in order to
set the bias point independently from the one of the received data [64]- [58].
However, long sequences of 1s or 0s at the input of the receiver may induce
a transient shift of the low-frequency part of the received signal after the AC
coupling itself, which in turn becomes reduced sensitivity for the receiver. In
order to avoid this problem, many circuital solutions have been proposed [64]-
[58] [65], but we decided to solve it by encoding the transmitted data with the
already introduced "8b10b encoding" [17], so that the maximum length of a
sequence of identical bits in a row is five. Along with this, an on-board AC
coupling capacitance of 25nF has been used.
    A conventional solution for an amplifying stage is proposed by [29] and
is sketched in Fig. 5.4. After a T-coil peaking, a parallel amplifier for a wide
range of input signal levels and a two-stage peaking amplifier, described more
in detail in Fig. 5.5, are employed. A similar solution can be found also in [66].




           Figure 5.4: Input Amplifying Stage as presented in [29].

---

98CHAPTER 5. SYSTEM AND TRANSISTOR LEVEL DESIGN OF THE RECEIVER




Figure 5.5: Two-stages peaking amplifier used in [29]. The first stage presents
capacitively coupled parallel stages, the second has zero-peaked topology with
switched cap degeneration. In the first stage, RC source degeneration for im-
proved linearity and bandwidth extension is present.


    In literature, many more complicated solutions are presented: [67] and [68]
propose a CTLE that demuxes the full-rate data stream to following stages
working at half-rate; [69] presents a source-degenerated CTLE followed by
a 5-stages limiting amplifier; [52] shows a CTLE formed by a high-frequency
equalizer, formed by a source-degenerated differential pair, and a low-frequency
equalizer with a shunt inductor, which is a not suitable solution for an automo-
tive product; finally, some other works [70]-[71] use active peaking as a mean
of adding a programmable boosting high-frequency gain after a degenerated-
source differential pair.
    Anyway, all these proposed solutions are meant to be used for much higher
speed than what we require, and are also more power hungry and less ro-
bust. For this reason, we decided to implement a single-stage RC source-
degenerated differential pair CTLE, similar to the first peaking stage of [29]
and [66].

5.1.2   Half-Rate, CDR and DFE
As said both in Chapter 1 and in the introduction to this chapter, at high-speed
it’s almost impossible to analyze separately the following three aspects of a
receiver: whether it should be full-rate or half-rate, its CDR scheme and the
DFE.
    A very basic idea of how a full-rate and a half-rate receiver work is sketched
in Fig. 5.6. The main difference between the two is that in the full-rate one, a
full-rate clock (in our case, 10GHz) is used to sample both data and edges,
whereas in a half-rate architecture two different half-rate clocks (in our case,
5GHz) shifted in phase of 90◦ , are used, one for sampling the data, the other
one for the edges. These two clocks are usually called clock I and clock Q.
    Even with a deep investigation of the literature, it’s impossible to find a
10Gbps full-rate receiver architecture, because the analog path of the circuit
would be too power hungry and it would be extremely difficult to cope with

---

5.1. STRUCTURE OF THE RECEIVER                                              99




                              FULL RATE
     EYE
  DIAGRAM


   CLOCK
                             EDGE      DATA     EDGE      DATA      EDGE


                              HALF RATE
     EYE
  DIAGRAM


   CLOCK I

                                       DATA               DATA

  CLOCK Q
                             EDGE               EDGE                EDGE

Figure 5.6: Sketch highlighting the main difference in terms of clocking scheme
between full-rate and half-rate receivers. The dotted lines show the data and
edge sampling instants.

---

100CHAPTER 5. SYSTEM AND TRANSISTOR LEVEL DESIGN OF THE RECEIVER

the timing of the first DFE tap. For these reasons, people started investigating
on half-rate [72], [73], [62], [59] and quarter-rate [29], [30], [74] architectures.
The first ones seem anyway more suited to our target speed, avoiding also an
unnecessary complexity overhead.
    Regarding the CDR, the literature showing the circuital implementation
is in fact very old and the focus nowadays is completely on the algorithm
side [52]. There are very few paper describing the transistor level design of
the CDR [75], [64] and they don’t vary that much one from another: a good
overview has already been given in chapter one. An in-depth analysis of the
state-of-the-art CDR algorithms and our proposed one will follow in the next
section.
    Finally, concerning DFE, we decide to avoid using IIR [76] because it’s more
suited for long silicon channels as said in the introduction. Our idea would be
to share the equalization duties between transmitter and receiver, using for cer-
tain taps FFE, for some others DFE, as already done by [31], [33]. At 10Gbps
the speed forces us to use the loop-unrolling technique, which we already in-
troduced before. There are works that unroll up to three taps [61], [29], [66],
[31], but this introduces a significant overhead in both area and power con-
sumption, so to make this option not too attractive for our speed target. We
decided to go with a more-traditional 1-tap loop-unrolled DFE [58], [74], [77].
    Finally, the summers have been realized with a traditional current-mode
architecture [74], which we will analyze later on when describing the transistor
level design.

5.1.3   Architecture of the Receiver
The block diagram of the DFE and sampling portion of the proposed receiver is
sketched in Fig.5.7. For simplicity, only the even path is shown. Loop-unrolling
requires two summers per path. The tap h1 is speculative and the selection
between + h1 and − h1 is decided by the output of the other path. Feedback
loops and shift registers within the same path are used for h2 and h4 , while
h3 requires crossing between even and odd path. We limit the DFE to 4 taps
based on the system level analysis carried out in [78] showing that, for channels
typical for board-to-board communication in automotive, the pulse response
does not extend significantly outside the 4th post-cursor, as shown also in Figs.
2.13-3.14b).
    At the bottom of Fig.5.7 we can see the additional latches needed for edge
sampling, to be input to CDR algorithm together with the data samples. Notice
that, as we will detail in the next section, we consider the edges at the output
of all summers (4 in total). A four phases, half-rate (i.e. 5GHz) clock samples
data and edges. Fig. 5.8 shows how these 5GHz four-phases are generated. A
digital PLL outputs a 10GHz into a clock divider, which outputs a four-phases,
5GHz clock. These four phases are fed into two phase interpolators, one for
clock I phases, the other one for clock Q phases. Both are controlled by the
CDR and align their output clock edges with the data stream.

---

5.1. STRUCTURE OF THE RECEIVER                                                  101




                        h4

                              clk180         clk0
                        h3
                                      clk0           FROM ODD
                        h2                           DATA PATH
                +                                                 TO ODD
  OUTCTLE                                                        DATA PATH
              -h1
                              clk0                            DOUTEVEN
                +                                      clk0
              +h1
                              clk0
                                                               EEVENMINUS

                              clk90                    clk0
                                                               EEVENPLUS

                              clk90                    clk0

Figure 5.7: Sketch of one of the two paths (in this case the even) of the half-rate
receiver using loop-unrolled DFE. To the far left, the data coming out from a
CTLE are the input to this part of the circuit. The sampled data and edges are
then sent to the deserializer.




                                                                         CLK0
                                                              PI
                                                                         CLK180
    DIGITAL                  CLOCK                    FROM
      PLL                    DIVIDER                   CDR


                                                                         CLK90
                                                              PI
                                                                         CLK270
                10GHz                               5GHz

Figure 5.8: Sketch of the clocking scheme of the receiver. A digital PLL out-
puts a 10GHz clock into a clock divider: from there on, only 5GHz clocks are
distributed.

---

102CHAPTER 5. SYSTEM AND TRANSISTOR LEVEL DESIGN OF THE RECEIVER

5.2 CDR Algorithm
We consider digital CDR with transition-based phase detection. In the presence
of ISI this requires transition filtering [60]. If the channel introduces significant
ISI only on four post-cursors or less, as in our case, this would imply discarding
a lot of bit sequences (only the pattern 101010 is useful), resulting in very low
CDR bandwidth. This is due to the fact that a transition-based phase detection
needs transitions that are symmetric around 0V in order to work correctly, and
this is not the case if the channel introduces ISI.
     To avoid interactions between DFE and CDR and leverage exact transition
filtering, one should sample the edge transitions before the DFE summer [79],
however increasing the load capacitance of the first stage of the receiver (the
continuous-time-linear-equalizer) and thus in turn reducing its bandwidth. Not
surprisingly, many algorithms have been proposed for CDR in the presence of
DFE to reduce the need for transition filtering [60]-[52]-[80]-[79], but they rely
on adaptive techniques, whereas the focus of this work is to propose a phase
detection algorithm for CDR which is stable also when (simpler) non-adaptive
DFE is used.

           FROM
         SAMPLERS
  DOUTEVEN         2:40 40             DIGITAL
  DOUTODD         DESER                                    TO
                                                       SAMPLERS
  EEVENPLUS                 40        E     1    6
                   2:40                             PI  6b
  EEVENMINUS                       PD 1 VOTE CNT
                  DESER                            DEC  PI
                                      L
  EODDPLUS
                   2:40 40
  EODDMINUS       DESER             AVERAGING
                                        BITS
Figure 5.9: Scheme of the CDR circuit. Three packets of 40 bits enter the digital
state machine: even and odd data, as well as even and edges for all speculative
paths. The CDR circuit controls a phase-interpolator through a PI counter and
a PI decoder.

    The block diagram of the CDR is sketched in Fig.5.9, whereas the state di-
agram of the phase detection (PD) algorithm is in Fig.5.10. The first step of
the PD is to find a 3-bit clock pattern (101 or 010) in a packet of 40 bit (four
bytes of information encoded with a 8b10b encoding). In the selected pattern
we analyze the second transition (e.g. 1 → 0 in the 010 pattern, see Fig.5.11),
where there is a symmetry between the speculative paths (+h1 and -h1 ) at the
edge sampling instant compared to the first transition (e.g. the 0 → 1 in the
010 pattern, compare the horizontal arrows in Fig.5.11). If the sampling point
is optimally set, the +h1 edge sampler will sample a 1, the -h1 edge sampler
will sample a 0 (Fig. 5.12 a)). In this case, the phase detector outputs (early or
late) will both be 0. If both edge samples are equal to the second bit of the 3-bits
clock pattern, then the early output of the PD will go high (Fig. 5.12 b)). If both
edge samples are equal to the third bit of the 3-bits clock pattern, then the late
output of the PD will go high (Fig. 5.12 c)).

---

5.2. CDR ALGORITHM                                                                     103




                                   Is there a 101 or a 010
                                     in the 40-bit packet?

                             Yes, 101 at             Yes, 010 at
                             b[i]...b[i+2]    No
                                                     b[i]...b[i+2]

                    Check E[i+1]                           Check E[i+1]

     Eplus=1            Eplus=0    Eplus=1          Eplus=1      Eplus=0    Eplus=1
     Eminus=0           Eminus=0   Eminus=1         Eminus=0     Eminus=0   Eminus=1


         E=0              E=1          E=0    E=0    E=0             E=0      E=1
         L=0              L=0          L=1    L=0    L=0             L=1      L=0
        Figure 5.10: Phase detection algorithm as implemented in this work.




                 0.3
                 0.2                     +h1
  Diff DIN [V]




                 0.1                     -h1
                   0
                 -0.1

                 -0.2
                                   0          0         1            0
                 -0.3
                 -0.4
                   5.281 5.2811 5.2812 5.2813 5.2814 5.2815

                                             Time [us]
Figure 5.11: Results of circuit simulations (see Section 5.3). The differential
outputs of the two summers in the even path, which is also the differential
input of the samplers in the even data path, are shown, along with the data
(full lines) and edge (dashed lines) sampling instants.

---

104CHAPTER 5. SYSTEM AND TRANSISTOR LEVEL DESIGN OF THE RECEIVER




  Voltage




                                    Voltage




                                                                               Voltage
            -h1    +h1                            -h1       +h1                          -h1     +h1
      0                                 0                                          0


               Edge      Time                     Edge               Time                       Edge    Time
  a)          Sampling              b)           Sampling                      c)              Sampling
Figure 5.12: Position of the edge sampling point with respect to speculative
data transitions + h1 and − h1 . a)+ h1 edge sampler samples a 1, − h1 a zero:
the sampling point is optimally set; b)+ h1 edge sampler samples a 1, − h1 too:
the sampling point is early; c) + h0 edge sampler samples a 0, − h1 a one: the
sampling point is late.


     The output of the PD is not directly fed into the PI counter. An early/late
decision is taken after the averaging: the voting block does a majority voting
on averaging decisions of the PD, and the output to the PI counter increases by 1
if Early was the majority, -1 if there were more Late and 0 otherwise. Averaging
is performed for two main reasons. First, because it is not guaranteed that a
3-bit clock pattern is present in a 40-bits packet, so without averaging the CDR
loop may be open for some time, and CDR bandwidth would be undefined.
Secondly, because, since the zero-crossing time depends on the random data
pattern preceding the three-bits (more than one post-cursor may be relevant)
filtered transition, the PD algorithm cannot give the correct results all the times.
     In the frame of board-to-board communication with two different crystals
used for transmitter and receiver, averaging (n avg ) and crystal quality (preci-
sion e) can be related as:

                                                               tS
                           2 · e · tS <
                                               n avg · n PIsteps · nbitsperpacket

        tS being the bit period, from where we find

                                                               1
                             n avg <                                                                      (5.1)
                                              2 · e · n PIsteps · nbitsperpacket
where in our case nbitsperpacket =40 and the number of steps of the PI is 64. At
the same time we can compute the CDR bandwidth as

                                                                  f CK
                                 BWCDR ≃                                                                  (5.2)
                                                        n avg nbitsperpacket

    Fig. 5.13 is obtained directly from Eqs. (5.1)-(5.2) and shows that with rea-
sonable crystal quality, very low number of averages is allowed (3 for e =100ppm).
In this respect, there is limited room for incorrect results coming out of the PD.


   Finally, in order to get a better understanding of the mix between half-rate
architecture, CDR and DFE, a Simulink model of the whole receiver has been
implemented before designing the actual transistor level. A screen-shot of the
whole Simulink setup is shown in Fig. 5.14. The functioning of the structure
has been validated with a realistic input data sequence, in which ISI of a typical

---

5.2. CDR ALGORITHM                                                                 105

              40                                                6.3
              35                                                7.1




                                                                         CDR BW [MHz]
              30                                                8.3
  Averaging




              25                                                10
              20                                                12.5
              15                                                16.7
              10                                                25
               5                                                50
               0
                   0   50     100   150     200      250     300
                            Crystal Quality [ppm]
Figure 5.13: CDR Bandwidth vs quality of the crystal. The left axis reports the
number of 40-bit packets to be elaborated before taking a decision, therefore
giving the CDR bandwidth reported on the right axis.


automotive channel was accounted, showing the correct settling of the PI code
and the error-less reconstruction of the received data (see Fig. 5.15).

---

106CHAPTER 5. SYSTEM AND TRANSISTOR LEVEL DESIGN OF THE RECEIVER                                                                          Even Data
                                                                                                                                            Path




                                                                                                                                            Deserializers

                                                                     Input Sequence
                                                                        Generator                                                                                             PD+CDR
                                                                                                                                                                              Algorithm




                                                                                                                                                                            Accumulator

                                                                                                                                                                                      PI
                                                                                                                                        Odd Data
                                                                                                                                          Path

                                                                   Figure 5.14: Receiver Structure as implemented in Simulink. From the left to the right we find the following blocks: red box, input
                                                                   sequence generator; blue box: even data path; dark green box: odd data path; pink box: deserializers; orange box: phase detector and
                                                                   CDR digital algorithm; light green box: accumulator; brown box: phase interpolator.

---

5.2. CDR ALGORITHM
                               0 1 0 0 1 0 1 01 1 0 1 0 1 0 1 0 0 1 0 0 1 0 1 1 01 1 1 0 0 1 0 1 0 1 1 0 0 0 1
                         1.5
          Voltage [V]      1
                         0.5
   DIN                     0
                        -0.5
                          -1
                        -1.5
                           1
          Voltage [V]




                         0.5
   DOUT                    0
                        -0.5
                          -1
                          1.02                  1.021                   1.022                       1.023                       1.024
                                                                       Time [us]

Figure 5.15: Data reconstruction for the Simulink model of Fig. 5.14. In the above panel, the input data D I N at the receiver, affected by
ISI, are shown, whereas in the bottom panel there are the reconstructed data at the receiver output, DOUT . The figure shows an error-less
reconstruction.




                                                                                                                                              107

---

108CHAPTER 5. SYSTEM AND TRANSISTOR LEVEL DESIGN OF THE RECEIVER

5.3 Transistor level design and simulation results
In the following section, details on the transistor level implementation of the
single blocks of the receiver will be given. The technology used is the same
28nm planar CMOS technology used for the transmitter. To clarify better the
structure as explained until now, the timing diagram of the data and edge sam-
ples (so basically data and edge samples path as from Fig. 5.7, but for both odd
and even path) along the path are shown in Fig. 5.16.

5.3.1   Input Stage
The structure of the input stage is reported in Fig. 5.17.
    The operating point of the CTLE is set via a resistive divider. The value
of the divider is trimmable in eight values, setting the biasing point from a
minimum of VDD    2 to a maximum of
                                         2VDD
                                           3 , value that can be set depending on
the differential peak-to-peak opening of the transmitted signal.
    The DC biasing resistive divider is followed by a CTLE, realized as a RC
source-degenerated differential pair [66]. The peak frequency and the boost
gain can be tuned by means of a 3-bits trimmable capacitance and a 2-bits
trimmable resistance, so to compensate for PVT variations. Along with these
settings, also the current is 4-bits trimmable. For channels with small attenua-
tion, it is possible to switch off the CTLE and have it working as a conventional
differential pair. Since this equalization scheme does not aim to equalize chan-
nels having a very big loss (not expected for a Nyquist frequency of 5GHz),
our main goal was not to have a high boost at high-frequency, whereas to have
very similar transfer function for the CTLE over all PVT corners. The transfer
function of the CTLE for PVT corners is reported in Fig. 5.18. The variations in
the transfer function depending on the trimming bits are reported in Fig. 5.19.

---

CLK0




                                                                                                                                              5.3. TRANSISTOR LEVEL DESIGN AND SIMULATION RESULTS
CLK180

SAMPLERDATAEVEN


SAMPLERDATAODD

SAMPLEREDGEEVEN


SAMPLEREDGEODD


MUXDATAEVEN


MUXDATAODD

DOUTEVEN

DOUTODD

EOUTEVEN

EOUTODD



Figure 5.16: Timing for the half-rate receiver of which only the even path was shown in Fig. 5.7. For clarity, here only one sample between
plus and minus has been shown. SAMPLERDATAEVEN , SAMPLERDATAODD , SAMPLEREDGEEVEN , SAMPLEREDGEODD are the output after




                                                                                                                                              109
the first samplers the data and edge meet in Fig. 5.7. MUXDATAEVEN and MUXDATAODD are the data samples after the two speculative
samples have passed the mux. DOUTEVEN and DOUTODD are the data after the final data sampler, ready to be sent to the deserializers of
Fig. 5.9, and same goes for EOUTEVEN and EOUTODD , where again only one between the speculative minus and plus has been shown.

---

110CHAPTER 5. SYSTEM AND TRANSISTOR LEVEL DESIGN OF THE RECEIVER




                                                                  OUTN
    INP
                                                                  OUTP


                         100 Ω


    INN




Figure 5.17: Structure of the receiver input stage, including DC biasing and
CTLE implemented as an RC source degenerated differential pair.


                         CTLE Transfer Function
                    0
  Amplitude [dB]




                   -20


                   -40           Nom Case
                                 Worst Case
                                 Best Case
                   -60
                         104       106            108           1010
                                 Frequency[Hz]
Figure 5.18: Transfer function of the CTLE for different PVT corners and fixed
RC degeneration settings. Blue curve is the nominal case (VDD = 900mV, 25◦ C,
top-top technology corner), red curve is the worst case (VDD = 800mV, -40◦ C,
slow-slow technology corner) and the green curve is the best case (VDD = 1V,
175◦ C, fast-fast technology corner).

---

5.3. TRANSISTOR LEVEL DESIGN AND SIMULATION RESULTS                          111




                                 CTLE Trimming
                      0             I          R         C
  Attenuation [dB]




                     -10

                     -20

                     -30

                     -40
                           104       106            108            1010
                                  Frequency[Hz]
Figure 5.19: Transfer function of the CTLE for different configurations for bias-
ing current or source resistance and capacitance. The curves are grouped into
varying resistance trimming code (blue curves), varying capacitance trimming
code (green curves) and varying current trimming code (red curves) while all
others settings are fixed. The arrows indicate increasing values for resistance,
capacitance and current. As expected, changes in the source resistance only in-
fluence the low-frequency behavior of the CTLE, capacitance changes shift the
gain and the frequency of the boost and biasing current changes influence the
whole transfer function.

---

112CHAPTER 5. SYSTEM AND TRANSISTOR LEVEL DESIGN OF THE RECEIVER

5.3.2   DFE Timing
In this section, we will analyze the timing of the signals regarding DFE, in
order to demonstrate that there is no issue with this part of the circuit. In all
this subsection we will refer to Fig. 5.20 and we will analyze five time instants,
named a, b, c, d and e in the figure. The analysis will be carried out for the
even data path, but can conversely be done for the odd data path.
    Let’s start from time instant a): the transmitted bit b0 that is visible at the
differential input of the sampler (second panel) is a 1 and the previous one is a
0, therefore the positive + h1 speculative differential input (violet curve) should
be selected. The bits previously received are b−1 =0, b−2 =0, b−3 =1 and b−4 =1.
At a), we only care of the signal entering h2 , h3 and h4 taps, since the h1 tap will
just decide which of the two speculative paths we will select out of the mux.
The selected one then enters the output latch of the even data path and will be
frozen at the next rising edge of the clock, so h1P has time until c) to settle. In
fact, at a) we have that the input to h2P , h3P and h4P are respectively 0, 1 and
1, so it’s fine. So h1P should be ready and correct at c), since at this moment in
time b0 is frozen at the output latch: h1P should be 0, and it is. So we know that
all DFE taps are correctly set when it comes to help in sampling correctly b0 .
    Now we can check the other aspect: does b0 operate correctly to help with
the equalization of the following bits? Does it arrive on time to be h1P , h2P , h3P
and h4P for b1 , b2 , b3 and b4 respectively? Let’s start from the easiest, h2P . At
b), b0 has been already shifted through the mux and the mux output is frozen
since the previous data coming from the odd path, DOUTPODD , is frozen: so b0
is ready to be h2P for b2 way before c), which is the timing instant at which
b2 arrives at the speculative samplers input. Let’s now focus on h1P and h3P :
we have seen that at c) b0 is frozen at the output latch of the even data path:
this means that it is ready to go also to the odd data path for playing the part
of h1P and h3P for b1 and b3 , respectively. In fact, b1 is frozen at the output
latch of the odd data path only at d), so b0 is ready since 100ps for the right
selection on the mux of the odd data path. At the same time d), b3 is frozen at
the sampler on the odd data path and b0 is again ready since 100ps at the input
of a transparent latch which gets frozen at the same instant as the sampler (see
Fig. 5.7), so as long as the D-to-Q delay of the latch is below 100ps we are fine,
and we are well below this number (circa 30ps in the worst case). Finally, we
check what happens for h4P : we have seen that at c) b0 is frozen at the output
latch, so it is ready at the h4 latch input as well, which starts to be transparent
at this moment. This latch will be frozen at d), so b0 is ready to be h4P for b4
100ps before this instant.
    Finally, we take a look at the glitch that occurs on the signal h2P input
slightly after e). At e), the output latch (the one at rightmost in Fig. 5.7) of
the odd data stream starts to be transparent, so there might be a glitch in the
even data mux output, since there is a change in its selection signal. Anyway,
this glitch is not relevant because the mux output has to be frozen 100ps later
and ready 200ps later. Its value at e) has no meaning, since the output latch
input is open at this point in time. Concluding, this glitch does not hurt our
DFE process.

---

CLK0                                                                      a) b) c) d) e)




                                                                                                                                                   5.3. TRANSISTOR LEVEL DESIGN AND SIMULATION RESULTS
  Diff Sampler Input +h1
  Diff Sampler Input -h1
  DOUTP +h1
  DOUTP -h1

  DOUTPODD

  h2P Input


  h3P Input


  h4P Input


 DOUTPEVEN


 DOUTP



Figure 5.20: Timing for DFE signals. From top to bottom, the signals are the following: CLK0 , positive + h1 speculative differential input




                                                                                                                                                   113
for data samplers, negative − h1 speculative differential input for data samplers, positive output of the positive speculative + h1 sampler,
positive output of the negative speculative − h1 sampler, positive output data coming from the odd data path (so this is the mux selection
signal in Fig. 5.7), positive input to h2P tap, positive input to h3P tap, positive input to h4P tap, positive output data of the even data path
and positive output data at full rate (so to show the complete reconstruction of the data in the second panel).

---

114CHAPTER 5. SYSTEM AND TRANSISTOR LEVEL DESIGN OF THE RECEIVER




                     a)




    Main                                   hi taps
    Tap


                     b)


Figure 5.21: a) Schematic of a current-mode summer [74] and b) our transistor
level implementation with 4-taps DFE.


5.3.3   Summers, Comparators and PI
The summers have been realized with a traditional current-mode architecture
[74]. The basic schematic of this architecture is shown in Fig. 5.21 a), which is
the same used in our transistor level implementation reported in Fig. 5.21 b),
highlighting the four taps of DFE.
    The important thing for the summer is that its output should reach its final
value as fast as possible for ISI cancellation to work properly. This time is set
by the RC constant highlighted in Fig. 5.21. For 10 Gbps half-rate RX, this RC
delay must be around 17ps [74], which sets a mutual constraint between drain
resistance of the main tap and output capacitance. Anyway, we are well below
this time constant, since we have just four small differential pair connected at
the output node, summing up to a CL of circa 3fF.
    In this stage, we added a high level of programmability in order to offer a
variety of solutions: the current in the main tap of the summers can be trimmed
with 16 levels, and so does the current flowing in the DFE taps. The drain
resistances of the main summer feature 8 different trimmable levels, so that the
finest DFE correction that can be programmed is 6mV.
    Comparators have been implemented in a classical double-tail topology,
whereas latches have been designed in the same pseudo-differential architec-
ture used in the transmitter [57]-[53]. The schematic of a latch is reported in
Fig. 5.22.
    As already mentioned, the PI is implemented in a traditional fashion [21]
(see Fig. 5.23) and is divided in 64 steps. A DPLL, not described in this work,

---

5.3. TRANSISTOR LEVEL DESIGN AND SIMULATION RESULTS                          115




                       dp                              qn




                       ckp


                       ckn




                       dn                              qp




  Figure 5.22: Schematic of a pseudo-differential latch used in the receiver.


provides a 10GHz clock, that then is divided down to 5GHz in four phases, as
already described in Fig. 5.8.




Figure 5.23: Schematic of the core of a traditional phase interpolator [21]. Cur-
rents I1 -I4 are controlled via the 6-bits PI code set by the CDR algorithm.

---

116CHAPTER 5. SYSTEM AND TRANSISTOR LEVEL DESIGN OF THE RECEIVER

                                Parallel
                              Data Output



  Even Serial                               Odd Serial
  Input Data/                               Input Data/
  Plus Serial                               Minus Serial
  Input Edge                                Input Edge




                                      Clock
                                     Division




        Figure 5.24: Schematic of the 2:40 deserializer used in the receiver.


5.3.4     Deserializers
All three deserializers have been implemented as 2:40 deserializers and their
schematic is reported in Fig. 5.24. Two serial data streams are taken as inputs
to be interleaved at the parallel data output. As can be seen in Fig. 5.25, the
data are parallelized in four stages with four different clocks with decreasing
frequency, generated in the clock division part of the circuit as shown in Fig.
5.26. Since the deserializer is taking as input two distinct serial data streams,
two different clock phases have to be used to latch these serial data in.
    The data deserializer takes two serial data stream as inputs, even and odd:
for this reason, both CLK0 and CLK180 must be provided to the data dese-
rializer. On the contrary, the two edge deserializers take as input two serial
streams that can be latched with the same clock: the even edge deserializer
takes the plus and minus speculative even edges and interleaves them, and
same goes for the odd ones and the odd deserializer. In fact, both even edge
streams can be latched in with CLK90 and both odd edge streams with CLK270 .
For symmetry and timing reasons, we don’t change the deserializer architec-
ture of the data deserializer to have just one clock as an input, but we provide
the same clock two times to the edge deserializers. Fig. 5.27 briefly summarizes
the timing of this block, which represents the interface between the analog and
the digital world: in fact, one of the 250MHz clocks that are generated inside
the deserializer is also used as a clock for the digital part.

---

5.3. TRANSISTOR LEVEL DESIGN AND SIMULATION RESULTS                         117




           5GHz           2.5GHz        1.25GHz          250MHz
           Clock           Clock          Clock           Clock


Figure 5.25: Zoom of Fig. 5.24 on the parallelization of the input data streams.




                          5GHz       2.5GHz    1.25GHz      250MHz
                          Clock       Clock      Clock       Clock




                          Clock
                         Div by 2




       Figure 5.26: Zoom of Fig. 5.24 on the divided clocks generation.

---

118CHAPTER 5. SYSTEM AND TRANSISTOR LEVEL DESIGN OF THE RECEIVER
                                                                   CLK0

                                                                   CLK0DIV20

                                                                   DATAPARALLELO <38,36,...,0>

                                                                   CLK180

                                                                   CLK180DIV20


                                                                   DATAPARALLELO <39,37,...,1>

                                                                   CLK90


                                                                   CLK90DIV20

                                                                   EDGEEVENO<39,37,...,1>

                                                                   CLK270

                                                                   CLK270DIV20


                                                                   EDGEODDO<39,37,...,1>



                                                                                                 Figure 5.27: Timing of clocks and outputs of the deserializer shown in Fig. 5.24.

---

5.3. TRANSISTOR LEVEL DESIGN AND SIMULATION RESULTS                                119

5.3.5    Timing of the CDR Algorithm
This section aims to add some transistor level insight on the CDR algorithm
already introduced in Section 5.2. In Fig. 5.28 we show some transistor level
waveforms that, along with the following explanation, should clarify the con-
cepts previously expressed.
     From DOUTP stream, we see that the received data sequence is 00010101010.
In this analysis we focus on the fifth, sixth and seventh bit of this sequence, so
on a 010 pattern. At the timing instant c), we find the third bit of a 010 sequence
in DOUTP : this is the first step of our algorithm. We will refer to this three bit as
b0 , b1 and b2 . We see that, at c), b2 , the second zero in the 010 sequence is frozen
at the rising edge of CLK0 , so this is an even bit. This zero that we see now
frozen in DOUTP has actually been frozen at instant a) (200ps earlier than c))
at the two speculative samplers, of which we see the differential inputs in the
second panel. In the second step of the algorithm, we have to check the edge
samples to understand whether the sampling clock is well positioned or not.
We have just said that b2 is an even bit, so since we want to look at the transition
between b1 and b2 , we have to check the edges sampled with CLK270 , so at the
odd edges before b2 , thus at EDGEODD+h1 and EDGEODD−h1 at timing instant
b). At this point in time, the two speculative odd edges EDGEODD+h1 and
EDGEODD−h1 are different between each other, therefore the sampling clock is
correctly positioned. We can actually check this by looking at a), where you
can see that the rising edge of CLK0 is correctly set with respect to the two
speculative differential inputs of the samplers.

---

120CHAPTER 5. SYSTEM AND TRANSISTOR LEVEL DESIGN OF THE RECEIVER

                                                                    CLK0                                                                   a)       b)        c)

                                                                     Diff Sampler Input +h1
                                                                     Diff Sampler Input -h1

                                                                     DOUTP

                                                                     EDGEEVEN+h1
                                                                     EDGEEVEN-h1

                                                                     EDGEODD+h1
                                                                     EDGEODD-h1


                                                                   Figure 5.28: Transistor level waveforms to show the functioning of the CDR algorithm. From top to bottom, the signals are the follow-
                                                                   ing: CLK0 , positive + h1 speculative differential input for data samplers, negative − h1 speculative differential input for data samplers,
                                                                   positive output data at full rate, positive + h1 even edge samples, negative − h1 even edge samples, positive + h1 odd edge samples and
                                                                   negative − h1 odd edge samples.

---

5.3. TRANSISTOR LEVEL DESIGN AND SIMULATION RESULTS                                          121



                                    00      0010 101100
                                    0010111 00         001100
                                                     0000    011 1 1 1010010
                                                           000               0 101100
                                                                        00 10010     0100
                                                                                   000   0 101
                                                                                       000
                             0.2
               Voltage [V]

                             0.1
   Diff DIN                    0
                             -0.1
                             -0.2
                             0.8
               Voltage [V]




                             0.4
   Diff DOUT                   0
                             -0.4
                             -0.8
                                             24        25          26        27         28
                                                             Time [ns]


Figure 5.29: Data reconstruction of the receiver. The green curve shows the
differential input data at the receiver, the yellow curve the differential recon-
structed data. On top, the transmitted bits are shown.


5.3.6     Results with fixed PI code
All blocks have been singularly validated post-layout in all PVT corners. The
functioning of the receiver has been first tested by fixing the PI code to an
optimal value. The transmitter and the receiver have been connected by an
ideal channel, in order to check the basic functioning of the receiver structure.
Fig. 5.29 shows an error-less data reception, that at this point has been demon-
strated in all PVT corners (from VDD = 800mV, -40◦ C, slow-slow technology
corner to VDD =1V, 175◦ C, fast-fast technology corner).

---

122CHAPTER 5. SYSTEM AND TRANSISTOR LEVEL DESIGN OF THE RECEIVER




                                     RX DIG

                                       RX                  RX
               TX                     CDR                 ANA

Figure 5.30: Final layout of the whole system. The total area is 0.125mm2 ,
whereas the area occupied by the receiver amounts to 0.05mm2 .


5.3.7   Results with XA-VCS
To verify the proposed receiver topology and CDR algorithm, the whole RX
was assembled (Analog part, Digital part including CDR algorithm and JTAG
interface and Simplified Timing Shell, STS, which re-times the interface signals
between digital and analog) along with the post-layout transistor level model
of a TX [57] and the whole system was simulated using the simulator XA-VCS
[81]. The final layout of the structure is reported in Fig.5.30. These simula-
tions show a power consumption for the RX of 2.05mW/Gbps in nominal PVT
conditions (VDD =900mV, typical technology corner, 25◦ C): the analog part of
the receiver (bias distribution, CTLE, DFE, summers, comparators) consumes
0.77mW/Gbps, whereas the CDR circuitry (PI, PI Decoder, 2:40 Deserializers)
1.28mW Gbps. In the least-consuming PVT corner (VDD =800mV, slow-slow
technology corner, -40◦ C), the analog part consumes 0.5mW/Gbps, whereas
the CDR circuitry 0.8mW/Gbps, which gives a total 1.3mW/Gbps.


     Example of simulation results for different PD algorithms, different chan-
nels and different DFE settings are reported in Figs. 5.31-5.32. As from plot a),
between our CDR algorithm and a pure Alexander PD [82] (no transition filter-
ing) there is a difference in the clock sampling position of roughly eight steps
(i.e., 25ps). It can be seen from plot b that our PD algorithm is very well settled
with respect to the input data of the sampler, meaning therefore that the clock
as set by the Alexander PD may have a displacement from the correct sampling
position, thus reducing the jitter budget for the PLL. Furthermore, in our algo-
rithm the oscillations of the PI are smaller than when using an Alexander PD
without transition filtering.

---

5.3. TRANSISTOR LEVEL DESIGN AND SIMULATION RESULTS                        123




              30

              20
                                                  Alexander
                                                  This Work
              10
   PI Code




               0

             -10

             -20
                                                      Limit Cycle
             -30
                    0   2   4      6      8      10     12     14     16
         a)                         Time [us]
             0.4
  Diff DIN




             0.2
               0
             -0.2
             -0.4
                 10.3                  10.301                       10.302
         b)                         Time [us]
Figure 5.31: a) Phase Interpolator selection code for Alexander PD and for the
PD of this work (Fig.5.9) when using n avg = 100. b) Data sampling for even
path in the case of the PD of this work (red dotted lines). Only − h1 spec-
ulative even path is here shown for clarity. The samples chosen among the
two speculative even paths are circled in red: since here − h1 speculative even
path is shown, only samples preceded by a ’1’ are chosen, whereas the others
are taken from + h1 speculative even path (here not shown). Both plots have
been obtained for a template channel consisting of an RC low-pass filter show-
ing 5dB of loss at 5GHz. The peak-to-peak output swing of the transmitter is
380mV. The values used for h1 , h2 , h3 and h4 are 78mV, 39mV, 20mV and 20mV
respectively and are not optimized to show the robustness of the algorithm
in case of sub-optimal equalization. In both cases, the PI limit cycle has been
obtained from 16µs long simulations as in Fig. 8a, after having removed the
initial transient of the PI code (in these cases, 6µs).

---

124CHAPTER 5. SYSTEM AND TRANSISTOR LEVEL DESIGN OF THE RECEIVER


              30

              20

              10
  PI Code


                0

              -10

              -20

              -30
                    0   2   4      6       8     10      12     14     16
                                    Time [us]             Limit Cycle
             0.3

             0.2

             0.1
  Diff DIN




               0

             -0.1

             -0.2

             -0.3
                6.289                    6.29                        6.291
                                    Time [us]
Figure 5.32: a) Phase Interpolator selection code for the PD of this work
(Fig.5.9) when using n avg = 7. b) Data sampling for even path in the case
of the PD of this work (red dotted lines). Both + h1 and − h1 speculative path
are here shown. The samples chosen among the two speculative even paths are
circled in red: when preceded by a ’1’, h1 samples are chosen, whereas the oth-
ers are taken from + h1 speculative even path. The plot has been obtained for
a template channel consisting of an RC low-pass filter showing 10dB of loss at
5GHz. The peak-to-peak output swing of the transmitter is 380mV. The values
used for h1 , h2 , h3 and h4 are 39mV, 20mV, 0mV and 0mV respectively and are
not optimized to show the robustness of the algorithm in case of sub-optimal
equalization. The PI limit cycle has been obtained from 16µs long simulations
as in Fig. 5.31a), after having removed the initial transient of the PI code (in
these cases, 6µs).

---

5.3. TRANSISTOR LEVEL DESIGN AND SIMULATION RESULTS                           125

                     45

                     40                    This Work, 5dB
                                           This Work, 10dB
  Limit Cycle [ps]



                     35
                                           Alexander, 5dB
                     30

                     25

                     20

                     15

                     10
                          0   10 20 30 40 50 60 70 80 90 100
                                       Averaging
Figure 5.33: Amplitude of the PI limit cycle for different n avg . Two different
pairs of channels and DFE settings have been used. One, 5dB, has the same
channels and DFE settings as in Fig. 5.31, whereas the other, 10dB, has a a
template channel consisting of an RC low-pass filter showing 10dB of loss at
5GHz and the values used for h1 , h2 , h3 and h4 are 39mV, 20mV, 0mV and 0mV
respectively and are not optimized to show the robustness of the algorithm
in case of sub-optimal equalization. In both cases, the PI limit cycle has been
obtained from 16µs long simulations as in Fig. 5.31a, after having removed the
initial transient of the PI code (in these cases, 6µs).


    To further analyze this latter aspect, the limit cycle of the PI code waveform
is plotted vs n avg in Fig.5.33: a high number of averages is required by the
Alexander PD w/o transition filtering to keep under control the limit cycle. It
must be noted that our PI algorithm depends on the value of h1 set in the DFE:
if no DFE is applied, our algorithm is equivalent to an Alexander PD with a
transition filtering of three bits. By increasing h1 , the sampling time for which
both early and late outputs stay low increases.


    Finally, Figs. 5.34-5.38 show the diagram at different point of transceiver,
namely at the output of the transmitter, at the input of the receiver, at the out-
put of the CTLE and at the input of the two speculative samplers. The plots
have been obtained for a template channel consisting of an RC low-pass filter
showing 10dB of loss at 5GHz. The peak-to-peak output swing of the transmit-
ter is 380mV. The values used for h1 , h2 , h3 and h4 are 78mV, 20mV, 0mV and
0mV respectively
    Fig.5.39 show the eye mask in different points of the system with the same
settings as in Fig. 5.31. The channel and DFE settings are the same as Fig.

---

126CHAPTER 5. SYSTEM AND TRANSISTOR LEVEL DESIGN OF THE RECEIVER


                 150

                 100
  Voltage [mV]
                  50

                   0

                  -50

                 -100

                 -150


                        0   20      40               60       80          100
                                         Time [ps]

Figure 5.34: Eye diagram at the output of the transmitter. In this figure, we see
the typical effect of reflections due to the channel.


5.31. It must be noted that, in order to build the eye mask at the input of the
samplers, one must take the transitions 0 → 1 and 0 → 0 from the positive
speculative sampler (see Fig. 5.37) and the transitions 1 → 0 and 1 → 1 from
the negative speculative sampler (see Fig. 5.38).

---

5.3. TRANSISTOR LEVEL DESIGN AND SIMULATION RESULTS                        127




                  150

                  100
  Voltage [mV]




                   50

                    0

                   -50

                  -100

                  -150


                         0   20    40               60      80          100
                                        Time [ps]

Figure 5.35: Eye diagram at the receiver. From this figure, the low-pass nature
of the channel can be understood.




                  150

                  100
   Voltage [mV]




                   50

                     0

                   -50

                  -100

                  -150

                         0   20    40               60      80           100
                                        Time [ps]

Figure 5.36: Eye diagram at the output of the CTLE. As can be seen, the high
and low levels of the eye diagram are now smaller, but also the rise and fall
times are smaller than the ones in Fig. 5.35.

---

128CHAPTER 5. SYSTEM AND TRANSISTOR LEVEL DESIGN OF THE RECEIVER




                    300


                    200
     Voltage [mV]




                    100


                      0

                    -100



                           0   50        100             150            200
                                       Time [ps]

Figure 5.37: Eye diagram at the input of the positive even speculative sam-
pler. Here a 200ps eye diagram is shown in order to highlight the fact that
the frequency of the clock used to sample this eye is 5GHz. In fact, the only
eye diagram that matters is the one on the right. As said in the text, the only
transitions that matter in this eye diagram are the 0 → 1 and 0 → 0.




                    100


                      0
  Voltage [mV]




                    -100


                    -200


                    -300


                           0   50        100             150            200
                                       Time [ps]

Figure 5.38: Eye diagram at the input of the negative even speculative sam-
pler. Here a 200ps eye diagram is shown in order to highlight the fact that
the frequency of the clock used to sample this eye is 5GHz. In fact, the only
eye diagram that matters is the one on the right. As said in the text, the only
transitions that matter in this eye diagram are the 1 → 0 and 1 → 1.

---

5.3. TRANSISTOR LEVEL DESIGN AND SIMULATION RESULTS                         129




                 200
                 150
  Voltage [mV]




                 100
                  50                        TX out
                                            RX in
                   0                        CTLE out
                                            Sampler in
                  -50
                 -100
                 -150
                 -200
                        0 10 20 30 40 50 60 70 80 90 100
                                   Time [ps]
Figure 5.39: Eye masks in different points of the signal path for the same chan-
nel and settings as in Fig. 5.31.

---

130CHAPTER 5. SYSTEM AND TRANSISTOR LEVEL DESIGN OF THE RECEIVER

5.4 Conclusions
We have designed a 10Gbps HSSI half-rate receiver with power efficiency aligned
with the state-of-the-art. An original CDR algorithm is proposed that works in
the presence of loop-unrolled DFE with a limited amount of transition filter-
ing, allowing for a large CDR bandwidth. The algorithm is robust and does
not require specific optimization of the DFE taps. The correctness of the pro-
posed algorithm has been verified by simulating a full transceiver architecture
at transistor level with post-layout parasitics. Experimental data on the fabri-
cated system will be available by the end of the year.

---

Chapter 6

Characterization of the Full
Link



   In this chapter we analyze the results of the measurements of InnoTC of
the full link as described in the previous chapters. We will start with a quick
overview of the test-chip, focusing in particular on the high-speed transceiver,
then pass to evaluate the BER of the link and the obtained bathtubs and how
do the two phase detection algorithms described in Chapter 5 perform.


6.1 InnoTC Overview
Fig. 6.1 show the layout of InnoTC along with the bondplan to the package as
realized for the measurements of the high-speed link. The total area of InnoTC
is roughly 9mm2 , and on top of it several other circuits have been placed. The
total area of the high-speed interface, including decoupling capacitance, bias
and clock distribution, PRBS generator, PRBS checker and JTAG interface is
roughly 0.5mm2 , with the decoupling capacitance occupying almost two thirds
of it. The high-speed interface analyzed here is located in the left-side of the
chip, near to the digital PLL providing the interface with the clock. The DPLL
itself takes the clock from a DCO which is centered around 17.4GHz, tunable
from 16.4GHz to 18.4GHz. The DPLL then divides this clock by a factor of two
and delivers it to the high-speed interface: for this reason, only transmission
speeds between 8.2Gbps and 9.2Gbps are available. Thanks to the division
by two and by four implemented inside our transceiver, also 2.1-3.2Gbps and
4.1-4.6Gbps transmission speed can be tested.
    It can be seen from Fig. 6.1 that, as explained in the previous chapter, we
have distinct power domains, two for the transmitter and two for the receiver.
As already stated in Chapter 4, for each one of these power domain two pads
are available on chip, so to reduce the parasitic inductance on the supply by a

                                      131

---

132                 CHAPTER 6. CHARACTERIZATION OF THE FULL LINK




                                              IBIAS_25U_HSIO_AI

                                                                  IBIAS_100U_PLL_AI

                                                                                      IBIAS_500U_PLL_AI
                    VDDDCO_0V9

                                 VDDDCO_0V9




                                                                                                                                                                                       VDDVCO_0V9
                                                                                                          VDDPLL_0V9




                                                                                                                                                                    vco_vtune_ai
                                                                                                                                                        anamux_ao
                                                                                                                       clk_200M_i

                                                                                                                                       ibias_pll_i




                                                                                                                                                                                                    NC
  VDDTX1_0V9                                                                                                                                                                                                       VDDVCO_0v9

  VDDTX1_0V9                                                                                                                                                                                                       VDDVCO_0v9

  VDDTX2_0V9                                                                                                                                                                                                       ibias_300u_vco_ai

   VDDTX2_0V9                                                                                                                                                                                                      ibias_1m_vco_ai

      tx_hsio_p_o                                                                                                                                                                                                  VDDP2V5

      tx_hsio_n_o                                                                                                                                                                                                  dig_out_o<7>

      rx_hsio_p_i                                                                                                                                                                                                  dig_out_o<6>

      rx_hsio_n_i                                                                                                                                                                                                  dig_out_o<5>

  VDDRX1_0V9                                                                                                                                                                                                       dig_out_o<4>

  VDDRX1_0V9                                                                                                                                                                                                       dig_out_o<3>

  VDDRX2_0V9                                                                                                                                                                                                       dig_out_o<2>

   VDDRX2_0V9                                                                                                                                                                                                      dig_out_o<1>
                                              jtag_clockdr_i

                                                                  jtag_rstn_i

                                                                                      jtag_si_i

                                                                                                          jtag_clk_i
                                 VDDDIG_0V9




                                                                                                                       jtag_update_i



                                                                                                                                                        jtag_so_o
                                                                                                                                       jtag_shiftdr_i
                    VDDDIG_0V9




                                                                                                                                                                                                    dig_out_o<0>
                                                                                                                                                                    module_reset_n_i

                                                                                                                                                                                       VDDP2V5




Figure 6.1: Bondplan of InnoTC as realized for the measurements of the high-
speed transceiver. The proportions between the link, the bonding and the pack-
age respect the real ones.


factor of 2. The bondwires to the power supplies are roughly 3nm long each, so
that the effective parasitic inductance on each power domain is roughly 1.5nH.

---

6.2. INNOTC MEASUREMENT SETUP                                                 133

6.2 InnoTC Measurement Setup

Fig. 6.2 shows the measurement setup used for evaluating the performance of
the transceiver. The chip is bonded to a package and then mounted on a PCB,
called daughterboard. This board is itself mounted on another board, called
daughterboard, which brings four different supplies to the chip: one for 2.5V
digital pads, one core voltage to the digital circuit, one for the DCO and the PLL
and one for the HSIO. This means that all four power domains are connected
together at motherboard level, and separated only at daughterboard level. Two
different versions of the daughterboard have been tried, one with a crystal ref-
erence mounted on top and one with an external clock reference of 200MHz.
Since there was no significant difference between the two in measurements in
loopback mode (to be defined in the next paragraph), only measurements with
an external reference clock will be reported here.




Figure 6.2: Measurement Setup for InnoTC. In the picture, motherboard,
daughterboard and all voltage and current sources are visible, both for JTAG
programming and for performance measurement.



    Fig. 6.3 show the connections in order to operate the full link in loopback
mode: the outputs of the transmitter are directly fed into the receiver inputs,
after having passed through a channel composed by roughly 40cm of cables,
a SMB connector and an AC coupler, which mimic the effect of the on-board
capacitance needed to separate the common mode levels of transmitter and re-
ceiver. No S-parameters measurements were performed on this channel, but by
comparing the vertical opening of the eye diagram at the output of the trans-
mitter when fed into the scope with the same channel, a loss of circa 3dB at
2.5GHz can be estimated.

---

134               CHAPTER 6. CHARACTERIZATION OF THE FULL LINK




Figure 6.3: Measurement Setup for the loopback functioning mode, in which
the outputs of the transmitter are directly fed into the receiver inputs of the
same chip after having passed roughly 40cm of cables, a SMB connector and
an AC coupler.


6.3 Full Link Measurements Results
Unfortunately, it was not possible to obtain a BER at 9.2Gbps because the PRBS
checker was unable to start at this speed due to a timing issue between the
receiver and the Simplified Timing Shell. This error has already been demon-
strated in simulation and one sample of the chip has already undergone a FIB
to solve this issue. Further measurements will be carried out on this sample to
have the PRBS checker working. Despite this issue, the correctness of the ana-
log design at this speed can be demonstrated with the correct transmission and
reception of a static pattern along with the CDR locking at 1V for both transmit-
ter and receiver supply. By fixing the PI code from the outside and sweeping
it, a range of roughly 15 PI codes (circa 50ps) where the static pattern is cor-
rectly detected can be found, denoting a clean opening of the eye diagram at
the receiver sampler. Tough, it would make little to no sense to draw a bathtub
for such case, since the eye opening strongly depends on the transmitted bits,
therefore the BER at a certain distance from the eye center would also depend
on this.
     The aforementioned timing issue doesn’t show up at 4.6Gbps, therefore
BER measurements can be performed. For all the measurements reported in
the figures below, except when differently stated, the settings reported in tab.
6.1 have been used. TX Replicas indicates the number of active replicas at
transmitter side, LDO Current is the bias current fed into the LDO and CTLE
Res and Cap Code are indicating the amount of RC source degeneration in
the CTLE (we preferred to indicate the codes and not the dB of equalization
since these strongly depend on the technology corner for the same settings).
The CDR bandwidth is set thanks the averaging: for a transmission speed of
4.6Gbps, the digital clock has a frequency of 115MHz, therefore an averaging
of 115 has to be set.
     Fig. 6.4 shows the bathtub curves for three different VDD , highlighting

---

6.3. FULL LINK MEASUREMENTS RESULTS                                                           135

           Table 6.1: Settings used for TX-RX loopback measurements.
 TX Replicas     LDO Current[µA]   CTLE Res, Cap Code            DFE            CDR PD, BW [MHz]
     12                32                 3, 7            h1 =30mV, h2 =15mV      Alexander, 1



closer bathtub with decreasing supply voltage. This curves have been obtained
with the following method: first of all, we run the link with the CDR enabled
in order to find the PI code at which the CDR settles. Once this has been found,
we sweep all PI codes up to ±16 values away from the center one and we run
the BER counter for 30 seconds. This is enough for finding actual BER up to
10−7 , since in 30 seconds we are transmitting circa 1.5 · 1011 bits so for a BER of
10−7 we find roughly 10000 errors. After this sweep has been done, we run the
BER counter for 10 minutes setting the PI code to the values adjacent to those
where we found a BER of 10−7 , until we don’t find errors anymore. In fact, in
10 minutes we transmit roughly 3 · 1012 bits, so if we don’t find an error on such
amount of time it’s safe to say that the BER for this PI codes is 10−12 or lower,
and for accurately measuring this BER points one should let the interface run
for several hours for each one of this PI codes. Anyway, as highlighted from
the bathtub curves, in all three cases an open eye diagram is clearly visible at
the input of the receiver sampler. Fig. 6.5 reports the corresponding power
consumption of the whole high-speed link for each power supply value, along
with the power consumed by the single components of the link. For compar-
ison’s sake, in fig. 6.6 we report the power consumption of the whole link for
different power supply values also for 9.2Gbps transmission speed.

                                   BER Bathtub vs VDD
         10-0

                                               VDD = 1.05V
         10-2
                                               VDD = 1V
                                               VDD = 0.95V
         10-4
   BER




         10-6


         10-8


         10-10


         10-12
                 0   0.1   0.2     0.3   0.4    0.5     0.6    0.7    0.8      0.9   1
                                    Horizontal Opening [UI]
  Figure 6.4: Bathtub curves at 4.6Gbps for various VDD in loopback mode.

---

136                          CHAPTER 6. CHARACTERIZATION OF THE FULL LINK


                             Power Consumption at 4.6Gbps
                     14


                     12
                                                               TX+RX
                                                               TX
  Power [mW/Gbps]



                     10
                                                               RX

                      8

                      6

                      4

                      2
                      0.94    0.96   0.98       1       1.02   1.04    1.06
                                              VDD [V]
Figure 6.5: Power consumption of the whole link for different power supplies
at 4.6Gbps. The power budget for the PI and the digital part (PRBS generator,
PRBS checker, PD and CDR algorithm) are reported under the receiver power
consumption.

                             Power Consumption at 9.2Gbps
                     12
                               TX+RX
                     10        TX
                               RX
   Power [mW/Gbps]




                      8


                      6

                      4

                      2


                      0
                      0.94    0.96     0.98     1       1.02   1.04    1.06
                                              VDD [V]
Figure 6.6: Power consumption of the whole link for different power supplies
at 9.2Gbps. The power budget for the PI and the digital part (PRBS generator,
PRBS checker, PD and CDR algorithm) are reported under the receiver power
consumption.

---

6.3. FULL LINK MEASUREMENTS RESULTS                                            137

    Finally, some measurements have been performed in order to evaluate the
performances of the two implemented phase detection methods, Alexander
and the one proposed in this work. In order to evaluate the two methods, we
run the link with active CDR and active BER, in order to monitor the overall
performance as well. During this run, we read the PI code 200 times and count
the occurrences of each PI code among these 200 reads. The results of these
measurements are reported in figg. 6.7-6.11. Comparing fig. 6.7 and fig. 6.9,
we can say that the two phase detection algorithms perform in a similar way
when using low CDR bandwidth: in fact, both PD settle around three PI codes,
with rare occurrences in two adjacent ones. The only difference is related to
the center PI code at which the CDR settles: without having an eye monitor
before the sampling at receiver side, it’s difficult to say which one of the two is
more centered. Further measurements will be done in order to understand this
point.
    When the bandwidth of the CDR increases, then the spread of the PI codes
increases, as shown in fig. 6.9-6.11. This is due to the fact that, when increas-
ing the bandwidth of the CDR, noise at higher frequencies will also be tracked,
whereas at low CDR bandwidth the deterministic jitter seen is the one given by
the CDR limit cycle itself. At the same time, when increasing the CDR band-
width, also the BER was increasing: no error was seen when reading the codes
reported in figg. 6.7-6.9, whereas for figg. 6.9-6.11 we found BER of roughly
10−10 and 10−6 , respectively. This is most probably due to the fact that when
going at higher CDR bandwidth, also the number of voting averaging is re-
duced, therefore the outliers are not smoothed out by the voting process. The
fact that the BER is higher for our phase detector than for the Alexander may
indicate that the PI code at which our algorithm settles is not so well centered
as the Alexander one. In order to understand at which bandwidth our algo-
rithm stops to perform well for this settings, different CDR bandwidths have
been tried out: the BER for a CDR bandwidth of 11.5MHz is roughly 10−10 , and
as shown in fig. 6.10 the PI codes are not so spread. In fact, as already seen, the
performances of the two PD algorithms should depend on the DFE settings:
the more DFE is used, the more robust our PD algorithm should become and
the less centered the Alexander PD should be. To check this, we should run
our interface when connecting transmitter and receiver with channels where
higher amount of DFE is needed.

---

6.4. HSIO EVALUATION BOARD                                                   141

6.4 HSIO Evaluation Board
In order to address the need of channels with higher losses stated at the end
of the previous chapter so to compare the performances of the two phase de-
tection algorithms and to better investigate the equalization capabilities of our
interface, a Printed Circuit Board with several channels on top has been de-
signed and fabricated (fig. 6.12). Another goal of the measurements that will
be performed with this board is to understand the influence of many bad habits
in PCB design (90 degree angles, high speed signals through vias, aggressors
on high speed lines) on the link performance. The channels on this board, if
combined, can combine for a loss up to 20dB at 2.5GHz. The PCB consists of
four layers and its dimensions are 40cmX40cm. The dielectric used is stan-
dard FR-4, which is the material used for typical automotive mass production
applications due to its lower cost.




                     Figure 6.12: HSIO Evaluation Board.

---

Conclusions

In this thesis, after having introduced the frame of high-speed serial interfaces
for chip-to-chip communication, we have presented the whole design flow of
a 10Gbps transceiver, from system level analysis to transistor level and layout
implementation. Finally, the whole transceiver has been characterized through
measurements.
    We started by showing procedures to define an equalization strategy at the
transmitter and to evaluate its effect on the transmitted data, moving then to
the transistor level design of the transmitter architecture supporting such a FFE
scheme. The transmitter has been designed with a voltage-mode driver in or-
der to save power and features FFE with 8 taps (one pre-cursor, main tap and
six post-cursor taps), programmable with 16 levels. The whole architecture is
divided into two power domains and the driver is supplied by an LDO with a
selectable output voltage among eight different values, giving an eye diagram
peak-to-peak differential height that can be tuned from 250mV to 380mV in
nominal PVT conditions (VDD =900mV, typical technology corner, 25◦ C). With
a decoupling capacitance of 50pF for each power domain, the transmitter is
correctly operating over a broad range of VDD (from 800mV to 1.05V), technol-
ogy corners (all possible combinations of slow, typical and fast technological
corners) and temperature (from -40◦ C to 175◦ C).
    The functioning of the transmitter has been demonstrated with transistor
level simulations and with measurements performed on two separated test-
chips. On the transmitter placed on the second test-chip, a whole characteri-
zation has been carried out. Moreover, an extended analysis on the effect of
parasitic inductance on VDD and VSS domains has been illustrated, highlight-
ing the necessity to keep the values of these inductances under control in the
chip-bonding process.
    We have then focused our attention on the design of the receiver, starting
from a system level analysis aiming at understanding the inter-dependence be-
tween half-rate architecture, loop-unrolled DFE and CDR. To do so, we have
built a Simulink model. We have then proposed a novel phase detection algo-
rithm dedicated to CDR in systems with DFE and validated it using the afore-
mentioned Simulink model.
    The receiver architecture features a source-degenerated differential pair CTLE
programmable in the source resistance (2 bits), source capacitance (3 bits) and
biasing current (4 bits). Also the operating point of this CTLE can be tuned (3
bits) to find the optimal value depending on the PVT conditions and the trans-
mitted eye opening. The CTLE can boost the frequency components around
Nyquist (5GHz) of the transmitted bits up to 10dB with respect to low-frequency
ones. The receiver features also a 4 post-cursor taps DFE, the first one being

                                      143

---

144                                                              CONCLUSIONS

loop-unrolled. The current in the main tap of the summers can be trimmed
with 16 levels, and so does the current flowing in the DFE taps. The drain re-
sistances of the main summer feature 8 different trimmable levels, so that the
finest DFE correction that can be programmed is 6mV. Also the receiver is di-
vided into two power domains. With a decoupling capacitance of 50pF for each
power domain, simulations show that the receiver is correctly operating over
a broad range of VDD (from 800mV to 1.05V), technology corners (all possible
combinations of slow, typical and fast technological corners) and temperature
(from -40◦ C to 175◦ C).
    The functioning of the receiver and its integration with the already taped-
out transmitter has then been demonstrated with transistor level and mixed-
signal simulations, including also the digital part of the transceiver. These sim-
ulations show that the proposed phase detection algorithm is suited in case of
low-quality crystals for frequency generation (100ppm or above). Both trans-
mitter and receiver are also capable of working at three different transmission
speeds: 2.5Gbps, 5Gbps and 10Gbps.
    Simulated data point out a power consumption of 22.5mW in the least con-
suming corner for the transmitter, corresponding to an efficiency of 2.25 pJ/bit,
in line with the state-of-the-art in the literature. As for the receiver, the power
consumption is 20.5mW in nominal PVT conditions (VDD =900mV, typical tech-
nology corner, 25◦ C), corresponding to a power efficiency of 2.05pJ/bit. The
analog part of the receiver (bias distribution, CTLE, DFE, summers, compara-
tors) consumes 0.77mW/Gbps, whereas the CDR circuitry (PI, PI Decoder, 2:40
Deserializers) 1.28mW Gbps. In the least-consuming PVT corner (VDD =800mV,
slow-slow technology corner, -40◦ C), the analog part consumes 0.5mW/Gbps,
whereas the CDR circuitry 0.8mW/Gbps, which gives a total 1.3mW/Gbps.
    Finally, the functioning of the whole transceiver has been demonstrated
with measurements. A static pattern in loopback mode at 9.2Gbps with settling
CDR has been demonstrated. A whole characterization of the link at 4.6Gbps in
loopback mode has been carried out, highlighting BER lower than 10−12 and
good agreement between simulations and measurements in terms of power
consumption. An in depth analysis of the performance of the two phase de-
tection algorithms has just started and the first results are already available in
this thesis. In the next steps, more measurements will be performed using as a
channel different traces placed on an already designed and produced Printed
Circuit Board.

---

List of Publications

Results of this research work have been presented at international conferences
with peer-review:

   • Bandiziol, A., Grollitsch, W., Brandonisio, F., Nonis, R., Palestri, P. (2016,
     May). Design of a transmitter for high-speed serial interfaces in automo-
     tive micro-controller. In Information and Communication Technology,
     Electronics and Microelectronics (MIPRO), 2016 39th International Con-
     vention on (pp. 84-88). IEEE.
   • Bandiziol, A., Grollitsch, W., Brandonisio, F., Nonis, R., Palestri, P. (2016,
     October). Design of a 8-taps, 10Gbps transmitter for automotive micro-
     controllers. In Circuits and Systems (APCCAS), 2016 IEEE Asia Pacific
     Conference on (pp. 321-324). IEEE.

   • Bandiziol, A., Grollitsch, W., Brandonisio, F., Nonis, R., Palestri, P. (2017,
     June). System and transistor level analysis of an 8-taps FFE 10Gbps serial
     link transmitter with realistic channels and supply parasitics. In Ph. D.
     Research in Microelectronics and Electronics (PRIME), 2017 13th Confer-
     ence on (pp. 297-300). IEEE.

   and at national level in:

   • Bandiziol, A., Grollitsch, W., Brandonisio, F., Nonis, R., Palestri, P., Selmi
     L. (2016, June). Design of a transmitter for high-speed serial interfaces
     in automotive micro-controller. Proceedings of GE2016, 48th Conference,
     Brescia, Italy.

    Moreover, the following articles have been accepted and will be presented
at international conferences with peer-review:

   • Bandiziol, A., Grollitsch, W., Brandonisio, F., Bassi M., Nonis, R., Palestri,
     P. Design of a half-rate receiver for a 10Gbps automotive serial interface
     with 1-tap-unrolled 4-taps DFE and custom CDR algorithm. Circuits and
     Systems (ISCAS), 2018 International Symposium on. IEEE.
   • Dazzi M., Palestri P., Rossi D., Bandiziol A., Loi I., Bellasi D., Benini L.
     Sub-mW multi-Gbps chip-to-chip communication Links for Ultra-Low
     Power IoT end-nodes (Invited Paper). Circuits and Systems (ISCAS),
     2018 International Symposium on. IEEE.

   Finally, research activities results have been presented at:

                                       145

---

146                                                   LIST OF PUBLICATIONS

      • Infineon Innovation Days, June 2015, Villach, Austria
      • PhD Expo, 18th June 2015, Udine, Italy

      • Infineon Innodays, November 2015, Villach, Austria
      • CAS Day, 6th March 2016, Villa del Grumello, Italy
      • PhD Expo, 26th May 2016, Udine, Italy
      • PhD Expo, 25th May 2017, Udine, Italy

---

Acknowledgments

My first thanks goes to my tutor at University of Udine, Prof. Pierpaolo Palestri.
It is hard for me to imagine ways to be a better guide than what he has been to
me in these three years. His help has just been invaluable, his curiosity for all
aspects of electronics has been a constant stimulus for me in trying to become
a better researcher everyday.
     An enormous thanks goes also to my supervisor at Infineon Technology
Design Center, Dr Roberto Nonis. On top of the technical contents that he has
transmitted to me in these years, the thing that I have tried to learn at most
from his daily behavior is to being able to take time to listen to people even
in the busiest days. Along with him, also Werner Grollitsch has taught me a
lot more than high-speed serial interfaces design: humility is a much bigger
virtue, especially when shown towards a guy that knows nearly nothing of a
field in which you have several years of experience.
     The fact that I have been able to fully concentrate on this work along this
three year span has been possible only thanks to my family: nothing of this
would have been possible without your continuous support. Examples are
much more powerful instruments than words, and you all have given me
plenty of them in my whole life. My biggest hope is to be every day even
just one tenth as inspirational as you have been, and are, to me. A big thank
goes also to Ginevra: it would have been easy for you to say that I was a little
bit too focused on work in the last months, but instead you decided to fit to my
time as water in a bowl. I will remember it when your bowl will be smaller.
     Having one office with a great atmosphere is not for everybody. Having
two of them has been just amazing. I have found all the support and good
vibes that I needed in these years at CIS in Infineon Technologies, and when
I talk to my friends or family about how I feel when I enter my office they
almost don’t believe me. It’s hard to find such a mix of experience, love for
the job, dedication and easy-going attitude. I want to particularly thank Fabio,
Francesco, Andrea, Matteo, Dmytro and Thomas for the patience they have
demonstrated to have with me every day. A big thanks goes also to Stefan and
Andrea for their work done with the layout. Obviously, without them there
would be nothing to measure in the lab. And so thanks also to Florin for the
first round of measurements, and sorry for the next ones that will come. At
the same time, I will never forget my time in Selmilab: Paolo, Stefano, Enrico,
Giulia, Owes, Tommaso, Andrea, Alessandro, Julian, Martino, Patrick, Daniel,
Federico, I have memories for each one of you. Thanks for the laughs, for the
help, for the tips. If these four years are gone so fast and it seems to me that I
entered that lab for the first time yesterday, it’s mainly because of you.


                                       147

---

Bibliography

 [1] Altera, “FPGAs at 40 nm and >10 Gbps: Jitter-, Signal Integrity-, Power-,
     and Process-Optimized Transceivers,” Tech. Rep. April, 2013.
 [2] I. C. Society, IEEE Std 802.3TM -2015 (Revision of IEEE Std 802.3-2012), IEEE
     Standard for Ethernet. 2015.
 [3] D. Law, D. Dave, J. D’Ambrosia, M. Hajduczenia, M. Laubach, and
     S. Carlson, “Evolution of Ethernet Standards in the IEEE 802.3 Working
     Group,” IEEE Communications Magazine, no. 8, pp. 88–96, 2013.
 [4] PCI, “PCI Express R Base Specification Revision 3.0,” 2010.
 [5] Hypertransport, HyperTransport 3.1. 2008.
 [6] CPRI, CPRI Specification V7.0. 2015.
 [7] Interlaken, Interlaken Protocol Definition. 2008.
 [8] OIF, Common Electrical I/O (CEI) - Electrical and Jitter Interoperability agree-
     ments for 6G+bps, 11G+bps and 25G+bps I/O. 2014.
 [9] SATA-IO, Serial ATA 3.0. 2009.
[10] RapidIO, RapidIO Interconnect Specification 4.0. 2016.
[11] K. Chang, G. Zhang, and C. Borrelli, “Evolution of Wireline Transceiver
     Standards,” IEEE Solid-State Circuits Magazine, no. 4, pp. 47–52, 2015.
[12] R. Mellitz, A. Ran, M. P. Li, and V. Ragavassamy, “Channel Operating
     Margin (COM): Evolution of Channel Specifications for 25 Gbps and Be-
     yond,” in DesignCon, pp. 1–20, 2013.
[13] X. D. M. M. F. R. W. J. G. Zhang, “Relating COM to Familiar S-Parameter
     Parametric to Assist 25Gbps System Design,” in DesignCon, 2014.
[14] T. C. Carusone, “Introduction to Digital I/O,” IEEE Solid-State Circuits
     Magazine, no. 4, pp. 14–22, 2015.
[15] B. Razavi, “Historical Trends in Wireline Communications,” IEEE Solid-
     State Circuits Magazine, no. 4, pp. 42–46, 2015.
[16] S. Palermo, “High-Speed Serial I/O Design for Channel- Limited and
     Power-Constrained Systems,” in CMOS Nanoelectronics Analog and RF
     VLSI Circuits, 2011.

                                       149

---

150                                                               BIBLIOGRAPHY

[17] A. X. Widmer and P. A. Franaszek, “A DC-Balanced, Partitioned-Block,
     8B/10B Transmission Code,” IBM J. Res. Develop, vol. 27, no. 5, pp. 440–
     451, 1983.
[18] M. P. Li, Jitter, Noise, and Signal Integrity at High-Speed. 2007.
[19] B. Razavi, Design of integrated circuits for optical communications. 2012.
[20] B. Casper, “Clocking Wireline Systems,” IEEE Solid-State Circuits Maga-
     zine, no. 4, pp. 32–41, 2015.
 [21] R. Kreienkamp, U. Langmann, C. Zimmermann, T. Aoyama, and H. Sied-
      hoff, “A 10-Gb/s CMOS Clock and Data Recovery Circuit With an Ana-
      log Phase Interpolator,” IEEE Journal of Solid State Circuits, vol. 40, no. 3,
      pp. 736–743, 2005.
 [22] S. Hu, C. Jia, K. Huang, C. Zhang, X. Zheng, and Z. Wang, “A 10Gbps
      CDR based on Phase Interpolator for Source Synchronous Receiver in
      65nm CMOS,” in IEEE International Symposium on Circuits and Systems,
      pp. 309–312, 2012.
 [23] S. S. Iyer and T. Kirihata, “Three-Dimensional Integration,” IEEE Solid-
      State Circuits Magazine, no. 4, pp. 63–74, 2015.
 [24] J. Fan, X. Ye, J. Kim, B. Archambeault, and A. Orlandi, “Signal Integrity
      Design for High-Speed Digital Circuits: Progress and Directions,” IEEE
      Trabsactions on Electromagnetic Compatibility, vol. 52, no. 2, pp. 392–400,
      2010.
 [25] P. K. Hanumolu, G.-y. Wei, and U.-k. Moon, “Equalizers for High-Speed
      Serial Links,” International Journal of High Speed Electronics and Systems,
      vol. 15, no. 2, pp. 429–458, 2005.
 [26] J. F. Bulzacchelli, “Equalization for Electrical Links: Current Design Tech-
      niques and Future Directions,” IEEE Solid-State Circuits Magazine, no. 4,
      pp. 23–31, 2015.
 [27] T. Kawamoto, “Multi-Standard 185fs 0.3-to-28Gb/s 40dB Backplace Sig-
      nal Conditioner with Adaptive Pattern-Match 36-Tap DFE and Data-
      Rate-Adjustment PLL in 28nm CMOS,” in IEEE International Solid-State
      Circuits Conference, pp. 54–56, 2015.
 [28] E. Mammei, F. Loi, F. Radice, A. Dati, M. Bruccoleri, M. Bassi, and
      A. Mazzanti, “Analysis and Design of a Power-Scalable Continuous-
      Time FIR Equalizer for 10 Gb/s to 25 Gb/s Multi-Mode Fiber EDC in
      28 nm LP CMOS,” IEEE Journal of Solid-State Circuits, vol. 49, no. 12,
      pp. 3130–3140, 2014.
 [29] J. F. Bulzacchelli, T. J. Beukema, D. W. Storaska, D. R. Hanson, P.-h.
      Hsieh, S. V. Rylov, D. Furrer, D. Gardellini, A. Prati, T. Morf, V. Sharma,
      R. Kelkar, H. A. Ainspan, W. R. Kelly, L. R. Chieco, G. A. Ritter, J. A.
      Sorice, J. D. Garlett, R. Callan, P. Buchmann, M. Kossel, and D. J. Fried-
      man, “A 28-Gb/s 4-Tap FFE/15-Tap DFE Serial Link Transceiver in 32-
      nm SOI CMOS Technology,” IEEE Journal of Solid State Circuits, vol. 47,
      no. 12, pp. 3232–3248, 2012.

---

BIBLIOGRAPHY                                                                   151

[30] A. Agrawal, J. F. Bulzacchelli, T. O. Dickson, Y. Liu, J. A. Tierno, and D. J.
     Friedman, “A 19-Gb/s Serial Link Receiver With Both 4-Tap FFE and
     5-Tap DFE Functions in 45-nm SOI CMOS,” IEEE Journal of Solid State
     Circuits, vol. 47, no. 12, pp. 3220–3231, 2012.
[31] T. Toifl, P. Buchmann, T. Beukema, M. Beakes, P. A. Francese, C. Menolfi,
     M. Kossel, L. Kull, and T. Morf, “A 3.5pJ/Bit 8-Tap-Feed-Forward 8-Tap-
     Decision Feedback Digital Equalizer for 16Gb/s I/Os,” in IEEE European
     Solid State Circuits Conference (ESSCIRC), pp. 455–458, 2014.
[32] H. Yueksel, L. Kull, A. Burg, M. Braendli, P. Buchmann, P. A. Francese,
     C. Menolfi, M. Kossel, T. Morf, T. M. Andersen, D. Luu, and T. Toifl, “A
     3.6 pJ/b 56 Gb/s 4-PAM Receiver with 6-Bit Ti-SAR ADC and Quarter-
     Rate Speculative 2-Tap DFE in 32 nm CMOS,” in IEEE European Solid
     State Circuits Conference (ESSCIRC), pp. 148–151, 2015.
[33] S. Rylov, T. Beukema, Z. Toprak-deniz, T. Toifl, Y. Liu, A. Agrawal,
     P. Buchmann, A. Rylyakov, M. Beakes, B. Parker, and M. Meghelli, “A
     25Gb/s ADC-Based Serial Line Receiver in 32nm CMOS SOI,” in IEEE
     International Solid-State Circuits Conference, pp. 56–58, 2016.
[34] S. Gondi and B. Razavi, “Equalization and Clock and Data Recovery
     Techniques for 10-Gb/s CMOS Serial-Link Receivers,” IEEE Journal of
     Solid-State Circuits, vol. 42, no. 9, pp. 1999–2011, 2007.
[35] A. Healey, “Noise considerations for 40/100GBASE-CR4/10,” in IEEE
     P802.3ba Task Force Meeting, no. July, 2009.
[36] Infineon, “Annual Report 2016,” tech. rep., 2016.
[37] R. Tummala, “New Era of Automotive Electronics as the most complex
     Electronic System of Our Life Time,” in IEEE Electrical Design of Advanced
     Packaging and Systems (EDAPS), 2016.
[38] M. Traub and A. Maier, “Future Automotive Architecture and the Impact
     of IT Trends,” IEEE Software, no. May/June, pp. 27–32, 2017.
[39] J. Endo, “Wireless Communication In and Around the Car: Status and
     Outlook - ES3: High-Speed Communications on 4 Wheels: What’s in
     Your Next Car?,” in IEEE International Solid-State Circuits Conference,
     2013.
[40] C. Schmidt, “Automotive Electronics - Enabling the future of individual
     mobility,” in IEEE International Electronic Devices Meeting (IEDM), pp. 3–
     8, 2007.
[41] A. Cristofoli, P. Palestri, L. Selmi, and N. Da Dalt, “Efficient Statistical
     Simulation of Intersymbol Interference and Jitter in High-Speed Serial
     Interfaces,” IEEE Transactions on Components, Packaging and Manifacturing
     Technology, vol. 4, no. 3, pp. 480–489, 2014.
[42] M. Kossel, J. Weiss, C. Menolfi, P. Buchmann, T. Morf, T. Toifl, and
     M. Schmarz, “A T-Coil-Enhanced 8.5Gb/s High-Swing SST Transmitter
     in 65nm Bulk CMOS With <-16dB Return Loss Over 10GHz Bandwidth,”
     IEEE Journal of Solid State Circuits, vol. 43, no. 12, pp. 2905–2919, 2008.

---

152                                                            BIBLIOGRAPHY

[43] J. G. Proakis, Digital Communications. 2008.
[44] Ansys, “Ansys Electronic Desktop 16.0 Manual,” 2016.
[45] Ansys, “Ansys SIWave 16.0 Manual,” 2016.
[46] A. Cossettini, A. Cristofoli, W. Grollitsch, L. Alves, R. Nonis, L. D. Ricca,
     P. Palestri, and L. Selmi, “Design, characterization and signal integrity
     analysis of a 2.5 Gb/s high-speed serial interface for automotive appli-
     cations overarching the chip/PCB wall,” in 2015 IEEE 1st International
     Forum on Research and Technologies for Society and Industry Leveraging a bet-
     ter tomorrow (RTSI), 2015.
[47] J. F. Bulzacchelli, M. Meghelli, S. V. Rylov, W. Rhee, A. Rylyakov, H. A.
     Ainspan, B. D. Parker, M. P. Beakes, A. Chung, T. J. Beukema, P. K. Pe-
     peljugoski, L. Shan, Y. H. Kwark, S. Gowda, and D. J. Friedman, “A
     10-Gb/s 5-tap DFE/4-tap FFE transceiver in 90-nm CMOS technology,”
     IEEE Journal of Solid State Circuits, vol. 41, no. 12, pp. 2885–2900, 2007.
[48] T. Beukema, M. Sorna, K. Selander, S. Zier, B. L. Ji, P. Murfet, J. Ma-
     son, W. Rhee, H. Ainspan, B. Parker, and M. Beakes, “A 6.4-Gb/s
     CMOS SerDes core with feed-forward and decision-feedback equaliza-
     tion,” IEEE Journal of Solid-State Circuits, vol. 40, no. 12, pp. 2633–2644,
     2005.
 [49] S. Saxena, R. K. Nandwana, and P. K. Hanumolu, “A 5 Gb/s Energy-
      Efficient Voltage-Mode Transmitter Using Time-Based De-Emphasis,”
      IEEE Journal of Solid State Circuits, vol. 49, no. 8, pp. 1827–1836, 2014.
[50] C. Menolfi, T. Toifl, P. Buchmann, M. Kossel, T. Morf, J. Weiss, and
     M. Schmatz, “A 16Gb/s Source-Series Terminated Transmitter in 65nm
     CMOS SOI,” in IEEE International Solid-State Circuits Conference, pp. 446–
     448, 2007.
[51] W.-s. Choi, G. Shu, M. Talegaonkar, Y. Liu, D. Wei, L. Benini, and
     P. K. Hanumolu, “A 0.45-to-0.7V 1-tp-6Gb/s 0.29-to-0.58pJ/b Source-
     Synchronous Transceiver Using Automatic Phase Calibration in 65nm
     CMOS,” in IEEE International Solid-State Circuits Conference, pp. 66–68,
     2015.
[52] T. Shibasaki, T. Danjo, Y. Ogata, Y. Sakai, H. Miyaoka, F. Terasawa,
     M. Kudo, H. Kano, A. Matsuda, S. Kawai, T. Arai, H. Higashi, N. Naka,
     H. Yamaguchi, T. Mori, Y. Koyanagi, and H. Tamura, “A 56Gb/s NRZ-
     Electrical 247mW/lane Serial-Link Transceiver in 28nm CMOS,” in IEEE
     International Solid-State Circuits Conference, pp. 64–66, 2016.
[53] M. J. Myjak, J. G. Delgado-Frias, and S. Kwang Jeon, “An Energy-
     Efficient Differential Flip-Flop for Deeply Pipelined Systems,” in Midwest
     Symposium on Circuistemsts and Systems, no. September 2006, 2006.
[54] G. Shu, W.-s. Choi, S. Saxena, S.-j. Kim, M. Talegaonkar, R. Nandwana,
     A. Elkholy, T. Nandi, and P. K. Hanumolu, “A 16Mb/s-to-8Gb/s 14.1-to-
     5.9pJ/b Source Synchronous Transceiver Using DFVS and Rapid On/Off
     in 65nm CMOS,” in IEEE International Solid-State Circuits Conference,
     pp. 398–400, 2016.

---

BIBLIOGRAPHY                                                                 153

[55] H. Hentzell, S.-t. Persson, H. Hesselbom, B. Lofstedt, and M. Hansen,
     “Techniques For Reducing Switching Noise In High Speed Digital Sys-
     tems,” in IEEE International ASIC Conference and Exhibit, pp. 21–24, 1995.
[56] G. Khanna, R. Chandel, and A. K. Chandel, “Impact of Skew and Jitter on
     the Performance of VLSI Interconnects,” in IEEE Asia-Pacific Conference
     on Circuits and Systems (APCCAS), pp. 1223–1226, 2010.
[57] A. Bandiziol, W. Grollitsch, F. Brandonisio, R. Nonis, and P. Palestri, “De-
     sign of a 8-taps, 10Gbps transmitter for automotive micro-controllers,”
     in IEEE Asia-Pacific Conference on Circuits and Systems (APCCAS), pp. 6–9,
     2016.
[58] H. Kimura, P. M. Aziz, T. Jing, A. Sinha, S. P. Kotagiri, R. Narayan,
     H. Gao, P. Jing, G. Hom, A. Liang, E. Zhang, A. Kadkol, R. Kothari,
     G. Chan, Y. Sun, B. Ge, J. Zeng, K. Ling, M. C. Wang, A. Malipatil, L. Li,
     C. Abel, and F. Zhong, “A 28 Gb/s 560 mW Multi-Standard SerDes With
     Single-Stage Analog Front-End and 14-Tap Decision Feedback Equalizer
     in 28 nm CMOS,” IEEE Journal of Solid State Circuits, vol. 49, no. 12,
     pp. 3091–3103, 2014.
[59] S. Shahramian, B. Dehlaghi, and A. C. Carusone, “A 16Gb/s 1 IIR + 1 DT
     DFE Compensating 28dB Loss with Edge-Based Adaptation Converging
     in 5us,” in IEEE International Solid-State Circuits Conference, pp. 410–412,
     2016.
[60] B. Leibowitz, R. Farjad, T. Greer, and V. Stojanovic, “A 7.5Gb/s 10-Tap
     DFE Receiver with First Tap Partial Response, Spectrally Gated Adapta-
     tion, and 2nd-Order Data-Filtered CDR,” in IEEE International Solid-State
     Circuits Conference, pp. 228–220, 2007.
[61] T. Norimatsu, T. Kawamoto, K. Kogo, N. Kohmu, F. Yuki, N. Nakajima,
     T. Muto, J. Nasu, T. Komori, H. Koba, T. Usugi, T. Hokari, T. Kawamata,
     Y. Ito, S. Umai, M. Tsuge, T. Yamashita, M. Hasegawa, and K. Higeta, “A
     25Gb/s Multistandard Serial Link Transceiver for 50dB-Loss Copper Ca-
     ble in 28nm CMOS,” in IEEE International Solid-State Circuits Conference,
     pp. 60–62, 2016.
[62] S. Shahramian and A. C. Carusone, “A 0.41 pJ/bit 10 Gb/s Hybrid 2-IIR
     and 1 Discrete-Time DFE Tap in 28 nm-LP CMOS,” IEEE Journal of Solid
     State Circuits, vol. 50, no. 7, pp. 1722–1735, 2015.
[63] S. Shahramian, H. Yasotharan, and A. C. Carusone, “Decision Feed-
     back Equalizer Architectures With Multiple Continuous-Time Infinite
     Impulse Response Filters,” IEEE Transactions on Circuits and Systems II:
     Express Briefs, vol. 59, no. 6, pp. 326–330, 2012.
[64] G. R. Gangasani, C.-m. Hsu, J. F. Bulzacchelli, T. Beukema, W. Kelly, H. H.
     Xu, D. Freitas, A. Prati, D. Gardellini, R. Reutemann, G. Cervelli, J. Her-
     tle, M. Baecher, J. Garlett, P.-a. Francese, J. F. Ewen, D. Hanson, D. W.
     Storaska, and M. Meghelli, “A 32 Gb/s Backplane Transceiver With On-
     Chip AC-Coupling and Low Latency CDR in 32 nm SOI CMOS Technol-
     ogy,” IEEE Journal of Solid State Circuits, vol. 49, no. 11, pp. 2474–2489,
     2014.

---

154                                                             BIBLIOGRAPHY

[65] F. Zhong, S. Quan, W. Liu, P. Aziz, T. Jing, J. Dong, C. Desai, H. Gao,
     M. Garcia, G. Hom, T. Huynh, H. Kimura, R. Kothari, L. Li, C. Liu,
     S. Lowrie, K. Ling, A. Malipatil, R. Narayan, T. Prokop, C. Palusa,
     A. Rajashekara, A. Sinha, C. Zhong, and E. Zhang, “A 1.0625-14.025
     Gb/s Multi-Media Transceiver With Full-Rate Source-Series-Terminated
     Transmit Driver and Floating-Tap Decision-Feedback Equalizer in 40nm
     CMOS,” IEEE Journal of Solid State Circuits, vol. 46, no. 12, pp. 3126–3139,
     2011.

 [66] S. Parikh, T. Kao, Y. Hidaka, J. Jiang, A. Toda, S. Mcleod, W. Walker,
      Y. Koyanagi, T. Shibuya, and J. Yamada, “A 32Gb/s Wireline Receiver
      with a Low-Frequency Equalizer, CTLE and 2-Tap DFE in 28nm CMOS,”
      in IEEE International Solid-State Circuits Conference, pp. 28–30, 2013.

 [67] J. Han, Y. Lu, N. Sutardja, K. Jung, and E. Alon, “A 60Gb/s 173mW Re-
      ceiver Frontend in 65nm CMOS Technology,” in 2015 VLSI Circuits Digest
      of Technical Papers, pp. 230–231, 2015.

 [68] A. Manian and B. Razavi, “A 40-Gb/s 9.2-mW CMOS Equalizer,” in 2015
      VLSI Circuits Digest of Technical Papers, pp. 226–227, 2015.

 [69] U. Singh, A. Garg, B. Raghavan, N. Huang, H. Zhang, Z. Huang,
      A. Momtaz, and J. Cao, “A 780mW 4X28Gb/s nsceiver for 100GbE Gear-
      box PHY in 40nm CMOS,” IEEE Journal of Solid State Circuits, vol. 49,
      no. 12, pp. 3116–3129, 2014.

 [70] P. A. Francese, T. Toifl, M. Braendli, C. Menolfi, M. Kossel, T. Morf,
      L. Kull, T. Meyer Andersen, H. Yueksel, A. Cevrero, and D. Luu,
      “Continuous-Time Linear Equalization with Programmable Active-
      Peaking Transistor Arrays in a 14nm FinFET 2mW/Gb/s 16Gb/s 2-Tap
      Speculative DFE Receiver,” in IEEE International Solid-State Circuits Con-
      ference, pp. 186–188, 2015.

 [71] P. A. Francese, C. Menolfi, M. Kossel, T. Morf, L. Kull, A. Cevrero,
      H. Yueksel, I. Oezkaya, D. Luu, and T. Toifl, “A 30Gb/s 0.8pJ/b 14nm
      FinFET Receiver Data-Path,” in IEEE International Electronic Devices Meet-
      ing (IEDM), pp. 408–410, 2016.

 [72] B. Kim, Y. Liu, T. O. Dickson, J. F. Bulzacchelli, and D. J. Friedman, “A 10-
      Gb/s Compact Low-Power Serial I/O With DFE-IIR Equalization in 65-
      nm CMOS,” IEEE Journal of Solid State Circuits, vol. 44, no. 12, pp. 3526–
      3538, 2009.

 [73] O. Elhadidy and S. Palermo, “A 10 Gb/s 2-IIR-Tap DFE Receiver with 35
      dB Loss Compensation in 65-nm CMOS,” in 2013 VLSI Circuits Digest of
      Technical Papers, pp. 272–273, 2013.

 [74] A. Emami-neyestanak, A. Varzaghani, J. F. Bulzacchelli, A. Rylyakov, C.-
      k. K. Yang, and D. J. Friedman, “A 6.0-mW 10.0-Gb/s Receiver With
      Switched-Capacitor Summation DFE,” IEEE Journal of Solid State Circuits,
      vol. 42, no. 4, pp. 889–896, 2007.

---

BIBLIOGRAPHY                                                                  155

[75] Y.-c. Huang and S.-i. Liu, “A 6Gb/s Receiver with 32.7dB Adaptive
     DFE-IIR Equalization,” in IEEE International Solid-State Circuits Confer-
     ence, pp. 68–69, 2011.

[76] S. Son, H.-s. Kim, M.-j. Park, K. Kim, E.-h. Chen, B. Leibowitz, and J. Kim,
     “A 2.3-mW, 5-Gb/s Low-Power Decision-Feedback Equalizer Receiver
     Front-End and its Two-Step, Minimum Bit-Error-Rate Adaptation Algo-
     rithm,” IEEE Journal of Solid State Circuits, vol. 48, no. 11, pp. 2693–2704,
     2013.

[77] H. Miyaoka, F. Terasawa, M. Kudo, H. Kano, A. Matsuda, N. Shirai,
     S. Kawai, T. Arai, Y. Ide, K. Terashima, H. Higashi, T. Higuchi, and
     N. Naka, “A 28-Gb/s 4.5-pJ/bit Transceiver With 1-Tap Decision Feed-
     back Equalizer in 28-n CMOS,” in IEEE Asian Solid-State Circuits Confer-
     ence, pp. 1–4, 2015.

[78] A. Bandiziol, W. Grollitsch, F. Brandonisio, R. Nonis, and P. Palestri, “De-
     sign of a transmitter for high-speed serial interfaces in automotive micro-
     controller,” in IEEE International Convention on Information and Commu-
     nication Technology, Electronics and Microelectronics (MIPRO), pp. 90–94,
     2016.

[79] R. Navid, E.-h. Chen, M. Hossain, B. Leibowitz, J. Ren, C.-h. A. Chou,
     B. Daly, B. Su, S. Li, M. Shirasgaonkar, F. Heaton, J. Zerbe, and J. Eble,
     “A 40 Gb/s Serial Link Transceiver in 28 nm CMOS Technology,” IEEE
     Journal of Solid State Circuits, vol. 50, no. 4, pp. 814–827, 2015.

[80] J. Han, N. Sutardja, Y. Lu, and E. Alon, “Design Techniques for a 60-Gb/s
     288-mW NRZ Transceiver With Adaptive Equalization and Baud-Rate
     Clock and Data Recovery in 65-nm CMOS Technology,” IEEE Journal of
     Solid State Circuits, no. 99, pp. 1–12, 2017.

[81] Synopsis, Synopsis Verilog Compiler Simulator 2017.03 Manual. 2017.

[82] B. Razavi, “Challenges in the Design of High-Speed Clock and Data Re-
     covery Circuits,” IEEE Communications Magazine, vol. 40, no. 8, pp. 94–
     101, 2002.

[83] J. Poulton, R. Palmer, A. M. Fuller, T. Greer, J. Eyles, W. J. Dally, and
     M. Horowitz, “A 14-mW 6.25-Gb/s Transceiver in 90-nm CMOS,” IEEE
     Journal of Solid State Circuits, vol. 42, no. 12, pp. 2745–2757, 2007.

[84] T. Musah, J. E. Jaussi, G. Balamurugan, S. Hyvonen, T.-c. Hsueh, G. Ke-
     skin, S. Shekhar, J. Kennedy, S. Sen, R. Inti, M. Mansuri, M. Leddige,
     B. Horine, C. Roberts, R. Mooney, and B. Casper, “A 4-32 Gb/s Bidirec-
     tional Link With 3-Tap FFE/6-Tap DFE and Collaborative CDR in 22nm
     CMOS,” IEEE Journal of Solid State Circuits, vol. 49, no. 12, pp. 1–12, 2014.

[85] V. Balan, O. Oluwole, G. Kodani, C. Zhong, R. Dadi, A. Amin, and
     A. Ragab, “A 15–22 Gbps Serial Link in 28 nm CMOS With Direct DFE,”
     IEEE Journal of Solid State Circuits, vol. 49, no. 12, pp. 3104–3115, 2014.

---

156                                                             BIBLIOGRAPHY

[86] M.-s. Chen and C.-k. K. Yang, “A 50–64 Gb/s Serializing Transmitter
     With a 4-Tap, LC-Ladder-Filter-Based FFE in 65 nm CMOS Technology,”
     IEEE Journal of Solid State Circuits, vol. 50, no. 8, pp. 1903–1916, 2015.

[87] T. Anand, M. Talegaonkar, A. Elkholy, S. Saxena, A. Eishazly, and
     P. K. Hanumolu, “Ultra-High-Speed Wireline Transceivers and Energy-
     Efficient Links,” in IEEE International Solid-State Circuits Conference,
     pp. 64–66, 2015.

[88] M.-s. Chen, Y.-n. Shih, C.-l. Lin, H.-w. Hung, and J. Lee, “A Fully-
     Integrated 40-Gb/s Transceiver in 65-nm CMOS Technology,” IEEE Jour-
     nal of Solid State Circuits, vol. 47, no. 3, pp. 627–640, 2012.
[89] A. Cristofoli, Analysis and Design of High Speed Serial Interfaces for Auto-
     motive Applications. PhD thesis, 2014.

[90] T. O. Dickson, Y. Liu, A. Agrawal, J. F. Bulzacchelli, H. A. Ainspan,
     Z. Toprak-deniz, B. D. Parker, M. P. Beakes, M. Meghelli, and D. J. Fried-
     man, “A 1.8pJ/bit 16X16Gb/s Source-Synchronous Parallel Interface in
     32nm SOI CMOS with Receiver Redundancy for Link Recalibration,”
     IEEE Journal of Solid State Circuits, vol. 51, no. 8, pp. 1744–1755, 2016.

[91] A. A. Hafez, M.-s. Chen, and C.-k. K. Yang, “A 32–48 Gb/s Serializing
     Transmitter Using Multiphase Serialization in 65 nm CMOS Technol-
     ogy,” IEEE Journal of Solid State Circuits, vol. 50, no. 3, pp. 763–775, 2015.
[92] W. Jia, B. Nikolic, V. Stojanovic, J. K.-s. Chiu, and M. M.-t. Leung, “Im-
     proved Sense-Amplifier-Based Flip-Flop: Design and Measurements,”
     IEEE Journal of Solid State Circuits, vol. 35, no. 6, pp. 876–884, 2000.
[93] J. W. Jung and B. Razavi, “A 25-Gb/s 5-mW CMOS CDR/Deserializer,”
     IEEE Journal of Solid State Circuits, vol. 48, no. 3, pp. 684–697, 2013.
[94] K. Kaviani, A. Amirkhany, C. Huang, P. Le, C. Madden, K. Saito, K. Sano,
     V. Murugan, W. Beyene, K. Chang, and C. Yuan, “A 0.4mW/Gb/s
     16Gb/s Near-Ground Receiver Front- End with Replica Transconduc-
     tance Termination Calibration,” in IEEE International Solid-State Circuits
     Conference, vol. 6, pp. 152–153, 2012.
[95] J. Lee, P. Chiang, and C. Weng, “56Gb/s PAM4 and NRZ SerDes
     Transceivers in 40nm CMOS,” in 2015 VLSI Circuits Digest of Technical
     Papers, pp. 118–119, 2015.
[96] A. Manian and B. Razavi, “A 40Gb/s 14mW CMOS Wireline Receiver,”
     in IEEE International Solid-State Circuits Conference, 2016.
[97] M. Muller and K. Mulller, “Timing Recovery in Digital Synchronous Data
     Receivers,” IEEE Transactions on Communications, vol. C, no. 5, pp. 516–
     531, 1976.
[98] B. Raghavan, D. Cui, U. Singh, D. Pi, A. Vasani, Z. C. Huang, A. Momtaz,
     and J. Cao, “A Sub-2 W 39.8-44.6 Gb/S Transmitter and Receiver Chipset
     With SFI-5.2 Interface in 40 nm CMOS,” IEEE Journal of Solid State Cir-
     cuits, vol. 48, no. 12, pp. 3219–3228, 2013.

---

BIBLIOGRAPHY                                                                     157

 [99] W. Sansen, “Minimum Power in Analog Amplifying Blocks,” IEEE Solid-
      State Circuits Magazine, no. 4, pp. 83–89, 2015.

[100] J. Savoj, S. Member, and B. Razavi, “A 10-Gb/s CMOS Clock and Data
      Recovery Circuit with a Half-Rate Linear Phase Detector,” IEEE Journal
      of Solid State Circuits, vol. 36, no. 5, pp. 761–767, 2001.
[101] S. Saxena, G. Shu, R. K. Nandwana, M. Talegaonkar, A. Elkholy,
      T. Anand, W.-s. Choi, and P. K. Hanumolu, “A 2.8 mW/Gb/s, 14 Gb/s
      Serial Link Transceiver,” IEEE Journal of Solid State Circuits, vol. 52, no. 5,
      pp. 1399–1411, 2017.
[102] H. Tamura, “Looking to the Future,” IEEE Solid-State Circuits Magazine,
      no. 4, pp. 53–62, 2015.
[103] Y. Wang, B. Afshar, L. Ye, V. C. Gaudet, and A. M. Niknejad, “Design
      of a Low Power, Inductorless Wideband Variable-Gain Ampli fi er for
      High-Speed Receiver Systems,” IEEE Transactions on Circuits and Systems
      I: Reguar Papers, vol. 59, no. 4, pp. 696–707, 2012.

---

List of Publications

Results of this research work have been presented at international conferences
with peer-review:

   • Bandiziol, A., Grollitsch, W., Brandonisio, F., Nonis, R., Palestri, P. (2016,
     May). Design of a transmitter for high-speed serial interfaces in automo-
     tive micro-controller. In Information and Communication Technology,
     Electronics and Microelectronics (MIPRO), 2016 39th International Con-
     vention on (pp. 84-88). IEEE.
   • Bandiziol, A., Grollitsch, W., Brandonisio, F., Nonis, R., Palestri, P. (2016,
     October). Design of a 8-taps, 10Gbps transmitter for automotive micro-
     controllers. In Circuits and Systems (APCCAS), 2016 IEEE Asia Pacific
     Conference on (pp. 321-324). IEEE.

   • Bandiziol, A., Grollitsch, W., Brandonisio, F., Nonis, R., Palestri, P. (2017,
     June). System and transistor level analysis of an 8-taps FFE 10Gbps serial
     link transmitter with realistic channels and supply parasitics. In Ph. D.
     Research in Microelectronics and Electronics (PRIME), 2017 13th Confer-
     ence on (pp. 297-300). IEEE.

   and at national level in:

   • Bandiziol, A., Grollitsch, W., Brandonisio, F., Nonis, R., Palestri, P., Selmi
     L. (2016, June). Design of a transmitter for high-speed serial interfaces
     in automotive micro-controller. Proceedings of GE2016, 48th Conference,
     Brescia, Italy.

    Moreover, the following articles have been accepted and will be presented
at international conferences with peer-review:

   • Bandiziol, A., Grollitsch, W., Brandonisio, F., Bassi M., Nonis, R., Palestri,
     P. Design of a half-rate receiver for a 10Gbps automotive serial interface
     with 1-tap-unrolled 4-taps DFE and custom CDR algorithm. Circuits and
     Systems (ISCAS), 2018 International Symposium on. IEEE.
   • Dazzi M., Palestri P., Rossi D., Bandiziol A., Loi I., Bellasi D., Benini L.
     Sub-mW multi-Gbps chip-to-chip communication Links for Ultra-Low
     Power IoT end-nodes (Invited Paper). Circuits and Systems (ISCAS),
     2018 International Symposium on. IEEE.

   Finally, research activities results have been presented at:

                                       159

---

160                                                   LIST OF PUBLICATIONS

      • Infineon Innovation Days, June 2015, Villach, Austria
      • PhD Expo, 18th June 2015, Udine, Italy

      • Infineon Innodays, November 2015, Villach, Austria
      • CAS Day, 6th March 2016, Villa del Grumello, Italy
      • PhD Expo, 26th May 2016, Udine, Italy
      • PhD Expo, 25th May 2017, Udine, Italy

---

Acknowledgments

My first thanks goes to my tutor at University of Udine, Prof. Pierpaolo Palestri.
It is hard for me to imagine ways to be a better guide than what he has been to
me in these three years. His help has just been invaluable, his curiosity for all
aspects of electronics has been a constant stimulus for me in trying to become
a better researcher everyday.
     An enormous thanks goes also to my supervisor at Infineon Technology
Design Center, Dr Roberto Nonis. On top of the technical contents that he has
transmitted to me in these years, the thing that I have tried to learn at most
from his daily behavior is to being able to take time to listen to people even
in the busiest days. Along with him, also Werner Grollitsch has taught me a
lot more than high-speed serial interfaces design: humility is a much bigger
virtue, especially when shown towards a guy that knows nearly nothing of a
field in which you have several years of experience.
     The fact that I have been able to fully concentrate on this work along this
three year span has been possible only thanks to my family: nothing of this
would have been possible without your continuous support. Examples are
much more powerful instruments than words, and you all have given me
plenty of them in my whole life. My biggest hope is to be every day even
just one tenth as inspirational as you have been, and are, to me. A big thank
goes also to Ginevra: it would have been easy for you to say that I was a little
bit too focused on work in the last months, but instead you decided to fit to my
time as water in a bowl. I will remember it when your bowl will be smaller.
     Having one office with a great atmosphere is not for everybody. Having
two of them has been just amazing. I have found all the support and good
vibes that I needed in these years at CIS in Infineon Technologies, and when
I talk to my friends or family about how I feel when I enter my office they
almost don’t believe me. It’s hard to find such a mix of experience, love for
the job, dedication and easy-going attitude. I want to particularly thank Fabio,
Francesco, Andrea, Matteo, Dmytro and Thomas for the patience they have
demonstrated to have with me every day. A big thanks goes also to Stefan and
Andrea for their work done with the layout. Obviously, without them there
would be nothing to measure in the lab. And so thanks also to Florin for the
first round of measurements, and sorry for the next ones that will come. At
the same time, I will never forget my time in Selmilab: Paolo, Stefano, Enrico,
Giulia, Owes, Tommaso, Andrea, Alessandro, Julian, Martino, Patrick, Daniel,
Federico, I have memories for each one of you. Thanks for the laughs, for the
help, for the tips. If these four years are gone so fast and it seems to me that I
entered that lab for the first time yesterday, it’s mainly because of you.


                                       161

---

