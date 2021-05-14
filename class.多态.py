# -*- codeing =utf-8 -*-
# @Time : 2021/4/25 10:03
# @Author : 小洛
# @File : class.多态.py
# @Software: PyCharm

class Dog(object):
    def sound(self):
        print("汪汪---")


class Car(object):
    def sound(self):
        print("喵喵----")



def make_sound(animal_obj):
    '''同一调用接口'''
    animal_obj.sound()  #不管传进来的是什么动物都用sound方法

# d = Dog()
# c = Car()
# make_sound(d)
# make_sound(c)

class Document(object):
    def __init__(self,name):
        self.name = name

    def show(self):
        raise NotImplementedError("Subclass must implement abstract method")
        #raise   加注  举起

class Word(Document):
    def show(self):
        return "  "

class Pdf(Document):
    def show(self):
        return "--"

pdf_obj = Pdf("pdf")

word_obj = Word("word")

objs = [pdf_obj,word_obj]

for way in objs:
    print(way.show())









