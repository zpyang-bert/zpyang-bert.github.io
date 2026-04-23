---
layout: post
title:      "ECEN 720: High-Speed Links Circuits and Systems"
date:       2026-04-15 23:36:57
author:     "Bert"
tags:
  - AI/ML
  - Channel
  - Fundamentals
  - Lecture
  - SerDes
---
## Lecture 4: Channel Pulse Model, ISI, and Modulation Schemes — Detailed Technical Reference

**Original Author:** Sam Palermo, Analog & Mixed-Signal Center, Texas A&M University  
**Expanded Document:** Professional Technical Reference for Signal Integrity and Communication Systems Engineering

---

## 1. Introduction and Scope

Modern high-speed serial links operate at symbol rates where the physical channel behaves as a band-limited linear time-invariant (LTI) system. Understanding how a transmitted symbol propagates through the channel, how energy from one symbol spills into adjacent symbol periods, and how to choose an appropriate modulation format are foundational skills for SerDes (Serializer/Deserializer) design and signal integrity (SI) engineering.

This document provides a rigorous, expanded treatment of the channel pulse model, intersymbol interference (ISI), peak distortion analysis, and the comparative study of NRZ (PAM-2) versus PAM-4 modulation. We develop the material from first principles—impulse and step responses, through convolution, discrete-time channel models, the Nyquist criterion, raised-cosine pulse shaping, bandwidth definitions, and finally practical link engineering trade-offs.

---

## 2. Channel Characterization: From S-Parameters to Time-Domain Behavior

### 2.1 The Linear Time-Invariant Channel Model

A high-speed interconnect (PCB trace, cable, backplane, or package) is accurately modeled as an LTI system over the voltage and temperature ranges of interest. In the frequency domain, the channel is described by its scattering parameters (typically $S_{21}$ for insertion loss) or transfer function $H(f)$. In the time domain, the same channel is fully characterized by its **impulse response** $h(t)$, defined as the output observed when the input is an ideal Dirac delta function $\delta(t)$.

The relationship between the frequency-domain transfer function and the time-domain impulse response is governed by the Fourier transform pair:

$$
H(f) = \mathcal{F}\{h(t)\} = \int_{-\infty}^{\infty} h(t) e^{-j2\pi ft} \, dt
$$

$$
h(t) = \mathcal{F}^{-1}\{H(f)\} = \int_{-\infty}^{\infty} H(f) e^{j2\pi ft} \, df
$$

For a physically realizable channel, $h(t)$ is real-valued and causal ($h(t) = 0$ for $t < 0$), and $H(f)$ exhibits Hermitian symmetry ($H(-f) = H^*(f)$). The magnitude $|H(f)|$ captures frequency-dependent attenuation (skin effect, dielectric loss), while the phase $\angle H(f)$ captures dispersion and delay.

### 2.2 Step Response and Its Relationship to Impulse Response

In practical lab environments and simulation tools, the **step response** $s(t)$ is often easier to measure than the impulse response. The step response is the channel output when the input is a unit step function $u(t)$:

$$
u_{in}(t) = u(t) = \begin{cases} 1, & t \geq 0 \\ 0, & t < 0 \end{cases}
$$

Because integration in the time domain corresponds to division by $j2\pi f$ in the frequency domain, the step response is related to the impulse response by integration:

$$
s(t) = \int_{-\infty}^{t} h(\tau) \, d\tau \quad \Longleftrightarrow \quad h(t) = \frac{ds(t)}{dt}
$$

This relationship is powerful: the rise time $t_r$ of the step response (commonly defined as the 10%–90% transition time) is inversely related to the channel bandwidth. For a first-order RC-like channel, the well-known approximation holds:

$$
t_r \approx \frac{0.35}{BW_{3\text{dB}}}
$$

where $BW_{3\text{dB}}$ is the $-3$ dB bandwidth of $|H(f)|$. For higher-order channels (e.g., transmission lines with skin and dielectric loss), the constant is closer to $0.3$–$0.4$. A slow-rising step response directly signals severe bandwidth limitation and, consequently, strong ISI.

---

## 3. Pulse Response and Convolution

### 3.1 From Impulse Response to Pulse Response

