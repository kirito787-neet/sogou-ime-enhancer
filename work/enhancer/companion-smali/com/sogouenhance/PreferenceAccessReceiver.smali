.class public final Lcom/sogouenhance/PreferenceAccessReceiver;
.super Landroid/content/BroadcastReceiver;

.method public constructor <init>()V
    .locals 0
    invoke-direct {p0}, Landroid/content/BroadcastReceiver;-><init>()V
    return-void
.end method

.method public onReceive(Landroid/content/Context;Landroid/content/Intent;)V
    .locals 0
    invoke-static {p1}, Lcom/sogouenhance/PreferenceAccessReceiver;->grant(Landroid/content/Context;)V
    return-void
.end method

.method public static grant(Landroid/content/Context;)V
    .locals 4
    :try_start
    const-string v0, "com.sohu.inputmethod.sogou"
    const-string v1, "content://com.sogouenhance.prefs/visibility"
    invoke-static {v1}, Landroid/net/Uri;->parse(Ljava/lang/String;)Landroid/net/Uri;
    move-result-object v1
    const/4 v2, 0x1
    invoke-virtual {p0, v0, v1, v2}, Landroid/content/Context;->grantUriPermission(Ljava/lang/String;Landroid/net/Uri;I)V
    :try_end
    .catch Ljava/lang/SecurityException; {:try_start .. :try_end} :failed
    return-void

    :failed
    move-exception v0
    const-string v1, "SogouEnhance"
    const-string v2, "Could not grant preference provider visibility"
    invoke-static {v1, v2, v0}, Landroid/util/Log;->w(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I
    return-void
.end method
