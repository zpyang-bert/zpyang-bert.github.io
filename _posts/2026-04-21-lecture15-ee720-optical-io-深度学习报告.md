---
layout: post
title:      "lecture15 ee720 optical io 深度学习报告"
date:       2026-04-21 10:47:52
author:     "Bert"
tags:
  - Fundamentals
  - Lecture
  - Optical
  - SerDes
  - 深度学习
---

ECEN720: High-Speed Links
   Circuits and Systems
       Spring 2023

    Lecture 15: Optical I/O




           Sam Palermo
   Analog & Mixed-Signal Center
       Texas A&M University

![](/img/serdes/fundamentals/lectures/lecture10_ee720_jitter_深度学习报告/_images/img-000.jpg)
> 🔍 深度说明：
> 【研究背景】本讲介绍光 I/O（Optical I/O）接口技术，探讨Serdes与光模块的接口设计，是数据中心和长距离通信中电光转换的核心技术。
> 【核心结论】光 I/O 系统架构：1) TX侧：Serdes输出 → 驱动器 → EAM（电吸收调制器）或 MZ（马赫-曾德）调制器 → 激光器 → 光纤；2) RX侧：PIN/APD光探测器 → TIA（跨阻放大器） → Serdes输入。光调制格式：NRZ（开/关键控 OOK）、PAM4（4电平），在数据中心内部主要用NRZ，长距离用相干检测。光模块类型：SFP-DD、QSFP-DD、OSFP，密度和功耗各异。
> 【工程价值】光 I/O 是突破电互连带宽距离积限制的关键技术，电互连在>100m后损耗急剧增加，而光纤损耗仅~0.2dB/km，可以传输更远；光模块的功耗约2~5W/通道，占整个光模块系统功耗的相当比例。
> 【落地注意】光模块与Serdes的接口电平有 CML、差分 ECL 等，要确保阻抗匹配（50Ω差分）；PAM4光模块对线性度要求更高（IMD3<-40dBc），因为多电平之间的间隔更小；光模块的部署要综合考虑功耗、散热和密度要求。

---

Announcements
• Exam 2 Apr 25
  • Focuses on material from Lectures 7-14
  • Previous years’ Exam 2s are posted on the website for
    reference

• Project Final Report due May 2
• Project Presentations May 4 (12:30PM-2:30PM)




                                                            2


> 🔍 深度说明：
> 【研究背景】本讲介绍光 I/O（Optical I/O）接口技术，探讨Serdes与光模块的接口设计，是数据中心和长距离通信中电光转换的核心技术。
> 【核心结论】光 I/O 系统架构：1) TX侧：Serdes输出 → 驱动器 → EAM（电吸收调制器）或 MZ（马赫-曾德）调制器 → 激光器 → 光纤；2) RX侧：PIN/APD光探测器 → TIA（跨阻放大器） → Serdes输入。光调制格式：NRZ（开/关键控 OOK）、PAM4（4电平），在数据中心内部主要用NRZ，长距离用相干检测。光模块类型：SFP-DD、QSFP-DD、OSFP，密度和功耗各异。
> 【工程价值】光 I/O 是突破电互连带宽距离积限制的关键技术，电互连在>100m后损耗急剧增加，而光纤损耗仅~0.2dB/km，可以传输更远；光模块的功耗约2~5W/通道，占整个光模块系统功耗的相当比例。
> 【落地注意】光模块与Serdes的接口电平有 CML、差分 ECL 等，要确保阻抗匹配（50Ω差分）；PAM4光模块对线性度要求更高（IMD3<-40dBc），因为多电平之间的间隔更小；光模块的部署要综合考虑功耗、散热和密度要求。

---

Optical Interconnects
• Electrical Channel Issues
• Optical Channel
• Optical Transmitter Technology
• Optical Receiver Technology
• Optical Integration Approaches




                                   3

