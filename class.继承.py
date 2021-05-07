# -*- codeing =utf-8 -*-
# @Time : 2021/4/17 11:46
# @Author : 小洛
# @File : class.继承.py
# @Software: PyCharm


#定义一个父类
class Animal:
    a_type = "哺乳动物"
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        print("-----父类的执行方法")

    def eat(self):
        print("%s is eating..."%self.name)

#子类继承父类

class Person(Animal):
    a_type = "哺乳高等动物"
    def __init__(self,name,age,sex,hobby):

        #Animal.__init__(self,name,age,sex) == super(Person, self).__init__(name,age,sex)
        #==super().__init__(name,age,sex)
        super().__init__(name,age,sex)
        self.hobby = hobby
        print("---子类的方法")

    def talk(self):
        print("preson %s is talking"%self.name)

    def eat(self):
        #Animal.eat(self)
        super().eat()           #继承父类的方法与Animal.eat(self)一样
        print("人有品味的吃饭")


class Dog(Animal):
    def chase_rabbit(self):
        print("狗在追兔子----")
'''
d = Dog("mjj",2,"W")
p = Person("lil",22,"W",'nr')
d.chase_rabbit()
p.eat()
print(p.name,p.hobby)

p.talk()
print(p.a_type)

'''


class Shenxinbease:
    def flight(self):
        print("早起神仙打架")


class Shenxin(Shenxinbease):
    def fly(self):
        print("--飞----")

class Monkeybase:
    def fight(self):
        print("猿猴打架")

class Monkey:
    def eat_peach(self):
        print("吃桃")

class Monkeying(Shenxin,Monkey):
    def play_gode(self):
        print("***---***")

m = Monkeying()
m.fly()
m.eat_peach()
m.flight()
m.play_gode()














