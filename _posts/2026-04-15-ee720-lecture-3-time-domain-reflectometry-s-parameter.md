---
layout: post
title:      "EE720 Lecture 3: Time-Domain Reflectometry & S-Parameter Channel Models"
date:       2026-04-15 23:36:38
author:     "Bert"
tags:
  - AI/ML
  - Fundamentals
  - Lecture
  - SerDes
  - TDR
---
**Course:** ECEN 720: High-Speed Links Circuits and Systems  
**Instructor:** Sam Palermo, Analog & Mixed-Signal Center, Texas A&M University  
**Document Type:** Expanded Technical Reference  

---

## 1. Introduction

The characterization of electrical interconnects is foundational to the design of modern high-speed serial links. As data rates exceed 10 Gb/s and approach 112 Gb/s PAM4 in contemporary systems, the channel—comprising printed circuit board (PCB) traces, vias, connectors, and cables—becomes the primary performance bottleneck. Accurate interconnect models enable system architects and circuit designers to perform hand calculations, run SPICE or MATLAB simulations, identify bottlenecks, and make informed design trade-offs.

Two principal measurement paradigms dominate high-speed interconnect characterization:

1. **Time-Domain Reflectometry (TDR):** Provides spatially resolved impedance profiles and is invaluable for locating physical discontinuities.
2. **Vector Network Analyzer (VNA):** Measures scattering parameters (S-parameters) in the frequency domain, offering complete linear characterization of multi-port networks.

This document provides a comprehensive treatment of both techniques, their theoretical underpinnings, parameter conversions, cascading methodologies, and their application to channel modeling, impulse response generation, and eye diagram analysis.

---

## 2. Time-Domain Reflectometry (TDR)

### 2.1. Fundamental Principle

A Time-Domain Reflectometer (TDR) consists of a fast step generator and a high-speed sampling oscilloscope. The operation is conceptually simple yet powerful:

1. A fast voltage step is launched into the device under test (DUT) via a precision coaxial cable with known characteristic impedance $Z_0$ (typically 50 Ω).
2. The oscilloscope monitors the voltage at the source port.
3. Any impedance discontinuity along the transmission path causes a reflected wave that superimposes on the incident step.
4. The **magnitude** of the reflection reveals the impedance of the discontinuity.
5. The **timing** of the reflection reveals the **location** of the discontinuity.

Crucially, TDR is a **single-port** measurement technique. Only the input port is accessible for direct observation; the behavior of the channel is inferred from reflected energy.

### 2.2. Reflection Coefficient and Impedance Extraction

When a traveling wave encounters an impedance change, the boundary conditions require that voltage and current remain continuous. This gives rise to the voltage reflection coefficient $\Gamma$ (also denoted $k_r$ in some texts):

$$
\Gamma(t) = \frac{V_r(t)}{V_i} = \frac{Z(t) - Z_0}{Z(t) + Z_0}
$$

Where:
- $V_i$ is the incident step voltage amplitude.
- $V_r(t)$ is the reflected voltage as a function of time.
- $Z(t)$ is the impedance seen by the wave at time $t$.
- $Z_0$ is the reference impedance of the TDR source and cable.

By inverting this relationship, we can extract the time-varying impedance profile $Z(t)$ directly from the measured waveform:

$$
Z(t) = Z_0 \frac{1 + \Gamma(t)}{1 - \Gamma(t)} = Z_0 \frac{V_i + V_r(t)}{V_i - V_r(t)} = Z_0 \frac{V_{total}(t)}{2V_i - V_{total}(t)}
$$

Where $V_{total}(t) = V_i + V_r(t)$ is the voltage observed by the oscilloscope.

For the common case where the TDR outputs a 1 V step into a 50 Ω system, the incident voltage at the DUT interface is $V_i = 0.5$ V (due to the voltage divider formed by the 50 Ω source and the initial 50 Ω line). The impedance formula simplifies to:

$$
Z(t) = Z_0 \frac{V_{total}(t)}{1\text{ V} - V_{total}(t)}
$$

Since time and distance are related by the propagation velocity $v_p$ of the transmission medium, the spatial impedance profile $Z(x)$ is:

