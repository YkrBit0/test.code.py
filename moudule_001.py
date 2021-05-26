# -*- codeing =utf-8 -*-
# @Time : 2021/5/17 21:12
# @Author : 小洛
# @File : moudule_001.py
# @Software: PyCharm


#模块-----具有特定功能的文件---函数

def Sum(x,y):
    return x+y

# i = Sum(12,20)
# print(i)

#创建类来实现两个数字的加减乘除
class mk_Sum(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def sum(self):
        return self.x+self.y
    def che(self):
        return self.x*self.y

    def lose(self):
        return self.x-self.y

    def except1(self):
        return self.x/self.y
#实例化类实现功能
#st = mk_Sum(10,20)
#加方法
#setattr(mk_Sum,"sum",Sum)
#setattr(st,"Sum",Sum)

# print(st.che())
# print(st.sum())
#引入模块

# import os
# print(os)












