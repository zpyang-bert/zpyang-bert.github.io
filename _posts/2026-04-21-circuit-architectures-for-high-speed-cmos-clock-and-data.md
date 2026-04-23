---
layout: post
title:      "Circuit Architectures for High Speed CMOS Clock and Data Recovery Circuits"
date:       2026-04-21 11:02:26
author:     "Bert"
tags:
  - CDR
  - SerDes
  - Thesis
  - 深度学习
---
## 深度学习报告 | Sabareeshkumar Ravikumar | University of Illinois at Urbana-Champaign, 2015

---

## 论文概述

本论文设计了三种不同架构的CDR（时钟数据恢复）电路，在180nm CMOS工艺下实现2 Gbps数据率，从性能、功耗和面积三个维度进行对比分析。

**关键词**：CMOS CDR、高 speed 串行接口、时钟恢复、SerDes

---

## 第一章 引言

### 研究背景

![](Circuit_Architectures_HighSpeed_CMOS_CDR_Ravikumar_112p_images/img-001.jpg)

> 🔍 深度说明：
> - **研究背景**：物联网时代对低功耗、低成本高速通信接口的迫切需求，片外带宽成为计算速度提升的瓶颈
> - **核心结论**：CMOS工艺可替代传统SiGe、InP技术实现高速SerDes，且成本更低、集成度更高
> - **工程价值**：为CDR电路设计提供完整理论框架和设计指南
> - **落地注意**：CDR性能是限制串行通信系统数据率提升的关键因素

截至2013年，互联网数据总量已达4.4 ZB（1 ZB = 10^21字节），预计2020年将增长10倍。

### 数据增长趋势

![](Circuit_Architectures_HighSpeed_CMOS_CDR_Ravikumar_112p_images/img-002.jpg)

> 🔍 深度说明：
> - **研究背景**：半导体工艺持续缩小带动存储成本下降，推动数据爆炸式增长
> - **核心结论**：硬盘存储成本每两年减半，刺激更多数据产生和存储需求
> - **工程价值**：量化了存储技术发展对信息时代的基础支撑作用
> - **落地注意**：成本下降趋势不可持续，未来需更高效的带宽利用方案

### 互联网接入速度增长

![](Circuit_Architectures_HighSpeed_CMOS_CDR_Ravikumar_112p_images/img-003.jpg)

> 🔍 深度说明：
> - **研究背景**：光纤通信技术进步推动骨干网速度提升
> - **核心结论**：美国平均用户接入速度正迈入千兆比特时代（Google Fiber等）
> - **工程价值**：验证了接入网与骨干网之间存在速度差距
> - **落地注意**：最后一公里仍是带宽提升的主要瓶颈

### IO接口数据率发展趋势

![](Circuit_Architectures_HighSpeed_CMOS_CDR_Ravikumar_112p_images/img-004.jpg)

> 🔍 深度说明：
> - **研究背景**：ISSCC 2011预测显示IO signaling链路数据率每4年翻番
> - **核心结论**：芯片间通信速率增长慢于互联网速度，甚至慢于摩尔定律
> - **工程价值**：明确了高速接口领域的研究紧迫性
> - **落地注意**：高频电路设计面临更多挑战（损耗、串扰、ISI抖动）

---

## 第二章 高速串行链路概述

### 串行 vs 并行链路

![](Circuit_Architectures_HighSpeed_CMOS_CDR_Ravikumar_112p_images/img-005.jpg)

> 🔍 深度说明：
> - **研究背景**：传统并行总线（IDE、PCI、AGP）受限明显，业界转向串行接口
> - **核心结论**：在给定CMOS工艺下，存在一个链路长度阈值，超过该值后串行链路在功耗和面积上更优
> - **工程价值**：量化了从并行向串行过渡的技术经济性
> - **落地注意**：随着工艺节点缩小，串行优势愈发明显

### 背板trace结构

![](Circuit_Architectures_HighSpeed_CMOS_CDR_Ravikumar_112p_images/img-006.jpg)

> 🔍 深度说明：
> - **研究背景**：数据中心和大型路由器中使用的典型高速信号传输结构
> - **核心结论**：线卡通过连接器与背板相连，实现芯片间高速通信
> - **工程价值**：展示了实际系统级互连架构
> - **落地注意**：连接器和过孔会引入额外损耗和反射

### 背板横截面示意

![](Circuit_Architectures_HighSpeed_CMOS_CDR_Ravikumar_112p_images/img-007.jpg)

> 🔍 深度说明：
> - **研究背景**：从电磁角度理解信号完整性的物理层结构
> - **核心结论**：PCB材料（FR4）和工艺对高速信号质量有决定性影响
> - **工程价值**：帮助设计者理解信号从芯片到背板的完整路径
> - **落地注意**：层压板选择和走线设计需考虑阻抗连续性

