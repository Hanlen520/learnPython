#!/usr/bin/env python
# encoding: utf-8
"""
@author:lichengyan
@file: beautifulsoup学习.py
@time: 2017/10/23 22:28
"""

from bs4 import BeautifulSoup

def run():
    path = u"F:\\PycharmProjects\\本地网站forStudy\\new_index.html"

    with open(path,'r') as fo:
        soup = BeautifulSoup(fo.read(),"lxml")

        # body > div.main - content > ul > li:nth-child(1) > img  图片
        # body > div.main - content > ul > li:nth - child(1) > div.article - info > h3 > a 标题
        # body > div.main - content > ul > li:nth - child(1) > div.article - info > p.meta - info 标签列表
        # body > div.main-content > ul > li:nth-child(1) > div.rate > span 评分
        # body > div.main - content > ul > li:nth - child(1) > div.article - info > p.description 描述

        imgs = soup.select("body > div.main-content > ul > li > img")
        titles = soup.select("body > div.main-content > ul > li > div.article-info > h3 > a")
        metaInfos = soup.select("body > div.main-content > ul > li > div.article-info > p.meta-info")
        scores = soup.select("body > div.main-content > ul > li > div.rate > span")
        descriptions = soup.select("body > div.main-content > ul > li > div.article-info > p.description")

    data = []
    for img,title,score,description,metaInfo in zip(imgs,titles,scores,descriptions,metaInfos):
        info = {
            u'img':img.get_text(),
            u'title':title.get_text(),
            u'score':float(score.get_text()),
            u'description': description.get_text(),
            u'metaInfo':list(metaInfo.stripped_strings)
        }


        data.append(info)

    # 找出评分>3的
    for one in data:
        if one['score'] > 3:
            print(one)


if __name__ == '__main__':
    run()