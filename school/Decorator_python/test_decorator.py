#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: test_decorator.py
@time: 2016/9/23 16:51
"""

import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from functools import wraps

def error_element(func):
    @wraps(func)
    def wrapper(self):
        try:
            func(self)
        except NoSuchElementException, e:
            print time.asctime(time.localtime(time.time()))
            print func.__name__
            print func.__doc__
            print e
        return func(self)
    return wrapper


class MyTest_Selenium(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r'D:\Item\MOBILE_M\template\chromedriver.exe')
        self.driver.get('http://m.jd.com')

    @error_element
    def test_0ne(self):
        u'| 测试使用'
        time.sleep(1)
        self.driver.find_element_by_id('index_newkeyword').click()
        time.sleep(1)
        self.driver.find_element_by_id('kw').click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()