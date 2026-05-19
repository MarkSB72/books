# 第1章 AUTOSAR 支持概览

- "AUTOSAR Blockset 产品描述"（第1-2页）
- "什么是 AUTOSAR？"（第1-3页）
- "AUTOSAR 标准"（第1-6页）
- "AUTOSAR Classic 与 Adaptive 平台对比"（第1-9页）
- "在 Simulink 中建模 AUTOSAR Classic 组件及元素"（第1-18页）
- "在 Simulink 中建模 AUTOSAR Adaptive 组件及元素"（第1-23页）
- "AUTOSAR 软件组件与组合"（第1-27页）
- "AUTOSAR 工作流"（第1-29页）
- "AUTOSAR 工作流示例"（第1-31页）
- "开发 AUTOSAR 软件组件模型"（第1-32页）
- "创建表示 AUTOSAR 软件组件行为的算法模型内容"（第1-34页）
- "为 Simulink 建模环境配置 AUTOSAR 软件组件元素"（第1-36页）
- "仿真并可选生成 AUTOSAR 软件组件代码（需要 Embedded Coder）"（第1-41页）
- "开发 AUTOSAR Adaptive 软件组件模型"（第1-44页）
- "创建表示 AUTOSAR Adaptive 软件组件行为的算法模型内容"（第1-46页）
- "为 Simulink 建模环境配置 AUTOSAR Adaptive 软件组件元素"（第1-49页）
- "仿真 AUTOSAR Adaptive 软件组件并可选生成代码（需要 Embedded Coder）"（第1-53页）
- "开发 AUTOSAR 软件架构模型"（第1-56页）
- "创建 AUTOSAR 软件架构模型"（第1-57页）
- "添加 AUTOSAR 组合与组件并链接组件实现"（第1-58页）
- "在 AUTOSAR 架构中仿真组件"（第1-64页）
- "可选：生成并打包组合 ARXML 及组件代码（需要 Embedded Coder）"（第1-67页）

---

## 1.1 AUTOSAR Blockset 产品描述

**设计和仿真 AUTOSAR 软件**

AUTOSAR Blockset 提供了用于开发 AUTOSAR Classic 和 Adaptive 软件的应用程序和模块，可基于 Simulink® 模型进行开发。您可以使用 AUTOSAR Component Designer 应用程序设计 Simulink 模型并将其映射到软件组件。此外，该 Blockset 还允许您通过从 AUTOSAR XML (ARXML) 文件导入软件组件和组合描述，生成新的 Simulink 模型用于 AUTOSAR 开发。

AUTOSAR Blockset 为 AUTOSAR 库例程和基础软件（BSW）服务（包括 NVRAM 和诊断功能）提供了模块和构造。通过将 BSW 服务与您的应用软件模型一起仿真，您无需离开 Simulink 即可验证 AUTOSAR ECU 软件。

AUTOSAR Blockset 允许您在 Simulink 中创建 AUTOSAR 架构模型（需要 System Composer™）。在 AUTOSAR 架构模型中，您可以编辑软件组合、带有接口的组件、数据类型、配置文件和构造型。您可以添加仿真行为，包括 BSW 服务组件。此外，还可以通过 ARXML 文件进行软件描述的往返（导入和导出）。

AUTOSAR Blockset 支持 C 和 C++ 生产代码生成（配合 Embedded Coder®）。它已通过认证，可用于 ISO 26262 标准（配合 IEC Certification Kit）。

---

## 1.2 什么是 AUTOSAR？

**本节内容...**

- "AUTOSAR 平台"（第1-4页）
- "在 Simulink 中开发 AUTOSAR 系统"（第1-4页）

AUTOSAR（AUTomotive Open System ARchitecture，汽车开放系统架构）是一个由整车制造商、供应商以及电子、半导体和软件行业的其他公司组成的全球性开发合作组织。AUTOSAR 标准旨在实现软件标准化、复用和互操作性。

AUTOSAR 标准提供了两个平台，以支持当前和未来世代的汽车电子控制单元（ECU）：

- **AUTOSAR Classic Platform（经典平台）**——该平台支持传统车内应用，如动力总成、底盘、车身和内部电子系统。
- **AUTOSAR Adaptive Platform（自适应平台）**——该平台支持基于服务的应用，如自动驾驶、Car-to-X（车联网）、无线软件更新（OTA）以及作为物联网（IoT）一部分的车辆。

AUTOSAR Classic、AUTOSAR Adaptive 和非 AUTOSAR ECU 可在同一车辆内互操作。

有关 AUTOSAR 标准的概览，请参见 "AUTOSAR 标准"（第1-6页）。

### AUTOSAR 平台

AUTOSAR 基于其软件架构，分为两个平台：AUTOSAR Classic Platform 和 AUTOSAR Adaptive Platform。AUTOSAR Classic Platform 是针对具有硬实时和安全约束的嵌入式系统的解决方案。AUTOSAR Adaptive Platform 是针对高性能计算 ECU 的解决方案，用于构建诸如自动驾驶等故障可运行系统。

AUTOSAR Classic Platform 架构具有三个层次：

- **应用软件（Application Software）**——在称为软件组件的独立单元中提供应用实现。构建软件组件会生成符合平台规范的 AUTOSAR XML 描述和 C 代码实现模块。
- **运行时环境（Runtime Environment, RTE）**——提供应用软件与基础软件之间的通信。软件组件仅通过 RTE 与其他组件和/或基础软件模块进行通信，这使得软件组件可以独立于任何特定 ECU 和其他软件组件。
- **基础软件（Basic Software, BSW）**——提供 ECU 抽象、微控制器抽象以及服务，包括内存和诊断功能。

AUTOSAR Adaptive Platform 架构具有与 AUTOSAR Classic Platform 类似的层次，但它是一种面向服务的架构（SOA），为处理高计算密集型应用提供了基础。Adaptive Platform 支持 POSIX 操作系统。

有关 AUTOSAR 平台的更多信息，请参见 "AUTOSAR Classic 与 Adaptive 平台对比"（第1-9页）。

### 在 Simulink 中开发 AUTOSAR 系统

Simulink 原生支持 AUTOSAR 标准。在 Simulink 中开发 AUTOSAR 软件的步骤如下：

- 使用 Simulink 和 AUTOSAR Blockset 设计和仿真 AUTOSAR Classic 和 Adaptive 系统。
- 可选地，使用 System Composer 编辑 AUTOSAR 软件组合和组件的层次结构。
- 使用 Embedded Coder 生成 ARXML 描述以及用于测试和 AUTOSAR RTE 集成的生产 C 或 C++ 算法代码。

Simulink、AUTOSAR Blockset 和 Embedded Coder 支持与 AUTOSAR 架构的往返集成，如下图所示：

1. 您可以使用 AUTOSAR 创作工具（AAT）或 Simulink 创建并导出 ARXML 文件。此 ARXML 文件用于开发 AUTOSAR SWC（软件组件）。
2. 然后将 SWC 导入 Simulink 以生成模型或更新现有模型。此时可生成 C 代码，模型可进行 SIL/PIL 测试。
3. 您可导出更新后的 ARXML 文件，包括您所做的任何更改。这些文件可由 Simulink 或其他 AUTOSAR 创作工具用于更新 SWC 和未来的 ARXML 版本。

AUTOSAR Blockset 已通过认证可用于 ISO 26262 标准。可选地，使用 IEC Certification Kit 对生成的 AUTOSAR 代码进行 ISO 26262 认证。有关认证的更多信息，请参见示例 "Highway Lane Following: A Model-Based Design Example for ISO 26262:2018"（IEC Certification Kit）。

**参见**

相关示例：

- "AUTOSAR Classic 与 Adaptive 平台对比"（第1-9页）
- "在 Simulink 中建模 AUTOSAR Classic 组件及元素"（第1-18页）
- "在 Simulink 中建模 AUTOSAR Adaptive 组件及元素"（第1-23页）
- "开发 AUTOSAR 软件组件模型"（第1-32页）
- "开发 AUTOSAR Adaptive 软件组件模型"（第1-44页）
- "开发 AUTOSAR 软件架构模型"（第1-56页）

---

## 1.3 AUTOSAR 标准

Simulink 软件支持 AUTOSAR（汽车开放系统架构），这是一种开放且标准化的汽车软件架构，由三个软件层次组成：应用层（Application）、运行时环境（Run-Time Environment, RTE）和基础软件（Basic Software）。

```
                    Application（应用层）

 AUTOSAR           AUTOSAR                AUTOSAR
 Software          Software               Software
Component         Component      ...     Component

            Run-Time Environment (RTE)
            （运行时环境）

 Service           Service       ...     Service

                  Basic Software
                  （基础软件）

               Microcontroller          API
```

汽车制造商、供应商和工具开发商共同开发应用层的组件。该标准将这些组件称为 AUTOSAR 软件组件。它们与运行时环境层交互。运行时环境层实现了以下对象之间的通信：

- 应用层的各组件之间
- 基础软件层与应用层的各组件之间

基础软件层提供应用层组件使用的共享通用系统服务。

AUTOSAR 标准涉及以下方面：

- **架构**——分层软件架构将应用软件与执行平台解耦。AUTOSAR 软件组件与运行时环境之间的标准接口允许在车辆的电子控制单元（ECU）拓扑中复用或重定位组件。

  该标准定义了称为 AUTOSAR 平台的软件架构变体：Classic Platform（经典平台）和 Adaptive Platform（自适应平台）。更多信息请参见 "AUTOSAR Classic 与 Adaptive 平台对比"（第1-9页）。

- **方法论**——配置描述文件定义 ECU 之间共享的系统信息、特定 ECU 独有的系统信息以及特定 ECU 的基础软件信息。

- **基础**——AUTOSAR 平台之间共享的需求和规范，支持平台互操作性。

- **应用接口**——通过为典型汽车应用指定接口并指定软件各层之间的接口，提供标准化的交换格式。

**参见**

更多信息：

- MATLAB and Simulink for AUTOSAR
- "AUTOSAR Classic 与 Adaptive 平台对比"（第1-9页）
- "建模模式"
- "AUTOSAR 工作流"（第1-29页）

外部网站：

- AUTOSAR: Automotive Open System Architecture

---

## 1.4 AUTOSAR Classic 与 Adaptive 平台对比

AUTOSAR 标准定义了称为 AUTOSAR 平台的软件架构变体：Classic Platform (CP) 和 Adaptive Platform (AP)。

在选择使用哪个平台来设计和实现 AUTOSAR 软件组件时，请参考下表中的指导信息。

**AUTOSAR 平台对比**

| 目标或特性 | Classic Platform（经典平台） | Adaptive Platform（自适应平台） |
|---|---|---|
| 用例 | 嵌入式系统 | 高性能计算、与外部资源通信、灵活部署 |
| 编程语言 | C | C++ |
| 操作系统 | Bareboard（裸板） | POSIX |
| 实时性要求 | 硬实时 | 软实时 |
| 计算能力 | 低 | 高 |
| 通信方式 | 基于信号 | 基于事件，面向服务 |
| 安全与安保 | 支持 | 支持 |
| 动态更新 | 不可用 | 支持增量部署和运行时配置更改 |
| 标准化程度 | 高——详细规范 | 低——API 和语义层面 |
| 敏捷开发 | 否 | 是 |

