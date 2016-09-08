#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: test_plus.py
@time: 2016/9/8 18:50
"""


def eco(func):
    def en(*arg):
        if len(arg) == 0:
            return 0
        for ch in arg:
            if not isinstance(ch, int):
                return 0
        return func(*arg)
    return en

@eco
def is_sum(*arg):
    return sum(arg)

print is_sum(1, 2, 3, 4, 5)
