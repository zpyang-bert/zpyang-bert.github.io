---
layout: post
title:      "EE720 Lecture 2: High-Speed Channel Components, Wires, and Transmission Lines — Detailed Technical Reference"
date:       2026-04-15 23:36:52
author:     "Bert"
tags:
  - AI/ML
  - Channel
  - Fundamentals
  - Lecture
  - SerDes
---
> **Course:** ECEN720: High-Speed Links Circuits and Systems  
> **Instructor:** Prof. Sam Palermo, Analog & Mixed-Signal Center, Texas A&M University  
> **Expanded & Annotated by:** Signal Integrity Engineering Team  
> **Scope:** This document significantly expands the original lecture material with rigorous derivations, modern design context for 112 Gb/s/PAM4 and 224 Gb/PAM4, and practical PCB/package-level insights.

---

## 1. Introduction: The Channel in Modern SerDes Systems

A high-speed serial link (SerDes) is only as good as the physical channel that carries its electromagnetic energy from transmitter (Tx) to receiver (Rx). In contemporary systems pushing **112 Gb/s/PAM4** and emerging **224 Gb/PAM4**, the channel is no longer a simple copper trace—it is a complex distributed network comprising:

- **IC packages** (FC-BGA, wirebond, interposer)
- **PCB traces** (microstrip, stripline, coplanar waveguide)
- **Vias** (through-hole, blind, buried, backdrilled)
- **Connectors** (board-to-board, edge, cabled backplane)
- **Discrete passive components** (AC caps, ESD structures)

Understanding each element through the lens of **transmission line theory**, **S-parameters**, and **electromagnetic field behavior** is essential for achieving bit-error rates (BER) below $10^{-15}$ in production systems.

---

## 2. Channel Component Deep Dive

### 2.1 IC Packages

Package selection directly constrains aggregate I/O bandwidth because pin-count scaling historically lags behind on-chip transistor scaling (Moore’s Law vs. package I/O). Modern high-performance links universally employ **Flip-Chip Ball Grid Array (FC-BGA)** packages due to their superior electrical and thermal characteristics.

| Package Type | Pin Count Range | Key Characteristics |
|--------------|-----------------|---------------------|
| SOP | 8 – 56 | Low cost, high inductance leads |
| QFP | 64 – 304 | Gull-wing leads, moderate performance |
| PBGA | 256 – 420 | Solder ball array, reduced inductance |
| EBGA | 352 – 896 | Enhanced thermal/electrical performance |
| **FC-BGA** | **1089 – 2116+** | **Lowest loop inductance, best SI/PI** |

#### 2.1.1 Package Parasitics

A first-order package model includes series inductance ($L$), shunt capacitance ($C$), and mutual coupling ($M$ or coupling coefficient $K$):

- **Bondwires:** $L \approx 0.7\text{–}1.0 \, \text{nH/mm}$, $C \approx 20 \, \text{fF/mm}$
- **Package traces ( redistribution layer / RDL ):** $L \approx 0.7\text{–}1.0 \, \text{nH/mm}$, $C \approx 80\text{–}90 \, \text{fF/mm}$
- **Mutual inductance/capacitance:** Significant crosstalk contributors in dense BGA arrays

Flip-chip packaging reduces the impedance seen at the die bump interface by an order of magnitude compared to wirebond because the current loop area (signal-to-return path) is dramatically smaller. At 56 GHz Nyquist frequencies, even 100 fF of parasitic capacitance or 100 pH of excess inductance can create severe impedance discontinuities.

### 2.2 Printed Circuit Boards (PCB)

PCBs provide the primary interconnection medium between package, connectors, and passive components.

- **Layer counts:** Consumer boards 4–8 signal layers; high-performance backplanes >30 layers
- **Stackup architecture:** Signal layers alternate with ground/power plane pairs to provide controlled impedance and low-impedance power delivery
- **Copper weights:** 0.5 oz (17.5 µm) for fine-pitch signal layers; 1 oz (35 µm) for power planes

