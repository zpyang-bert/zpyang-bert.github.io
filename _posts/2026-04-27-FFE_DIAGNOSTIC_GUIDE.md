---
layout: post
title:      "FFE 诊断分析指南"
date:       2026-04-27 09:00:00
author:     "Bert"
tags:
  - SerDes
  - FFE
  - Diagnostic
  - Signal Integrity
---

# FFE 诊断分析指南

## 概述

FFE (Feed-Forward Equalizer) 是一种 11 抽头的 FIR 滤波器，用于补偿 SerDes 信道损耗。本文档介绍如何通过 FFE 抽头系数判断信道状态是否健康，以及常见问题的诊断方法。

---

## 1. FFE 抽头结构

```
索引:    0      1      2      3      4      5      6      7      8      9      10
        ───    ───    ───    ───    ───    ───    ───    ───    ───    ───    ───
名称:   pre4   pre3   pre2   pre1   main   post1  post2  post3  post4  post5  post6
        ───    ───    ───    ───    ───    ───    ───    ───    ───    ───    ───
        前向预光标          主抽头          后向后光标
```

- **主抽头 (main)**: 索引 4，信道能量主体
- **前抽头 (pre)**: 索引 0-3，抵消前端反射
- **后抽头 (post)**: 索引 5-10，抵消后端反射

---

## 2. 合理的 FFE 系数特征

### 2.1 主抽头 (Main Tap)

| 指标 | 合理范围 | 说明 |
|------|----------|------|
| 幅值 | 0.3 ~ 0.98 | 过小表示衰减过大，过大表示过驱 |
| 极性 | 正值 | 负值表示相位反转 |

**判断方法**:
```python
main_tap = coeffs[4]
if not (0.3 <= abs(main_tap) <= 0.98):
    print("WARNING: Main tap out of range!")
if main_tap < 0:
    print("ALERT: Negative main tap - phase inversion!")
```

### 2.2 前后比 (Pre/Main Ratio)

Pre 抽头能量与主抽头能量的比值，反映前端反射强度。

| 指标 | 合理范围 | 说明 |
|------|----------|------|
| pre_ratio | < 40% | 超过 40% 表示前端反射严重 |

```python
pre_e = sum(c**2 for c in coeffs[:4])
main_e = coeffs[4]**2
pre_ratio = pre_e / main_e if main_e != 0 else 0

if pre_ratio >= 0.4:
    print("HIGH: Excessive pre-cursor reflection")
```

### 2.3 后前比 (Post/Main Ratio)

Post 抽头能量与主抽头能量的比值，反映后端反射强度。

| 指标 | 合理范围 | 说明 |
|------|----------|------|
| post_ratio | < 50% | 超过 50% 表示后端反射严重 |

```python
post_e = sum(c**2 for c in coeffs[5:])
main_e = coeffs[4]**2
post_ratio = post_e / main_e if main_e != 0 else 0

if post_ratio >= 0.5:
    print("HIGH: Excessive post-cursor reflection")
```

### 2.4 能量分布

总能量应主要集中在主抽头，前后抽头辅助补偿反射。

**典型健康分布**:
```
Pre:  ~5-15%
Main: ~60-80%
Post: ~15-35%
```

### 2.5 频域响应

频率响应应平滑，在低频处增益较高（信道衰减特性），不应有明显纹波或陷波。

```python
# 归一化频率 [0, 1] (Nyquist)
# 健康响应特征:
# - 单调递减趋势（信道衰减特性）
# - 无深陷波（<-20dB 需关注）
# - 高频衰减合理
```

---

## 3. 健康度评分 (Health Score)

综合多个指标计算 0-100 分的健康度评分：

| 分值 | 状态 | 说明 |
|------|------|------|
| 80-100 | EXCELLENT | 信道状态极佳 |
| 60-79 | PASS | 正常范围，可接受 |
| 40-59 | WARNING | 需关注，建议检查 |
| 0-39 | FAIL | 严重问题，需立即处理 |

**评分因素**:
- 主抽头位置和幅值
- 前后比是否超标
- 总增益是否超限
- CMA/DDLMS 收敛状态

---

## 4. 常见问题及诊断

### 4.1 主抽头过大 (> 0.98)

**可能原因**:
- 信道过短或衰减不足
- 发射端驱动过强
- 采样点靠近眼图中心

**建议**:
- 检查发射端预加重设置
- 验证信道连接是否正确

### 4.2 主抽头过小 (< 0.3)

**可能原因**:
- 信道过长，衰减过大
- 发射端功率不足
- 采样点偏离最佳位置

**建议**:
- 检查发射端幅度设置
- 验证信道完整性（连接器、线缆）
- 考虑使用更高阶的均衡

### 4.3 前抽头能量过高 (Pre/Main > 40%)

**可能原因**:
- 信道前端存在强烈反射
- PCB 走线阻抗不匹配
- 连接器阻抗突变

**建议**:
- 检查 PCB 阻抗设计
- 验证连接器安装
- 使用时域反射计(TDR)定位问题点

### 4.4 后抽头能量过高 (Post/Main > 50%)

**可能原因**:
- 信道末端反射
- 终端匹配不良
- 连接器质量差

**建议**:
- 检查终端电阻匹配
- 验证远端连接器状态
- 考虑添加预加重/去加重

### 4.5 系数震荡/不稳定

**可能原因**:
- 均衡器收敛参数不当
- 信号噪声比过低
- CDR 锁定不稳定

**建议**:
- 切换 CMA/DDLMS 算法
- 调整收敛步长
- 检查时钟恢复电路

### 4.6 CMA 未收敛

**判断标志**:
- `cma_converged = False`
- 系数长时间不稳定
- 健康度持续偏低

**建议**:
- 等待更长时间让其收敛
- 检查输入信号质量
- 验证时钟/数据恢复

### 4.7 总增益超限 (> 1.8)

**可能原因**:
- 均衡量过大
- 链路增益异常

**建议**:
- 减少均衡深度
- 检查 AFE 增益设置

---

## 5. Diagnostic Table 参数说明

| 参数 | 说明 | 正常值 |
|------|------|--------|
| Main Tap | 主抽头幅值 | 0.3 ~ 0.98 |
| Pre/Main | 前抽头/主抽头比 | < 40% |
| Post/Main | 后抽头/主抽头比 | < 50% |
| Total Gain | 均衡后总增益 | <= 1.8 |
| Health | 健康度评分 | >= 60 |
| DC Gain | 直流增益 | 取决于信道 |
| Nyquist | Nyquist频率增益 | 取决于信道 |
| Ch Loss | 信道损耗 | 取决于信道长度 |
| FFE Effort | 均衡工作量 | 反映均衡深度 |

---

## 6. 代码示例

### 完整诊断分析