$$
Z(x) = Z_T\left(t = \frac{2x}{v_p}\right)
$$

The factor of 2 arises because the wave must travel to the discontinuity at distance $x$ and reflect back.

### 2.3. TDR Waveform Signatures

Understanding the raw TDR waveform for canonical terminations and discontinuities is essential for practical diagnosis.

| Condition | Reflection Coefficient $\Gamma$ | TDR Response |
|-----------|-----------------------------------|--------------|
| **Open Circuit** | $\Gamma = +1$ | Full positive reflection. Voltage steps up to twice the incident level. |
| **Short Circuit** | $\Gamma = -1$ | Full negative reflection. Voltage drops to zero. |
| **Matched Load** ($Z_L = Z_0$) | $\Gamma = 0$ | No reflection. Voltage remains at the incident level. |
| **Mismatch: $Z_L > Z_0$** | $0 < \Gamma < 1$ | Partial positive reflection. Voltage rises above incident level. |
| **Mismatch: $Z_L < Z_0$** | $-1 < \Gamma < 0$ | Partial negative reflection. Voltage dips below incident level. |

### 2.4. Reactive Discontinuities: Capacitance and Inductance

Real interconnects contain localized reactive discontinuities such as vias, pads, and connectors. These produce characteristic exponential responses on a TDR waveform.

#### 2.4.1. Shunt Capacitance

A shunt capacitance $C$ to ground creates a low-impedance path at high frequencies, causing an initial negative dip in the TDR waveform followed by a slow recovery. The time constant of the recovery is:

$$
\tau_C = \frac{Z_0 C}{2}
$$

By curve-fitting the exponential recovery, the capacitance value can be extracted. The factor of 2 appears because the capacitor is driven by the Thevenin equivalent of the incident wave, which has an effective source resistance of $Z_0/2$.

#### 2.4.2. Series Inductance

A series inductance $L$ impedes current flow instantaneously, causing an initial positive voltage spike. The peak voltage spike magnitude and time constant are:

$$
\frac{\Delta V_{peak}}{V_r} = \frac{\tau_L}{t_r} \left[1 - e^{-t_r / \tau_L} \right], \quad \tau_L = \frac{L}{2Z_0}
$$

Where $t_r$ is the rise time of the TDR step. For small inductances where $t_r \gg \tau_L$, the exponential term can be linearized, and the inductance is approximately:

$$
L \approx \frac{2 Z_0 \Delta V_{peak} t_r}{V_i}
$$

### 2.5. TDR Spatial Resolution

The ability of a TDR to resolve two closely spaced discontinuities is fundamentally limited by the **rise time** $t_r$ of the incident step. Two discontinuities separated by a distance $\Delta x$ can only be resolved if:

$$
\Delta x > \frac{t_r v_p}{2}
$$

For a typical PCB material with $v_p \approx 1.5 \times 10^8$ m/s (half the speed of light) and a TDR with $t_r = 30$ ps, the spatial resolution is approximately:

$$
\Delta x > \frac{(30 \text{ ps})(1.5 \times 10^8 \text{ m/s})}{2} = 2.25 \text{ mm}
$$

Furthermore, the step rise time **degrades** as it propagates through the channel due to:
- **Skin-effect dispersion:** Frequency-dependent losses attenuate high-frequency content.
- **Lumped discontinuities:** Each capacitor or inductor acts as a low-pass filter, further slowing the edge.

This dispersion makes it challenging to accurately estimate $L$ and $C$ values deep into a lossy channel. Paradoxically, the channel filtering can sometimes **compensate** for lumped discontinuity spikes in the time domain, making them less visible than they are electrically.

### 2.6. Multiple Reflections

In a channel with multiple impedance discontinuities (e.g., connector A, via B, connector C), the TDR waveform becomes a superposition of primary reflections and secondary (multiple) reflections.

Consider a wave reflecting off discontinuity A, then traveling to B, reflecting back to A, reflecting again at A, and finally returning to the source. These multiple reflections produce "echoes" in the TDR trace that can be misinterpreted as additional physical structures. Expert interpretation requires deconvolving the primary reflections from the higher-order terms using the reflection coefficients at each boundary.

