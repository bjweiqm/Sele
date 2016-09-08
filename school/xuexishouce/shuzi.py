#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: shuzi.py
@time: 2016/8/11 15:16
"""


##############
#     数字   #
##############
'''
# i = 30
# print bin(i)                                              # 二进制
# print oct(i)                                              # 八进制
# print hex(i)                                              # 十六进制
# print int('64', 16)                                       # int函数会将一个数字的字符串变换成为一个整数，并可以通过定义的第二个参数来确定变换后的数字的进制
# print '{0:o}, {1:x}, {2:b}'.format(64, 64, 64)            # 转换类型

# print 10/3                                                # 整数运算 3.0版本后会保留小数
# print 10/3.0                                              # 浮点数运算
# print 10//3                                               # (截断除法)不考虑对象的类型，总会省略掉结果的小数部分

# print ord('w')                                            # 字符转换成数字
# print chr(99)                                             # 数字转换成字符

# from __future__ import division                           # 在python2.6中打开python3.0的 /；不建议使用浮点数强制转换
# print 10/3                                                # python 3.0 中 / 总是保留小数
'''

##############
#     集合   #
##############
x = set('abcde')
y = set('bdxyz')

print 'e' in x                                                      # ’e‘ 是否存在x内
print x - y                                                         #
print x | y                                                         # 并集
print x & y                                                         # 交集
print x ^ y                                                         # 差集


