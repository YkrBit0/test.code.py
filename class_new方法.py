# -*- codeing =utf-8 -*-
# @Time : 2021/5/11 19:16
# @Author : 小洛
# @File : class_new方法.py
# @Software: PyCharm


class Student(object):
    #初始化方法
    def __init__(self,name):
        self.name = name
        print("hahxixi")
    #重写new方法
    def __new__(cls, *args, **kwargs):
        #负责执行__init__进行一些实例初始化前的工作
        print(cls,args,kwargs)
        return object.__new__(cls)

#p = Student("likd")



#设计  模式  23种 单例模式

class Print(object):
    tasks = []
    instance = None
    def __init__(self,name):
        self.name = name

    def add_task(self,job):
        self.tasks.append(job)
        print("%s添加任务%s到打印机,总任务数%s"%(self.name,job,len(self.tasks)))

    def __new__(cls, *args, **kwargs):
        #只有第一次实例化的时候，正常进行，后面每次实例化，并不正真创建一个新实例
        if cls.instance is None:
            #进行正常的实例化，并把实例化后的的对象 存在cls.instance里
            obj = object.__new__(cls) #实例化过程
            print("obj",obj)
            cls.instance = obj  #把实例化的对象存下来
        return cls.instance   #以后的每次实例化，直接返回第一次存的实例对象
                #在上一次实例对象的基础上，在次执行__init__

'''
p1 = Print("Word app")
p2 = Print("pdf app")
p3 = Print("excel app")

p1.add_task("word file")
p2.add_task("pdf  file")
p3.add_task("excel file")
print(p1,p2,p3)

'''
class Tasks(object):
    tasks = []
    course = None
    def __init__(self,name):
        self.name = name

    def add_tasks(self,job):
        self.tasks.append(job)
        print("%s加任务%s到线成,总任务%s"%(self.name,job,len(self.tasks)))

    def __new__(cls, *args, **kwargs):
        if cls.course is None:
            obj = object.__new__(cls)
            print("obj",obj)
            cls.course = obj
        return cls.course


t = Tasks("word app")
t1 = Tasks("excel app")
t3 = Tasks("pdf app")

t.add_tasks("clse")
t1.add_tasks("print")
t3.add_tasks("input")

print(t,t1,t3)