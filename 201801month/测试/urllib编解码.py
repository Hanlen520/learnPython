#!/user/bin/env python
# -*- coding:utf-8 -*-
import urllib

if __name__ == '__main__':
    url = 'http://test.com/s?wd=哈哈'
    # 如果此网站编码是gbk的话，需要进行解码，从gbk解码成unicode，再从Unicode编码编码为utf-8格式。
    url = url.decode('gbk', 'replace')
    print urllib.quote(url.encode('utf-8', 'replace'))

    encoded_url = 'http%3a%2f%2ftest.com%2fs%3fwd%3d%e5%93%88%e5%93%88'
    print urllib.unquote(encoded_url).decode('utf-8', 'replace').encode('gbk', 'replace')  # 反过来