```python
from serwave.ui.tabs.mv_framework.ffe_dashboard_renderers import _get_latest_coeffs

def diagnose_ffe(values, lane=0):
    """诊断 FFE 状态"""
    coeffs = _get_latest_coeffs(values)
    if not coeffs or len(coeffs) < 11:
        return {"status": "NO_DATA"}

    results = {
        "coefficients": coeffs,
        "main_tap": coeffs[4],
        "pre_ratio": sum(c**2 for c in coeffs[:4]) / max(coeffs[4]**2, 1e-10),
        "post_ratio": sum(c**2 for c in coeffs[5:]) / max(coeffs[4]**2, 1e-10),
    }

    # 判断主抽头
    main_tap = abs(coeffs[4])
    if main_tap < 0.3:
        results["main_status"] = "LOW"
    elif main_tap > 0.98:
        results["main_status"] = "HIGH"
    else:
        results["main_status"] = "OK"

    # 判断前后比
    if results["pre_ratio"] >= 0.4:
        results["pre_status"] = "HIGH"
    else:
        results["pre_status"] = "OK"

    if results["post_ratio"] >= 0.5:
        results["post_status"] = "HIGH"
    else:
        results["post_status"] = "OK"

    return results
```

---

## 7. 过度均衡 (Over EQ) 诊断

### 7.1 什么是 Over EQ

Over EQ (过度均衡) 是指 FFE 补偿量超过信道实际损耗需求的状态。FFE 本应补偿信道的频率选择性衰减（低频衰减大、高频衰减更大），但如果均衡量过大，会变成对高频的过度放大，而非补偿。

**正常均衡 vs 过度均衡**:

```
正常均衡（补偿信道衰减）:
  频率响应
    ^
    |\
    | \          __________
    |  \________/          ← 平滑衰减，无放大
    |
    +-------------------> 频率
       0    0.5    1.0 (Nyquist)

过度均衡（放大高频）:
  频率响应
    ^
    |\
    | \
    |  \____________
    |               \_____
    |                        ← 高频被放大上翘
    +-----------------------> 频率
       0    0.5    1.0 (Nyquist)
```

### 7.2 Over EQ 的时域判断标准

#### 7.2.1 主抽头过大

| 指标 | 警告阈值 | 严重阈值 | 说明 |
|------|----------|----------|------|
| Main Tap | > 0.98 | > 1.0 | 主抽头接近或超过 1.0 表示过驱 |

```python
main_tap = coeffs[4]

if main_tap > 1.0:
    print("SEVERE: Main tap > 1.0 - OVER EQ (saturated)")
elif main_tap > 0.98:
    print("WARNING: Main tap > 0.98 - approaching over EQ")
elif main_tap > 0.9:
    print("CAUTION: Main tap > 0.9 - elevated, monitor closely")
```

**主抽头 > 1.0 的含义**:
- FFE 输出信号的幅度会超过输入信号
- 任何后续链路（CTLE、DFE、ADC）可能面临饱和
- 眼图会出现畸形，边缘毛刺

#### 7.2.2 前后抽头能量过高

| 指标 | 警告阈值 | 严重阈值 |
|------|----------|----------|
| Pre/Main | > 40% | > 60% |
| Post/Main | > 50% | > 80% |

```python
pre_e = sum(c**2 for c in coeffs[:4])
main_e = coeffs[4]**2
post_e = sum(c**2 for c in coeffs[5:])
total_e = pre_e + main_e + post_e

pre_ratio = pre_e / main_e
post_ratio = post_e / main_e

# 前后抽头能量占比过高 = 过度补偿反射/高频
pre_pct = pre_e / total_e * 100
post_pct = post_e / total_e * 100

if post_pct > 40:
    print(f"OVER EQ: Post energy {post_pct:.1f}% (too high)")
if pre_pct > 20:
    print(f"OVER EQ: Pre energy {pre_pct:.1f}% (too high)")
```

**判断逻辑**:
- Pre 抽头过高 → 过度补偿前端高频衰减/反射
- Post 抽头过高 → 过度补偿后端高频衰减/反射
- 能量分布中 Main 占比应 > 60%，若 < 50% 则是明显 Over EQ

#### 7.2.3 总增益 (Total Gain) 过大

总增益是所有抽头幅值的平方和开根号，反映 FFE 对信号的总体放大程度。

| 指标 | 正常范围 | 警告阈值 | 严重阈值 |
|------|----------|----------|----------|
| Total Gain | 1.0 ~ 1.5 | > 1.8 | > 2.0 |

```python
total_gain = np.sqrt(sum(c**2 for c in coeffs))

if total_gain > 2.0:
    print(f"SEVERE OVER EQ: Total gain = {total_gain:.2f}")
elif total_gain > 1.8:
    print(f"WARNING: Total gain = {total_gain:.2f}")
```

**为什么 > 1.8 要警告**:
- 信道损耗一般不会超过 ~20dB (10x)
- FFE 总增益超过 1.8 意味着在补偿信道衰减之外还额外放大了信号
- 这通常发生在 DDLMS/CMA 收敛到错误值时

#### 7.2.4 抽头系数饱和

FFE 抽头系数的位宽有限（如 10-bit，范围 -512~+511），如果系数接近饱和值，说明均衡器在拼命放大。

```python
# 假设 10-bit 有符号: -512 ~ 511
MAX_ABS = 511

for i, tap in enumerate(coeffs):
    if abs(tap) > MAX_ABS * 0.95:  # 95% 饱和度
        print(f"OVER EQ: Tap {i} ({tap}) is {abs(tap)/MAX_ABS*100:.1f}% saturated")
```

### 7.3 Over EQ 的频域判断标准

#### 7.3.1 频率响应上翘

正常信道衰减特性：高频衰减大于低频，频率响应应**单调递减或平坦**，不应上翘。

```python
# 计算频率响应
w = np.linspace(0, np.pi, 512)
k = np.arange(len(coeffs))
h = np.exp(-1j * np.outer(w, k)) @ coeffs
mag_db = 20 * np.log10(np.abs(h) + 1e-10)

# 检查高频是否有上翘
# 比较 Nyquist (freq=1.0) vs 0.5 Nyquist (freq=0.5)
nyquist_idx = len(mag_db) - 1
half_nyquist_idx = len(mag_db) // 2

nyquist_gain = mag_db[nyquist_idx]
half_nyquist_gain = mag_db[half_nyquist_idx]

# 正常: 高频衰减更多 (nyquist_gain < half_nyquist_gain)
# Over EQ: 高频增益更高或相近 (nyquist_gain >= half_nyquist_gain)
if nyquist_gain >= half_nyquist_gain:
    print(f"OVER EQ: Freq response upward slope at Nyquist")
    print(f"  Nyquist(1.0) = {nyquist_gain:.1f} dB")
    print(f"  0.5*Nyq(0.5) = {half_nyquist_gain:.1f} dB")
```