### 信道失真分析

![](Circuit_Architectures_HighSpeed_CMOS_CDR_Ravikumar_112p_images/img-008.jpg)

> 🔍 深度说明：
> - **研究背景**：信道不完美性导致信号畸变，10 Gb/s时尤为严重
> - **核心结论**：干净的数据经过信道后产生严重ISI和幅度衰减
> - **工程价值**：揭示了接收机设计必须具备高保真采样能力
> - **落地注意**：BER需控制在10^-12量级（每万亿比特约1个错误）

### 典型SERDES系统框图

![](Circuit_Architectures_HighSpeed_CMOS_CDR_Ravikumar_112p_images/img-009.jpg)

> 🔍 深度说明：
> - **研究背景**：完整的串行通信系统包括TX、Channel、RX三大部分
> - **核心结论**：Serializer、Driver、PLL、CDR等模块协同实现高速传输
> - **工程价值**：提供了系统级架构视图
> - **落地注意**：各模块需协同设计才能确保整体性能

### 多路复用型Serializer

![](Circuit_Architectures_HighSpeed_CMOS_CDR_Ravikumar_112p_images/img-010.jpg)

> 🔍 深度说明：
> - **研究背景**：并行转串行的直接实现方式
> - **核心结论**：需要N位计数器产生2^N倍频选通信号
> - **工程价值**：概念直观，但实际应用中面临频率和功耗挑战
> - **落地注意**：N=3时，1 GHz系统时钟需8 GHz选通信号，设计困难

### 树形结构Serializer

![](Circuit_Architectures_HighSpeed_CMOS_CDR_Ravikumar_112p_images/img-011.jpg)

> 🔍 深度说明：
> - **研究背景**：解决直接多路复用结构的高频难题
> - **核心结论**：将大MUX分解为N级2:1 MUX，每级半速运行
> - **工程价值**：降低时序要求，减少动态功耗
> - **落地注意**：使用latch保持级间数据，是当前主流拓扑

### 典型PLL框图

![](Circuit_Architectures_HighSpeed_CMOS_CDR_Ravikumar_112p_images/img-012.jpg)

> 🔍 深度说明：
> - **研究背景**：PLL是产生高频低抖动时钟的核心模块
> - **核心结论**：PFD+CP+LF+VCO+Divider构成闭环相位控制系统
> - **工程价值**：为CDR提供精确时钟基准
> - **落地注意**：相位噪声和抖动是PLL关键性能指标

### 信道频率响应

![](Circuit_Architectures_HighSpeed_CMOS_CDR_Ravikumar_112p_images/img-013.jpg)

> 🔍 深度说明：
> - **研究背景**：实际背板信道的频率衰减特性
> - **核心结论**：高频衰减严重，具有明显低通特性
> - **工程价值**：指导均衡器设计
> - **落地注意**：损耗来源包括导体趋肤效应和介质损耗

### 眼图分析

![](Circuit_Architectures_HighSpeed_CMOS_CDR_Ravikumar_112p_images/img-014.jpg)

> 🔍 深度说明：
> - **研究背景**：10 Gb/s下眼图闭合程度
> - **核心结论**：信道后眼图严重恶化，需要均衡
> - **工程价值**：眼图是评估链路性能的重要可视化工具
> - **落地注意**：均衡后眼图张开度是设计目标

### 均衡后眼图

![](Circuit_Architectures_HighSpeed_CMOS_CDR_Ravikumar_112p_images/img-015.jpg)

> 🔍 深度说明：
> - **研究背景**：均衡技术可恢复部分信道损失
> - **核心结论**：CTLE和DFE可有效张开眼图
> - **工程价值**：证明了均衡技术的必要性
> - **落地注意**：均衡需权衡噪声放大和ISI消除

### CDR系统框图

![](Circuit_Architectures_HighSpeed_CMOS_CDR_Ravikumar_112p_images/img-016.jpg)

> 🔍 深度说明：
> - **研究背景**：CDR是接收端核心，负责时钟提取和数据采样
> - **核心结论**：Phase Detector + Loop Filter + VCO构成闭环跟踪系统
> - **工程价值**：框图清晰，是CDR设计的起点
> - **落地注意**：锁定时间、抖动跟踪带宽是核心设计参数

### 调制技术比较

![](Circuit_Architectures_HighSpeed_CMOS_CDR_Ravikumar_112p_images/img-017.jpg)

> 🔍 深度说明：
> - **研究背景**：不同调制方式对带宽效率的影响
> - **核心结论**：NRZ、PAM-4等技术在频谱效率上有本质差异
> - **工程价值**：为调制方案选型提供依据
> - **落地注意**：PAM-4可双倍速率但需更高SNR

### 抖动类型

![](Circuit_Architectures_HighSpeed_CMOS_CDR_Ravikumar_112p_images/img-018.jpg)