#### 2.2.1 Trace Configurations

| Configuration | Structure | Advantages | Disadvantages |
|---------------|-----------|------------|---------------|
| **Microstrip** | Signal trace on outer PCB surface | Easy to route, lower loss (air dielectric) | Exposed to EMI, higher skew, more crosstalk |
| **Stripline** | Signal sandwiched between two ground planes | Excellent isolation, controlled impedance, lower crosstalk | Higher dielectric loss (fully embedded), fabrication tolerance on $h$ |

For 112G/224G designs, **stripline routing** is preferred for long traces because it offers better electromagnetic containment and reduced far-end crosstalk (FEXT).

### 2.3 Connectors

Board-to-board connectors must preserve differential impedance (typically $85\,\Omega$ or $100\,\Omega$) while achieving high density (16–32 differential pairs per 10 mm). At mm-wave frequencies:

- **Crosstalk** becomes the dominant bottleneck (both near-end NEXT and far-end FEXT).
- **Ground shielding** and optimized pin-field ground-signal-signal-ground (GSSG) patterns are standard.
- Cabled backplanes (e.g., twinax, micro-coax) are increasingly replacing traditional PCB backplanes for 224G links due to lower loss and superior crosstalk control.

### 2.4 Vias

Vias transition signals between PCB layers. A plated-through-hole (PTH) via consists of:
- **Barrel:** Plated copper cylinder
- **Pads:** Annular rings connecting to traces
- **Anti-pads (clearance holes):** Openings in power/ground planes to prevent shorting

#### 2.4.1 Via Stubs and Backdrilling

Any via segment that does not carry signal current acts as a **stub**—an unterminated transmission line branching off the main path. The stub resonates when its electrical length approaches $\lambda/4$, creating deep nulls in $S_{21}$ (insertion loss). The null frequency is:

$$
f_{null} = \frac{c}{4 \cdot h_{stub} \cdot \sqrt{\varepsilon_r}}
$$

where $h_{stub}$ is the physical stub length and $\varepsilon_r$ is the dielectric constant.

For a typical backplane via with a 60 mil stub in FR-4 ($\varepsilon_r \approx 4.2$):

$$
f_{null} \approx \frac{3 \times 10^8 \, \text{m/s}}{4 \times 1.524 \times 10^{-3} \, \text{m} \times \sqrt{4.2}} \approx 32 \, \text{GHz}
$$

This falls directly within the 56 GHz Nyquist band of 112 Gb/s PAM4. **Backdrilling** (controlled-depth drilling to remove unused barrel length) is therefore mandatory. Backdrilling can reduce stubs to <10 mil, pushing nulls beyond 100 GHz.

---

## 3. Wire and Trace Models: From Lumped to Distributed

Before invoking full transmission line theory, we establish the per-unit-length (PUL) parameters: resistance $R$, inductance $L$, capacitance $C$, and conductance $G$.

### 3.1 Resistance ($R$)

DC resistance is governed by material resistivity $\rho$ and conductor geometry:

$$
R_{DC} = \frac{\rho \cdot l}{A} = \frac{\rho \cdot l}{w \cdot h}
$$

For cylindrical wires:

$$
R_{DC} = \frac{\rho \cdot l}{\pi r^2}
$$

where $w$ = trace width, $h$ = trace thickness, and $r$ = wire radius.

### 3.2 Capacitance ($C$)

Capacitance depends on dielectric permittivity $\varepsilon = \varepsilon_r \varepsilon_0$ and geometry:

| Geometry | Capacitance (per unit length) |
|----------|------------------------------|
| Parallel plate (approx.) | $C \approx \frac{w \varepsilon}{h}$ |
| Round wire above ground | $C \approx \frac{2\pi\varepsilon}{\ln(2h/r)}$ |
| Two round wires | $C \approx \frac{\pi\varepsilon}{\ln(s/r)}$ |
| Two rectangular traces | $C \approx \frac{w\varepsilon}{s} + \frac{2\pi\varepsilon}{\ln(4s/h)}$ |

