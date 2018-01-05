#!/user/bin/env python
# -*- coding:utf-8 -*-
import unittest
import requests
import HTMLTestRunner
import sys,os
import smtplib
from email.mime.text import MIMEText
from email.header import Header

class post_signIn(unittest.TestCase):
	##初始化工作
	def setUp(self):
		pass
	# 退出清理工作
	def tearDown(self):
		pass

	# 具体的测试用例，一定要以test开头
	def test_signIn(self):# 登录
		url = 'http://120.55.42.27/caifu/user/signIn'
		data={
			'name':'13572489850',
			'password':123456
		}
		response = requests.post(url=url,data=data)
		self.assertEqual(response.status_code, 200, 'signIn OK')
		print "test1:", response.content

	def test2(self): #app消息通知
		token = self.getToken()
		url = 'http://120.55.42.27/caifu/appMessage/getAmsglist'
		print "test2-token:",token
		params={
			'number':1,
			'token':token
		}
		response = requests.get(url=url,params=params)
		self.assertEqual(response.status_code, 200, 'signIn OK')
		print "test2:", response.json()

	def getToken(self):
		token = ""
		url = 'http://120.55.42.27/caifu/user/signIn'
		data={
			'name':'13572489850',
			'password':123456
		}
		response = requests.post(url=url,data=data)
		if response.status_code == 200:
			dict = response.json()['properties']
			token = dict[0]['token']
		return token

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


if __name__ == '__main__':
	# unittest.main()
	# test = unittest.TestSuite()
	# test.addTests(post_signIn('test1'))
	# test.addTests(post_signIn('test2'))

	test = unittest.TestLoader().loadTestsFromTestCase(post_signIn)

	filePath = os.getcwd() + '/tempfile/new_report.html'
	fp = file(filePath, 'wb')
	runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="test",description="XXXXXXXXXXXXXXXXXXXXXXXXX")
	runner.run(test)
	fp.close()

	send_mail(filePath)
