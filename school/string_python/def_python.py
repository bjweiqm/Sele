#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: def_python.py
@time: 2016/9/2 18:31
"""

name = 'zhangsan'  #全局变量

def test01():
    age = 20 #本地变量


# nonlocal 只能在3.0以上版本使用
# def fi(js):
#     js = js
#     def action(label):
#         nonlocal js
#         print(label, js)
#         js += 1
#     return action

def fl(js):
    def action(label):
        print label, action.js
        action.js += 1
    action.js = js
    return action

# f = fl(0)
# f('zhangsan')
# f('lis')
# f('wang')
# s = fl(0)
# s('xiaowang--')
# s('xiaoli--')

class fi():
    def __init__(self, l):
        self.l = l

    def action(self, label):
        print label, self.l
        self.l += 1
f = fi(0)
f.action('zhangsan')
f.action('lisi')









