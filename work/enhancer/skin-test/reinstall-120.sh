#!/system/bin/sh
set -eu
backup=/data/local/tmp/sogou-skin-120-backup
test -s "$backup/user-data.tgz"
test -s /data/local/tmp/sogou-enhancer-120.apk
test -s /data/local/tmp/sogou-single-120.apk
pm path com.sohu.inputmethod.sogou.xiaomi > "$backup/xiaomi-before.txt"
pm path com.sohu.inputmethod.sogou > "$backup/official-before.txt"
test -s "$backup/xiaomi-before.txt"
test -s "$backup/official-before.txt"

# Explicit whitelist: do not uninstall either the official or Xiaomi input method.
pm uninstall com.sogouenhance | grep -x Success
pm install /data/local/tmp/sogou-enhancer-120.apk | grep -x Success
pm uninstall com.sohu.inputmethod.sogou.enhanced | grep -x Success
pm install /data/local/tmp/sogou-single-120.apk | grep -x Success
am force-stop com.sogouenhance
am force-stop com.sohu.inputmethod.sogou.enhanced
mkdir -p "$backup/restored"
tar -xzf "$backup/user-data.tgz" -C "$backup/restored"
for package in com.sogouenhance com.sohu.inputmethod.sogou.enhanced; do
    destination=/data/user/0/$package
    test -d "$destination"
    owner=$(stat -c %u "$destination")
    # Preserve user settings, dictionaries and skins; let the new APK rebuild code caches.
    for part in shared_prefs files databases no_backup; do
        if test -d "$backup/restored/$package/$part"; then
            cp -a "$backup/restored/$package/$part" "$destination/"
            chown -R "$owner:$owner" "$destination/$part"
        fi
    done
    restorecon -RF "$destination"
done
pm path com.sohu.inputmethod.sogou.xiaomi > "$backup/xiaomi-after.txt"
pm path com.sohu.inputmethod.sogou > "$backup/official-after.txt"
cmp "$backup/xiaomi-before.txt" "$backup/xiaomi-after.txt"
cmp "$backup/official-before.txt" "$backup/official-after.txt"
echo 'REINSTALLED_ENHANCERS_ONLY; OFFICIAL_AND_XIAOMI_PATHS_UNCHANGED'
