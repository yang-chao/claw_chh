# encoding: utf-8
__author__ = 'yangchao'

import sys
reload(sys) # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
sys.setdefaultencoding('utf-8')

import MySQLdb
import logging


class DBHelper:

    def __init__(self):
        # self.__db__ = MySQLdb.connect("localhost", "root", "", "cral_chh", charset="utf8", use_unicode=True)
        self.__db__ = MySQLdb.connect(host='localhost', user='root', passwd='', port=3306, charset="utf8", use_unicode=True)
        self.__db__.select_db('cral_chh')

    def close(self):
        # 关闭数据库连接
        self.__db__.close()

    def insert(self, table, title, link, time, category, author, message_count):
        # 使用cursor()方法获取操作游标
        cursor = self.__db__.cursor()

        # SQL 插入语句
        sql = 'insert into news (title, link, time, type, author, message_count) values(%s,%s,%s,%s,%s,%s)'
        args = (title, link, time, category, author, message_count)
        # print(sql)

        try:
            # 执行sql语句
            cursor.execute(sql, args)

            # 提交到数据库执行
            self.__db__.commit()
        except MySQLdb.IntegrityError:
            # Rollback in case there is any error
            self.__db__.rollback()
        finally:
            cursor.close()
