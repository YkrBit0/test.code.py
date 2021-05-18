# -*- codeing =utf-8 -*-
# @Time : 2021/3/20 17:03
# @Author : 小洛
# @File : class_1.py
# @Software: PyCharm

'''
def main():
    print("-----")
    num = Student


if __name__ == '__main__':
    main()
'''
import random

from scipy import rand

'''
import urllib
from urllib import request
import urllib.parse
class Person(object):
    def __init__(self,url):
        self.url = url

    def getdata(self):
        datalist = []
        for i in range(0, 10):
            self.url = url+ str(i * 25)

    def Askurl(self):
        head= {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63'
               }
        data = bytes(urllib.parse.urlencode({"name":"ldis"}),encoding="utf-8")
        req = urllib.request.Request(url,headers=head,data=data)
        response = urllib.request.urlopen(req)
        html = response.read().decode("utf-8")
        return html
url = input("请输入网页连接")
xiaoming = Person(url)

xiaoming.getdata()

#define a class  定义一个类
class Student(object):
    def __init__(self,a,b):
        self.name = a
        self.score = b

   # def print_score(self):
     #   print("%S,%d"%(self.name,self.score))
bath = Student("Bath Limi",99)
print(bath.name)
print(bath.score)
'''
class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distance(self,other):
        x_diff_sq = (self.x-other.x)
        y_diff_aq = (self.y-other.y)
        return (x_diff_sq + y_diff_aq)

    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) +">"
'''
c = Coordinate(3,9)
origin  = Coordinate(0,0)
print(c.distance(origin))
print(Coordinate.distance(c,origin))
print(c)
#判断实列是否为内置
print(isinstance(c,Coordinate))
'''
class Fraction:
    def __init__(self,num,denom):
        #assert 判断数据类型
        assert type(num) == int and type(denom) == int,"Int not used"
        self.num = num
        self.denom = denom

    def __str__(self):
        return str(self.num) + "/" + str(self.denom)

    def __add__(self, other):
        top = self.num * self.denom + self.denom * other.num
        bott = self.denom*other.denom
        return Fraction(top,bott)

    def __sub__(self, other):
        top = self.num * other.denom - self.denom * other.num
        bott = self.denom * other.denom
        return Fraction(top,bott)

    def __float__(self):
        return self.num / self.denom

    def inverse(self):
        return Fraction(self.denom,self.num)
#实例化对象
# a = Fraction(3,8)
# b = Fraction(13,27)
# print(a)
# print(b)
# print(a+b)
# print(a-b)
# print(a.inverse())
# print(float(a))
# print(isinstance(a,Fraction))
# print(isinstance(b,Fraction))

class Fraction1(object):
    def __init__(self,num,denom):
        assert type(num) == int and type(denom) == int
        self.num = num
        self.denom = denom
        self.x = ""
    def __str__(self):
        return "<"+str(self.num)+"/"+str(self.denom)+">"
    def __add__(self, other):
        top = self.num*other.denom+self.denom*other.num
        butt = self.denom*other.denom
        return Fraction(top,butt)
    def __sub__(self, other):
        top = self.num*other.denom-self.denom*other.num
        butt = self.denom*other.denom
        return Fraction(top,butt)

    def __float__(self):
        return self.num/self.denom

    def inserse(self):
        return Fraction(self.denom,self.num)

#类生成的实体的过程-----对象或实例

a = Fraction1(9,3)

b = Fraction1(5,4)
print(a+b)

print(a.inserse())

print(float(a))

































