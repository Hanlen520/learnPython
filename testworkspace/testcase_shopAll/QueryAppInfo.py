#!/user/bin/env python
# -*- coding:utf-8 -*-
from getToken import *

def test_signIn(confighttp):
    data = {
        'name': USERINFO['cellphone'],
        'password': encrypt(USERINFO['password'])
    }
    s = json.dumps(data)
    result = confighttp.post('lqmall/user/signIn', data=s)
    token = ''
    if result['status_code'] == 200:
        token = result['properties']['token']
    return token

# 用于根据审核情况查询轮播图
def test_slideShowList(confighttp):
    data = {
        'platform': '2',
        "appVersion": "1.0.0"
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

if __name__ == '__main__':
    confighttp = ConfigHttp("47.96.171.4",'8090')

    # token = test_signIn(confighttp)
    #
    # print u"当前token为：", token

    # 用于根据审核情况查询轮播图
    test_slideShowList(confighttp)

    # 获得版本地址
    test_url(confighttp)
