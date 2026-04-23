---
layout: post
title:      "Wavelength-on-Demand Multimode and Multicore Fiber Optical Parametric Oscillators"
date:       2026-04-18 11:56:57
author:     "Bert"
tags:
  - Mineru
---
Kunhao Ji1, Muhammad I.M. Abdul Khudus1,2, Jayanta Sahu1, Ian Davidson1, Pooja Naik1, Jack Haines1, Lin Xu1, Massimiliano Guasoni1\*

1 Optoelectronics Research Centre, University of Southampton, Southampton SO17 1BJ, United Kingdom 2 Department of Physics, Faculty of Science, Universiti Malaya, 50603 Kuala Lumpur, Malaysia \*m.guasoni@soton.ac.uk

Abstract: We demonstrate the first unseeded multimode/multicore parametric oscillator platform, with wavelength selection encoded in the pump spatial state. It generates wavelengths on-demand with up to 40% per-line pump conversion and detunings to ±45 THz.

## 1. Introduction

As novel optical technologies move beyond the traditional telecom windows, driven by free-space links and by the growing practicality of new fibre-accessible bands, the ability to access previously underutilized spectral regions is becoming increasingly important [1-3]. This trend is sharpening the need for sources that combine high spectral purity with wavelength agility.

The practical requirement is rapid access to a limited set of well-defined wavelength channels (e.g. atmospheric windows and WDM grids), rather than truly continuous tunability. Supercontinuum and frequency combs can span hundreds of terahertz, but they distribute power across many lines, yielding low spectral power density and limited independent control of individual frequencies [4]. By contrast, established narrowband sources, such as tunable fiber lasers and optical parametric oscillator sources, can provide high spectral power density and narrow linewidths, yet extending their operation across multiple discrete spectral windows demands dispersion and cavity redesign and band-specific filtering and optics, making multi-window coverage and reconfiguration cumbersome[5].

In this work, we demonstrate for the first time an unseeded multimode/multicore fiber optical parametric oscillator (FOPO) platform that generates multiple high-power, wavelength-selective lines without narrowband intracavity filtering or bespoke cavity management. We have recently shown that multimode fibers (MMFs) and multicore fibers (MCFs) provide an exceptional platform for engineering complex nonlinear dynamics, enabling both new fundamental phenomena [6] and all-optical control of the spatial state [7]. Here, by selectively configuring the pump modal (or core) distribution, we activate distinct intermodal four-wave-mixing (FWM) processes, enabling either single-line or multi-line emission at well-defined wavelengths within a single resonator architecture (see e.g. Fig. 1). This approach offers three distinctive features. First, the OPO cavity boosts the average power of the generated sidebands into the hundreds-of-milliwatt to watt level, far beyond typical single-pass intermodal generation in multimode fibers [8-9]. Second, the fiber geometry can be engineered to impose specific phase-matching conditions: in a tri-core fiber, we design two target detunings (≈7 THz and ≈13.2 THz), with the latter intentionally overlapping the silica Raman gain peak to access a cooperative Raman–FWM regime with high conversion efficiency. Finally, we introduce the concept of spectral concatenation, stitching distinct intermodal parametric bands to expand the accessible set of emission lines.

![](images/c6b1577de445b5663951ac244ed683f925fecaaa6bf1c48d9a8c5af0fe144443.jpg)

![](images/c33989f6fe40c128e6860918d10c41a24b85c13a71f8558dc1794972b33a7139.jpg)

![](images/bdbb241dec3a0224d4a651057d97e2fba656414e4f57e4c3861a4d0413806d23.jpg)  
Fig. 1. (a) Illustration of wavelength-on-demand operation in multicore fibers. Distinct pump launch states across the cores select different output Stokes $( \mathrm { f _ { S 1 } } , \mathrm { f _ { S 2 } } , \mathrm { f _ { S 3 } } )$ and anti-Stokes $( \mathrm { f _ { A S 1 } } , \mathrm { f _ { A S 2 } } , \mathrm { f _ { A S 3 } } )$ lines. Moreover, with a tunable pump and switching between launch states, multiple parametric bands can be concatenated to extend wavelength coverage. (b) Experimental setup of the unseeded MCF oscillator. BM: broadband mirror; BS: beamsplitter; PBS: polarization beamsplitter; OSA: optical spectrum analyser; Delay: delay line; Block: beam block. At the far right, we show microscope images of the multicore-fiber facets fabricated and tested in this work (dual-core, tri-core, and four-core fibers).

## 2. Experimental Setup and Fiber Fabrication

Two distinct FOPO configurations are implemented for MMFs and MCFs. The MCF setup is shown in Fig. 1b; the MMF arrangement is similar. We primarily use a 1040-nm pump laser: an in-house, multi-Watt all-fiber ytterbium master-oscillator power amplifier delivering linearly polarised 0.5 ns pulses at 7.57 MHz. For seeded single-pass tests we employ a lower-power 1064-nm source delivering 2-ns pulses at 1 MHz (200 mW average power).

