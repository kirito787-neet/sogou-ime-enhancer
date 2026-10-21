.class public Llocal/sogou/enhancerprobe/ProbeActivity;
.super Landroid/app/Activity;

.method public constructor <init>()V
    .locals 0
    invoke-direct {p0}, Landroid/app/Activity;-><init>()V
    return-void
.end method

.method protected onCreate(Landroid/os/Bundle;)V
    .locals 3
    invoke-super {p0, p1}, Landroid/app/Activity;->onCreate(Landroid/os/Bundle;)V
    new-instance v0, Landroid/widget/EditText;
    invoke-direct {v0, p0}, Landroid/widget/EditText;-><init>(Landroid/content/Context;)V
    const-string v1, "Sogou enhancer verification - local text only"
    invoke-virtual {v0, v1}, Landroid/widget/EditText;->setHint(Ljava/lang/CharSequence;)V
    const v1, 0x20001
    invoke-virtual {v0, v1}, Landroid/widget/EditText;->setInputType(I)V
    invoke-virtual {p0, v0}, Landroid/app/Activity;->setContentView(Landroid/view/View;)V
    invoke-virtual {v0}, Landroid/widget/EditText;->requestFocus()Z
    invoke-virtual {p0}, Landroid/app/Activity;->getWindow()Landroid/view/Window;
    move-result-object v1
    const/4 v2, 0x5
    invoke-virtual {v1, v2}, Landroid/view/Window;->setSoftInputMode(I)V
    return-void
.end method
