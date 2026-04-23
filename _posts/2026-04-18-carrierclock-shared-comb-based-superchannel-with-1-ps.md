---
layout: post
title:      "Carrier/clock-shared comb-based superchannel with <1-ps timing error enabling baud-rate sampling coherent reception for scale-across AIDCs"
date:       2026-04-18 12:56:30
author:     "Bert"
tags:
  - Mineru
---
Chenbo Zhang1,\*, Yixiao Zhu2,\*, Xiang Cai1, Yi Zou1, Weiwei Hu 1, Zhangyuan Chen 1, Weisheng Hu2, Fan Zhang1, Xiaopeng Xie1

1 State Key Laboratory of Photonics and Communications, School of Electronics, Peking University, Beijing 100871, China 2State Key Laboratory of Photonics and Communications, Shanghai Jiao Tong University, Shanghai 200240, China \*zhangchenbo@pku.edu.cn, yixiaozhu@sjtu.edu.cn

Abstract: We demonstrate electro-optic comb-based 18λ ×384Gb/s superchannel for AIDC distributed training. It achieves clock synchronization and <0.9-ps sampling instant jitter, enabling low-power baud-rate-sampling coherent-lite reception with negligible 0.12dB long-term SNR penalty over 1 hour. © 2026 The Author(s)

## 1. Introduction

Large-scale artificial intelligence (AI) engines are reshaping modern computing infrastructures. As large language models scale toward trillion-level parameters, AI datacenters (AIDCs) increasingly rely on scale-across architectures enabled by high-speed optical interconnects to overcome electrical I/O limitations in bandwidth density, reach, and energy efficiency. Distributed training across multiple AIDCs requires optical links that simultaneously support higher data rates and extended transmission distances, imposing stringent constraints on power consumption. Conventional intensity modulation and direct detection (IM-DD) links are struggling due to limited dispersion tolerance and spectral efficiency, driving a transition toward coherent detection. However, DSP complexity and power consumption remain major barriers for coherent adoption in AIDCs. In this context, baud-rate coherent reception is an attractive solution, as it significantly reduces ADC sampling rates and DSP workloads, enabling 50% potential power reduction while preserving the reach and capacity advantages of coherent transmission [1,2].

However, baud-rate sampling coherent-lite reception across all wavelength-division-multiplexed (WDM) channels remains challenging, and total DSP power consumption requires further reduction within a superchannel architecture. Current baud-rate sampling methods rely on local timing recovery at the receiver [1,2], where a digital timing-error detector in the DSP drives a phase-locked loop (PLL) to align the sampling instants. In WDM reception, this typically involves one clock-recovery loop and one PLL per channel, making hardware complexity and power consumption scale linearly with channel count. Additionally, carrier-frequency offset and decision-assisted timing induce a larger penalty in baud-rate sampling systems, especially when using high-order modulation formats. As an alternative, optical-clock-assisted baud-rate sampling has been explored by modulating a Tx-side clock onto an optical carrier and transmitting it alongside the data [3-5]. The delivered clock can then be used to synchronize the receiver sampling clock. Nevertheless, previous demonstrations mostly utilize multicore or multilane configurations [3-5], where the clock signal occupies an auxiliary spatial channel. Such spatial requirements limit compatibility with the standard single-mode fiber (SMF) links deployed in practical datacenter interconnects.

Here, we propose and demonstrate a photonics-enabled baud-rate sampling coherent reception across all WDM channels over a standard SMF link, utilizing an electro-optic (EO) comb-based architecture. The EO comb plays three roles simultaneously. Its comb lines delivers the Tx-side clock while supplying the multi-wavelength carriers for high-capacity WDM signals. Moreover, its fixed repetition frequency ( fr) ensures stable relative timing among all channels. Leveraging these properties, our system (1) synchronizes Tx- and Rx-side clocks using 2 pilot comb lines and locks $f _ { r }$ for both carrier and LO combs, and (2) maintains a relative timing fluctuation below ±0.9 ps between channels separated by ∼ 1 THz. This joint clock synchronization and wavelength timing locking provide precise sampling-time alignment across the entire WDM system. We therefore demonstrate the first baud-rate sampling coherent reception of dual-polarization (DP) signals across all channels over an SMF, without requiring any auxiliary link. 18×32 GBd DP-64-QAM signals are sampled in baud-rate and the entire receiver DSP is also operated at baud-rate. In addition, the need for frequency-offset and carrier phase estimation is removed. During a continuous 1-hour measurement, the penalty induced by sampling-phase drift remains below only 0.12 dB.

## 2. Principle and experimental setup

