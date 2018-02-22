#!/user/bin/env python
# -*- coding:utf-8 -*-
from config import *

# 管理员登录
def test_signIn(confighttp):
    data = {
        'name': 'admin',
        'password': '123456'
    }
    r = confighttp.post('lqmall_admin/admin/signIn', data=data)

# 管理员列表
def test_list(confighttp):
    result = confighttp.get('lqmall_admin/admin/list')

# 查询商品列表接口
def test_getProductList(confighttp):
    data = {
        'queryType': 1
    }
    r = confighttp.post('lqmall_admin/product/getProductList', data=data)

#通过productId查询商品详细信息
def test_getProductInfo(confighttp):
    data = {
        'productId': 3
    }
    r = confighttp.post('lqmall_admin/product/getProductInfo', data=data)

# 查询物流列表信息
def test_express(confighttp):
    r = confighttp.post('lqmall_admin/order/express')

# 添加（编辑）商品接口
def test_editOrAddProduct(confighttp):
    data={
        'productName':'test_shop',
        'productGroundingState':0,
        'productIsSupport':0,
        'productCategory':[0],
        'productMaxPrice':1000.00,
        'productMinPrice':1000.00
    }
    r = confighttp.post('lqmall_admin/product/editOrAddProduct')

# 编辑规格商品的库存数量接口
def test_updateStockNum(confighttp):
    data={
        'productSpecId':33,
        'productSpecStockNum':189
    }
    r = confighttp.post('lqmall_admin/product/updateStockNum',data=data)

# 通过productId集合批量修改商品的上下架状态
def test_toUpOrDowm(confighttp):
    data={
        'productIdList':[3],
        'state':2
    }
    r = confighttp.post('lqmall_admin/product/toUpOrDowm',data=data)
# 查询订单列表
def test_orderlist(confighttp):
    r = confighttp.post('lqmall_admin/order/list')

# 查询用户消费记录
def test_findUserOrderHistory(confighttp):
    data = {'uid': 6084}
    r = confighttp.post('lqmall_admin/order/findUserOrderHistory',data=data)

# 录入相应订单物流信息
def test_udapteExpress(confighttp):
    data = {
        'oiCode': 'DDBH20180106000001',
        'oiExpressCo': '中通快递',
        'oiExpressCode': 'KD125aaa2213a'
    }
    r = confighttp.post('lqmall_admin/order/udapteExpress',data=data)

# 操作日志列表
def test_loglist(confighttp):
    data = {
        'pageNum': 1,
        'pageSize': 10
    }
    r = confighttp.post('lqmall_admin/log/list',data=data)

if __name__ == '__main__':
    with requests.Session() as session:
        # http: // 47.96.171.4:8099
        confighttp = ConfigHttp("10.1.11.51", '8080',session)
        # confighttp = ConfigHttp("47.96.171.4", '8099', session)
        test_signIn(confighttp)

        # 将CookieJar转为字典：
        print session.cookies.get_dict()
        # print requests.utils.dict_from_cookiejar(session.cookies)

        test_getProductList(confighttp)
        test_express(confighttp)

        # test_updateStockNum(c)

        # test_toUpOrDowm(confighttp)

        # test_getProductInfo(confighttp)
        #
        # test_orderlist(confighttp)
        #
        # test_findUserOrderHistory(confighttp)

        test_udapteExpress(confighttp)

        test_loglist(confighttp)