For a channel with discontinuities at points A, B, and C, followed by a load, the observed reflections include:
- **A:** Primary reflection from the first discontinuity.
- **B, BAB:** Primary reflection from B and a secondary reflection involving A.
- **C, CBC, BAC, CAB, CBCBC:** A rapidly growing family of reflections.

### 2.7. Time-Domain Transmission (TDT)

While TDR monitors the input port, Time-Domain Transmission (TDT) monitors the **output** port of a two-port channel. The TDT response is directly proportional to the channel's transfer function $H(j\omega)$:

$$
H(j\omega) = \frac{V_2(j\omega)}{V_1(j\omega)}
$$

TDT is excellent for measuring overall channel attenuation and delay but is **poor** at isolating individual impedance discontinuities because all effects are superimposed on a single rising edge at the output.

---

## 3. Network Analyzer and Directional Couplers

### 3.1. Vector Network Analyzer (VNA)

A Vector Network Analyzer is the workhorse of frequency-domain interconnect characterization. Unlike a TDR, which uses a step stimulus, a VNA stimulates the DUT with a **swept-frequency sinusoidal source** and measures both the amplitude and phase of the response.

A VNA can measure:
- **Transfer functions** ($S_{21}$, $S_{12}$)
- **Scattering matrices** (full S-parameters)
- **Input and output impedance**
- **Group delay and phase linearity**

The test set (the RF front-end of the VNA) is configured differently depending on the measurement type.

### 3.2. Directional Couplers

High-frequency VNAs rely on **directional couplers** to separate forward-traveling (incident) waves from backward-traveling (reflected) waves. A directional coupler consists of two transmission lines placed in close proximity over a short coupling length.

- If the auxiliary line is properly terminated at port A, the voltage across $Z_A$ is proportional to the **forward-traveling wave** ($a_1$).
- If terminated at port B, the voltage across $Z_B$ is proportional to the **reflected wave** ($b_1$).

This separation is critical because it allows the VNA to simultaneously measure the incident power and the reflected power, from which $S_{11}$ is computed.

### 3.3. Measurement Configurations

#### 3.3.1. Transfer Function Measurement
- The "input" signal for the receiver is sampled from a directional coupler that captures the forward-traveling wave at the input.
- The "output" signal is the raw voltage at the DUT's output port.
- The ratio gives the transmission coefficient $S_{21}$.

#### 3.3.2. Impedance Measurement
- The input signal is again the forward-traveling wave sampled by a directional coupler.
- The reflected wave from the DUT is captured by a second directional coupler.
- Comparing the reflected wave to the incident wave characterizes the input impedance $Z_{in}(\omega)$ and $S_{11}$.

---

## 4. Scattering (S) Parameters

### 4.1. Why S-Parameters?

At microwave frequencies (above a few hundred MHz), traditional two-port parameters such as Y-parameters (admittance) and Z-parameters (impedance) become impractical to measure because they require:
- **Open-circuit conditions** (for Y-parameters), which are difficult to achieve due to parasitic capacitance.
- **Short-circuit conditions** (for Z-parameters), which are difficult to achieve due to parasitic inductance.

**S-parameters** solve this problem because they are measured with the DUT terminated in its **nominal impedance** (typically 50 Ω). They are based on the ratio of **incident** and **reflected** traveling waves, which are well-defined even at millimeter-wave frequencies.

### 4.2. Formal Definitions

For a linear $N$-port network, we define normalized incident and reflected wave variables $a_n$ and $b_n$ at each port $n$:

$$
a_n = \frac{V_n^{+}}{\sqrt{Z_0}}, \quad b_n = \frac{V_n^{-}}{\sqrt{Z_0}}
$$

Where $V_n^{+}$ is the voltage of the wave entering port $n$, and $V_n^{-}$ is the voltage of the wave exiting port $n$. The relationship between all ports is described by the scattering matrix $[S]$:

