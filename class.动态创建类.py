# -*- codeing =utf-8 -*-
# @Time : 2021/5/14 20:00
# @Author : 小洛
# @File : class.动态创建类.py
# @Software: PyCharm

class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print("姓名：%s ,年龄：%d"%(self.name,self.age))

# p = Person("lik",21)
# print(type(p))
# print(type(Person))

#通过type动态产生类
def __init__(self,name,age):
    self.name = name
    self.age = age
def show(self):
    print("这只%s的名字是%s,年龄是%d"%(self.role,self.name,self.age))

def walk(self):
    print("看家")
#类名---Dog
dog_class = type("Dog",(object,),{"role":"dog","__init__":__init__,"show":show,"walk":walk})

print(dog_class)
#实例化
d = dog_class("lik",3)
print(d.role,d.name,d.age)
d.show()
d.walk()

#动态创建个类-----type
Cat_class = type("Cat",(object,),{"role":"animal","__init__":__init__,"show":show})

c = Cat_class("aik",2)

c.show()










