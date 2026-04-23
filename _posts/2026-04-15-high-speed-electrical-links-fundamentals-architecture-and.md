---
layout: post
title:      "High-Speed Electrical Links: Fundamentals, Architecture, and Evolution"
date:       2026-04-15 23:36:19
author:     "Bert"
tags:
  - AI/ML
  - Fundamentals
  - Lecture
  - SerDes
---
## A Detailed Expansion of EE720 Lecture 1: Introduction to High-Speed Links

**Original Source:** ECEN720: High-Speed Links Circuits and Systems, Texas A&M University, Spring 2023  
**Author:** Sam Palermo, Analog & Mixed-Signal Center  
**Document Version:** Expanded Technical Reference (2026)

---

## Abstract

High-speed serial input/output (SerDes) interfaces form the critical communication backbone of modern electronic systems, ranging from multi-terabit Ethernet switches in hyperscale data centers to the camera and display interfaces in mobile handsets. This document provides a comprehensive technical introduction to the principles, architectures, and design trade-offs inherent in high-speed electrical link design. Beginning with the physical mechanisms that degrade signal integrity in electrical channels—skin effect, dielectric loss, reflections, and crosstalk—we develop the mathematical foundations required to analyze and model these impairments. We then examine the end-to-end link architecture, emphasizing the complementary roles of transmitter feed-forward equalization (FFE), receiver continuous-time linear equalization (CTLE), decision-feedback equalization (DFE), and clock and data recovery (CDR). A detailed case study of IBM's seminal 10 Gb/s backplane transceiver in 90 nm CMOS serves as a concrete design example, illustrating how circuit-level innovations overcome severe channel attenuation. Finally, we contextualize these concepts within the trajectory toward 112 Gb/s and 224 Gb/s PAM4 interfaces, discussing the architectural and technological shifts required by contemporary standards.

---

## 1. Introduction and Historical Context

The evolution of chip-to-chip and chip-to-module interconnects over the past three decades represents one of the most persistent challenges in mixed-signal integrated circuit design. As Moore's Law enabled exponential increases in on-chip computational throughput, the bandwidth available at the package pins became a fundamental bottleneck—a phenomenon often termed the **I/O gap**. Early digital systems relied on wide parallel buses (e.g., PCI, AGP, DDR SDRAM) to move data between processors, memory, and peripherals. However, as clock frequencies rose into the hundreds of megahertz, parallel buses suffered from severe **simultaneous switching noise (SSN)**, **clock skew** across dozens or hundreds of traces, and **pin-limited packaging** costs.

The transition to **serial I/O** architectures in the late 1990s and early 2000s addressed these limitations by embedding the clock within the data stream and utilizing differential signaling over controlled-impedance transmission lines. Early SerDes standards such as Fibre Channel (1.0625 Gb/s) and PCI Express 1.0 (2.5 Gb/s) demonstrated the viability of this paradigm. By the mid-2000s, backplane transceivers operating at **10 Gb/s**—such as the IBM design analyzed in this document—pushed CMOS circuits to their limits, requiring sophisticated equalization and low-jitter clock generation.

Today, electrical I/Os operating at **56 Gb/s NRZ** and **112 Gb/s PAM4** per lane are commonplace in networking switch ASICs, with research prototypes exceeding **224 Gb/s PAM4**. These data rates approach the fundamental physical limits of conventional PCB materials, driving innovation in advanced packaging (e.g., chiplets, silicon photonics co-packaging), machine-learning-assisted equalization, and new modulation formats.

---

## 2. Applications and System Hierarchy

### 2.1 Processor Platforms and Peripheral Interconnects

A typical high-performance computing platform integrates multiple SerDes protocols to serve diverse connectivity requirements:

| Application Domain | Typical Standard | Data Rate (Representative) | Key Characteristics |
|--------------------|------------------|---------------------------|---------------------|
| Processor-to-Memory | DDR4/DDR5 | 3.2–6.4 Gbps/pin | Parallel, single-ended, source-synchronous |
| Processor-to-Peripheral | PCI Express 5.0/6.0 | 32/64 GT/s | Differential, packetized, LR/FR channels |
| Mobile Display | MIPI DSI | 1.5–4.5 Gbps/lane | Low-power, short-reach |
| Mobile Camera | MIPI CSI | 1.5–4.5 Gbps/lane | Low EMI, small form factor |
| Storage | SATA / NVMe (PCIe) | 6–64 GT/s | Point-to-point topology |
| Networking | Ethernet (10GBASE-KR to 802.3ck) | 10–112 Gb/s/lane | Backplane, copper cable, optical modules |