$$
\begin{bmatrix} b_1 \\ b_2 \\ \vdots \\ b_N \end{bmatrix} = \begin{bmatrix} S_{11} & S_{12} & \cdots & S_{1N} \\ S_{21} & S_{22} & \cdots & S_{2N} \\ \vdots & \vdots & \ddots & \vdots \\ S_{N1} & S_{N2} & \cdots & S_{NN} \end{bmatrix} \begin{bmatrix} a_1 \\ a_2 \\ \vdots \\ a_N \end{bmatrix}
$$

For a two-port network, the defining equations are:

$$
\begin{aligned}
b_1 &= S_{11} a_1 + S_{12} a_2 \\
b_2 &= S_{21} a_1 + S_{22} a_2
\end{aligned}
$$

### 4.3. Physical Interpretation of Two-Port S-Parameters

| Parameter | Definition | Physical Meaning |
|-----------|------------|------------------|
| **$S_{11}$** | $\left. \frac{b_1}{a_1} \right\|_{a_2=0}$ | Input reflection coefficient with output matched. Measures return loss. |
| **$S_{21}$** | $\left. \frac{b_2}{a_1} \right\|_{a_2=0}$ | Forward transmission coefficient with output matched. Measures insertion loss/gain. |
| **$S_{12}$** | $\left. \frac{b_1}{a_2} \right\|_{a_1=0}$ | Reverse transmission coefficient with input matched. Measures isolation. |
| **$S_{22}$** | $\left. \left. \frac{b_2}{a_2} \right\|_{a_1=0} \right.$ | Output reflection coefficient with input matched. |

### 4.4. Differential S-Parameters (Mixed-Mode)

High-speed digital systems almost exclusively use differential signaling. A differential pair constitutes a 4-port network (two signal lines, each with a near-end and far-end port). To analyze differential and common-mode behavior, we use **mixed-mode S-parameters**.

For a 4-port network with ports 1, 2 (line 1) and 3, 4 (line 2), the differential-mode reflection and transmission coefficients are:

$$
\begin{aligned}
S_{dd11} &= \frac{1}{2}(S_{11} + S_{33} - S_{13} - S_{31}) \\
S_{dd21} &= \frac{1}{2}(S_{21} + S_{43} - S_{23} - S_{41})
\end{aligned}
$$

Where:
- $S_{dd11}$ is the differential input return loss.
- $S_{dd21}$ is the differential insertion loss.

A complete 4-port S-parameter file (e.g., from 50 MHz to 15 GHz in 10 MHz steps) contains $4 \times 4 = 16$ complex values per frequency point and serves as the "golden" channel model for system simulations.

---

## 5. ABCD Parameters and Conversions

### 5.1. Definition of ABCD Parameters

While S-parameters are ideal for measurement, they are inconvenient for **cascading** networks because the output waves of one stage are not the direct input waves of the next in a simple matrix multiplication sense. The **ABCD parameter** (or transmission parameter) matrix solves this by relating the total voltage and current at the input port to those at the output port:

$$
\begin{bmatrix} V_1 \\ I_1 \end{bmatrix} = \begin{bmatrix} A & B \\ C & D \end{bmatrix} \begin{bmatrix} V_2 \\ -I_2 \end{bmatrix}
$$

The individual parameters are defined as:

$$
\begin{aligned}
A &= \left. \frac{V_1}{V_2} \right\|_{I_2=0} & B &= \left. \frac{V_1}{I_2} \right\|_{V_2=0} \\
C &= \left. \frac{I_1}{V_2} \right\|_{I_2=0} & D &= \left. \frac{I_1}{I_2} \right\|_{V_2=0}
\end{aligned}
$$

### 5.2. Converting Between S and ABCD Parameters

The conversion from S-parameters to ABCD parameters for a two-port network with reference impedance $Z_0$ is:

$$
\begin{aligned}
A &= \frac{(1 + S_{11})(1 - S_{22}) + S_{12} S_{21}}{2 S_{21}} \\
B &= Z_0 \frac{(1 + S_{11})(1 + S_{22}) - S_{12} S_{21}}{2 S_{21}} \\
C &= \frac{1}{Z_0} \frac{(1 - S_{11})(1 - S_{22}) - S_{12} S_{21}}{2 S_{21}} \\
D &= \frac{(1 - S_{11})(1 + S_{22}) + S_{12} S_{21}}{2 S_{21}}
\end{aligned}
$$