> 🔍 深度说明：
> - **研究背景**：时钟抖动对高速链路的影响
> - **核心结论**：抖动类型（DCD、Jitter等）影响系统性能
> - **工程价值**：建立抖动分析框架
> - **落地注意**：CDR必须精确跟踪和补偿抖动

---

## 第三章 CDR理论与分析

### CDR环路详细框图

![](Circuit_Architectures_HighSpeed_CMOS_CDR_Ravikumar_112p_images/img-019.jpg)

> 🔍 深度说明：
> - **研究背景**：CDR闭环工作原理的数学描述
> - **核心结论**：锁相环路的相位传递函数分析
> - **工程价值**：为环路参数设计提供理论依据
> - **落地注意**：环路带宽决定抖动跟踪能力

### 相位检测器传递特性

![](Circuit_Architectures_HighSpeed_CMOS_CDR_Ravikumar_112p_images/img-020.jpg)

> 🔍 深度说明：
> - **研究背景**：线性PD vs 二进制PD的工作特性
> - **核心结论**：线性PD有更宽工作范围但电路更复杂
> - **工程价值**：帮助选择合适的PD架构
> - **落地注意**：Hogge PD是经典线性相位检测器

### Hogge相位检测器

![](Circuit_Architectures_HighSpeed_CMOS_CDR_Ravikumar_112p_images/img-021.jpg)

> 🔍 深度说明：
> - **研究背景**：经典CDR相位检测电路
> - **核心结论**：通过XOR和DFF实现相位到脉宽转换
> - **工程价值**：广泛应用的CDR鉴相器
> - **落地注意**：存在死区和抖动容限问题

### 电荷泵电路

![](Circuit_Architectures_HighSpeed_CMOS_CDR_Ravikumar_112p_images/img-022.jpg)

> 🔍 深度说明：
> - **研究背景**：将数字鉴相脉冲转换为模拟控制电压
> - **核心结论**：CP将PFD输出泵入/抽出电荷到LF电容
> - **工程价值**：连接数字与模拟域的关键模块
> - **落地注意**：电流匹配和开关泄漏是关键设计点

### 环路滤波器

![](Circuit_Architectures_HighSpeed_CMOS_CDR_Ravikumar_112p_images/img-023.jpg)

> 🔍 深度说明：
> - **研究背景**：一阶RC滤波器实现
> - **核心结论**：简单RC滤波器提供积分功能
> - **工程价值**：为二阶环提供基础
> - **落地注意**：电阻电容取值影响环路稳定性

---

## 第四章 CDR行为级建模

### Verilog-AMS建模

本论文采用Verilog-AMS对CDR各模块进行行为级建模，包括：
- Phase Detector
- Charge Pump
- Loop Filter
- VCO

> 🔍 深度说明：
> - **研究背景**：晶体管级仿真耗时过长，行为级建模可加速设计迭代
> - **核心结论**：AMS混合信号仿真可在合理时间内验证系统功能
> - **工程价值**：缩短设计周期，提高验证覆盖率
> - **落地注意**：模型精度与仿真速度需权衡

---

## 第五章 单端CDR设计

### 单端CDR架构

![](Circuit_Architectures_HighSpeed_CMOS_CDR_Ravikumar_112p_images/img-024.jpg)

> 🔍 深度说明：
> - **研究背景**：第一种CDR实现架构
> - **核心结论**：采用静态CMOS反相器构建CDR
> - **工程价值**：面积最小，功耗最低
> - **落地注意**：噪声性能较差，适用于低速率应用

---

## 第六章 互补逻辑CDR设计

### 互补逻辑CDR架构

![](Circuit_Architectures_HighSpeed_CMOS_CDR_Ravikumar_112p_images/img-025.jpg)

> 🔍 深度说明：
> - **研究背景**：改进的单端CDR变体
> - **核心结论**：PMOS+NMOS互补驱动提高速度
> - **工程价值**：平衡速度与功耗
> - **落地注意**：设计复杂度增加

---

## 第七章 电流模式逻辑CDR设计

### CML CDR电路图

![](Circuit_Architectures_HighSpeed_CMOS_CDR_Ravikumar_112p_images/img-026.jpg)

> 🔍 深度说明：
> - **研究背景**：最高性能CDR架构
> - **核心结论**：恒定电流切换，速度最快
> - **工程价值**：适用于2 Gbps以上高速应用
> - **落地注意**：功耗较高，版图需注意匹配

### 超缓冲驱动器

![](Circuit_Architectures_HighSpeed_CMOS_CDR_Ravikumar_112p_images/img-027.jpg)

> 🔍 深度说明：
> - **研究背景**：强驱动能力需求
> - **核心结论**：多级缓冲逐级放大
> - **工程价值**：提供足够驱动强度
> - **落地注意**：延迟和功耗需优化

