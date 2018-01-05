#!/user/bin/env python
# -*- coding:utf-8 -*-
import requests
def test1():
    url = 'http://120.55.42.27/caifu/user/signIn'
    data = {
        'name': '13572489850',
        'password': 123456
    }
    response = requests.post(url=url, data=data)
    print "test1:", response.content

# /borrow/shop/queryLoanAmount
# /borrow/shop/payResult
def test2():
    url = 'http://120.55.42.27/borrow/shop/queryLoanAmount'
    data = {
        'mobileMd5': '6ecd4afcd41dcee0dc0a2fde717c5309'
    }
    response = requests.post(url=url, data=data)
    print "test2:", response.content

if __name__ == '__main__':
    test2()