### 2.2 Data Center Interconnect Hierarchy

Data centers employ a hierarchy of interconnect technologies scaled to link distance and aggregate bandwidth:

1. **Chip-to-Module / Chip-to-Chip:** Electrical I/Os over short PCB traces or package substrates (< 10 cm). Losses are moderate, and power efficiency (pJ/bit) is paramount.
2. **Intra-Rack:** Electrical backplanes or direct-attach copper (DAC) cables spanning 0.5–2 m. Channel losses often exceed 20–30 dB at Nyquist, mandating TX/RX equalization.
3. **Top-of-Rack (TOR) to Edge Switch:** Traditionally optical (multi-mode or single-mode fiber). Emerging **co-packaged optics (CPO)** and **linear pluggable optics (LPO)** aim to reduce power by minimizing DSP retiming.
4. **Inter-Rack / Inter-Datacenter:** Fully optical links using dense wavelength-division multiplexing (DWDM).

The aggressive scaling of Ethernet switch bandwidth—depicted in the progression from 10 GbE to 800 GbE and 1.6 TbE—requires a commensurate scaling of per-lane data rates. Because increasing lane count indefinitely is constrained by die edge length and package ballout, **per-lane data rate scaling** remains the dominant strategy.

---

## 3. The Electrical Channel: Physics and Signal Degradation

The electrical channel in a high-speed link is never ideal. It comprises PCB traces, vias, connectors, package substrates, and bond wires—each contributing frequency-dependent attenuation and impedance discontinuities. Understanding these impairments quantitatively is essential for designing effective equalization.

### 3.1 Frequency-Dependent Loss Mechanisms

The propagation constant $\gamma(\omega)$ of a transmission line governs how signals attenuate and disperse as they travel:

$$
\gamma(\omega) = \alpha(\omega) + j\beta(\omega) = \sqrt{(R + j\omega L)(G + j\omega C)}
$$

where $R$, $L$, $G$, and $C$ are the resistance, inductance, conductance, and capacitance per unit length, respectively. At high frequencies, two loss mechanisms dominate:

**Skin Effect:** Current concentrates near the conductor surface, causing the effective AC resistance to increase with the square root of frequency:

$$
R_{ac}(f) \approx R_{dc} + R_s \sqrt{f}
$$

The associated attenuation coefficient due to conductor loss is approximately:

$$
\alpha_c(f) \approx \frac{R_{ac}(f)}{2Z_0} \quad \text{[Np/m]}
$$

**Dielectric Loss:** Dielectric materials are not perfect insulators; the alternating electric field dissipates energy proportional to frequency:

$$
\alpha_d(f) \approx \frac{\pi f \sqrt{\varepsilon_r}}{c} \tan\delta \quad \text{[Np/m]}
$$

where $\tan\delta$ is the loss tangent and $\varepsilon_r$ is the relative permittivity. For modern low-loss PCB materials (e.g., Megtron 6, EM-890K), $\tan\delta \approx 0.002$, whereas traditional FR-4 exhibits $\tan\delta \approx 0.02$.

The total insertion loss (IL) in decibels over a channel of length $l$ is:

$$
\text{IL}(f) \approx 8.686 \, l \left( k_1 \sqrt{f} + k_2 f \right) \quad \text{[dB]}
$$

where $k_1$ and $k_2$ are empirical constants capturing skin effect and dielectric loss, respectively, and $f$ is in GHz. For a typical backplane trace, losses range from **0.5 dB/inch to 1.5 dB/inch** at 5 GHz.

### 3.2 Dispersion and Intersymbol Interference (ISI)

Because $\beta(\omega)$ is nonlinear with frequency, different spectral components of a digital pulse propagate at different **group velocities**, causing the pulse to spread in time. This **dispersion** manifests as **intersymbol interference (ISI)**, where energy from one symbol leaks into adjacent symbol periods.

For a transmitted pulse $p(t)$ and channel impulse response $h(t)$, the received signal is:

$$
y(t) = \sum_n a_n \, p(t - nT_b) * h(t) + n(t)
$$