### Classic Platform（经典平台）

Classic Platform 满足深度嵌入式电子控制单元（ECU）的需求，这些 ECU 根据输入信号和来自车辆网络上其他 ECU 的信息来控制电气输出信号。通常，您为特定类型的车辆设计和实现控制软件，这些软件在车辆的整个生命周期内不会改变。

软件架构的运行时环境（RTE）层负责处理应用层中 AUTOSAR 软件组件之间的通信，以及 AUTOSAR 软件组件与基础软件层提供的服务之间的通信。基础软件层包括：

- 服务，如系统服务、内存服务和通信服务
- 设备驱动
- ECU 抽象
- 微控制器抽象

```
                    Application（应用层）

  AUTOSAR          AUTOSAR                AUTOSAR
  Software         Software               Software
 Component        Component      ...     Component

          Run-time Environment (RTE)
          （运行时环境）

 Services                        ECU Abstraction
                                 （ECU 抽象）      Device Drivers
                                                  （设备驱动）

              Microcontroller Abstraction
              （微控制器抽象）

                Basic Software（基础软件）

            Embedded Control Unit (ECU)
            （嵌入式控制单元）
```

Classic Platform 使用虚拟功能总线（Virtual Functional Bus, VFB）来支持 AUTOSAR 应用软件的硬件无关开发和使用。该总线由特定 ECU 的 RTE 抽象表示组成，将架构应用层中的 AUTOSAR 软件组件与架构基础设施解耦。AUTOSAR 软件组件和总线通过专用端口进行通信。您通过将组件端口映射到系统 ECU 的 RTE 表示来配置应用。

```
                    Application（应用层）

  AUTOSAR          AUTOSAR                AUTOSAR
  Software         Software               Software
 Component        Component      ...     Component

          Virtual Functional Bus (VFB)
          （虚拟功能总线）

          Run-Time Environment (RTE)

              Mapping for Deployment
              （部署映射）

 Microcontroller  Microcontroller       Microcontroller

 AUTOSAR AUTOSAR  AUTOSAR AUTOSAR       AUTOSAR AUTOSAR
 SoftwareSoftware Software Software     Software Software
ComponentComp...  ComponentComponent   ComponentComponent
      RTE              RTE                   RTE

   Basic Software   Basic Software       Basic Software

                     Gateway（网关）
```

### Adaptive Platform（自适应平台）

Adaptive Platform 是一种分布式计算和面向服务的架构（SOA）。该平台提供高性能计算、基于消息的通信机制和灵活的软件配置，以支持诸如自动驾驶和信息娱乐系统等应用。基于此平台的软件可以：

- 满足严格的完整性和安全性要求
- 处理环境感知和行为响应规划
- 将车辆集成到外部系统的后端或基础设施中
- 应对外部系统的变化，因为您可以在车辆生命周期内更新软件

软件架构的 RTE 层包含 C++ 标准库。它支持应用层中 AUTOSAR 软件组件之间的通信，以及 AUTOSAR 软件组件与基础软件层提供的软件之间的通信。基础软件层由系统基础软件和服务组成。应用层中的 AUTOSAR 软件组件通过响应事件驱动的消息，相互之间、与非平台服务以及基础软件和服务进行通信。软件组件通过 C++ 应用程序编程接口（API）与基础软件层的软件交互。

基础软件包括 POSIX® 操作系统和用于系统管理任务的软件，例如：

- 执行管理
- 通信管理
- 时间同步
- 身份访问管理
- 日志记录和跟踪

服务示例包括：

- 更新和配置管理
- 诊断
- 信号到服务的映射
- 网络管理

运行 Adaptive Platform 应用单个实例的 ECU 硬件称为机器（Machine）。一台机器可以是一个或多个芯片，也可以是虚拟硬件组件。硬件可以是托管一台或多台机器的单个芯片，也可以是托管一台机器的多个芯片。

```
                    Application（应用层）
                                                  Service        Service
 AUTOSAR   AUTOSAR   AUTOSAR                    Non-Platform   Non-Platform
 Software  Software  Software       ...           Service        Service
Component Component Component

        AUTOSAR Runtime Adaptive (ARA) Environment
        （AUTOSAR 自适应运行时环境）

                Foundation Software（基础软件）

       API                     API

                    Functional System Software        Services（服务）
 Operating System        API
 （操作系统）
                    Functional System Software

                           ...
                    Basic Software（基础软件）

    High-Performance Microcontroller or Virtual Machine
    （高性能微控制器或虚拟机）
```

Adaptive Platform 支持 AUTOSAR 应用软件的硬件无关开发和使用。特定 ECU（微控制器、高性能微控制器和虚拟机）的 RTE 抽象表示将架构应用层中的 AUTOSAR 软件组件与架构基础设施解耦。AUTOSAR 软件组件以及基础软件和服务通过专用端口进行通信。您通过将组件端口映射到系统 ECU 的 RTE 表示来配置应用。

```
                    Application（应用层）

 AUTOSAR  AUTOSAR  AUTOSAR   Service         Service
 Software Software Software  Non-Platform    Non-Platform
Component Comp...  Component   Service         Service

        AUTOSAR Runtime Adaptive (ARA) Environment
        （AUTOSAR 自适应运行时环境）

              Mapping for Deployment
              （部署映射）

High-Performance    Virtual Machine      Virtual Machine
Microcontroller

AUTOSAR  AUTOSAR   AUTOSAR              AUTOSAR
Software Software   Software             Software
Comp...  Component  Component            Component

   Application      Application  ...     Application

      ARA               ARA                 ARA

POSIX Operating    POSIX Operating    POSIX Operating
System and Other   System and Other   System and Other
Basic Software     Basic Software     Basic Software

                    Gateway（网关）
```

**参见**

更多信息：

- "在 Simulink 中建模 AUTOSAR Classic 组件及元素"（第1-18页）
- "在 Simulink 中建模 AUTOSAR Adaptive 组件及元素"（第1-23页）

外部网站：

- AUTOSAR: Automotive Open System Architecture

---

## 1.5 在 Simulink 中建模 AUTOSAR Classic 组件及元素

**本节内容...**

- "Simulink 到 AUTOSAR 的映射"（第1-18页）
- "创建 AUTOSAR 软件组件"（第1-18页）
- "配置和生成 AUTOSAR 代码"（第1-21页）

AUTOSAR Blockset 允许您从 Simulink 模型创建 AUTOSAR Classic 软件组件，并生成符合 AUTOSAR 标准的 C 代码，用于在 Simulink 中进行测试和集成到 AUTOSAR 运行时环境。

您可以通过以下方式从 Simulink 模型创建 AUTOSAR Classic 软件组件：

- 从现有的 Simulink 模型创建 AUTOSAR 软件组件。更多信息请参见 "在 Simulink 中创建 AUTOSAR 软件组件"（第3-2页）。
- 从 AUTOSAR XML (ARXML) 文件将 AUTOSAR 软件组件或组合导入 Simulink 模型。更多信息请参见 "将 AUTOSAR XML 描述导入 Simulink"（第3-13页）。

### Simulink 到 AUTOSAR 的映射

当您从 Simulink 模型创建 AUTOSAR 软件组件时，Simulink 会将其模型元素转换为 AUTOSAR 元素。下表显示了 Simulink 建模元素与相应 AUTOSAR 元素之间的映射关系。

| Simulink 元素 | AUTOSAR 元素 |
|---|---|
| 入口点函数 | Runnable（可运行实体） |
| 输入端口 | 数据读取访问或内部可运行变量（Inter-Runnable Variable） |
| 输出端口 | 数据写入访问或内部可运行变量 |
| 状态或信号线 | 每实例内存（Per-Instance Memory） |
| 模型参数 | 常量内存或共享参数 |
| 模型参数实参 | 端口参数或每实例参数 |
| 数据存储 | 每实例内存 |
| 函数调用器 | 客户端端口和操作 |
| Rate-Transition 模块 | 内部可运行变量 |

### 创建 AUTOSAR 软件组件

通过执行以下任务，从 Simulink 模型创建 AUTOSAR Classic 软件组件。

**配置 AUTOSAR Classic Platform**

您可以通过两种方式将 Simulink 模型配置为 AUTOSAR Classic Platform。

- 打开 Simulink 模型，在模型配置参数的 Code Generation 部分中将 System target file 设置为 `autosar.tlc`。保存模型并运行命令：

  ```
  autosar.api.create(modelName,"default");
  ```

- 打开 Simulink 模型，从 Apps 选项卡中点击 AUTOSAR Component Designer 应用程序。

**选择组件类型**

配置 AUTOSAR Classic Platform 后，您可以从 AUTOSAR 组件快速启动窗口中选择组件类型。AUTOSAR 软件组件是 AUTOSAR 软件的可复用构建块。AUTOSAR 软件组件连接到 AUTOSAR 运行时环境（RTE），以与 AUTOSAR 软件架构中基础软件（BSW）层的其他 AUTOSAR 软件组件和软件进行通信。在 Simulink 中，您使用 Simulink 模型组件（例如从组合模型引用的 Model 模块）来表示 AUTOSAR 软件组件。

AUTOSAR Blockset 允许您定义以下软件组件类型：

| 组件类型 | 描述 |
|---|---|
| Application（应用） | 实现软件应用的一部分，可以使用所有 AUTOSAR 通信机制和服务。 |
| Sensor-actuator（传感器-执行器） | 提供表示传感器或执行器物理值的 AUTOSAR 信号。 |
| Complex device driver（复杂设备驱动） | 为复杂或资源关键的传感器评估或执行器控制建模，位于正常 AUTOSAR BSW 栈之外的功能。 |
| ECU abstraction（ECU 抽象） | 包含对相应硬件元素的引用，并提供对 ECU 特定 I/O 能力的访问。 |
| Service proxy（服务代理） | 充当代理，为一个或多个远程 ECU 提供对内部服务的访问。 |

**定义端口和接口**

AUTOSAR 组件通过其端口与其他 AUTOSAR 软件组件或 BSW 服务进行通信。端口向其通信伙伴发送信息或从其接收信息。组件拥有的每个端口都基于组件的功能需求映射到一个通信接口。

端口使软件组件能够相互通信。AUTOSAR 使用以下类型的端口：

- **Required port（需求端口）**——当软件组件从其他实体接收或期望数据时使用。
- **Provided port（提供端口）**——当软件组件向其他实体传输数据或提供服务时使用。

端口接口指定了端口提供或需求的元素或操作。

要为组件端口配置 AUTOSAR 通信，需要创建 AUTOSAR 接口并将端口映射到该接口，然后根据接口类型的要求，将 Simulink 元素（如根级 Inport 或 Outport 模块）映射到 AUTOSAR 端口。AUTOSAR Blockset 允许您定义以下接口类型：

