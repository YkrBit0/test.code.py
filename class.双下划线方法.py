# -*- codeing =utf-8 -*-
# @Time : 2021/5/10 20:39
# @Author : 小洛
# @File : class.双下划线方法.py
# @Software: PyCharm


class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return "姓名" + self.name + "年龄" + str(self.age)


    def __len__(self):
        print("trigger------")
        return self.age

    def __hash__(self):
        print("hash")
        return 3
    def __eq__(self, other):
        print(self.name,self.age)
        print(other.name,other.age)

    # 自定义下划线方法---
    def __num__(self):
        return 2


# p = Person("lik",22)
# p1 = Person("kil",23)
# len(p)
#
# print(p==p1)   #触发__eq__(self, other):方法

class Brand:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    #可以将一个对象变成dict(字典),可以像dict一样增删改查
    #自动触发方法
    def __getitem__(self, item):
        print("get item---",item)
        print(self.__dict__)

    def __setitem__(self, key, value):
        print("set item")
        self.__dict__[key] = value

    def __delattr__(self, item):
        print("del obj.key时执行--")
        self.__dict__.pop(item)

    def __delitem__(self, key):
        print("obj")
        self.__dict__.pop(key)




'''
b = Brand("字典001",21)
b["name"]

b["website"] = "www.applend.cn"
#改
b["website"] = "https.www.applend.cn"
print(b.website)

del b["name"]

del b.age

'''

class Shool(object):
    def __init__(self,name,addr,type):
       self.name = name
       self.addr = addr
       self.type = type

    def __str__(self):
        return 'shool(%s,%s)'%(self.name,self.addr)

    def __repr__(self):
        return '(%s,%s)'%(self.name,self.addr)


s1 = Shool("lik","上海","私立")

print(str(s1))

print(repr(s1))   #在解析器上直接打印时就调用repr方法





