where $a_n \in \{-1, +1\}$ for NRZ/PAM2 signaling, $T_b$ is the bit period, and $n(t)$ represents noise and crosstalk. The channel response creates a **long tail** on $p(t) * h(t)$, such that the amplitude at the sampling instant $kT_b$ depends on multiple preceding bits:

$$
y(kT_b) = a_k \cdot h_{main} + \sum_{n \neq k} a_n \cdot h_{k-n} + n(kT_b)
$$

The summation term is the ISI. In severe channels (e.g., 25 dB loss at 5 GHz), the ISI can completely close the **eye diagram** at the receiver input, making direct slicing impossible without equalization.

### 3.3 Reflections and Impedance Discontinuities

Reflections arise wherever the instantaneous impedance changes along the signal path—at vias, connectors, bond pads, and trace corners. The reflection coefficient at an impedance discontinuity is:

$$
\Gamma = \frac{Z_L - Z_0}{Z_L + Z_0}
$$

where $Z_L$ is the load impedance and $Z_0$ is the characteristic impedance of the transmission line (typically 50 Ω single-ended, 100 Ω differential). Even small reflections ($\Gamma \approx 0.1$) create significant ripple in the channel's frequency response and produce deterministic jitter in the time domain.

**Via stubs** are particularly problematic in backplane channels. A via stub acts as a shorted transmission line stub resonating at:

$$
f_{res} \approx \frac{c}{4 l_{stub} \sqrt{\varepsilon_{r,eff}}}
$$

For a 3.8 mm stub in FR-4 ($\varepsilon_{r,eff} \approx 4$), the resonance occurs near 10 GHz, causing a deep notch in the insertion loss and severe phase distortion.

### 3.4 Crosstalk

Electromagnetic coupling between adjacent traces introduces **co-channel interference**:

- **Near-End Crosstalk (NEXT):** Energy couples from the aggressor transmitter back to the victim transmitter. NEXT is more significant at lower frequencies and in closely packed connector pins.
- **Far-End Crosstalk (FEXT):** Energy couples from the aggressor transmitter forward to the victim receiver. FEXT increases with channel length and is proportional to the derivative of the aggressor signal, making it particularly severe at high data rates.

The **power sum** of crosstalk and noise is a critical budget item in link design. Standards such as IEEE 802.3ck specify maximum integrated crosstalk noise (ICN) limits to ensure bit-error rates below $10^{-5}$ (for PAM4 with FEC) or $10^{-12}$ (for NRZ).

---

## 4. High-Speed Link Architecture

A complete high-speed electrical link comprises three principal subsystems: the transmitter (TX), the channel, and the receiver (RX). Each subsystem employs specific circuit and signal-processing techniques to maximize data fidelity.

### 4.1 Transmitter Equalization: Feed-Forward Equalization (FFE)

The TX FFE is a finite-impulse-response (FIR) filter that pre-distorts the transmitted waveform to compensate for anticipated channel loss. A general $N$-tap FFE output is:

$$
x(t) = \sum_{i=0}^{N-1} c_i \, a_{k-i}
$$

where $c_i$ are the tap coefficients and $a_k$ is the current data symbol. The coefficients are constrained by a **transmit power budget**:

$$
\sum_{i=0}^{N-1} |c_i| \leq 1 \quad \text{(normalized)}
$$

For a 4-tap FFE with one pre-cursor tap ($c_{-1}$), one main cursor ($c_0$), and two post-cursor taps ($c_1, c_2$), typical de-emphasis settings might be:

| Tap | Coefficient | Function | Typical Swing |
|-----|-------------|----------|---------------|
| $c_{-1}$ (Pre-cursor) | $-0.15$ | Pre-shoot, compensates pre-cursor ISI | 15% of main |
| $c_{0}$ (Cursor) | $+0.85$ | Main signal energy | 100% (reference) |
| $c_{1}$ (1st Post) | $-0.30$ | De-emphasis, attenuates low-frequency content | 30–50% of main |
| $c_{2}$ (2nd Post) | $-0.10$ | Secondary post-cursor cancellation | 10–25% of main |

FFE is attractive because it is linear, unconditionally stable, and consumes relatively little power in the TX. However, it cannot cancel pre-cursor ISI without reducing the main cursor amplitude, and it amplifies high-frequency noise (including crosstalk) in the channel.

### 4.2 Receiver Equalization: CTLE and DFE

At the receiver, a **Variable Gain Amplifier (VGA)** and **Continuous-Time Linear Equalizer (CTLE)** provide initial gain and high-frequency boost. A first-order CTLE transfer function has the form:

