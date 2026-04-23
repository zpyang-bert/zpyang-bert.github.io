---
layout: post
title:      "Optics GPT: The First Vertically Pre-trained Foundation Model for Optics and Optical Communications"
date:       2026-04-18 12:51:52
author:     "Bert"
tags:
  - Mineru
---
Zekun Niu, 1,\* Kaida Chen, 1 Nianheng Jiang, 1 Xin Qin, 2 Xiaoli Huo, 2 Hui Chen, 3 Cheng Deng, 1 Zhixue He, 3 Junjie Li, 2 Weisheng Hu, 1 and Lilin Yi1,\*

1 State Key Laboratory of Photonics and Communications, School of Integrated Circuits (School of Information Science and Electronic Engineering), Shanghai Jiao Tong University, Shanghai, China

2 China Telecom Research Institute, State Key Laboratory of Optical Fiber and Cable Manufacture Technology, Beijing, China 3 Pengcheng Laboratory, Shenzhen, China \*zekunniu@sjtu.edu.cn, lilinyi@sjtu.edu.cn

Abstract: We present Optics GPT, the first vertically pre-trained foundation model for optics and optical communications. Through three-stage cognitive training, our 8B model outperforms GPT-4o and DeepSeek-R1 (671B) on specialized benchmarks, enabling DSP generation, accurate OSNR estimation, and autonomous fault repair with private on-premise deployment.

## 1. Introduction

Large Language Models (LLMs) have demonstrated remarkable capabilities across diverse tasks, with recent research exploring their application in optical networks for intent-based configuration [1-3], alarm log analysis [4,5], and AI-agent frameworks for optical networks [6]. However, these approaches typically rely on prompt engineering, retrieval-augmented generation (RAG), or fine-tuning of general-purpose models, which suffer from data privacy concerns and insufficient domain expertise. Embedding optical knowledge during pre-training is essential to capture the physical principles and logical constraints underlying optical systems.

In this work, we present Optics GPT# , the first vertical foundation model pre-trained from a general-purpose base model specifically for the optics domain. Through a novel three-stage progressive cognitive curriculum mirroring human expert development, our 8B model undergoes complete pre-training on massive optical corpora to internalize deep domain knowledge. To rigorously evaluate performance, we also built OptiEval# , the first comprehensive optical benchmark comprising graduate examinations and expert-crafted items across six subfields. Optics GPT achieves state-of-the-art performance, substantially outperforming ChatGPT-4o and DeepSeek-R1 [7] (671B) despite its compact scale. Experimental validation on real testbeds demonstrates three transformative capabilities: automatic nonlinear DSP code generation achieving 0.4 dB performance gain, autonomous network management with 1.48 dB OSNR improvement and 100% fault diagnosis accuracy, and field-trial OSNR prediction with 0.44 dB average error, confirming that knowledge-embedded Optics GPT holds immense potential to improve optical communication R&D.

## 2. Progressive Cognitive Training and Benchmark Evaluation of Optics GPT

The fundamental innovation of Optics GPT lies in being the first foundation model pre-trained from general-purpose base model specifically for the optics domain, rather than a general-purpose instruct model adapted through superficial fine-tuning. Optics GPT undergoes complete pre-training on massive optical corpora, enabling deep internalization of domain knowledge, where the pipeline follows a strict cognitive training (Fig. 1a), just like human learning. Stage 1 trains specific base model with the optics corpus internet data from general-purpose base model. And then the model establishes mathematical and physical foundations through undergraduate course texts, with specialized tasks forcing bidirectional translation between natural language and mathematical logic. Stage 3 exposes the model to research frontiers as a undergraduate student via millions of academic texts and high-quality code repositories in past research, teaching it to extract methodologies and convert descriptions into executable algorithms. The pre-training data includes optics, information science and physics, as shown in Fig. 1b. Optics GPT is trained from Qwen 3 with 8B parameters through the novel three-stage progressive pipeline that mirrors human expert development, requiring weeks of optimization process with 72 Ascend 910a NPUs and multi-year data curation efforts. The loss of pre-training is shown in Fig. 1c and 1d. After pre-training, the post-training pipeline is activated as shown in Fig. 1e to teach model how to solve real problems in the research.

