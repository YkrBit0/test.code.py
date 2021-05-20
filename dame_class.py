# -*- codeing =utf-8 -*-
# @Time : 2021/4/10 10:25
# @Author : 小洛
# @File : dame_class.py
# @Software: PyCharm

#字典
# dog1 = {
#     "name":"mjj",
#     "d_type":"京巴",
#     "attack_val":30,
#     "life_val":100
# }

attack_vals = {
    '京巴':30,
    '二哈':50,

}
#函数-----模板
def dog(name,d_type):
    data = {
        "name": name,
        "d_type": d_type,
        "life_val": 100
    }
    if d_type in attack_vals:
        data["attack_val"] = attack_vals[d_type]
    else:
        data["attack_val"] = 15
    def dog_bite(person_obj):
        person_obj['life_val'] -= data["attack_val"]
        print("狗[%s]咬了人[%s]一口，人掉血[%s],还有血量[%s]..." % (data['name'],
                                                      person_obj['name'],
                                                      data["attack_val"],
                                                      person_obj['life_val']))
    data['bite'] = dog_bite  #为了从函数外面调用这个dog_bite这个函数
    return data

def person(name,age):
    data = {
        "name" :name,
        "age":age,
        "life_val":100
    }
    if age > 18:
        data["attack_val"] = 50
    else:
        data["attack_val"] = 30
    def beat(dog_obj):
        dog_obj["life_val"] -= data["attack_val"]
        print("人[%s]打了狗[%s]一棒，狗掉血[%s],还有血量[%s]..." % (data['name'],
                                                      dog_obj['name'],
                                                      data['attack_val'],
                                                      dog_obj['life_val']))
    data["beat"] = beat
    return data

#定义动作函数
def dog_bite(dog_obj,person_obj):
    person_obj['life_val'] -= dog_obj["attack_val"]
    print("狗[%s]咬了人[%s]一口，人掉血[%s],还有血量[%s]..."%(dog_obj['name'],
                                                         person_obj['name'],
                                                         dog_obj["attack_val"],
                                                        person_obj['life_val']))
def bite(perso_obj,dog_obj):
    dog_obj["life_val"] -= perso_obj["attack_val"]
    print("人[%s]打了狗[%s]一棒，狗掉血[%s],还有血量[%s]..."%(perso_obj['name'],
                                                        dog_obj['name'],
                                                        perso_obj['attack_val'],
                                                        dog_obj['life_val']))

# d1 = dog("mij","京巴")
# d2 = dog("mjj2","二哈")
# p1 = person("Alex",22)
# a = dog_bite(d1,p1)
# b = bite(p1,d1)
# 找到b1下的函数
# d1['bite'](p1)
# d2["bite"](p1)  #咬人
# d2["bite"](p1)  #咬人
# p1["beat"](d1)  #打狗


class Dog:
    d_type = "京巴"  #属性，类属性，类变量
    sss = "sss"     #属性，类属性，类变量
    def __init__(self,name,age): #初始化方法，构造方法，构造函数，实例化时会自动执行，进行一些初始化工资
        print("haha")
        print(name,age)
        #要想把name,age这两值，真正的存到实例里，那就要把2个值跟实例绑定
        self.name2 = name  #绑定参数值到实例
        self.age2 = age

    def say_hi(self):  # 方法，第一个参数，必须为self,  self---代表实例本身
        print("hell,i am a dog, my type is",self.d_type,self.name2,self.age2)


# d = Dog("mjj",5)     #生成一个实例
# d2 = Dog("md",3)

# d.sex = "w"
# print(d.sex)
# d.say_hi()
# d2.say_hi() #实例.方法
#
# Dog.d_type = "二哈"
# #print(id(d.d_type),id(d2.d_type))
# Dog.d_type = "金毛"
#
# print(d.d_type)

class People:
    nationlity = 'tw'           # 公共属性
    def __init__(self,name,age,sex):    #,nationality
        self.name = name
        self.age = age
        self.sex = sex
        # self.nationlity = nationlity


p = People("mjj",21,"m")
p2 = People("Aliex",21,"w")
p3 = People("jackli",'20','w')
People.nationlity = 'cn'
print(p.nationlity)
p.nationlity = 'jp'  #实例自己改国籍/------改变量---相当于给p实例创建了一个新的实例属性
print(p.nationlity)
print(People.nationlity)