In a digital communication system, the transmitter does not send ideal impulses; it sends **pulses** $p(t)$ of finite duration (typically one symbol period $T_b$ or $T_s$). For NRZ signaling, the basic pulse representing a logical "1" is a rectangular pulse:

$$
c^{(1)}(t) = u(t) - u(t - T_b)
$$

where $T_b$ is the bit period. A logical "0" is represented by the negative of this pulse (for a bipolar NRZ scheme) or by the absence of the pulse (for unipolar NRZ). The **pulse response** $y^{(1)}(t)$ is the channel output when this rectangular pulse is transmitted:

$$
y^{(1)}(t) = c^{(1)}(t) * h(t) = \int_{-\infty}^{\infty} c^{(1)}(\tau) h(t - \tau) \, d\tau
$$

Using the relationship between step and impulse responses, the pulse response can also be written as:

$$
y^{(1)}(t) = s(t) - s(t - T_b)
$$

This form is particularly useful in SPICE-like circuit simulators, where one can simulate the channel step response $s(t)$ once and then construct the pulse response by simple subtraction.

### 3.2 Superposition and the Data Stream Response

An arbitrary NRZ data stream can be modeled as a superposition of time-shifted isolated "1" and "0" pulses. Let the transmitted data sequence be $\{d_k\}$ with $d_k \in \{0, 1\}$. The transmitted voltage waveform is:

$$
V_i(t) = \sum_{k=-\infty}^{\infty} d_k \, c^{(1)}(t - kT_b)
$$

By linearity of the channel, the output voltage $V_o(t)$ is the superposition of the individual pulse responses:

$$
V_o(t) = \sum_{k=-\infty}^{\infty} d_k \, y^{(1)}(t - kT_b)
$$

This equation is the cornerstone of channel pulse modeling: the response to a digital data stream is the summation of shifted, amplitude-scaled pulse responses. Each pulse response extends over many bit periods because of channel bandwidth limitation, causing the tails of past and future pulses to overlap at the sampling instant.

---

## 4. Intersymbol Interference (ISI) Modeling

### 4.1 Origins of ISI

Intersymbol interference is the distortion of the current symbol by the residual energy of neighboring symbols. The primary physical causes in high-speed links are:

| Mechanism | Physical Origin | Effect on Pulse Response |
|-----------|-----------------|--------------------------|
| **Channel Loss (Dispersion)** | Skin effect and dielectric loss increase with frequency | High-frequency components are attenuated, causing pulse spreading and slow rise/fall times |
| **Reflections** | Impedance discontinuities (vias, connectors, stubs) | Echoes and ringing superimposed on the main pulse |
| **Resonances** | Cavity modes in packages or backplanes | Frequency-selective notches and oscillatory ringing in the time domain |

### 4.2 Decomposing the Pulse Response: Cursor, Pre-cursor, and Post-cursor

The pulse response $y^{(1)}(t)$ is sampled at integer multiples of the bit period relative to its peak (the **cursor**). Denoting the cursor sample as $y^{(1)}(t_0)$, the remaining samples are classified as:

- **Pre-cursor ISI**: Samples occurring *before* the cursor ($k < 0$), caused by non-causal equalization or pre-shoot in the pulse.
- **Post-cursor ISI**: Samples occurring *after* the cursor ($k > 0$), caused by the decaying tail of the pulse response.

A typical sampled pulse response looks like:

$$
y^{(1)}(t_0 + kT_b) = [\dots, \, 0.003, \, 0.036, \, \underbrace{0.540}_{\text{cursor } a_0}, \, 0.165, \, 0.065, \, 0.033, \, 0.020, \, 0.012, \, 0.009, \, \dots]
$$

with corresponding index $k = [\dots, -2, -1, 0, 1, 2, 3, 4, 5, 6, \dots]$.

For a symmetric, linear channel, the "0" pulse response is simply the negative of the "1" pulse response:

$$
y^{(0)}(t) = -y^{(1)}(t)
$$

This linearity assumption simplifies analysis significantly and holds well for differential signaling over passive, linear media.

---

## 5. Discrete-Time Channel Models: The Channel FIR

### 5.1 Finite Impulse Response Approximation

Because the pulse response typically decays to negligible levels after a finite number of bit periods, the channel can be approximated by a **Finite Impulse Response (FIR)** filter. The discrete-time channel model is:

$$
a_k = y^{(1)}(t_0 + kT_b)
$$

where $\{a_k\}$ are the FIR tap coefficients. The channel output at sampling instant $n$ is:

$$
V_o[n] = \sum_{k=-L}^{M} d_{n-k} \, a_k
$$

Here, $L$ pre-cursor taps and $M$ post-cursor taps capture the significant ISI. This discrete-time model is the workhorse of link simulators and equalizer design (TX FIR, RX DFE, FFE).

### 5.2 Visualizing the Channel FIR

Conceptually, the channel FIR can be visualized as a tapped delay line:

```
Input: d_n ──┬──► a_0 (cursor) ──┐
             │                   │
             ├──► a_{-1} ────────┤
             │                   │
             ├──► a_{+1} ────────┤
             │                   ├──► V_o[n]
             ├──► a_{+2} ────────┤
             │                   │
             └──► ... ───────────┘
```

The cursor $a_0$ represents the desired signal, while all other taps represent ISI contributions. The ratio of total ISI energy to cursor energy is a common figure of merit for channel severity:

$$
\text{ISI Energy Ratio} = \frac{\sum_{k \neq 0} |a_k|^2}{|a_0|^2}
$$

Channels with an ISI energy ratio greater than unity are generally considered severe and require significant equalization.

---

## 6. Nyquist Criterion for ISI-Free Transmission

### 6.1 The Sampling Theorem and Symbol Rate

Harry Nyquist established the theoretical minimum bandwidth required to transmit symbols without ISI. The key insight is that if the overall system pulse shape (transmitter pulse + channel + receiver filter) satisfies certain conditions, then the sampled output contains only the desired symbol with zero interference from neighbors.

Let the overall system impulse response be $g(t)$, with Fourier transform $G(f)$. For ISI-free transmission at rate $R_s = 1/T_s$ symbols per second, $g(t)$ must satisfy:

$$
g(kT_s) = \begin{cases} 1, & k = 0 \\ 0, & k \neq 0 \end{cases}
$$

This is the **Nyquist pulse criterion** in the time domain.

### 6.2 Frequency-Domain Formulation

Transforming the time-domain condition to the frequency domain yields the more powerful **Nyquist frequency criterion**:

$$
\sum_{m=-\infty}^{\infty} G\left(f - \frac{m}{T_s}\right) = T_s \quad \text{(constant)}
$$

This equation states that when replicas of $G(f)$ are shifted by multiples of the symbol rate $R_s = 1/T_s$ and summed, the result must be a constant. The minimum bandwidth over which this can be satisfied is the **Nyquist bandwidth**:

$$
W_{\text{Nyquist}} = \frac{R_s}{2} = \frac{1}{2T_s}
$$

Thus, the theoretical maximum **spectral efficiency** is:

$$
\frac{R_s}{W} \leq 2 \quad \text{symbols/s/Hz}
$$

### 6.3 The Ideal Sinc Pulse

The pulse shape that achieves the Nyquist bandwidth with rectangular spectral support is the sinc function:

$$
g(t) = \frac{\sin(\pi t / T_s)}{\pi t / T_s} = \text{sinc}\left(\frac{t}{T_s}\right)
$$

with spectrum:

$$
G(f) = \begin{cases} T_s, & |f| \leq \frac{1}{2T_s} \\ 0, & |f| > \frac{1}{2T_s} \end{cases}
$$

While mathematically optimal in bandwidth, the sinc pulse is physically unrealizable because it:
1. Is non-causal (extends to $t = -\infty$).
2. Has very slow $1/t$ decay, making it extremely sensitive to timing jitter.

For these reasons, practical systems use pulse shapes with smoother spectral roll-off and faster time-domain decay.

---

## 7. Raised Cosine Pulse Shaping

### 7.1 Definition and Parameters

The **raised cosine (RC) filter** is the most widely used practical approximation to the ideal Nyquist pulse. It introduces a controllable excess bandwidth (roll-off factor $\alpha$) in exchange for faster time-domain decay and reduced sensitivity to timing errors.

The frequency response of a raised cosine filter is:

$$
G_{\text{RC}}(f) = \begin{cases}
T_s, & |f| \leq \dfrac{1 - \alpha}{2T_s} \\[10pt]
\dfrac{T_s}{2}\left[1 + \cos\left(\dfrac{\pi T_s}{\alpha}\left(|f| - \dfrac{1 - \alpha}{2T_s}\right)\right)\right], & \dfrac{1 - \alpha}{2T_s} < |f| \leq \dfrac{1 + \alpha}{2T_s} \\[10pt]
0, & |f| > \dfrac{1 + \alpha}{2T_s}
\end{cases}
$$

where the **roll-off factor** $\alpha$ ranges from 0 to 1:
- $\alpha = 0$: Ideal sinc pulse (no excess bandwidth).
- $\alpha = 1$: Maximum excess bandwidth; bandwidth is $1/T_s$.

The corresponding time-domain impulse response is:

$$
g_{\text{RC}}(t) = \frac{\sin(\pi t / T_s)}{\pi t / T_s} \cdot \frac{\cos(\pi \alpha t / T_s)}{1 - (2\alpha t / T_s)^2}
$$

### 7.2 Practical Significance of Roll-off Factor

| Roll-off Factor $\alpha$ | Occupied Bandwidth | Time-Domain Decay | Jitter Tolerance |
|--------------------------|-------------------|-------------------|------------------|
| 0.0 | $R_s/2$ (minimum) | $1/t$ (slow) | Very poor |
| 0.2 | $0.6 R_s$ | $1/t^3$ | Moderate |
| 0.5 | $0.75 R_s$ | $1/t^3$ | Good |
| 1.0 | $R_s$ | $1/t^3$ | Excellent |

The raised cosine pulse decays as $1/t^3$, significantly faster than the sinc pulse. This rapid decay means that a small timing offset $\Delta t$ at the sampler produces bounded ISI, whereas the same offset with a sinc pulse could produce unbounded ISI. In high-speed wireline systems, the combination of channel rolloff and transmitter equalization often shapes the received pulse toward a raised-cosine-like form.

### 7.3 Root-Raised Cosine Filtering

In practical systems, the overall raised cosine response is split equally between the transmitter and receiver. Each uses a **root-raised cosine (RRC)** filter, such that:

$$
G_{\text{TX}}(f) \cdot G_{\text{RX}}(f) = G_{\text{RC}}(f)
$$

with $|G_{\text{TX}}(f)| = |G_{\text{RX}}(f)| = \sqrt{G_{\text{RC}}(f)}$. This partitioning maximizes the signal-to-noise ratio at the sampler (matched filtering) while preserving the ISI-free property of the overall response.

---

## 8. Channel Bandwidth Definitions

### 8.1 $-3$ dB Bandwidth ($BW_{3\text{dB}}$)

The $-3$ dB bandwidth is the frequency at which the channel insertion loss reaches $-3$ dB relative to DC. It is a simple, commonly cited metric:

$$
|H(f_{3\text{dB}})| = \frac{|H(0)|}{\sqrt{2}} \approx -3 \text{ dB}
$$

For NRZ signaling, the bit rate $R_b$ has a significant frequency component at $R_b/2$ (the Nyquist frequency). If the channel $-3$ dB bandwidth is less than $R_b/2$, significant ISI is expected.

### 8.2 Effective Nyquist Bandwidth

For data communication, a more relevant bandwidth definition is the **Nyquist bandwidth** required to support the symbol rate without ISI. As derived above:

| Modulation | Bits/Symbol | Nyquist Frequency |
|------------|-------------|-------------------|
| NRZ (PAM-2) | 1 | $R_s/2 = R_b/2$ |
| PAM-4 | 2 | $R_s/2 = R_b/4$ |

PAM-4 halves the required Nyquist frequency relative to NRZ for the same bit rate $R_b$, which is the primary motivation for adopting PAM-4 in bandwidth-limited channels.

### 8.3 Insertion Loss Metrics

In high-speed link design, channel quality is often judged by insertion loss at specific frequencies:
- **Loss at Nyquist**: The insertion loss at $R_b/2$ for NRZ or $R_b/4$ for PAM-4.
- **Loss slope per octave**: The rate at which loss increases with frequency. If the loss increases by more than approximately $9.5$ dB per octave, PAM-4 becomes advantageous because the reduced Nyquist frequency falls on a significantly lower-loss part of the curve.