**上翘判断标准**:
```
nyquist_gain - half_nyquist_gain > 0 dB  → 明显 Over EQ
nyquist_gain - half_nyquist_gain > -3 dB  → 警告，可能 Over EQ
nyquist_gain - half_nyquist_gain < -3 dB  → 正常
```

#### 7.3.2 Nyquist 增益异常高

Nyquist 频率（归一化频率 1.0）处的增益反映了信道最差情况的补偿需求。

| Nyquist 增益 | 状态 |
|-------------|------|
| < 0 dB | 正常（高频仍有一定衰减）|
| 0 ~ -3 dB | 轻微放大，可接受 |
| > 0 dB | Over EQ（高频被净放大）|
| > +3 dB | 严重 Over EQ |

```python
nyquist_gain_db = mag_db[-1]

if nyquist_gain_db > 3.0:
    print(f"SEVERE OVER EQ: Nyquist gain = {nyquist_gain_db:.1f} dB")
elif nyquist_gain_db > 0:
    print(f"WARNING: Nyquist gain = {nyquist_gain_db:.1f} dB (amplifying)")
```

#### 7.3.3 频率响应有峰值

正常频率响应应平滑或单调递减。如果在某个频段出现**峰值（peak）**，说明该频率被过度放大。

```python
# 检测峰值
peak_threshold = 3.0  # dB above local average
local_avg = np.convolve(mag_db, np.ones(20)/20, mode='same')
peaks = mag_db - local_avg > peak_threshold

if np.any(peaks):
    peak_freqs = freqs[peaks]
    print(f"OVER EQ: Peak detected at {peak_freqs}")
```

### 7.4 Over EQ 的能量分布判断

正常 FFE 能量分布：主抽头占主导地位（60-80%），前后抽头辅助。

**Over EQ 特征**:
```
正常:       Pre 5-15% | Main 60-80% | Post 15-35%
Over EQ:    Pre 10-20% | Main 40-60% | Post 25-45%
严重 Over:  Pre 15-30% | Main 30-50% | Post 30-50%
```

```python
def check_energy_distribution(coeffs):
    pre_e = sum(c**2 for c in coeffs[:4])
    main_e = coeffs[4]**2
    post_e = sum(c**2 for c in coeffs[5:])
    total = pre_e + main_e + post_e

    if total == 0:
        return None

    pre_pct = pre_e / total * 100
    main_pct = main_e / total * 100
    post_pct = post_e / total * 100

    issues = []
    if main_pct < 50:
        issues.append(f"Main tap energy {main_pct:.1f}% < 50% (Over EQ)")
    if pre_pct > 25:
        issues.append(f"Pre tap energy {pre_pct:.1f}% > 25% (excessive)")
    if post_pct > 45:
        issues.append(f"Post tap energy {post_pct:.1f}% > 45% (excessive)")

    return {
        "pre_pct": pre_pct,
        "main_pct": main_pct,
        "post_pct": post_pct,
        "issues": issues
    }
```

### 7.5 Over EQ 的危害

#### 7.5.1 链路层面

| 危害 | 说明 |
|------|------|
| 噪声放大 | 过度放大高频 = 放大噪声 + ISI |
| 后续级联饱和 | CTLE/DFE/ADC 饱和 |
| 眼图闭合 | 边缘模糊，抖动增大 |
| 误码率上升 | SNR 实际下降 |

#### 7.5.2 信号完整性

```
过度均衡的眼图:
      |        |        |
      |  /--\  |  /--\  |  ← 毛刺/双峰
      | /    \ | /    \ |
      |/      \|/      \|
      |        |        |
    上升沿过冲  下降沿过冲
```

#### 7.5.3 自适应算法失效

Over EQ 会导致 DDLMS/CMA 陷入局部最优或发散，无法正确收敛。

### 7.6 Over EQ 的根因

#### 7.6.1 根因分类

| 根因 | 症状 | 解决方法 |
|------|------|----------|
| 信道损耗估算过高 | DDLMS 认为需要更多补偿 | 重新校准信道模型 |
| 目标响应设置错误 | 期望的频率响应曲线不对 | 修正 Target Response |
| 步长过大 | CMA/DDLMS 收敛超调 | 减小收敛步长 |
| 训练序列不足 | 收敛精度差 | 增加训练时间 |
| 输入信号过弱 | 均衡器拼命放大 | 检查前端 AFE 增益 |
| 多径反射干扰 | 某些频率被重复补偿 | TDR 定位反射点 |

#### 7.6.2 DDLMS vs CMA 的 Over EQ 倾向

| 算法 | 特点 | Over EQ 风险 |
|------|------|-------------|
| CMA (Constant Modulus) | 盲均衡，只关注幅度 | 中等，取决于初始化 |
| DDLMS (Decision Directed) | 利用判决反馈 | 较低，但可能陷入错误锁定 |

```python
# 如果怀疑 Over EQ 是 DDLMS 锁定错误导致
# 可以尝试切换算法或重置
if use_ddlms:
    # 切换到 CMA 重收敛
    switch_to_cma()
else:
    # 切换到 DDLMS 重收敛
    switch_to_ddlms()
```

### 7.7 Over EQ 修复指南

#### 7.7.1 快速修复步骤

```
1. 检查总增益 > 1.8?
   → 是: 手动限制 FFE 增益或重置均衡器

2. 检查主抽头 > 0.98?
   → 是: 降低发射端预加重或 FFE 目标增益

3. 检查 Post/Main > 50%?
   → 是: 可能是远端反射被过度补偿，检查终端匹配

4. 检查频响 Nyquist > 0 dB?
   → 是: 降低 DDLMS 步长或切换算法重收敛
```

#### 7.7.2 分步诊断代码

