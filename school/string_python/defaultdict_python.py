#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: defaultdict_python.py
@time: 2016/9/6 9:51
"""









'''
def minaax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res

def lessthan(x,y): return x < y
def grtrthan(x,y): return x > y

print minaax(lessthan, 4,2,1,5,6,3)
print minaax(grtrthan, 4,2,1,5,6,3)


def min1(*args):
    res = args[0]
    for arg in args[1:]:
        if arg < res:
            res = arg
    return res

def min2(first, *rest):
    print first, rest
    for arg in rest:
        if arg < first:
            if arg < first:
                first = arg
    return first

def min3(*args):
    tmp = list(args)
    tmp.sort()
    return tmp[0]

print min1(3,4,1,2)
print min2('bb', 'aa')
print min3([2,2],[1,1],[3,3])

'''
