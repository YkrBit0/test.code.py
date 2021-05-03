# -*- codeing =utf-8 -*-
# @Time : 2021/4/16 20:50
# @Author : 小洛
# @File : class_game.py
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


class Person:
    rose = "person"
    def __init__(self,name,sex,attack_val):
        self.name = name
        self.sex = sex
        self.attack_val = attack_val
        self.life_val = 130

    def attack(self,dog):
        dog.life_val -= self.attack_val
        print("人[%s]打了狗[%s],狗掉血[%s],还有血量[%s]" % (self.name, dog.name, self.attack_val, dog.life_val))



# d1 = Dog("mji","二哈",30)
# d2 = Dog("dt","金毛",50)
#
# p1 = Person("Alex",'m',50)
#
# p1.attack(d1)   #两个对象就交互
#
# d1.bite(p1)

class Dog1:
    def __init__(self,name,age,bread,master):
        self.name = name
        self.age = age
        self.bread = bread
        self.master = master
        self.sayhi()   #调用自己的方法在实例化的时候
    def sayhi(self):
        print("Hi,I am a %s,a %s dog,my master is %s"%(self.name,self.bread,self.master.name))

class Person1:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def walk_dog(self,dog_obj):
        print("主人%s带狗%s去上网..."%(self.name,dog_obj.name))

# p1 = Person1("Aerx",22,"W")
# b1 = Dog1("mjj",2,"二哈",p1)
# p1.walk_dog(b1)

class RelationShip:
    '''保存couple之间的对象关系'''
    def __init__(self):
        self.couple = []
    def make_couple(self, obj1, obj2):
        self.couple = [obj1, obj2]  # 对象进行绑定
        print("%s和%s确定关系" % (obj1.name, obj2.name))
    def get_my_parter(self,obj):
        for i in self.couple:
            if i != obj:
                return i
            else:
                print("---------------")
    def break_up(self):
        print("江湖再见")
        self.couple.clear()

    def break_on(self,a,b):
        print("两人和好")
        self.make_couple(a,b)

class Person2:
    def __init__(self,name,age,sex,relation):
        self.name = name
        self.age = age
        self.sex = sex
        self.relation = relation    #在每个人的实例存储 关系对象
        # self.parter = None      # 要是一个对象
    def do_private_stuff(self):
        pass
relation_obj = RelationShip()   #创建一个实例
#双向关联
p1 = Person2("mjj",23,"M",relation_obj)
p2 = Person2("Lyy",22,"F",relation_obj)
relation_obj.make_couple(p1,p2)
p1.relation.break_up()
p2.relation.get_my_parter(p2)

relation_obj.break_on(p2,p1)







# p1.parter = p2
# p2.parter = p1
# print(p1.parter.name,p2.parter.name)
#
# #解除关联关系
# p2.parter = None
# p1.parter = None








