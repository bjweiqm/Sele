#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: dianying.py
@time: 2016/8/4 13:45
"""

import urllib2
from lxml import etree

url = 'http://www.mp4ba.com/index.php?sort_id=3'
data = urllib2.urlopen(url).read()


def save():
    with open('') as f:
        pass




def ele(data):
    html = etree.HTML(data)
    et = html.xpath('//*[@class="alt2"]')
    for value in et:
        leixing = value.xpath('td[2]/a/text()')[0]
        mingcheng = value.xpath('td[3]/a/text()')[0]
        lianjie = value.xpath('td[3]/a/@href')[0]
        daxiao = value.xpath('td[4]/text()')[0]
        print leixing, mingcheng.strip(), daxiao, lianjie



if __name__ == '__main__':
    ele(data)

