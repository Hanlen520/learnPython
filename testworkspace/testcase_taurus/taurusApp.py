#!/user/bin/env python
# -*- coding:utf-8 -*-
from config import *
from testworkspace.common.tool import *

def test_signIn(confighttp):
    data = {
        'cellphone': '13572489850',
        'password': encrypt('111111')
    }
    r = confighttp.post('taurus/user/signIn', data=data)
    token = r['properties'][0]['token']
    return token

def test_accountingCategoryAdd(confighttp,token):
    data = {
        'type': 1,  # 类型 1收入 2支出
        'category': '收入3',
        'token':token
    }
    r = confighttp.post('taurus/accountingCategory/add', data=data)

def test_userAccountingAdd(confighttp,token):
    data = {
        'accountingType': 1,  # 类型 1收入 2支出
        'categoryId': 85,
        'amount':66.07,
        'useDate':'2018-01-06',
        'remark':'支出支出支出支出支出支出支出支出支出',
        'token':token
    }
    r = confighttp.post('/taurus/userAccounting/add', data=data)

if __name__ == '__main__':
    with requests.Session() as session:
        # http://jngjsc.51aoshuo.com/taurus/user/signIn
        confighttp = ConfigHttp("jngjsc.51aoshuo.com", '',session)
        token = test_signIn(confighttp)
        print u'当前token:',token

        # 新增记账类别
        # test_accountingCategoryAdd(confighttp,token)
        # 新增记账
        test_userAccountingAdd(confighttp, token)