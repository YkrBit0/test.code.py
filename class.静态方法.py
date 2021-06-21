# -*- codeing =utf-8 -*-
# @Time : 2021/5/5 22:38
# @Author : 小洛
# @File : class.静态方法.py
# @Software: PyCharm

class Animal(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def eat(self):
        print("****")

class Dog(object):
    role = "animal"
    def __init__(self,name):
        self.name = name
    #静态方法---隔断与类中的所有变量的联系
    @staticmethod
    def eat(self):
        print(self.name,"is eating ****")

d = Dog("Akli")
#d.eat()     #报错 静态方法要传入具体的实例
d.eat(d)