Minimizing $\varepsilon_r$ (e.g., using PTFE/Teflon or low-Dk materials like Megtron 6) reduces both capacitance and propagation delay.

### 3.3 Inductance ($L$)

Inductance is determined by magnetic permeability $\mu$ and the closed current loop area. For a wire in a homogeneous medium, the useful product is:

$$
L \cdot C = \mu \varepsilon = \mu_r \mu_0 \varepsilon_r \varepsilon_0
$$

with $\mu_0 = 4\pi \times 10^{-7} \, \text{H/m}$.

### 3.4 Choosing the Right Model

| Model | Condition | Use Case |
|-------|-----------|----------|
| Ideal wire | $l \ll \lambda/20$ | Very short on-chip interconnects |
| Lumped R, L, C | Low frequency, short traces | Package bumps, short bond pads |
| RC transmission line | $R \gg \omega L$ | Long on-chip metal lines |
| **LC transmission line** | $R \ll \omega L$, $G \ll \omega C$ | **Most PCB traces >~50 MHz** |
| **RLGC transmission line** | General case | **All high-frequency channels** |

The transition frequency from RC to LC behavior is:

$$
f > \frac{R}{2\pi L}
$$

Examples:
- AWG24 twisted pair: $f > 32 \, \text{kHz}$
- PCB trace: $f > 2.7 \, \text{MHz}$
- On-chip minimum-width M6 (0.18 µm): $f > 1.6 \, \text{GHz}$

---

## 4. Transmission Line Theory and the RLGC Model

### 4.1 The Telegrapher’s Equations

Consider an infinitesimal segment $dx$ of a transmission line modeled as a series impedance $R\,dx + j\omega L\,dx$ and shunt admittance $G\,dx + j\omega C\,dx$. Applying Kirchhoff’s laws and taking the limit as $dx \rightarrow 0$ yields the **telegrapher’s equations**:

$$
\frac{\partial V(x,t)}{\partial x} = -R \, I(x,t) - L \frac{\partial I(x,t)}{\partial t}
\tag{1}
$$

$$
\frac{\partial I(x,t)}{\partial x} = -G \, V(x,t) - C \frac{\partial V(x,t)}{\partial t}
\tag{2}
$$

### 4.2 Time-Harmonic Form

Assuming sinusoidal steady-state with angular frequency $\omega$, we convert to phasor form:

$$
\frac{dV(x)}{dx} = -(R + j\omega L) \, I(x)
\tag{3}
$$

$$
\frac{dI(x)}{dx} = -(G + j\omega C) \, V(x)
\tag{4}
$$

Differentiating (3) with respect to $x$ and substituting (4):

$$
\frac{d^2 V(x)}{dx^2} = \gamma^2 V(x)
\tag{5}
$$

$$
\frac{d^2 I(x)}{dx^2} = \gamma^2 I(x)
\tag{6}
$$

where the **propagation constant** $\gamma$ is:

$$
\gamma = \alpha + j\beta = \sqrt{(R + j\omega L)(G + j\omega C)} \quad [\text{m}^{-1}]
\tag{7}
$$

### 4.3 Propagation Constant Interpretation

The general solution to (5) and (6) describes forward-traveling and backward-traveling waves:

$$
V(x) = V_f(x) + V_r(x) = V_{f0} e^{-\gamma x} + V_{r0} e^{+\gamma x}
$$

$$
I(x) = I_f(x) + I_r(x) = I_{f0} e^{-\gamma x} + I_{r0} e^{+\gamma x}
$$