To rigorously evaluate Optics GPT, we built OptiEval, the first comprehensive benchmark specifically designed for the optical domain (Fig. 1f). OptiEval integrates three complementary sources requiring extensive curation: (1) 169 real-world graduate entrance examination questions in optics; and (2) 5,772 designed optics testing derived from authoritative textbooks and papers, organized into six core subfields: Optical Communication, Ultrafast Optics, Optical Physics, Optical Design, Optical Computing, and Quantum Optics. This represents the first standardized, multi-faceted evaluation framework for optical AI systems, requiring thousands of person-hours in data collection, cleaning, and validation.

![](images/7be4060061e1a185cd18ad86978471b1f19b5997a5487d30dafa67f620e404a7.jpg)

<table><tr><td>Subset</td><td>Furner category</td><td>Counts</td></tr><tr><td rowspan="6">Lesigneo opocs tocing</td><td>Optical comuricaion</td><td>024</td></tr><tr><td>Urefat optica</td><td>1040</td></tr><tr><td>Opfeal physics</td><td>1901</td></tr><tr><td>Opfical Jesiyi</td><td>608</td></tr><tr><td>Optical eomputation</td><td>610</td></tr><tr><td>Quamum ogtics</td><td>1230</td></tr><tr><td>Croduate cntrance eramnaton</td><td></td><td>169</td></tr><tr><td>OgtEval</td><td>ALL</td><td>0240</td></tr></table>

<table><tr><td rowspan="2">Model</td><td colspan="7">Designed optics tasting</td><td rowspan="2">Gratuatn examination entrance</td></tr><tr><td>Cptica ptssics</td><td>Qaantum optics</td><td>Cpticar design</td><td>Utrareat agtes</td><td>Optca computation</td><td>Optcat com.</td><td>Average</td></tr><tr><td>GPT-40</td><td>78.92</td><td>74.52</td><td>80.89</td><td>77.13</td><td>80.73</td><td>83.49</td><td>76.53</td><td>60</td></tr><tr><td>OeepSeek R1 (571日)</td><td>79.19</td><td>75.00</td><td>82.2</td><td>76.31</td><td>43.0a</td><td>82.5</td><td>78.62</td><td>60.41</td></tr><tr><td>OgtcS oPT 18B</td><td>84.48</td><td>7.22</td><td>86.48</td><td>83.75</td><td>80.7</td><td>84.4</td><td>82.45</td><td>74.12</td></tr></table>

Fig. 1. Overview of technology and benchmarks. (a) Pre-training pipeline of Optics GPT. (b) Data distribution. (c) and (d) Pre-training loss. (e) Post-training pipeline. (f) OptiEval benchmark. (g) Optics GPT evaluation.

Our evaluation under zero-shot settings demonstrates that Optics GPT with 8B parameters achieves the best score of 82.45 on the designed optics testing, substantially outperforming competitors including ChatGPT-4o (76.53), and Deepseek R1 (78.52%). In the graduate entrance examination, Optics GPT achieves best score of 74.12, precisely the subfields requiring deep integration of physical principles with algorithmic thinking. Remarkably, this 8B parameter model surpasses models with orders of magnitude larger parameter counts (e.g., DeepSeek-R1 at 671B). These results validate that structured, progressive knowledge injection during pre-training produces fundamentally deeper understanding than scale alone, while the compact 8B scale enables private on-premise deployment for real-world optical network operators and researchers.

## 3. Experimental and Field-trial Application Demonstrations for Optical communications

![](images/9d5c4a4286a2f8481ab3deac8efe804c0fa76b0f5596b518edff277ec2b4fe2c.jpg)

![](images/ac0d9a4f187f8a0a6d602b0f789b6bb9c54a0dfe4e244852ab47f6a9e8a182cc.jpg)

![](images/f255377991381b78c621cfafc366bfff11eb9f2e6891b123334375806b517889.jpg)

![](images/eb875fc3b7ef13294ffefea1caafd927603ec403f0b29c6fb4fbfecef162201d.jpg)

<table><tr><td>Model</td><td>Method</td><td>Ripple of the optimized OSNR</td><td>Fault location accuracy</td></tr><tr><td>Owen BB</td><td>No Thinking</td><td>2.35 cB</td><td>25% (5/20)</td></tr><tr><td>OeepSeek R1</td><td>Trnking</td><td>1.17 c0</td><td>75% (15/20)</td></tr><tr><td>Oetics GPT</td><td>No Thinkno</td><td>0.96 cB</td><td>100% (20/20)</td></tr></table>

Fig. 2. Experiment results. (a) Schematic of the optical transmission experimental system. (b) Power spectrum density of input signal. (c) Optics GPT Q&A records of DSP generation task. (d) Q factor performance of generated DSP. (e) LLM-based automated optical network. (f) Performance of Optics GPT under different optical network tasks.

