#!/user/bin/env python
# -*- coding:utf-8 -*-
import requests
from config import *
from testworkspace.common.tool import *

def getShopToken():
    url = URL + '/lqmall/user/signIn'
    data = {
        'name': USERINFO['cellphone'],
        'password': encrypt(USERINFO['password'])
    }
    s = json.dumps(data)
    response = requests.post(url=url, data=s)
    token = ""
    if response.status_code == 200:
        token = response.json()['properties']['token']
    return token

if __name__ == '__main__':
    print u"当前token为：", getShopToken()