| Parameter | Symbol | Physical Meaning |
|-----------|--------|------------------|
| Attenuation constant | $\alpha$ | Signal amplitude decay per unit length [Np/m] |
| Phase constant | $\beta$ | Phase shift per unit length [rad/m] |
| Phase velocity | $v_p = \omega / \beta$ | Speed of wave propagation [m/s] |
| Wavelength | $\lambda = 2\pi / \beta$ | Spatial period of the wave [m] |

### 4.4 Characteristic Impedance ($Z_0$)

For an infinitely long line (no reflections), the ratio of voltage to current at any point is the **characteristic impedance**:

$$
Z_0 = \frac{V(x)}{I(x)} = \sqrt{\frac{R + j\omega L}{G + j\omega C}} \quad [\Omega]
\tag{8}
$$

If the line is terminated in $Z_0$, the source sees an equivalent infinite line. This is the fundamental basis for impedance matching in high-speed links.

---

## 5. Lossless, Low-Loss, and Lossy Transmission Lines

### 5.1 Lossless LC Line ($R = 0$, $G = 0$)

For an ideal lossless line:

$$
\gamma = j\omega\sqrt{LC} \quad \Rightarrow \quad \alpha = 0, \quad \beta = \omega\sqrt{LC}
$$

Key properties:
- **No attenuation:** $\alpha = 0$
- **Dispersionless:** $v_p = \frac{1}{\sqrt{LC}}$ is independent of frequency
- **Real impedance:** $Z_0 = \sqrt{\frac{L}{C}}$

This idealization is useful for conceptual understanding but breaks down above a few GHz.

### 5.2 Low-Loss RLGC Line

For practical PCB traces where $R \ll \omega L$ and $G \ll \omega C$, we can expand $\gamma$ using a binomial approximation:

$$
\gamma = j\omega\sqrt{LC} \left[ 1 - j\frac{RC + GL}{2\omega LC} \right]^{1/2}
$$

Keeping first-order terms:

$$
\gamma \approx \underbrace{\frac{R}{2Z_0} + \frac{GZ_0}{2}}_{\alpha} + j\underbrace{\omega\sqrt{LC} \left[ 1 + \frac{1}{8}\left(\frac{R}{\omega L}\right)^2 + \frac{1}{8}\left(\frac{G}{\omega C}\right)^2 \right]}_{\beta}
$$

where $Z_0 = \sqrt{L/C}$.

This reveals two distinct loss mechanisms:
- **Resistive (conductor) loss:** $\alpha_R \approx \frac{R}{2Z_0}$
- **Dielectric loss:** $\alpha_D \approx \frac{GZ_0}{2}$

The frequency-dependent $\beta$ term causes **dispersion**: different frequency components travel at different velocities, distorting the pulse shape. In practice, this manifests as a "fast step followed by a slow DC tail" in the step response.

---

## 6. Frequency-Dependent Loss Mechanisms: Skin Effect and Dielectric Loss

### 6.1 Skin Effect (Resistive Loss)

At high frequencies, the magnetic field generated by the current induces eddy currents that force the net current density to concentrate near the conductor surface. The current density decays exponentially with depth:

$$
J(d) = J_0 e^{-d/\delta}
$$

The **skin depth** $\delta$ is the depth at which current density falls to $1/e$ of its surface value:

$$
\delta = \sqrt{\frac{1}{\pi f \mu \sigma}} = \sqrt{\frac{\rho}{\pi f \mu}}
$$

where $\sigma$ is conductivity and $\rho = 1/\sigma$ is resistivity.

For a rectangular trace, the critical frequency $f_s$ is defined where $\delta = h/2$ (half the trace thickness):

$$
f_s = \frac{4\rho}{\pi \mu h^2}
$$

Above $f_s$, the effective cross-sectional area decreases with $\sqrt{f}$, so:

$$
R(f) = R_{DC} \sqrt{\frac{f}{f_s}}
$$

Consequently, the resistive attenuation constant becomes:

$$
\alpha_R = \frac{R_{DC}}{2Z_0} \sqrt{\frac{f}{f_s}} \quad [\text{Np/m}]
$$

