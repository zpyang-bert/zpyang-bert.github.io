---
layout: post
title:      "High-Resolution Trans-Oceanic Distributed Acoustic Sensing Enabled by a Bi-Directional Sensor Implementation"
date:       2026-04-18 21:52:46
author:     "Bert"
tags:
  - Mineru
---
M. Mazur(1), N. K. Fontaine(1), R. Ryf(1), M. Karrenbach(2), K. M. McBrian(3), K. L. McLaughlin(3), B. J. Sperry(3), A. G. Butler(3), V. Kamalov(4), L. Dallachiesa(1), E. Burrows(1), D. Winter(1), H. Chen(1), J. Naik(5), K. Padmaraju(5), A. Mistry(5), D. T. Neilson(1)

(1) Nokia Bell Labs, 600 Mountain Ave., Murray Hill, NJ 07974, USA. mikael.mazur@nokia-bell-labs.com (2) Seismics Unusual, LLC, Brea, CA 92821, USA (3) Leidos Inc., Arlington, VA 22203, USA (4) Valey Kamalov LLC, Gainesville, FL 32607, USA (5) Nokia Advanced Optics, 171 Madison Ave, New York City, NY 10016, USA

Abstract: We demonstrate continuous distributed acoustic sensing over a 4400 km long undersea cable. Bi-directional operation improves the strain signal-to-noise rate by >20 dB, enabling 88000 50-m-spaced measurement points at a nominal telecom launch power. © 2026 The Author(s)

## 1. Introduction

Deep ocean monitoring is currently limited to sparse coastal installations. To bridge this gap, interest has surged in repurposing undersea telecommunication cables for real-time seismic and environmental sensing [1]. This global approach would enhance earthquake early warnings [2] and address the majority of ”grand challenges” in seismology [3]. While Distributed Acoustic Sensing (DAS) has demonstrated potential for seismic and oceanic monitoring [4], it has traditionally been limited to the first and last spans of undersea cables. We recently overcame this limitation by using a long-reach OFDR prototype, making the entire cable length accessible for sensing with sub-repeater-spacing resolution [5]. Compared to other methods such as per-span interferometry [7], it enables a 1000x improvement in spatial resolution. However, global scaling requires addressing two key hurdles: sensing power levels must be minimized to preserve telecom throughput, and the signal-to-noise ratio (SNR) must be improved to overcome the ∼40 dB loss typical of loopback couplers.

We address these challenges by demonstrating distributed strain sensing with 50-m spatial resolution over a 4,400-km undersea cable featuring about 100 submerged optical repeaters. The cable connects California to Hawaii, supporting approximately 20 channels on a 100-GHz grid. By employing two separate long-reach sensing systems, enabled by wavelength multiplexing (WDM) of narrow-band signals, we simultaneously monitor the cable in both directions at a nominal launch power of -3 dBm for a 100-GHz channel slot. The bi-directional implementation allows for overcoming SNR limitations, providing >20 dB improvement along the entire cable.√ This allows for distributed sensing with 50-m spatial resolution with a noise floor of ≈1 nε/s/ Hz at 0.2 Hz along the entire cable. We furthermore verify the performance by a detailed analysis of the 30-11-2025 M4.9 earthquake in Susanville California, about 1250 km from the cable landing station and high-resolution recording of seismic waves on the deep ocean floor. Our results demonstrate that continuous, transoceanic, sensing with sub-100-m resolution is achievable using only the power and bandwidth of a single telecom channel. This paves the way for integrating long-reach sensing into all undersea infrastructure, transforming the global subsea network into a planetary-scale instrument for real-time Earth monitoring.

![](/img/mineru_output/Th4C.7/auto/images/39a795e9e560d1517d4eb50f320985a482566d8ffae2635770e1c9dda4946b72.jpg)

![](/img/mineru_output/Th4C.7/auto/images/9ff8dc24be1569534eab1b14bf28c2bfa1889ca0813aba3d1eea9f062c486cdb.jpg)

![](/img/mineru_output/Th4C.7/auto/images/310026b1f9475d783217717811145d1440db18736a526efdf30e1623d2d96a70.jpg)

![](/img/mineru_output/Th4C.7/auto/images/8a5a57d3c254eb1853c2f35d4c6ad42e49cc99e1925e505a85d728966b09b429.jpg)  
Fig. 1: (a) Experimental setup for the bi-directional implementation. The sensing signals were combined with ASE loading using 100-GHz WDM filters.(b) Map showing the 4400-km undersea cable connecting California to Hawaii, USA. (c) Cable depth profile. More than 4000 km is at depths exceeding 4000 m. (d) Estimate of the optical signal-to-noise-ratio for various launch power from both directions. Lowest power of -3 dBm equals allocating one 100-GHz WDM channel for sensing. Correspondingly, 7 dBm equals allocating half the available power for sensing. A launch power of -3dBm was used in this experiment.