---

## 9. Peak Distortion Analysis

### 9.1 Worst-Case Eye Height Estimation

Peak distortion analysis (PDA) is a deterministic method for estimating the worst-case eye opening from the channel pulse response. It assumes the channel is linear and that the worst-case pattern can be found by constructing the data sequence that maximally distorts the signal.

For a "1" being detected, the worst-case interference occurs when all neighboring pulse responses with negative polarity are added (constructive interference downward), and all positive neighboring pulse responses are absent. The worst-case "1" voltage is:

$$
s_1(t) = y^{(1)}(t) + \sum_{\substack{k=-\infty \\ k \neq 0}}^{\infty} y^{(d_k)}(t - kT_b) \quad \text{where } d_k \text{ chosen to minimize } s_1
$$

Because $y^{(0)}(t) = -y^{(1)}(t)$, this simplifies to adding all negative ISI samples with a "1" pulse and all positive ISI samples with a "0" pulse. The worst-case "1" becomes:

$$
s_1(t) = y^{(1)}(t_0) + \sum_{\substack{k=-\infty \\ k \neq 0 \\ y^{(1)}(t_0 - kT_b) < 0}}^{\infty} y^{(1)}(t_0 - kT_b)
$$

Similarly, the worst-case "0" voltage is:

$$
s_0(t) = y^{(0)}(t_0) + \sum_{\substack{k=-\infty \\ k \neq 0 \\ y^{(1)}(t_0 - kT_b) > 0}}^{\infty} y^{(1)}(t_0 - kT_b)
$$

### 9.2 Worst-Case Eye Height

The worst-case eye height is the vertical separation between the worst-case "1" and worst-case "0" levels:

$$
s(t_0) = s_1(t_0) - s_0(t_0)
$$

Substituting $y^{(0)} = -y^{(1)}$:

$$
s(t_0) = 2\left[ y^{(1)}(t_0) + \sum_{\substack{k=-\infty \\ k \neq 0 \\ y^{(1)} < 0}} y^{(1)}(t_0 - kT_b) - \sum_{\substack{k=-\infty \\ k \neq 0 \\ y^{(1)} > 0}} y^{(1)}(t_0 - kT_b) \right]
$$

Equivalently, if we define $y_{\text{neg}}$ as the sum of all negative ISI samples and $y_{\text{pos}}$ as the sum of all positive ISI samples (excluding the cursor):

$$
s(t_0) = 2\left[ a_0 + y_{\text{neg}} - y_{\text{pos}} \right] = 2\left[ a_0 - \sum_{k \neq 0} |a_k| \right]
$$

**Example 1:** Given pulse response samples with cursor $a_0 = 0.540$, total negative ISI $= -0.007$, and total positive ISI $= 0.389$:

$$
s = 2(0.540 - 0.007 - 0.389) = 2(0.144) = 0.288
$$

**Example 2:** Given cursor $a_0 = 0.426$, total negative ISI $= -0.053$, and total positive ISI $= 0.542$:

$$
s = 2(0.426 - 0.053 - 0.542) = 2(-0.169) = -0.338
$$

A negative eye height indicates that the channel is **unusable without equalization**—even the best-case data pattern cannot guarantee correct detection.

### 9.3 Finding the Worst-Case Bit Pattern

The worst-case input data pattern can be constructed directly from the sign of the pulse response ISI samples:

1. Start with the pulse response tap vector: $[\dots, a_{-2}, a_{-1}, a_0, a_1, a_2, \dots]$.
2. For each pre-cursor tap $a_k$ ($k < 0$), the worst-case interfering bit at position $k$ is the one with the *opposite* sign of $a_k$ relative to the cursor.
3. For each post-cursor tap $a_k$ ($k > 0$), the same rule applies.
4. Because $y^{(0)} = -y^{(1)}$, flipping the sign of each ISI sample and placing a "1" at the cursor position yields the worst-case bit pattern.

Mathematically, if the cursor is at position 0, the worst-case bit sequence is:

$$
\text{Pattern} = [\dots, -\text{sign}(a_{-2}), -\text{sign}(a_{-1}), 1, -\text{sign}(a_1), -\text{sign}(a_2), \dots]
$$