```python
def diagnose_over_eq(coeffs, channel_info=None):
    """
    完整 Over EQ 诊断
    返回: {
        "is_over_eq": bool,
        "severity": "none" | "mild" | "moderate" | "severe",
        "issues": [...],
        "recommendations": [...]
    }
    """
    if not coeffs or len(coeffs) < 11:
        return {"is_over_eq": False, "issues": ["NO_DATA"]}

    main_tap = coeffs[4]
    pre_e = sum(c**2 for c in coeffs[:4])
    main_e = coeffs[4]**2
    post_e = sum(c**2 for c in coeffs[5:])
    total_e = pre_e + main_e + post_e
    total_gain = np.sqrt(total_e)

    issues = []
    severity = "none"

    # 检查1: 主抽头
    if main_tap > 1.0:
        issues.append(f"Main tap {main_tap:.4f} > 1.0 (SATURATED)")
        severity = "severe"
    elif main_tap > 0.98:
        issues.append(f"Main tap {main_tap:.4f} > 0.98 (over EQ)")
        severity = max(severity, "moderate")

    # 检查2: 总增益
    if total_gain > 2.0:
        issues.append(f"Total gain {total_gain:.2f} > 2.0 (severe)")
        severity = "severe"
    elif total_gain > 1.8:
        issues.append(f"Total gain {total_gain:.2f} > 1.8 (warning)")
        severity = max(severity, "moderate")

    # 检查3: 前后比
    pre_ratio = pre_e / main_e if main_e > 0 else 0
    post_ratio = post_e / main_e if main_e > 0 else 0
    if post_ratio > 0.8:
        issues.append(f"Post/Main {post_ratio:.1%} > 80% (severe)")
        severity = "severe"
    elif post_ratio > 0.5:
        issues.append(f"Post/Main {post_ratio:.1%} > 50% (warning)")
        severity = max(severity, "moderate")
    if pre_ratio > 0.6:
        issues.append(f"Pre/Main {pre_ratio:.1%} > 60% (severe)")
        severity = "severe"
    elif pre_ratio > 0.4:
        issues.append(f"Pre/Main {pre_ratio:.1%} > 40% (warning)")
        severity = max(severity, "moderate")

    # 检查4: 能量分布
    main_pct = main_e / total_e * 100 if total_e > 0 else 0
    if main_pct < 40:
        issues.append(f"Main energy only {main_pct:.1f}% < 40%")
        severity = max(severity, "moderate")

    # 建议
    recommendations = []
    if severity in ("moderate", "severe"):
        recommendations.append("Reduce FFE target gain")
        recommendations.append("Decrease DDLMS step size")
        recommendations.append("Check transmitter pre-emphasis settings")
    if main_tap > 0.98:
        recommendations.append("Verify channel loss estimation")
    if post_ratio > 0.5:
        recommendations.append("Check far-end termination")
        recommendations.append("Use TDR to locate reflection source")

    return {
        "is_over_eq": severity != "none",
        "severity": severity,
        "issues": issues,
        "recommendations": recommendations,
        "metrics": {
            "main_tap": main_tap,
            "total_gain": total_gain,
            "pre_ratio": pre_ratio,
            "post_ratio": post_ratio,
            "main_pct": main_pct,
        }
    }
```

---

## 8. 欠均衡 (Under EQ) 诊断

### 8.1 什么是 Under EQ

Under EQ (欠均衡) 与 Over EQ 相反，是指 FFE 对信道的补偿**不足**，高频衰减未被充分补偿，信号眼图仍然因 ISI 而严重闭合。

**正常均衡 vs 欠均衡的频域对比**:

```
正常均衡:
  频率响应
    ^
    |\
    | \
    |  \__________
    |             \_____
    +-----------------------> 频率
       0    0.5    1.0
    (低频增益高，高频适当衰减)

欠均衡:
  频率响应
    ^
    |\
    | \
    |  \__
    |      \_____________
    |                    \__
    +-------------------------> 频率
       0    0.5    1.0
    (高频处衰减过大，补偿不够)
```

### 8.2 Under EQ 的时域判断标准

#### 8.2.1 主抽头过小

| 指标 | 警告阈值 | 严重阈值 | 说明 |
|------|----------|----------|------|
| Main Tap | < 0.5 | < 0.3 | 主抽头过小 = 信道衰减大但FFE没补偿够 |

```python
main_tap = abs(coeffs[4])

if main_tap < 0.3:
    print("SEVERE: Main tap < 0.3 - UNDER EQ")
elif main_tap < 0.5:
    print("WARNING: Main tap < 0.5 - weak equalization")
```

**主抽头 < 0.5 的含义**:
- FFE 认为信道损耗很大，但抽头能量整体偏低
- 可能 FFE 未收敛或步长过小
- 信道中高频能量严重不足

#### 8.2.2 后抽头能量过低

Post 抽头能量过低意味着 FFE 几乎没有对后向 ISI 进行补偿。

| 指标 | 警告阈值 | 说明 |
|------|----------|------|
| Post/Main | < 10% | 后向补偿几乎不存在 |
| Post/Main | < 20% | 后向补偿偏弱 |

```python
post_ratio = post_e / main_e if main_e > 0 else 0

if post_ratio < 0.1:
    print("UNDER EQ: Post/Main < 10% (insufficient post-cursor compensation)")
elif post_ratio < 0.2:
    print("CAUTION: Post/Main < 20% (weak post-cursor compensation)")
```

#### 8.2.3 总增益过低

总增益过低说明 FFE 整体补偿力度不够。

| 指标 | 警告阈值 | 严重阈值 |
|------|----------|----------|
| Total Gain | < 0.8 | < 0.5 |

```python
total_gain = np.sqrt(sum(c**2 for c in coeffs))

if total_gain < 0.5:
    print(f"SEVERE UNDER EQ: Total gain = {total_gain:.2f} < 0.5")
elif total_gain < 0.8:
    print(f"WARNING: Total gain = {total_gain:.2f} < 0.8")
```

### 8.3 Under EQ 的频域判断标准

#### 8.3.1 Nyquist 增益过低

Nyquist 增益反映高频处的补偿效果，过低说明高频衰减未被补偿。

| Nyquist 增益 | 状态 |
|-------------|------|
| -5 ~ -10 dB | 正常（适度补偿） |
| -10 ~ -15 dB | 警告（补偿偏弱） |
| < -15 dB | 严重 Under EQ（高频几乎没补偿） |
| < -20 dB | 极严重（FFE 几乎失效） |

```python
nyquist_gain_db = mag_db[-1]

if nyquist_gain_db < -20:
    print(f"SEVERE UNDER EQ: Nyquist = {nyquist_gain_db:.1f} dB")
elif nyquist_gain_db < -15:
    print(f"WARNING: Nyquist = {nyquist_gain_db:.1f} dB (under EQ)")
elif nyquist_gain_db < -10:
    print(f"CAUTION: Nyquist = {nyquist_gain_db:.1f} dB")
```

#### 8.3.2 频响曲线整体偏低

正常 FFE 的频响应该在低频处有一定增益（> 0 dB），如果整体低于 0 dB，说明 FFE 变成了衰减器。

```python
dc_gain = mag_db[0]
if dc_gain < -3:
    print(f"WARNING: DC gain = {dc_gain:.1f} dB < -3 dB (FFE acting as attenuator)")
```

### 8.4 Under EQ 的危害

| 危害 | 说明 |
|------|------|
| 眼图高度不足 | 高频衰减导致信号幅度下降 |
| ISI 严重 | 前后符号干扰未被消除 |
| 误码率上升 | 信号幅度低于噪声容限 |
| 抖动增大 | 采样点附近的 ISI 导致时间偏移 |
| CDR 失锁 | 眼图闭合导致时钟恢复困难 |

### 8.5 Under EQ 的根因