![](/img/serdes/fundamentals/lectures/lecture15_ee720_optical_io_深度学习报告/_images/img-002.jpg)
> 🔍 深度说明：
> 【研究背景】光调制原理示意图，介绍不同类型的光调制器及其工作原理，是光 I/O 发射端的核心技术。
> 【核心结论】主要光调制器类型：1) EAM（电吸收调制器）——基于量子限制 Stark 效应，调制速度快（>60GBd），体积小，常用于 DFB 激光器集成；2) MZ（马赫-曾德）调制器——基于干涉原理，消光比高（>30dB），线性度好，适合相干检测；3) SiPho（硅光子）调制器——基于等离子体色散效应，与CMOS工艺兼容，适合集成光模块。调制特性参数：Vπ（半波电压，越低越好）、消光比（ER，越高越好，>30dB）、插入损耗（IL，越低越好）、调制带宽（>60GHz for 112GBd）。
> 【工程价值】选择合适的调制器直接影响光模块的性能和成本；EAM集成DFB激光器是目前数据中心光模块的主流方案，体积小、成本低；MZ调制器用于高性能相干系统。
> 【落地注意】调制器的驱动电压要足够（通常2~5Vpp），驱动器要提供足够的摆幅；调制器的偏置点要稳定（温度变化会导致Vπ变化），需要闭环偏置控制；SiPho调制器的Vπ随工艺偏差可达±20%，要在模块校准时补偿。

---

High-Speed Electrical Link System




                                    4


> 🔍 深度说明：
> 【研究背景】光探测器（PIN/APD）和跨阻放大器（TIA）的电路原理，RX侧的第一级放大器，决定了光接收的灵敏度。
> 【核心结论】光探测器类型：1) PIN二极管——响应速度快（>50GHz），灵敏度一般，需要后级放大；2) APD（雪崩光电二极管）——有内部增益，灵敏度比PIN高6~10dB，但需要高偏置电压（30~80V），带宽受限。TIA（跨阻放大器）功能：将光电流转换为电压并放大，带宽要>0.7× Baud Rate，噪声要足够低；核心指标：跨阻增益（RFB）、输入噪声电流（I_in,n）、带宽（BW）、过载电流（I_overload）。
> 【工程价值】TIA的输入噪声直接决定了系统灵敏度，灵敏度每提升1dB，光模块可传输距离可增加约10%；在112G系统中，TIA输入参考噪声应<1μA rms，才能保证足够的灵敏度。
> 【落地注意】TIA的输入电容要尽可能小（<50fF），包括探测器电容和封装寄生电容；TIA的动态范围要覆盖光功率变化范围（通常-15dBm~+3dBm），过载会导致失真；APD的倍增因子（M）要优化，过大虽然增益高但噪声也大，存在最优工作点。

---

Channel Performance Impact




                             5


> 🔍 深度说明：
> 【研究背景】光通道的损耗和色散特性分析，是光通信系统设计的核心考量，影响传输距离和信号质量。
> 【核心结论】光纤损耗来源：1) 吸收损耗——材料杂质吸收光能量；2) 散射损耗——瑞利散射；3) 连接损耗——光纤端面不匹配。标准单模光纤（SSMF）损耗：~0.2dB/km @ 1550nm，是目前最常用的光纤。色散：1) 模式色散（多模光纤）；2) 色度色散（材料色散+波导色散）；3) 偏振模色散（PMD）。色度色散在1550nm窗口约17ps/nm/km，是限制高速率（>100Gb/s）长距离传输的主要因素。PMD在高速系统中也不能忽视，典型值~0.1ps/√km，高速系统需要用PMD补偿。
> 【工程价值】了解通道特性才能正确设计链路预算，链路预算 = 发射功率 - 损耗 - 余量，必须 > 接收灵敏度；色散会导致脉冲展宽，产生码间干扰，需要均衡补偿。
> 【落地注意】色散补偿在长距离系统中用DCF（色散补偿光纤）或FBG（光纤布拉格光栅），成本高；在数据中心内部（<10km）主要靠数字信号处理（DSP）均衡，包括色散均衡滤波器和MLSE；设计时要考虑温度对色散的影响（约10%变化）。

---

Link with Equalization




                         Deserializer
   Serializer




                                        6


> 🔍 深度说明：
> 【研究背景】光 I/O 与 Serdes 的系统集成，探讨电光联合设计，是实现高性能光传输系统的关键技术。
> 【核心结论】电光集成方案：1) 分离方案——Serdes芯片和光模块独立，通过Serdes芯片输出驱动光模块的调制器；2) 共封装（CPO）——Serdes和光模块物理上紧耦合，Serdes输出的信号直接驱动调制器，减少Serdes I/O功耗和延迟；3) 混合集成——在同一封装内集成多个芯片。光模块的电接口：CEI-56G/112G（芯片到模块），定义电气特性、连接器、协议。Serdes与光模块的接口：PAM4调制、预加重/去加重、线性化驱动。发展趋势：CPO将Serdes和光引擎放在同一个SiP封装中，Serdes I/O功耗可降低30%~50%，是数据中心网络架构的未来方向。
> 【工程价值】CPO方案可以显著降低Serdes到光模块的信号完整性难题，因为距离从10~30cm（PCB走线）缩短到<5mm（封装内走线）；但CPO的散热是主要挑战，Serdes和光模块的功耗合计可达20W+，需要先进的散热技术。
> 【落地注意】CPO的Serdes芯片要和光引擎精确对齐（精度<1μm），对封装工艺要求极高；光模块的可靠性（Connector的插拔寿命、激光器的寿命>25年）是产品化的关键；电光联合设计需要光学和电子设计团队紧密协作。

