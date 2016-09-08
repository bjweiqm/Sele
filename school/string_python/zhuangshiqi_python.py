#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: zhuangshiqi_python.py
@time: 2016/9/8 11:42
"""


def dec(func):
    def in_dec(*arg):
        if len(arg) == 0:
            return 0
        for val in arg:
            if not isinstance(val, int):
                return 0
        return func(*arg)
    return in_dec

@dec
def my_sum(*arg):
    return sum(arg)

@dec
def my_average(*arg):
    return sum(arg) / len(arg)




print my_sum(1,2,3,4,5)

print my_average(1,2,3,4,5)




