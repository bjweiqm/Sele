#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: file_python.py
@time: 2016/8/23 14:54
"""


with open('files.txt', 'rb') as f:
    fs = f.read()
    # print fs
    try:
        print unicode(fs, 'gbk')
        print 'gbk'
    except Exception, e:
        print fs





