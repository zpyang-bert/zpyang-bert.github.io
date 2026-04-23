---
layout: post
title:      "SerDes/oDSP 论文学习笔记"
date:       2026-04-15 09:00:00
author:     "Bert"
tags:
  - Fundamentals
  - Paper
  - SerDes
---
**整理时间**：2026/04/15
**负责人**：Martin（高级研究员）
**状态**：待深入学习

---

## 文档列表与分类

| 文件名 | 主题领域 | 技术关键词 |
|--------|----------|------------|
| 面向100G_400GbE...传输链路关键技术研究与实现_展永政.pdf | 光传输 | 100G/400GbE, 传输链路 |
| 应用于高速SerDes的时钟数据恢复电路的设计研究_曹启富.pdf | CDR | 时钟数据恢复, 电路设计 |
| 高速直调直检光传输系统均衡算法研究.pdf | 均衡 | 直调直检, 光传输, 均衡算法 |
| 光纤通信系统中MLSE均衡器的性能分析及优化.pdf | 均衡 | MLSE, 光纤通信, 性能优化 |
| 2014_Survey_FEC.pdf | FEC | 前向纠错, 综述 |
| 高速光通信接收机前端与时钟数据恢复电路研究与实现.pdf | CDR/接收机 | 光接收机, 前端电路, CDR |
| DPLL Modeling.pptx | 时钟 | DPLL, 建模 |
| LPO_serdes_oDSP.pdf | LPO/oDSP | Linear Pluggable Optics |
| PAM4 oDSP原理介绍.PPTX | PAM4 | oDSP原理 |
| PAM4 oDSP原理介绍.pdf | PAM4 | oDSP原理 |

---

## 重点技术分类

### 1. CDR (时钟数据恢复) - 3篇
- `应用于高速SerDes的时钟数据恢复电路的设计研究_曹启富.pdf`
- `高速光通信接收机前端与时钟数据恢复电路研究与实现.pdf`
- `DPLL Modeling.pptx`

### 2. 均衡技术 - 2篇
- `高速直调直检光传输系统均衡算法研究.pdf`
- `光纤通信系统中MLSE均衡器的性能分析及优化.pdf`

### 3. FEC (前向纠错) - 1篇
- `2014_Survey_FEC.pdf`

### 4. PAM4/oDSP - 2篇
- `PAM4 oDSP原理介绍.pdf`
- `PAM4 oDSP原理介绍.PPTX`

### 5. LPO (Linear Pluggable Optics) - 1篇
- `LPO_serdes_oDSP.pdf`

### 6. 光传输系统 - 2篇
- `面向100G_400GbE...传输链路关键技术研究与实现_展永政.pdf`
- `高速直调直检光传输系统均衡算法研究.pdf`

---

## 学习计划

### 第一阶段：CDR 基础
1. 阅读 CDR 电路设计原理
2. 理解 DPLL 建模方法
3. 整理 CDR 关键指标

### 第二阶段：均衡技术
1. MLSE 均衡器原理
2. 直调直检系统均衡算法
3. 对比不同均衡方案

### 第三阶段：调制技术
1. PAM4 调制原理
2. oDSP 处理流程
3. LPO 技术趋势

### 第四阶段：FEC 与传输
1. FEC 编解码原理
2. 100G/400GbE 传输技术
3. 光通信系统集成

---

## 待解决问题

1. PDF 阅读工具尚未配置
2. 需要可访问的 PDF 阅读环境
3. 建议：使用本地机器的 PDF 阅读器进行深入学习

---

## 相关标签

`#serdes` `#cdr` `#equalization` `#fec` `#pam4` `#odsp` `#lpo` `#optical`