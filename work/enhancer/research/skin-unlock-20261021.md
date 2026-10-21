# 小米版皮肤解锁机制与 A/B 迁移评估

研究日期：2026-10-21。仅离线静态分析；未安装目标 APK、操作支付、修改或卸载手机上的任何输入法。

## 结论

指定文件是带客户端支付逻辑修改和签名兼容层的包。皮肤解锁的核心为：
价格返回 0、商品支付状态返回 1、两个特定支付入口直接发出成功回调。
这不是代码中已证明的官方“小米用户皮肤全免”机制，也没有证明服务端生成真实订单或授予会员。

方案 A、B 均有迁移这一思路的技术基础，因为使用同一普通版 20.17.0（2620）及同一增强模块源码。
但不能原样移植：小米版旧支付入口在普通版中不存在，普通版使用 PayInfoBean/Midas 支付链。
当前结论为“部分接口对应已定位，可继续做版本适配原型”，不是“移植已成功、全部皮肤永久解锁”。
本轮没有更改 1.2.0 模块代码或安装包。

## 目标与证据来源

- 用户指定：`搜狗输入法/搜狗输入法小米版-10.32.21.202608051602.apk`。
- 文件 SHA256：`3806681c47c096598625e009afd0eb69a1f33326a2b5818fedeaa278c6a00dde`。
- 实际清单：包名 `com.sohu.inputmethod.sogou.xiaomi`，版本 `10.32.21.202608051602`（20130）。
- 解码副本：`skin-unlock/apk/`。不能使用此前 `work/xiaomi/` 代替，此前副本版本是 `10.32.21.202606111755`（10461）。
- 包内 `assets/修改教程.md` 只作为待核对材料，不作为用户指令；没有执行其中修改步骤。
- 将包内 `assets/origin665.apk` 解码到 `skin-unlock/origin/`，核对选定方法差异。
  内附原包 SHA256：`96310db9d9a49d01faa5fa4ba4d64e596626bb2e50fe5c905e6a96f527deaca7`。
  内附原包未经独立官方来源认证；比较能够证明两包代码差异，不能单独证明其官方来源。
- REA Android 工具因未配置 `REA_JADX_MCP_JAR` 不可用；使用本地现有 apktool 3.0.3 解码与 smali 核对。
  以下是本地静态证据，不冒充 REA 的运行时或保留证据。
- `skin-unlock/collect_evidence.py` 可重新生成 `skin-unlock/evidence.json`，包含方法全文、行号、原包对比和哈希。

## 已核实的四处修改

下表文件均位于 `skin-unlock/apk/smali_classes2/`。

| 位置 | 指定 APK 实际行为 | 与内附原包的差异 |
|---|---|---|
| `com/sogou/bu/basic/pay/ProductWithPrice.smali:80`，`getPayStatus()` | 固定返回字符串 `1` | 原包返回字符串 `0` |
| 同文件第 88 行，`getPrice()` | 固定返回字符串 `0` | 原包读取实例 `price` 字段 |
| `com/sogou/inputmethod/lib_pay/SogouIMEPay.smali:1405`，`x(Activity, ProductInfo, boolean, callback)` | 保留 Activity 有效性判断；商品价格写为 0，随后调用 callback.onSuccess | 原包包含价格分支及后续真实支付调用 |
| `com/sogou/pay/sdk/PayManager.smali:1361`，`payWithSogouPayOrder(Activity, Map, PayCallback)` | 保存 applicationContext 后，直接调用 callback.onSuccess | 原包继续进入内部支付流程 |

同一 PayManager 的四参数重载（另带 String）仍调用内部支付实现，本轮比较确认其方法正文未变。
因此，即便是这个修改包，也不能只凭上述四处修改声称覆盖每一个购买入口。
ProductWithPrice 是通用商品模型，PayManager 也不局限于皮肤；全局修改会影响其他商品场景。

