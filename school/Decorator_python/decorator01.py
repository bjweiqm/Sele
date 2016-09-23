#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: decorator01.py
@time: 2016/9/23 14:26
"""



'''装饰器学习基础'''


"""
def talk():
    def whisper(word='yes'):
        return word + '...'
    return whisper

try:
    print whisper()
except NameError, e:
    print e

t = talk()
print t()

"""
# 函数可以返回函数
"""
def get_talk(kind='shut'):
    def whisper(word='yes'):
        return word.lower() + '...'

    def shout(word='yes'):
        return word.capitalize() + '!'
    return whisper if kind == 'whisper' else shout

talk = get_talk()

# print talk
print talk()
print get_talk('whisper')()
"""

"""
# 把函数作为参数传递

def whisper(word='yes'):
    return word.lower() + '....'

def do_something_before(func):
    print 'I do something before.'
    print 'Now the function you gave me:\n', func()

do_something_before(whisper)
"""


'''
#手工装饰器

def my_shiny_new_docorator(a_function_to_decorate):
    """
    Inside, the decorate defines a function on the fly:the wrapper.
    this function is going to be wrapped around the original function
    so it can execute code before and after it.
    """
    def the_wrapper_around_the_original_function():
        """
        Put here the code you want to be executed BEFORE the original function is called
        """
        print 'Before the function runs'
        a_function_to_decorate()
        """
        Put here the code you want to be executed AFTER the original function is called
        """
        print 'After the function runs'
    """
    At this point , 'a_function_to_decorate' HAS NEVER ＢＥＥＮ EXECUTED.
    We return the contains the function and the code to execute before
    and after. It`s ready to use!
    """
    return the_wrapper_around_the_original_function

def a_stand_alone_function():
    print 'I am a stand alone function, don`t you dare modify me'

# a_stand_alone_function()

# a_stand_alone_function_decorated = my_shiny_new_docorator(a_stand_alone_function)
# a_stand_alone_function_decorated()

# 装饰器实现方法
@my_shiny_new_docorator
def anther_stand_alone_function():
    print 'Leave me alone'


anther_stand_alone_function()
'''


"""
# 嵌套装饰器

def bread(func):
    def wrapper():
        print "</``````\>"
        func()
        print "<\______/>"
    return wrapper

def ingredients(func):
    def wrapper():
        print '#tomatoes#'
        print func.__name__ , 'xxxxxx'
        func()
        print '~salad~'
    return wrapper

def sandwich(food='--ham--'):
    print food

# sandwich = bread(ingredients(sandwich))
# sandwich()

@bread
@ingredients
def sandwich(food='--ham_2--'):
    print food

sandwich()
"""


# 装饰器高级用法

"""
# 改装饰器函数传递参数

def a_decorator_passing_arguments(function_to_decorate):
    def a_wrapper_accepting_arguments(arg1, arg2):
        print "I got args! Look:", arg1, arg2
        function_to_decorate(arg1, arg2)
    return a_wrapper_accepting_arguments

@a_decorator_passing_arguments
def print_full_name(first_name, last_name):
    print 'My name is', first_name, last_name

print_full_name('Peter', 'Venkman')

"""


"""
# 装饰器方法

def method_friendly_decorator(method_to_decorate):
    def wrapper(self, lie):
        lie = lie - 3
        print lie
        return method_to_decorate(self, lie)
    return wrapper


class Lucy(object):
    def __init__(self):
        self.age = 32

    @method_friendly_decorator
    def asyYourAge(self, lie):
        print 'I am %s, what did you think?' % (self.age + lie)


l = Lucy()
l.asyYourAge(-3)
"""


"""
# functools.wraps 被封装的名称，模块，文档拷贝给封装函数

'''
def foo():
    print 'foo'

print foo.__name__

def bar(func):
    def wrapper():
        print 'bar'
        return func()
    return wrapper

@bar
def foo():
    print 'foo'
print foo.__name__
'''

import functools

def bar(func):
    @functools.wraps(func)
    def wrapper():
        print 'bar'
        return func()
    return wrapper

@bar
def foo():
    print 'foo'

print foo.__name__

"""


# 使用装饰器做缓存 没研究明白

from functools import wraps

def cache(func):
    caches = {}
    @wraps(func)
    def wrap(*args):
        if args not in caches:
            print 'args == ', args
            print 'caches == ', caches
            caches[args] = func(*args)
            print 'caches +++>', caches
        return caches[args]

    return wrap

# fib_cache = cache(fib_cache(10))
@cache
def fib_cache(n):
    assert n > 0, 'invalid n'
    if n < 3:
        return 1
    else:
        return fib_cache(n - 1) + fib_cache(n - 2)

print fib_cache(10)