| 接口类型 | 描述 |
|---|---|
| Sender-receiver interface（发送方-接收方接口） | 发送方-接收方接口使用发送方和接收方端口，在软件组件与其他软件组件或 BSW 模块之间进行单向数据交换。发送方端口是向一个或多个接收方写入数据的提供端口。接收方端口是从一个或多个发送方读取数据的需求端口。发送方-接收方接口将 VariableDataPrototype 定义为 DataElement。 |
| Mode-switch interface（模式切换接口） | 模式切换接口向软件组件通知模式变更。不能跨 ECU 边界连接带有模式切换接口的端口。 |
| Client-server interface（客户端-服务器接口） | 客户端-服务器接口定义了服务器提供并由客户端使用的操作。服务器端口提供可由一个或多个客户端调用的操作。服务器等待来自客户端的传入通信请求，执行所请求的服务，并将响应分派给该请求。客户端端口是调用一个兼容服务器端口操作的需求端口。客户端发起通信，请求服务器执行服务，并在必要时传输参数集。对客户端-服务器接口操作的调用可以是同步或异步通信。在两种情况下，客户端都等待服务器的响应。 |
| Nonvolatile data interface（非易失性数据接口） | 非易失性数据接口必须属于非易失性块软件组件。 |
| Parameter interface（参数接口） | 参数接口允许参数软件组件访问常量数据、固定数据或标定数据。连接到参数接口的发送方和接收方端口必须位于同一 ECU 上，因为参数软件组件类型仅表示包含标定参数的内存。 |
| Trigger interface（触发接口） | 当没有数据需要交换，或者触发需要快速响应时间时，软件组件可以使用触发接口触发另一个软件组件。 |

更多信息请参见 "配置 AUTOSAR 端口"（第4-12页）。

定义端口和接口后，Simulink 模型即表示一个 AUTOSAR 组件。您可以添加 AUTOSAR 特有元素，例如：

- **Runnables（可运行实体）**——RTE 可以通过一个或多个 RTEEvent 激活一个可运行实体。RTE 可以通过其软件组件的端口与其他组件通信。更多信息请参见 "配置 AUTOSAR 可运行实体"（第4-20页）。
- **Inter-runnable variables（内部可运行变量）**——软件组件实例内的可运行实体可以通过将 VariableDataPrototype 定义为内部可运行变量来交换数据。不能从软件组件内部行为之外访问内部可运行变量。更多信息请参见 "配置 AUTOSAR 内部可运行变量"（第4-26页）。

**配置 AUTOSAR 元素和属性**

在 Simulink 中，您可以单独或组合使用 AUTOSAR Dictionary 和 Code Mappings Editor，以图形方式配置 AUTOSAR 软件组件并将 Simulink 模型元素映射到 AUTOSAR 组件元素。更多信息请参见 "AUTOSAR 组件配置"（第4-3页）。

AUTOSAR Dictionary 以树形格式显示已映射的 AUTOSAR 组件及其元素、通信接口、计算方法（CompuMethods）、软件地址方法（SwAddrMethods）和 XML 选项。使用该树选择 AUTOSAR 元素并配置其属性。导出的 ARXML 描述以及可能生成的符合 AUTOSAR 标准的 C 代码将反映您修改的属性。更多信息请参见 "配置 AUTOSAR 元素和属性"（第4-8页）。

### 配置和生成 AUTOSAR 代码

您可以从 AUTOSAR 软件组件模型生成符合 AUTOSAR 标准的 C 代码并导出 ARXML 描述。

使用 Embedded Coder 构建 AUTOSAR 软件组件模型。构建 Classic 软件组件模型会生成 C 代码并导出符合 AUTOSAR Classic Platform 规范的 ARXML 描述。

您还可以配置 AUTOSAR 代码生成，以根据特定的 AUTOSAR 模式版本生成 C 代码和 ARXML 描述，指定 XML 选项来源、AUTOSAR 包路径和平台类型，并修改默认的 AUTOSAR 代码生成选项。有关模式版本的更多信息，请参见 Generate XML file for schema version。

- 要配置 AUTOSAR 代码生成参数，请在 Simulink 模型 Configuration Parameters 对话框中选择 Code Generation > AUTOSAR Code Generation Options。
- 要配置 AUTOSAR XML 导出选项，请使用 AUTOSAR Dictionary 或 `autosar.api.getAUTOSARProperties` 函数。

有关配置 AUTOSAR 代码生成的更多信息，请参见 AUTOSAR XML Options Settings、`autosar.api.getAUTOSARProperties` 和 "配置 AUTOSAR 代码生成"（第5-11页）。

有关创建 AUTOSAR Classic 软件组件、生成 C 代码和 ARXML 描述的示例，请参见 "创建和配置 AUTOSAR 软件组件"（第3-8页）。

**参见**

`autosar.api.create` | `autosar.api.getAUTOSARProperties`

相关示例：

- "开发 AUTOSAR 软件组件模型"（第1-32页）
- "创建和配置 AUTOSAR 软件组件"（第3-8页）
- "创建和配置 AUTOSAR Adaptive 软件组件"（第6-6页）

更多信息：

- "什么是 AUTOSAR？"（第1-3页）
- "AUTOSAR Classic 与 Adaptive 平台对比"（第1-9页）
- "在 Simulink 中建模 AUTOSAR Adaptive 组件及元素"（第1-23页）
- "开发 AUTOSAR 软件架构模型"（第1-56页）

---

## 1.6 在 Simulink 中建模 AUTOSAR Adaptive 组件及元素

**本节内容...**

- "Simulink 到 AUTOSAR 的映射"（第1-23页）
- "创建 AUTOSAR Adaptive 软件组件"（第1-23页）
- "配置和生成 AUTOSAR 代码"（第1-25页）

AUTOSAR Blockset 允许您从 Simulink 模型创建 AUTOSAR Adaptive 应用程序，并生成符合 AUTOSAR 标准的 C++ 代码，用于集成到 AUTOSAR 运行时环境。对于 AUTOSAR Adaptive 模型，您可以生成可执行文件，并通过 Embedded Coder Support Package for Linux® Applications 将其部署到基于 POSIX 的目标机器上。

您可以通过以下方式从 Simulink 模型创建 AUTOSAR Adaptive 软件组件：

- 从现有的 Simulink 模型创建 AUTOSAR 软件组件。更多信息请参见 "在 Simulink 中创建 AUTOSAR 软件组件"（第3-2页）。
- 从 AUTOSAR XML (ARXML) 文件将 AUTOSAR 软件组件或组合导入 Simulink 模型。更多信息请参见 "导入 AUTOSAR Adaptive 软件描述"（第6-12页）。
- 从现有的 AUTOSAR 架构模型创建 AUTOSAR 软件组件。更多信息请参见 "将 AUTOSAR 组合导入架构模型"（第8-104页）。

### Simulink 到 AUTOSAR 的映射

当您从 Simulink 模型创建 AUTOSAR 软件组件时，Simulink 会将其模型元素转换为 AUTOSAR 元素。下表显示了 Simulink 建模元素与相应 AUTOSAR 元素之间的映射关系。

| Simulink 元素 | AUTOSAR 元素 |
|---|---|
| 输入端口 | ServiceRequiredPort 和 Event |
| 输出端口 | ServiceProvidedPort 和 Event |
| 端口作用域 Simulink 函数 | ServiceProvidedPort 和 Method |
| 端口作用域函数调用器 | ServiceRequiredPort 和 Method |
| 数据存储 | PersistencyProvidedRequiredPort 和 DataElement |

### 创建 AUTOSAR Adaptive 软件组件

通过执行以下任务，从 Simulink 模型创建 AUTOSAR Adaptive 软件组件。

**配置 AUTOSAR Adaptive Platform**

您可以通过两种方式将 Simulink 模型配置为 AUTOSAR Adaptive Platform。

- 打开 Simulink 模型，在模型配置参数的 Code Generation 部分中将 System target file 设置为 `autosar_adaptive.tlc`。保存模型并运行命令：

  ```
  autosar.api.create(<modelName>,'default');
  ```

- 打开 Simulink 模型，从该模型的 Apps 选项卡中点击 AUTOSAR Component Designer 应用程序。

**定义端口和接口**

AUTOSAR 组件通过其端口与其他 AUTOSAR 软件组件进行通信。端口要么消费来自其通信伙伴的服务，要么向其通信伙伴提供服务。组件拥有的每个端口都基于组件的功能需求映射到一个通信接口。

端口使软件组件能够相互通信。AUTOSAR 使用以下类型的端口：

- **Required port（需求端口）**——当软件组件消费来自其他实体的服务时使用。
- **Provided port（提供端口）**——当软件组件向其他实体提供服务时使用。
- **Persistency provided required port（持久化提供需求端口）**——当软件组件访问持久内存时使用。

为实现基于事件的通信，AUTOSAR Blockset 提供了 Event Send 和 Event Receive 模块，用于将 AUTOSAR Adaptive 运行时的事件语义转换为 Simulink 信号语义。

- 在每个根级 Inport 之后，添加一个 Event Receive 模块，该模块将输入事件转换为信号，同时保留信号值和数据类型。
- 在每个根级 Outport 之前，添加一个 Event Send 模块，该模块将输入信号转换为事件，同时保留信号值和数据类型。

为实现持久化存储，必须将 Simulink 数据存储映射到持久化端口。

要为 Adaptive 组件配置 AUTOSAR 通信，需要指定该组件将提供或消费的服务接口。将组件的每个需求端口和提供端口分配到一个特定的服务接口。将组件的每个持久化提供需求端口分配到一个特定的持久化键值接口。

| 接口类型 | 描述 |
|---|---|
| Service interface（服务接口） | AUTOSAR Adaptive Platform 定义了 Adaptive 软件组件之间面向服务的通信。服务接口允许您定义接口事件、方法和 C++ 命名空间。 |
| Persistency key value interface（持久化键值接口） | 持久化提供了通过键值存储（Key-Value Storages）访问持久内存的机制。Adaptive 应用程序的持久化使用在 Execution manifest 文件中描述。 |

Adaptive AUTOSAR 支持应用软件组件之间的客户端-服务器通信。AUTOSAR 服务接口上的方法定义了建模为提供接口实现的服务器软件组件与建模为需求接口的客户端软件组件之间的交互。在基于方法的通信中，客户端应用程序调用在远程服务器上执行的方法。更多信息请参见 "建模客户端-服务器通信"（第6-57页）。

更多信息请参见 "配置 AUTOSAR Adaptive 服务接口和端口"（第6-25页）和 "配置 AUTOSAR Adaptive 持久内存接口和端口"（第6-33页）。

**配置 AUTOSAR 元素和属性**

在 Simulink 中，您可以单独或组合使用 AUTOSAR Dictionary 和 Code Mappings Editor，以图形方式配置 AUTOSAR 软件组件并将 Simulink 模型元素映射到 AUTOSAR 组件元素。更多信息请参见 "AUTOSAR 组件配置"（第4-3页）。

