#!/user/bin/env python
# -*- coding:utf-8 -*-
import unittest
import os,time
import smtplib,yagmail
from email.mime.text import MIMEText
from email.header import Header
import common.HTMLTestRunnerCN as HTMLTestRunnerCN

from testcase.test_getAmsglist import case_getAmsglist
from testcase.test_isFirstBorrow import case_isFirstBorrow

def send_mail(file_new):
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body,'html','utf-8')
    msg['Subject'] = Header('xxx接口自动化测试报告','utf-8')
    msg['From'] = 'wuluopiaoxue@163.com'
    msg['To'] = "18192496382@163.com"

    user = 'wuluopiaoxue@163.com'
    password = '19880801lcy'

    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login(user,password)
    smtp.sendmail('wuluopiaoxue@163.com','18192496382@163.com',msg.as_string())
    smtp.quit()
    print('邮件已发出！注意查收。')

def send_mail_new(file_new):
    f = open(file_new,'rb')
    body = f.read()
    f.close()

    msg = MIMEText(body,'html','utf-8')
    # msg['Subject'] = Header('xxx接口自动化测试报告', 'utf-8')
    smtp = yagmail.SMTP(user='wuluopiaoxue@163.com',password='19880801lcy',host='smtp.163.com')
    smtp.send(to='18192496382@163.com',subject='subject',contents=msg.as_string())

if __name__ == '__main__':
    testsuit = unittest.TestSuite()
    testsuit.addTest(case_getAmsglist('test_getAmsglist'))
    testsuit.addTest(case_isFirstBorrow('test_isFirstBorrow'))

    now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
    filePath = os.getcwd() + '\\report\\'+ now + 'new_report.html'

    fp = file(filePath, 'wb')
    runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title="test", description="XXXXXXXXXXXXXXXXXXXXXXXXX")
    runner.run(testsuit)
    fp.close()

    send_mail(filePath)