**Practical example:** A 5-mil stripline with $R_{DC} = 7 \, \Omega/\text{m}$ has $f_s \approx 43 \, \text{MHz}$. At 56 GHz, skin effect dominates the channel budget.

### 6.2 Dielectric Absorption (Dielectric Loss)

Dielectric materials are not perfect insulators. Under an alternating electric field, polar molecules rotate and dissipate energy as heat. This is quantified by the **loss tangent** $\tan\delta$:

$$
\tan\delta = \frac{G}{\omega C}
$$

The dielectric attenuation constant is:

$$
\alpha_D = \frac{GZ_0}{2} = \frac{2\pi f C \tan\delta \cdot \sqrt{L/C}}{2} = \pi f \tan\delta \sqrt{LC} = \frac{\pi f \tan\delta}{v_p}
$$

Key distinction: dielectric loss increases **linearly** with frequency, whereas skin-effect loss increases only as $\sqrt{f}$. At sufficiently high frequencies (typically >20–30 GHz for advanced laminates), dielectric loss becomes the dominant budget item.

### 6.3 Total Insertion Loss

The total voltage attenuation with distance is:

$$
\frac{V(x)}{V(0)} = e^{-(\alpha_R + \alpha_D)x}
$$

In decibels:

$$
\text{IL}(f) = 8.686 \times (\alpha_R + \alpha_D) \times l \quad [\text{dB}]
$$

| Material | Loss @ 56 GHz (dB/in) | 25 dB Reach (inches) |
|----------|----------------------|----------------------|
| Megtron 6 | ~1.1 | ~12.5" |
| Tachyon 100G | ~1.6 | ~15.6" |
| Standard FR-4 | ~2.0+ | <10" |
| PTFE (Teflon) | ~1.1 | ~22.7" |

Modern 112G systems typically budget **25–30 dB** of total channel loss at Nyquist. Therefore, material selection and trace length are co-optimized during architecture definition.

---

## 7. Reflections, Impedance Discontinuities, and Termination

### 7.1 Reflection Coefficient

Whenever a traveling wave encounters an impedance discontinuity, a portion reflects back toward the source. The **voltage reflection coefficient** at the load is:

$$
\Gamma_L = \frac{V_r}{V_i} = \frac{Z_L - Z_0}{Z_L + Z_0}
$$

Similarly, at the source:

$$
\Gamma_S = \frac{Z_S - Z_0}{Z_S + Z_0}
$$

### 7.2 Lattice Diagrams and Multiple Reflections

For a line with both source and load mismatch, reflections bounce back and forth. The voltage at any time can be computed via a **Bounce Diagram (Lattice Diagram)**:

$$
V_{total}(t) = V_i \sum_{n=0}^{\infty} (\Gamma_S \Gamma_L)^n \cdot [u(t - n \cdot T_{RT}) + \Gamma_L \cdot u(t - (n+0.5) \cdot T_{RT})]
$$

where $T_{RT} = 2l\sqrt{LC}$ is the round-trip delay.

#### Termination Examples

| Case | $Z_S$ | $Z_L$ | $\Gamma_S$ | $\Gamma_L$ | Behavior |
|------|-------|-------|------------|------------|----------|
| Ideal | $50\,\Omega$ | $50\,\Omega$ | 0 | 0 | Clean step, no ringing |
| Open | $50\,\Omega$ | $\infty$ | 0 | +1 | Voltage doubles at load |
| Short | $50\,\Omega$ | $0$ | 0 | –1 | Voltage inverts at load |
| Mismatched | $400\,\Omega$ | $600\,\Omega$ | 0.778 | 0.846 | Severe ringing, slow convergence |

### 7.3 Termination Schemes

