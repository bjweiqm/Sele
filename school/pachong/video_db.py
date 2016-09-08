#!/usr/bin/env python
# encoding:utf-8

"""
@software: PyCharm
@file: video_db.py
@time: 2016/8/4 16:56
"""
import sqlite3


class Create_DB():

    def __init__(self):
        self.conn = sqlite3.connect('video.db')
        self.cn = self.conn.cursor()

    def create_table(self, table):
        # 创建表格 table == 创建表命令
        self.cn.execute(table)

    def insert_db(self):
        # 插入数据
        pass

    def select_db(self):
        # 查询数据
        pass


if __name__ == '__main__':
    pass



