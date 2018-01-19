#!/user/bin/env python
# -*- coding:utf-8 -*-
import os,time
import unittest
import common.HTMLTestRunnerCN as HTMLTestRunnerCN
from testcase_shop.QueryLoanAmount import QueryLoanAmount
from testcase_shop.OrderInfo import OrderInfo

if __name__ == '__main__':
    testsuit = unittest.TestSuite()
    # 用户信息查询
    # testsuit.addTest(QueryLoanAmount('test_queryLoanAmount'))
    # testsuit.addTest(QueryLoanAmount('test_queryLoanAmountv1'))

    #商城下订单
    testsuit.addTest(OrderInfo('test_order'))

    unittest.TextTestRunner(verbosity=2).run(testsuit)

    # now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    # filePath = os.getcwd() + '\\report\\'+ now + '_report.html'
    #
    # fp = file(filePath, 'wb')
    # runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title="接口Test", description="接口Test")
    # runner.run(testsuit)
    # fp.close()