#!/user/bin/env python
# -*- coding:utf-8 -*-
import yagmail

def main():
	user = 'wuluopiaoxue@163.com'
	password = '19880801lcy'
	yag = yagmail.SMTP(user=user,password=password,host='smtp.163.com')

	# 邮箱正文
	contents = ['This is the body, and here is just text http://somedomain/image.png',
				'You can find an audio file attached.', '/local/path/song.mp3']

	# 发送邮件
	yag.send('18192496382@163.com', 'subject', contents)

if __name__ == '__main__':
	main()