| Scheme | Description | Application |
|--------|-------------|-------------|
| **No termination** | $Z_S \ll Z_0$, $Z_L \gg Z_0$ | Only when $t_r \gg n \cdot T_{RT}$ (very short lines) |
| **Source termination** | $Z_S = Z_0$ | Point-to-point, moderate speed; source sees half-step initially |
| **Receiver termination** | $Z_L = Z_0$ | Absorbs incident wave; intermediate discontinuities still reflect |
| **Double termination** | $Z_S = Z_L = Z_0$ | **Gold standard for high-speed serial links**; reflections absorbed at both ends; signal swing is halved |

For modern SerDes, **double termination** is the norm. The Tx driver includes a calibrated source termination (often $50\,\Omega$ single-ended or $100\,\Omega$ differential), and the Rx presents a matched termination to the line.

---

## 8. S-Parameter Interpretations for Channel Analysis

While time-domain reflectometry (TDR) provides intuitive spatial impedance profiles, **S-parameters** are the lingua franca of frequency-domain channel characterization.

### 8.1 Two-Port S-Parameters

For a linear, time-invariant (LTI) channel, the scattering matrix relates incident and reflected waves:

$$
\begin{bmatrix} b_1 \\ b_2 \end{bmatrix} = \begin{bmatrix} S_{11} & S_{12} \\ S_{21} & S_{22} \end{bmatrix} \begin{bmatrix} a_1 \\ a_2 \end{bmatrix}
$$

### 8.2 Key Parameter Meanings

| Parameter | Name | Physical Insight | Design Relevance |
|-----------|------|------------------|------------------|
| $S_{21}$ | Insertion Loss (IL) | Forward transmission | Channel bandwidth, equalizer requirements |
| $S_{11}$ | Input Return Loss | Reflection at port 1 | Impedance matching quality |
| $S_{12}$ | Reverse Isolation | Backward transmission | Reciprocity check ($S_{12} = S_{21}$ for passive channels) |
| $S_{22}$ | Output Return Loss | Reflection at port 2 | Receiver termination quality |

### 8.3 Derived Metrics

- **Insertion Loss Deviation (ILD):** Variation of $|S_{21}|$ from a fitted line; indicates resonant behavior from stubs or coupling.
- **Integrated Crosstalk Noise (IXN/ICN):** RMS sum of all NEXT and FEXT transfer functions ($S_{31}$, $S_{41}$, etc.) weighted by transmitter spectrum.
- **Insertion Loss to Crosstalk Ratio (ICR):** $|\text{IL}| - |\text{XTALK}|$ in dB; a figure of merit for channel feasibility.

For 112G/224G channels, $S_{21}$ is routinely extracted from 3D EM solvers (HFSS, CST, SIwave) and used directly in statistical eye and time-domain simulation (COM, HSpice, ADS).

---

## 9. Differential Transmission Lines and Crosstalk

### 9.1 Why Differential Signaling?

Differential signaling is mandatory for multi-gigabit links because it provides:
- **Self-referencing:** Rejects common-mode noise (power supply noise, EMI)
- **Double signal swing:** $V_{diff} = V_+ - V_-$, effectively doubling dynamic range
- **Reduced SSO (Simultaneous Switching Output) noise:** Current returns locally through the pair
- **Improved EMI:** Far-field radiation from equal and opposite currents partially cancels

The pin overhead is roughly $1.3\text{–}1.8\times$ (not $2\times$) because fewer dedicated return pins are needed.

### 9.2 Odd and Even Modes

A differential pair supports two orthogonal propagation modes:

#### Even Mode (Common Mode)
- Both lines driven with $V_+ = V_-$
- Virtual open between the traces
- Effective capacitance: $C_{even} = C_{signal\_to\_ground}$
- Effective inductance: $L_{even} = L + M$
- Characteristic impedance: $Z_{even} = \sqrt{\frac{L + M}{C_{sig}}}$