| 根因 | 症状 | 解决方法 |
|------|------|----------|
| 信道过长 | 损耗超出 FFE 补偿能力 | 增加 CTLE 增益或启用 DFE |
| FFE 抽头数不足 | 11-tap 无法覆盖 ISI 范围 | 增加抽头数或改用更高阶均衡 |
| 收敛步长过小 | 系数长时间停留在较小值 | 增大步长或重新初始化 |
| 训练序列不足 | 算法未充分学习信道 | 增加训练时间 |
| CTLE 未开启/增益不足 | 前置补偿缺失 | 启用/增加 CTLE 增益 |
| 输入信号过强 | FFE 认为不需要补偿 | 检查发射端幅度 |
| DDLMS 错误锁定到局部最优 | 系数停留在次优解 | 重置或切换 CMA |

### 8.6 Under EQ 修复指南

```
1. 检查 Total Gain < 0.8?
   → 是: 增大 FFE 目标增益或步长

2. 检查 Nyquist < -15 dB?
   → 是: 启用 CTLE 或增加 CTLE 高频增益

3. 检查 Post/Main < 10%?
   → 是: 增加后抽头权重或检查信道模型

4. 检查 CMA/DDLMS 是否已收敛?
   → 否: 增加训练时间或重置算法

5. 检查是否启用 CTLE?
   → 否: 启用 CTLE，让 FFE 只处理残余 ISI
```

### 8.7 Over EQ vs Under EQ 快速区分

| 特征 | Over EQ | Under EQ |
|------|---------|----------|
| Main Tap | > 0.98 | < 0.5 |
| Total Gain | > 1.8 | < 0.8 |
| Post/Main | > 50% | < 10% |
| Nyquist 增益 | > 0 dB (上翘) | < -15 dB |
| 眼图表现 | 过冲/双峰 | 高度不足/模糊 |
| 噪声 | 被放大 | 相对可控 |
| 常见原因 | 步长过大/信道短 | 信道长/CTLE不足 |

---

## 9. FFE / CTLE / DFE 协同均衡链

### 9.1 接收端均衡链路结构

高速 SerDes 接收端的典型均衡链路如下：

```
输入信号
    │
    ▼
┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
│  CTLE   │───→│  FFE    │───→│  DFE    │───→│  CDR    │
│(连续时间│    │(前向均衡│    │(判决反馈│    │(时钟恢复│
│ 线性均衡)│    │  FIR)   │    │ 均衡)   │    │        │
└─────────┘    └─────────┘    └─────────┘    └─────────┘
    │              │              │
    ▼              ▼              ▼
 高频提升       前后 ISI       后向 ISI
 粗补偿        精细补偿        噪声不放大
```

### 9.2 各模块分工

#### CTLE (Continuous Time Linear Equalizer)

| 属性 | 说明 |
|------|------|
| 类型 | 模拟/连续时间 |
| 功能 | 高频提升，粗补偿信道高频衰减 |
| 优点 | 不放大噪声（针对信号），无时延 |
| 缺点 | 无法精确补偿，可能过补偿 |
| 典型增益 | 6 ~ 15 dB @ Nyquist |

**CTLE 与 FFE 的关系**:
- CTLE 负责"粗活"：补偿信道主要的频率选择性衰减
- FFE 负责"细活"：补偿 CTLE 未能消除的残余 ISI
- 如果 FFE 总增益很高 (> 1.5)，说明 CTLE 补偿不足
- 理想状态：CTLE 补偿 70% 的高频损耗，FFE 补偿剩余的 30%

#### FFE (Feed-Forward Equalizer)

| 属性 | 说明 |
|------|------|
| 类型 | 离散时间 FIR 滤波器 |
| 功能 | 消除前向和后向 ISI |
| 优点 | 可同时处理前后 ISI，自适应 |
| 缺点 | 会放大噪声（高频噪声被一起放大） |
| 典型抽头 | 5 ~ 15 抽头 |

#### DFE (Decision Feedback Equalizer)

| 属性 | 说明 |
|------|------|
| 类型 | 离散时间 IIR/反馈滤波器 |
| 功能 | 消除后向 ISI |
| 优点 | **不放大噪声**（使用判决后的干净信号） |
| 缺点 | 有误码传播风险，不能消除前向 ISI |
| 典型抽头 | 1 ~ 5 抽头 |

### 9.3 理想的分工状态

```
信道损耗:  高频衰减 15 dB

CTLE 补偿:   10 dB  (约 2/3)
FFE 补偿:     3 dB  (约 1/5)
DFE 补偿:     2 dB  (约 1/7)
─────────────────────────────
总补偿:      15 dB

此时 FFE 的系数特征:
  - Main Tap: ~0.7 (适中)
  - Post/Main: ~25% (适度补偿后向 ISI)
  - Total Gain: ~1.2 (不需要拼命放大)
```

### 9.4 不均衡链路的诊断

#### CTLE 不足，FFE 拼命补偿

```
症状:
  - CTLE 增益设置过低或未开启
  - FFE Total Gain > 1.5
  - FFE Main Tap > 0.9
  - FFE Post/Main > 40%

原因:
  - CTLE 没有分担足够的补偿工作
  - FFE 被迫承担所有高频补偿 + ISI 消除

修复:
  - 增加 CTLE 高频增益
  - 开启 CTLE 的 peaking 模式
  - 重新分配补偿责任
```

#### FFE 过度工作，DFE 闲置

```
症状:
  - FFE Post/Main > 50%
  - DFE 抽头几乎为 0
  - 噪声被 FFE 过度放大

原因:
  - DFE 未启用或抽头数不足
  - 后向 ISI 全部由 FFE 承担

修复:
  - 启用 DFE，分担后向 ISI
  - 适当降低 FFE 的后抽头能量
  - 让 DFE 处理主要的 post-cursor ISI
```

#### CTLE 过补偿，FFE 反向补偿

```
症状:
  - CTLE 增益设置过高
  - FFE 前抽头为负值（反相补偿）
  - 频域响应出现峰值后急剧下降

原因:
  - CTLE 过度提升高频
  - FFE 被迫反向衰减来平衡

修复:
  - 降低 CTLE 增益
  - 重新校准 CTLE 的零点/极点
```

### 9.5 联合诊断方法

```python
def diagnose_equalizer_chain(ctle_gain_db, ffe_coeffs, dfe_coeffs):
    """
    诊断整个均衡链的健康状态
    """
    ffe_gain = np.sqrt(sum(c**2 for c in ffe_coeffs))
    ffe_post_ratio = sum(c**2 for c in ffe_coeffs[5:]) / max(ffe_coeffs[4]**2, 1e-10)
    dfe_energy = sum(c**2 for c in dfe_coeffs)

    issues = []

    # CTLE 检查
    if ctle_gain_db < 6:
        issues.append("CTLE gain too low (< 6 dB)")
    elif ctle_gain_db > 18:
        issues.append("CTLE gain too high (> 18 dB)")

    # FFE 检查
    if ffe_gain > 1.5:
        issues.append(f"FFE overworked (gain={ffe_gain:.2f})")
    elif ffe_gain < 0.6:
        issues.append(f"FFE underworked (gain={ffe_gain:.2f})")

    # FFE vs DFE 分工检查
    if ffe_post_ratio > 0.5 and dfe_energy < 0.1:
        issues.append("FFE doing DFE's job - enable DFE")

    return {
        "ctle_gain": ctle_gain_db,
        "ffe_gain": ffe_gain,
        "dfe_energy": dfe_energy,
        "issues": issues
    }
```