AUTOSAR Dictionary 以树形格式显示已映射的 AUTOSAR 组件及其元素、服务接口、持久化键值接口和 XML 选项。使用该树选择 AUTOSAR 元素并配置其属性。导出的 ARXML 描述和生成的符合 AUTOSAR 标准的 C++ 代码将反映您修改的属性。更多信息请参见 "配置 AUTOSAR Adaptive 元素和属性"（第6-21页）。

### 配置和生成 AUTOSAR 代码

您可以从 AUTOSAR Adaptive 模型生成符合 AUTOSAR 标准的 C++ 代码，导出 ARXML 描述、清单文件（manifest files）和独立的可执行文件。

清单文件是 AUTOSAR 模型描述的一部分，用于支持 AUTOSAR Adaptive Platform 的配置，并与包含可执行代码的其他工件（如二进制文件）一起上传到 AUTOSAR Adaptive Platform，清单文件适用于这些可执行代码。

清单文件可分为以下几类：

| 清单文件类型 | 描述 |
|---|---|
| Service Instance manifest file（服务实例清单文件） | 服务实例清单文件用于根据底层传输协议的要求指定面向服务通信的配置方式。服务实例清单文件在设计时创建，并与可执行文件一起部署到机器上。 |
| Execution manifest file（执行清单文件） | 执行清单文件用于提供应用程序实际部署所需的信息。执行清单文件在设计时创建，并与可执行文件一起部署到机器上。 |
| Machine manifest file（机器清单文件） | 机器清单文件用于描述仅与底层机器配置相关的部署内容（即不涉及机器上运行的任何应用程序），这些机器运行 AUTOSAR Adaptive 应用程序。 |

AUTOSAR Adaptive 模型还生成一个可执行文件，可部署到基于 POSIX 的目标机器上，定义日志行为并执行标定和测量。您可以使用 Embedded Coder Support Package for Linux Applications 部署 AUTOSAR Adaptive 应用程序。更多信息请参见 "Build Simulink Model and Deploy Application"（Embedded Coder）。

您还可以配置 AUTOSAR 代码生成，以根据特定的 AUTOSAR 模式版本生成 C++ 代码和 ARXML 描述，指定 XML 选项、AUTOSAR 包路径，并修改默认的 AUTOSAR 代码生成选项。有关模式版本的更多信息，请参见 Generate XML file for schema version (Embedded Coder)。

- 要配置 AUTOSAR 代码生成参数，请在 Simulink 模型 Configuration Parameters 对话框中选择 Code Generation > AUTOSAR Code Generation Options。
- 要配置 AUTOSAR XML 导出选项，请使用 AUTOSAR Dictionary 或 `autosar.api.getAUTOSARProperties` 函数。

有关配置 AUTOSAR 代码生成的更多信息，请参见 AUTOSAR XML Options Settings、"配置 AUTOSAR Adaptive 代码生成"（第6-80页）和 `autosar.api.getAUTOSARProperties`。

有关创建 AUTOSAR Adaptive 软件组件并生成 C++ 代码和 ARXML 描述的示例，请参见 "创建和配置 AUTOSAR Adaptive 软件组件"（第6-6页）。

**参见**

`autosar.api.create` | `autosar.api.getAUTOSARProperties`

相关示例：

- "开发 AUTOSAR 软件组件模型"（第1-32页）
- "创建和配置 AUTOSAR 软件组件"（第3-8页）
- "创建和配置 AUTOSAR Adaptive 软件组件"（第6-6页）

更多信息：

- "什么是 AUTOSAR？"（第1-3页）
- "AUTOSAR Classic 与 Adaptive 平台对比"（第1-9页）
- "在 Simulink 中建模 AUTOSAR Classic 组件及元素"（第1-18页）
- "开发 AUTOSAR 软件架构模型"（第1-56页）

---

## 1.7 AUTOSAR 软件组件与组合

AUTOSAR 软件组件是 AUTOSAR 软件的可复用构建块。AUTOSAR 软件组件封装一个或多个算法，并通过定义良好的端口与其环境通信。例如，一个油门（throttle）应用可能包含代表油门传感器和加速踏板传感器、油门位置监测器、控制器和执行器的 AUTOSAR 软件组件。

AUTOSAR 软件组件连接到 AUTOSAR 运行时环境，用于与 AUTOSAR 软件架构中基础软件层的其他软件组件和软件进行通信。您可以在 ECU 之间复用和重定位软件组件。

在 Simulink 中，您使用 Simulink 模型组件（如 Model、Subsystem 和 Simulink Function 模块）来表示 AUTOSAR 软件组件。

AUTOSAR 组合（Compositions）是聚合一组具有相关功能的软件组件的 AUTOSAR 软件组件。组合是一种系统抽象，有助于实现可扩展性，并在设计软件应用的逻辑表示时帮助管理复杂性。

下图展示了一个用于油门位置控制的组合：

该组合由代表以下对象的软件组件组成：

- 两个油门位置传感器
- 油门位置监测器
- 加速踏板位置传感器
- 控制器
- 油门位置执行器

此外，您还可以通过将组合的 ARXML 描述导入 Simulink，或使用 AUTOSAR 架构模型编辑软件组合（需要 System Composer）来建模 AUTOSAR 软件组合。

**参见**

更多信息：

- "开发 AUTOSAR 软件组件模型"（第1-32页）
- "开发 AUTOSAR Adaptive 软件组件模型"（第1-44页）
- "建模 AUTOSAR 软件组件"（第2-3页）
- "建模 AUTOSAR Adaptive 软件组件"（第6-2页）
- "将 AUTOSAR XML 描述导入 Simulink"（第3-13页）
- "导入 AUTOSAR Adaptive 软件描述"（第6-12页）
- "在 Simulink 中创建 AUTOSAR 软件组件"（第3-2页）
- "将 AUTOSAR 组合导入 Simulink"（第7-2页）
- "导入带有原子软件组件的 AUTOSAR 软件组合（Classic Platform）"（第3-24页）
- "在架构模型中编辑 AUTOSAR 组合和组件"（第8-80页）

外部网站：

- AUTOSAR: Automotive Open System Architecture

---

## 1.8 AUTOSAR 工作流

**本节内容...**

- "Simulink 发起（自底向上）工作流"（第1-29页）
- "往返工作流"（第1-29页）

要在 Simulink 中开发 AUTOSAR 软件组件，需要创建 AUTOSAR 软件组件的 Simulink 表示。AUTOSAR 组件的创建可以从现有的 Simulink 设计开始，也可以从在另一个开发环境中创建的 AUTOSAR XML (ARXML) 组件描述开始。

在 Simulink 发起（自底向上）的工作流中，您采用现有的 Simulink 设计或算法，将其映射为 AUTOSAR 软件组件模型。

在往返工作流中，您导入由另一个开发环境中的创作工具创建的 AUTOSAR 组件描述。将组件规范导入 Simulink 会创建一个 AUTOSAR 软件组件模型。

### Simulink 发起（自底向上）工作流

在 Simulink 发起（或自底向上）的工作流中，您采用源自 Simulink 的设计或算法，将其配置为 AUTOSAR 软件组件模型。入门时，可使用 AUTOSAR Component Quick Start 或 Simulink Start Page 上的 AUTOSAR 模型模板。更多信息请参见 "在 Simulink 中创建 AUTOSAR 软件组件"（第3-2页）。

您在 Simulink 中开发组件设计和行为。例如，配置 AUTOSAR 软件组件元素，将 Simulink 模型元素映射到 AUTOSAR 软件组件元素，开发组件行为算法，以及仿真组件行为。

使用 Simulink Coder™ 和 Embedded Coder，您可以从组件模型生成符合 AUTOSAR 标准的 XML 描述和 C 或 C++ 代码。您可以在 Simulink 中测试代码，或将描述和代码集成到 AUTOSAR 运行时环境中。

### 往返工作流

在往返工作流中，您将在另一个开发环境中创建的 AUTOSAR 软件组件描述导入 Simulink。Simulink 可以导入由常见 AUTOSAR 创作工具（AAT）导出的符合 AUTOSAR 标准的 XML 描述。导入 AUTOSAR 软件组件的 XML 描述会创建该组件的 Simulink 模型表示。更多信息请参见 "将 AUTOSAR XML 描述导入 Simulink"（第3-13页）或 "导入 AUTOSAR Adaptive 软件描述"（第6-12页）。

与 Simulink 发起的设计一样，您在 Simulink 中开发组件设计和行为。例如，配置 AUTOSAR 软件组件元素，将 Simulink 模型元素映射到 AUTOSAR 软件组件元素，开发组件行为算法，以及仿真组件行为。

使用 Simulink Coder 和 Embedded Coder，您可以从组件模型生成符合 AUTOSAR 标准的 XML 描述和 C 或 C++ 代码，用于测试或集成。

在往返工作流中，您将生成的描述文件和代码交付回原始的 AAT。使用 AAT，将您的 Simulink 设计工作与其他组件和系统合并。如果您在另一个开发环境中进一步修改了组件，则使用 AAT 导出更新后的 XML 规范。在您的 Simulink 环境中，导入新的描述并更新组件模型以反映更改。更多信息请参见 "更新 AUTOSAR 软件组件"（第3-25页）。

为支持 AAT 与 Simulink 之间 AUTOSAR 元素的往返，ARXML 导入会保留导入的 AUTOSAR XML 文件结构和内容，以供 ARXML 导出。更多信息请参见 "AUTOSAR XML 文件结构和元素信息的往返保留"（第3-52页）。

**参见**

相关示例：

- "在 Simulink 中创建 AUTOSAR 软件组件"（第3-2页）
- "将 AUTOSAR XML 描述导入 Simulink"（第3-13页）
- "更新 AUTOSAR 软件组件"（第3-25页）
- "导入 AUTOSAR Adaptive 软件描述"（第6-12页）
- "AUTOSAR XML 文件结构和元素信息的往返保留"（第3-52页）

---

## 1.9 AUTOSAR 工作流示例

| 示例 | 如何... |
|---|---|
| "创建和配置 AUTOSAR 软件组件"（第3-8页） | 从算法模型创建 AUTOSAR 软件组件模型。 |
| "将 AUTOSAR 组件导入 Simulink"（第3-19页） | 从 AUTOSAR 软件组件的 XML 描述创建 Simulink 模型。 |
| "设计和仿真 AUTOSAR 组件并生成代码"（第4-86页） | 通过实现行为算法、仿真组件和组合以及生成组件代码来开发 AUTOSAR 组件。 |
| "AUTOSAR 可运行实体建模模式"（第2-12页） | 使用 Simulink 模型、子系统和函数来建模 AUTOSAR 原子软件组件及其可运行实体（Runnables）。 |
| "创建和配置 AUTOSAR Adaptive 软件组件"（第6-6页） | 从算法模型创建 AUTOSAR Adaptive 软件组件模型。 |
| "将 AUTOSAR Adaptive 组件导入 Simulink"（第6-13页） | 从 AUTOSAR Adaptive 软件组件的 XML 描述创建 Simulink 模型。 |
| "仿真 AUTOSAR 基础软件服务和运行时环境"（第7-42页） | 使用参考实现对基础软件内存和诊断服务的 AUTOSAR 组件调用进行仿真。 |
| "生成 AUTOSAR C 代码和 XML 描述"（第5-2页） | 使用 Embedded Coder 软件从 AUTOSAR 组件模型生成符合 AUTOSAR 标准的 C 代码并导出 AUTOSAR XML (ARXML) 描述。 |
| "生成 AUTOSAR Adaptive C++ 代码和 XML 描述"（第6-75页） | 使用 Embedded Coder 软件从 AUTOSAR Adaptive 组件模型生成符合 AUTOSAR 标准的 C++ 代码并导出 AUTOSAR XML (ARXML) 描述。 |
| "在架构模型中编辑 AUTOSAR 组合和组件"（第8-80页） | 使用 System Composer 软件，利用架构模型为 Classic Platform 开发 AUTOSAR 组合和组件。 |

