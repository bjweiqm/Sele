#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: zhuangshiqi_python02.py
@time: 2016/9/8 11:47
"""

from school.string_python.zhuangshiqi_python import dec

@dec
def my_sum(*arg):
    return sum(arg)


print my_sum(1,2,3,4,5,6)