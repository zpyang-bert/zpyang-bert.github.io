---
layout: post
title:      "SerDes/光通信/IEEE/OIF 技术调研报告"
date:       2026-04-13 09:00:00
author:     "Bert"
tags:
  - SerDes
---
**研究员：Martin**
**日期：2026/04/13**
**状态：初稿（网络搜索受限，基于知识库）**

---

## 目录

1. [SerDes 技术综述](#1-serdes-技术综述)
2. [光通信技术综述](#2-光通信技术综述)
3. [IEEE 标准概览](#3-ieee-标准概览)
4. [OIF 规范概览](#4-oif-规范概览)

---

## 1. SerDes 技术综述

### 1.1 基本原理

**SerDes (Serializer/Deserializer)** 是一种将并行数据转换为串行数据（反之亦可）的技术，广泛应用于高速数据传输。

**核心原理：**
- **发送端 (Serializer)**：将并行总线数据转换为高速串行流
- **接收端 (Deserializer)**：将高速串行流恢复为并行数据
- **关键技术**：时钟数据恢复(CDR)、预加重(Pre-emphasis)、均衡(EQ)、噪声抑制

**主要调制技术：**
- **NRZ (Non-Return-to-Zero)**：传统不归零制，1 bit/symbol
- **PAM4 (Pulse Amplitude Modulation 4)**：四电平脉冲幅度调制，2 bits/symbol，2024-2026年主流技术
- **PAM6/PAM8**：下一代研究方向

### 1.2 架构设计

**SerDes 架构组件：**
```
┌─────────────────────────────────────────────────────────────┐
│                      SerDes 系统架构                         │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌────────┐ │
│  │  并行接口  │───▶│ Serializer │───▶│  传输通道  │───▶│       │ │
│  │ (Data I/O)│    │ (PMA/PCS) │    │(Channel) │    │       │ │
│  └──────────┘    └──────────┘    └──────────┘    │       │ │
│                                                   │       │ │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    │       │ │
│  │  并行接口  │◀───│Deserializer│◀───│  接收均衡  │◀───│       │ │
│  │ (Data I/O)│    │ (PMA/PCS) │    │ (CTLE/DFE)│    │       │ │
│  └──────────┘    └──────────┘    └──────────┘    └────────┘ │
└─────────────────────────────────────────────────────────────┘
```

**主要架构类型：**
- **TI (Texas Instruments)**：广泛用于数据中心
- **Broadcom (Brcm)**：Proprietary SerDes IP
- **Marvell**：Alaska系列
- **Intel/Fujitsu**：满足PCIE/以太网标准

### 1.3 2024-2026 最新技术进展

**高速率发展：**
| 年份 | 速率 (Gbps/lane) | 主要应用 |
|------|------------------|---------|
| 2024 | 112G | 800G/1.6T 光模块, PCIE 6.0 |
| 2025 | 224G | 3.2T 光模块, CXL 3.0 |
| 2026 | 448G (研究方向) | 未来超高速互联 |

**技术热点：**
1. **PAM4 成为主流**：56Gbaud/s → 112Gbaud/s
2. **224G SerDes**：下一代技术，IS for 1.6T/3.2T 光互连
3. **Co-packaged optics (CPO)**：光电子集成封装
4. **AI/ML 驱动**：GPU/CPU 互联推动 SerDes 速率提升

### 1.4 市场应用

**数据中心：**
- 800G/1.6T Ethernet Switch
- AI/ML 集群互联（GPU-DRAM, GPU-GPU）
- CXL (Compute Express Link) 3.0

**主要厂商：**
- Broadcom (Tomahawk, Jericho)
- Marvell (Alaska, Prestera)
- Intel/Sonic
- Nvidia (ConnectX, Mellanox)
- Cisco

### 1.5 关键资源链接

**标准组织：**
- OIF (Optical Internetworking Forum): https://www.oiforum.com
- IEEE 802.3: https://ieee802.org/3/
- PCI-SIG: https://pcisig.com/

**技术资源：**
- SerDes Essentials (Design Guide): 各大厂商IP白皮书
- Broadcom SerDes Guide
- Intel SerDes Architecture

---

## 2. 光通信技术综述

### 2.1 技术原理

**光通信基本架构：**
```
电信号 ──▶ [驱动器] ──▶ [激光器/调制器] ──▶ 光纤 ──▶ [探测器] ──▶ 电信号
                              ↓
                        [光放大器 EDFA/SOA]
```

**关键器件：**
- **发射端**：DFB激光器、EML (电吸收调制激光器)、VCSEL
- **接收端**：PIN光电二极管、APD (雪崩光电二极管)
- **调制格式**：NRZ, PAM4, QPSK, 16QAM, 64QAM

### 2.2 相干光通信 (Coherent Optics)

**相干检测原理：**
- 利用本振激光与信号光干涉
- 可同时检测振幅、相位、偏振态
- 大幅提升接收灵敏度

**数字相干处理 (DSP) 流程：**
1. 偏振分束 (PBS)
2. 90度混频 (I/Q mixing)
3. 模数转换 (ADC)
4. 均衡与恢复 (CMA, LMS)
5. 前向纠错 (FEC)

### 2.3 2024-2026 最新进展

**行业趋势：**

| 技术 | 2024 | 2025 | 2026 (预测) |
|------|------|------|-------------|
| 单波长速率 | 800G | 1.6T | 3.2T |
| 光模块封装 | QSFP-DD/OSFP | OSFP-XD | CPO (co-packaged) |
| 传输距离 | 80km (相干) | 120km+ | 200km+ |
| 调制格式 | 16QAM | 64QAM | 更高阶 |

**技术热点：**
1. **1.6T 光模块**：2025年主流，16x100G或8x200G
2. **CPO (Co-Packaged Optics)**：光引擎与交换芯片封装
3. **LPO (Linear Pluggable Optics)**：低功耗可插拔光模块
4. **IM/DD (强度调制/直接检测)**：短距离应用崛起
5. **空分复用 (SDM)**：多芯光纤、空分复用

### 2.4 主要厂商与产品

**北美厂商：**
- **Cisco (Acacia)**：相干光模块，1.6T OSFP
- **Intel (Silicon Photonics)**：硅光平台
- **Nvidia (Mellanox)**：InfiniBand 光互联
- **Marvell (Photonics)**：相干DSP

**亚太厂商：**
- **华为 (Huawei)**：光网络全套解决方案
- **中兴 (ZTE)**：光传输设备
- **海信 (Hisense)**：光模块
- **光迅 (Accelink)**：光器件
- **中际旭创 (Innolight)**：800G/1.6T 光模块

**欧洲厂商：**
- **Finisar (via II-VI)**：光器件
- **Lumentum**：相干激光器

### 2.5 关键资源链接

**行业组织：**
- OIF (Optical Internetworking Forum): https://www.oiforum.com
- IEEE 802.3 (Ethernet): https://ieee802.org/3/
- CCSA (中国通信标准化协会)
- ITU-T SG15：光网络标准

**市场研究：**
- LightCounting Market Research
- Dell'Oro Group
- Cignal AI

---

## 3. IEEE 标准概览

### 3.1 IEEE 802.3 (以太网)

**标准发展历史：**
| 标准 | 速率 | 年份 |
|------|------|------|
| 10BASE-T | 10 Mbps | 1990 |
| 100BASE-TX | 100 Mbps | 1995 |
| 1000BASE-T | 1 Gbps | 1999 |
| 10GBASE-T | 10 Gbps | 2006 |
| 25GBASE-T | 25 Gbps | 2016 |
| 40GBASE-T | 40 Gbps | 2016 |
| 100GBASE-T | 100 Gbps | 2017 |
| 200GBASE-T | 200 Gbps | 2020 |
| 400GBASE-T | 400 Gbps | 2017 |
| 800GBASE-T | 800 Gbps | 2020 |
| 1.6TBASE-T | 1.6 Tbps | 2025-2026 (制定中) |

**2024-2026 关键标准：**

1. **IEEE 802.3dj** (800G/1.6T Ethernet)
   - 定义 800Gb/s 和 1.6Tb/s Ethernet
   - 目标：2025年正式发布
   - 关键速率：200G/lane, 400G/lane

2. **IEEE 802.3df** (224G/lane Ethernet)
   - 定义下一代 224G SerDes 接口
   - 支持 1.6T/3.2T Ethernet
   - 2026-2027 预期发布

3. **IEEE 802.3ba** (40G/100G Ethernet)
   - 已发布，多通道并行

### 3.2 IEEE 802.15 (光网络相关)

- **IEEE 802.15.3**：高速 WPAN (Wirelessly Attached PAN)
- **IEEE 802.15.3c**：mmWave (60 GHz) 个人局域网
- 关注：光无线融合通信

### 3.3 其他高速接口标准

**PCI Express (PCIe)：**
- PCIe 5.0：32 GT/s (128Gbps/lane)
- PCIe 6.0：64 GT/s PAM4 (128Gbps/lane)
- PCIe 7.0：128 GT/s (2025-2026制定中)

**CXL (Compute Express Link)：**
- CXL 2.0：32 GT/s
- CXL 3.0：64 GT/s，支持1.6T带宽
- CXL 4.0：2025-2026，224G/lane

**InfiniBand：**
- HDR：200 Gbps (NDR)
- HDR100：100 Gbps
- NDR (Next Data Rate)：400 Gbps
- XDR：800 Gbps (2025)

### 3.4 关键资源链接

**标准文档：**
- IEEE 802.3 官方：https://ieee802.org/3/
- IEEE GET Program：免费获取标准草稿
- IEEE 802.3 邮件列表：stds-802-3@ieee.org

---

## 4. OIF 规范概览

### 4.1 关于 OIF

**OIF (Optical Internetworking Forum)** 是光网络行业最重要的标准组织之一，成员包括运营商、设备商、器件商。

**主要工作：**
- 制定光网络 Implementation Agreements (IA)
- 推动多厂商互操作性
- 定义物理层和链路层规范

### 4.2 CEI (Common Electrical Interface)

**CEI 规范演进：**

| 规范 | 速率 | 应用 |
|------|------|------|
| CEI-28G | 28 Gbps/lane | 100G/400G 光模块 |
| CEI-56G | 56 Gbps/lane | 400G/800G |
| CEI-112G | 112 Gbps/lane | 800G/1.6T |
| CEI-224G | 224 Gbps/lane | 1.6T/3.2T (研究) |

**CEI-112G 关键参数：**
- 速率：112 Gbps/lane NRZ 或 PAM4
- 距离：Short reach (SR) ≤ 2m, Long reach (LR) ≤ 10m
- 编码：NRZ (112G) 或 PAM4 (56Gbaud)
- 应用：QSFP-DD, OSFP 光模块

### 4.3 重要 Implementation Agreements (IA)

**1. 56G SerDes/光模块 IA：**
- 56 Gbps/lane PAM4
- 400G 短距离光模块
- 已广泛部署

**2. 112G SerDes/光模块 IA (2022-2024)：**
- 112 Gbps/lane
- 800G 可插拔光模块 (QSFP-DD800, OSFP800)
- 1.6T 技术预研

**3. 相干 Optics IA：**
- 400G/600G/800G 相干光模块
- CFP2/DCO form factor
- 短距离相干 (≤120km)

**4. FlexE (Flexible Ethernet)：**
- FlexE 1.0/2.0/3.0
- 以太网速率灵活性
- 5G传输网络应用

**5. CIA (Coherent Interface Agreement)：**
- 相干光模块电气接口
- C-COI (Coherent Common Interface)

### 4.4 OIF 2024-2025 最新动态

**重点领域：**

1. **224G SerDes 研究**
   - 推动下一代 224G/lane 规范
   - 2025-2026 预期 IA 发布

2. **CPO (Co-Packaged Optics)**
   - 光引擎与交换芯片共封装
   - 物理接口规范制定

3. **LPO (Linear Pluggable Optics)**
   - 低功耗可插拔光模块
   - Linear drive 架构

4. **800G/1.6T 光模块**
   - 16x50G → 16x100G
   - 8x100G → 8x200G

### 4.5 关键资源链接

**OIF 官方网站：**
- 主站：https://www.oiforum.com
- 技术文档：需要OIF会员或购买
- 白皮书：https://www.oiforum.com/resources/

**重要文档：**
- CEI-112G IA
- OIF-FlexE-01.0 (FlexE)
- OIF-High-Speed-Interfaces (HSI)

---

## 5. 总结与建议

### 5.1 技术趋势总结

| 领域 | 当前热点 (2024-2025) | 未来方向 (2026+) |
|------|---------------------|-----------------|
| SerDes | 112G/lane PAM4 | 224G/lane |
| 光模块 | 800G/1.6T QSFP-DD | 3.2T CPO |
| 以太网 | 800G Ethernet | 1.6T/3.2T Ethernet |
| 相干光 | 400G/800G 短距 | 1.6T+ 距离扩展 |

### 5.2 关注重点

1. **224G SerDes**：下一代高速互联基础
2. **1.6T 光模块**：2025-2026年主流
3. **CPO 技术**：光电子集成趋势
4. **AI/ML 互联**：推动高速 SerDes 需求

### 5.3 后续行动建议

- 定期关注 OIF 邮件列表和技术会议
- 跟踪 IEEE 802.3dj/df 标准进展
- 关注 Broadcom/Marvell/Nvidia 新产品发布
- 参加 OFC (Optical Fiber Communication) 会议

---

## 附录：术语表

| 缩写 | 全称 | 说明 |
|------|------|------|
| SerDes | Serializer/Deserializer | 串行器/解串器 |
| CDR | Clock Data Recovery | 时钟数据恢复 |
| PAM4 | Pulse Amplitude Modulation 4 | 四电平脉冲幅度调制 |
| EQ | Equalization | 均衡器 |
| CTLE | Continuous Time Linear Equalizer | 连续时间线性均衡 |
| DFE | Decision Feedback Equalizer | 判决反馈均衡 |
| COBO | Co-Packaged Optics | 共封装光学 |
| CPO | Co-Packaged Optics | 共封装光学 |
| LPO | Linear Pluggable Optics | 线性可插拔光模块 |
| OSFP | Octal Small Form Factor Pluggable | 八通道小型可插拔 |
| QSFP-DD | Quad Small Form Factor Pluggable Double Density | 四通道双密度QSFP |
| MSA | Multi-Source Agreement | 多源协议 |
| IA | Implementation Agreement | 实施协议 |
| FlexE | Flexible Ethernet | 灵活以太网 |
| CXL | Compute Express Link | 计算快速链接 |
| CFP | C Form-factor Pluggable | C封装可插拔 |

---

*报告完成*
*Martin - 高级研究员*
*2026/04/13*
