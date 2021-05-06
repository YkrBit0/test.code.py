# -*- codeing =utf-8 -*-
# @Time : 2021/4/17 9:57
# @Author : 小洛
# @File : class_game2.py
# @Software: PyCharm
class Dog:
    rose = 'dog'
    def __init__(self,name,breed,attack_val):
        self.name = name
        self.bread = breed   #--类型
        self.attack_avl = attack_val
        self.life_val = 100

    def bite(self,person):
        person.life_val -= self.attack_avl
        print("狗[%s]咬了人[%s],人掉血[%s],还有血量[%s]"%(self.name,person.name,self.attack_avl,person.life_val))


class Weapon:
    def dog_stick(self, obj):
        self.name = "打狗棒"
        self.attack_val = 40
        obj.life_val -= self.attack_val
        self.print_log(obj)

    def hnife(self, obj):
        self.name = "圣剑"
        self.attack_val = 80
        obj.life_val -= self.attack_val
        self.print_log(obj)

    def gun(self, obj):
        self.name = "AK47"
        self.attack_val = 90
        obj.life_val -= self.attack_val
        self.print_log(obj)

    def print_log(self, obj):
        print("%s被%s攻击,掉血%s,还剩血量%s..." % (obj.name, self.name, self.attack_val, obj.life_val))


class Person:
    rose = "person"
    def __init__(self,name,sex,attack_val):
        self.name = name
        self.sex = sex
       # self.attack_val = attack_val
        self.life_val = 130
        self.Weapon = Weapon()  #直接实例化

    # def attack(self,dog):
    #     dog.life_val -= self.attack_val
    #     print("人[%s]打了狗[%s],狗掉血[%s],还有血量[%s]" % (self.name, dog.name, self.attack_val, dog.life_val))



d = Dog("mjj","二哈",30)
p = Person("Alex","M",0)
d.bite(p)
p.Weapon.gun(d)
p.Weapon.hnife(d)