Optics GPT's deep understanding of algorithms and code enables automatic generation of deployable DSP code from natural language specifications. We validated this capability on an experimental platform supporting 60 GBaud transmission over 1600 km standard single-mode fiber with 21-channel WDM signals (Fig. 2a-2b). For the task " PMD compensation," Optics GPT generated 347 lines of executable Python code that successfully compensated polarization mode dispersion. For an end-to-end task involving experimental data collection and DSP implementation within our IFTS (Intelligent fiber transmission system) coding platform, the generated linear DSP achieved performance nearly identical to human-designed algorithms [8], while generated 1 StPS DBP algorithm with optimized nonlinear coefficients delivered 0.4 dB performance improvement (Fig. 2d). The entire program integrated directly into our hardware control pipeline without manual modification, representing true automated algorithm engineering from natural language.

Beyond code generation, Optics GPT demonstrates autonomous network management capabilities. Receiving high-level tasks such as OSNR flattening or fault diagnosis, the model interacts directly with optical equipment, capturing amplifier gains, link power information, and WSS attenuation, then analyzes the data and proposes implementation strategies (Fig. 2e). For OSNR optimization over a 640 km, 6-span link with a 21.0 dB target, where the ripple of original link OSNR is 2.44 dB. Optics GPT reduced OSNR ripple by 1.48 dB, significantly outperforming Qwen 8B (0.09 dB) and DeepSeek R1 (1.27 dB). For fault diagnosis across 20 induced faults including modulator bias drift, abnormal attenuation/gain settings, abnormal WSS settings, Optics GPT achieved 100% accuracy versus 75% for DeepSeek (Fig. 2f).

Optics GPT further exhibits remarkable capability in understanding optical network topologies for end-to-end OSNR prediction. In field-trial transmission with two services over two spans (Fig. 3a), the model processed topology descriptions, amplifier specifications, and fiber parameters to predict OSNR for proposed services (Fig. 3b). Using 235 measured OSNR values as reference data and tested on 100 samples, Optics GPT achieved an average prediction error of 0.44 dB, comparable to human-designed CNN (0.41 dB). This confirms that the model has internalized propagation equations from textbooks into genuine network insight, enabling accurate performance estimation without additional fine-tuning.

![](images/43ca8a652bcfbfde550c4e2c70128a6efc42fca24a337739c5a64df608a46a70.jpg)  
Fig. 3. Field-trial transmission system and OSNR prediction performance. (a) Field-trial optical network topologies. (b) Optics GPT Q&A records. (c) OSNR prediction performance evaluation.

## 4. Conclusion

We have demonstrated that domain expertise in LLMs requires more than fine-tuning general-purpose models, it demands fundamental knowledge injection during pre-training. Optics GPT, the first vertical foundation model pretrained from a base model specifically for optics, validates this paradigm through its novel three-stage cognitive curriculum training. This approach enables our compact 8B model to achieve what scale alone cannot: outperforming 671B-parameter general models on specialized optical tasks while maintaining deployability in security-sensitive environments. The creation of OptiEval further provides the community with the first standardized benchmark for optical AI, establishing a foundation for future advancements. Across experimental demonstrations, from autonomous DSP generation achieving 0.4 dB performance gains to fault diagnosis with 100% accuracy and OSNR prediction within 0.44 dB error, Optics GPT proves that deeply embedded optical knowledge translates directly to practical capability. This work establishes a new paradigm for vertical foundation models: by mirroring human cognitive development during pre-training, relatively compact models can achieve expert-level performance, bridging the gap between general AI capabilities and the specialized demands of scientific and engineering domains.

## 5. References

[1] C. Sun, et al., in ECOC’2024, paper Th3B.6.

[2] Y. Song, et al., IEEE Commun. Mag., 63, 90-96 (2025).

[3] Q. Qiu, et al., J. Lightw. Technol., Early Access (2025).

[4] Y. Wang, et al., J. Opt. Commun. Netw., 16, 681-694 (2024).

[5] Y. Pang, et al., J. Opt. Commun. Netw., 16, 1116-1132 (2024).

[6] Y. Zhang, et al., J. Opt. Commun. Netw., 18, A159-A178 (2026).

[7] D. Guo, et al., Nature, 645, 633-638 (2025).

[8] Z. Niu, et al., Light: Sci. Appl., 13, 188 (2024).