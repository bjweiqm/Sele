#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: apihelper.py
@time: 2016/10/11 12:22
"""

def info(object, spacing=10, collapse=1):
    '''Print methods and doc strings.

    Takes module, class, list, dictionary, or string. '''
    methodList = [method for method in dir(object) if callable(getattr(object, method))]
    processFunc = collapse and (lambda s:' '.join(s.split())) or (lambda s: s)
    print '\n'.join(['%s %s' % (method.ljust(spacing), processFunc(str(getattr(object, method).__doc__))) for method in methodList])



if __name__ == '__main__':
    li = []
    # info(li, 15, 0)
    # print [method for method in dir(li) if callable(getattr(li, method))]




