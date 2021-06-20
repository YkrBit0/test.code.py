# -*- codeing =utf-8 -*-
# @Time : 2021/5/15 15:38
# @Author : 小洛
# @File : assert.断言.py
# @Software: PyCharm


'''
def my_interface(name,age,score):
    #进行断言判断
    assert type(name) is str
    assert type(age) is int
    assert type(score) is float

my_interface("lij",21,120.1)
'''


def kadanAl(array):
    currentMax = -float('inf')
    maxSubArray = currentMax

    for element in array:
        currentMax = max(currentMax+element,element)
        maxSubArray = max(currentMax,maxSubArray)
    return maxSubArray

array = [3,5,-9,1,3,-2,3,4,7,2,-9,6,3,1,-5,4]

print(kadanAl(array))


class Dog(object):
    _sty = 1

    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.cl_dog(self)

    def __str__(self):
        return "名字",self.name,"年龄",self.age


    @classmethod
    def cl_dog(cls,obj):

        if obj.name:
            cls._sty +=1

            print("生成一只狗",cls._sty,obj.name)


a = Dog("KAIDA",2)

print(a.__str__())











