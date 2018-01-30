#!/user/bin/env python
# -*- coding:utf-8 -*-
import requests

if __name__ == '__main__':
    url = 'http://47.96.171.4:8080/admin_web/admin/loginPage.json'
    response = requests.session().get(url)

    print response.content