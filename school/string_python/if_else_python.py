#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: if_else_python.py
@time: 2016/8/29 17:32
"""


if 'zhang':
    print 'li'
elif 'wang':
    print 'li1'
else:
    print 'hh'




#三元表达式
# a = 'zhang' if 'li' else 'lisi'
# print a
# a = 'zhang' if '' else 'lisi'
# print a
#等介于
# if 'li':
#     a = 'zhangsan'
# else:
#     a = 'lisi'
# print a

'''range/zip/map/enumerate'''
# print range(10)
# l1 = [1, 2, 3, 4]
# l2 = [5, 6, 7, 8]
# l3 = [9, 10, 11]
# print zip(l1, l2)
# print dict(zip(l1, l2))
# print list(zip(l1, l2))
# print tuple(zip(l1, l2))
# print zip(l1, l3)
# print map(None, l1, l3)
# print list(map(ord, 'name'))
# li = enumerate('zhagnsan')
# print li.next()
# for (k, v) in enumerate('zhangsan'):
#     print k , 'and', v
#
# print ['%s and %s' %(k, v) for (k, v) in enumerate('zhangsan')]
#
# print [c*i for (i, c) in enumerate('zhangsan')]


print [(a,b,c,d,e,f,(g)) for a in range(1,33) for b in range(1,33) for c in range(1,33) for d in range(1,33) for e in range(1,33) for f in range(1,33) for g in range(1,17)]





