.class public Lcom/sogouenhance/AHomeActivity;
.super Landroid/app/Activity;
.implements Landroid/view/View$OnClickListener;

.method public constructor <init>()V
    .locals 0
    invoke-direct {p0}, Landroid/app/Activity;-><init>()V
    return-void
.end method

.method protected onCreate(Landroid/os/Bundle;)V
    .locals 6
    invoke-super {p0, p1}, Landroid/app/Activity;->onCreate(Landroid/os/Bundle;)V
    const-string v0, "搜狗增强 · 方案 A"
    invoke-virtual {p0, v0}, Landroid/app/Activity;->setTitle(Ljava/lang/CharSequence;)V
    new-instance v0, Landroid/widget/ScrollView;
    invoke-direct {v0, p0}, Landroid/widget/ScrollView;-><init>(Landroid/content/Context;)V
    const v1, 0xfff2f3f5
    invoke-virtual {v0, v1}, Landroid/view/View;->setBackgroundColor(I)V
    const/4 v1, 0x1
    invoke-virtual {v0, v1}, Landroid/widget/ScrollView;->setFillViewport(Z)V
    new-instance v2, Landroid/widget/LinearLayout;
    invoke-direct {v2, p0}, Landroid/widget/LinearLayout;-><init>(Landroid/content/Context;)V
    invoke-virtual {v2, v1}, Landroid/widget/LinearLayout;->setOrientation(I)V
    const/16 v3, 0x18
    invoke-direct {p0, v3}, Lcom/sogouenhance/AHomeActivity;->dp(I)I
    move-result v3
    invoke-virtual {v2, v3, v3, v3, v3}, Landroid/view/View;->setPadding(IIII)V
    const-string v3, "搜狗增强 · 方案 A"
    const/high16 v4, 0x41c00000
    invoke-direct {p0, v2, v3, v4}, Lcom/sogouenhance/AHomeActivity;->text(Landroid/widget/LinearLayout;Ljava/lang/String;F)V
    const-string v3, "官方输入法 + 独立增强模块\n\n输入法主页、皮肤和词库在官方搜狗中；本应用负责增强功能设置。"
    const/high16 v4, 0x41800000
    invoke-direct {p0, v2, v3, v4}, Lcom/sogouenhance/AHomeActivity;->text(Landroid/widget/LinearLayout;Ljava/lang/String;F)V
    const-string v3, "打开官方搜狗输入法"
    invoke-direct {p0, v2, v3, v1}, Lcom/sogouenhance/AHomeActivity;->button(Landroid/widget/LinearLayout;Ljava/lang/String;I)V
    const/4 v1, 0x2
    const-string v3, "增强功能设置"
    invoke-direct {p0, v2, v3, v1}, Lcom/sogouenhance/AHomeActivity;->button(Landroid/widget/LinearLayout;Ljava/lang/String;I)V
    const/4 v1, 0x3
    const-string v3, "系统输入法设置"
    invoke-direct {p0, v2, v3, v1}, Lcom/sogouenhance/AHomeActivity;->button(Landroid/widget/LinearLayout;Ljava/lang/String;I)V
    const-string v3, "使用说明\n1. 安装并启用官方搜狗输入法。\n2. 在 LSPosed 启用本模块，作用域仅勾选官方普通版搜狗。\n3. 模块更新后，重启搜狗相关进程或软重启使其生效。\n\n勿将本模块作用于方案 B 或搜狗小米版。\n\n包含原增强功能及全面屏底栏配色适配；本版未加入付费皮肤解锁。"
    const/high16 v4, 0x41600000
    invoke-direct {p0, v2, v3, v4}, Lcom/sogouenhance/AHomeActivity;->text(Landroid/widget/LinearLayout;Ljava/lang/String;F)V
    invoke-virtual {v0, v2}, Landroid/view/ViewGroup;->addView(Landroid/view/View;)V
    invoke-virtual {p0, v0}, Landroid/app/Activity;->setContentView(Landroid/view/View;)V
    return-void
.end method

.method private dp(I)I
    .locals 2
    invoke-virtual {p0}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;
    move-result-object v0
    invoke-virtual {v0}, Landroid/content/res/Resources;->getDisplayMetrics()Landroid/util/DisplayMetrics;
    move-result-object v0
    iget v0, v0, Landroid/util/DisplayMetrics;->density:F
    int-to-float v1, p1
    mul-float/2addr v0, v1
    const/high16 v1, 0x3f000000
    add-float/2addr v0, v1
    float-to-int v0, v0
    return v0
