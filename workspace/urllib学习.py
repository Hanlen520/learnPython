#!/usr/bin/env python
# encoding: utf-8
"""
@author:lichengyan
@file: urllib学习.py
@time: 2017/12/26 20:58
"""
import os
import urllib.parse
import urllib.request
import urllib.error
import socket

# get请求
def get_run1():
    response = urllib.request.urlopen('http://httpbin.org/deny')
    # print(response.read())
    print(u"类型：",type(response))
    print(u"状态码：", response.status)
    print(u"响应头：", response.getheaders())
    print(u"响应头（server）：", response.getheader('server'))

# get请求:在规定的时间内得不到响应的话抛出异常
def get_run2():
    try:
        response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
    except urllib.error.URLError as e:
        if isinstance(e.reason,socket.timeout):
            print("time out!!")

# get请求:负责请求
def get_run3():
    url = 'http://httpbin.org/post'
    headers = {
        # 'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
        'Host': 'httpbin.org'
    }
    data = bytes(urllib.parse.urlencode({'world': 'hello'}), encoding='utf8')

    res = urllib.request.Request(url=url,data=data,headers=headers,method='POST')
    res.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
    response = urllib.request.urlopen(res)
    print(response.read())

# post请求
def post_run1():
    # urllib库里面有个urlencode函数，可以把key - value这样的键值对转换成我们想要的格式，返回的是a = 1 & b = 2这样的字符串
    data = bytes(urllib.parse.urlencode({'world':'hello','XXX':'test'}),encoding='utf8')
    response = urllib.request.urlopen('http://httpbin.org/post',data=data)
    print(response.read())

if __name__ == '__main__':
    # get_run1()
    # post_run1()
    # get_run2()

    get_run3()