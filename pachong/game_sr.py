#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: game_sr.py
@time: 2016/8/23 15:05
"""


import urllib2
import time
from lxml import etree


class GifJia():
    def __init__(self):
        self.li = []
        self.su = 1
        self.cookie = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36',
            'Cookie': 'CNZZDATA1000162133=1543152136-1451709521-http%253A%252F%252Fwww.mianfeib.com%252F%7C1474205080; amvid=b7dfa82fed808726f246e508bc651d61'
        }

    def get_Html(self, urls):
        try:
            html = urllib2.urlopen(urllib2.Request(urls, headers=self.cookie))
            return html.read()
        except Exception, e:
            print e
            with open('error.txt', 'ab') as f:
                f.write(urls)

    def etr(self, deta):
        ht = etree.HTML(deta)
        lis = ht.xpath('//*[@id="long"]')
        for i in lis:
            img = i.xpath('a/@href')[0]
            self.li.append('http://www.lovefou.com' + img)

    def img_like(self, data):
        ht = etree.HTML(data)
        urls = ht.xpath('//*[@class="lovetu"]/div/div[1]/div[3]/p[1]/a/img/@src')[0]
        name = ht.xpath('//*[@class="lovetu"]/div/div[1]/div[3]/p[1]/a/img/@alt')[0]
        print self.su, '===>', name, '===>', urls
        self.su += 1
        with open(name + '.gif', 'wb') as f:
            imgs = self.get_Html(urls)
            if imgs:
                f.write(imgs)
        time.sleep(3)




if __name__ == '__main__':
    gif = GifJia()
    for i in range(1, 85):
        url = 'http://www.lovefou.com/dongtaitu/list_%s.html' % i
        html = gif.get_Html(url)
        if html:
            gif.etr(html)
    for ii in gif.li:
        gif.img_like(gif.get_Html(ii))