## 2. Experimental Setup

The experimental setup for the long-reach DAS system is shown in Fig. 1(a). It uses a bi-directional configuration with two long-reach OFDR systems [5]. Each system consists of a cavity-stabilized fiber laser, which is externally fed to a real-time sensing unit in a homodyne configuration. The sensing unit use a dual-polarization transmit and receive photonic integrated circuit (PIC), connected to an FPGA (AMD/Xilinx ZU48DR). The FPGA generates and detects dual-polarization chirped pulses with 250 MHz bandwidth and 67 ms pulse duration. The real-time receiver processing is split between the FPGA and GPU, which are connected via a 100-Gbit/s optical link. The system outputs all intensity, phase and polarization information in parallel, supporting a wide range of uses cases from environmental sensing to repeater monitoring. The phase-sensitive ”DAS” data outputting phase change, or strain rate, was calculated using standard DAS processing very similar to ref [9], with a tunable spatial resolution down to about 10 m.

![](/img/mineru_output/Th4C.7/auto/images/0f89b06a5cc2a65b9c419d5d8632a44a8a3bb5c6036948f22ab19f2e76df4206.jpg)

![](/img/mineru_output/Th4C.7/auto/images/6b1677a62171831b8004f86e7b075b90fe3f3e0c805121f5713abd14945d2b0c.jpg)

![](/img/mineru_output/Th4C.7/auto/images/3fa7a780041c0b4ca33e2e1e32af2bf46a1029876e6f8dc25ff8631c6302aef7.jpg)  
Fig. 2: (a) Received power, or corresponding SNR, from the bi-directional sensing system. The lowest SNR point is shifted to the center of each span. (b) Individual spectrograms for each direction and from the combined signals. Bi-directional operation clearly reduces the noise level, improving all spans with >20 dB at 100 mHz and up to 40 dB at 10 mHz. The remaining red stripes are from cable movements and not limited by noise. (c) Corresponding waterfall plot for the first 200 km, showing high SNR detection of a M4.9 earthquake about 1250 km from the cable shore. (d) Waterfall diagram for a 1-minute trace with 50-m spatial resolution 2000 km offshore California. Combining both signals overcomes the noise limitation, enabling clear tracking of seismic waves on the ocean floor, which can be used for tomographic studies of earth’s structure.

The systems were installed on a ≈4400 km long undersea cable connecting California and Hawaii, as shown in Fig. 1(b). It has about 100 submerged repeaters with a median span length around 45 km. The cable depth profile is shown in Fig. 1(c). Most of the cable is at a depth exceeding 4000 m. High-loss loopback couplers (HLLBs) [10] with about 40 dB added loss are present in each repeater, enabling backscattered light to bypass the inline isolators, as conceptually shown in Fig. 1(a). In addition, two equivalent HLLBs are inserted on the shore sides, enabling backscattered light from the first spans to be coupled into the Rx fiber. The data is stored locally and synchronized using a combination of referenced system clocks and pulse-level time-counting. We rely on a single fiber-pair implementation. The backscattered light from the CA to HI probe therefore co-propagates with HI to CA probe. To avoid interference, the two signals must be offset in wavelength. However, given the sub-GHz total signal bandwidth, both easily fit within a standard 50 or 100 GHz wavelength slot. However, due to laser availability limitations, the CA-HI system used an edge channel at 1546.92 nm and the HI-CA system used 1550.12 nm. The usable cable bandwidth was about 2 THz and the OFDR channel launch power was -3 dBm. The rest of the spectrum was filled with noise at nominal power density.

## 3. Results

Figure 1(d) shows optical SNR scans from the bi-directional implementation. The allocated power is varied between -3 dBm and +7 dBm. Equivalently, -3 dBm is the nominal launch power for the allocated 100-GHz channel. In contrast, +7 dBm corresponds to allocating 50% of the total available launch power to the sensing signal. We can observe ≈5 dB improvement when increasing the launch power to 7 dBm. These results are also in line with previous lab experiments [8]. In addition, we observe a larger roll-off in SNR for the CA to HI direction, which is due to 1546.92 nm being an edge channel with worse repeater performance. The fiber loss is about 0.2 dB/km (0.4 dB/km for backscattered light) and 5 dB therefore corresponds to 12.5 km additional reach. However, we here focus on high resolution sensing with minimal impact on telecom channels and therefore use -3 dBm launch power and the bi-directional approach to cover the entire cable instead.