**参见**

更多信息：

- "AUTOSAR 工作流"（第1-29页）

外部网站：

- AUTOSAR: Automotive Open System Architecture

---

## 1.10 开发 AUTOSAR 软件组件模型

**前提条件**

本教程假设您熟悉 AUTOSAR 标准和 Simulink 的基础知识。本教程的代码生成部分假设您具备 Embedded Coder 的基础知识。有关 AUTOSAR 标准的更多信息，请参见 "什么是 AUTOSAR？"（第1-3页）。

要完成本教程，您必须具备：

- MATLAB®
- Simulink
- AUTOSAR Blockset

本教程的可选部分需要 Simulink Coder 和 Embedded Coder 软件。

**示例模型**

本教程使用示例模型 `swc` 和 `autosar_swc`。要打开包含这些模型的本地工作文件夹，请在 MATLAB Command Window 中输入以下命令：

```
openExample("autosarblockset/GettingStartedWithAUTOSARCodeGenerationExample");
```

**您将学习什么**

您将学习如何：

1. 创建表示 AUTOSAR 软件组件行为的算法模型内容。
2. 为 Simulink 建模环境配置 AUTOSAR 软件组件的元素。
3. 仿真 AUTOSAR 软件组件。
4. 可选地，生成 AUTOSAR 软件组件代码。

要开始教程，请参见 "创建表示 AUTOSAR 软件组件行为的算法模型内容"（第1-34页）。

---

## 1.11 创建表示 AUTOSAR 软件组件行为的算法模型内容

AUTOSAR Blockset 软件支持 AUTOSAR Classic Platform 的 AUTOSAR 软件组件建模。要在 Simulink 中开发 AUTOSAR 软件组件，需要创建一个表示该 AUTOSAR 软件组件的 Simulink 模型。通过以下方式之一启动模型创建：

- 将现有的 AUTOSAR XML (ARXML) 组件描述作为模型导入 Simulink 环境。您可使用 AUTOSAR ARXML 导入器 `arxml.importer` 导入组件描述。
- 使用 AUTOSAR Component Designer 应用程序将现有 Simulink 模型改造为 AUTOSAR 软件组件的表示。
- 从 AUTOSAR Blockset 模型模板开始，创建一个 Simulink 模型。

在创建初始模型设计之后，细化算法内容。

本教程使用示例模型 `autosar_swc` 来展示 AUTOSAR 软件组件的示例模型表示。

1. 通过在 MATLAB Command Window 中输入以下命令打开示例模型 `autosar_swc`：

   ```
   openExample("autosarblockset/GettingStartedWithAUTOSARCodeGenerationExample","supportingFile"
   ```

2. 探索模型组件。该模型包括：

   - 周期性可运行实体 `Runnable_1s`，配置为 1 秒的采样率（`In1_1s`）。
   - 周期性可运行实体 `Runnable_2s`，配置为 2 秒的采样率（`In2_2s`）。
   - Initialize Function 模块 `Runnable_Initialize`，将 `Runnable_2s` 中的积分器初始化为值 1。

3. 探索模型配置。

   模型配置参数 System target file 设置为 `autosar.tlc`。此系统目标文件设置启用了 AUTOSAR Blockset 软件的使用。

   为最大化执行效率，模型配置为多任务模式。求解器设置如下：

   - Type 设置为 `Fixed-step`（固定步长）。
   - Solver 设置为 `discrete (no continuous states)`（离散，无连续状态）。
   - Fixed-step size (fundamental sample time) 设置为 `auto`。
   - Treat each discrete rate as a separate task（将每个离散速率视为独立任务）已选中。

   在 Simulink Editor 中，您可以通过选择 Debug 选项卡并选择 Diagnostics > Information Overlays > Colors 来启用采样时间颜色编码。采样时间图例会显示隐式速率分组。红色表示最快的离散速率。绿色表示第二快的离散速率。黄色表示两种速率的混合。

   由于模型具有多个速率，且 Solver 参数 Treat each discrete rate as a separate task 已选中，模型以多任务模式仿真。模型使用 Rate Transition 模块显式处理 `In2_2s` 的速率转换。

   Rate Transition 模块参数 Ensure deterministic data transfer（确保确定性数据传输）已清除，以方便集成到 AUTOSAR 运行时环境中。

   模型的生成代码会调度模型中的子速率。对于此模型，Inport 模块 `In2_2s` 的速率（绿色速率）是子速率。生成的代码正确地以不同速率运行的任务之间传输数据。

接下来，为在 Simulink 建模环境中使用而配置 AUTOSAR 软件组件的元素。

**参见**

相关示例：

- "建模模式"

---

## 1.12 为 Simulink 建模环境配置 AUTOSAR 软件组件元素

在 Simulink Editor 中创建 AUTOSAR 软件组件的表示之后，需要配置软件组件的元素以便在 Simulink 中使用。该配置将 AUTOSAR 软件组件元素映射到 Simulink 建模元素。

AUTOSAR Blockset 软件通过提供 AUTOSAR Component Quick Start 工具减少了设置配置的工作量。如有必要，您可以使用 Code Mappings Editor 和 AUTOSAR Dictionary 修改初始配置。

### 设置初始组件配置

使用 AUTOSAR Component Quick Start 工具设置 AUTOSAR 软件组件的初始配置。

1. 要打开未配置为 AUTOSAR 平台的示例模型 `swc`，请在 MATLAB Command Window 中输入以下命令：

   ```
   openExample("autosarblockset/GettingStartedWithAUTOSARCodeGenerationExample","supportingFile"
   ```

2. 将示例模型的副本保存到当前 MATLAB 搜索路径中的可写文件夹。将文件命名为 `my_autosar_swc.slx`。

3. 将模型配置参数 System target file 设置为 `autosar.tlc`。

4. 运行 AUTOSAR Component Quick Start 工具。从 Apps 选项卡打开 AUTOSAR Component Designer 应用程序。当您为配置了 AUTOSAR 系统目标文件的未映射模型打开该应用程序时，AUTOSAR Component Quick Start 工具会运行。

5. 推进 AUTOSAR Component Quick Start 工具的各个步骤。每一步都会提示您输入工具用于为 Simulink 环境配置 AUTOSAR 软件组件的信息。

   - 您正在配置的 AUTOSAR 软件组件的名称、包和类型。
   - 您是希望使用基于模型的默认属性，还是从 ARXML 文件导入 AUTOSAR 软件组件属性。

   对于本教程，使用默认值。

   点击 Finish 后，该工具会：

   - 在 AUTOSAR 软件组件的元素与 Simulink 模型元素之间创建映射。
   - 在 Simulink Editor 的 AUTOSAR Code 透视图中打开模型。AUTOSAR Code 透视图显示模型以及模型正下方的 Code Mappings Editor。
   - 在 Code Mappings Editor 中显示 AUTOSAR 软件组件映射，您可以使用该编辑器自定义配置。

6. 保存模型。

### 自定义组件配置

AUTOSAR Component Quick Start 工具为 AUTOSAR 软件组件设置了初始配置。要细化或更改现有的组件配置，请使用 Code Mappings Editor 和 AUTOSAR Dictionary。

Code Mappings Editor 以选项卡式表格格式显示 Simulink 模型元素，如入口点函数、Inport、Outport 和数据传输。使用该编辑器将 Simulink 模型元素映射到 AUTOSAR 软件组件元素。AUTOSAR 软件组件元素在 AUTOSAR 标准中定义，包括可运行实体（Runnables）、端口和内部可运行变量（IRVs）。

1. 如果尚未打开，请打开模型 `my_autosar_swc`。

2. 在 Code Mappings Editor 中，选择 Inports 选项卡。

3. 选择模型 Inport `In1_1s`。选择该 Inport 会高亮显示模型中的相应元素。该 Inport 映射到 AUTOSAR 端口 `In1_1s` 和数据元素 `In1_1s`，数据访问模式为 `ImplicitReceive`。

   在每个 Code Mappings Editor 选项卡中，您可以选择模型元素并修改其 AUTOSAR 映射和属性。修改将反映在生成的 ARXML 描述和 C 代码中。

4. 使用已映射模型元素的属性设置修改额外的映射属性。对于本教程，修改 Inport `In1_1s` 的通信属性。点击图标并：

   - 将 AliveTimeout 设置为 30
   - 选中 HandleNeverReceived
   - 将 InitValue 设置为 1

5. 保存模型。

### 从 AUTOSAR 标准视角配置 AUTOSAR 软件组件元素

使用 AUTOSAR Dictionary 从 AUTOSAR 标准的视角配置 AUTOSAR 软件组件元素。

1. 如果尚未打开，请打开模型 `my_autosar_swc`。

2. 打开 AUTOSAR Dictionary。在 Code Mappings Editor 中，点击 AUTOSAR Dictionary 按钮。AUTOSAR Dictionary 会在与您在 Code Mappings Editor 中最后选择和映射的 Simulink 元素对应的 AUTOSAR 视图中打开。如果您选择并映射了一个 Simulink Inport，字典会在 ReceiverPorts 视图中打开，并显示您映射该 Inport 到的 AUTOSAR 端口。

   AUTOSAR Dictionary 以树形格式显示已映射的 AUTOSAR 软件组件、其元素、通信接口、计算方法、软件地址方法和 XML 选项。

3. 使用 AUTOSAR Dictionary 进一步自定义组件配置。在 ReceiverPorts 视图中，选择端口 `In1_1s`，即 Simulink Inport 映射到的 AUTOSAR 接收方端口。会显示一个属性面板，显示该元素的属性设置。

4. 在 AUTOSAR Dictionary 中，将 AUTOSAR 接收方端口 `In1_1s` 重命名为 `In1_1s_SS1`。要启动编辑，双击 Name 值字段。

   Code Mappings Editor 会反映名称更改。

5. 保存模型。

接下来，仿真 AUTOSAR 软件组件。

**参见**

相关示例：

- "在 Simulink 中创建 AUTOSAR 软件组件"（第3-2页）
- "为代码生成映射 AUTOSAR 元素"（第4-57页）
- "配置 AUTOSAR 元素和属性"（第4-8页）

---

## 1.13 仿真并可选生成 AUTOSAR 软件组件代码（需要 Embedded Coder）

