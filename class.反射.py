# -*- codeing =utf-8 -*-
# @Time : 2021/5/7 18:53
# @Author : 小洛
# @File : class.反射.py
# @Software: PyCharm


#神奇的反射---可以通过字符串的形来式操作对象的属性

class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name,"吃饭")

    def walk(self):
        print("***")


    def sleep(self):
        print("***")

def talk(self):
    print(self.name,"is speaking....")

p = Person("Aliks",21)
print(p.name)

if hasattr(p,'name2'):  #反射
    print("***")

#反射,映射,自省
# getattr()  获取
# setattr()  设置---赋值
# delattr()  删除
#hasattr()    判断对象是否有某种属性

# getattr()  获取
a = getattr(p,'age')
print(a)

#hasattr()    判断对象是否有某种属性
# user_command = input(">>:").strip()
# if hasattr(p,user_command):
#     func = getattr(p,user_command)      #获取的是一个函数方法
#     func()

# setattr()  设置---赋值
#----static 静态属性
setattr(p,"sex","Female")  #第一个变量为所加的属性---sex，第二个变量为属性值---Female
print(p.sex)

#加方法
#实例中加方法
#setattr(p,"speak",talk)
#p.speak(p)

#类中加方法
setattr(Person,"speak",talk)
p.speak()

# delattr()  删除
delattr(p,"age")
if hasattr(p,"age"):
    print("**")
#del p.age

#---------反射模块成员

#print(__name__) #在当前模块主动执行的情况下(不是被导入执行)，等于__main__
                #在被其他的模块导入的情况下，模块名

# if __name__ == "__main__":   #只会在被别的模块导入的时候发挥作用
#     print("hahaha")

import sys
# for k,v in sys.modules.items():
#     print(k,v)

print(sys.modules["__main__"])
mod = sys.modules[__name__]
if hasattr(mod,"p"):
    o = getattr(mod,"p")
    print(o)
#print(mod.p)


class User(object):
    def login(self):
        print("欢迎来到登录界面")
    def register(self):
        print("欢迎来到注册页面")
    def save(self):
        print("欢迎来到储存页面")
def menu():
    print("*** 1:继续  0 ：退出 ***")

while True:
    user_cmd = User()
    menu()
    n = int(input("请输人>>:"))
    if n==1:
        choose = input(">>:").strip()
        if hasattr(user_cmd,choose):
            func = getattr(user_cmd,choose)
            func()
    elif n == 0:
        break
    else:
        print("输入错误，请重新输入")


#用反射优化猜字游戏
class Game(object):
    def __init__(self,number):
        self.number = number
    def game(self):
        num = round(10)
        print("请输入猜测次数")
        k = int(input(">>:"))
        j = 1
        while (j<=k):
            j+=1
            print("请输入猜测数字")
            n = int(input(">>:"))
            if(n>num):
                print("你猜大了")
            elif(n<num):
                print("你猜小了")
            else:
                print("你猜对了")
                break

    def test(self):
        while True:
            menu()
            print("请输入")
            i = int(input(">>:"))
            print("开始游戏")
            if i == 1:
                self.game()
                print("猜测次数结束")
            if i == 0:
                break
g = Game(123)
print("*** game and test ***请选着模式")
n = input(">>:")
if hasattr(g,n):
    fuuc = getattr(g,n)
    fuuc()