$$
H_{CTLE}(s) = G \cdot \frac{1 + s/\omega_z}{1 + s/\omega_p}
$$

where $\omega_z < \omega_p$ to create peaking at the Nyquist frequency. CTLEs are simple and fast but, like FFE, amplify noise and crosstalk.

**Decision-Feedback Equalization (DFE)** offers a powerful alternative. A DFE uses past detected bits to subtract their ISI contributions from the current sample:

$$
y_{eq}[k] = y[k] - \sum_{m=1}^{M} h_m \, \hat{a}_{k-m}
$$

Because the feedback uses **decisions** (quantized, noise-free bits), the DFE does not amplify noise or crosstalk. This makes DFE the most SNR-efficient equalizer for post-cursor ISI cancellation. The key architectural challenge is the **feedback loop latency**: the multiplication, summation, and slicer must complete within one unit interval (UI). For a half-rate architecture operating at 10 Gb/s, the UI is 200 ps; at 112 Gb/s, it is only 17.86 ps.

### 4.3 Clock and Data Recovery (CDR)

Because high-speed links embed the clock in the data, the receiver must extract the sampling phase from the incoming data transitions. A digital CDR typically employs a **bang-bang phase detector** (Alexander detector) that produces "early" or "late" decisions based on data and edge samples. These decisions drive a digital loop filter, which in turn controls a **phase interpolator (PI)** or a **phase-locked loop (PLL)** to align the sampling clock.

The CDR loop bandwidth, $f_{BW}$, is a critical parameter. It must be wide enough to track low-frequency jitter from the reference clock and supply noise, yet narrow enough to suppress high-frequency random jitter. Typical $f_{BW}$ values range from **1/1000 to 1/100** of the baud rate.

---

## 5. Case Study: IBM 10 Gb/s Backplane Transceiver in 90 nm CMOS

A landmark design in high-speed link history is the **10 Gb/s 5-tap DFE / 4-tap FFE transceiver** developed by IBM T. J. Watson Research Center and published at ISSCC 2006. Fabricated in a 90 nm CMOS process, this transceiver demonstrated robust operation over electrical backplane channels with up to **25 dB of loss at 5 GHz**—a remarkable achievement for its era.

### 5.1 System Context and Channel

The target channel included package traces, edge connectors, a 16-inch backplane trace, via stubs, and a second package. The cumulative insertion loss reached approximately **24.6 dB at 5 GHz** (the Nyquist frequency for 10 Gb/s NRZ). Without equalization, the received eye was completely closed, as confirmed by both simulation and measurement.

### 5.2 Transmitter Architecture

The transmitter employed a **half-rate CML (current-mode logic)** architecture clocked at 5 GHz to serialize 10 Gb/s data. Key features included:

- **4-tap FFE** with one pre-cursor tap, one main tap, and two post-cursor taps.
- **Current-steering IDACs** generating programmable tap weights.
- **Tap polarity control** allowing both positive and negative coefficients.
- **Output driver** with 50 Ω back-termination to $V_{DDA} = 1.2$ V, and a 1.0 V supply for the core logic.

The tap weight resolutions and full-scale currents were:

| Tap | Full-Scale Current | DAC Resolution |
|-----|-------------------|----------------|
| Pre-cursor | 25% of main | 4 bits |
| Cursor (main) | 100% (24 mA nominal) | 6 bits |
| 1st Post-cursor | 50% of main | 5 bits |
| 2nd Post-cursor | 25% of main | 4 bits |

The TX consumed **70 mW** at 10 Gb/s with the main tap fully active and no FFE de-emphasis. Measured eye diagrams showed a clean, wide-open transmitted eye with no FFE, and a pre-equalized eye with FFE settings of `[0, 85%, -15%, 0]` (pre-cursor, cursor, post-cursor 1, post-cursor 2), demonstrating effective pre-compensation of channel loss.

### 5.3 Receiver Architecture

The receiver was also a **half-rate** design, partitioning the data into even and odd phases to relax timing constraints. Its key components were:

1. **ESD Protection:** Robust human-body model (HBM) and charged-device model (CDM) protection without excessive parasitic capacitance.
2. **T-Coil Input Network:** Broadened the bandwidth of the ESD and package-limited input impedance.
3. **Variable Gain Amplifier (VGA):** Provided gain adjustment to normalize the received signal amplitude before slicing.
4. **5-Tap Continuously Adaptive DFE:** Cancelled severe post-cursor ISI.
5. **Digital CDR:** Achieved clock recovery with independent I/Q phase rotator control.