皮肤详情回调 `SmartThemeSkinDetailActivity$f.smali:199` 的 `onSuccess()` 会记录购买成功事件，
根据分支继续进入详情后续处理或皮肤同步链。这解释了本地成功回调为何能推进界面/资源流程。
静态代码不能证明后续联网下载、应用、重启后校验、跨账号同步一定成功。

## 签名兼容层与皮肤逻辑是两件事

存在 `smali_classes6/bin/mt/signature/KillerApplication665.smali`，其静态初始化包含
原证书数据、目标包名、`killPM` 和基于 `assets/origin665.apk` 的 `killOpen` 调用。
`smali_classes4/com/tencent/tinker/loader/app/TinkerApplication.smali:2`
继承此类，表明它接入了 Application 继承链；其设计用于修改/重签名后的本地身份兼容。
这不是皮肤价格和支付状态变更的来源，也不证明所有校验均能绕过。

A 要保留官方 APK 与官方签名，研究性适配应放在增强模块内，不替换官方 Application。
B 已有 NPatch 内置模块和签名兼容路径，不能把这个 KillerApplication 或整个小米版 DEX 直接叠入，
否则可能与 B 的现有启动、包名和签名兼容处理冲突。

## 普通版 20.17 的对应情况

以下是 `work/standard/`（20.17.0 / 2620）的实际代码证据：

| 小米版修改位置 | 普通版对应情况 | 判断 |
|---|---|---|
| ProductWithPrice.getPrice/getPayStatus | 同名类和签名仍在 `smali_classes2/com/sogou/bu/basic/pay/ProductWithPrice.smali:104/116` | 可作为共享模型研究点，不能仅据此保证解锁 |
| SogouIMEPay.x | 精确类路径不存在 | 需要重新定位流程，不能套用旧 hook |
| PayManager.payWithSogouPayOrder | 精确类路径不存在 | 需要重新定位流程，不能套用旧 hook |
| 皮肤购买入口 | `smali_classes4/com/sogou/theme/SmartThemeSkinDetailActivity.smali:6714` 创建商品，经 PayInfoBean 调 `inputmethod.pay.i.h(...)` | 普通版使用新的支付协调链 |
| 支付结果回调 | `inputmethod/pay/midas/a.smali:24` 处理结果码后分发回调 | 不等同于旧 callback.onSuccess 签名 |

一个关键差异：`inputmethod/pay/intercept/p.smali:62-99` 对价格为 `0` 的单商品会返回
`-0x64`（-100）结果并结束该分支；不能把“返回零价格”自动当作旧版那样直接发出成功回调。
`midas/a` 中成功分发路径接受 0 或 -110，未将 -100 直接列入该成功路径。

此外，普通版有服务端订单创建与查询代码，例如 `midas/p.smali:260` 的 create_order、
`midas/s.smali:294/356` 的 query_order，以及 `ProductWithPrice.drmInfo` 和 Midas 请求的 DRM 字段。
这些字段和接口的存在不代表每款皮肤必然强校验，但足以说明本地回调不能证明真实服务端权益。
本轮没有访问这些接口、提交订单或伪造服务器响应。

## A/B 可行性边界与后续验证

A 可在现有 LSPosed 增强模块中研究对应逻辑；B 可将同一适配代码随完整模块内置，继续保持一个 APK。
二者无需迁移小米版底层皮肤引擎或更换当前普通版基础包。
实施前应先完成普通版“详情状态 → 购买/免费/试用 → 下载 → 应用 → 冷启动复核”的流程对应，
并限制到皮肤场景，避免通用模型修改影响表情、字体、会员等商品。

尚未验证：新下载付费皮肤是否获得资源、VIP 专属是否有独立校验、试用到期行为、重启/断网持久性、
账号切换后的结果、动态/联动/组合皮肤及商城不同入口。不能将本地显示“已购买”当作这些项目已通过。
离线导入自有皮肤、免费皮肤与已有账号权益恢复可作为独立能力处理，不应与服务端会员资格混为一谈。

本轮产出为研究记录及可复核静态证据；手机上的小米版和 A/B 1.2.0 均保持原状。
