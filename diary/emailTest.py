#!/user/bin/env python
# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def main():
	# 发送邮箱服务器
	smtpserver = 'smtp.163.com'
	# 发送邮箱用户/密码
	user = 'wuluopiaoxue@163.com'
	password = '19880801lcy'
	# 发送邮箱
	sender = 'wuluopiaoxue@163.com'
	# 接收邮箱
	receiver = '18192496382@163.com'
	# 发送邮件主题
	subject = 'Python email test'

	# 编写HTML类型的邮件正文
	msg = MIMEText('<html><h1>你好！</h1></html>', 'html', 'utf-8')
	msg['Subject'] = Header(subject, 'utf-8')
	msg['From'] = 'wuluopiaoxue@163.com'
	msg['To'] = "18192496382@163.com"

	# 连接发送邮件
	smtp = smtplib.SMTP()
	smtp.connect(smtpserver)
	smtp.login(user, password)
	smtp.sendmail(sender, receiver, msg.as_string())
	smtp.quit()

if __name__ == '__main__':
	main()