The bi-directional advantage is clear in Fig. 2(a), showing the combined measured distributed intensity profile. We observe that the optical SNR crosses zero around half-way through the span, matching the results in Fig. 1(d). The measured strain rate power spectral density is shown in Fig. 2(b), showing a distinct noise level improvement along the entire cable for the bi-directional approach. Zoom-ins focusing on shore-ends together with the middle point highlights the achieved improvement. Combining both signals, we achieve a typical noise level of 1 nε/s/ Hz at 0.2 Hz, a reduction of >20 dB compared to the single-ended approach. At 0.01 Hz, the typical improvement is close to 40 dB. The residual ”red” regions, are the results of increased background noise level. For example, up until about 80 km the cable is at a water depth of < 100 m and around 3400 km the cable is traversing rocky underwater mountain train with poor coupling to the ocean floor. A waterfall plot for the first 200 km is shown in Fig. 2(c). Here we clearly see the arrival of surface waves from the 30-11-2025 M4.9 earthquake with epicenter in Susanville California, about 1250 km from the cable landing station. We note two things, first, in line with Fig. 2(b), the bi-directional approach enables high SNR sensing along the entirety of each span, despite the fact that it is after >4000 km propagation from the HI-CA system, the performance is still orders of magnitude better than for the CA-HI system alone. Secondly, we observe the varying cable coupling and background noise level from Fig. 2(b). In addition, we observe some point of strong motion such as around 165 km. Figure 2(d) shows a waterfall representation of a 1-minute duration from Fig. 2(b). Here we clearly see the low-SNR regimes from both directions, together with the stitching improvement. Following stitching, we can clearly resolve seismic coherent waves propagating on the ocean floor. These are waves in the secondary microseismic bands, originating from nonlinear pressure interaction between opposing trains of ocean waves. Monitoring and tracking of these waves can be used to perform ambient noise tomography to understand earth’s crust and layers underneath the ocean.

## 4. Conclusion

We demonstrated distributed acoustic sensing with 50-m resolution over a 4400-km undersea cable, effectively creating an array of 88,000 sensors on the ocean floor. By employing a bi-directional architecture, we achieved√ a noise floor of ≈1 nε/s/ Hz at 0.2 Hz across the entire span. This approach successfully compensates for the ≈40 dB attenuation of the loop-back couplers, delivering high SNR monitoring while consuming the optical power of only a single 100-GHz telecom channel. Our results confirm the viability of high-resolution sensing along transoceanic cables with negligible impact on the data transmission capacity. This paves the way for transforming the global subsea network into a planetary-scale instrument, illuminating the unmonitored deep ocean to revolutionize seismic monitoring and tsunami early warning systems.

## References

1. B. M. Howe et al, “SMART Cables for Observing the Global Ocean: Science and Implementation”, Front. in. Marine Science, 2019.

2. R. M. Allen and D. Melgar, “Earthquake early warning:...”, Ann. Rev. of Earth and Planetary Sci., vol. 47, no. 1, pp. 361–388, 2019.

3. T. Lay et al,, “Seismological grand challenges...”, Report to the National Science Foundation, IRIS Consortium, vol. 76, 2009.

4. E. F. Williams et al, “Distributed sensing of microseisms and teleseisms...”, Nature communications, vol. 10, no. 1, p. 5778, 2019.

5. M. Mazur et al, “Submarine Cable Deep-Ocean Observation of Mega-Thrust Earthquake and Tsunami...”, Proc. ECOC paper , 2025.

6. M. Mazur et al, “Real-Time In-Line Coherent Distributed Sensing over a Legacy Submarine Cable,”, Proc. OFC paper Th4B.8, 2024.

7. G. Marra et al, “Optical interferometry–based array of seafloor environmental sensors...”, Science 376 (6595), 2022.

8. R. Ryf et al, “Coexistence demonstration of reflective OFDR sensing and commercial transceivers...“, Proc. OFC paper M4J, 2026.

9. O. H. Waagaard et al, “Real-time low noise distributed acoustic sensing...”, OSA continuum, vol. 4, no. 2, pp. 688–701, 2021.

10. T. Otani et al, ”Fault Localization of Optical WDM Submarine Cable Networks Using Coherent-Optical...”, IEEE PTL 10(7) 1998.