#!/user/bin/env python
# -*- coding:utf-8 -*-
import requests
from config import *

def getToken():
    token = ""
    url = URL + '/caifu/user/signIn'
    data = {
        'name': '13572489850',
        'password': '123456'
    }
    response = requests.post(url=url, data=data)
    if response.status_code == 200:
        dict = response.json()['properties']
        token = dict[0]['token']
    return token