# 第2章 AUTOSAR 组件的建模模式

- [2.1 Simulink 中 AUTOSAR 的建模模式](#simulink-中-autosar-的建模模式)
- [2.2 建模 AUTOSAR 软件组件](#建模-autosar-软件组件)
- [2.3 AUTOSAR Runnable 的建模模式](#autosar-runnable-的建模模式)
- [2.4 使用导出函数建模 AUTOSAR Runnable](#使用导出函数建模-autosar-runnable)
- [2.5 建模 AUTOSAR 通信](#建模-autosar-通信)
- [2.6 建模 AUTOSAR 组件行为](#建模-autosar-组件行为)
- [2.7 建模 AUTOSAR 变体](#建模-autosar-变体)
- [2.8 建模 AUTOSAR 非易失性存储器](#建模-autosar-非易失性存储器)
- [2.9 建模 AUTOSAR 数据类型](#建模-autosar-数据类型)
- [2.10 建模 AUTOSAR 标定参数与查找表](#建模-autosar-标定参数与查找表)

---

## Simulink 中 AUTOSAR 的建模模式

以下主题介绍了常见 AUTOSAR 元素的 Simulink 建模模式。在为 AUTOSAR Classic Platform 开发模型时，您可以使用这些建模模式。

- [建模 AUTOSAR 软件组件](#建模-autosar-软件组件)
- [AUTOSAR Runnable 的建模模式](#autosar-runnable-的建模模式)
- [使用导出函数建模 AUTOSAR Runnable](#使用导出函数建模-autosar-runnable)
- [建模 AUTOSAR 通信](#建模-autosar-通信)
- [建模 AUTOSAR 组件行为](#建模-autosar-组件行为)
- [建模 AUTOSAR 变体](#建模-autosar-变体)
- [建模 AUTOSAR 非易失性存储器](#建模-autosar-非易失性存储器)
- [建模 AUTOSAR 数据类型](#建模-autosar-数据类型)
- [建模 AUTOSAR 标定参数与查找表](#建模-autosar-标定参数与查找表)

---

## 建模 AUTOSAR 软件组件

**本节内容包括：**
- [关于 AUTOSAR 软件组件](#关于-autosar-软件组件)
- [实现注意事项](#实现注意事项)
- [基于速率的组件](#基于速率的组件)
- [基于函数调用的组件](#基于函数调用的组件)
- [多实例组件](#多实例组件)
- [启动、复位与关闭](#启动复位与关闭)

在 Simulink 中，您可以灵活地建模 AUTOSAR Classic Platform 软件组件的结构和行为。组件可以包含一个或多个 Runnable 实体，并且可以是单实例或多实例的。要设计组件的内部行为，您可以使用 Simulink 建模风格，例如基于速率和基于函数调用的建模方式。

### 关于 AUTOSAR 软件组件

AUTOSAR 应用程序由相互连接的软件组件（Software Components, SWC）组成。每个软件组件封装了汽车行为的功能实现，并具有明确定义的对外连接点。

在 Simulink 中，您可以建模：

- **原子软件组件（Atomic Software Component）**——原子软件组件在恰好一个汽车电子控制单元（ECU）上运行，且不能进一步拆分为更小的软件组件。
- **参数软件组件（Parameter Software Component）**——参数软件组件表示包含 AUTOSAR 标定参数的内存，并向连接的原子软件组件提供参数数据。

Simulink 中 AUTOSAR 建模的主要焦点是原子软件组件。关于参数软件组件的信息，请参见 [建模 AUTOSAR 标定参数与查找表](#建模-autosar-标定参数与查找表)。

> **注意：** 请勿将此处的"原子"与 Simulink 中原子子系统（Atomic Subsystem）的概念混淆。

AUTOSAR 原子软件组件通过明确定义的连接点（称为端口，Port）与其他 AUTOSAR 软件组件或系统服务进行交互。端口可以使用 Inport 和 Outport 模块或 Simulink 总线端口来建模。一个或多个 Runnable 实体（Runnable）实现组件的行为。

### 实现注意事项

要在 Simulink 中开发 AUTOSAR 原子软件组件，您需要创建 AUTOSAR 组件的初始 Simulink 表示形式，如"组件创建"中所述。您可以从 ARXML 文件导入 AUTOSAR 组件描述，也可以在现有模型中基于模型内容构建默认的 AUTOSAR 组件。生成的表示形式包括：

- 对 AUTOSAR 元素（如端口、Runnable、Runnable 间变量（Inter-Runnable Variable, IRV）和参数）进行建模的 Simulink 模块、连接和数据。
- 为软件组件中的 AUTOSAR 元素存储的属性，这些属性在 AUTOSAR 标准中定义。
- Simulink 元素到 AUTOSAR 元素的映射。

通常，AUTOSAR 组件的 Simulink 表示形式是基于速率的模型，其中周期性 Runnable 被建模为具有周期性速率的原子子系统。

以 AUTOSAR 示例模型 `autosar_swc` 为例。该模型展示了 AUTOSAR 原子软件组件基于速率的实现。该模型使用多个速率实现周期性 Runnable。一个 Initialize Function 模块用于初始化组件。

然而，如果您的组件设计需要 server 函数或周期性函数调用，则可以使用导出函数模型。此类模型包含 Simulink Function 模块或具有周期性速率的函数调用子系统。更多信息请参见"导出函数模型概述"。

以 AUTOSAR 示例模型 `autosar_swc_slfcns` 为例。该模型展示了 AUTOSAR 原子软件组件基于函数调用的实现。在根层级，模型使用一个 Simulink Function 模块和一个周期性函数调用子系统。一个 Initialize Function 模块用于初始化组件。

如果您的 AUTOSAR 软件组件设计包含周期性 Runnable，您必须决定组件需要基于速率还是基于函数调用的建模方法。在创建 AUTOSAR 组件的初始 Simulink 表示形式之前，请指定如何建模周期性 Runnable：

- 如果您使用 `arxml.importer` 对象函数 `createComponentAsModel` 从 ARXML 文件导入 AUTOSAR 组件描述，请将属性 `ModelPeriodicRunnablesAs` 设置为 `AtomicSubsystem`（默认值，基于速率）或 `FunctionCallSubsystem`（基于函数调用）。
- 如果您在现有模型中构建默认 AUTOSAR 组件，请使用基于速率或基于函数调用的内容填充模型。
  - 对于基于速率的建模，创建具有一个或多个周期性速率的模型内容。要建模 AUTOSAR Runnable 间变量，请使用 Rate Transition 模块处理以不同速率运行的模块之间的数据传输。生成的组件具有 N 个周期性步进 Runnable，其中 N 是模型中的离散速率数量。表示基于速率的中断的事件使用速率单调调度（Rate Monotonic Scheduling）来启动周期性步进 Runnable 的执行。
  - 对于基于函数调用的建模，在模型顶层创建函数调用子系统，或者对于客户端-服务器建模，创建 Simulink Function 模块。添加根模型 inport 和 outport。要建模 AUTOSAR Runnable 间变量，请使用信号线连接函数调用子系统。生成的组件具有 N 个导出函数或 server Runnable，其中 N 是模型顶层的函数调用子系统或 Simulink Function 模块的数量。表示函数调用的事件启动基于函数的 Runnable 的执行。

除非您的设计需要基于函数调用的建模，否则请选择基于速率的建模（默认值）。

AUTOSAR 软件组件中的某些条件可能会阻止使用基于速率的建模，例如，如果 AUTOSAR 软件组件包含：

- 一个 server Runnable
- 一个被多个 Runnable 读写的 Runnable 间变量（IRV）
- 一个速率不是最快速率整数倍的周期性 Runnable
- 多个以不同速率访问相同读或写数据的 Runnable
- 一个也被其他事件触发的周期性 Runnable
- 多个以相同周期触发的周期性 Runnable

有关 AUTOSAR 软件组件不同建模方式示例，请参见 [基于速率的组件](#基于速率的组件)、[基于函数调用的组件](#基于函数调用的组件)和 [AUTOSAR Runnable 的建模模式](#autosar-runnable-的建模模式)。

### 基于速率的组件

您可以使用 Simulink 基于速率的多任务建模来建模 AUTOSAR 多 Runnable。首先，创建或导入具有多个周期性速率的模型内容。您可以：

- 在 Simulink 中创建具有多个周期性 Runnable 的软件组件。
- 从 ARXML 文件导入具有多个周期性 Runnable 的软件组件到 Simulink。使用 `arxml.importer` 对象函数 `createComponentAsModel`，并将属性 `ModelPeriodicRunnablesAs` 设置为 `AtomicSubsystem`。
- 将现有的基于速率、多任务 Simulink 模型迁移到 AUTOSAR 目标。

根模型 inport 和 outport 表示 AUTOSAR 端口，Rate Transition 模块表示 AUTOSAR Runnable 间变量（IRV）。

以下是一个适用于仿真和 AUTOSAR 代码生成的基于速率的多任务模型示例（该示例使用示例模型 `mMultitasking_4rates.slx`）。该模型表示一个 AUTOSAR 软件组件。更新模型时显示的彩色编码（如果在 Debug 选项卡的 Diagnostics > Information Overlays 下启用了颜色）表示存在的不同周期性速率。Rate Transition 模块表示 AUTOSAR IRV。

生成代码时，模型的 C 代码包含与 AUTOSAR Runnable 对应的速率分组模型步进函数，模型中每个离散速率对应一个。（周期性步进函数必须以速率单调调度器的方式被调用。）更多信息请参见 [AUTOSAR Runnable 的建模模式](#autosar-runnable-的建模模式)。

基于速率的 AUTOSAR 软件组件可以同时包含周期性和异步 Runnable。例如，在 JMAAB 类型 beta 架构中，一个异步触发 Runnable 与周期性基于速率的 Runnable 交互。

以 AUTOSAR 示例模型 `autosar_swc_fcncalls` 为例。该模型展示了 AUTOSAR 原子软件组件基于速率的实现，包含一个位于根层的异步（触发）函数调用子系统。一个 Initialize Function 模块用于初始化组件。

更多信息请参见第 4-230 页的"向周期性基于速率系统添加顶层异步触发"。

### 基于函数调用的组件

您可以使用 Simulink 函数调用子系统——或者（对于客户端-服务器建模）在模型顶层使用 Simulink Function 模块——来建模 AUTOSAR 多 Runnable。首先，创建或导入具有多个函数的模型内容。您可以：

- 在 Simulink 中创建具有多个 Runnable 的软件组件，这些 Runnable 被建模为函数调用子系统或 Simulink Function 模块。
- 从 ARXML 文件导入具有多个 Runnable 的软件组件到 Simulink。使用 `arxml.importer` 对象函数 `createComponentAsModel`，并将属性 `ModelPeriodicRunnablesAs` 设置为 `FunctionCallSubsystem`。
- 将现有的基于函数的 Simulink 模型迁移到 AUTOSAR 目标。

根模型 inport 和 outport 表示 AUTOSAR 端口，连接函数调用子系统的信号线表示 AUTOSAR Runnable 间变量（IRV）。

以下是一个基于函数调用的模型示例，具有多个 Runnable 实体，适用于仿真和 AUTOSAR 代码生成（该示例使用 AUTOSAR 示例模型 `autosar_swc_slfcns`）。该模型表示一个 AUTOSAR 软件组件。标记为 SS1 的函数调用子系统和 Simulink Function 模块 `readData` 表示实现其行为的 Runnable。一个 Initialize Function 模块用于初始化组件。信号线 `curValIRV` 表示一个 AUTOSAR IRV。

生成代码时，模型的 C 代码包含可调用的模型入口点函数，这些函数与 AUTOSAR Runnable 一一对应，每个顶层函数调用子系统或 Simulink Function 模块对应一个。更多信息请参见 [AUTOSAR Runnable 的建模模式](#autosar-runnable-的建模模式)。

### 多实例组件

您可以在 Simulink 中建模多实例 AUTOSAR 软件组件。例如，您可以：

- 将 Simulink 模型映射并配置为多实例 AUTOSAR 软件组件，并验证该配置。使用模型参数 `Code interface packaging`（Simulink Coder）的 `Reusable function` 设置。
- 生成具有可重入 Runnable 函数和多实例 RTE API 调用的 C 代码。您可以访问外部 I/O、标定参数和每实例内存，并在多实例模式下使用可重用子系统。
- 通过软件在环（SIL）和处理器在环（PIL）仿真验证 AUTOSAR 多实例 C 代码。
- 导入和导出多实例 AUTOSAR 软件组件描述 XML 文件。

您可以为配置为多实例 AUTOSAR 软件组件且包含全局 Simulink Function 模块的模型生成代码。但是，不支持对包含全局 Simulink Function 模块的多实例 AUTOSAR 模型进行仿真。

> **注意：** 多实例 AUTOSAR 代码生成不支持某些建模模式，包括：
>
> - 包含不符合代码重用规范的 S-Function 的模型
> - 由多个函数调用触发的子系统
> - 使用带消息的队列 Sender-Receiver 通信的模型

### 启动、复位与关闭

AUTOSAR 应用程序有时需要在系统初始化、复位和终止序列期间执行复杂的逻辑。要建模 AUTOSAR 软件组件中的启动、复位和关闭处理，请使用 Simulink 模块 Initialize Function 和 Terminate Function。

Initialize Function 和 Terminate Function 模块可以控制组件响应 initialize、reset 或 terminate 事件的执行。您可以将这些模块放置在模型层次结构的任何层级。每个非虚拟子系统可以拥有自己的一组 initialize、reset 和 terminate 函数。在较低层级的模型中，Simulink 会将函数的内容与父模型中对应的实例进行聚合。

Initialize Function 和 Terminate Function 模块包含一个 Event Listener 模块。要指定函数的事件类型——Initialize、Reset 或 Terminate——请使用 Event Listener 模块的 `Event type` 参数。此外，函数模块会读取或写入其他模块的状态条件。默认情况下，Initialize Function 模块通过 State Writer 模块初始化模块状态。类似地，Terminate Function 模块通过 State Reader 模块保存模块状态。当函数被触发时，状态变量的值会被写入指定模块或从指定模块读取。

AUTOSAR 模型可以使用这些模块来建模可能很复杂的 AUTOSAR 启动、复位和关闭序列。这些子系统适用于任何 AUTOSAR 组件建模风格。（但是，AUTOSAR initialize、reset 或 terminate Runnable 的软件在环仿真仅适用于导出函数建模。）

在 AUTOSAR 模型中，您将每个 Simulink initialize、reset 或 terminate 入口点函数映射到一个 AUTOSAR Runnable。为每个 Runnable 配置激活该 Runnable 的 AUTOSAR 事件。通常，除了 TimingEvent 之外，您可以选择任何 AUTOSAR 事件类型。

更多信息请参见第 4-224 页的"配置 AUTOSAR Initialize、Reset 或 Terminate Runnable"。

**另请参阅：**
Rate Transition | Simulink Function | Initialize Function | Terminate Function | Event Listener | State Writer | State Reader

**相关示例：**
- "将 AUTOSAR XML 描述导入 Simulink"（第 3-13 页）
- "使用 Simulink 总线端口配置 AUTOSAR 端口"（第 4-153 页）
- "配置 AUTOSAR Runnable 和事件"（第 4-213 页）
- "配置 AUTOSAR Initialize、Reset 或 Terminate Runnable"（第 4-224 页）
- "向周期性基于速率系统添加顶层异步触发"（第 4-230 页）
- "配置 AUTOSAR 代码生成"（第 5-11 页）

**更多信息：**
- "AUTOSAR 组件配置"（第 4-3 页）
- [AUTOSAR Runnable 的建模模式](#autosar-runnable-的建模模式)

---

## AUTOSAR Runnable 的建模模式

使用 Simulink® 模型、子系统和函数来建模 AUTOSAR 原子软件组件及其 Runnable 实体（Runnable）。

### 配置为多任务的多个周期性 Runnable

打开示例模型 `autosar_swc.slx`。

```
open_system('autosar_swc')
```

该模型展示了一个 AUTOSAR 原子软件组件（ASWC）的实现。两个周期性 Runnable——`Runnable_1s` 和 `Runnable_2s`——使用多个采样时间建模：1 秒（`In1_1s`）和 2 秒（`In2_2s`）。为最大化执行效率，模型配置为多任务模式。

模型包含一个 Initialize Function 模块，它使用值 1 初始化 `Runnable_2s` 中的积分器。

要显示带有注释和标注的彩色编码采样时间，请在 Debug 选项卡上选择 Diagnostics > Information Overlays > Colors。

**相关的模型配置参数设置：**

- Solver > Type 设置为 `Fixed-step`。
- Solver > Solver 设置为 `discrete (no continuous states)`。
- Solver > Fixed-step size (fundamental sample time) 设置为 `auto`。
- Solver > Treat each discrete rate as a separate task 被选中。

**调度：**

在模型窗口中，通过选择 Debug 选项卡并选择 Diagnostics > Information Overlays > Colors 来启用采样时间彩色编码。采样时间标注显示隐式的速率分组。红色表示最快的离散速率。绿色表示第二快的离散速率。黄色表示两种速率的混合。

由于模型具有多个速率，且 Solver 参数 `Treat each discrete rate as a separate task` 被选中，因此模型以多任务模式进行仿真。模型通过 Rate Transition 模块显式处理 `In2_2s` 的速率转换。

Rate Transition 模块参数 `Ensure deterministic data transfer` 被清除，以便于集成到 AUTOSAR 运行环境中。

模型的生成代码会调度子速率。在此示例中，Inport 模块 `In2_2s` 的速率（绿色速率）是一个子速率。生成的代码正确地在以不同速率运行的任务之间传输数据。

**生成代码和报告（Embedded Coder）：**

如果您拥有 Simulink Coder 和 Embedded Coder 软件，可以生成代码和代码生成报告。该示例模型生成一份报告。

生成的代码符合 AUTOSAR 标准，以便您可以使用 AUTOSAR 运行环境对其进行调度。

**查看生成的代码：**

在代码生成报告中，查看生成的代码。

- `autosar_swc.c` 包含实现模型算法的代码入口点。此文件包含速率调度代码。
- `autosar_swc.h` 声明模型数据结构和模型入口点及数据结构的公共接口。
- `autosar_swc_private.h` 包含模型和子系统所需的局部 define 常量和局部数据。
- `autosar_swc_types.h` 提供实时模型数据结构和参数数据结构的前向声明。
- `rtwtypes.h` 定义生成的代码所需的数据类型、结构体和宏。
- `autosar_swc_component.arxml`、`autosar_swc_datatype.arxml`、`autosar_swc_implementation.arxml` 和 `autosar_swc_interface.arxml` 包含表示 AUTOSAR 软件组件、端口、接口、数据类型和包的元素与对象。您可以将 ARXML 文件集成到 AUTOSAR 运行环境中。您可以使用 AUTOSAR ARXML 导入器工具将 ARXML 文件导入 Simulink 环境。
- `Compiler.h`、`Platform_Types.h`、`Rte_ASWC.h`、`Rte_Type.h` 和 `Std_Types.h` 包含 AUTOSAR 运行环境函数的桩实现。使用这些文件可以在 Simulink 中测试生成的代码，例如在进行被测组件的软件在环（SIL）或处理器在环（PIL）仿真时。

**代码接口：**

打开并查看代码接口报告。这些信息被记录在 ARXML 文件中。运行环境生成器使用 ARXML 描述将代码接入 AUTOSAR 运行环境。

输入端口：

- Require 端口，接口：1 维 `real-T` 类型的 Sender-Receiver
- Require 端口，接口：1 维 `real-T` 类型的 Sender-Receiver

入口点函数：

- 初始化入口点函数，`void Runnable_Initialize(void)`。在启动时调用此函数一次。
- 输出和更新入口点函数，`void Runnable_1s(void)`。以模型中最快的速率周期性地调用此函数。对于此模型，每秒调用一次。为实现实时执行，将此函数附加到定时器上。
- 输出和更新入口点函数，`void Runnable_2s(void)`。以模型中第二快的速率周期性地调用此函数。对于此模型，每 2 秒调用一次。为实现实时执行，将此函数附加到定时器上。

输出端口：

- Provide 端口，接口：1 维 `real-T` 类型的 Sender-Receiver
- Provide 端口，接口：1 维 `real-T` 类型的 Sender-Receiver

### 配置为周期性速率 Runnable 和异步函数调用 Runnable 的多个 Runnable

打开示例模型 `autosar_swc_fcncalls.slx`。

```
open_system('autosar_swc_fcncalls')
```

该模型展示了一个 AUTOSAR 原子软件组件（ASWC）的实现。模型使用一个异步函数调用 Runnable `Runnable_Trigger`，它由外部事件触发。模型还包含一个基于周期性速率的 Runnable `Runnable_1s`。Rate Transition 模块表示 Runnable 间变量（IRV）。

使用此方法来建模 JMAAB 复杂控制模型类型 beta 架构。在 JMAAB 类型 beta 建模中，在控制模型的顶层，您将函数层置于调度层之上。

模型包含一个 Initialize Function 模块，该模块使用值 0 初始化 `Runnable_1s` 中的单位延迟。

要显示带有注释和标注的彩色编码采样时间，请在 Debug 选项卡上选择 Diagnostics > Information Overlays > Colors。

**相关的模型配置参数设置：**

- Solver > Type 设置为 `Fixed-step`。
- Solver > Solver 设置为 `discrete (no continuous states)`。
- Solver > Fixed-step size (fundamental sample time) 设置为 `1`。
- Solver > Treat each discrete rate as a separate task 被清除。

**调度：**

在模型窗口中，通过选择 Debug 选项卡并选择 Diagnostics > Information Overlays > Colors 来启用采样时间彩色编码。采样时间标注显示隐式的速率分组。红色表示离散速率。品红色表示异步函数触发。黄色表示两种速率的混合。

异步触发 Runnable 以异步速率运行（函数调用子系统 Trigger 模块的 `Sample time type` 参数设置为 `triggered`），而周期性速率 Runnable 以指定的离散速率运行。生成的代码使用单任务假设来管理速率。对于只有一个离散速率的模型，代码生成器不会产生调度代码，因为只有一个速率需要执行。当您只有一个周期性 Runnable 时，将此技术用于单速率应用。

模型通过两个 Rate Transition 块处理相连 Runnable 的异步速率和离散速率之间的转换。Rate Transition 模块参数 `Ensure deterministic data transfer` 被清除，以便于集成到 AUTOSAR 运行环境。

**生成代码和报告（Embedded Coder）：**

如果您拥有 Simulink Coder 和 Embedded Coder 软件，可以生成代码和代码生成报告。该示例模型生成一份报告。

生成的代码符合 AUTOSAR 标准，以便您可以使用 AUTOSAR 运行环境对其进行调度。

**查看生成的代码：**

在代码生成报告中，查看生成的代码。

- `autosar_swc_fcncalls.c` 包含实现模型算法的代码入口点。此文件包含速率调度代码。
- `autosar_swc_fcncalls.h` 声明模型数据结构和模型入口点及数据结构的公共接口。
- `autosar_swc_fcncalls_private.h` 包含模型和子系统所需的局部 define 常量和局部数据。
- `autosar_swc_fcncalls_types.h` 提供实时模型数据结构和参数数据结构的前向声明。
- `rtwtypes.h` 定义生成的代码所需的数据类型、结构体和宏。
- `autosar_swc_fcncalls_component.arxml`、`autosar_swc_fcncalls_datatype.arxml`、`autosar_swc_fcncalls_implementation.arxml` 和 `autosar_swc_fcncalls_interface.arxml` 包含表示 AUTOSAR 软件组件、端口、接口、数据类型和包的元素与对象。您可以将 ARXML 文件集成到 AUTOSAR 运行环境中。您可以使用 AUTOSAR ARXML 导入器工具将 ARXML 文件导入 Simulink 环境。
- `Compiler.h`、`Platform_Types.h`、`Rte_ASWC.h`、`Rte_Type.h` 和 `Std_Types.h` 包含 AUTOSAR 运行环境函数的桩实现。使用这些文件可以在 Simulink 中测试生成的代码，例如在进行被测组件的软件在环（SIL）或处理器在环（PIL）仿真时。

**代码接口：**

打开并查看代码接口报告。这些信息被记录在 ARXML 文件中。运行环境生成器使用 ARXML 描述将代码接入 AUTOSAR 运行环境。

输入端口：

- Require 端口，接口：1 维 `real-T` 类型的 Sender-Receiver

入口点函数：

- 初始化入口点函数，`void Runnable_Initialize(void)`。在启动时调用此函数一次。
- Simulink 函数，`void Runnable_1s(void)`。以模型中最快的速率周期性地调用此函数。对于此模型，每秒调用一次。为实现实时执行，将此函数附加到定时器上。
- 导出函数，`void Runnable_Trigger(void)`。可在任何时候从外部触发器调用此函数。

输出端口：

- Provide 端口，接口：1 维 `real-T` 类型的 Sender-Receiver

### 配置为函数调用子系统和 Simulink Function 的多个 Runnable

打开示例模型 `autosar_swc_slfcns.slx`。

```
open_system('autosar_swc_slfcns')
```

该模型展示了一个 AUTOSAR 原子软件组件（ASWC）的实现。模型包含一个使用函数调用子系统 SS1 的周期性速率 Runnable `Runnable_1s`。模型还包含一个 Simulink 函数 `readData`，用于向请求它的客户端提供值（`CurVal`）。

模型包含一个 Initialize Function 模块，该模块使用值 0 初始化子系统 `RollingCounter` 中的单位延迟。

要显示带有注释和标注的彩色编码采样时间，请在 Debug 选项卡上选择 Diagnostics > Information Overlays > Colors。

在以下情况下使用函数调用子系统：

- 当在 Simulink 模型中难以或不可能指定系统事件时。
- 为实现复杂的多速率 Runnable 调度时。将每个速率建模为单独的函数调用子系统。

**相关的模型配置参数设置：**

- Solver > Type 设置为 `Fixed-step`。
- Solver > Solver 设置为 `discrete (no continuous states)`。
- Solver > Fixed-step size (fundamental sample time) 设置为 `1`。
- Solver > Treat each discrete rate as a separate task 被选中。

**调度：**

在模型窗口中，通过选择 Debug 选项卡并选择 Diagnostics > Information Overlays > Colors 来启用采样时间彩色编码。采样时间标注显示隐式的速率分组。红色表示离散速率。绿色表示从导出函数继承的速率，表明它们的执行在 Simulink 调度的上下文之外。

您的执行框架必须调度生成的函数代码并处理函数之间的数据传输。

**生成代码和报告（Embedded Coder）：**

如果您拥有 Simulink Coder 和 Embedded Coder 软件，可以生成代码和代码生成报告。该示例模型生成一份报告。

代码生成器：

- 为模型根层的函数调用子系统生成一个 AUTOSAR Runnable。
- 将 Runnable 之间的信号连接实现为 AUTOSAR Runnable 间变量（IRV）。

生成的代码符合 AUTOSAR 标准，以便您可以使用 AUTOSAR 运行环境对其进行调度。

**查看生成的代码：**

在代码生成报告中，查看生成的代码。

- `autosar_swc_slfcns.c` 包含实现模型算法的代码入口点。此文件包含速率调度代码。
- `autosar_swc_slfcns.h` 声明模型数据结构和模型入口点及数据结构的公共接口。
- `autosar_swc_slfcns_private.h` 包含模型和子系统所需的局部 define 常量和局部数据。
- `autosar_swc_slfcns_types.h` 提供实时模型数据结构和参数数据结构的前向声明。
- `readData_private.h` 包含 Simulink 函数所需的局部 define 常量和局部数据。
- `rtwtypes.h` 定义生成的代码所需的数据类型、结构体和宏。
- `autosar_swc_slfcns_component.arxml`、`autosar_swc_slfcns_datatype.arxml`、`autosar_swc_slfcns_implementation.arxml` 和 `autosar_swc_slfcns_interface.arxml` 包含表示 AUTOSAR 软件组件、端口、接口、数据类型和包的元素与对象。您可以将 ARXML 文件集成到 AUTOSAR 运行环境中。您可以使用 AUTOSAR ARXML 导入器工具将 ARXML 文件导入 Simulink 环境。
- `Compiler.h`、`Platform_Types.h`、`Rte_ASWC.h`、`Rte_Type.h` 和 `Std_Types.h` 包含 AUTOSAR 运行环境函数的桩实现。使用这些文件可以在 Simulink 中测试生成的代码，例如在进行被测组件的软件在环（SIL）或处理器在环（PIL）仿真时。

**代码接口：**

打开并查看代码接口报告。这些信息被记录在 ARXML 文件中。运行环境生成器使用 ARXML 描述将代码接入 AUTOSAR 运行环境。

输入端口：

- Require 端口，接口：1 维 `uint16_T` 类型的 Sender-Receiver
- Require 端口，接口：1 维 `real_T` 类型的 Sender-Receiver

入口点函数：

- 初始化入口点函数，`void Runnable_Init(void)`。在启动时调用此函数一次。
- 导出函数，`void Runnable_1s(void)`。每秒周期性地调用此函数。
- Simulink 函数，`Std_ReturnType readData(real_T Data[2])`。可在任何时间调用此函数。

输出端口：

- Provide 端口，接口：1 维 `uint16-T` 类型的 Sender-Receiver

**相关链接：**

- [建模 AUTOSAR 软件组件](#建模-autosar-软件组件)
- "组件创建"
- "代码生成"

---

## 使用导出函数建模 AUTOSAR Runnable

使用 Simulink® 导出函数来建模 AUTOSAR Runnable。

### 配置为函数导出的多个周期性 Runnable

打开示例模型 `autosar_swc_expfcns.slx`。

```
open_system('autosar_swc_expfcns')
```

该模型展示了使用导出函数建模的 AUTOSAR 原子软件组件（ASWC）的实现。导出函数模型是为独立函数生成代码的 Simulink 模型。您可以将独立的函数代码与外部环境和调度器进行集成。函数通常使用 Function-Call Subsystem 和 Simulink Function 模块来定义。

此模型使用具有周期性速率的 Function-Call Subsystem 模块实现了三个 AUTOSAR 周期性 Runnable。这些 Runnable 的采样时间分别为 1 秒、1 秒和 10 秒。要显示带有注释和标注的彩色编码采样时间，请在 Debug 选项卡上选择 Diagnostics > Information Overlays > Colors。

Simulink 信号线用于建模 AUTOSAR Runnable 间变量（IRV），这些变量将 Runnable 连接起来。

**生成 AUTOSAR 组件代码和 XML 描述（Embedded Coder）：**

如果您拥有 Simulink Coder 和 Embedded Coder 软件，可以生成算法 C 代码和 AUTOSAR XML（ARXML）组件描述。您可以在 Simulink 中测试生成的代码，或将代码和描述集成到 AUTOSAR 运行环境中。

例如，要构建 `autosar_swc_expfcns` 组件模型，请打开模型。按 Ctrl+B 或输入 MATLAB 命令 `slbuild('autosar_swc_expfcns')`。构建完成后，将打开代码生成报告。

在代码生成报告中，选择 Code Interface Report 部分，并检查 Entry-Point Functions 表。

在生成的代码中，每个根级函数调用 Inport 模块生成一个 void-void 函数。从生成的 `autosar_swc_expfcns.c` 文件中，以下是 `Runnable1` 的生成代码。

**相关链接：**

"导出函数模型概述"

---

## 建模 AUTOSAR 通信

在 Simulink 中，对于 Classic Platform，您可以建模 AUTOSAR Sender-Receiver（S-R）、Client-Server（C-S）、Mode-Switch（M-S）、Nonvolatile（NV）数据、参数和触发通信。

### 关于 AUTOSAR 通信

AUTOSAR 软件组件提供明确定义的连接点，称为端口。AUTOSAR 端口有三种类型：

- Require（In）
- Provide（Out）
- 组合的 Provide-Require（InOut——在 AUTOSAR 模式版本 4.1 中引入）

AUTOSAR 端口可以引用以下类型的接口：

- Sender-Receiver
- Client-Server
- Mode-Switch
- Nonvolatile Data
- Parameter
- Trigger

下图展示了一个具有四个端口的 AUTOSAR 软件组件，这些端口表示了 Sender-Receiver 和 Client-Server 接口的端口与接口组合。

一个引用 Mode-Switch 接口的 Require 端口称为 Mode-Receiver 端口。

### Sender-Receiver 接口

在 AUTOSAR 基于端口的 Sender-Receiver（S-R）通信中，AUTOSAR 软件组件向其他组件或服务读写数据。为实现 S-R 通信，AUTOSAR 软件组件定义：

- 一个包含数据元素的 AUTOSAR Sender-Receiver 接口。
- 发送和接收数据的 AUTOSAR Provide 和 Require 端口。

在 Simulink 中，您可以：

1. 使用 AUTOSAR Dictionary 创建 AUTOSAR S-R 接口和端口。
2. 使用 Simulink 根级 outport 和 inport 建模 AUTOSAR Provide 和 Require 端口。
3. 使用 Code Mappings 编辑器将 outport 和 inport 映射到 AUTOSAR Provide 和 Require 端口。

Sender-Receiver 接口由一个或多个数据元素组成。虽然 Require、Provide 或 Provide-Require 端口可以引用一个 Sender-Receiver 接口，但 AUTOSAR 软件组件不一定访问所有数据元素。例如，考虑下图。

AUTOSAR 软件组件有一个 Require 端口和一个 Provide 端口，它们引用同一个 Sender-Receiver 接口 `Interface1`。虽然此接口包含数据元素 DE1、DE2、DE3、DE4 和 DE5，但组件并未使用所有数据元素。

下图是一个示例，说明如何在 Simulink 中建模访问数据元素的 AUTOSAR 软件组件。

ASWC 访问数据元素 DE1 和 DE2。您按如下方式建模数据元素访问：

- 对于 Require 端口，使用 Simulink inport。例如，`RPort_DE1` 和 `RPort1_DE2`。
- 对于 Provide 端口，使用 Simulink outport。例如，`PPort_DE1` 和 `PPort_DE2`。
- 对于 Provide-Require 端口（模式 4.1 或更高版本），使用一对具有匹配数据类型、维度和信号类型的 Simulink inport 和 outport。更多信息请参见第 4-110 页的"配置 AUTOSAR Provide-Require 端口"。

`ErrorStatus` 是 AUTOSAR Runtime Environment（RTE）返回的值，用于指示通信系统为每个数据元素检测到的错误。从 ARXML 文件导入时，如果关联的 Sender-Receiver 数据元素满足以下条件之一，则会将 ErrorStatus 端口添加到接收方组件：

- `INVALIDATION-POLICY` 设置为 `KEEP` 或 `REPLACE`。
- 元素的 `COM-SPECS` 使用正的 `ALIVE-TIMEOUT` 值。
- 元素的 `COM-SPECS` 将 `HANDLE-NEVER-RECEIVED` 设置为 `true`。
- 元素的 `COM-SPECS` 将 `USES-END-TO-END-PROTECTION` 设置为 `true`。

您可以使用 Simulink inport 来建模错误状态，例如 `RPort_DE1 (ErrorStatus)`。

使用 AUTOSAR Dictionary 和 Code Mappings 编辑器为每个 inport 和 outport 指定 AUTOSAR 设置。更多信息请参见第 4-109 页的"配置 AUTOSAR Sender-Receiver 通信"。

### 队列式 Sender-Receiver 接口

在 AUTOSAR 队列式 Sender-Receiver（S-R）通信中，AUTOSAR 软件组件向其他组件或服务读写数据。由 AUTOSAR 发送方软件组件发送的数据被添加到由 AUTOSAR Runtime Environment（RTE）提供的队列中。新接收的数据不会覆盖已有的未读数据。之后，接收方软件组件从队列中读取数据。

为实现队列式 S-R 通信，AUTOSAR 软件组件定义：

- 一个包含数据元素的 AUTOSAR Sender-Receiver 接口。
- 发送和接收队列数据的 AUTOSAR Provide 和 Require 端口。

在 Simulink 中，您可以：

1. 使用 AUTOSAR Dictionary 创建 AUTOSAR 队列式 S-R 接口和端口。
2. 使用 Simulink 根级 outport 和 inport 建模 AUTOSAR Provide 和 Require 端口。
3. 使用 Code Mappings 编辑器将 outport 和 inport 映射到 AUTOSAR Provide 和 Require 端口。将 AUTOSAR 数据访问模式设置为 `QueuedExplicitSend` 或 `QueuedExplicitReceive`。

要使用队列建模发送和接收 AUTOSAR 数据，请使用 Simulink Send 和 Receive 模块。如果您的队列式 S-R 通信实现涉及状态或需要决策逻辑，请使用 Stateflow® 图表。您可以处理队列为空或队列已满时发生的错误。您可以指定队列的大小。更多信息请参见"Simulink 消息概述"。

您可以在组件模型之间仿真 AUTOSAR 队列式 Sender-Receiver（S-R）通信，例如在复合级仿真中。数据发送方和接收方可以以不同的速率运行。多个数据发送方可以与单个数据接收方通信。

要入门，您可以从 ARXML 文件将带有队列式 S-R 接口和端口的组件导入到 Simulink 中，或者使用 Simulink 创建这些接口和端口。更多信息请参见第 4-126 页的"配置 AUTOSAR 队列式 Sender-Receiver 通信"。

### Client-Server 接口

AUTOSAR 允许在以下对象之间进行 Client-Server 通信：

- 应用软件组件之间
- 应用软件组件与基础软件（Basic Software）之间

AUTOSAR Client-Server 接口定义了提供接口的软件组件与需要接口的软件组件之间的交互。提供接口的组件是 Server。需要接口的组件是 Client。

要在 Simulink 中建模 AUTOSAR Client 和 Server，以用于仿真和代码生成：

- 要建模 AUTOSAR Server，请在模型根层使用 Simulink Function 模块。
- 要建模 AUTOSAR Client 调用，请使用 Function Caller 模块。
- 使用基于函数调用的建模风格，在模型顶层创建相互连接的 Simulink 函数、函数调用以及根模型 inport 和 outport。

下图展示了一个函数调用框架，其中 Simulink Function 模块用于建模 AUTOSAR Server Runnable，Function Caller 模块用于建模 AUTOSAR Client 调用，Simulink 数据传输线用于建模 AUTOSAR Runnable 间变量（IRV）。

在 Simulink 中开发 AUTOSAR Client 和 Server 的高级工作流程如下：

1. 在 Simulink 中建模 Server 函数和 Caller 模块。例如，在模型根层创建 Simulink Function 模块，并创建调用这些函数的相应 Function Caller 模块。
2. 在配置为 AUTOSAR 的模型中，将 Simulink 函数映射并配置为 AUTOSAR Server Runnable。验证配置、进行仿真，并从模型生成 C 代码和 ARXML 文件。
3. 在另一个配置为 AUTOSAR 的模型中，将 Function Caller 模块映射并配置为 AUTOSAR Client 端口和 AUTOSAR 操作。验证配置、进行仿真，并从模型生成 C 代码和 ARXML 文件。
4. 将生成的 C 代码集成到测试框架中进行测试，例如通过 SIL 仿真。（最终，生成的 C 代码和 ARXML 文件将被集成到 AUTOSAR Runtime Environment（RTE）中。）

更多信息请参见第 4-166 页的"AUTOSAR Client-Server 通信"。

### Mode-Switch 接口

AUTOSAR Mode-Switch（M-S）通信依赖于一个 Mode Manager 和连接的模式用户（Mode User）。Mode Manager 是软件组件查询当前模式以及在模式更改时接收通知的权威来源。Mode Manager 可以由 AUTOSAR Basic Software（BSW）提供，或者实现为一个 AUTOSAR 软件组件。实现为软件组件的 Mode Manager 称为应用模式管理器（Application Mode Manager）。查询 Mode Manager 并接收模式更改通知的软件组件是 Mode User。

- [Mode User](#mode-user)
- [Application Mode Manager](#application-mode-manager)

#### Mode User

要在 Simulink 中建模 AUTOSAR Mode User 软件组件：

- 创建一个 AUTOSAR Mode-Switch 接口。
- 创建一个 AUTOSAR Mode Receiver 端口，并将其映射到 Simulink inport。
- 对于模型中的初始化 Runnable 或其他 AUTOSAR Runnable，指定一个 Mode-Switch 事件来触发该 Runnable。

要建模 AUTOSAR 软件组件 Mode-Receiver 端口，一般步骤可以包括：

1. 使用 Simulink 枚举声明一个 Mode Declaration Group（一组模式值）。例如，您可以创建一个枚举类型 `mdgModes`，包含枚举值 `MANUAL_ADJUST` 和 `AUTO_ADJUST`。将存储类型指定为无符号整数。

```
Simulink.defineIntEnumType("mdgModes", ...
    {"MANUAL_ADJUST", "AUTO_ADJUST"}, ...
    [18 28], ...
    "Description", "Type definition of mdgModes.", ...
    "HeaderFile", "Rte_Type.h", ...
    "DefaultValue", "MANUAL_ADJUST", ...
    "AddClassNameToEnumNames", false,...
    "StorageType", "uint16"...
    );
```

2. 将枚举数据类型应用到表示 AUTOSAR Mode-Receiver 端口的 Simulink inport。在此 Inport 模块对话框中，将枚举类型 `mdgModes` 指定为 inport 数据类型。

3. 要指定 Simulink inport 到 AUTOSAR Mode-Receiver 端口的映射，请使用 Code Mappings 编辑器（或等效的 AUTOSAR map 函数）。

   在以下示例中，在 Code Mappings 编辑器的 Inports 选项卡中，Simulink inport `mode_receive` 被映射到 AUTOSAR Mode-Receiver 端口 `mode_receive_port` 和 AUTOSAR 元素 `mdgModes`。

要指定一个 Mode-Switch 事件来触发 Initialize Runnable 或导出 Runnable，一般步骤可以包括：

1. 要编辑、添加或移除 AUTOSAR Mode-Switch 接口和 Mode-Receiver 端口，请使用 AUTOSAR Dictionary（或等效的 AUTOSAR 属性函数）。
2. 在您的模型中，选择或添加一个您希望由 Mode-Switch 事件激活的 Runnable。
3. 在 AUTOSAR Dictionary 的 Runnables 视图中，选择您希望由 Mode-Switch 事件激活的 Runnable。配置该事件。在以下示例中，为 `Runnable_Auto` 添加了一个 Mode-Switch 事件，并配置为在入口时激活（相对于在出口时或转换时激活）。它被映射到先前配置的 Mode-Receiver 端口和一个对所选择端口有效的 Mode Declaration 值。

更多信息请参见第 4-190 页的"配置 AUTOSAR Mode-Switch 通信"。

#### Application Mode Manager

要在 Simulink 中建模 Application Mode Manager 软件组件，请使用 AUTOSAR Mode Sender 端口。Mode Sender 端口向连接的模式用户组件输出模式切换。例如，以下是一个在 Simulink 中建模的 Application Mode Manager，它使用 Mode Sender 端口输出 `EngineMode` 的当前值。

您将 Mode Sender 端口建模为模型根 outport，它被映射到 AUTOSAR Mode Sender 端口和一个 Mode-Switch（M-S）接口。outport 数据类型是一个具有无符号整数存储类型的枚举类，表示一个 AUTOSAR Mode Declaration Group。

在 Simulink 中，您可以：

- 从 ARXML 文件导入 AUTOSAR Mode-Switch 通信元素。
  - 软件导入 `ModeSwitchPoints`、`ModeSwitchInterfaces` 和 `ModeDeclarationGroups`。
  - 对于每个引用 M-S 接口的 AUTOSAR Provider 端口，导入器会创建一个具有 `ModeSend` 数据访问权限和一个 AUTOSAR Mode Declaration Group 枚举类的根 outport。
  - 导入器将模型 outport 映射到具有 M-S 接口的 AUTOSAR Mode Sender 端口。
- 创建 AUTOSAR Mode-Switch 通信元素。
  - 创建一个模型根 outport，并将 outport 数据类型设置为表示 AUTOSAR Mode Declaration Group 的枚举类。
  - 创建一个具有关联 M-S 接口的 AUTOSAR Mode Sender 端口。
  - 在 Code Mappings 编辑器中，将 outport 数据访问模式设置为 `ModeSend`，并将 outport 映射到 AUTOSAR Mode Sender 端口。
- 为 AUTOSAR Mode Sender 端口和相关的 AUTOSAR M-S 通信元素生成 ARXML 文件和 C 代码。
  - ARXML 文件包括引用的 `ModeSwitchPoints`、`ModeSwitchInterfaces` 和 `ModeDeclarationGroups`。
  - C 代码包括 `Rte_Switch` API 调用，用于将模式切换传达给其他软件组件。

更多信息请参见第 4-190 页的"配置 AUTOSAR Mode-Switch 通信"。

### Nonvolatile Data 接口

AUTOSAR 标准定义了基于端口的非易失性（Nonvolatile, NV）数据通信，其中 AUTOSAR 软件组件向 AUTOSAR 非易失性组件读取和写入数据。为实现 NV 数据通信，AUTOSAR 软件组件定义发送和接收 NV 数据的 Provide 和 Require 端口。有关建模软件组件对 AUTOSAR 非易失性存储器访问的更多信息，请参见 [建模 AUTOSAR 非易失性存储器](#建模-autosar-非易失性存储器)。

在 Simulink 中，您可以：

- 从 ARXML 文件导入 AUTOSAR NV 数据接口和端口。
- 创建 AUTOSAR NV 接口和端口，并将 Simulink inport 和 outport 映射到 AUTOSAR NV 端口。

  您以与 [Sender-Receiver 接口](#sender-receiver-接口) 中描述的相同方式，使用 Simulink inport 和 outport 建模 AUTOSAR NV 端口。
- 为 AUTOSAR NV 数据接口和端口生成 C 代码和 ARXML 文件。

更多信息请参见第 4-198 页的"配置 AUTOSAR Nonvolatile 数据通信"。

### Parameter 接口

AUTOSAR 标准定义了基于端口的参数用于参数通信。AUTOSAR 参数通信依赖于一个参数软件组件（`ParameterSwComponent`）和一个或多个需要基于端口访问参数数据的原子软件组件。`ParameterSwComponent` 表示包含 AUTOSAR 参数的内存，并向连接的原子软件组件提供参数数据。

在 Simulink 中，您可以建模 AUTOSAR 基于端口参数通信的接收方部分。在 AUTOSAR 原子软件组件中，您创建一个包含数据元素的参数接口和一个参数接收方端口。

更多信息请参见第 4-200 页的"配置 AUTOSAR 端口参数以与参数软件组件通信"。

### Trigger 接口

AUTOSAR 标准定义了外部触发事件通信，其中 AUTOSAR 软件组件或服务向另一个组件发出发生了外部触发事件（`ExternalTriggerOccurredEvent`）的信号。接收方组件激活一个 Runnable 来响应该事件。

在 Simulink 中，您可以建模 AUTOSAR 外部触发事件通信的接收方部分。在您希望对外部触发做出反应的组件中，您创建一个 Trigger 接口、一个用于接收 `ExternalTriggerOccurredEvent` 的 Trigger Receiver 端口，以及一个由该事件激活的 Runnable。

更多信息请参见第 4-206 页的"配置 AUTOSAR 外部触发事件通信的接收方"。

**另请参阅：**

**相关示例：**
- "配置 AUTOSAR Sender-Receiver 通信"（第 4-109 页）
- "配置 AUTOSAR 队列式 Sender-Receiver 通信"（第 4-126 页）
- "AUTOSAR Client-Server 通信"（第 4-166 页）
- "配置 AUTOSAR Mode-Switch 通信"（第 4-190 页）
- "配置 AUTOSAR Nonvolatile 数据通信"（第 4-198 页）
- "配置 AUTOSAR 端口参数以与参数软件组件通信"（第 4-200 页）
- "配置 AUTOSAR 外部触发事件通信的接收方"（第 4-206 页）

**更多信息：**
- "AUTOSAR 组件配置"（第 4-3 页）

---

## 建模 AUTOSAR 组件行为

在 Simulink 中，您可以建模 AUTOSAR 组件行为，包括 Runnable、事件和 Runnable 间变量的行为。

### 用于建模组件行为的 AUTOSAR 元素

要建模 AUTOSAR 组件行为，您需要建模描述组件调度和资源共享方面的 AUTOSAR 元素。与组件行为相关的 AUTOSAR 元素包括：

- Runnable 及其响应的事件
- Runnable 间变量（Inter-Runnable Variables），用于在同一组件中的 Runnable 之间传递数据
- Included Data Type Sets（包含的数据类型集），提供组件内部数据类型
- 系统常量（System Constants），用于指定可在组件算法中引用的系统级常量值
- 每实例内存（Per-Instance Memory），用于指定组件内实例特定的全局内存
- 静态内存和常量内存（Static and Constant Memory），用于在组件内访问全局数据和参数值
- 共享参数和每实例参数（Shared and Per-Instance Parameters），用于访问组件内部参数数据
- 端口参数（Port Parameters），用于基于端口访问参数数据

本主题介绍如何建模帮助您定义组件行为的 AUTOSAR 元素。

### Runnable

AUTOSAR 软件组件包含由底层 AUTOSAR 操作系统直接或间接调度的 Runnable。

下图展示了一个具有两个 Runnable 的 AUTOSAR 软件组件：Runnable 1 和 Runnable 2。RTEEvents（AUTOSAR Runtime Environment（RTE）生成的事件）触发每个 Runnable。例如，`TimingEvent` 是一个周期性生成的 RTEEvent。

组件还可以包含单个由模型表示的 Runnable，并且可以是单速率或多速率的。

> **注意：** 无论使用何种建模模式，软件都会为初始化函数生成一个额外的 Runnable。

更多信息请参见第 4-213 页的"配置 AUTOSAR Runnable 和事件"。

### Runnable 间变量

在 AUTOSAR 中，Runnable 间变量用于在同一组件中的 Runnable 之间传递数据。您在 Simulink 模型中通过连接子系统（Runnable）的信号线来定义这些变量。例如，在下图中，`irv1`、`irv2`、`irv3` 和 `irv4` 都是 Runnable 间变量。

您可以指定导出的 Runnable 间变量的名称和数据访问模式。

### Included Data Type Sets

在 AUTOSAR 软件组件模型中，您可以导入和导出 AUTOSAR Included Data Type Set（`IncludedDataTypeSet`）的 ARXML 描述。`IncludedDataTypeSet` 是软件组件内部行为的一部分而定义的。它包含对 AUTOSAR 数据类型定义的引用，这些数据类型定义是组件内部的，不存在于组件接口描述中。引用的内部数据类型定义可以在多个软件组件之间共享，如第 3-38 页的"将 AUTOSAR 数据类型和共享元素导入 Simulink"所述。

如果您将包含 `IncludedDataTypeSet` 描述的 ARXML 文件导入 Simulink，导入器会在 AUTOSAR 组件模型中创建内部数据类型，并将它们映射到头文件 `Rte_Type.h`。

在 AUTOSAR 组件模型中，要配置内部数据类型以导出到 ARXML `IncludedDataTypeSet` 描述中，请将内部数据类型映射到头文件 `Rte_Type.h`。构建组件模型时：

- 导出模型代码中使用的内部数据类型的 ARXML `IncludedDataTypeSet` 描述。
- 为内部数据类型生成 `Rte_Type.h` 头文件条目。

对于 AUTOSAR `IncludedDataTypeSet` 导出，Simulink 支持以下数据类型：

- Numeric（数值型）
- Alias（别名型）
- Bus（总线型）
- Fixed-point（定点型）
- Enumerated（枚举型）

枚举文本的文字前缀在导入和创建的 `IncludedDataTypeSet` 中处理方式不同：

- 如果您导入一个 `IncludedDataTypeSet`，它定义了 `LiteralPrefix` 作为枚举文本的公共前缀，导入器会保留该 `LiteralPrefix` 以用于导出和 `IncludedDataTypeSet` 的往返。
- 如果您在组件模型中配置内部数据类型以导出到 AUTOSAR `IncludedDataTypeSet`，导出器会生成一个 `LiteralPrefix` 为空的 `IncludedDataTypeSet` 中的数据类型。

更多信息请参见第 4-237 页的"为 AUTOSAR IncludedDataTypeSets 配置内部数据类型"。

### 系统常量

AUTOSAR 系统常量（`SwSystemConstants`）指定了可在组件算法中引用的系统级常量值。要将 AUTOSAR 系统常量添加到模型中，您可以：

- 从 ARXML 文件导入它们。
- 在具有 AUTOSAR Classic Platform 映射的 Simulink 数据字典的 Architectural Data 部分中创建它们。
- 尽管不推荐，您也可以使用存储类（Storage class）设置为 `SystemConstant` 的 `AUTOSAR.Parameter` 对象在 Simulink 中创建系统常量。

然后，您可以在 Simulink 算法中引用 AUTOSAR 系统常量。例如，您可以在 Gain 模块中引用系统常量，或在变体子系统或模型引用内部的条件公式中引用系统常量。

在您的模型中引用 AUTOSAR 系统常量时：

- 导出的 ARXML 文件包含相应的 `SwSystemConstant` 和一个引用该 `SwSystemConstant` 的相应 AUTOSAR 变体点代理（`VariationPointProxy`）。如果您生成模块化 ARXML 文件，`SwSystemConstant` 位于 `modelname_datatype.arxml` 中，而 `VariationPointProxy` 位于 `modelname_component.arxml` 中。
- 生成的 C 代码在模型使用 `SwSystemConstant` 的地方使用生成的 `VariationPointProxy`。

有关表示与变体条件逻辑相关的条件值的 AUTOSAR 系统常量示例，请参见第 4-259 页的"为 AUTOSAR Runnable 实现配置变体"。

### 每实例内存

AUTOSAR 支持每实例内存（Per-Instance Memory），它允许您在软件组件内指定实例特定的全局内存。AUTOSAR 运行环境生成器分配此内存，并提供一个可通过它访问此内存的 API。

每实例内存可以是 AUTOSAR 类型的或 C 类型的。AUTOSAR 类型的每实例内存（`arTypedPerInstanceMemory`）使用 AUTOSAR 数据类型而不是 C 类型来描述。当在 ARXML 文件中导出时，`arTypedPerInstanceMemory` 允许使用标定和测量工具来监视与每实例内存对应的全局变量。

AUTOSAR 还允许您将每实例内存用作非易失性 RAM（NVRAM）中数据的 RAM 镜像。您可以在 AUTOSAR 应用程序中访问和使用 NVRAM。有关建模软件组件对 AUTOSAR 非易失性存储器访问的更多信息，请参见 [建模 AUTOSAR 非易失性存储器](#建模-autosar-非易失性存储器)。

要将 AUTOSAR 每实例内存添加到模型中，您可以：

- 从 ARXML 文件导入每实例内存定义。
- 创建表示每实例内存的模型内容。

要建模 `arTypedPerInstanceMemory`，您可以在 AUTOSAR 模型中使用模块信号、离散状态或数据存储：

- 要使用模块信号和离散状态，请使用 Code Mappings 编辑器的 Signals/States 选项卡，选择一个信号或状态并将其映射到 `arTypedPerInstanceMemory`。要查看和修改每实例内存的 AUTOSAR 代码和标定属性，请点击 ![icon] 图标。
- 要使用数据存储，请使用 Code Mappings 编辑器的 Data Stores 选项卡，选择一个数据存储并将其映射到 `arTypedPerInstanceMemory`。要查看和修改每实例内存的 AUTOSAR 代码和标定属性，请点击 ![icon] 图标。

更多信息请参见第 4-240 页的"配置 AUTOSAR Per-Instance Memory"。

### 静态内存和常量内存

AUTOSAR 支持静态内存（`StaticMemory`）和常量内存（`ConstantMemory`）数据。静态内存对应于 Simulink 内部全局信号。常量内存对应于 Simulink 内部全局参数。在 Simulink 中，您可以导入和导出 AUTOSAR 静态内存和常量内存的 ARXML 描述。当在 ARXML 文件中导出时，静态内存和常量内存允许使用标定和测量工具来监视内部内存数据。

要在 Simulink 中建模 AUTOSAR 静态内存，请使用 Code Mappings 编辑器的 Signals/States 或 Data Stores 选项卡。选择一个信号、状态或数据存储，并将其映射到 `StaticMemory`。要查看和修改静态内存的 AUTOSAR 代码和标定属性，请点击 ![icon] 图标。

要在 Simulink 中建模 AUTOSAR 常量内存，请使用 Code Mappings 编辑器的 Parameters 选项卡，选择一个参数并将其映射到 `ConstantMemory`。要查看和修改常量内存的 AUTOSAR 代码和标定属性，请点击 ![icon] 图标。

更多信息请参见第 4-245 页的"配置 AUTOSAR Static Memory"和第 4-249 页的"配置 AUTOSAR Constant Memory"。

### 共享参数和每实例参数

AUTOSAR 支持共享参数（`SharedParameters`）和每实例参数（`PerInstanceParameters`），用于可能被多次实例化的软件组件。共享参数值在组件的所有实例之间共享。每实例参数值对于每个组件实例是唯一且私有的。

在 Simulink 中，您可以导入和导出 AUTOSAR 共享参数和每实例参数的 ARXML 描述。当在 ARXML 文件中导出时，共享参数和每实例参数允许使用标定和测量工具来监视组件参数。

要在 Simulink 中建模 AUTOSAR 共享参数，请配置一个不是模型参数（即对多实例模型的每个实例不唯一）的模型工作区参数。例如，在参数的 Model Explorer 视图中，清除 `Argument` 属性。在 Code Mappings 编辑器的 Parameters 选项卡中，选择该参数并将其映射到参数类型 `SharedParameter`。要查看和修改共享参数的 AUTOSAR 代码和标定属性，请点击 ![icon] 图标。

要在 Simulink 中建模 AUTOSAR 每实例参数，请配置一个作为模型参数（即对多实例模型的每个实例唯一）的模型工作区参数。例如，在参数的 Model Explorer 视图中，选择 `Argument` 属性。在 Code Mappings 编辑器的 Parameters 选项卡中，选择该参数并将其映射到参数 `PerInstanceParameter`。要查看和修改每实例参数的 AUTOSAR 代码和标定属性，请点击 ![icon] 图标。

更多信息请参见第 4-251 页的"配置 AUTOSAR 共享参数或每实例参数"。

### 端口参数

AUTOSAR 标准定义了基于端口的参数用于参数通信。AUTOSAR 参数通信依赖于一个参数软件组件（`ParameterSwComponent`）和一个或多个需要基于端口访问参数数据的原子软件组件。`ParameterSwComponent` 表示包含 AUTOSAR 参数的内存，并向连接的原子软件组件提供参数数据。

在 Simulink 中，您可以建模 AUTOSAR 参数通信的接收方。通过导入 ARXML 描述或配置软件组件模型，您可以建模：

- AUTOSAR 参数接收方组件，与 `ParameterSwComponent` 通信以接收参数数据。
- AUTOSAR 参数接口，包含参数数据元素。数据元素映射到模型工作区中的参数或查找表对象。
- AUTOSAR 参数接收方端口，用于与 `ParameterSwComponent` 通信。

当您为 AUTOSAR 参数接收方组件生成代码时：

- 导出的 ARXML 文件包含参数接收方组件、参数接口、参数数据元素和参数接收方端口的描述。
- 生成的 C 代码包含 AUTOSAR 端口参数 Rte 函数调用。

在运行时，软件可以将参数数据元素作为基于端口的参数进行访问。

由于端口参数数据的作用域限于模型工作区和 AUTOSAR 组件：

- 不同的组件可以使用相同的参数名称而不会发生命名冲突。
- AUTOSAR 组合可以包含参数接收方组件的多个实例，每个实例具有特定于实例的端口参数数据值。

更多信息请参见第 4-200 页的"配置 AUTOSAR 端口参数以与参数软件组件通信"。

**另请参阅：**
Data Store Memory

**相关示例：**
- "配置 AUTOSAR Runnable 和事件"（第 4-213 页）
- "为 AUTOSAR Runnable 实现配置变体"（第 4-259 页）
- "为 AUTOSAR IncludedDataTypeSets 配置内部数据类型"（第 4-237 页）
- "配置 AUTOSAR Per-Instance Memory"（第 4-240 页）
- "配置 AUTOSAR Static Memory"（第 4-245 页）
- "配置 AUTOSAR Constant Memory"（第 4-249 页）
- "配置 AUTOSAR 共享参数或每实例参数"（第 4-251 页）
- "配置 AUTOSAR 端口参数以与参数软件组件通信"（第 4-200 页）

**更多信息：**
- "AUTOSAR 组件配置"（第 4-3 页）
- "为 AUTOSAR 内部变量指定默认数据打包"（第 4-71 页）

---

## 建模 AUTOSAR 变体

AUTOSAR 软件组件使用变体来基于定义的条件在执行路径中启用或禁用 AUTOSAR 接口或实现。组件中的变体点（Variation Points）提供在两个或多个变体之间进行选择。组件可以：

- 启用或禁用 AUTOSAR 端口或 Runnable。
- 改变 AUTOSAR Runnable 的实现。
- 改变 AUTOSAR 端口的数组大小。
- 指定预定义变体和系统常量值集，用于控制组件中的变体。

在 Simulink 中，您可以：

- 导入和导出带有变体的 AUTOSAR 端口和 Runnable。
- 建模 AUTOSAR 变体。
  - 要启用或禁用 AUTOSAR 端口或 Runnable，请使用 Variant Sink 和 Variant Source 模块。
  - 要改变 AUTOSAR Runnable 的实现，请使用 Variant Subsystem 模块。
  - 要改变 AUTOSAR 端口的数组大小，请使用 Simulink 符号维度。
- 通过使用从 ARXML 文件导入的预定义变体和系统常量值集来解析建模的变体。

AUTOSAR 系统常量作为控制组件变体点的输入。要建模系统常量，请使用 `AUTOSAR.Parameter` 数据对象。

### 端口和 Runnable 的变体

AUTOSAR 软件组件可以使用 `VariationPoint` 元素来基于定义的条件启用或禁用 AUTOSAR 元素，例如端口和 Runnable。在 Simulink 中，您可以：

- 导入带有变体点的 AUTOSAR 端口和 Runnable。
  - ARXML 导入器创建所需的模型元素，包括用于传播变体条件的 Variant Sink 和 Variant Source 模块，以及用于表示带有条件值的系统常量的 `AUTOSAR.Parameter` 数据对象。
- 建模带有变体点的 AUTOSAR 元素。
  - 要定义变体条件逻辑并传播变体条件，请使用 Variant Sink 和 Variant Source 模块。
  - 要建模 AUTOSAR 系统常量并定义条件值，请使用存储类为 `SystemConstant` 的 `AUTOSAR.Parameter` 数据对象。
- 对 AUTOSAR 配置运行验证。验证软件会验证 Simulink 模块上的变体条件是否与导入的 ARXML 文件中设计的行为相匹配。
- 导出带有变体点的 AUTOSAR 端口和 Runnable。

更多信息请参见第 4-256 页的"为 AUTOSAR 元素配置变体"。

### Runnable 实现的变体

要改变 AUTOSAR Runnable 的实现，AUTOSAR 软件组件可以在 Runnable 内部指定变体条件逻辑。在 Simulink 中，要在 Runnable 内部建模变体条件逻辑：

- 使用 Variant Subsystem 模块来定义变体实现及其关联的变体条件逻辑。
- 使用 `AUTOSAR.Parameter` 数据对象来建模 AUTOSAR 系统常量并定义条件值。

更多信息请参见第 4-259 页的"为 AUTOSAR Runnable 实现配置变体"。

### 数组大小的变体

AUTOSAR 软件组件可以通过使用对系统常量的符号引用来灵活指定 AUTOSAR 元素（如端口）的维度。系统常量定义端口数据类型的数组大小。代码生成器支持包含具有变体（符号）数组大小的 AUTOSAR 元素的模型。

在 Simulink 中，您可以：

- 导入具有变体数组大小的 AUTOSAR 元素。
  - ARXML 导入器创建所需的模型元素，包括存储类为 `SystemConstant` 的 `AUTOSAR.Parameter` 数据对象，以表示数组大小值。
  - 每个表示具有变体数组大小的 AUTOSAR 元素的模块引用 `AUTOSAR.Parameter` 数据对象来定义其维度。
- 建模具有变体数组大小的 AUTOSAR 元素。
  - 创建表示 AUTOSAR 元素的模块。
  - 要表示数组大小值，请添加存储类为 `SystemConstant` 的 `AUTOSAR.Parameter` 数据对象。
  - 要为 AUTOSAR 元素指定数组大小，请引用一个 `AUTOSAR.Parameter` 数据对象。
- 在模型仿真之间修改系统常量中的数组大小值，而无需重新生成仿真代码。
- 生成具有与变体数组大小对应的符号的 C 代码和 ARXML 文件。

更多信息请参见第 4-264 页的"为 AUTOSAR 数组大小配置维度变体"。

### 预定义变体和系统常量值集

要定义在 AUTOSAR 软件组件中控制变体点的值，组件使用以下 AUTOSAR 元素：

- `SwSystemconst`——定义一个系统常量，作为控制变体点的输入。
- `SwSystemconstantValueSet`——指定一组系统常量值。
- `PredefinedVariant`——描述一组系统常量值的组合（在可能多个有效组合中），应用于 AUTOSAR 软件组件。

假设您有一个 AUTOSAR 软件组件的 ARXML 规范。如果 ARXML 文件还定义了一个 `PredefinedVariant` 或 `SwSystemconstantValueSets` 用于控制组件中的变体点，您可以在模型创建时解析变体点。指定一个 `PredefinedVariant` 或 `SwSystemconstantValueSets`，导入器可以使用它来初始化 `SwSystemconst` 数据。

模型创建后，您可以基于指定的变体点输入值组合运行仿真并生成代码。

在 Simulink 中，使用 AUTOSAR 属性函数 `createSystemConstants`，您可以重新定义控制变体点的 `SwSystemconst` 数据，而无需重新创建模型。您可以基于修改后的变体点输入值组合运行仿真并生成代码。

构建模型会将之前导入的 `PredefinedVariants` 和 `SwSystemconstantValueSets` 导出到 ARXML 文件。

更多信息请参见第 4-266 页的"使用预定义值组合控制 AUTOSAR 变体"。

**另请参阅：**

**相关示例：**
- "为 AUTOSAR 元素配置变体"（第 4-256 页）
- "为 AUTOSAR Runnable 实现配置变体"（第 4-259 页）
- "为 AUTOSAR 数组大小配置维度变体"（第 4-264 页）
- "使用预定义值组合控制 AUTOSAR 变体"（第 4-266 页）

**更多信息：**
- "AUTOSAR 组件配置"（第 4-3 页）

---

## 建模 AUTOSAR 非易失性存储器

AUTOSAR 标准定义了隐式和显式两种机制，AUTOSAR 软件组件可以通过这些机制在汽车系统中读写非易失性存储器：

- **隐式访问**使用 Sender-Receiver 端口或数据存储内存块来访问 RAM 中 AUTOSAR 非易失性存储器块的副本。
- **显式访问**使用 Client-Server 调用来直接访问 AUTOSAR 非易失性存储器块。

### AUTOSAR 非易失性存储器的隐式访问

AUTOSAR 非易失性存储器的隐式访问使用启动事件开始在 RAM 中映射或镜像非易失性存储器块。使用非易失性存储器的 RAM 副本可以支持更快的访问。

1. 在 ECU 上电期间，当发生启动事件时，后台任务将存储器块从非易失性存储器空间复制到 RAM。
2. 当系统运行时，软件组件可以以 RAM 速度访问非易失性数据。
3. 当发生关闭事件时，在关闭之前，后台任务将映射或镜像的存储器块复制回非易失性存储器空间。

要在 AUTOSAR 组件模型中建模非易失性存储器的隐式读写访问，您可以配置基于端口的 Nonvolatile（NV）数据通信或配置 NVRAM 镜像块。

在基于端口的 NV 数据通信中，AUTOSAR 软件组件向 AUTOSAR 非易失性组件读取和写入数据。为实现 NV 数据通信，AUTOSAR 软件组件定义发送和接收 NV 数据的 Provide 和 Require 端口。在 Simulink 中，您可以：

- 从 ARXML 文件导入 AUTOSAR NV 数据接口和端口。
- 创建 AUTOSAR NV 接口和端口，并将 Simulink inport 和 outport 映射到 AUTOSAR NV 端口。

  您以与 [Sender-Receiver 接口](#sender-receiver-接口) 中描述的相同方式，使用 Simulink inport 和 outport 建模 AUTOSAR NV 端口。
- 为 AUTOSAR NV 数据接口和端口生成 C 代码和 ARXML 文件。

使用基于端口的 NV 数据通信，您可以跨软件组件分发或协调 NV 数据访问。例如，多个组件可以从非易失性软件组件读取相同的 NV 数据，而一个组件向其写入。

更多信息请参见第 4-198 页的"配置 AUTOSAR Nonvolatile 数据通信"。

要配置 NVRAM 镜像块，AUTOSAR 软件组件将数据存储内存块映射到 AUTOSAR 类型的每实例内存（`ArTypedPerInstanceMemory`），并选择 `NeedsNVRAMAccess` 选项。此选项表示 `ArTypedPerInstanceMemory` 是一个 RAM 镜像块，需要来自 NVRAM Manager（NvM）管理器模块的服务。在 Simulink 中，您可以：

- 从 ARXML 文件导入 AUTOSAR NVRAM 镜像块。
- 创建将数据存储内存块配置为 AUTOSAR NVRAM 镜像块的模型内容。
- 为 AUTOSAR NVRAM 镜像块生成 C 代码和 ARXML 文件。AUTOSAR 运行环境生成器分配内存，并提供一个 API，组件通过该 API 访问内存。

更多信息请参见第 4-240 页的"配置 AUTOSAR Per-Instance Memory"。

### AUTOSAR 非易失性存储器的显式访问

对于 AUTOSAR Classic Platform，AUTOSAR 标准将重要服务定义为在 AUTOSAR Runtime Environment（RTE）中运行的基础软件（Basic Software, BSW）的一部分。示例包括由 NVRAM Manager 和 Diagnostic Event Manager 提供的服务。在 AUTOSAR RTE 中，AUTOSAR 软件组件通常使用 Client-Server 通信来访问 BSW 服务。

AUTOSAR 非易失性存储器的显式访问使用对 NVRAM Manager（NvM）服务的调用来直接访问 AUTOSAR 非易失性存储器空间。显式访问可以用于响应事件（例如安全气囊事件），或在每个时间步使用（例如，对于没有关闭序列的控制器）。

为了支持 AUTOSAR 组件和服务的系统级建模，AUTOSAR Blockset 提供了一个 AUTOSAR Basic Software 模块库。该库包含预配置的 Function Caller 模块，用于建模组件对 NVM 服务接口的调用，包括 `NvMAdminCaller` 和 `NvMServiceCaller`。

要在 AUTOSAR 软件组件中实现对 AUTOSAR NVM 服务接口的客户端调用，请将 Basic Software 模块拖放到 AUTOSAR 模型中。每个模块都有预填充的参数，例如 `Client port name` 和 `Operation`。如果您修改操作选择，软件会更新模块的输入和输出以对应。

要在 AUTOSAR 软件组件中配置添加的模块，请点击模型的 Code Mappings 编辑器视图中的 Update 按钮 ![update]。软件创建 AUTOSAR Client-Service 接口、操作和端口，并将每个 Simulink Function Caller 映射到 AUTOSAR Client 端口和操作。

更多信息请参见第 7-32 页的"配置对 AUTOSAR NVRAM Manager 服务的调用"。

要仿真调用 BSW 服务的 AUTOSAR 组件模型，请创建一个包含组合、系统或测试框架模型。在该包含模型中，提供组件调用的 NvM 服务操作的参考实现。

AUTOSAR Basic Software 模块库包含一个 NVRAM Service Component 模块。该模块提供 NvM 服务操作的参考实现。为支持组件对 NvM 服务调用的仿真，请在包含模型中包含这些模块。您可以以以下两种方式之一插入这些模块：

- 通过创建 Simulink Test™ 测试框架模型自动插入模块。
- 手动将模块插入包含组合、系统或测试框架模型。

更多信息请参见第 7-38 页的"为仿真配置 AUTOSAR 基础软件服务实现"和第 7-42 页的"仿真 AUTOSAR 基础软件服务和运行环境"。

**另请参阅：**
NvMAdminCaller | NvMServiceCaller | NVRAM Service Component

**相关示例：**
- "配置 AUTOSAR Nonvolatile 数据通信"（第 4-198 页）
- "配置 AUTOSAR Per-Instance Memory"（第 4-240 页）
- "配置对 AUTOSAR NVRAM Manager 服务的调用"（第 7-32 页）
- "为仿真配置 AUTOSAR 基础软件服务实现"（第 7-38 页）
- "仿真 AUTOSAR 基础软件服务和运行环境"（第 7-42 页）

---

## 建模 AUTOSAR 数据类型

AUTOSAR 数据类型在汽车软件模型中提供一致且可靠的数据交换。在 Simulink 中，您可以建模用于组件、组合和架构的各种元素的 AUTOSAR 数据类型。当您从 ARXML 文件导入 AUTOSAR 组件到 Simulink 时，AUTOSAR 数据类型描述用于创建相应的 Simulink 数据类型。在代码生成期间，Embedded Coder 导出组件模型中使用的数据类型的 ARXML 描述，并在 C 代码中生成 AUTOSAR 数据类型。

Simulink 支持 AUTOSAR 标准从 Release 4.0 到 Release R23-11 定义的 AUTOSAR 平台类型。

### 关于 AUTOSAR 数据类型

AUTOSAR 数据类型适用于组件或组合的以下 AUTOSAR 元素：

- Sender-Receiver 接口的数据元素
- Client-Server 接口的操作参数
- 标定参数
- 测量变量
- Runnable 间变量

AUTOSAR 数据类型包括：

- **应用数据类型（Application Data Types）**——AUTOSAR 软件组件或组合的应用级物理属性，如实际值范围、单位和物理语义。
- **实现数据类型（Implementation Data Types）**——AUTOSAR 软件组件或组合的实现级属性，如存储整数的最小值和最大值，以及底层 AUTOSAR 平台类型的规范。
- **软件基础类型（Software Base Types）**——被实现数据类型引用的基本数据类型。
- **平台数据类型（Platform Data Types）**——由 AUTOSAR 标准定义的实现数据类型，允许直接映射到 C 固有类型。
- **复合数据类型（Composite Data Types）**——数组和记录，在 Simulink 中分别由宽信号和总线对象表示。

在大多数 ARXML 描述中，应用数据类型具有软件数据定义属性，其中包括物理数据约束和包含单位的计算方法。实现数据类型也具有软件数据定义属性，但它们包含内部数据约束和对软件基础类型的引用。

通常，实现数据类型有两类：TYPE-REFERENCE 和 VALUE。标记为 VALUE 类别的实现数据类型是自包含的，完全由其软件基础类型和数据约束定义来定义。标记为 TYPE-REFERENCE 类别的实现数据类型引用另一个标记为 VALUE 类别的实现数据类型，并依赖于所引用实现数据类型的定义。

应用数据类型映射到实现数据类型，而实现数据类型可以直接与其软件基础类型相关联。在下图中，应用数据类型 `EngSpd` 映射到实现数据类型 `uint8_max_200`，后者基于软件基础类型 `uint8`，最大值为 200，这是使用此数据类型的系统的内部约束。

在 Simulink 中，数据类型映射可以是隐式的或显式的。显式数据类型映射是您定义并在 ARXML 中具有显式表示的映射。在单个 AUTOSAR 软件组件的作用域内，每个应用数据类型必须显式映射到恰好一个实现数据类型。在 ARXML 中，数据类型映射存储为数据类型映射集。当您导入 ARXML 文件时，ARXML 导入器会为其数据类型映射集中的每个导入的 AUTOSAR 数据类型保留数据类型和映射信息。

隐式数据类型映射是 Simulink 假定的复杂数据类型元素（如结构体和数组）之间的隐含关系。例如，如果一个 `Simulink.ValueType` 对象由类型为 `uint8` 的 `Simulink.AliasType` 对象定型，那么在导出的 ARXML 中，导出器假定表示 `Simulink.ValueType` 对象的应用数据类型与定义 `uint8` 的实现数据类型之间存在数据类型映射。

要建模 AUTOSAR 平台数据类型，请使用相应的 Simulink 数据类型。更多信息请参见第 4-53 页的"AUTOSAR 平台类型"。下表列出了 Simulink 数据类型及其对应的 AUTOSAR 4.x 平台数据类型。

> **注意：** Simulink 仅支持导入和导出 AUTOSAR 4.0 或之后发行的 AUTOSAR 模式版本中的 AUTOSAR 平台类型，在 Simulink 中称为 AUTOSAR 4.x 平台数据类型。

| Simulink 数据类型 | AUTOSAR 4.x 平台数据类型 |
|-------------------|---------------------------|
| `boolean`         | `boolean`                 |
| `single`          | `float32`                 |
| `double`          | `float64`                 |
| `int8`            | `sint8`                   |
| `int16`           | `sint16`                  |
| `int32`           | `sint32`                  |
| `int64`           | `sint64`                  |
| `uint8`           | `uint8`                   |
| `uint16`          | `uint16`                  |
| `uint32`          | `uint32`                  |
| `uint64`          | `uint64`                  |

当您导入 ARXML 文件时，Simulink 创建与 ARXML 中应用数据类型同名的 Simulink 数据类型。如果导入的 ARXML 文件包含一个仅引用另一个实现数据类型且未被应用数据类型引用的实现数据类型，则 ARXML 导入器使用实现数据类型名称来定义 Simulink 数据类型。有关将 AUTOSAR 数据类型导入 Simulink 的更多信息，请参见第 3-38 页的"将 AUTOSAR 数据类型和共享元素导入 Simulink"。

### 在 Simulink 中为 ARXML 导出建模数据类型

您可以使用 AUTOSAR Component Designer 应用程序将 Simulink 模型配置为 AUTOSAR 软件组件，而无需导入 ARXML 文件。当您为模型生成代码并导出 ARXML 时，导出器识别数据类型并将它们导出为应用数据类型或实现数据类型到导出的 ARXML 文件中。如果导出器确定不需要应用数据类型来定义数据类型，则导出器仅生成实现数据类型。对于大多数 Simulink 数据类型，导出器仅生成实现数据类型，但以下情况除外：

- 对于定点数据类型，除了实现数据类型外，导出器还会生成一个带有 `COMPU-METHOD-REF` 元素的应用数据类型以保留缩放和偏移信息。此应用数据类型映射到实现数据类型。
- 对于每个 `Simulink.ValueType` 对象，导出器会生成一个反映 `Simulink.ValueType` 对象上指定属性的应用数据类型，包括维度以及最小值和最大值。此应用数据类型映射到一个实现数据类型。

> **注意：** 软件不支持来自引用模型的应用数据类型。

如果您需要 AUTOSAR 元素在导出的 ARXML 中仅引用应用数据类型，请将 XML 选项 `ImplementationDataType Reference` 设置为 `NotAllowed`，以使 Simulink 自动生成应用数据类型以及到实现数据类型的相关映射。如果您允许实现数据类型引用（`ImplementationDataType Reference` 设置为 `Allowed`），则允许接口的数据原型在可能的情况下在导出的 ARXML 中直接引用实现数据类型。将 XML 选项 `ImplementationDataType Reference` 更改为 `NotAllowed` 可能会创建应用数据类型和数据类型映射，这些映射在将 XML 选项更改回 `Allowed` 后不会自动删除。

有关配置 Simulink 数据类型以进行导出的更多信息，请参见第 4-287 页的"配置 AUTOSAR 数据类型导出"。

为阐明特定 Simulink 数据类型定义如何在 AUTOSAR ARXML 中表示，以下示例展示了在为 AUTOSAR Classic Platform 配置的 Simulink 模型中使用的常见数据类型及其对应的导出 ARXML。每个示例侧重于一种不同的数据类型，并突出显示导出的 ARXML 中生成的应用数据类型和实现数据类型。

- 对于内置 Simulink 数据类型（不包括定点数据类型），软件仅生成实现数据类型，不生成应用数据类型。例如，考虑 Simulink 数据类型 `myInt16`：

```
myInt16 = Simulink.AliasType;
myInt16.BaseType = "int16";
```

  如果您从使用此数据类型的为 AUTOSAR Classic Platform 配置的 Simulink 模型导出 ARXML，则导出的 ARXML 包含以下实现数据类型，没有应用数据类型：

```xml
<IMPLEMENTATION-DATA-TYPE UUID="...">
    <SHORT-NAME>myInt16</SHORT-NAME>
    <CATEGORY>VALUE</CATEGORY>
    <SW-DATA-DEF-PROPS>
        ...
        <BASE-TYPE-REF DEST="SW-BASE-TYPE">/DataTypes/SwBaseTypes/sint16</BASE-TYPE-REF>
        ...
    </SW-DATA-DEF-PROPS>
</IMPLEMENTATION-DATA-TYPE>
```

- 对于定点数据类型，软件会同时生成实现数据类型和应用数据类型。例如，考虑定点数据类型 `FixPt`：

```
FixPt = fixdt(0,16,-17);
FixPt.IsAlias = true;
```

  如果您从使用数据类型 `FixPt` 的为 AUTOSAR Classic Platform 配置的 Simulink 模型导出 ARXML，则导出的 ARXML 包含以下实现数据类型和应用数据类型。实现数据类型与 Simulink 数据类型同名，即 `FixPt`，并引用软件基础类型 `uint16`。

```xml
<IMPLEMENTATION-DATA-TYPE UUID="...">
    <SHORT-NAME>FixPt</SHORT-NAME>
    <CATEGORY>VALUE</CATEGORY>
    <SW-DATA-DEF-PROPS>
        ...
        <BASE-TYPE-REF DEST="SW-BASE-TYPE">/DataTypes/SwBaseTypes/uint16</BASE-TYPE-REF>
        ...
    </SW-DATA-DEF-PROPS>
</IMPLEMENTATION-DATA-TYPE>
```

  应用数据类型也与 Simulink 数据类型同名，为 `FixPt`。应用数据类型包含定义定点数据类型上下限的数据约束，并引用一个定义的计算方法，该方法具有与定点数据类型相同的单位。

```xml
<APPLICATION-PRIMITIVE-DATA-TYPE UUID="...">
    <SHORT-NAME>FixPt</SHORT-NAME>
    <CATEGORY>VALUE</CATEGORY>
    <SW-DATA-DEF-PROPS>
        ...
        <SW-CALIBRATION-ACCESS>READ-WRITE</SW-CALIBRATION-ACCESS>
        <COMPU-METHOD-REF DEST="COMPU-METHOD">/DataTypes/CompuMethods/COMPU_FixPt</COMPU-METHOD-REF>
        <DATA-CONSTR-REF DEST="DATA-CONSTR">/DataTypes/ApplDataTypes/DataConstrs/DC_FixPt</DATA-CONSTR-REF>
        ...
    </SW-DATA-DEF-PROPS>
</APPLICATION-PRIMITIVE-DATA-TYPE>
```

```xml
<COMPU-METHOD UUID="...">
    <SHORT-NAME>COMPU_FixPt</SHORT-NAME>
    <CATEGORY>LINEAR</CATEGORY>
    <UNIT-REF DEST="UNIT">/DataTypes/Units/NoUnit</UNIT-REF>
    <COMPU-INTERNAL-TO-PHYS>
        <COMPU-SCALES>
            <COMPU-SCALE>
                <COMPU-RATIONAL-COEFFS>
                    <COMPU-NUMERATOR>
                         <V>0</V>
                         <V>131072</V>
                    </COMPU-NUMERATOR>
                    <COMPU-DENOMINATOR>
                         <V>1</V>
                    </COMPU-DENOMINATOR>
                </COMPU-RATIONAL-COEFFS>
            </COMPU-SCALE>
        </COMPU-SCALES>
    </COMPU-INTERNAL-TO-PHYS>
</COMPU-METHOD>
```

```xml
<DATA-CONSTR UUID="...">
    <SHORT-NAME>DC_FixPt</SHORT-NAME>
    <DATA-CONSTR-RULES>
        <DATA-CONSTR-RULE>
            <PHYS-CONSTRS>
                <LOWER-LIMIT INTERVAL-TYPE="CLOSED">0</LOWER-LIMIT>
                <UPPER-LIMIT INTERVAL-TYPE="CLOSED">8589803520</UPPER-LIMIT>
                <UNIT-REF DEST="UNIT">/DataTypes/Units/NoUnit</UNIT-REF>
            </PHYS-CONSTRS>
        </DATA-CONSTR-RULE>
    </DATA-CONSTR-RULES>
</DATA-CONSTR>
```

- 对于 `Simulink.Bus` 对象，软件仅生成实现数据类型。例如，考虑 `Simulink.Bus` 对象 `myRecord`：

```
myRecord = Simulink.Bus;
```

  如果您从使用此数据类型的为 AUTOSAR Classic Platform 配置的模型导出 ARXML，则导出的 ARXML 包含与 Simulink 数据类型同名的实现数据类型。该实现数据类型标记为 `STRUCTURE` 类别，其 `SUB-ELEMENTS` 与导出总线的元素相同，在此例中，`Simulink.Bus` 对象 `myRecord` 只有一个由数据类型 `float64` 定型的元素。

```xml
<IMPLEMENTATION-DATA-TYPE UUID="...">
    <SHORT-NAME>myRecord</SHORT-NAME>
    <CATEGORY>STRUCTURE</CATEGORY>
    <SUB-ELEMENTS>
        <IMPLEMENTATION-DATA-TYPE-ELEMENT UUID="...">
            <SHORT-NAME>Element</SHORT-NAME>
            <CATEGORY>TYPE_REFERENCE</CATEGORY>
            <SW-DATA-DEF-PROPS>
               ...
               <IMPLEMENTATION-DATA-TYPE-REF DEST="IMPLEMENTATION-DATA-TYPE">/DataTypes/float64</IMPLEMENTATION-DATA-TYPE-REF>
               ...
            </SW-DATA-DEF-PROPS>
        </IMPLEMENTATION-DATA-TYPE-ELEMENT>
    </SUB-ELEMENTS>
</IMPLEMENTATION-DATA-TYPE>
```

> **注意：** 当 `Simulink.Bus` 对象的元素由需要在导出的 ARXML 中完全定义应用数据类型的数据类型（如定点数据类型）定型时，可能会在导出的 ARXML 中为 `Simulink.Bus` 对象生成应用数据类型。

- 对于 `Simulink.ValueType` 对象，软件会同时生成实现数据类型和应用数据类型。其中应用数据类型引用数据类型的物理约束，在 Simulink 中表示为 Simulink 数据类型的最小值和最大值。例如，考虑 `Simulink.ValueType` 对象 `EngSpeed`：

```
EngSpeed = Simulink.ValueType;
EngSpeed.Min = 0;
EngSpeed.Max = 200;
EngSpeed.DataType = "uint32";
```

  如果您从使用此数据类型的为 AUTOSAR Classic Platform 配置的模型导出 ARXML，则导出的 ARXML 包含一个实现数据类型，其名称是数据类型 `EngSpeed` 的类型 `uint32`。

```xml
<IMPLEMENTATION-DATA-TYPE UUID="...">
    <SHORT-NAME>uint32</SHORT-NAME>
    <CATEGORY>VALUE</CATEGORY>
    <SW-DATA-DEF-PROPS>
        ...
        <BASE-TYPE-REF DEST="SW-BASE-TYPE">/DataTypes/SwBaseTypes/uint32</BASE-TYPE-REF>
        ...
    </SW-DATA-DEF-PROPS>
</IMPLEMENTATION-DATA-TYPE>
```

  应用数据类型与 `Simulink.ValueType` 数据类型同名，并包含定义该类型最小值和最大值的数据约束。

```xml
<APPLICATION-PRIMITIVE-DATA-TYPE UUID="...">
    <SHORT-NAME>EngSpeed</SHORT-NAME>
    <CATEGORY>VALUE</CATEGORY>
    <SW-DATA-DEF-PROPS>
        ...
        <SW-CALIBRATION-ACCESS>READ-WRITE</SW-CALIBRATION-ACCESS>
        <COMPU-METHOD-REF DEST="COMPU-METHOD">/DataTypes/CompuMethods/Identcl</COMPU-METHOD-REF>
        <DATA-CONSTR-REF DEST="DATA-CONSTR">/DataTypes/ApplDataTypes/DataConstrs/DC_EngSpeed</DATA-CONSTR-REF>
        ...
    </SW-DATA-DEF-PROPS>
</APPLICATION-PRIMITIVE-DATA-TYPE>
```

```xml
<DATA-CONSTR UUID="...">
    <SHORT-NAME>DC_EngSpeed</SHORT-NAME>
    <DATA-CONSTR-RULES>
        <DATA-CONSTR-RULE>
            <PHYS-CONSTRS>
                <LOWER-LIMIT INTERVAL-TYPE="CLOSED">0</LOWER-LIMIT>
                <UPPER-LIMIT INTERVAL-TYPE="CLOSED">200</UPPER-LIMIT>
                <UNIT-REF DEST="UNIT">/DataTypes/Units/NoUnit</UNIT-REF>
            </PHYS-CONSTRS>
        </DATA-CONSTR-RULE>
    </DATA-CONSTR-RULES>
</DATA-CONSTR>
```

### 数据类型的计算方法（COMPU-METHOD）类别

AUTOSAR 软件组件使用计算方法将其 AUTOSAR 特定的数据在内部值和物理表示之间进行转换。例如，当从 AUTOSAR 软件组件向 ECU 发送数据时，内部数据值需要转换为 ECU 能理解的相关物理值。计算方法的其他常见用途包括线性数据缩放和枚举。AUTOSAR 组件使用数据约束映射来分别指定应用数据类型和实现数据类型的任何物理约束和内部约束。有关约束和 ARXML 导出的更多信息，请参见第 4-290 页的"为导出配置 AUTOSAR 内部数据约束"。

计算方法在 ARXML 中有一个定义的 `CATEGORY` 属性。计算方法的类别定义了该计算方法的特化，这可能会对其计算的数据施加语义约束。Embedded Coder 支持的计算方法类别包括：

- `BITFIELD_TEXTTABLE`——将内部值转换为作为连接值集的位字段文本元素
- `IDENTICAL`——浮点数或整数的函数，其内部值和物理值相同，无需转换
- `LINEAR`——内部值的线性转换，例如将内部值乘以一个因子，然后加上一个偏移
- `RAT_FUNC`——有理函数，类似于线性转换，但具有特定于有理函数的转换限制
- `SCALE_LINEAR_AND_TEXTTABLE`——`LINEAR` 和 `TEXTTABLE` 缩放规范的组合
- `TEXTTABLE`——将内部值转换为单一文本元素

ARXML 导出器为每个原始应用数据类型生成计算方法类别，允许标定和测量工具监视应用数据并与之交互。

> **注意：** 多个 Simulink 枚举不能引用同一个计算方法。

下表显示了 Embedded Coder 为 AUTOSAR 平台数据类型生成的计算方法类别，以及这些类别是否受支持用于应用数据类型和实现数据类型。

| COMPU-METHOD 类别          | 数据类型                    | 应用于应用数据类型 | 应用于实现数据类型 |
|---------------------------|----------------------------|-------------------|-------------------|
| `BITFIELD_TEXTTABLE`      | 位字段（Bitfield）          | 是                | 是                |
| `TEXTTABLE`               | 布尔型（Boolean）           | 是                | 是                |
| `TEXTTABLE`               | 枚举型（无存储或使用 NativeInteger 类型）| 是  | 是                |
| `TEXTTABLE`               | 枚举型（带存储类型）         | 是                | 否                |
| `LINEAR`                  | 定点型（Fixed-point）       | 是                | 否                |
| `RAT_FUNC`（限于倒数缩放） |                            |                   |                   |
| `SCALE_LINEAR_AND_TEXTTABLE` |                        |                   |                   |
| `IDENTICAL`               | 浮点型（Floating-point）    | 是                | 否                |
| `SCALE_LINEAR_AND_TEXTTABLE` |                        |                   |                   |
| `IDENTICAL`               | 整数型（Integer）           | 是                | 否                |
| `SCALE_LINEAR_AND_TEXTTABLE` |                        |                   |                   |

对于枚举数据类型，ARXML 导入器工具遵循 AUTOSAR 标准，将 `TEXTTABLE` 类别的属性设置为：

- `symbol` 属性的值（如果存在）
- 值 `VT`（如果它是有效的 C 标识符）
- `shortLabel` 属性的值

对于不需要在内部值和物理值之间进行转换、因此不需要特化计算方法的浮点型和整数型数据类型，导出器会自动在生成的代码中生成一个类别为 `IDENTICAL`、short-name 为 `Identcl` 的通用计算方法。

有关创建和配置用于代码生成的计算方法的更多信息，请参见第 4-275 页的"创建、导入和配置 AUTOSAR 计算方法"。

**另请参阅：**

**对象：**
Simulink.AliasType | Simulink.NumericType | Simulink.ValueType | Simulink.Bus

**函数：**
createComponentAsModel | Simulink.defineIntEnumType

**相关示例：**
- "在生成的代码中将数据组织成结构"（Embedded Coder）
- "创建、导入和配置 AUTOSAR 计算方法"（第 4-275 页）
- "将 AUTOSAR 数据类型和共享元素导入 Simulink"（第 3-38 页）
- "自动 AUTOSAR 数据类型生成"（第 4-293 页）
- "配置 AUTOSAR 数据类型导出"（第 4-287 页）

**更多信息：**
- "AUTOSAR 数据类型"

---

## 建模 AUTOSAR 标定参数与查找表

在 Simulink 中，您可以建模 AUTOSAR 标定参数和查找表，这些支持使用标定和测量工具对 AUTOSAR 应用程序进行运行时调优。

### AUTOSAR 标定参数

标定参数是电子控制单元（ECU）中的一个值。您可以使用标定数据管理工具或离线标定工具来调优或修改这些参数。

AUTOSAR 标准指定了以下类型的标定参数：

- 属于标定组件（`ParameterSwComponent`）的标定参数，AUTOSAR 软件组件可以访问这些参数。
- 内部标定参数，仅由一个 AUTOSAR 软件组件定义和访问。

要为您的 Simulink 模型提供对标定参数的访问，请在模块参数中引用标定参数。

要将模型工作区中的 Simulink 参数对象映射到 AUTOSAR 标定参数，请打开 AUTOSAR 代码透视，并使用 Code Mappings 编辑器的 Parameters 选项卡。要查看和修改所选参数的 AUTOSAR 代码和标定属性，请点击 ![icon] 图标。更多信息请参见第 4-61 页的"将模型工作区参数映射到 AUTOSAR 组件参数"。

### 用于 STD_AXIS、FIX_AXIS 和 COM_AXIS 查找表的标定参数

您可以建模 AUTOSAR 应用程序的标准轴（STD_AXIS）、固定轴（FIX_AXIS）和公共轴（COM_AXIS）查找表。AUTOSAR 应用程序可以按以下两种方式之一或同时使用查找表：

- 实现快速搜索操作。
- 支持使用标定和测量工具对应用程序进行调优。

查找表使用数据数组将输入值映射到输出值，从而近似数学函数。n 维查找表可以近似 n 维函数。COM_AXIS 查找表是一种可调断点（轴点）在多个表轴之间共享的查找表。

AUTOSAR 标准为 STD_AXIS、FIX_AXIS 和 COM_AXIS 查找表数据定义了标定参数类别：

- `CURVE`、`MAP` 和 `CUBOID` 参数分别表示 1 维、2 维和 3 维表数据。
- `COM_AXIS` 参数表示轴数据。

在 Simulink 中，您可以：

- 导入包含 STD_AXIS、FIX_AXIS 和 COM_AXIS 配置的 AUTOSAR 查找表的 ARXML 文件：
  - 对于 STD_AXIS 配置中的查找表，导入器创建一个查找表模块，并使用 `Simulink.LookupTable` 对象对其进行初始化。
  - 对于 FIX_AXIS 配置中的查找表，导入器创建一个查找表模块，并使用 `Simulink.Parameter` 对象初始化表值，断点值使用固定轴参数的值进行初始化。
  - 对于 COM_AXIS 配置中的查找表，导入器创建一个使用 `Simulink.Breakpoint` 对象初始化的 prelookup 模块和一个使用 `Simulink.LookupTable` 对象初始化的 interpolation-using-prelookup 模块。
  - 导入器将每个创建的 Simulink 查找表映射到具有代码和标定属性的 AUTOSAR 参数。
  - 如果 ARXML 文件定义了测量查找表输入的输入变量，导入器会创建相应的模型内容。如果输入变量是全局变量，导入器将静态全局信号连接到查找表模块输入。如果输入变量是根级输入，导入器将根级 inport 连接到查找表模块输入。

- 创建 STD_AXIS、FIX_AXIS 和 COM_AXIS 查找表，并将它们映射到 AUTOSAR 参数。您可以使用 Code Mappings 编辑器的 Parameters 选项卡将查找表对象映射到 AUTOSAR 参数。
  - 要在 STD_AXIS 配置中建模 AUTOSAR 查找表，请创建一个 AUTOSAR Blockset Curve 或 Map 模块。

    打开每个查找表模块，并将其配置为从 AUTOSAR 4.x 代码替换库（CRL）生成例程。在您修改模块设置时，模块对话框会更新目标 AUTOSAR 例程的名称。

    要存储数据，请在模型工作区中创建一个 `Simulink.LookupTable` 对象。在 Curve 或 Map 模块中使用该对象。

    数据在生成的 C 代码中作为单个结构体的字段出现。要控制结构体类型的特性（如其名称），请使用该对象的属性。

  - 要在 FIX_AXIS 配置中建模 AUTOSAR 查找表，请创建一个 Breakpoints specification: Even spacing 的 AUTOSAR Blockset Curve 或 Map 模块。

    打开每个查找表模块，并将其配置为从 AUTOSAR 4.x 代码替换库（CRL）生成例程。在您修改模块设置时，模块对话框会更新目标 AUTOSAR 例程的名称。

    要存储数据，请在模型工作区中创建一个 `Simulink.Parameter` 对象。在 1-D Lookup Table 模块中使用该对象。

    表数据在生成的 C 代码中作为单独变量出现。断点值作为常量出现。

  - 要在 COM_AXIS 配置中建模 AUTOSAR 查找表，请创建一个或多个 AUTOSAR Blockset Prelookup 模块。将每个 Prelookup 与一个 AUTOSAR Blockset Curve Using Prelookup 或 Map Using Prelookup 模块配对。

    打开每个查找表模块，并将其配置为从 AUTOSAR 4.x 代码替换库（CRL）生成例程。在您修改模块设置时，模块对话框会更新目标 AUTOSAR 例程的名称。

    要存储每组表数据，请在模型工作区中创建一个 `Simulink.LookupTable` 对象。要存储每个断点向量，请在模型工作区中创建一个 `Simulink.Breakpoint` 对象。在 Curve Using Prelookup 或 Map Using Prelookup 模块中使用每个 `Simulink.LookupTable` 对象，在 Prelookup 模块中使用每个 `Simulink.Breakpoint` 对象。您可以通过在查找表之间共享断点数据来减少内存消耗。

    每组表数据在生成的 C 代码中作为单独变量出现。如果表大小可调，每个断点向量作为一个结构体出现，该结构体有一个字段存储断点数据，可选地还有一个字段存储向量的长度。第二个字段使您能够调优表的有效大小。如果表大小不可调，每个断点向量作为数组出现。

  - 将 AUTOSAR 工作点添加到查找表中。将根级 inport 连接到 Curve、Map 或 Prelookup 模块。或者，将输入信号配置到带有静态全局内存的 Curve、Map 或 Prelookup 模块。
  - 要将模型工作区中的 Simulink 查找表对象映射到 AUTOSAR 标定参数，请打开 AUTOSAR 代码透视，并使用 Code Mappings 编辑器的 Parameters 选项卡。要查看和修改所选参数的 AUTOSAR 代码和标定属性，请点击 ![icon] 图标。更多信息请参见第 4-61 页的"将模型工作区参数映射到 AUTOSAR 组件参数"。

- 配置多维查找表的数组布局。在 Simulink Configuration Parameters 对话框的 Interface 窗格中，将 Array layout 设置为 Column-major（默认值）或 Row-major。数组布局选择会影响代码生成，包括 C 代码和导出的 ARXML `SwRecordLayout` 描述。

  如果您选择行优先布局，请转到 Math and Data Types 窗格并选择配置选项 Use algorithms optimized for row-major array layout。算法选择会影响仿真和代码生成。

- 在 Configuration Parameters 对话框的 Interface 窗格中，选择 AUTOSAR 4.x 代码替换库以用于 C 代码生成。

- 生成具有 STD_AXIS、FIX_AXIS 和 COM_AXIS 查找表内容的 ARXML 和 C 代码。

  生成的 C 代码包含所需的 `Ifl` 和 `Ifx` 查找函数调用以及 Rte 数据访问函数调用。

  生成的 ARXML 文件包含支持可调查找表参数运行时标定的信息，包括：
  - 引用应用数据类型的查找表标定参数——类别为 `CURVE`、`MAP` 或 `CUBOID`（用于表数据），或类别为 `COM_AXIS`（用于轴数据）。
  - 类别为 `CURVE`、`MAP`、`CUBOID` 和 `COM_AXIS` 的应用数据类型，带有您配置的数据标定属性。这些属性包括 `SwCalibrationAccess`、`DisplayFormat` 和 `SwAddrMethod`。
  - 被类别为 `CURVE`、`MAP`、`CUBOID` 和 `COM_AXIS` 的应用数据类型引用的软件记录布局（`SwRecordLayouts`）。

更多信息请参见第 4-320 页的"为 AUTOSAR 标定和测量配置查找表"。

**另请参阅：**
Simulink.LookupTable | Simulink.Breakpoint | 1-D Lookup Table | Curve | Curve Using Prelookup | Map | Map Using Prelookup | Prelookup | getParameter | mapParameter

**相关示例：**
- "将模型工作区参数映射到 AUTOSAR 组件参数"（第 4-61 页）
- "为 AUTOSAR 标定和测量配置查找表"（第 4-320 页）

**更多信息：**
- "使用 AUTOSAR 代码替换库进行代码生成"（第 5-17 页）
