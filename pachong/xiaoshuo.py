#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: xiaoshuo.py
@time: 2016/6/13 16:41
"""


import urllib2
import time
from lxml import etree

url = 'http://www.00ksw.com/html/4/4413/'

hml = urllib2.urlopen(url).read()
hr = etree.HTML(hml)
en = hr.xpath('//*[@id="list"]/dl/dd/a')
print en

'''
for cheo in en:
    line = cheo.xpath('@href')
    # print line

    if len(line) > 0 and int(line[0].split('.')[0]) > 1857853:
        print url + line[0]
        html = urllib2.urlopen(url + line[0]).read()
        he = etree.HTML(html)
        time.sleep(2)
        data = he.xpath('//*[@id="content"]')[0]
        info = data.xpath('string(.)').encode('utf-8').replace('    ', '\n\r')
        with open(u'魅影逍遥.txt', 'ab') as f:
            f.writelines(info)

'''


