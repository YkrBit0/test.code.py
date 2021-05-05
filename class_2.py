# -*- codeing =utf-8 -*-
# @Time : 2021/4/6 21:31
# @Author : 小洛
# @File : class_2.py
# @Software: PyCharm

'''
class Animal(object):
    def __init__(self,age):
        #定义或判断数据类型
        #assert type(self.age) == int and type(self.name) == str
        self.age = age
        self.name = None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self,newmage):
        self.age = newmage
    def set_name(self,newname=""):
        self.name = newname
    def __str__(self):
        return "Animal:"+str(self.name)+":"+str(self.age)

a = Animal(5)
print(a)

a.set_name()
print(a)

a.set_name("lucy")
print(a)
'''

#定义基类
class Animal(object):
    def __init__(self,age):
        #定义或判断数据类型
        #assert type(self.age) == int and type(self.name) == str
        self.age = age
        self.name = None
    #获取
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self,newmage):
        self.age = newmage
    def set_name(self,newname=""):
        self.name = newname
    def __str__(self):
        return "Animal:"+str(self.name)+":"+str(self.age)

#定义子类---继承基类的所有属性和方法
class Dog(Animal):
    def speak(self):
        print("woof")
    def __str__(self):
        return "Dog:"+str(self.name)+":"+str(self.age)
d1 = Dog(4)
print(d1.get_age())
print(d1.set_name("dog"))
d1.get_name()
d1.speak()
print(d1)
#定义子类---继承基类的所有属性和方法
class Person(Animal):
    def __init__(self,name,age):
        #调用Animal中的数据属性
        Animal.__init__(self,age)
        self.set_name(name)
        #存储所有的name
        self.friend = []
    def get_friend(self):
        return self.friend

    def add_friend(self,fname):
        if fname not in self.friend:
            self.friend.append(fname)
    def speak(self):
        print("hello")
    #计算年龄差
    def age_diff(self,other):
        diff = self.age - other.age
        print(diff)
    #定义输出方式
    def __str__(self):
        return "Person:"+str(self.name)+":"+str(self.age)

p1 = Person("Mike",16)
p2 = Person("lucy",18)
print(p1.get_age())
print(p2)
p1.add_friend(p2.get_name())
print(p1.friend)
p2.speak()
p2.age_diff(p1)