And the inverse conversion from ABCD to S-parameters:

$$
\begin{aligned}
S_{11} &= \frac{A + B/Z_0 - C Z_0 - D}{A + B/Z_0 + C Z_0 + D} \\
S_{12} &= \frac{2(AD - BC)}{A + B/Z_0 + C Z_0 + D} \\
S_{21} &= \frac{2}{A + B/Z_0 + C Z_0 + D} \\
S_{22} &= \frac{-A + B/Z_0 - C Z_0 + D}{A + B/Z_0 + C Z_0 + D}
\end{aligned}
$$

These conversions are exact and must be performed at each frequency point independently.

---

## 6. Cascaded Networks and De-embedding

### 6.1. Cascading with ABCD Matrices

The primary advantage of ABCD parameters is that the overall matrix for a cascade of $N$ networks is simply the ordered matrix product:

$$
[ABCD]_{total} = [ABCD]_1 \times [ABCD]_2 \times \cdots \times [ABCD]_N
$$

**Example: Cascaded Via and Transmission Line**

Consider a channel segment consisting of a PCB via, followed by a transmission line, followed by another via. The procedure is:
1. Measure or simulate the 2-port S-parameters of the via ($S_{via}$) and the transmission line ($S_{TL}$) independently.
2. Convert $S_{via}$ to $[ABCD]_{via}$ and $S_{TL}$ to $[ABCD]_{TL}$.
3. Compute the total ABCD matrix: $[ABCD]_{total} = [ABCD]_{via1} \times [ABCD]_{TL} \times [ABCD]_{via2}$.
4. Convert $[ABCD]_{total}$ back to S-parameters to obtain the composite channel model.

### 6.2. T-Parameters (Alternative for Cascading)

An alternative to ABCD parameters is the **scattering transfer matrix** or **T-matrix**, which directly cascades in the wave domain:

$$
\begin{bmatrix} b_1 \\ a_1 \end{bmatrix} = \begin{bmatrix} T_{11} & T_{12} \\ T_{21} & T_{22} \end{bmatrix} \begin{bmatrix} a_2 \\ b_2 \end{bmatrix}
$$

T-matrices cascade via simple multiplication just like ABCD matrices and are often preferred in microwave CAD tools because they avoid conversions to voltage/current.

### 6.3. De-embedding Techniques

In practical measurements, the DUT is often not directly accessible at the VNA reference planes. Instead, it is embedded within fixtures, cables, probes, or launch structures. **De-embedding** is the process of mathematically removing these extraneous networks to isolate the DUT.

#### 6.3.1. 2x-Thru De-embedding

The most common technique in high-speed digital characterization is the **2x-Thru** method (also known as SOLR or SOLT depending on calibration standards). Here:
1. A "thru" standard is measured to characterize the fixture on both sides.
2. The DUT is then measured in the fixture.
3. Using ABCD or T-matrix inversion, the fixture effects are removed:

$$
[ABCD]_{DUT} = [ABCD]_{fixture\_left}^{-1} \times [ABCD]_{measured} \times [ABCD]_{fixture\_right}^{-1}
$$

#### 6.3.2. Port Extension

For simple, electrically short extensions (e.g., a short coaxial cable), **port extension** can be applied. This adds a known electrical delay and loss to the measurement reference plane without full matrix de-embedding.

---

## 7. Measurement Calibration

Accurate S-parameter measurements depend critically on calibration. A VNA must be calibrated to remove systematic errors from the test cables, adapters, and internal hardware.

### 7.1. Types of Calibration

| Calibration Type | Standards Used | Application |
|------------------|----------------|-------------|
| **SOLT** | Short, Open, Load, Thru | General-purpose, coaxial measurements |
| **SOLR** | Short, Open, Load, Reciprocal Thru | When a perfect thru is unavailable |
| **TRL** | Thru, Reflect, Line | Most accurate for non-coaxial environments (PCB, on-wafer) |
| **E-Cal** | Electronic calibration module | Fast, repeatable, automated |

