#!/user/bin/env python
# -*- coding:utf-8 -*-

import urllib2

def download(url):
    print 'download:',url
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print "download error:",e.reason
        html = None
    return html