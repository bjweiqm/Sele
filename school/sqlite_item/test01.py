#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: test01.py
@time: 2016/8/4 16:17
"""

import sqlite3


class ceshi():

    def __init__(self):
        self.conn = sqlite3.connect('test.db')
        self.cu = self.conn.cursor()


    def create_db(self):
        self.cu.execute("CREATE TABLE 'video_2016'('id' int PRIMARY KEY ,'name' varchar(20) NOT NULL ,'lianjie' varchar(80) NOT NULL )")
        self.conn.commit()
        self.conn.close()

    def insert_db(self):
        self.cu.execute("INSERT INTO video_2016 (name, lianjie) VALUES ('zhangsan', 'www.lianjia.com');")
        self.conn.commit()
        self.conn.close()



if __name__ == '__main__':
    c = ceshi()
    c.create_db()
    # c.insert_db()