where $\text{sign}(x)$ is $+1$ for $x > 0$, $-1$ for $x < 0$, and $0$ for $x = 0$.

---

## 10. NRZ (PAM-2) vs. PAM-4 Modulation

### 10.1 Fundamental Definitions

**NRZ (Non-Return-to-Zero), also called PAM-2 (Pulse Amplitude Modulation with 2 levels):**
- Two symbol levels: logic 0 and logic 1.
- One bit transmitted per symbol.
- Symbol rate $R_s = R_b$ (equal to the bit rate).

**PAM-4 (Pulse Amplitude Modulation with 4 levels):**
- Four symbol levels, encoding two bits per symbol: $00 \rightarrow -1$, $01 \rightarrow -1/3$, $11 \rightarrow +1/3$, $10 \rightarrow +1$ (normalized).
- Symbol rate $R_s = R_b / 2$ (half the bit rate).
- Receiver requires three decision thresholds.

### 10.2 Spectral Efficiency and Bandwidth

Because PAM-4 transmits 2 bits per symbol, its Nyquist frequency is half that of NRZ:

| Parameter | NRZ (PAM-2) | PAM-4 |
|-----------|-------------|-------|
| Bits per Symbol | 1 | 2 |
| Symbol Rate $R_s$ | $R_b$ | $R_b/2$ |
| Nyquist Frequency | $R_b/2$ | $R_b/4$ |
| Required Bandwidth (ideal) | $R_b/2$ | $R_b/4$ |

The majority of NRZ signal power is concentrated within approximately $R_b/2$, while PAM-4 power is concentrated within approximately $R_b/4$. This bandwidth reduction is the principal advantage of PAM-4 in lossy channels.

### 10.3 Voltage Margin and Noise Sensitivity

For a fixed peak-to-peak transmit swing of $2A$, the NRZ eye height is $2A$. For PAM-4, the three eyes each have a height of $2A/3$.

| Parameter | NRZ Eye Height | PAM-4 Eye Height (per eye) |
|-----------|----------------|---------------------------|
| Normalized | $2A$ | $2A/3$ |
| Relative to NRZ | 1.0 | $1/3$ ($\approx -9.54$ dB) |

The peak distortion analysis for PAM-4 must account for the fact that the outer eyes ($\pm A$ levels) see ISI from symbols at $\pm A/3$, and the inner eyes see ISI from all four levels. Consequently:

$$
\text{PAM-4 eye height} = \frac{2}{3}\left(A - \sum_{k \neq 0} |a_k|\right)
$$

Wait—more precisely, because the symbol spacing is $2A/3$ and ISI from any neighbor can shift the received level by any multiple of $A/3$, the effective noise margin is reduced not only by the smaller eye but also by the multi-level interference. PAM-4 is **more sensitive to residual ISI** than NRZ.

### 10.4 When to Choose PAM-4 Over NRZ

The classical rule of thumb is:

> **Consider PAM-4 when the channel insertion loss slope exceeds the reduction in PAM-4 eye height.**

Specifically, if the insertion loss over one octave (a doubling in frequency) is greater than:

$$
20 \log_{10}\left(\frac{1}{3}\right) \approx -9.54 \text{ dB}
$$

then the bandwidth savings of PAM-4 outweigh its voltage penalty.

**Case Study 1 — Desktop Channel:**
- Loss at 5 GHz = $-7.5$ dB
- Loss at 2.5 GHz = $-4.8$ dB
- Loss in the octave 2.5–5 GHz = $2.7$ dB

Since $2.7$ dB $< 9.54$ dB, NRZ has better voltage margin and is the preferred choice.

**Case Study 2 — T20 Server Channel:**
- Loss at 2.5 GHz = $-11.1$ dB
- Loss at 5 GHz = $-26.9$ dB
- Loss in the octave 2.5–5 GHz = $15.8$ dB

Since $15.8$ dB $> 9.54$ dB, PAM-4 might be advantageous because halving the Nyquist frequency moves the operating point from $-26.9$ dB to $-11.1$ dB.

### 10.5 Receiver Complexity

PAM-4 receivers are considerably more complex than NRZ receivers:

- **Comparators**: PAM-4 requires 3 slicers (thresholds at $-A/3$, $0$, and $+A/3$) versus 1 slicer for NRZ. This is effectively a 2-bit flash ADC.
- **Reference generation**: The optimal thresholds depend on channel loss and TX equalization, requiring adaptive level calibration.
- **CDR challenges**: PAM-4 has multiple zero-crossing transitions, which can confuse clock-and-data recovery (CDR) circuits and introduce additional jitter.
- **Crosstalk sensitivity**: Smaller eye openings make PAM-4 more vulnerable to crosstalk and power supply noise.

Modern advanced equalization techniques (e.g., multi-tap decision-feedback equalization, DFE) can enable NRZ to remain competitive even in channels with $> 9.5$ dB/octave loss, so the modulation choice is never made in isolation from the equalization budget.

---

## 11. Practical Design Considerations and Trade-offs

### 11.1 Link Analysis Flow

A complete link analysis for modulation selection follows these steps:

1. **Characterize the channel**: Measure or simulate $S_{21}(f)$ and extract the impulse response $h(t)$.
2. **Construct the pulse response**: Convolve the TX pulse shape with $h(t)$, or use $s(t) - s(t - T_b)$.
3. **Sample the pulse response**: Extract the discrete-time FIR coefficients $\{a_k\}$.
4. **Perform peak distortion analysis**: Compute the worst-case eye height for NRZ and PAM-4.
5. **Account for equalization**: Include TX FIR, CTLE, and RX DFE in the effective pulse response.
6. **Evaluate noise budget**: Add crosstalk, jitter, and power supply noise to determine final timing and voltage margins.
7. **Select modulation and architecture**: Choose NRZ or PAM-4 based on the integrated analysis.

### 11.2 Take-Away Points for Link Engineers

- **Loss-slope guidelines** ($\approx 9.5$ dB/octave) are an excellent starting point for modulation selection, but they are not the final word.
- **Equalization capability** can shift the balance back toward NRZ even in seemingly PAM-4-favorable channels.
- **Receiver complexity** (comparators, thresholds, CDR) must be traded off against transmitter and equalizer complexity.
- **PAM-4 challenges** include peak TX power limitations, comparator offset control, CDR jitter, and heightened crosstalk sensitivity.
- Comprehensive link analysis tools (e.g., statistical eye simulators, bit-by-bit channel simulators) that integrate voltage, timing, and crosstalk noise are essential for making the optimal modulation choice.

---

## 12. Conclusion

The channel pulse model provides an intuitive yet mathematically rigorous framework for analyzing high-speed serial links. By understanding the relationship between impulse response, step response, and pulse response, engineers can predict how a digital data stream will be distorted by a physical channel. The decomposition of the pulse response into cursor, pre-cursor, and post-cursor ISI enables discrete-time FIR modeling, which underpins modern equalizer design.

The Nyquist criterion and raised cosine pulse shaping establish the theoretical limits of ISI-free communication, while peak distortion analysis offers a practical deterministic method for estimating worst-case eye openings. Finally, the comparison between NRZ and PAM-4 illustrates the fundamental trade-off between bandwidth efficiency and noise margin—a trade-off that every high-speed link designer must navigate with care.

---

## References and Further Reading

1. **S. Palermo**, *ECEN 720: High-Speed Links Circuits and Systems*, Texas A&M University, Spring 2023.
2. **B. Casper**, "Accurate and Efficient Simulation of Multichannel Transmission with Pulse Response Interconnect Models," *IEEE Trans. Adv. Packag.*, 2006.
3. **H. Song**, Lecture Notes on High-Speed I/O Design, Arizona State University.
4. **V. Stojanovic et al.**, "Autonomous Dual-Mode (PAM2/4) Serial Link Transceiver with Adaptive Equalization and Data Recovery," *IEEE J. Solid-State Circuits*, 2005.
5. **J. G. Proakis and M. Salehi**, *Digital Communications*, 5th Ed., McGraw-Hill, 2008.
6. **E. A. Lee and D. G. Messerschmitt**, *Digital Communication*, 3rd Ed., Springer, 2004.

---

*Document prepared as an expanded technical reference for graduate-level study in high-speed link design and signal integrity.*
