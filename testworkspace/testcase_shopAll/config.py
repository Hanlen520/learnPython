#!/user/bin/env python
# -*- coding:utf-8 -*-
import requests,json

USERINFO = {'cellphone':'13572489850','password':'123456'}

URL = "http://47.96.171.4:8090"
HOST = "47.96.171.4"
PORT = '8090'

class ConfigHttp():
    def __init__(self, host,port):
        self.host = host
        self.port = port

    def get(self, url, params=None):
        result = {}
        url = "http://" + self.host + ":" + self.port + "/" + url
        print '请求地址：',url
        r = requests.get(url,params=params)
        if r.status_code == 200:
            result = json.loads(r.text)
        result["status_code"] = r.status_code
        print '响应结果：',result
        return result

    # 封装HTTP POST请求方法,支持上传图片
    def post(self, url, files=None, data=None):
        url = 'http://' + self.host + ':' + self.port + "/" + url
        print '请求地址：', url
        r = requests.post(url, files=files, data=data)
        result = {}
        if r.status_code == 200:
            result = json.loads(r.text)
        result["status_code"] = r.status_code
        print '响应结果：', result
        return result