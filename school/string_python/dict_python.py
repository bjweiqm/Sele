#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: dict_python.py
@time: 2016/8/23 12:01
"""

def dict_def():
    # 字典的所有方法
    for i in dir(dict):
        if not i.startswith('_'):
            print i

'''
clear
copy
fromkeys
get
has_key
items
iteritems
iterkeys
itervalues
keys
pop
popitem
setdefault
update
values
viewitems
viewkeys
viewvalues
'''


# d = {
#     'a': 'zhangsan',
#     'b': 'lisi',
#     'c': 'wangwu',
# }
#
# print d.clear()                                                # 清空字典
# print d.copy()                                                  # 复制字典
# print d.fromkeys((1, 2, 3), None)                               # a.fromkeys(seq[, value]) 创建一个新的字典，其中的键来自sql，值来自value
# print d.get('1')                                                # 使用字典的key 获取字典的value， 如果key不存在 则返回None
# print d.get('1', -1)                                            # 使用字典的key 获取字典的value， 如果key不存在 则返回-1 （修改返回值）
# print d.has_key('a')                                            # 判断字典的key 是否存在，如果存在返回True 3.0版本去除此方法 使用 in
# print 'a' in d                                                  # 判断字典的key 是否存在，如果存在返回True
# print d.items()                                                 # 以列表的形式返回字典所有内容， key与value在一个元组内 3.0 返回一个迭代器
# print d.iteritems()                                             # 返回一个迭代器
# print d.keys()                                                  # 以列表的形式返回字典所有的key  3.0 返回一个迭代器
# print d.iterkeys()                                              # 返回一个迭代器
# print d.values()                                                # 以列表的形式返回字典所有的value  3.0 返回一个迭代器
# print d.viewitems()
#
# print dir(tuple)



li = 'proto=UDP dzone="" vsys=0 usrid=0'
print dict([x.split('=') for x in li.replace('""', '').split(' ')])


print [x+y for x in 'abcd' for y in 'xyzf']
print [line.strip() for line in open('__init__.py') if line[0] == '@']



