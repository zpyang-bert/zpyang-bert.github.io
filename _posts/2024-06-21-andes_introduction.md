---
layout:     post
title:      "Andes Custom Extension and COPILOT Workshop培训"
date:       2024-06-21 13:47:22
author:     "Bert"
header-style: text
tags:
  - Andes
  - RISC-V
---

有缘参加`Andes`在珠海举办的`ACE-COPILOT`的技术分享培训. 以下是培训过程中的内容.

### What is ACE-COPILOT?

[`ACE`](https://www.andestech.com/en/products-solutions/andes-custom-extension/): (Andes)**A**utomated **C**ustom **E**xtension

[`COPILOT`](https://www.andestech.com/wp-content/uploads/Andes-Custom-Extension%E2%84%A2-ACE-Enables-Customers-to-Add-Application-Specific-Instructions-to-AndesCore%E2%84%A2-Processors.pdf): **C**ustom-**OP**timized **I**nstruction deve**LO**pment **T**ools 

**Features:**

+ 自定指令
  + 控制指令
  + 运算指令
+ `COPILOT` - RISC-V改装工具包, 自动生成组件
+ `ACR`/`ACP`/`ACM` (Andes Custom Register/Port/Memory)
+ `ACE_RVV`
  + 客制化`vector`
  + `VPU`  (客制化sine指令)
+ `ASP` (Andes Streaming Port)

![image-20240624090217200](/img/2024-06-21-andes_introduction/image-20240624090217200.png)

![image-20240624090733325](/img/2024-06-21-andes_introduction/image-20240624090733325.png)

**在pipeline中当decode ACE指令时, 则会运行ACE逻辑, 不会阻塞pipeline水线执行.**

### Why ACE-COPILOT

+ 工具自动化 (软件+`RTL`)

+ 降低门槛

+ 自主产权

+ 速度 time-to-market

  + `COPILOT`跑一次不超过1分钟(Andes cases)
  + 软/硬一次到位

### What ACE Can Do

+ 客制指令
  + 运算指令
  + 控制指令
+ RISC-V之外
  + `DSA`
  + `CISC`
  + `OoO`
  + `MIMD`
+ Vector data bus (Andes streaming port)
  + 化整为零(1k + 1k)
  + 不抢bus, 低延迟.
+ `ACE` pipeline 可以多条
+ `VPU`
  + `ACC-RVV` ---> `ASIC` 客制指令sine

#### MIMD Example

`ACP`: Andes Custom Port

```
Andes <------> Coprocessor

ACP: cmd/in1/in2/invalid/inready/out/ovtvalid/outready
```

Command Buffer 定制指令来处理in/out 平衡.

 ### Why Andes Streaming Port

Bus优化

Vector bus和scaler bus分开

`AX45MPV`

```
VRF         |<-1024b-> HVM
XRF <-> ASP |<-1024b + 1024b->coprocessor 
FRF         |
-------------------
|
BUS Matrix <-> DMA
		   <-> MEMORY
```

#### ASP

`ASP`是[`axi-bus`](https://zhuanlan.zhihu.com/p/646353937?utm_id=0)的精简模型

Vector Memory ---> `databus` > 85%.

### How to Use ACE/COPILOT

+ CPU `RTL`

+ CPU `ISS` (`Imperas` Simulator)
+ Compiler

`user.ace`/`user.v` --> copilot --> 自动整合上述 --> 产生cross check(UVM)环境(test cases: Extended ISS/RTL)

![image-20240624090616420](/img/2024-06-21-andes_introduction/image-20240624090616420.png)

### Cases

["TWS 方案使用Andes D25 + ACE"](https://www.andestech.com/wp-content/uploads/WEI_TWS_V5_Processors_Webinar_Final.pdf)
