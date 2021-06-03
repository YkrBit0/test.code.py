# -*- codeing =utf-8 -*-
# @Time : 2021/3/14 12:34
# @Author : 小洛
# @File : 文件.py
# @Software: PyCharm


# try......finally----和嵌套
'''
import time
try:
    f = open("test1.txt","r")

    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    finally:
        f.close()
        print("文件关闭")

except Exception as result:
    print("发生异常--")
'''

import time



def read():
    try:
        f = open("gushi.txt", "w")
        f1 = open("copy.txt", "w")
        f.write("朝辞白帝彩云间，千里江陵一日还。两岸猿声啼不住，轻舟已过万重山。")
        try:
            while True:
                content = str(f.readlines)
                f1.write(content)
        finally:
            f1.close()
            f.close()
            print("复制完毕")
    except Exception as result:
        print("发生异常---")






f = open("gushi.txt", "w")
f1 = open("copy.txt", "w")
f.write("朝辞白帝彩云间，千里江陵一日还。两岸猿声啼不住，轻舟已过万重山。")
count = str(f.readlines)
print(count)
f1.write(count)
counter = f1.readlines
print(counter)


























