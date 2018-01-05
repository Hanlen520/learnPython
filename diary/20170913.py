#!/user/bin/env python
# -*- coding:utf-8 -*-

from download import download
import time
from bs4 import BeautifulSoup

if __name__ == '__main__':
    baidu_html = download("http://example.webscraping.com/places/default/view/American-Samoa-5")
    # print baidu_html
    start = time.time()
    soup = BeautifulSoup(baidu_html,'html.parser')

    # print soup.prettify()
    tr = soup.find(attrs={'id':'places_area__row'})
    td = tr.find(attrs={'class':'w2p_fw'})
    end = time.time()
    print td.text
    print "---",end-start

