#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: Search_bt.py
@time: 2016/9/21 17:49
"""


import urllib2
from urllib import quote
from lxml import etree


def like(url):
    btmeet = url.format(quote(raw_input('search content :')))
    return btmeet

def html(urls):
    head = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36',
    }
    try:
        return urllib2.urlopen(urllib2.Request(urls, headers=head)).read()
    except Exception, e:
        with open('log.txt', 'ab') as f:
            f.write(str(e) + ' ===> ' + urls + '\n')


class BTmeetSearch():

    def __init__(self):
        self.detail = []

    def meet_content(self, deta):
        htm = etree.HTML(deta)
        link = htm.xpath('//*[@class="item-title"]')
        for li in link:
            self.detail.append(li.xpath('h3/a/@href')[0])

    def detail_content(self, deta):
        htm = etree.HTML(deta)
        print htm.xpath('//*[@id="wall"]/h2/script/text()')
        box = htm.xpath('//*[@class="fileDetail"]//td')
        print box[0].xpath('string(.)')
        print box[1].xpath('string(.)')
        print box[4].xpath('string(.)')
        # box = htm.xpath('//*[@id="wall"]')[0]
        # td =  htm.xpath('//td')
        # print td[0].xpath('string(.)')
        # print td[1].xpath('string(.)')
        # print td[4].xpath('string(.)')
        # print td[5].xpath('string(.)')

        print htm.xpath('//*[@class="panel-body"][1]/a/@href')




def run():
    url = 'http://www.btmeet.net/search/{}.html'
    meet = BTmeetSearch()
    data = html(like(url))
    print data
    exit()
    meet.meet_content(data)
    for i in meet.detail:
        print html('http://www.btmeet.net' + i)
        exit()
        # meet.detail_content(html('http://www.btmeet.net' + i))


if __name__ == '__main__':
    run()