#### Odd Mode (Differential Mode)
- Lines driven with $V_+ = -V_-$
- Virtual ground plane exists midway between traces
- Effective capacitance: $C_{odd} = C_{sig} + 2C_{mutual}$
- Effective inductance: $L_{odd} = L - M$
- Characteristic impedance: $Z_{odd} = \sqrt{\frac{L - M}{C_{sig} + 2C_{mutual}}}$

### 9.3 Differential and Common-Mode Impedances

$$
Z_{diff} = 2 \cdot Z_{odd} = 2 \sqrt{\frac{L - M}{C_{sig} + 2C_{mutual}}}
$$

$$
Z_{CM} = \frac{Z_{even}}{2} = \frac{1}{2} \sqrt{\frac{L + M}{C_{sig}}}
$$

Standard target values are $Z_{diff} = 85\,\Omega$ or $100\,\Omega$.

### 9.4 Crosstalk Mechanisms

Crosstalk arises from capacitive and inductive coupling between adjacent traces:

$$
V_{NEXT} \propto \frac{1}{4} \left( \frac{C_m}{C_t} + \frac{L_m}{L_t} \right) \cdot V_{ aggressor }
$$

$$
V_{FEXT} \propto \frac{1}{2} \left( \frac{L_m}{L_t} - \frac{C_m}{C_t} \right) \cdot l \cdot \frac{dV_{aggressor}}{dt}
$$

where $C_m$ and $L_m$ are mutual capacitance and inductance, and $C_t$, $L_t$ are total capacitance and inductance per unit length.

In a homogeneous medium (e.g., stripline), $L_m/L_t = C_m/C_t$, causing **FEXT to cancel to first order**. This is another major reason stripline is preferred for dense routing at 112G/224G.

Mitigation strategies:
- Increase trace-to-trace spacing ($3W$ or $5W$ rules)
- Implement ground-signal-ground (GSG) routing
- Use zig-zag or tabbed routing in advanced packages
- Shield critical lines with ground strips

---

## 10. Via Modeling for 112G/224G Channels

A via is a vertical transition that behaves as a short coaxial stub with characteristic impedance $Z_{via}$ typically in the $30\text{–}50\,\Omega$ range. For accurate channel models, vias must be represented as either:

1. **Lumped π/T networks** (for short vias < $\lambda/20$)
2. **Distributed transmission line segments** (for longer vias)
3. **Full 3D EM models** (gold standard for 112G+)

### 10.1 Via Equivalent Circuit

A typical via model includes:
- **Pad capacitance** ($C_{pad}$): ~50–150 fF per pad
- **Barrel inductance** ($L_{barrel}$): ~10–50 pH
- **Stub capacitance/inductance:** Dominates high-frequency behavior
- **Anti-pad capacitance:** Fringing fields across the clearance hole

### 10.2 Backdrilling and Stub Control

As derived in Section 2.4.1, the quarter-wave stub resonance is:

$$
f_{null} = \frac{c}{4 h_{stub} \sqrt{\varepsilon_{eff}}}
$$

For 224G links (Nyquist = 56 GHz for PAM4), stubs must be backdrilled such that $f_{null} > 70\,\text{GHz}$ to provide adequate margin. This requires $h_{stub} < 8\,\text{mil}$ in typical low-Dk materials.

### 10.3 Advanced Via Techniques
- **Blind/buried vias:** Eliminate stubs entirely but increase fabrication cost
- **Staggered vias:** Reduce crosstalk by offsetting transition layers
- **Via fencing:** Ground vias placed alongside signal vias to improve return path continuity

---

## 11. Modern PCB/Package Design Considerations for 112G/224G

### 11.1 Material Selection

| Property | Target for 112G+ | Rationale |
|----------|------------------|-----------|
| $D_k$ ($\varepsilon_r$) | 3.0–3.6 @ 10 GHz | Lower $D_k$ reduces capacitance and increases $v_p$ |
| $D_f$ ($\tan\delta$) | < 0.002 @ 10 GHz | Minimizes dielectric loss at mm-wave frequencies |
| $T_g$ | > 180°C | Survives multiple reflow cycles |
| Copper roughness | < 1 µm RMS | Reduces conductor loss enhancement |