Figure 1 illustrates the principle of our architecture, where a single EO comb unifies the clock, time, and frequency domains. In the clock domain, the Tx-side clock reference set the comb $f _ { r } ,$ and 2 pilot comb lines deliver this reference to the Rx-side to synchronize the ADC sampling clock. In the time domain, the EO comb provides a constant channel spacing, unlike a free-running laser array. This fixed spacing preserves a deterministic timing offset relative to the reference channel after a dispersive link, regardless of seed laser frequency drifting. The architecture thus achieves accurate alignment of the sampling phases across all WDM channels. In the frequency domain, the LO comb inherits the same $f _ { r } ,$ so all signal-LO pairs share the same relative phase evolution. Carrier frequency and phase recovery can therefore be recovered from a pilot and shared across all channels, removing perchannel frequency/phase estimation at baud-rate sampling. Together, the 2 pilots and the comb-based architecture enable baud-rate sampling coherent-lite reception across the entire WDM system.

![](images/20351f7a3be38c01de7017fb89013402dcdd5f4e24b212ae081e17ebb89f775d.jpg)  
Fig. 1. Principle of EO comb-based baud-rate sampling coherent-lite reception across all WDM channels.

The experimental setup is shown in Fig. 2 (a). At the transmitter, a seed laser with a 1 kHz linewidth is injected into cascaded intensity and phase modulators to generate a 41-line EO comb. A low-noise frequency synthesizer sets $f _ { r }$ to 25 GHz and provides the common clock reference. A WSS flattens all comb lines and divides them into pilots and data carriers. Two central comb lines are reserved as pilots, while the remaining comb lines are filtered to retain every second comb line, forming 18 signal carriers with 50 GHz spacing. A 120 GS/s AWG (Keysight 8194A), synchronized to the common clock, generates 32 GBaud 64-QAM signals with a 0.05 roll-off factor. The signals are loaded onto the optical carriers using a single-polarization IQ modulator and a polarization-divisionmultiplexing emulator. The relative delay between the two polarization streams is tuned close to an integer number of symbols. The 18 data channels (CH -9 to -1 and CH 1 to 9) are then combined with the 2 pilots and transmitted over a 20 km SMF link. The total launch power is set to 4 dBm to reduce fiber nonlinearity.

At the receiver, pilots and data channels are separated by a WSS. To achieve clock synchronization, the 2 pilots beat at a photodiode, and a servo loop is employed to phase-lock the voltage-controlled oscillator (VCO) to the beat tone, thereby recovering fr = 25 GHz. The VCO output is frequency-divided to synchronize the sampling clock of the oscilloscope (Keysight UXR0594A), establishing a shared time base between the Tx- and Rx-side instruments. This VCO also drives the Rx-side modulators to generate an LO comb with the same fr.

To demonstrate baud-rate sampling with an asynchronously triggered laboratory oscilloscope, we simultaneously acquire the test channel CH n and a reference channel (Ref CH) that is used to determine the optimum sampling phase. Ref CH can be taken from the pilot pair (whose beat note delivers the reference clock) or from a data channel. Here we use CH -1/1 as Ref CH, limited by a single coherent receiver and only four oscilloscope analog inputs. As shown in Fig. 2 (b), CH n is received at baseband while Ref CH is shifted by 50 GHz, and both are sampled at 128 GS/s simultaneously. The optimum sampling phase is first identified from Ref CH, then a fixed delay determined by dispersion is applied to map this phase to CH n. As summarized in Fig. 2 (c), the sampled waveforms are low-pass filtered to avoid aliasing from high-frequency noise and then 1/4 down-sampled to baud-rate by retaining only the first of every four sampling points. Baud-rate DSP is subsequently performed, also shown in Fig. 2 (c). Note that the simultaneous acquisition of a reference channel is only an oscilloscopebased workaround for the lab demonstration and is not required in practical continuous data reception. Regarding the optical properties, Fig. 2 (d) shows the optical spectrum for the transmitted signals and pilots, and Fig. 2 (e) provides the spectrum of the LO comb.

![](images/0af099477493bdf39076a9f8502790b30e5a41e6d37d2bab8ec9fce8a843b769.jpg)  
Fig. 2. (a) Experimental setup. (b) Simultaneously reception of the test channel (CH n) and the frequency-shifted ref. channel (CH -1/1) that is used for sampling phase determination. (c) Baud-rate sampling and DSP stream. (d)/(e) Optical spectrum for transmitted signals / LO comb. IM/PM, intensity/phase modulator; PM-EDFA, polarization-maintaining erbium-doped fiber amplifier; WSS, wavelength selective switch; AWG, arbitrary waveform generator; PDME, polarization-division-multiplexing emulator; SMF, single-mode fiber. D dDi

## 3. Results and Discussions

We first evaluate the performance of clock synchronization. Figure 3 (a) compares the Tx-/Rx-side 25 GHz clocks. After synchronization, the phase noise power spectral densities are nearly identical for offset frequencies <200 kHz. We then examine the long-term stability of the inter-channel timing offset by monitoring two comb-based channels separated by 1 THz. As shown in Fig. 3 (b), the measured time difference fluctuation remains within ±0.9 ps over 1 hour, even after transmission over 20 km of SMF. The residual timing jitter is mainly attributed to temperature-induced slow variations in fiber dispersion. By contrast, an array of free-running lasers with ±3 GHz frequency drift [1] would lead to an inter-channel timing error of up to 16.3 ps, which is insufficiently stable to support baud-rate sampling (e.g., the symbol period is 31.25 ps for 32 GBd signals).

