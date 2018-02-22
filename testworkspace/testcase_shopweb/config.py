#!/user/bin/env python
# -*- coding:utf-8 -*-
import requests,json

HOST = "10.1.11.51"
PORT = '8080'
# http://47.96.171.4:8099/lqmall_admin/
# http://10.1.11.51:8080/lqmall_admin/
class ConfigHttp():
    def __init__(self, host,port,session):
        self.host = host
        self.port = port
        self.session = session

    def get(self, url, params=None):
        result = {}
        url = "http://" + self.host + ":" + self.port + "/" + url
        print '请求地址：',url
        r = self.session.get(url,params=params)
        if r.status_code == 200:
            result = json.loads(r.content)
        print '响应结果：',r.content
        return result

    # 封装HTTP POST请求方法,支持上传图片
    def post(self, url, files=None, data=None):
        url = 'http://' + self.host + ':' + self.port + "/" + url
        print '请求地址：', url
        r = self.session.post(url, files=files, data=data)
        result = {}
        if r.status_code == 200:
            result = json.loads(r.content)
        print '响应结果：', r.content
        return result