.end method

.method private text(Landroid/widget/LinearLayout;Ljava/lang/String;F)V
    .locals 3
    new-instance v0, Landroid/widget/TextView;
    invoke-direct {v0, p0}, Landroid/widget/TextView;-><init>(Landroid/content/Context;)V
    invoke-virtual {v0, p2}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V
    invoke-virtual {v0, p3}, Landroid/widget/TextView;->setTextSize(F)V
    const v1, 0xff20252c
    invoke-virtual {v0, v1}, Landroid/widget/TextView;->setTextColor(I)V
    const/16 v1, 0x10
    invoke-direct {p0, v1}, Lcom/sogouenhance/AHomeActivity;->dp(I)I
    move-result v1
    const/4 v2, 0x0
    invoke-virtual {v0, v2, v1, v2, v1}, Landroid/view/View;->setPadding(IIII)V
    invoke-virtual {p1, v0}, Landroid/view/ViewGroup;->addView(Landroid/view/View;)V
    return-void
.end method

.method private button(Landroid/widget/LinearLayout;Ljava/lang/String;I)V
    .locals 2
    new-instance v0, Landroid/widget/Button;
    invoke-direct {v0, p0}, Landroid/widget/Button;-><init>(Landroid/content/Context;)V
    invoke-virtual {v0, p2}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V
    invoke-virtual {v0, p3}, Landroid/view/View;->setId(I)V
    const/4 v1, 0x0
    invoke-virtual {v0, v1}, Landroid/widget/TextView;->setAllCaps(Z)V
    invoke-virtual {v0, p0}, Landroid/view/View;->setOnClickListener(Landroid/view/View$OnClickListener;)V
    invoke-virtual {p1, v0}, Landroid/view/ViewGroup;->addView(Landroid/view/View;)V
    return-void
.end method

.method public onClick(Landroid/view/View;)V
    .locals 4
    new-instance v0, Landroid/content/Intent;
    invoke-direct {v0}, Landroid/content/Intent;-><init>()V
    invoke-virtual {p1}, Landroid/view/View;->getId()I
    move-result v1
    const/4 v2, 0x1
    if-ne v1, v2, :settings
    const-string v1, "com.sohu.inputmethod.sogou"
    const-string v2, "com.sohu.inputmethod.sogou.SogouIMELauncher"
    invoke-virtual {v0, v1, v2}, Landroid/content/Intent;->setClassName(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;
    const-string v1, "android.intent.action.MAIN"
    invoke-virtual {v0, v1}, Landroid/content/Intent;->setAction(Ljava/lang/String;)Landroid/content/Intent;
    const-string v1, "android.intent.category.LAUNCHER"
    invoke-virtual {v0, v1}, Landroid/content/Intent;->addCategory(Ljava/lang/String;)Landroid/content/Intent;
    goto :launch
    :settings
    const/4 v2, 0x2
    if-ne v1, v2, :system
    invoke-virtual {p0}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    move-result-object v1
    const-string v2, "com.sogouenhance.SettingsActivity"
    invoke-virtual {v0, v1, v2}, Landroid/content/Intent;->setClassName(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;
    goto :launch
    :system
    const/4 v2, 0x3
    if-ne v1, v2, :done
    const-string v1, "android.settings.INPUT_METHOD_SETTINGS"
    invoke-virtual {v0, v1}, Landroid/content/Intent;->setAction(Ljava/lang/String;)Landroid/content/Intent;
    :launch
    :try_start
    invoke-virtual {p0, v0}, Landroid/app/Activity;->startActivity(Landroid/content/Intent;)V
    :try_end
    .catch Landroid/content/ActivityNotFoundException; {:try_start .. :try_end} :missing
    .catch Ljava/lang/SecurityException; {:try_start .. :try_end} :missing
    goto :done
    :missing
    move-exception v0
    const-string v1, "无法打开，请确认已安装官方普通版搜狗并允许启动。"
    const/4 v2, 0x1
    invoke-static {p0, v1, v2}, Landroid/widget/Toast;->makeText(Landroid/content/Context;Ljava/lang/CharSequence;I)Landroid/widget/Toast;
    move-result-object v0
    invoke-virtual {v0}, Landroid/widget/Toast;->show()V
    :done
    return-void
.end method
