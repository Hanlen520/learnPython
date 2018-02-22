#!/user/bin/env python
# -*- coding:utf-8 -*-
from getToken import *
import base64

def test_signIn(confighttp):
    data = {
        'name': USERINFO['cellphone'],
        'password': encrypt(USERINFO['password'])
    }
    s = json.dumps(data)
    result = confighttp.post('lqmall/user/signIn', data=s)
    token = result['properties']['token']
    return token

# 用于根据审核情况查询轮播图
def test_slideShowList(confighttp):
    data = {
        'platform': '1',
        "appVersion": "1.0.0120"
    }
    s = json.dumps(data)
    result = confighttp.post('lqmall/slideShowList',data=s)
    if result['status_code'] == 200:
        print u'轮播图-showList:',result['properties']['showList']

# 获得版本地址
def test_url(confighttp):
    result = confighttp.get('lqmall/version/url')
    if result['status_code']==200:
        print 'versionUrl:',result['properties']['versionUrl']

# 上传支付宝截图
def test_screenshot(token):
    data = {'token': token}
    s = json.dumps(data)

    f = open(r"C:\Users\Public\Pictures\2cd16e4561a07add0671e82e744548d1.jpg", 'rb')  # 二进制方式打开图文件
    ls_f = base64.b64encode(f.read())  # 读取文件内容，转换为base64编码
    f.close()

    files = {
        "field1" : open(r"C:\Users\Public\Pictures\2cd16e4561a07add0671e82e744548d1.jpg", "rb"),
        "field1": open(r"C:\Users\Public\Pictures\2cd16e4561a07add0671e82e744548d1.jpg", "rb")
    }
    result = requests.post('http://47.96.171.4/caifu/social/security/upload/screenshot',
                             data=ls_f)
    print result.content

if __name__ == '__main__':
    confighttp = ConfigHttp("47.96.171.4",'8090')

    token = test_signIn(confighttp)
    #
    print u"当前token为：", token

    # 用于根据审核情况查询轮播图
    # test_slideShowList(confighttp)
    #
    # # 获得版本地址
    # test_url(confighttp)

    test_screenshot(token)