在为 Simulink 环境配置 AUTOSAR 软件组件模型之后，仿真您在 "为 Simulink 建模环境配置 AUTOSAR 软件组件元素"（第1-36页）中配置的模型 `my_autosar_swc`。

1. 如果尚未打开，请打开您配置的模型 `my_autosar_swc` 版本。

2. 在 Simulink Editor 中，点击 Simulate 按钮。

如果您有 Simulink Coder 和 Embedded Coder 软件的访问权限，接下来为 AUTOSAR 模型生成代码。

1. 如果尚未打开，请打开您配置的模型 `my_autosar_swc` 版本。

2. 通过点击 AUTOSAR 功能区 Generate Code 部分中的 Generate Code 按钮，或按 Ctrl+B 来启动代码生成。代码生成器生成 C 代码和 ARXML 文件。生成的代码符合 AUTOSAR 标准，因此您可以使用 AUTOSAR 运行时环境调度代码。

   代码生成器还会生成并显示一个代码生成报告。

3. 在代码生成报告中，查看生成的代码。在您当前的 MATLAB 文件夹中，`my_autosar_swc_autosar_rtw` 文件夹包含下表列出的主要文件。

   **生成的代码文件**

   | 文件 | 描述 |
   |---|---|
   | `my_autosar_swc.c` | 包含实现模型算法的代码入口点。该文件包含速率调度代码。 |
   | `my_autosar_swc.h` | 声明模型数据结构和模型入口点及数据结构的公共接口。 |
   | `my_autosar_swc_component.arxml`、`my_autosar_swc_datatype.arxml`、`my_autosar_swc_implementation.arxml`、`my_autosar_swc_interface.arxml` | 包含表示 AUTOSAR 软件组件、端口、接口、数据类型和包的元素和对象。您将 ARXML 文件集成到 AUTOSAR 运行时环境中。您可以使用 AUTOSAR ARXML 导入器工具将 ARXML 文件导入 Simulink 环境。 |

   默认情况下，AUTOSAR Blockset 代码生成在生成的代码中使用 AUTOSAR 平台类型，并在 `Platform_Types.h` 中定义平台类型。如果需要支持遗留实现，您可以使用 Data Type Replacement 配置参数指定代码生成器创建 Simulink 数据类型头文件 `rtwtypes.h`，并在生成的代码中使用它，以编码器类型定义的方式描述 AUTOSAR 平台类型。

   AUTOSAR Blockset 代码生成创建并要求 `rtwtypes.h` 支持文件。

4. 打开并查看代码接口报告。有关代码接口报告的更多信息，请参见 "Analyze Generated Data Code Interface Report"（Embedded Coder）。代码接口报告会为配置了 AUTOSAR 系统目标文件的模型自动生成。代码接口信息被捕获在生成的 ARXML 文件中。运行时环境生成器使用 ARXML 描述将代码接口接入 AUTOSAR 运行时环境。

   入口点函数：

   - 初始化入口点函数 —— `void my_autosar_swc_Init(void)`。在启动时调用此函数一次。
   - 输出和更新入口点函数 —— `void my_autosar_swc_Step(void)`。以模型中最快的速率周期性地调用此函数。对于此模型，每秒调用该函数一次。为实现实时执行，将此函数附加到定时器。
   - 输出和更新入口点函数 —— `void my_autosar_swc_Step1(void)`。以模型中第二快的速率周期性地调用此函数。对于此模型，每 2 秒调用该函数一次。为实现实时执行，将此函数附加到定时器。

   入口点函数也可在 Code Mappings Editor 的 Functions 选项卡中访问。您可以从外部代码或从您修改的生成主函数版本调用这些生成的函数。如有需要，您可以更改函数名称。对于基于速率的模型的基速率步进函数以及导出函数模型的步进函数，您可以自定义函数名称和参数。

   输入端口：

   - Block In1_1s —— 需求端口，接口：发送方-接收方，类型为 1 维 real-T
   - Block In2_2s —— 需求端口，接口：发送方-接收方，类型为 1 维 real-T

   输出端口：

   - Block Out1 —— 提供端口，接口：发送方-接收方，类型为 1 维 real-T
   - Block Out2 —— 提供端口，接口：发送方-接收方，类型为 1 维 real-T

5. 使用 Code 透视图中的 Code 面板检查您所做的配置更改是否出现在生成的代码中。要打开 Code 面板，在 AUTOSAR 选项卡上点击 View Code。Code 面板在模型右侧打开。在搜索字段中，键入 `In1_1s_SS1`，即 AUTOSAR 软件组件端口 `In1_1s` 的新名称。然后点击箭头按钮前进到 ARXML 文件 `my_autosar_swc_component.arxml` 中该名称的实例。验证您为 AUTOSAR 软件组件端口修改的通信属性设置是否正确显示。

6. 使用 Code 透视图 Code 面板探索生成代码的其他方面。例如，如果您选择文件 `my_autosar_swc.c`，然后点击搜索字段，会显示一个指向代码元素（包括入口点函数）的链接列表。使用这些链接快速导航到生成的 C 代码的关键区域。

**参见**

相关示例：

- "配置 AUTOSAR 代码生成"（第5-11页）

---

## 1.14 开发 AUTOSAR Adaptive 软件组件模型

**前提条件**

本教程假设您熟悉 AUTOSAR 标准和 Simulink 的基础知识。本教程的代码生成部分假设您具备 Embedded Coder 的基础知识。

要完成本教程，您必须具备：

- MATLAB
- Simulink

本教程的可选部分需要 Simulink Coder 和 Embedded Coder 软件。

**示例模型**

本教程使用示例模型 `LaneGuidance` 和 `autosar_LaneGuidance`。

**您将学习什么**

您将学习如何：

1. 创建表示 AUTOSAR Adaptive 软件组件行为的算法模型内容。
2. 为 Simulink 建模环境配置 AUTOSAR Adaptive 软件组件的元素。
3. 仿真 AUTOSAR Adaptive 软件组件。
4. 可选地，生成 AUTOSAR Adaptive 软件组件代码。

要开始教程，请参见 "创建表示 AUTOSAR Adaptive 软件组件行为的算法模型内容"（第1-46页）。

---

## 1.15 创建表示 AUTOSAR Adaptive 软件组件行为的算法模型内容

AUTOSAR Blockset 软件支持 AUTOSAR Adaptive Platform 的 AUTOSAR 软件组件建模。要在 Simulink 中开发 AUTOSAR Adaptive 软件组件，需要创建一个表示该 AUTOSAR Adaptive 软件组件的 Simulink 模型。通过以下方式之一启动模型创建：

- 将现有的 AUTOSAR XML (ARXML) 组件描述作为模型导入 Simulink 环境。您可使用 AUTOSAR ARXML 导入器导入组件描述。
- 将现有 Simulink 模型改造为 AUTOSAR Adaptive 软件组件的表示。
- 从 AUTOSAR Blockset 模型模板开始，创建一个 Simulink 模型。

在创建初始模型设计之后，细化算法内容。

本教程展示了 AUTOSAR Adaptive 软件组件的示例模型表示。

1. 通过在 MATLAB Command Window 中输入以下命令打开模型 `LaneGuidance`：

   ```
   openExample("LaneGuidance");
   ```

2. 探索模型。它由一个子系统 `LaneGuidanceAlgorithm` 组成。该子系统有六个 Inport，代表 AUTOSAR Adaptive 软件组件的需求端口：`leftLaneDistance`、`leftTurnIndicator`、`leftCarInBlindSpot`、`rightLaneDistance`、`rightTurnIndicator` 和 `rightCarInBlindSpot`。两个 Outport 代表提供端口：`leftHazardIndicator` 和 `rightHazardIndicator`。

3. 将模型配置参数 System target file 设置为 `autosar_adaptive.tlc`。该系统目标文件设置启用了 AUTOSAR Blockset 软件的使用，并影响其他模型配置参数设置。例如：

   - Language 设置为 C++。
   - Generate code only 已选中。
   - Toolchain 设置为 AUTOSAR Adaptive | CMake。
   - Code interface packaging 设置为 C++ class。

4. 在模型的顶层设置基于事件的通信。AUTOSAR Adaptive 软件组件提供和消费服务。每个组件包含：

   - 一个响应接收到的事件而执行任务的算法
   - 需求端口和提供端口，每个端口关联一个服务接口
   - 服务接口，带有相关事件和相关命名空间

   AUTOSAR Blockset 提供 Event Receive 和 Event Send 模块来进行必要的事件和信号连接。

   - 在每个根级 Inport 之后，添加一个 Event Receive 模块，该模块将输入事件转换为信号，同时保留信号值和数据类型。
   - 在每个根级 Outport 之前，添加一个 Event Send 模块，该模块将输入信号转换为事件，同时保留信号值和数据类型。

   为加快模块插入速度，您可以从完成版本的示例模型 `autosar_LaneGuidance` 复制事件模块。

5. 探索模型配置。求解器设置如下：

   - Type 设置为 `Fixed-step`（固定步长）。
   - Solver 设置为 `auto`（自动求解器选择）。
   - Fixed-step size (fundamental sample time) 设置为 `1/10`。
   - Periodic same time constraint 设置为 `Unconstrained`（无约束）。

   在 Simulink Editor 中，您可以通过选择 Debug 选项卡并选择 Diagnostics > Information Overlays > Colors 来启用采样时间颜色编码。采样时间图例会显示隐式速率分组。此模型的图例显示模型使用 0.1 秒的单一速率。模型以单任务模式仿真。

6. 将模型保存到当前 MATLAB 搜索路径中的可写文件夹。将文件命名为 `my_autosar_LaneGuidance.slx`。

接下来，为在 Simulink 建模环境中使用而配置 AUTOSAR Adaptive 软件组件的元素。

**参见**

相关示例：

- "建模模式"

---

## 1.16 为 Simulink 建模环境配置 AUTOSAR Adaptive 软件组件元素

在 Simulink Editor 中创建 AUTOSAR Adaptive 软件组件的表示之后，需要配置软件组件的元素以便在 Simulink 中使用。该配置将 AUTOSAR Adaptive 软件组件元素映射到 Simulink 建模元素。

AUTOSAR Blockset 软件通过提供 AUTOSAR Component Quick Start 工具减少了设置配置的工作量。如有必要，您可以使用 Code Mappings Editor 和 AUTOSAR Dictionary 修改初始配置。

### 设置初始组件配置

使用 AUTOSAR Component Quick Start 工具设置 AUTOSAR Adaptive 软件组件的初始配置。

1. 打开您保存的示例模型 `my_autosar_LaneGuidance` 版本。

2. 将模型配置参数 System target file 设置为 `autosar_adaptive.tlc`。

3. 运行 AUTOSAR Component Quick Start 工具。从 Apps 选项卡打开 AUTOSAR Component Designer 应用程序。当您为配置了 AUTOSAR 系统目标文件的未映射模型打开该应用程序时，AUTOSAR Component Quick Start 工具会运行。

