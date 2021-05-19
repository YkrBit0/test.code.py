# -*- codeing =utf-8 -*-
# @Time : 2021/3/4 19:57
# @Author : 小洛
# @File : domo.1.py
# @Software: PyCharm
'''
f = open("test.txt","w")    #新建文件

f.write("hello world,i am here")    #写入内容

f.close()   #关闭文件
'''
'''
f = open("test.txt","r")

content = f.read(5)

print(content)

content = f.read(10)

print(content)

f.close()
'''

'''
f = open("test.txt","r")

content = f.readlines()
i = 1
for temp in content:
    print("%d:%s"%(i,temp)) #一次性读取所有文件为列表，每行为一个字符串元素
    i+=1
f.close()
'''
'''
f = open("test.txt","r")
content = f.readline()
print("1:%s"%content)
'''
'''
str = "chendu"
print(str)
print(str[0:2])
print(str+",你好")        #字符串连接
print(str*3)
print(r"hello\nchendu")
print("hello\nchendu")      #r表示直接显示原始字符串
'''

'''
namelist = ["小张","小王","小李"]
testlist = [1,"列表"]
print(type(testlist[0]))
print(type(testlist[1]))
print(namelist[2])
'''
'''
namelist = ["小张","小王","小李"]
for name in namelist:
    print(name)
print(len(namelist))


length = len(namelist)
i = 0
while i<length:
    print(namelist[i])
    i+=1
'''

'''
#增------append
namelist = ["小张","小王","小李"]

print("-----增加前，名单数据----")
for name in namelist:
    print(name)
nametemp = input("请输入一个名单")
namelist.append(nametemp)
print("-----增加前，名单数据----")
for name in namelist:
    print(name)
'''

'''
a = [1,2]
b = [3,4]
a.append(b)

print(a)

a.extend(b)           #extend将b中的元素，逐一加到a列表中
print(a)
'''

#增------insert
'''
a = [0,1,2]
a.insert(1,3)   #第一个变量表示下标，第二个表示元素（对象）
print(a)        #指定下标插入元素

'''

'''
#删------del  pop   remove

movieName = ["加勒比海盗","指环王","骇客帝国","第一滴血","指环王","速度与激情",]
print("-----删除前，电影数据----")
for name in movieName:
    print(name)
del movieName[2]
movieName.pop()             #弹出最后一个元素
movieName.remove("指环王")     #直接移除指定元素
print("-----删除后，电影数据----")
for name in movieName:
    print(name)

'''

#改 ：
'''
namelist = ["小张","小王","小李"]

print("-----增加前，名单数据----")
for name in namelist:
    print(name)
namelist[1] = "小明"

print("-----增加前，名单数据----")
for name in namelist:
    print(name)
'''

#查:【in , not in】
'''
namelist = ["小张","小王","小李"]
findname = input("请输入你要查找的学生姓名：")

if findname in namelist:
    print("在学生名单中找到")
else:
    print("未找到")
'''
#用  index  查找指定下标范围的元素，并返回找到对应数据的下标
'''
mylist = ['a','b','c','a','b']

i = mylist.index("a",1,4)
print(i)
#i = mylist.index("a",1,3)       #范围区间左闭右开，找不到会报错，
print(mylist.count("c"))

'''
#升序，降序，反转
'''
a = [1,4,2,3]
print(a)

a.reverse()         #将列表所有元素反转
print(a)

a.sort()            #升序
print(a)

a.sort(reverse=True)    #降序
print(a)
'''

#数组

#schoolName = [[],[],[]]   有3个元素的空列表.每个元素都是一个空列表
'''
schoolName = [["北京大学","清华大学"],["南开大学","天津大学","天津师范大学"],["山东大学","中国海洋大学"]]

print(schoolName[0][0])

temp = len(schoolName)
print(temp)

for names in schoolName:
    for name in names:
        print(name)
 



import random

offices = [[],[],[]]
names = ['a','b','c','d','e','f','g','h']

for name in names:
    index = random.randint(0,2)
    offices[index].append(name)

i = 1
for office in offices:
    print("办公室%d的人数为:%d"%(i,len(office)))
    i+=1
    for name in office:
        print("%s"%name,end="\t")
    print("\n")
    print("-"*20)

'''
'''
products = [["iphone",1688],["MacPro",14800],["小米",2499],["Coffee",31],["Book",60],["Nike",699]]
i = 0

for product in products:
    print("%d"%i,product)
    i+=1
'''
'''
tup1 = ()   #创建一个元组
print(type(tup1))

#tup2 = (50)    #----<class 'int'> 非元组
#tup2 = (50,)
#tup2 = (50,60,70)   <class 'tuple'>
tup2 = (50,60,70)
print(type(tup2))
'''

'''
tup1 = ("abc","def",2000,2020,2222,555)
print(tup1[0])
print(tup1[2])
print(tup1[-1])     #访问最后一个元素
print(tup1[1:5])
'''

'''
#增
tup1 = (12,35,57)
#tup1[0] = 100       #报错，不允许修改
tup2 = ("abc","xyz")
tup = tup1 + tup2
print(tup)
'''

#删
'''
tup1 = (12,35,57)
print(tup1)
del tup1        #删除了整个元组变量
#print("删除后")
#print(tup1)
'''

#字典的定义
'''
info = {"name":"小明","age":18}


#字典的访问
print(info["name"])
print(info["age"])

#访问不存在的键
#print(info["gender"])      #直接访问，报错
print(info.get("gender"))     #使用get方法，没有找到相应的键，返回None
print(info.get("gender","m"))
'''

'''
info = {"name":"小明","age":18}
#增
newID = input("请输入：")
info["id"] = newID

print(info['id'])
'''
#删-----del
'''
info = {"name":"小明","age":18}

print("删除前：%s"%info["name"])

del info["name"]

print("删除后:%s"%info["name"])    #删除了指定键值对后，在次访问会报错
'''
'''
info = {"name":"小明","age":18}
print("删除前：%s"%info)
del info
print("删除后：%s"%info)    #删除字典后，再次访问会报错
'''

#改
'''
info = {"name":"小明","age":18}

info["age"] = 20

print(info["age"])
'''

#查
'''
info = {"name":"小明","age":18}
print(info.keys())          #得到所有的键（列表）

print(info.values())        #得到所有的值（列表）

print(info.items())         #得到所有的项(列表)，每个键值对是一个元组

'''

#遍历所有的键
'''
info = {"name":"小明","age":18}
for key in info.keys():
    print(key)

#遍历所有的值
for value in info.values():
    print(value)
'''
#遍历所有的键值对
'''
info = {"name":"小明","age":18}
for key,value in info.items():
    print("key=%s,value=%s"%(key,value))
'''
#使用枚举函数同时拿到下标和元素
'''
mylist = ["a","b","c","d"]
for i,x in enumerate(mylist):       #enumerate---枚举，列举
    print(i+1,x)
'''
'''
import turtle
q = turtle.Pen("black")
sides = 7
colors = ["red","yellow","cyan","red","blue","purple"]
for x in range(360):
    q.pencolor(colors[x%sides])
    q.forward(x*3/sides+x)
    q.left(360/sides+1)
    q.width(x*sides)
'''

import turtle

q = turtle.Pen()
sides = 7
colors = ["red","yellow","cyan","red","blue","purple"]
for x in range(360):
    q.pencolor(colors[x%sides])
    q.forward(x*3/sides+x)
    q.left(360/sides+1)         # angle 角度
    q.width(x*sides)            # width 宽度












































