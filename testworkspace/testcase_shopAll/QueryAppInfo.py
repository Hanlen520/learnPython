#!/user/bin/env python
# -*- coding:utf-8 -*-
from getToken import *

# 用于根据审核情况查询轮播图
def test_slideShowList():
    url = URL + '/lqmall/slideShowList'
    data = {
        'platform': '2',
        "appVersion": "1.0.0"
    }
    s = json.dumps(data)
    response = requests.post(url=url, data=s)
    if response.status_code == 200:
        print response.content

if __name__ == '__main__':
    # test_slideShowList()
    url_list = ['/lqmall/slideShowList','/lqmall/version/update']