---

Channel Performance Impact




                             7

---

High-Speed Optical Link System




• Optical interconnects remove many               Optical Channel

  channel limitations
  • Reduced complexity and power
    consumption
  • Potential for high information density with
    wavelength-division multiplexing (WDM)
                                                              8

---

Wavelength-Division Multiplexing




                                          [Young JSSC 2010]

• WDM allows for multiple high-bandwidth (10+Gb/s)
  signals to be packed onto one optical channel

                                                          9

---

Optical Interconnects
• Electrical Channel Issues
• Optical Channel
• Optical Transmitter Technology
• Optical Receiver Technology
• Optical Integration Approaches




                                   10

---

Optical Channels
• Short distance optical I/O channels are
  typically either waveguide (fiber)-based or
  free-space
• Optical channel advantages
  • Much lower loss
  • Lower cross-talk
  • Smaller waveguides relative to electrical traces
  • Potential for multiple data channels on single
    fiber via WDM

                                                       11

---

Waveguide (Fiber)-Based Optical Links
• Optical fiber loss is specified            Optical Fiber Cross-Section
  in dB/km
   • Single-Mode Fiber loss
     ~0.25dB/km at 1550nm
   • RF coaxial cable loss ~100dB/km
     at 10GHz
                                          Single-Mode Fiber Loss & Dispersion
• Frequency dependent loss is
  very small
   • <0.5dB/km over a bandwidth
     >10THz
• Bandwidth may be limited by
  dispersion (pulse-spreading)
   • Important to limit laser linewidth
     for long distances (>1km)
                                                                 [Sackinger]
                                                                           12

---

Inter-Chip Waveguide Examples
    12-Channel Ribbon Fiber

                                  Optical Polymer Waveguide in PCB




                                        [Immonen 2009]
        [Reflex Photonics]
  12 channels at a 250m pitch     <100m channel pitch possible
  10Gb/s mod.  40Gb/s/mm          10Gb/s mod.  100+Gb/s/mm

• Typical differential electrical strip lines are at ~500m pitch

                                                                   13

---

Free-Space Optical Links
                                        [Gruber]




• Free-space (air or glass) interconnect systems
  have also been proposed
• Optical imaging system routes light chip-to-chip

                                                     14

---

CMOS Waveguides – Bulk CMOS
• Waveguides can be made in a bulk process with a
  polysilicon core surrounded by an SiO2 cladding
• However, thin STI layer means a significant portion of the
  optical mode will leak into the Si substrate, causing
  significant loss (1000dB/cm)
• Significant post-processing is required for reasonable loss
  (10dB/cm) waveguides in a bulk process




                      [Holzwarth CLEO 2008]
                                                                15

---

CMOS Waveguides – SOI
• SOI processes have thicker buried oxide layers to
  sufficiently confine the optical mode
• Allows for low-loss waveguides




                 [Narasimha JSSC 2007]
                                                      16

---

CMOS Waveguides – Back-End Processing

• Waveguides & optical
                               [Young JSSC 2010]
  devices can be fabricated
  above metallization
• Reduces active area
  consumption
• Allows for independent
  optimization of transistor
  and optical device
  processes


                                                   17

---

Optical Interconnects
• Electrical Channel Issues
• Optical Channel
• Optical Transmitter Technology
• Optical Receiver Technology
• Optical Integration Approaches




                                   18

---

Optical Modulation Techniques
• Due to it’s narrow frequency (wavelength) spectrum, a
  single-longitudinal mode (SLM) laser source often
  generates the optical power that is modulated for data
  communication
   • This is required for long-haul (multi-km) communication
   • May not be necessary for short distance (~100m) chip-to-chip I/Os
• Two modulation techniques
   • Direct modulation of laser
   • External modulation of continuous-wave (CW) “DC” laser with
     absorptive or refractive modulators




                                                                         19

---

Directly Modulated Laser




• Directly modulating laser output power
• Simplest approach
• Introduces laser “chirp”, which is unwanted frequency
  (wavelength) modulation