The pump is coupled into \~25-m fibers under test through a free-space launch stage that enables controlled excitation of selected spatial modes (MMF) or cores (MCF). In the MMF configuration, only the anti-Stokes sideband is recirculated via a fixed long-pass filter, requiring no tuning. In the MCF configuration, all wavelengths are recirculated to enable OPO operation. Stokes and anti-Stokes powers are monitored at the output ports with calibrated photodiodes and power meters. We test both commercial MMFs and in-house engineered MCFs (≈4.8 μm core diameter, ≈9.5 μm core pitch) with a core arrangement providing high birefringence. The MCFs are fabricated by stack-and-draw in the University of Southampton cleanrooms [6].

## 3. Results

In our first set of experiments, we demonstrate unseeded multimode FOPO in a commercial PM2000 polarizationmaintaining fiber (Thorlabs) pumped at 1040 nm. In Fig. 2, we compare single-pass operation (OPG) with cavity operation (OPO). For LP01y–LP11ax and LP01y–LP11bx pump launches, the single-pass gain is modest, so closing the OPO loop substantially increases the conversion efficiency. By contrast, for LP01x–LP01y pumping the singlepass gain is already high, and recirculation provides a smaller additional benefit.

The largest frequency translation reaches detunings of up to ±45 THz from the pump, corresponding to Stokes and anti-Stokes bands around \~1230 nm and \~900 nm, respectively. Even at these far detunings, the FOPO delivers up to \~4% Stokes conversion, rising to \~8% for the 1210-nm Stokes line (40.5 THz detuning). For a more moderate Stokes line near \~1072 nm (8.6 THz detuning), the conversion reaches \~27%, corresponding to \~250 mW average power per line. Importantly, operating in the normal-dispersion regime keeps the output sidebands discrete and relatively narrowband, in strong contrast to single-mode schemes operated near the zero-dispersion wavelength.

Note that increasing the coupled pump power beyond 1 W further enhances the sideband conversion efficiency. For example, in OPO operation the 1210 nm Stokes band reaches \~100 mW for \~1.3 W in-fiber pump power. However, in the current setup, further scaling is practically limited by the onset of efficient stimulated Raman scattering.

Overall, these results show that with a fixed 1040-nm pump we can efficiently generate multiple discrete wavelength lines in the near- and short-wave infrared, relevant to free-space photonics applications including communications, sensing, and imaging. Importantly, the sidebands track the pump wavelength: moving the pump to 1064 nm yields similar frequency detunings, shifting the longer-wavelength sidebands towards 1260 nm, thereby supporting fiber systems that target O-band operation.

(a)  
![](images/2bb6461697c8f6c5c2111419c821b813f2c1d45ff0c629656224fb10770b06b3.jpg)

![](images/969af4adf80de327473b3d435d4cac7c551da4dbdadf7a91f05dc863e24be7ee.jpg)

![](images/21d2d8869ed171c76b5f0f8eb81726d608b806080311b7e57e837c9b37cf8f84.jpg)

![](images/39c520c3b1f0f8e40ceea0af112742e57f70d15af7adfedf0eebc9d760e808a4.jpg)

![](images/a3b1196fde5f9b596ac51fbe65ae7821702da69f13cf14ebbfc6fbb7a2ee5963.jpg)

![](images/60387c3eaec4efcd78329c2b21c97bbf71f200d49691b20891654794b464bd0d.jpg)  
Fig. 2. Experimental results in the PM2000 fiber (a) The pump is mainly coupled to the LP01y and LP01x modes. Top: Output spectra of OPG (black) and OPO (red) for an input pump power of 1 W. The insets show the far-field intensity profiles and polarization states of the anti-Stokes (1010 nm) and Stokes sideband (1072 nm). Bottom: OPG and OPO conversion efficiency (CE, left axis) of the Stokes sideband and related output power (right axis). (b) Same as in panel a, but for a pump mainly coupled to LP01y and LP11ax (Stokes at 1210 nm and anti-Stokes sidebands at 912 nm) (c) Same as in panel a, but for a pump mainly coupled to LP01y and LP11bx (Stokes at 1230 nm, anti-Stokes at 900 nm)

Among the various multicore-fiber experiments and fabrication iterations, we focus here on the tri-core fiber (TCF) as a representative example. The TCF supports 3 modes (indicated with m₁, m₂ and m3) and was engineered to meet two wavelength targets. First, we aimed for a sideband at a detuning of \~13.2 THz, chosen to overlap with the main