---

## 10. 按信道长度分类的参考阈值

### 10.1 分类标准

不同长度的 PCB 走线或线缆具有不同的信道特性，FFE 的合理范围也不同。

| 类别 | 长度 | 典型场景 | 信道损耗 @ Nyquist |
|------|------|----------|-------------------|
| 超短距 | < 3 cm | 芯片内互联 | < 5 dB |
| 短距 | 3 ~ 10 cm | 背板近端 | 5 ~ 10 dB |
| 中距 | 10 ~ 25 cm | 背板中端 | 10 ~ 20 dB |
| 长距 | 25 ~ 50 cm | 背板远端/线缆 | 20 ~ 30 dB |
| 超长距 | > 50 cm | 有源线缆/AOC | > 30 dB |

### 10.2 各长度对应的 FFE 参考值

#### 超短距 (< 3 cm)

| 指标 | 正常范围 | 说明 |
|------|----------|------|
| Main Tap | 0.85 ~ 0.98 | 信道衰减很小 |
| Post/Main | 5% ~ 15% | 几乎没有后向 ISI |
| Pre/Main | < 10% | 前端反射可忽略 |
| Total Gain | 0.9 ~ 1.2 | 接近直通 |
| Nyquist Gain | -3 ~ +2 dB | 可能有轻微过补偿 |

**诊断要点**:
- 如果 Post/Main > 25%，可能是连接器反射而非信道损耗
- 如果 Main < 0.7，检查是否误配置为长距模式

#### 短距 (3 ~ 10 cm)

| 指标 | 正常范围 | 说明 |
|------|----------|------|
| Main Tap | 0.7 ~ 0.9 | 轻微衰减 |
| Post/Main | 10% ~ 25% | 轻度后向 ISI |
| Pre/Main | 10% ~ 25% | 轻度前端反射 |
| Total Gain | 1.0 ~ 1.4 | 适度补偿 |
| Nyquist Gain | -8 ~ -2 dB | 适度高频补偿 |

**诊断要点**:
- 如果 Total Gain > 1.5，检查 CTLE 是否开启
- 如果 Post/Main > 40%，可能是阻抗不连续

#### 中距 (10 ~ 25 cm)

| 指标 | 正常范围 | 说明 |
|------|----------|------|
| Main Tap | 0.5 ~ 0.75 | 明显衰减 |
| Post/Main | 20% ~ 40% | 中度后向 ISI |
| Pre/Main | 15% ~ 30% | 中度前端反射 |
| Total Gain | 1.2 ~ 1.6 | 较大补偿 |
| Nyquist Gain | -12 ~ -6 dB | 较大高频补偿 |

**诊断要点**:
- 这是最常见的场景，FFE 工作负载适中
- 如果 Main < 0.5，考虑启用 DFE
- 如果 Post/Main > 50%，检查终端匹配

#### 长距 (25 ~ 50 cm)

| 指标 | 正常范围 | 说明 |
|------|----------|------|
| Main Tap | 0.35 ~ 0.6 | 严重衰减 |
| Post/Main | 30% ~ 50% | 严重后向 ISI |
| Pre/Main | 20% ~ 35% | 明显前端反射 |
| Total Gain | 1.3 ~ 1.7 | 大补偿 |
| Nyquist Gain | -18 ~ -10 dB | 大高频补偿 |

**诊断要点**:
- 通常需要 CTLE + FFE + DFE 联合工作
- 如果 FFE Total Gain > 1.8，增加 CTLE 增益
- 如果 DFE 未启用，BER 会很高
- 注意检查 Over EQ（长距信道容易被过度补偿）

#### 超长距 (> 50 cm)

| 指标 | 正常范围 | 说明 |
|------|----------|------|
| Main Tap | 0.3 ~ 0.5 | 极严重衰减 |
| Post/Main | 35% ~ 55% | 极严重 ISI |
| Pre/Main | 25% ~ 40% | 明显反射 |
| Total Gain | 1.4 ~ 1.8 | 接近极限 |
| Nyquist Gain | -20 ~ -12 dB | 接近补偿极限 |

**诊断要点**:
- 必须使用 CTLE + FFE + DFE
- FFE 可能接近能力极限
- 考虑使用有源线缆或重定时器
- 密切监控 Over EQ（> 1.8 即警告）

### 10.3 快速参考表

| 指标 | 超短距 | 短距 | 中距 | 长距 | 超长距 |
|------|--------|------|------|------|--------|
| Main Tap | 0.85-0.98 | 0.7-0.9 | 0.5-0.75 | 0.35-0.6 | 0.3-0.5 |
| Post/Main | 5-15% | 10-25% | 20-40% | 30-50% | 35-55% |
| Total Gain | 0.9-1.2 | 1.0-1.4 | 1.2-1.6 | 1.3-1.7 | 1.4-1.8 |
| Nyquist | -3~+2dB | -8~-2dB | -12~-6dB | -18~-10dB | -20~-12dB |
| 需要 DFE | 否 | 可选 | 推荐 | 必须 | 必须 |
| 需要 CTLE | 可选 | 推荐 | 必须 | 必须 | 必须 |

---

## 11. 物理层指标映射

### 11.1 FFE 系数与 ISI (符号间干扰)

ISI 是由信道的记忆效应导致的相邻符号重叠。FFE 的目标就是消除 ISI。

#### ISI 量化方法

**峰值失真 (Peak Distortion)**:
```
ISI_peak = sum(|c_i| for i != main) / |c_main|
```

**均方根失真 (RMS Distortion)**:
```
ISI_rms = sqrt(sum(c_i^2 for i != main)) / |c_main|
```

| ISI 指标 | 可接受 | 警告 | 严重 |
|----------|--------|------|------|
| ISI_peak | < 0.3 | 0.3 ~ 0.5 | > 0.5 |
| ISI_rms | < 0.2 | 0.2 ~ 0.35 | > 0.35 |

```python
def compute_isi(coeffs, main_idx=4):
    """从 FFE 系数计算 ISI"""
    main = abs(coeffs[main_idx])
    if main < 1e-10:
        return {"peak": float('inf'), "rms": float('inf')}

    others = [abs(c) for i, c in enumerate(coeffs) if i != main_idx]
    peak = sum(others) / main
    rms = np.sqrt(sum(c**2 for c in others)) / main

    return {
        "peak": peak,
        "rms": rms,
        "status": "GOOD" if peak < 0.3 else "WARN" if peak < 0.5 else "BAD"
    }
```

#### ISI 与眼图的关系

