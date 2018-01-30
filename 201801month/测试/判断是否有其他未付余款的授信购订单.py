#!/user/bin/env python
# -*- coding:utf-8 -*-
import requests
from tool import *
from SqlQuery import *

# URL_SHOP = "http://10.1.11.51:8080"
# URL_SHOP = "http://lqmallapi.51kaledai.com:8080"
URL_SHOP = "http://47.96.171.4:8090"
cellphone = '13572489850'
psw = '123456'

# 用户登录
def signIn():
    url = URL_SHOP + '/lqmall/user/signIn'
    data = {
        'name': cellphone,
        'password': encrypt(psw)
    }
    s = json.dumps(data)
    response = requests.post(url=url, data=s)
    token = ""
    if response.status_code == 200:
        print response.content
        token = response.json()['properties']['token']
    return token

def hasUnFinalPayOrder(token):
    url = URL_SHOP + '/lqmall/merch/hasUnFinalPayOrder'
    data = {
        'token': token,
        'orderId': 17170,
        'payStep': 1
    }
    s = json.dumps(data)
    response = requests.post(url=url, data=s)
    token = ""
    if response.status_code == 200:
        print response.content

if __name__ == '__main__':
    token = signIn()
    print u'当前token：',token

    hasUnFinalPayOrder(token)