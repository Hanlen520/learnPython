#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'Administrator'
from auto_http_api.DAL import Dhttpbase

class ConfigHttp():
    def __init__(self, mhttpbase):
        self.mhttpbase = mhttpbase
        self.mh = Dhttpbase.ConfigHttp(self.mhttpbase)

    def get(self, url, params={}):
       return self.mh.get(url, params)

    def post(self, url, files=None, params=None):
        return self.mh.post(url, files, params)

    # def check_param(self):