4. 推进 AUTOSAR Component Quick Start 工具的各个步骤。每一步都会提示您输入工具用于为 Simulink 环境配置 AUTOSAR 软件组件的信息。对于本教程，使用默认值。

   点击 Finish 后，该工具会：

   - 在 AUTOSAR Adaptive 软件组件的元素与 Simulink 模型元素之间创建映射。
   - 在 Simulink Editor 的 AUTOSAR Code 透视图中打开模型。AUTOSAR Code 透视图显示模型以及模型正下方的 Code Mappings Editor。
   - 在 Code Mappings Editor 中显示 AUTOSAR 软件组件映射，您可以使用该编辑器自定义配置。

5. 保存模型。

### 自定义组件配置

AUTOSAR Component Quick Start 工具为 AUTOSAR Adaptive 软件组件设置了初始配置。要细化或更改现有的组件配置，请使用 Code Mappings Editor 和 AUTOSAR Dictionary。

Code Mappings Editor 以选项卡式表格格式显示 Simulink 模型 Inport 和 Outport。在该编辑器中将 Simulink Inport 和 Outport 映射到 AUTOSAR Adaptive 软件组件端口。AUTOSAR Adaptive 软件组件端口在 AUTOSAR 标准中定义。

1. 如果尚未打开，请打开模型 `my_autosar_LaneGuidance`。

2. 在 Code Mappings Editor 中，检查 Simulink Inport 和 Outport 到 AUTOSAR 端口和事件的映射。在每个选项卡中，您可以选择模型元素并修改其 AUTOSAR 映射和属性。修改将反映在生成的 ARXML 描述和 C 代码中。

   选择 Inports 选项卡。对于每个 Simulink Inport，编辑器会列出相应的 AUTOSAR 端口类型和事件。例如，Simulink Inport `leftLaneDistance` 映射到 AUTOSAR 需求端口和事件 `LeftLaneDistance`。

3. 选中 Code Mappings Editor 中的一行，打开 Property Inspector。检查是否需要重新配置数据类型或模型数据的其他属性。例如，验证事件数据是否为设计正确配置。对于本教程，不做任何更改。

### 从 AUTOSAR 标准视角配置 AUTOSAR Adaptive 软件组件元素

使用 AUTOSAR Dictionary 从 AUTOSAR 标准的视角配置 AUTOSAR 软件组件元素。

1. 如果尚未打开，请打开模型 `my_autosar_LaneGuidance`。

2. 打开 AUTOSAR Dictionary。在 Code Mappings Editor 中，点击 AUTOSAR Dictionary 按钮。AUTOSAR Dictionary 会在与您在 Code Mappings Editor 中最后选择和映射的 Simulink 元素对应的 AUTOSAR 视图中打开。如果您选择并映射了一个 Simulink Inport，字典会在 RequiredPorts 视图中打开，并显示您映射该 Inport 到的 AUTOSAR 端口。

   AUTOSAR Dictionary 以树形格式显示已映射的 AUTOSAR 软件组件及其元素、接口和 XML 选项。

3. 使用 AUTOSAR Dictionary 进一步自定义组件配置。例如，您可以使用字典来：

   - 展开服务接口节点以检查在默认组件映射期间创建的 AUTOSAR 事件。
   - 为每个服务接口定义唯一的命名空间。代码生成器在为模型生成 C++ 代码时使用定义的命名空间。
   - 配置导出的 AUTOSAR XML 的特性。

   在字典的左侧窗格中，展开树节点并探索模型中定义的内容。

4. 对于本教程，为服务接口 ProvidedInterface 和 RequiredInterface 添加命名空间。

   a. 在字典的左侧窗格中，展开 Service Interfaces 和 ProvidedInterface 节点。
   b. 选择 Namespaces。

   c. 在右侧窗格中，点击加号图标。
   d. 将 Name 和 Symbol 设置为 company。
   e. 添加 chassis 和 provided 的命名空间条目。
   f. 为 RequiredInterface 节点添加 company、chassis 和 required 命名空间条目。

5. 关闭字典。
6. 保存模型。

接下来，仿真 AUTOSAR Adaptive 软件组件。

**参见**

相关示例：

- "在 Simulink 中创建 AUTOSAR 软件组件"（第3-2页）
- "为代码生成映射 AUTOSAR Adaptive 元素"（第6-41页）
- "配置 AUTOSAR Adaptive 元素和属性"（第6-21页）

---

## 1.17 仿真 AUTOSAR Adaptive 软件组件并可选生成代码（需要 Embedded Coder）

在为 Simulink 环境配置 AUTOSAR Adaptive 软件组件模型之后，仿真您在 "为 Simulink 建模环境配置 AUTOSAR Adaptive 软件组件元素"（第1-49页）中配置的模型 `my_autosar_LaneGuidance`。

1. 如果尚未打开，请打开您配置的模型 `my_autosar_LaneGuidance` 版本。

2. 在 Simulink Coder Editor 中，点击 Simulate 按钮。

如果您有 Simulink Coder 和 Embedded Coder 软件的访问权限，可以构建 AUTOSAR Adaptive 模型。当您构建 AUTOSAR Adaptive 模型时，代码生成器生成符合 AUTOSAR Adaptive Platform 标准的 C++ 代码和 ARXML 描述。

1. 如果尚未打开，请打开您配置的模型 `my_autosar_LaneGuidance` 版本。
2. 按 Ctrl+B 启动代码生成。代码生成器生成 C++ 代码和 ARXML 文件。生成的代码符合 AUTOSAR 标准，因此您可以使用 AUTOSAR 运行时环境调度代码。

   代码生成器还会生成并显示一个代码生成报告。
3. 在代码生成报告中，查看生成的代码。在您当前的 MATLAB 文件夹中，`my_autosar_LaneGuidance_autosar_adaptive` 文件夹包含下表列出的主要文件。

   **生成的代码文件**

   | 文件 | 描述 |
   |---|---|
   | `my_autosar_LaneGuidance.cpp` | 包含实现模型算法的代码入口点。该文件包含速率调度代码。 |
   | `my_autosar_LaneGuidance.h` | 声明模型数据结构和模型入口点及数据结构的公共接口。 |
   | `my_autosar_LaneGuidance.arxml`、`my_autosar_LaneGuidance_ExecutionManifest.arxml`、`my_autosar_LaneGuidance_ServiceInstanceManifest.arxml` | 主 ARXML 文件包含表示 AUTOSAR 软件组件、端口、接口、数据类型和包的元素和对象。清单文件提供部署相关和服务配置信息。您将 ARXML 文件集成到 AUTOSAR 运行时环境中。您可以使用 AUTOSAR ARXML 导入器工具将 ARXML 文件导入 Simulink 环境。 |
   | `main.cpp` | 提供运行 Adaptive 软件组件服务代码的框架。 |

   默认情况下，AUTOSAR Blockset 代码生成在生成的代码中直接使用平台类型。如果需要支持遗留实现，您可以使用 Data Type Replacement 配置参数指定代码生成器通过 Simulink 数据类型头文件 `rtwtypes.h` 中的类型定义，以中间层方式定义平台类型。

   AUTOSAR Blockset 代码生成创建并要求 `rtwtypes.h` 支持文件。
4. 打开并查看代码接口报告。该信息被捕获在 ARXML 文件中。运行时环境生成器使用 ARXML 描述将代码接口接入 AUTOSAR 运行时环境。

   入口点函数：

   - 初始化入口点函数 —— `void my_autosar_LaneGuidanceModelClass::initialize()`。在启动时调用此函数一次。
   - 输出入口点函数 —— `void my_autosar_LaneGuidanceModelClass::step()`。每 0.1 秒周期性地调用此函数一次。
   - 终止入口点函数 —— `void my_autosar_LaneGuidanceModelClass::terminate()`。在关机时调用此函数一次。

   输入端口：

   - Block leftLaneDistance —— 需求端口，接口：发送方-接收方，类型为 1 维 real-T
   - Block leftTurnIndicator —— 需求端口，接口：发送方-接收方，类型为 1 维 real-T
   - Block rightLaneDistance —— 需求端口，接口：发送方-接收方，类型为 1 维 real-T
   - Block rightTurnIndicator —— 需求端口，接口：发送方-接收方，类型为 1 维 real-T
   - Block leftCarInBlindSpot —— 需求端口，接口：发送方-接收方，类型为 1 维 real-T
   - Block rightCarInBlindSpot —— 需求端口，接口：发送方-接收方，类型为 1 维 real-T

   输出端口：

   - Block leftHazardIndicator —— 外部定义的端口，类型为 1 维 real-T
   - Block rightHazardIndicator —— 外部定义的端口，类型为 1 维 real-T
5. 使用 Code 透视图中的 Code 面板检查您所做的配置更改是否出现在生成的代码中。要打开 Code 面板，在 AUTOSAR 选项卡上点击 View Code。Code 面板在模型右侧打开。

   选择文件 `my_autosar_LaneGuidance.cpp`，在搜索字段中键入 `company`（您为服务接口定义的命名空间值之一）。Code 视图会高亮显示 `company` 的实例，展示命名空间符号如何在代码中应用。
6. 使用 Code 透视图 Code 面板探索生成代码的其他方面。例如，如果您选择文件 `my_autosar_LaneGuidance.cpp`，然后点击搜索字段，会显示一个指向代码元素的链接列表。使用这些链接快速导航到生成的代码的关键区域。

**参见**

相关示例：

- "配置 AUTOSAR Adaptive 代码生成"（第6-80页）

---

## 1.18 开发 AUTOSAR 软件架构模型

**前提条件**

本教程假设您熟悉 AUTOSAR 标准和 Simulink 的基础知识。本教程的代码生成部分假设您具备 Embedded Coder 的基础知识。

本教程的可选部分需要 Simulink Coder 和 Embedded Coder 软件。

**示例模型**

本教程使用示例模型 `autosar_tpc_composition` 和多个实现 AUTOSAR 组件行为的辅助模型。要打开这些模型，请在 MATLAB Command Window 中输入以下命令：

```
openExample("autosar_tpc_composition");
```

**您将学习什么**

您将学习如何：

1. 创建用于开发 AUTOSAR 组合和组件的软件架构画布。
2. 添加并连接 AUTOSAR 组合和组件，并向组件添加 Simulink 行为。
3. 在 AUTOSAR 架构模型中仿真聚合组件的行为。
4. 可选地，导出组合和组件的 AUTOSAR XML 文件，并从 AUTOSAR 架构模型生成组件代码。

本教程重点介绍如何开发 AUTOSAR Classic 架构模型，但请注意，开发 Adaptive 架构模型的工作流是相同的。

要开始教程，请参见 "创建 AUTOSAR 软件架构模型"（第1-57页）。

---

## 1.19 创建 AUTOSAR 软件架构模型

要开始在软件架构画布中开发 AUTOSAR 组合和组件，请创建一个 AUTOSAR 架构模型（需要 System Composer）。

1. 要打开包含本教程所需示例模型的本地工作文件夹，请在 MATLAB Command Window 中输入以下命令：

   ```
   openExample("autosar_tpc_composition");
   ```

   打开文件夹后，您可以关闭 `autosar_tpc_composition` 模型，或将其保持打开以供参考。