### 7.2. Error Correction Models

VNA calibration mathematically corrects for 12-term error models in a 2-port measurement:
- **Directivity error:** Imperfect isolation in the directional coupler.
- **Source match error:** Imperfect 50 Ω match at the source.
- **Load match error:** Imperfect 50 Ω match at the load.
- **Reflection tracking and transmission tracking:** Frequency response errors in the receivers.
- **Isolation (crosstalk):** Leakage between ports.

Without proper calibration, measured $S_{11}$ and $S_{21}$ can be in error by several dB, particularly at frequencies above 10 GHz.

---

## 8. Impulse Response Generation from S-Parameters

### 8.1. Theoretical Basis

Channel impulse responses are essential for time-domain simulation and link analysis tools. Given the channel transfer function $H(j\omega)$, which for a transmission measurement is simply $S_{21}(j\omega)$, the output spectrum $Y(j\omega)$ for an input $X(j\omega)$ is:

$$
Y(j\omega) = H(j\omega) X(j\omega)
$$

The time-domain output is the convolution:

$$
y(t) = h(t) * x(t) = \int_{-\infty}^{\infty} h(t - \tau) x(\tau) d\tau
$$

Where the impulse response $h(t)$ is the inverse Fourier transform of the transfer function:

$$
h(t) = \mathcal{F}^{-1}\{ H(j\omega) \}
$$

### 8.2. Practical IFFT Procedure

Because S-parameters are typically measured only over a positive frequency range ($f_{min}$ to $f_{max}$), we must construct a two-sided spectrum before applying the Inverse Fast Fourier Transform (IFFT).

**Step 1:** Construct the negative-frequency components using the complex conjugate symmetry of real-valued impulse responses:

$$
S(-f) = S^*(f)
$$

**Step 2:** Zero-pad the frequency axis to increase the time-domain resolution. The native time resolution $\Delta t$ is determined by the maximum measured frequency:

$$
\Delta t = \frac{1}{2 f_{max}}
$$

For example, with $f_{max} = 15$ GHz, $\Delta t \approx 33.3$ ps. To achieve 1 ps resolution, one must zero-pad the frequency data out to $\pm 500$ GHz before performing the IFFT.

**Step 3:** Perform the IFFT. The resulting $h(t)$ should be real (any small imaginary residual is numerical noise).

**Step 4 (Sanity Check):** Perform an FFT on the generated $h(t)$ and compare it back to the original measured S-parameter data to verify correctness.

### 8.3. Windowing and Causality

Real physical channels are **causal**; the impulse response must be zero for $t < 0$. However, raw S-parameter measurements may contain small non-causal artifacts due to noise, calibration errors, or finite measurement bandwidth. Applying a **Hilbert transform** or a causal windowing function can enforce causality and improve the quality of the generated impulse response.

---

## 9. Channel Transient Response and Eye Diagrams

### 9.1. Channel Transient Response

Once the impulse response $h(t)$ is available, the response to any arbitrary input waveform (e.g., a PRBS data pattern) can be computed via convolution. This allows designers to simulate the signal at the receiver input for different data rates, transmitter equalization settings, and channel geometries.

### 9.2. Eye Diagrams

An **eye diagram** is a superposition of many unit intervals (UIs) of a received signal, triggered by the data clock. It provides an instantaneous visual summary of signal integrity health.

Key eye diagram metrics include:
- **Eye Height (Voltage):** The vertical opening, indicating noise margin.
- **Eye Width (Time):** The horizontal opening, indicating timing margin.
- **Jitter:** Horizontal closure due to noise and inter-symbol interference.
- **Eye Slope:** Indicates sensitivity to timing errors.

As data rates increase, the eye diagram transitions from wide open (low data rate) to nearly closed (high data rate), necessitating equalization techniques such as Feed-Forward Equalization (FFE) and Decision Feedback Equalization (DFE) at the receiver.

---

## 10. Inter-Symbol Interference (ISI)

### 10.1. Causes of ISI

**Inter-Symbol Interference (ISI)** occurs when the residual energy from previous data bits distorts the current bit. In high-speed links, ISI is primarily caused by:

