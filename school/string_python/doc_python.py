#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: doc_python.py
@time: 2016/9/1 17:05
"""




'''test doc'''

span = 40

def square(x):
    '''
        求X的平方
    '''
    return x ** 2

class MyDoc():

    '''MyDoc test doc'''

    def ceshi(self):
        '''ceshi test01'''
        pass

    def ceshi01(self):
        '''zhangsanlisi yao jiarenle '''
        pass



# print square(4)
# print square.__doc__
# print MyDoc.ceshi01.__doc__

def maker(N):
    def action(X):
        return X ** N
    return action

# f = maker(2)
# print f(3)

def f1():
    x = 2
    action = (lambda n: n ** x)
    return action
f = f1()
print f(4)