Total RX power was **130 mW** including the DFE and CDR logic.

### 5.4 DFE Implementation: Speculation and Loop Unrolling

The first post-cursor tap ($H_1$) is the most challenging in a DFE because it must settle within one UI. To relax this timing bottleneck, the IBM design used **$H_1$ speculation** (also known as loop unrolling). Rather than waiting for the previous bit decision, the receiver computes two conditional sums for each possible value of $\hat{a}_{k-1}$ (i.e., +1 and -1) and then selects the correct result with a 2:1 multiplexer once the decision is known.

The deeper taps ($H_2$ through $H_5$) fed back directly because they had more than one UI to settle in the half-rate architecture. The DFE tap weight resolutions were:

| Tap | Resolution |
|-----|------------|
| $H_1$ | 6 bits |
| $H_2$ | 5 bits |
| $H_3, H_4, H_5$ | 4 bits each |

Offset cancellation was provided at every slicer input to compensate for device mismatch and residual baseline wander. The adaptive algorithm maximized the **vertical eye opening** at the data slicing instant.

### 5.5 Digital CDR and Jitter Tolerance

The CDR utilized a fully digital loop with bang-bang phase detection, a digital loop filter, and D/A-converter-driven phase interpolators (PIs) for the I and Q clock paths. Independent control of the I and Q paths simplified half-rate clock distribution.

The CDR demonstrated:
- **Frequency offset tolerance:** Up to **±4000 ppm**, accommodating significant crystal oscillator mismatch between TX and RX.
- **Tracking bandwidth:** Approximately **9 MHz**.
- **Jitter tolerance:** Measured in unit-interval peak-to-peak (UIpp) versus modulation frequency, the receiver met typical standards with > 0.4 UIpp tolerance at low modulation frequencies.

### 5.6 Link Measurement Results

The team evaluated four backplane trace configurations with varying lengths, losses, and via stub conditions:

| Trace | Length | 5 GHz Loss | Via Configuration |
|-------|--------|------------|-------------------|
| #1 | 10" | 12 dB | 2 stubs (3.8 mm) / 0 through |
| #2 | 10" | 10 dB | 0 stubs / 2 through |
| #3 | 15" | 25 dB | 4 stubs (3.8 mm) / 2 through |
| #4 | 20" | 15 dB | 0 stubs / 0 stubs / 2 through |

Horizontal eye opening measurements at the receiver slicer input (BER < $10^{-9}$) confirmed that:
- FFE alone or DFE alone was insufficient for the most challenging 15" channel.
- The combination of **FFE + DFE** maintained an open eye across all configurations, including the 25 dB loss channel.

---

## 6. Performance Metrics and Design Trade-offs

### 6.1 Eye Diagram Metrics

The eye diagram is the primary diagnostic tool for high-speed links. Key metrics include:

- **Eye Height ($V_{eye}$):** Vertical opening, determining noise margin.
- **Eye Width ($T_{eye}$):** Horizontal opening, determining timing margin.
- **Eye Area:** Proportional to the product of height and width, giving a composite figure of merit.

For NRZ signaling, the minimum eye height required for a target BER with additive white Gaussian noise (AWGN) is related to the $Q$-factor:

$$
Q = \frac{V_{eye}}{2\sigma_n} \approx \text{erfcinv}(2 \cdot \text{BER})
$$

For $\text{BER} = 10^{-12}$, $Q \approx 7.04$ (14 dB), requiring $V_{eye} \approx 14\sigma_n$.

### 6.2 Power Efficiency

Power efficiency is quantified in **picojoules per bit (pJ/bit)** or **milliwatts per gigabit per second (mW/Gbps)**. The IBM 10 Gb/s transceiver consumed approximately 200 mW total (70 mW TX + 130 mW RX), yielding:

$$
\text{Energy Efficiency} = \frac{200 \, \text{mW}}{10 \, \text{Gb/s}} = 20 \, \text{pJ/bit}
$$

Modern 112 Gb/s PAM4 SerDes IPs achieve **1–5 pJ/bit**, enabled by advanced CMOS nodes (3 nm, 5 nm), aggressive supply scaling, and architectural optimizations.

### 6.3 Channel Loss Budget

