#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: Iteration.py
@time: 2016/9/19 15:48
"""

''' 迭代和解析 '''

# 列表解析与map
# ord()返回一个单位的ASCII  print ord('k')
# chr() ord()函数的逆过程   print chr(107)
# map(函数， 可迭代对象)

print list(map(ord, 'spam'))        # 收集字符串中的所有字符的ascii编码

print [ord(x) for x in 'spam']      # 列表推导式 实现

print [x ** 2 for x in range(10)]

print list(map((lambda x: x ** 2), range(10)))

print '-' * 40

print [x for x in range(99) if x % 2 == 0 and x % 3 == 0]

print list(filter((lambda x: x % 2 == 0 and x % 3 == 0), range(99)))

print [x + y for x in [0, 1, 2] for y in [100, 200, 300]]
# || 31行列表推导式 等价于 下方for循环
res = []
for x in [0, 1, 2]:
    for y in [100, 200, 300]:
       res.append(x + y)
print res
# -----------------------------------------------------------------------
print '-' * 40

m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

n = [
    [2, 2, 2],
    [3, 3, 3],
    [4, 4, 4]
]

print [row[1] for row in m]

print [m[row][1] for row in (0, 1, 2)]

print [m[i][i] for i in range(len(m))]