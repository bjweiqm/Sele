#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: game_sr.py
@time: 2016/8/23 15:05
"""


from selenium import webdriver
import unittest, time

class Game(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r'D:\Item\new_mobile01\template\chromedriver.exe')
        self.driver.get('http://play.11h5.com/legend/game.html?v=1471935885571&fuid=315256525')

    def test_open_game(self):
        self.driver.find_element_by_xpath('/html/body/div[1]').click()
        time.sleep(30)
        while True:
            self.driver.find_element_by_id('StageDelegateDiv').click()
            time.sleep(0.1)

if __name__ == '__main__':
    unittest.main()