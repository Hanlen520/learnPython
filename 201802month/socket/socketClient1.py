#!/user/bin/env python
# -*- coding:utf-8 -*-
import socket

if __name__ == '__main__':
    sk = socket.socket()
    host = socket.gethostname()  # 获取本地主机名
    sk.connect((host,5666))

    ret = str(sk.recv(1024))
    print ret