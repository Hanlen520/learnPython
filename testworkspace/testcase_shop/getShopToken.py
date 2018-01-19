#!/user/bin/env python
# -*- coding:utf-8 -*-
import requests
import json
from config import *
from testworkspace.common.tool import *

def getShopToken():
    url = URL_SHOP + '/lqmall/user/signIn'
    data = {
        'name': USERINFO['cellphone'],
        'password': encrypt(USERINFO['password'])
    }
    s = json.dumps(data)
    response = requests.post(url=url, data=s)
    token = ""
    if response.status_code == 200:
        token = response.json()['properties']['token']
    print u"当前token为：",token
    return token

# if __name__ == '__main__':
#     token = getShopToken()
#     url = URL_SHOP + '/lqmall/kale/queryLoanAmount'
#     data = {
#         'token': token
#     }
#     s = json.dumps(data)
#     response = requests.post(url=url, data=s)
#     print response.content