Link designers work within a **channel loss budget** that allocates attenuation to each component. For a 112 Gb/s PAM4 link (Nyquist = 28 GHz), a typical budget might be:

| Component | Loss @ 28 GHz |
|-----------|---------------|
| Package (ball to trace) | 3–5 dB |
| PCB trace (6 inches) | 12–18 dB |
| Connector | 1–2 dB |
| Via transitions | 1–3 dB |
| Margin | 3–5 dB |
| **Total allowable** | **~35 dB** |

When total loss exceeds the budget, alternative solutions such as retimers, active cables, or optical modules must be considered.

---

## 7. Evolution to Modern Interfaces: 112 Gb/s and 224 Gb/s

The principles established by early 10 Gb/s transceivers scale directly to today's leading-edge interfaces, but several architectural shifts have been necessary:

### 7.1 Modulation: From NRZ to PAM4

As channel losses scale with frequency, increasing the baud rate becomes prohibitively difficult. **Pulse-amplitude modulation with 4 levels (PAM4)** encodes 2 bits per symbol, halving the Nyquist frequency for a given data rate. For 112 Gb/s:

- **NRZ:** Nyquist = 56 GHz (impractical on standard PCBs)
- **PAM4:** Nyquist = 28 GHz (challenging but feasible)

The trade-off is a **9.5 dB SNR penalty** relative to NRZ, because the vertical eye is divided into three distinct eyes with smaller separation. PAM4 therefore requires stronger FEC (forward error correction) and more sophisticated equalization.

### 7.2 Technology Scaling Impact

Moving from 90 nm (circa 2006) to 3 nm CMOS (circa 2024) provides:
- **~10× improvement in $f_T$** (transition frequency), enabling broadband amplifiers and faster slicers.
- **Reduced supply voltages** (from 1.2 V to ~0.5 V core), necessitating lower-swing signaling and careful noise management.
- **FinFET/GAA devices** with improved electrostatic control, reducing mismatch and enabling finer DFE tap resolution.

### 7.3 Advanced Equalization Architectures

Modern 112G/224G SerDes often deploy a **concatenated equalization chain**:

$$
\text{TX FFE} \rightarrow \text{Channel} \rightarrow \text{RX CTLE} \rightarrow \text{RX FFE (analog or DSP)} \rightarrow \text{DFE} \rightarrow \text{Slicer}
$$

In long-reach applications, **digital signal processing (DSP)** with maximum-likelihood sequence detection (MLSD) or **machine-learning-based nonlinear equalization** is emerging to handle severe nonlinearity from ADC quantizers and package discontinuities.

---

## 8. Conclusion

High-speed electrical link design sits at the intersection of electromagnetics, communication theory, analog circuit design, and digital signal processing. This document has traced the fundamental impairments that degrade signals in electrical channels—frequency-dependent loss, dispersion, reflections, and crosstalk—and developed the mathematical relationships that govern them. Through the detailed case study of IBM's 10 Gb/s transceiver, we illustrated how a combination of transmitter FFE, receiver CTLE/VGA, speculative DFE, and digital CDR can recover reliable data even over channels with 25 dB of attenuation. Looking forward, the relentless demand for bandwidth in data centers and AI accelerators is pushing electrical I/O toward 112 Gb/s and 224 Gb/s PAM4, where advanced modulation, aggressive equalization, and novel packaging technologies will continue to define the state of the art.

---

## References and Further Reading

1. **Dally, W. J., & Poulton, J. W.** (1998). *Digital Systems Engineering*. Cambridge University Press.
2. **Hall, S. H., & Heck, H. L.** (2009). *Advanced Signal Integrity for High-Speed Digital Designs*. John Wiley & Sons.
3. **Johnson, H., & Graham, M.** (1993). *High-Speed Digital Design: A Handbook of Black Magic*. Prentice Hall.
4. **Razavi, B.** (2003). *Design of Integrated Circuits for Optical Communications*. McGraw-Hill.
5. **Meghelli, M., et al.** (2006). "A 10Gb/s 5-Tap DFE/4-Tap FFE Transceiver in 90nm CMOS Technology." *IEEE ISSCC*.
6. **Rylyakov, A., et al.** (2005). "A Low Power 10Gb/s Serial Link Transmitter in 90-nm CMOS." *IEEE CSICs*.
7. **Zhou et al.** (2017). "Evolution of Optical Interconnects in Data Centers." *Optical Fiber Technology*.