```
无 ISI 的眼图:          有 ISI 的眼图:
    ───┐   ┌───           ───┐   ┌───
       │   │                  ╲   ╱
       │   │                   │ │
       │   │                   │ │
    ───┘   └───              ─┘   └──
    
    眼图完全睁开          眼图闭合/模糊
```

- ISI_peak < 0.3: 眼图高度良好 (> 70%)
- ISI_peak 0.3-0.5: 眼图高度中等 (40-70%)
- ISI_peak > 0.5: 眼图严重闭合 (< 40%)

### 11.2 FFE 系数与 Jitter (抖动)

#### 抖动来源分析

FFE 系数与抖动的关系：

| FFE 特征 | 对应的抖动类型 | 说明 |
|----------|---------------|------|
| Post/Main > 50% | Data-Dependent Jitter (DDJ) | 后向 ISI 导致边沿偏移 |
| Pre/Main > 40% | DDJ (pre-cursor) | 前向 ISI 导致边沿偏移 |
| 系数剧烈震荡 | Random Jitter (RJ) | 均衡不稳定导致随机偏移 |
| Over EQ (Main > 0.98) | Deterministic Jitter (DJ) | 过冲导致边沿提前/延后 |
| Under EQ (Main < 0.5) | DDJ + RJ | 眼图闭合导致采样点偏移 |

#### 抖动估算

```python
def estimate_jitter_from_ffe(coeffs):
    """
    从 FFE 系数估算抖动贡献
    返回: {'ddj_ps': float, 'rj_ps': float, 'total_ps': float}
    """
    main = abs(coeffs[4])
    pre_e = sum(c**2 for c in coeffs[:4])
    post_e = sum(c**2 for c in coeffs[5:])

    # DDJ 与前后 ISI 能量成正比
    # 假设 UI = 1 ps 为单位
    ddj_ps = np.sqrt(pre_e + post_e) * 100  # 粗略估算

    # RJ 与系数变化率相关（这里简化处理）
    rj_ps = 0.5  # 固定基线

    total_ps = np.sqrt(ddj_ps**2 + rj_ps**2)

    return {
        "ddj_ps": ddj_ps,
        "rj_ps": rj_ps,
        "total_ps": total_ps
    }
```

**抖动与误码率的关系**:
```
BER ≈ 0.5 * erfc(Q / sqrt(2))
Q = (眼图高度 / 2) / (噪声 + 抖动贡献)
```

当抖动增大时，有效眼图宽度减小，采样窗口变窄。

### 11.3 FFE 系数与 BER (误码率)

#### SNR 估算

FFE 对 SNR 的影响是双刃剑：
- **消除 ISI** → 提高 SNR
- **放大噪声** → 降低 SNR (尤其是 Over EQ 时)

```python
def estimate_snr_from_ffe(coeffs, snr_before_db, is_over_eq=False):
    """
    估算 FFE 后的 SNR
    """
    total_gain = np.sqrt(sum(c**2 for c in coeffs))

    # FFE 放大噪声: 噪声功率增加 gain^2 倍
    noise_increase_db = 20 * np.log10(total_gain)

    # ISI 消除带来的改善 (简化模型)
    isi_improvement_db = 3.0  # 典型值

    if is_over_eq:
        # Over EQ 时噪声放大更严重
        noise_increase_db += 3.0
        isi_improvement_db -= 1.5

    snr_after_db = snr_before_db - noise_increase_db + isi_improvement_db

    return snr_after_db
```

#### BER 估算

| SNR (dB) | 近似 BER | 状态 |
|----------|----------|------|
| > 20 | < 1e-12 | 极好 |
| 15 ~ 20 | 1e-9 ~ 1e-12 | 良好 |
| 12 ~ 15 | 1e-6 ~ 1e-9 | 可接受 |
| 10 ~ 12 | 1e-4 ~ 1e-6 | 警告 |
| < 10 | > 1e-4 | 严重 |

#### FFE 状态与 BER 的对应

| FFE 状态 | 典型 BER | 说明 |
|----------|----------|------|
| 健康 | < 1e-12 | 所有指标正常 |
| Under EQ | 1e-6 ~ 1e-9 | ISI 未消除 |
| Over EQ | 1e-4 ~ 1e-7 | 噪声被放大 |
| 未收敛 | > 1e-3 | 系数不稳定 |
| 震荡 | 1e-3 ~ 1e-5 | 抖动大 |

### 11.4 眼图质量评估

#### 从 FFE 系数预测眼图

```python
def predict_eye_quality(coeffs):
    """
    基于 FFE 系数预测眼图质量指标
    """
    main = abs(coeffs[4])
    total_gain = np.sqrt(sum(c**2 for c in coeffs))
    post_ratio = sum(c**2 for c in coeffs[5:]) / max(coeffs[4]**2, 1e-10)
    pre_ratio = sum(c**2 for c in coeffs[:4]) / max(coeffs[4]**2, 1e-10)

    # 眼图高度估算 (归一化)
    # 健康: ~0.7-1.0, 警告: ~0.4-0.7, 严重: < 0.4
    eye_height = main / total_gain if total_gain > 0 else 0

    # 眼图宽度估算 (受 ISI 影响)
    # ISI 越大，眼图宽度越窄
    isi_total = pre_ratio + post_ratio
    eye_width = max(0, 1.0 - isi_total * 0.5)

    # 综合质量
    if eye_height > 0.7 and eye_width > 0.7:
        quality = "GOOD"
    elif eye_height > 0.4 and eye_width > 0.4:
        quality = "FAIR"
    else:
        quality = "POOR"

    return {
        "eye_height": eye_height,
        "eye_width": eye_width,
        "quality": quality
    }
```

---

## 12. Tx FFE vs Rx FFE

### 12.1 基本概念

| 属性 | Tx FFE (发射端) | Rx FFE (接收端) |
|------|-----------------|-----------------|
| 别名 | 预加重 (Pre-emphasis) | 接收均衡 (Rx Equalization) |
| 位置 | 发射端芯片 | 接收端芯片 |
| 实现方式 | 模拟电路/数字 | 模拟 ADC + 数字 FIR |
| 信号基础 | 数字码流 | ADC 采样值 |

### 12.2 Tx FFE (预加重)

#### 工作原理

Tx FFE 在发射端对信号进行**预失真**，提前增强高频分量，以抵消信道的高频衰减。

```
原始信号:      ┌──┐  ┌──┐    ┌──┐
               │  │  │  │    │  │
            ───┘  └──┘  └────┘  └───
            
预加重后:      ┌┐    ┌┐      ┌┐
              ││    ││      ││
            ──┘└────┘└──────┘└────
            
            ↑ 上升沿/下降沿被增强
            
经信道后:      ┌──┐  ┌──┐    ┌──┐
               │  │  │  │    │  │
            ───┘  └──┘  └────┘  └───
            
            ↑ 经信道衰减后恢复平坦
```

#### Tx FFE 的优缺点

