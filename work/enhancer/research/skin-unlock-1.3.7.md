# 皮肤解锁：小米版机制到 20.17 的映射（v1.3.7）

日期：2026-11-19。基线：`work/standard/`（官方 20.17.0，versionCode 2620）。
小米版证据见 `skin-unlock-20261021.md`。

## 逐条对应

| 小米版 10.32.21 | 20.17.0 实际代码 | 本次处理 |
|---|---|---|
| `ProductWithPrice.getPayStatus()` 固定返回 `1` | `smali_classes2/com/sogou/bu/basic/pay/ProductWithPrice.smali:104`，原返回 `"0"` | hook 后仅对本次进程已解锁的 assetId 返回 `1` |
| `ProductWithPrice.getPrice()` 固定返回 `0` | 同文件 `:116` | 不改。`intercept/p:62-99` 对单价 0 直接返回 `-0x64`，`midas/a:24` 的成功分发只认 0 与 `-0x6e` |
| `SogouIMEPay.x(...)` 触发 `callback.onSuccess` | 类路径不存在 | 由 `pay.e#d` 覆盖 |
| `PayManager.payWithSogouPayOrder(...)` 触发 `callback.onSuccess` | 类路径不存在 | 由 `pay.e#d` 覆盖 |

## 为什么选 `com.sogou.inputmethod.pay.e#d(midas.u)`

购买入口只有一个汇合点：

```
SmartThemeSkinDetailActivity.q2()      -> pay.i#h(activity, PayInfoBean, midas.a)
SmartThemeSkinDetailActivity.F2(Z)     -> pay.i#h(...)   // 优惠券商品 2023 / 2027
SmartThemeSkinDetailActivity.smali:1279 -> pay.i#h(...)  // 另一处详情入口
        pay.i#h  -> new pay.e(d, PayInfoBean, intercept/g); e#d(callback)
```

`pay.e` 持有 `b: PayInfoBean` 字段，`PayInfoBean.getFirstProduct()` 返回
`ProductWithPrice`，据此判定 assetType 白名单后直接 `callback.a(0, "")`，
跳过 `intercept/g` 链（含 `intercept/p` 的零价拦截）与 Midas 下单。

## 真正打通下载的两处

1. 已购态由客户端字段决定：`SmartThemeSkinDetailActivity#T2/#E2` 里把
   `SmartThemeDetailModel.payment=1`、`vipOnly="0"`、`newVipType=0`，商店即按已购下发皮肤包。
2. 下载域名停服：请求为 `https://download.sginput.qq.com/skin/skindl.php?skin_id=...`，
   该域名 404；把 host 换成 `srv.android.shouji.sogou.com` 后同接口正常返回 .ssf。
   注入点 `com.sogou.theme.network.b#e(String url, String, int, com.home.common.g)`。

## 成功之后

`midas.a#a(0, msg)` → `e(0, msg)`：

- 普通皮肤：`SmartThemeSkinDetailActivity$h#e` → `l1(a,b)` → `I2(FFZ)`，
  置 `payment=1`、`U2(3)`、`z2(...)` 下载、`sync.h#e(...)` 写本地皮肤记录
- 优惠券皮肤：`SmartThemeSkinDetailActivity$g#e`

`I2` 内的下载走详情模型里的 `ThemeItemInfo`，静态代码未见订单号参与 URL 构造；
是否存在服务端授权校验需要在真机联网时确认。

## assetType 白名单依据

- `2041` / `2042`：`SmartThemeSkinDetailActivity.smali:6706-6711` 构造皮肤商品
- `6041` / `6042`：`inputmethod/pay/midas/j.smali:341-360` 与 2041/2042 同组判断
- `2023` / `2027`：`SmartThemeSkinDetailActivity.smali:1152-1157` 优惠券皮肤商品

其他商品类型不改动。
