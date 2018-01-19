#!/user/bin/env python
# -*- coding:utf-8 -*-
import requests
from tool import *
from SqlQuery import *

# URL_SHOP = "http://10.1.11.51:8080"
URL_SHOP = "http://lqmallapi.51kaledai.com:8080"
cellphone = '15800876020'
psw = '456456'

# 发送短信
def sendVeriCodes():
    url = URL_SHOP + '/lqmall/veriCodes/sendVeriCodes'
    data = {
        'cellphone': cellphone,
        'type':2,
        # 手机前3位+salt+手机后8位，得到的结果再MD5一下
        'sign': md5(cellphone[:3] + "9544b351297a40b18cb5252eb7cdedd6" + cellphone[3:])
    }
    s = json.dumps(data)    # 以json形式发送post请求
    response = requests.post(url=url, data=s)
    if response.status_code == 200:
        print response.content

# 验证短信
def validVeriCodes(code):
    url = URL_SHOP + '/lqmall/veriCodes/validVeriCodes'
    data = {
        'cellphone': cellphone,
        'type':2,
        'code':code
    }
    # 以json形式发送post请求
    s = json.dumps(data)
    response = requests.post(url=url, data=s)
    identifier = ""
    if response.status_code == 200:
        print response.content
        identifier = response.json()['identifier']
    return identifier
# 注册
def signUp(identifier):
    url = URL_SHOP + '/lqmall/user/signUp'
    data = {
        'cellphone': cellphone,
        'identifier':identifier,
        'password': encrypt(psw)
    }
    s = json.dumps(data)
    response = requests.post(url=url, data=s)
    if response.status_code == 200:
        print response.content

# 是否注册
def isregister():
    url = URL_SHOP + '/lqmall/isregister'
    params = {'cellphone': cellphone}
    response = requests.get(url=url, params=params)
    if response.status_code == 200:
        print response.content
# 用户登录
def signIn():
    url = URL_SHOP + '/lqmall/user/signIn'
    data = {
        'name': cellphone,
        'password': encrypt(psw)
    }
    s = json.dumps(data)
    response = requests.post(url=url, data=s)
    print response
    token = ""
    if response.status_code == 200:
        print response.content
        token = response.json()['properties']['token']
    return token

# 用户退出
def signOut(token):
    url = URL_SHOP + '/lqmall/user/signOut'
    data = {'token': token}
    s = json.dumps(data)
    response = requests.post(url=url, data=s)
    if response.status_code == 200:
        print response.content

if __name__ == '__main__':
    # 1.发送短信
    # sendVeriCodes()

    # 查询数据中验证码
    # mysql_query_codes(cellphone)

    # 2.验证短信
    # identifier = validVeriCodes(832647)
    # 注册
    # signUp(identifier)

    # isregister()

    # 查询卡乐贷数据库中用户是否存在
    # mysql_query_users(cellphone)

    # 登录获取token
    token = signIn()

    # 用户退出
    # signOut(token)