Raman-gain peak of silica so that stimulated Raman scattering and intermodal four-wave mixing (FWM) can cooperatively transfer energy from the pump to the Stokes band, boosting efficiency beyond either mechanism alone [10]. Second, we targeted a further sideband at \~6.7 THz detuning. The separation between these detunings (13.2 − 6.7 = 6.5 THz) is comparable to the frequency shift between 1040 nm and 1064 nm pumps, enabling the spectralconcatenation condition: tuning the pump over 1040–1064 nm would continuously sweep the generated Stokes sideband from \~6.7 THz to \~19.9 THz detuning by sequentially activating different intermodal interactions (Fig.1a). Figure 3b reports the output spectra in OPG and OPO configurations when the pump is launched to excite all three guided modes of the fiber, so that both m₁–m₃ and m₂–m₃ interactions are driven simultaneously. Consistently with the design, two dominant sideband pairs appear near the targeted detunings of 6.7 THz and 13.2 THz. Experimentally, these occur at \~7.2 THz and \~13.0 THz, corresponding to Stokes components at 1067 nm and 1089 nm and to the associated anti-Stokes bands at 1014 nm and 996 nm, respectively. The 1067-nm Stokes sideband reaches up $t o \sim 1 0 \%$ conversion, delivering \~200 mW average power. By contrast, the 1089-nm Stokes line shows strong cavity assistance: single-pass OPG gives only modest conversion, while OPO operation boosts it to \~40%, with average power approaching 800 mW. Additional measurements and simulations confirm that the observed performance is due to the simultaneous action of Raman scattering and intermodal FWM.

Figure 3 extends these outcomes to other multicore geometries, including dual-core and four-core fibers, and to a seed-assisted operation pumped at 1064 nm. As in the case of the TCF, the fibers are engineered to achieve emission at specific wavelengths through appropriate modal excitation. These experiments illustrate the versatility of the platform, which can be implemented with different multicore architectures.

![](images/822cdcf8be093210d89e960c48253f1118218f433da4a5fff9843432880bd9ec.jpg)

![](images/50dd9eaa594ab6eead11f6ce6d6e1a7e89afa3d260e14478bc65f5a5326a9a3a.jpg)

![](images/eaae98eee10b14009283337cc028f245350642801db72b376cc95d0057457f4b.jpg)

![](images/15b45fa0082c6094e928a242bdbbe734f71aad152e3c1b5d0eca723c98d18743.jpg)

![](images/76bd621865ce735f2e0f974b1856c836068f5fa000275c5fd20fb589202bef32.jpg)

![](images/4e99b573470905c1e9ee482b93d89726358495a70d76f9a49dea58c01b952761.jpg)  
Fig. 3. Experimental results in home-made multicore fibers (a). Left: Output spectrum of OPG (black) and OPO (red) for a 1040-nm pump with power of 1.8 W and coupled to all the 3 fiber modes. Rigth: conversion efficiency and output power of the sideband generated at 1067 nm and 1089 nm. (b) Spectral measurements with a seed-assisted 1064-nm pump (100 mW power). The seeded anti-Stokes and generated Stokes are: 1038 nm → 1093 nm (pump to Stokes detuning Δf=7.3 THz); 1016 nm → 1118 nm ( Δf=13.5 THz); 994 nm → 1146 nm (Δf=20.0 THz)

## 4. Conclusion

Using multimode and multicore fibers inside an unseeded oscillator, we demonstrate discrete, wavelength-ondemand multi-line emission with up to 40% conversion per line (hundreds of milliwatts) and detunings reaching ±45 THz, while preserving narrowband peaks. Spectral selection is encoded in the pump spatial state: switching the excited mode pair or core distribution steers intermodal FWM to distinct Stokes/anti-Stokes wavelengths, enabling access to bands of interest for sensing, free-space links and emerging telecom bands, without intracavity filters or cavity retuning. Straightforward upgrades include digitally controlled pump shaping for faster switching.

## References

[1] K. Zou et al, “High-capacity free-space optical communications using …,” Nat. Commun. 13, 7662 (2022).

[2] E. Agrell et al., “Roadmap on optical communications,” J. Opt. 26, 093001 (2024)

[3] T. Hoshida et al, “Ultrawideband Systems and Networks: Beyond C + L-Band,” Proc. IEEE 110(11), 1725–1741 (2022).

[4] T. J. Kippenberg et al., “Microresonator-based optical frequency combs,” Science 332, 555–559 (2011).

[5] Y. Q. Xu and S. G. Murdoch, “High conversion efficiency fiber optical parametric oscillator,” Optics Letters 36(21), 4266–4268 (2011).

[6] K.Ji et al, “Mode attraction, rejection and control in nonlinear multimode optics, “ Nat Commun. 14, 7704 (2023).

[7] K. Ji et al., “Sub-nanosecond all-optically reconfigurable photonics in optical fibres,” Nat Commun. 16, 6665 (2025).

[8] A. Bendahmane et al., “Seeded intermodal four-wave mixing in a highly multimode fiber,” J. Opt. Soc. Am. B 35, 295–303 (2018).

[9] S.-M. M. Friis et al., “Inter-modal four-wave mixing study in a two-mode fiber,” Opt. Express 24, 30338–30351 (2016).

[10] K.Ji et al., "Unified theory of parametric and Raman scattering processes in multimode fibers:…" Photon. Res. 14, 898-908 (2026)