Leading materials: **Megtron 6/7**, **Tachyon 100G**, **EM-890K**, **PTFE blends**.

### 11.2 Copper Surface Roughness

Real copper foil is not smooth. The tooth-like profile (e.g., VLP, HVLP, RTF) effectively increases the conductor surface area, exacerbating skin-effect loss. The **Huray model** or **Hammerstad-Jensen correction** modifies $R_{AC}$ with a roughness factor $K_r$:

$$
K_r = 1 + \frac{2}{\pi} \arctan\left(1.4 \left(\frac{\Delta}{\delta}\right)^2\right)
$$

where $\Delta$ is the RMS roughness. For 112G/224G, **HVLP (Hyper Very Low Profile)** copper with $\Delta < 0.5\,\mu\text{m}$ is strongly recommended.

### 11.3 Cabled Backplanes and Alternative Media

As data rates push beyond 112 Gb/s, purely PCB-based channels face fundamental limits from dielectric loss and crosstalk. **Cabled backplanes** using twinax or micro-coaxial cables offer:
- Lower loss (~0.3–0.5 dB/m @ 26 GHz vs. ~1.5 dB/in for PCB)
- Superior crosstalk isolation (>40 dB)
- Reach >1 m at 224 Gb/s

These are already being standardized in IEEE 802.3dj and OIF CEI-224G.

### 11.4 Design Rules of Thumb

1. **Loss budget:** Target < 28 dB total channel loss at Nyquist for CTLE + 1-tap DFE architectures; < 35 dB if advanced DSP (MLSD/NN equalization) is available.
2. **Impedance tolerance:** Maintain $\pm5\%$ on $Z_0$ ($95\text{–}105\,\Omega$ differential for $100\,\Omega$ target) to keep reflections below –26 dB.
3. **Via stub length:** Backdrill to <10 mil for 112G; <6 mil for 224G.
4. **Trace length matching:** Skew between P and N of a differential pair < 1 ps for 112G PAM4.
5. **Return path continuity:** Never allow a signal trace to cross a plane split without a nearby stitching capacitor or return via.

---

## 12. Summary

This document has expanded the foundational concepts of EE720 Lecture 2 into a comprehensive signal integrity reference. Key takeaways:

- The **channel** is a distributed RLGC network; lumped approximations fail above a few GHz.
- **Skin effect** ($\sqrt{f}$) and **dielectric loss** ($f$) dictate the channel's frequency response and equalization requirements.
- **Reflections** arise from impedance discontinuities; double termination is the standard for high-speed serial links.
- **S-parameters** provide the rigorous frequency-domain characterization required for 112G/224G channel compliance.
- **Differential signaling** in stripline configurations offers the best trade-off between density, crosstalk, and loss.
- **Via stubs** and **copper roughness** are no longer second-order effects—they can consume the entire loss budget at 224G.
- **Material selection** (low-$D_k$, low-$D_f$, HVLP copper) and **cabled architectures** are critical enablers for next-generation links.

---

## References

1. Dally, W. J., & Poulton, J. W. *Digital Systems Engineering*. Cambridge University Press, 1998.
2. Hall, S. H., Heck, H. L., & McCall, J. *Advanced Signal Integrity for High-Speed Digital Designs*. Wiley, 2009.
3. Johnson, H., & Graham, M. *High-Speed Signal Propagation: Advanced Black Magic*. Prentice Hall, 2003.
4. Palermo, S. *ECEN720: High-Speed Links Circuits and Systems, Lecture 2*. Texas A&M University, Spring 2023.
5. Samtec Technical Whitepaper: *Advanced Board Dielectrics for 112G Applications*.
6. Ghiasi, A. *Cabled Backplane for 224Gb/s Ethernet*. IEEE 802.3, 2017.
