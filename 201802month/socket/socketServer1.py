#!/user/bin/env python
# -*- coding:utf-8 -*-
import socket

if __name__ == '__main__':
    sk = socket.socket()

    host = socket.gethostname()  # 获取本地主机名
    ip = socket.gethostbyname(host)  # 获取本地IP

    sk.bind((host, 5666))  # 绑定端口

    sk.listen(5)  # 等待客户端连接,最大连接数5
    while True:
        c, addr = sk.accept()  # 建立客户端连接。
        print '连接地址：', addr
        c.send('欢迎')
        c.close()  # 关闭连接