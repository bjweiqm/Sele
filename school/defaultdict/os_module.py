#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: os_module.py
@time: 2016/9/22 10:50
"""


"""
import os

def tree2(dpath):
    ''' 遍历目录函数 '''
    for d in os.listdir(dpath):    # 遍历目录
        a_path = '|'+'_'*(len(os.path.abspath(dpath))-1)+'|_'    # 定义输出符号
        if os.path.isdir(os.path.join(dpath,d)):
            print(a_path,d)
            tree2(os.path.join(dpath,d))    # 传入绝对路径，这样就不需要再 chdir
        else:
            print(a_path,d)

# dpath = r'E:\' ; print(dpath)    # 接受用户输入及目录的判断等这里就不写了
# tree2(dpath)
"""


import os

def walk(path='.', level=2):     # 拼接路径的方法实现
    for file in os.listdir(path):    # 遍历列出的文件
        print('|%s|'%('-' * level), file)    # 根据缩进，先打印文件或者目录
        if os.path.isdir(os.path.join(path, file)):   # 判断是目录就递归
            walk(os.path.join(path, file), level + 2)   # 下一层递归，缩进+2

def walk1(path='.', level=2):    # 切换路径的方法实现
    os.chdir(path)   # 进入目标目录
    for file in os.listdir():
        print('|%s|' %('-'*level), file)
        if os.path.isdir(os.path.join(path, file)):
            walk(os.path.join(path, file), level + 2)
            os.chdir('..')          # 因为递归调用会进入下个目录，所以，递归完成时返回上层目录

def walk2(path='.', prefix=''):  # 类似linux中tree命令的风格
    for file in os.listdir(path):
        print(prefix + '|_', file)   # 根据前缀打印文件
        if os.path.isdir(os.path.join(path, file)):
            if file == os.listdir(path)[-1]:
                tmp = prefix + '  '      # 是结尾的目录，后面没有其他该目录的文件，就不要先导的'|'，否则就加上
            else:
                tmp = prefix + '| '
            walk2(os.path.join(path, file), tmp)