![](images/ee55badb837834c6c120d351d00c62018c81557b6bec2163adfdd11948c6bd72.jpg)

![](images/c3aa5a7c1ea970353d5a0245aec0f167b6e2b14311ae348df318fbd1303b8b1c.jpg)

![](images/e7ecd21b02a2b3de953fcb0aaf78d813b600bd638bab03d26466f8254d6e598a.jpg)

![](images/852c75e809b1975fa62bbd7075e2ef5f9124fcbb7c20c17800a420cd4f635a3a.jpg)

![](images/a527595dea2b4a89a61f480b63e0f9e3c126e79f93c81b4309a497d83b9c0642.jpg)

![](images/2325557a56e0ce43bc6ada953aa16c8c9fc90b24c04ab1601097796cac7f50a9.jpg)

![](images/42ec1438760d4d061fee33d31f76dda5371e22cad67fb96ce3dbddf56856a0b8.jpg)

![](images/fe590682e0a6b86993c560a9921d9e71015bbdb43c85a2f3576a0b0af3ecdf7f.jpg)  
Fig. 3. (a) Phase noise power spectral densities of the TX- and Rx-side 25 GHz clocks. (b) Time difference fluctuations in 3600 seconds between two comb-based channels apart by 1 THz. (c) SNR versus received optical power when using buad-rate sampling. (d) Stable baud-rate reception over 1 hour with a shared timing reference. (e) Carrier phase noises for reference and test channels. (f) Constellations for 32 GBd DP-64-QAM signals in CH 8. (g) SNR performance for baud-rate reception of all 18 WDM channels. (h) Capability matrix.

With the synchronized clock and stable inter-channel timing established above, we demonstrate baud-rate sampling coherent-lite reception for all 18 WDM channels. Figure 3 (c) shows the SNR versus received optical power under baud-rate sampling. The SD-FEC threshold for 64-QAM [6] is reached at -25 dBm. We further evaluate the long-term stability of baud-rate reception over a 1-hour measurement. Figure 3 (d) shows an outer channel (CH 8) maintaining a stable and high SNR without an independent timing recovery loop. This channel relies entirely on the shared time base from the reference channel. Compared to the optimum sampling phase obtained by digital scanning, the SNR penalty remains below 0.12 dB over the entire hour. Furthermore, Fig. 3 (e) illustrates consistent carrier phase noise between the reference and test channels. Figure 3 (f) presents representative constellations for 32 GBd DP-64QAM signals, revealing a clear difference between synchronized and unsynchronized states. Even a slight clock offset degrades the BER to > 10−1. Finally, we measure the baud-rate reception performance for all channels, with 15 minutes of measurement per channel. As shown in Fig. 3 (g), all channels achieve SNRs above 18.6 dB, and the variation stays within 1 dB, which is primarily driven by power fluctuations of the comb lines and the EDFAs. Figure 3 (h) provides a capability comparison, revealing that this work achieves the widest range of functions and maximum compatibility among current methods.

## 4. Conclusion

We have demonstrated baud-rate sampling coherent-lite reception across WDM superchannel. By using EO comb, we synchronize the Rx-side clock and establish a shared sampling time base with fluctuations within ±0.9 ps. 18× 384 Gb/s signals are successfully recovered under baud-rate sampling, and the SNR penalty due to sampling phase drift remains below 0.12 dB in long-term measurements. This prototype validates scalability and power-efficiency of comb-based shared timing, and sets the stage for distributed training across next-generation AI datacenters.

Acknowledgements National Natural Science Foundation of China (62501017, 62475147), Postdoctoral Fellowship Program of CPSF (GZB20250811), Beijing Natural Science Foundation (JQ24027), National Key R&D Program of China (2023YFB2906000). Reference

[1] T. Gui, et al., IEEE 802.3dj (2023).

[2] O. Vidal, et al., IEEE 802.3dj (2023).

[3] M. Zhang, et al., ACP (2023) DOI:10.1109/ACP/POEM59049.2023.10368881.

[4] M. Zhang, et al., OFC, M3E.3 (2023).

[5] Q. Hu, et al., ECOC, (2025).

DOI: 10.1109/ECOC66593.2025.11263168.

[6] M. Mazur et al., J. Lightw. Technol. 36(16), 3176 (2018).

[7] G. Tao, et al., OFC, Th4C.3 (2020).

[8] C. Zhang, et al., Nat. Commun., 15: 6621 (2024).

[9] L.Lundberg, et al., Nat. Commun., 11: 201 (2020).

[10] C. Zhang et al., Nat. Photon. 17(11), 1000-1008 (2023).