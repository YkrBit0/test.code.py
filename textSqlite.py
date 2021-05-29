# -*- codeing =utf-8 -*-
# @Time : 2020/12/24 22:24
# @Author : 小洛
# @File : textSqlite.py
# @Software: PyCharm

#import sqlite3   #数据库
#
# conn = sqlite3.connect("test.db")           #打开或创建数据库
# #
# print("Opend database successfully")
import sqlite3   #数据库
#创建数据库
conn = sqlite3.connect("test.db")
#获取操作数据的游标
cur = conn.cursor()
#写语句
sqlr = '''
create table top120(
    id integer primary key  autoincrement,
    name char ,
    age  integer ,
    sore numeric,
    interint varchar 
)
'''
cur.execute(sqlr)
conn.commit()
conn.close()

print("Opend database successfolly")

















