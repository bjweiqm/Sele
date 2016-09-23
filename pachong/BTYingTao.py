#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: BTYingTao.py
@time: 2016/8/11 20:16
"""

import urllib2
from lxml import etree


head = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36',
}


def url_open(url):
    try:
        html = urllib2.urlopen(urllib2.Request(url, headers = head)).read()
        return html
    except urllib2.URLError:
        print url


def xpath_element(html):
    li = []
    if not html:
        exit()
    data = etree.HTML(html)
    content = data.xpath('//div[@class="r"]')
    for ele in content:
        url = ele.xpath('a/@href')
        name = ele.xpath('a/h5')
        if name:
            names = name[0].xpath('string(.)')
            li.append([url[0], names])
    return li

def na(data):
    li = []
    html = etree.HTML(data)
    cili = html.xpath('//*[@id="content"]/div/ul/li[1]/span/a/text()')
    riqi = html.xpath('//*[@id="content"]/div/ul/li[2]/span/text()')
    daxiao = html.xpath('//*[@id="content"]/div/ul/li[3]/span/text()')
    return [cili[0], riqi[0], daxiao[0]]



def run():
    search = raw_input('输入搜索关键词: ')
    with open('content.txt', 'wb') as f:
        f.write(search.center(66, '~') + '\n')
    url = 'http://www.btcherry.org/search?keyword=%s' %search
    data = url_open(url)
    host = 'http://www.btcherry.org'
    for dizhi in xpath_element(data):
        data = url_open(host + dizhi[0])
        if data:
            neirong = na(data)
            with open('content.txt', 'ab') as f:
                f.write('标题: ' + dizhi[1].encode('utf-8') + '\n')
                f.write('链接: ' + neirong[0].encode('utf-8') + '\n')
                f.write('日期: ' + neirong[1].encode('utf-8') + '\n')
                f.write('大小: ' + neirong[2].encode('utf-8') + '\n')
                f.write('-' * 66 + '\n')

if __name__ == '__main__':
    run()
