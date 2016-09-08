#!/usr/bin/env python
#encoding:utf-8










print '中文'


'''
# 重要内置方法

apply()  #执行函数
map()   #
filter() #True 序列
reduce() #累加
zip()  #
'''

'''
# 内置方法
li = ['alex','zhangsan','lizi']

print vars() #当前模块的所有变量
print __name__

all() #接收一个序列，如果所有的值都是真的 return 真，否则 return 假

'''
'''
{'__builtins__': <module '__builtin__' (built-in)>,
 '__file__': 'D:/Item/day02/day02/day02.py',
 'li': ['alex', 'zhangsan', 'lizi'],
 '__name__': '__main__',
 '__package__': None,
 '__doc__': None}

'''


'''
# 冒泡排序

lis = [13,22,6,99,11]

for m in range(len(lis) - 1):

    for n in range(m + 1, len(lis)):
        if lis[m] > lis[n]:
            temp = lis[n]
            lis[n] = lis[m]
            lis[m] = temp
print lis
'''


'''
# 单项队列

# 队列 FIFO :先进先出
# 栈： 后进先出 （类似弹夹）
from Queue import Queue

q = Queue(10)
q.put(1)  #添加值
q.put(2)

print q.get()  #取数据
print q.get()
print q.get()
print q.get()
'''

'''
#双向队列

import collections

q = collections.deque()
q.append(1)
q.append(11)
q.append(12)
q.append(13)
print q.pop()
'''

'''
#计数器

import collections

c1 = collections.Counter('qweqwertyu')
print c1
'''

'''
作业 计算器 and 购物车

购物车
1. 打印购物车列表 （需要死循环）

eval() 内置计算器
a = "3*5/-2 -(8*3/(20+3/2-5)+4/(3-2)*-3)"
#需要使用正则表达式
'''

'''
集合

a = [5, 6, 7, 8, 9]
b = [7, 8, 9, 10, 11]

c = set(a)
d = set(b)
'''

'''
字典：

clear() 清除内容
copy（）浅拷贝
import copy #深拷贝， 独立的拷贝模块。 copy.deepcopy()
get() 根据key获取value 接收一个自定义返回值。
'''

'''
编码：

# 转换成16进制
print hex(10)
# 转换成8进制
print oct(10)
# 转换成二进制
print bin(3)
'''

'''
 类中的方法：

    __方法__: 内置方法，可能有多种执行方法，至少一种
    方法    ：只有一种执行方法，对象.方法


n1 = 1
n2 = 2
print n1.__add__(n2)
'''

'''
# 三元运算

name = 'alex'
if 1==1:
    name = 'sb'
else:
    name = '2b'

name = 'alex'
name = 'sb' if 1==1 else '2b' #三元运算

names = raw_input('name:')
name = 'sb' if names == 'alex' else 'haoren'
print name
'''