### Hogge PD实现

![](Circuit_Architectures_HighSpeed_CMOS_CDR_Ravikumar_112p_images/img-028.jpg)

> 🔍 深度说明：
> - **研究背景**：CML版本的Hogge PD
> - **核心结论**：高速率下的鉴相实现
> - **工程价值**：满足2 Gbps设计目标
> - **落地注意**：版图对称性影响线性度

### 主从D触发器

![](Circuit_Architectures_HighSpeed_CMOS_CDR_Ravikumar_112p_images/img-029.jpg)

> 🔍 深度说明：
> - **研究背景**：高速分频器基础单元
> - **核心结论**：CML latch实现边缘触发
> - **工程价值**：可靠的时序电路单元
> - **落地注意**：时钟馈通和寄生效应需控制

### CML Latch

![](Circuit_Architectures_HighSpeed_CMOS_CDR_Ravikumar_112p_images/img-030.jpg)

> 🔍 深度说明：
> - **研究背景**：CML电路核心存储单元
> - **核心结论**：背靠背反相器实现锁存
> - **工程价值**：高线性度鉴相器基础
> - **落地注意**：设计时需考虑静态电流

### CML XOR门

![](Circuit_Architectures_HighSpeed_CMOS_CDR_Ravikumar_112p_images/img-031.jpg)

> 🔍 深度说明：
> - **研究背景**：Hogge PD核心计算单元
> - **核心结论**：差分结构实现高速XOR
> - **工程价值**：鉴相器关键模块
> - **落地注意**：需优化晶体管尺寸

---

## 第八章 结果与对比

### 控制电压锁定过程

![](Circuit_Architectures_HighSpeed_CMOS_CDR_Ravikumar_112p_images/img-032.jpg)

> 🔍 深度说明：
> - **研究背景**：CDR上电锁定行为
> - **核心结论**：控制电压从初始值收敛到稳定值
> - **工程价值**：验证环路稳定性
> - **落地注意**：锁定时间影响系统启动

### VCO频率锁定过程

![](Circuit_Architectures_HighSpeed_CMOS_CDR_Ravikumar_112p_images/img-033.jpg)

> 🔍 深度说明：
> - **研究背景**：VCO控制电压与输出频率关系
> - **核心结论**：频率逐渐锁定到目标值
> - **工程价值**：展示PLL环路跟踪过程
> - **落地注意**：Kvco非线性影响锁定特性

### 发射机眼图

![](Circuit_Architectures_HighSpeed_CMOS_CDR_Ravikumar_112p_images/img-034.jpg)

> 🔍 深度说明：
> - **研究背景**：TX输出信号质量
> - **核心结论**：眼图张开良好
> - **工程价值**：发射机设计满足要求
> - **落地注意**：上升下降沿需均衡

### 信道输出眼图

![](Circuit_Architectures_HighSpeed_CMOS_CDR_Ravikumar_112p_images/img-035.jpg)

> 🔍 深度说明：
> - **研究背景**：信道衰减后的信号
> - **核心结论**：眼图明显闭合
> - **工程价值**：说明均衡必要性
> - **落地注意**：ISI是主要损伤来源

### CDR输出眼图

![](Circuit_Architectures_HighSpeed_CMOS_CDR_Ravikumar_112p_images/img-036.jpg)

> 🔍 深度说明：
> - **研究背景**：CDR恢复的信号质量
> - **核心结论**：眼图重新张开
> - **工程价值**：验证CDR有效工作
> - **落地注意**：抖动残余决定眼图质量

### 采样相位示意

![](Circuit_Architectures_HighSpeed_CMOS_CDR_Ravikumar_112p_images/img-037.jpg)

> 🔍 深度说明：
> - **研究背景**：CDR时钟与数据的关系
> - **核心结论**：时钟在最佳点采样数据
> - **工程价值**：展示CDR跟踪过程
> - **落地注意**：相位偏移需精确控制

---

## 三种架构对比总结

| 架构 | 功耗 | 速度 | 面积 | 适用场景 |
|------|------|------|------|----------|
| 单端CMOS | 低 | 慢 | 小 | 低速、低功耗应用 |
| 互补逻辑 | 中 | 中 | 中 | 中速应用 |
| CML | 高 | 快 | 大 | 高速（>2 Gbps）应用 |

---

## 核心结论

1. **CML架构最适合高速应用**：在2 Gbps目标速率下，CML CDR性能最优
2. **功耗与速度需权衡**：无免费午餐，设计需根据应用场景选择架构
3. **行为级建模价值**：Verilog-AMS可有效加速CDR设计验证
4. **信道均衡不可或缺**：10 Gb/s以上传输必须采用均衡技术

---

*报告生成时间：基于Circuit_Architectures_HighSpeed_CMOS_CDR_Ravikumar_112p.pdf深度分析*
