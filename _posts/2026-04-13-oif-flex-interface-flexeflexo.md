---
layout: post
title:      "OIF Flex Interface (FlexE/FlexO)"
date:       2026-04-13 22:11:14
author:     "Bert"
tags:
  - OIF
---
本目录存放 OIF Flex Interface 相关规范。

## FlexE 概述

FlexE (Flexible Ethernet) 是 OIF 制定的灵活以太网接口规范，实现多厂商以太网设备的互联。

### FlexE 架构
- FlexE Shim 层
- 40G/100G/200G/400G 绑定
- 子速率映射
- 通道化/非通道化

### FlexE 标准
| 版本 | 说明 |
|------|------|
| FlexE 1.0 | 基础规范 |
| FlexE 2.0 | 增强特性 |
| FlexE 3.0 | 800G 支持 |

## FlexO 概述

FlexO (Flexible Optical) 是针对光网络的灵活接口规范。

### FlexO 特性
- 绑定多路 FlexO
- 可变速率
- 适用于 DWDM 系统

## FlexE vs FlexO

| 特性 | FlexE | FlexO |
|------|-------|-------|
| 层级 | MAC 层 | PHY 层 |
| 介质 | 铜缆/光纤 | 光纤 |
| 应用 | 以太网互联 | 光网络互联 |

## 相关标签

`#oif` `#flexe` `#flexo` `#flex-interface`
