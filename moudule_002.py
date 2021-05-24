# -*- codeing =utf-8 -*-
# @Time : 2021/5/17 21:44
# @Author : 小洛
# @File : moudule_002.py
# @Software: PyCharm

#引入自定义模块
'''
import moudule_001

stu = moudule_001.mk_Sum(10,20)
print(stu.che())

sr = moudule_001.Sum(10,50)
print(sr)
'''

import time
#time.sleep(3)
print(time.time())
print(time.localtime(12345))        #转成元组

t = time.gmtime()
print(time.mktime(t))

print(time.asctime())
#time.sleep(3)
#自定义显示时间  字符串----日期
print(time.strftime("%Y %m-%d %H:%M",time.localtime()))

#自定义显示时间  日期----字符串

print(time.strptime("2021/05/21 19:30","%Y/%m/%d %H:%M"))


#数据库操作
import sqlite3

def sql():
    data = ["lsau",12,"sex"]
    cn = sqlite3.connect("KIhsd")
    cu = cn.cursor()
    sql = '''
        create table selfg
        (
        id integer primary key autoincrement, 
        name text,
        age integer ,
        sex text
        )
    
    '''
    cu.execute(sql)
    cn.commit()
    for d in data:
        d = '"'+d+'"'
        sql1 = '''
            insert into selfg
            (
            name,age,sex
            )values (%s)'''%",".join(d)
        cu.execute(sql1)
        cn.commit()
        cn.close()


#文件操作
def file():
    f = open("text.db",'wb')
    f.read()
    f.write("SAEDWRSFDERTWERFWE")
    f.__str__()
    f.close()



# list = [1,2,34,5,6,7,8,9]
# for i in list:
#     print(i)
print("---------------")

import datetime
d = datetime.date
print(d)

print(datetime.datetime.now())

#时间运算

print(datetime.timedelta())

t = datetime.datetime.now()

t1 = t-datetime.timedelta(days=3)

print(t1)








