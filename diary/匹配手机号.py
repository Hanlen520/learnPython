#!/user/bin/env python
# -*- coding:utf-8 -*-

import re

# 正则匹配电话号码
phone = "18105770206"
tesp = '^((\+?86)|(\(\+86\)))?((13[0-9])|(15[^4])|(18[0,2,3,5-9])|(17[0-8])|(147))\d{8}$'
correct='^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}'
p2 = re.compile(tesp)
phonematch = p2.match(phone)

if phonematch:
    print phonematch.group(),'is OK'
else:
    print "phone number is error!"

# --------www.iplaypy.com---------

# 正则匹配邮箱和电话号码
emailorphone = "wuluopiaoxue@qq.com"
p3 = re.compile('^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}|[^\._-][\w\.-]+@(?:[A-Za-z0-9]+\.)+[A-Za-z]+')
emailorphonematch = p3.match(emailorphone)

if emailorphone:
    print emailorphonematch.group(),'is ok'
else:
    print "phone or email error..."