2. 通过输入 MATLAB 命令 `simulink` 打开 Simulink Start Page。

   在 New 选项卡中，向下滚动到 AUTOSAR Blockset 并展开模型模板列表。将光标悬停在 Software Architecture 模板上，然后点击 Create Model。

   一个新的 AUTOSAR 架构模型随即打开。

   - 在 Simulink Toolstrip 中，Modeling 选项卡支持架构建模的常见任务。
   - 模型窗口左侧的 Palette 包含用于向模型添加不同类型 AUTOSAR 组件的图标：Classic Component、Software Composition、Variant Component，以及用于基础软件（BSW）建模的：Diagnostic Service Component 和 NVRAM Service Component。
   - 组合编辑器提供基于 AUTOSAR 虚拟功能总线（Virtual Function Bus, VFB）的 AUTOSAR 软件架构视图。模型画布初始为空。

本教程构建一个油门位置控制应用。请在新的架构模型中执行这些步骤，或参考示例模型 `autosar_tpc_composition` 了解最终结果。

接下来，添加并连接 AUTOSAR 组合和组件，并向组件添加 Simulink 行为。

**参见**

相关示例：

- "创建 AUTOSAR 架构模型"（第8-2页）

---

## 1.20 添加 AUTOSAR 组合与组件并链接组件实现

创建 AUTOSAR 架构模型后，您开始编写 AUTOSAR 软件设计的顶层。使用组合编辑器和 Simulink Toolstrip 的 Modeling 选项卡添加并连接 AUTOSAR 组合和组件。

在上一步中，您打开了一个本地工作示例文件夹并创建了一个空的 AUTOSAR 架构模型。如有必要，请重复该步骤以打开工作文件夹并创建空模型。

在构建油门位置控制应用的过程中，您可以参考示例模型 `autosar_tpc_composition` 了解最终结果。通过在 MATLAB Command Window 中输入以下命令打开示例模型：

```
openExample("autosar_tpc_composition");
```

### 向架构画布添加组合和组件

通常，一个 AUTOSAR 组合包含一组具有共同目的的 AUTOSAR 组件和组合。作为构建油门位置控制应用的一部分，本教程将四个传感器组件放在一个 sensors 组合中。请注意，该模型通过将 Toolstrip 上的 Platform selection 设置为 Classic Platform，配置为 Classic 架构建模。

要将 sensors 组合及其组件添加到 AUTOSAR 架构模型中：

1. 在架构模型画布中，添加一个 Software Composition 模块并将其命名为 Sensors。例如，在 Modeling 选项卡上选择 Software Composition，然后在画布中插入一个 Software Composition 模块。在高亮显示的名称字段中输入 Sensors。

2. 要填充组合，需要打开 Software Composition 模块并添加软件组件。

   打开 Sensors 模块，使模型画布显示组合内容。在组合内部，添加名为 TPS_Primary、TPS_Secondary、Monitor 和 PedalSensor 的 AUTOSAR 软件组件。例如，在 Modeling 选项卡上，您可以选择 Classic Component 来创建每个组件。

接下来，为组件添加需求端口和提供端口，然后将组件端口连接到其他组件模块或组合根端口。为了添加组件需求端口和提供端口，本教程将软件组件模块链接到已在其中定义端口的实现模型。

### 通过链接实现模型定义组件行为

AUTOSAR 应用的行为由其 AUTOSAR 软件组件定义。在 AUTOSAR 架构模型中插入软件组件模块后，您可以向组件添加 Simulink 行为。对于每个软件组件模块，您可以：

- 基于模块接口创建模型。
- 链接到实现模型。
- 从 AUTOSAR XML (ARXML) 组件描述创建模型。

为方便起见，本教程为每个 AUTOSAR 组件提供了一个 Simulink 实现模型：

- `autosar_tpc_throttle_sensor1.slx` 用于组件 TPS_Primary
- `autosar_tpc_throttle_sensor2.slx` 用于组件 TPS_Secondary
- `autosar_tpc_throttle_sensor_monitor.slx` 用于组件 Monitor
- `autosar_tpc_pedal_sensor.slx` 用于组件 PedalSensor

要向组件添加 Simulink 行为：

1. 在架构模型中，如果尚未打开 Sensors 组合模块，请将其打开。在组合内部，将每个 AUTOSAR 传感器组件链接到实现其行为的 Simulink 模型。

   例如，选择 TPS_Primary 组件模块，将光标悬停在显示的省略号上，然后选择提示 Link to Model。

   在 Link to Model 对话框中，导航到实现模型 `autosar_tpc_throttle_sensor1.slx`。

   要将组件链接到实现模型，点击 OK。
2. 将组件 TPS_Secondary、Monitor 和 PedalSensor 链接到它们的实现模型。链接每个模型后，您可以调整关联组件模块的大小，以更好地显示组件端口。

   将软件组件模块链接到指定的实现模型会更新模块和模型接口以匹配。如果您链接到使用根级 Inport 和 Outport 模块的模型，软件会将模型信号端口转换为总线端口。要查看模型内容，请打开组件模块。
3. 将组件相互连接并连接到组合根端口。

   - 要互连组件，从一个组件提供端口拖动一条线到另一个组件接收端口，或在 Modeling Toolstrip 的 Connect 部分中点击 Smart Connect 按钮。
   - 要将组件连接到 Sensors 组合边界上的根级端口，从组件端口点击并拖动到 Sensors 组合边界。
4. 可选地，为了与示例模型 `autosar_tpc_composition` 中的根端口命名完全匹配，将端口 TPS_HwIO 和 TPS_HwIO1 重命名为 TPS1_HwIO 和 TPS2_HwIO。

### 完成架构模型顶层

完成油门位置控制应用：

1. 返回架构模型的顶层。添加两个 Classic Component 模块，并分别命名为 Controller 和 Actuator。
2. 将 AUTOSAR 组件 Controller 和 Actuator 链接到它们的 Simulink 实现模型 `autosar_tpc_controller.slx` 和 `autosar_tpc_actuator.slx`。
3. 将 Sensors 组合、Controller 组件和 Actuator 组件相互连接，并连接到架构模型边界。
4. 接口和数据类型在数据字典 `tpc_interfaces.sldd` 中定义。将此数据字典链接到软件架构模型。在 Modeling 选项卡上，在 Design 部分中选择 Interfaces and Types > Link Existing Dictionary。

   要检查接口或数据类型问题，请更新架构模型。在 Modeling 选项卡上，选择 Update Model。如果发现任何问题，请将您的模型与示例模型 `autosar_tpc_composition` 进行比较。
5. 使用唯一名称保存模型，例如 `myTPC_Composition.slx`。

接下来，在 AUTOSAR 架构模型中仿真聚合组件的行为。

**参见**

相关示例：

- "添加并连接 AUTOSAR Classic 组件和组合"（第8-4页）
- "通过创建或链接模型定义 AUTOSAR 组件行为"（第8-34页）

---

## 1.21 在 AUTOSAR 架构中仿真组件

要在 AUTOSAR 架构模型中仿真聚合组件的行为，请转到架构模型的顶层并点击 Run。

如果您尝试运行本教程中构建的架构模型，会显示一条错误消息，报告未找到基础软件（BSW）模块的函数定义。四个组件实现模型中的三个包含需要 BSW 服务实现的 BSW 函数调用。

要查看这些函数调用，请打开您在上一节中创建的架构模型 `myTPC_Composition.slx`。在 Debug 选项卡上，选择 Information Overlays > Connectors > Function Connectors。此选择会列出每个包含函数调用的模型的函数连接器。要查看包含 BSW 函数调用的模型，请打开 Sensors 组合。

这些模型包含对 Diagnostic Event Manager (Dem) 和 NVRAM Manager (NvM) 服务的函数调用。在可以对应用进行仿真之前，必须将 Diagnostic Service Component 和 NVRAM Service Component 模块添加到顶层模型中。

1. 返回架构模型的顶层并选择 Modeling 选项卡。要添加服务实现模块，请选择并放置一个 Diagnostic Service Component 实例和一个 NVRAM Service Component 实例。要连接函数调用方与 BSW 服务实现，请更新模型。

2. 将 DEM/FIM 和 NvM 服务模块添加到模型后，检查 BSW 函数调用方客户端端口到 BSW 服务 ID 的映射。Dem 客户端端口映射到 Dem 服务事件 ID，NvM 客户端端口映射到 NvM 服务模块 ID。对于本教程，请更新 Dem 映射。打开 DEM/FIM 模块对话框，在 RTE 选项卡中输入所示的事件 ID 值。点击 OK。有关 BSW ID 映射的更多信息，请参见 "仿真 AUTOSAR 基础软件服务和运行时环境"（第7-42页）。

3. 架构模型现在可以进行仿真了。点击 Run。

接下来，如果您有 Embedded Coder 软件的访问权限，可以导出组合和组件的 AUTOSAR XML (ARXML) 文件，并从 AUTOSAR 架构模型生成组件代码。

**参见**

相关示例：

- "配置 AUTOSAR 调度与仿真"（第8-58页）
- "建模 AUTOSAR 基础软件服务调用"（第7-12页）

---

## 1.22 可选：生成并打包组合 ARXML 及组件代码（需要 Embedded Coder）

如果您有 Simulink Coder 和 Embedded Coder 软件的访问权限，可以导出组合和组件的 AUTOSAR XML (ARXML) 文件，并从 AUTOSAR 架构模型生成组件代码。可选地，您可以创建一个 ZIP 文件来打包模型层次结构的构建工件，例如用于迁移到测试或集成环境。

1. 打开本教程中构建的架构模型，或通过在 MATLAB Command Window 中输入以下命令打开示例模型 `autosar_tpc_composition`。

   ```
   openExample("autosar_tpc_composition");
   ```
2. 可选地，为准备导出 ARXML，您可以检查和修改 XML 选项。在 Modeling 选项卡上选择 XML Options。在架构模型级别指定的 XML 选项在导出时由模型中的每个组件继承。有关这些设置的信息，请参见 AUTOSAR XML Options Settings。
3. 要为油门位置控制应用生成并打包代码，在 Modeling 选项卡上选择 Share > Generate Code and ARXML。在 Export Composition 对话框中，指定用于打包生成文件的 ZIP 文件名。本例使用文件夹名称 MyTPC_Composition。要开始导出，点击 OK。

   在架构模型构建过程中，您可以在 Diagnostic Viewer 中查看构建日志。首先构建各组件模型，每个模型作为独立的顶层模型进行构建。最后，导出组合 ARXML。构建完成后，会为架构模型和层次结构中的每个组件模型创建文件夹层次结构和指定的 ZIP 文件。
4. 解压 ZIP 文件。其内容组织在 `arxml` 和 `src` 文件夹中。
5. 检查 `arxml` 文件夹。每个 AUTOSAR 组件都有组件描述文件和实现描述文件，而架构模型则有组合、数据类型、接口和时序描述文件。组合文件包含组合、组件原型以及组合端口和连接器的 XML 描述。数据类型、接口和时序文件聚合了整个架构模型层次结构中的元素。

TRANSLATION_COMPLETE