• This chirp causes unwanted pulse dispersion when passed
  through a long fiber
                                                            20

---

Externally Modulated Laser




• External modulation of continuous-wave (CW)
  “DC” laser with absorptive or refractive modulators
  • Adds an extra component
  • Doesn’t add chirp, and allows for a transform limited
    spectrum
                                                            21

---

Optical Sources for Chip-to-Chip Links
• Vertical-Cavity Surface-Emitting Laser
  (VCSEL)

• Mach-Zehnder Modulator (MZM)

• Electro-Absorption Modulator (EAM)

• Ring-Resonator Modulator (RRM)

                                           22

---

Vertical-Cavity Surface-Emitting Laser (VCSEL)
     VCSEL Cross-Section                  VCSEL L-I-V Curves




                                                             



• VCSEL emits light perpendicular
  from top (or bottom) surface                    ITH = 700A
                                                 = 0.37mW/mA
• Important to always operate
  VCSEL above threshold current,
  ITH, to prevent “turn-on delay”              Po   I  I TH 
  which results in ISI                                           P  W 
                                       Slope Efficiency            
• Operate at finite extinction ratio                             I  A 
  (P1/P0)
                                                                            23

---

VCSEL Bandwidth vs Reliability
 10Gb/s VCSEL Frequency Response [1]
                                                                  • Mean Time to Failure (MTTF) is
                                                                    inversely proportional to current
                                                                    density squared

                                                                                                    E A   1 1 
                                                                                                         
                                                                                    A               k   T j 373 
                                                                             MTTF  2 e                                      [2]
                                                                                    j

                                                                  • Steep trade-off between
                                                                    bandwidth and reliability
                                                                                                   1
                                                                                  MTTF 
                                                                                                  BW 4
              BW  I avg  I TH

1.   D. Bossert et al, "Production of high-speed oxide confined VCSEL arrays for datacom applications," Proceedings of SPIE, 2002.
2.   M. Teitelbaum and K. Goossen, "Reliability of Direct Mesa Flip-Chip Bonded VCSEL’s," LEOS, 2004.                            24

---

VCSEL Drivers
 Current-Mode VCSEL Driver           VCSEL Driver w/ 4-tap
                                     FIR Equalization




• Current-mode drivers often
  used due to linear L-I
  relationship
• Equalization can be added
  to extend VCSEL              S. Palermo and M. Horowitz, “High-Speed Transmitters in 90nm
                               CMOS for High-Density Optical Interconnects," ESSCIRC, 2006.
  bandwidth for a given
  current density
                                                                                          25

---

Electro-Absorption Modulator (EAM)
         QWAFEM Modulator*




  *N. Helman et al, “Misalignment-Tolerant Surface-Normal Low-Voltage Modulator for Optical Interconnects," JSTQE, 2005.

• Absorption edge shifts with changing bias voltage
  due to the “quantum-confined Stark or Franz-                                            Waveguide EAM [Liu]
  Keldysh effect” & modulation occurs
• Modulators can be surface-normal devices or
  waveguide-based
• Maximizing voltage swing allows for good contrast
  ratio over a wide wavelength range
• Devices are relatively small and can be treated as
  lump-capacitance loads
    •   10 – 500fF depending on device type
                                                                                                                           26

---

Ring-Resonator Modulator (RRM)




• Refractive devices which modulate by
  changing the interference light coupled into
  the ring with the waveguide light
• Devices are relatively small (ring diameters
  < 20m) and can be treated as lumped
  capacitance loads (~10fF)
• Devices can be used in WDM systems to
  selectively modulate an individual            Optical Device Performance from: I. Young, E.
  wavelength or as a “drop” filter at receivers Mohammed,    J. Liao, A. Kern, S. Palermo, B. Block,
                                                M. Reshotko, and P. Chang, “Optical I/O Technology
                                                              for Tera-Scale Computing," ISSCC, 2009.
                                                                                                        27

---

Wavelength Division Multiplexing
w/ Ring Resonators




                                                              [Rabus]




• Ring resonators can act as both modulators and add/drop filters to
  steer light to receivers or switch light to different waveguides
• Potential to pack >100 waveguides, each modulated at more than
  10Gb/s on a single on-chip waveguide with width <1m (pitch ~4m)
                                                                       28

---

Ring-Resonator-Based
Silicon Photonics Transceiver




                        [Li ISSCC 2013]

• High-voltage drivers with simple pre-emphasis to extend
  bandwidth of silicon ring-resonator modulators
