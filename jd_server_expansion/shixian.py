#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: shixian.py
@time: 2016/8/5 10:20
"""


import os
import urllib2
from shutil import copy
from ConfigParser import ConfigParser

from lxml import etree

path = os.path.split(os.path.realpath(__file__))[0]
host_path = 'C:\Windows\System32\drivers\etc\hosts'

def ReadConfig(key, value):
    cf = ConfigParser()
    cf.read('config.ini')
    return cf.get(key, value)

class Modify_host():

    ''' 有关host的所有操作封装 '''

    def host_back(self):
        # 备份
        copy(host_path, os.path.join(path, 'hosts.bak'))

    def host_write(self, i):
        # 写入host
        with open(host_path, 'wb') as f:
            f.write(i)

    def host_reduction(self):
        # 还原
        copy(os.path.join(path, 'hosts.bak'), host_path)

class jd_server_exp():

    ''' 实现打开页面 获取页面元素操作 '''

    def __init__(self):
        self.head = {'User-Agent': ReadConfig('url', 'head'), 'Cookie': ReadConfig('url', 'cookie')}

    def open_url(self, url, i):
        # 打开网址 返回网页内容
        try:
            print '正在打开ip为 [%s] 的服务器' %i
            data = urllib2.urlopen(urllib2.Request(url, headers=self.head)).read()
            return unicode(data, 'utf-8')
        except UnicodeDecodeError, e:
            return unicode(data, 'gbk')
        except urllib2.HTTPError, e:
            with open('errorhost.txt', 'ab') as f:
                f.write('urllib2.HTTPError ==>' + i + '\n')
            return False
        except urllib2.URLError, e:
            with open('errorhost.txt', 'ab') as f:
                f.write('urllib2.HTTPError ==>' + i + '\n')
            return False
        except Exception, e:
            print e
    def element_jd(self, data, element):
        # 获取页面中需要的元素
        # print data
        # print type(data)
        html = etree.HTML(data)
        try:
            name = html.xpath(element)[0].strip()
            print name
            return name
        except IndexError :
            print '未找到元素！！'

def open_user_hosts():
    # 打开设置的host文件，拼接host文件
    host_lie_biao = []
    with open('host') as f:
        for i in f.readlines():
            host = i.strip() + '\t' + ReadConfig('yuming', 'yuming')
            host_lie_biao.append(host)
    return host_lie_biao

def dui_bi_shu_ju(con1, con2, ip):
    # 对比元素 con1 页面获取的内容  con2 对比的内容 IP IP地址
    assis = []
    if all(con1):
        for i in range(len(con1)):
            if con1[i] == con2[i].decode('utf-8'):
                assis.append(1)
            else:
                assis.append(0)
        print assis
        print all(assis)
        if not all(assis):
            with open('errorhost.txt', 'ab') as f:
                f.write('对比error ==>' + ip + '\n')
    else:
        with open('errorhost.txt', 'ab') as f:
                f.write('error ==>' + ip + '\n')

def file_name(li):
    # 接收一个IP，返回一个拼接的字符转
    lis = li.split('\t')
    for i in lis:
        name = lis[0].split('.')
        return ''.join(name)

def getPing(filename):
    # ping 指定的域名，保证访问的IP无误
    ping = os.popen('ping %s' % ReadConfig('yuming', 'yuming'))
    log = os.path.join(os.path.join(path, 'ping'), '%s.txt' %filename)
    with open(log, 'ab') as f:
        for i in ping:
            f.write(i)

def jie_xi(key, value):
    # 解析 元素 返回一个list 接收两个参数
        ele = ReadConfig(key, value)
        return ele.split(';')

def zu_zhi_ye_mian(i):
    # 循环在页面中拿出需要的元素
    yuansu = []
    jd = jd_server_exp()
    html = jd.open_url(ReadConfig('url', 'url'), i)
    if html:
        for ele in jie_xi('element', 'elements'):
            ys = jd.element_jd(html, ele)
            yuansu.append(ys)
        return yuansu
    else:
        return False

def run():
    # 运行程序
    hs = Modify_host()
    hs.host_back()
    for i in open_user_hosts():
        hs.host_write(i)
        getPing(file_name(i))
        lis = zu_zhi_ye_mian(i)
        if lis:
            dui_bi_shu_ju(lis, jie_xi('element', 'yuansu'), i)
        else:
            continue
    hs.host_reduction()

if __name__ == '__main__':
    run()