| 优点 | 缺点 |
|------|------|
| 不放大接收端噪声 | 降低信号摆幅（峰值功率受限） |
| 实现简单，功耗低 | 无法自适应信道变化 |
| 无收敛问题 | 会引入额外的 EMI |
| 无时延 | 固定抽头，灵活性差 |

#### Tx FFE 的典型配置

```python
# 常见的 Tx FFE 抽头配置 (3-tap)
tx_taps = {
    "pre_cursor": -0.1,    # 预光标（去加重）
    "main_cursor": 0.8,    # 主抽头
    "post_cursor": -0.1,   # 后光标（去加重）
}

# 判断 Tx FFE 是否合适的标准:
# 1. 发射端眼图满足模板要求
# 2. 接收端眼图张开度 > 30%
# 3. 总功率不超过规范限制
```

### 12.3 Rx FFE (接收均衡)

#### 工作原理

Rx FFE 在接收端对 ADC 采样后的数字信号进行滤波，补偿信道失真。

```
发射信号 ──→ 信道 ──→ 接收端
                          │
                          ▼
                      ┌─────────┐
                      │   CTLE  │
                      └────┬────┘
                           │
                           ▼
                      ┌─────────┐
                      │   ADC   │
                      └────┬────┘
                           │
                           ▼
                      ┌─────────┐
                      │  Rx FFE │──→ 消除 ISI
                      └────┬────┘
                           │
                           ▼
                      ┌─────────┐
                      │   DFE   │──→ 进一步消除后向 ISI
                      └────┬────┘
                           │
                           ▼
                      判决器 (Slicer)
```

#### Rx FFE 的优缺点

| 优点 | 缺点 |
|------|------|
| 可自适应信道变化 | 会放大噪声 |
| 可同时处理前后 ISI | 需要 ADC，功耗较高 |
| 抽头数可配置 | 有收敛时间 |
| 灵活性高 | 增加接收端延迟 |

### 12.4 Tx FFE 与 Rx FFE 的对比

| 对比项 | Tx FFE | Rx FFE |
|--------|--------|--------|
| 噪声影响 | 不放大噪声 | 放大噪声 |
| 功耗 | 低 | 高（需要 ADC + DSP） |
| 灵活性 | 低（固定或有限配置） | 高（自适应） |
| 信号摆幅 | 降低（预加重消耗功率） | 不影响发射端 |
| 适用场景 | 短距/固定信道 | 长距/变化信道 |
| 典型抽头 | 2-4 | 5-15 |
| 收敛 | 无需收敛 | 需要训练收敛 |

### 12.5 联合使用策略

#### 场景 1: 短距固定信道

```
推荐: 仅 Tx FFE
原因:
  - 信道固定，不需要自适应
  - 功耗敏感
  - 噪声放大不是问题（SNR 高）

配置:
  Tx FFE: main=0.85, pre=-0.05, post=-0.1
  Rx FFE: 关闭或 minimal (main=0.95)
```

#### 场景 2: 中距变化信道

```
推荐: Tx FFE (轻度) + Rx FFE (自适应)
原因:
  - Tx FFE 做粗补偿，不浪费功率
  - Rx FFE 做细调，适应信道变化

配置:
  Tx FFE: main=0.9, pre=-0.02, post=-0.08
  Rx FFE: 11-tap, 自适应
```

#### 场景 3: 长距/恶劣信道

```
推荐: Tx FFE + CTLE + Rx FFE + DFE
原因:
  - 需要多层补偿
  - 功耗不是主要问题，性能优先

配置:
  Tx FFE: main=0.8, pre=-0.05, post=-0.15
  CTLE: 高频增益 12 dB
  Rx FFE: 11-tap, 自适应
  DFE: 3-5 tap
```

### 12.6 诊断 Tx/Rx FFE 分工是否合理

```python
def diagnose_tx_rx_balance(tx_coeffs, rx_coeffs, channel_loss_db):
    """
    诊断 Tx FFE 和 Rx FFE 的分工是否合理
    """
    tx_main = abs(tx_coeffs.get("main", 1.0))
    rx_gain = np.sqrt(sum(c**2 for c in rx_coeffs))

    issues = []

    # 信道短但 Rx FFE 工作量大
    if channel_loss_db < 10 and rx_gain > 1.3:
        issues.append("Rx FFE overworking for short channel - increase Tx pre-emphasis")

    # 信道长但 Tx FFE 设置保守
    if channel_loss_db > 20 and tx_main > 0.85:
        issues.append("Tx FFE too weak for long channel - increase post-cursor")

    # Rx FFE 增益过高（Over EQ 风险）
    if rx_gain > 1.8:
        issues.append("Rx FFE gain too high - reduce and let DFE handle more")

    return {
        "tx_main": tx_main,
        "rx_gain": rx_gain,
        "issues": issues
    }
```

### 12.7 常见误区

| 误区 | 正确做法 |
|------|----------|
| "Tx FFE 越强越好" | Tx FFE 过强会降低信号摆幅，反而恶化 SNR |
| "Rx FFE 可以完全替代 Tx FFE" | 长距时 Rx FFE 噪声放大严重，需要 Tx FFE 分担 |
| "关闭 Tx FFE 省电" | 长距时 Rx FFE 被迫 Over EQ，总功耗更高 |
| "Tx FFE 固定一种配置" | 不同信道需要不同预加重，应可配置 |

---

## 13. 快速检查清单

### 基础检查
- [ ] 主抽头在 0.3 ~ 0.98 范围内
- [ ] 主抽头 < 0.98（避免 Over EQ）
- [ ] 主抽头 > 0.3（避免 Under EQ）
- [ ] Pre/Main < 40%
- [ ] Post/Main < 50%
- [ ] Total Gain < 1.8
- [ ] Total Gain > 0.8
- [ ] 健康度评分 >= 60
- [ ] CMA/DDLMS 已收敛
- [ ] 系数无剧烈震荡

### Over EQ 检查
- [ ] 频域响应**单调递减或平坦**，无上翘
- [ ] Nyquist 增益 < 0 dB（或在可接受范围内）
- [ ] 能量分布 Main 占比 > 50%

### Under EQ 检查
- [ ] Nyquist 增益 > -15 dB（或根据信道长度调整）
- [ ] Post/Main > 10%（有后向补偿）
- [ ] DC 增益 > -3 dB

### 协同均衡检查
- [ ] CTLE 已开启且增益合理（6-18 dB）
- [ ] FFE 未承担全部补偿工作（Total Gain < 1.5 为佳）
- [ ] 长距信道已启用 DFE
- [ ] Tx FFE 和 Rx FFE 分工合理

### 物理层指标检查
- [ ] ISI_peak < 0.5
- [ ] 估算抖动在可接受范围
- [ ] 估算 SNR > 12 dB（对应 BER < 1e-6）
- [ ] 预测眼图质量不是 POOR