1. **Reflections:** Energy reflected from impedance discontinuities arrives at the receiver delayed and superimposed on the current bit.
2. **Channel Resonances:** Standing waves created by reflections can create frequency-selective attenuation or peaking.
3. **Channel Loss (Dispersion):** Frequency-dependent attenuation (dominated by dielectric and conductor losses) causes the pulse to spread out in time, with its tail overlapping into subsequent bit periods.

### 10.2. ISI Impact on Link Performance

At the transmitter output (channel input), the eye diagram is typically wide open because the signal has not yet experienced the channel's distortions. After propagation through the channel, the pulses experience severe dispersion, and the eye at the receiver input is significantly closed.

A practical example from a 10 Gb/s backplane link illustrates this dramatically:
- **Input Eye:** Large voltage swing, wide eye opening.
- **Output Eye:** Reduced amplitude, significant jitter, and ISI-induced closure.

The amount of ISI is directly related to the impulse response: if the impulse response has significant energy outside the intended bit period (i.e., a long, ringing tail), ISI will be severe.

---

## 11. Practical Applications in High-Speed Link Characterization

### 11.1. Link Budget Analysis

S-parameters are used to build the **channel model** for link budget analysis. By extracting $S_{dd21}$ (differential insertion loss), designers can quantify the total channel attenuation at the Nyquist frequency ($f_{Nyq} = \text{Data Rate}/2$). This attenuation figure directly determines the required transmitter drive strength, receiver sensitivity, and equalization complexity.

### 11.2. Crosstalk Analysis

A 4-port or 8-port S-parameter file captures not only the differential insertion loss ($S_{dd21}$) but also the near-end crosstalk ($S_{NEXT}$) and far-end crosstalk ($S_{FEXT}$) between adjacent channels. These are critical for determining whether a multi-lane system can operate without excessive aggressor-victim coupling.

### 11.3. Equalization Co-design

The channel S-parameters are imported into system simulators (e.g., Keysight ADS, MATLAB, HSPICE) to co-design transmitter pre-emphasis/de-emphasis and receiver CTLE/DFE. The goal is to find the equalization settings that maximize the eye opening at the receiver sampler.

### 11.4. Compliance Testing

Industry standards (PCIe, Ethernet, DDR, USB) specify channel compliance masks in the S-parameter domain. For example, an Ethernet backplane channel must have an insertion loss within a specified range and a return loss below a specified threshold across the operating bandwidth. VNA-based S-parameter measurement is the definitive compliance test.

---

## 12. Summary

This document has presented a comprehensive treatment of Time-Domain Reflectometry and S-parameter-based channel modeling, expanding significantly on the foundational lecture material. Key takeaways include:

- **TDR** provides spatially resolved impedance profiles via reflection coefficients but is fundamentally limited by step rise time and multiple reflection ambiguity.
- **VNA-based S-parameters** provide the complete linear characterization of multi-port networks and are the industry standard for high-speed channel modeling.
- **ABCD and T-parameters** enable the mathematical cascading and de-embedding of networks, which is essential for building composite channel models from individually characterized structures.
- **Impulse response generation** via IFFT of $S_{21}$ bridges the frequency-domain measurement to the time-domain simulation world.
- **ISI and eye diagram closure** are the ultimate manifestations of channel imperfections, and understanding their root causes in the S-parameter and TDR domains is critical for designing robust high-speed links.

---

## References

1. W. Dally and J. Poulton, *Digital Systems Engineering*, Cambridge University Press, 1998. (TDR material, Ch. 3.4, 3.6–3.7)
2. S. H. Hall and H. L. Heck, *Advanced Signal Integrity for High-Speed Digital Designs*, Wiley-IEEE Press, 2009. (S-parameter material, Ch. 9)
3. Keysight Technologies, *TDR Theory Application Note*.
4. S. Palermo, *ECEN 720: High-Speed Links Circuits and Systems*, Texas A&M University, Spring 2023.
5. M. Meghelli, "A 10Gb/s 5-tap DFE/4-tap FFE Transceiver in 90nm CMOS," *ISSCC Dig. Tech. Papers*, Feb. 2006.