• Forwarded-clock receiver with adaptive power-sensitivity RX
• Bias-based tuning loop to stabilize photonic device’s
  resonance wavelength
                                                           29

---

CMOS Modulator Driver
• Simple CMOS-style
  voltage-mode drivers can
  drive EAM and RRM due to
  their small size
                                           Pulsed-Cascode Driver
• Device may require swing
  higher than nominal CMOS
  supply
  • Pulsed-Cascode driver can
    reliably provide swing of
    2xVdd (or 4xVdd) at up to
    2FO4 data rate


                                S. Palermo and M. Horowitz, “High-Speed Transmitters in 90nm
                                CMOS for High-Density Optical Interconnects," ESSCIRC, 2006. 30

---

Mach-Zehnder Modulator (MZM)
                                                                 [Analui]




• Refractive modulator which splits incoming light into two paths,
  induces a voltage-controlled phase shift in the two paths, and
  recombines the light in or out of phase
• Long device (several mm) requires driver to drive low-impedance
  transmission line at potentially high swing (5Vppd)
• While much higher power relative to RRM, they are less sensitive to
  temperature variations
                                                                        31

---

Optical Interconnects
• Electrical Channel Issues
• Optical Channel
• Optical Transmitter Technology
• Optical Receiver Technology
• Optical Integration Approaches




                                   32

---

Optical Receiver Technology
• Photodetectors convert optical
  power into current
   • p-i-n photodiodes
   • Integrated metal-semiconductor-
     metal photodetector


• Electrical amplifiers then
  convert the photocurrent into a
  voltage signal
   • Transimpedance amplifiers
   • Limiting amplifiers
   • Integrating optical receiver


                                       33

---

p-i-n Photodiode
                                         Responsivity:
[Sackinger]
                                            pd q
                                                    8  10 5  pd  
                                     I
                                                                        mA/mW 
                                    Popt     hc

                            Quantum Efficiency:                     pd  1  e W


                             Transit-Time Limited Bandwidth:
                                                        2.4     0.45vsat
                                           f 3dBPD           
                                                       2 tr     W




• Normally incident light absorbed in intrinsic
  region and generates carriers
• Trade-off between capacitance and transit-time
• Typical capacitance between 100-300fF
                                                                                      34

---

Integrated Ge MSM Photodetector
                                                                     XSEM                        SiO2
          Cu                           Cu
                                                                                               0.75 um                 Cu
                            Ge


                                     SiN waveguide                                     Ge
                Cu
                          2 um                                                                                         Silicon
                                                                                              SiO2
                                                                                                                       nitride

                                                                           Very low capacitance: <1 fF
                      Detector                                               Active area: < 2 um2
• Lateral Metal-Semiconductor-Metal (MSM Detector)
• Silicon Nitride Waveguide-Coupled
• Direct Germanium deposition on oxide
I. Young, E. Mohammed, J. Liao, A. Kern, S. Palermo, B. Block, M. Reshotko, and P. Chang, “Optical I/O Technology for Tera-
Scale Computing," IEEE Journal of Solid-State Circuits, 2010.                                                                    35

---

Optical Interconnects
• Electrical Channel Issues
• Optical Channel
• Optical Transmitter Technology
• Optical Receiver Technology
• Optical Integration Approaches




                                   36

---

Optical Integration Approaches
• Efficient cost-effective optical integration
  approaches are necessary for optical
  interconnects to realize their potential for
  improved power efficiency at higher data rates

• Hybrid integration
  • Optical devices fabricated on a separate substrate


• Integrated CMOS photonics
  • Optical devices part of CMOS chip


                                                         37

---

Hybrid Integration
 [Kromer]        [Schow]              [Mohammed]




Wirebonding   Flip-Chip Bonding

                                  Short In-Package Traces



                                                        38

---

Integrated CMOS Photonics
SOI CMOS Process
                    [Analui]
                               “Optics On Top”


                                Optical Layer


                                                 [Young]
Bulk CMOS Process




     [Batten]                                              39

---

Future Photonic CMOS Chip




• Unified optical interconnect for on-chip core-to-core and off-
  chip processor-to-processor and processor-to-memory
I. Young, E. Mohammed, J. Liao, A. Kern, S. Palermo, B. Block, M. Reshotko, and P. Chang, “Optical I/O Technology for Tera-
Scale Computing," IEEE International Solid-State Circuits Conference, 2009.                                                   40

---

Conclusion
• Thanks for the fun semester!




                                 41

---

