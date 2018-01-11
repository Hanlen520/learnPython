#!/user/bin/env python
# -*- coding:utf-8 -*-

import os

def getcellphoneInfo(aapt_path,apk_path,cmd):
    # 切换到aapt所在的目录下
    os.chdir(aapt_path)
    tmp = os.popen(cmd + apk_path)
    res = tmp.read()
    for line in res.splitlines():
        print line.decode('cp936').encode('utf-8')

if __name__ == '__main__':
    aapt_path = r"D:\android\android-sdk-windows\build-tools\27.0.1"
    apk_path = r"D:\android\android-sdk-windows\tools\Testapp\app-release.apk"

    print u"----查看apk包的packageName、versionCode、applicationLabel、launcherActivity、permission等各种详细信息----"
    cmd = "aapt dump badging "
    getcellphoneInfo(aapt_path,apk_path,cmd)
    print u"-----查看权限-------------------------------------------------------------------------------------------"
    cmd = "aapt dump permissions "
    getcellphoneInfo(aapt_path,apk_path,cmd)
    print u"-----查看资源列表-------------------------------------------------------------------------------------------"
    cmd = "aapt dump resources "
    getcellphoneInfo(aapt_path, apk_path, cmd)
    print u"-----查看apk配置信息-------------------------------------------------------------------------------------------"
    cmd = "aapt dump configurations "
    getcellphoneInfo(aapt_path, apk_path, cmd)