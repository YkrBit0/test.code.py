# -*- codeing =utf-8 -*-
# @Time : 2021/4/25 19:21
# @Author : 小洛
# @File : class.校园IT.py
# @Software: PyCharm
'''
1 定义模型


2 定义多少类

-- 总部  分校 学员 老师 员工 课程 班级 --

3 定义属性
   总部： 名称  地址 电话 网址 财务 员工列表 学员列表 发工资 开分校 招人

   分校：
        pass

   学员: 姓名  年龄 班级  于额  上学打卡  转学  交学费

   员工： 姓名  职务  部门  工资  上班打卡

   老师：  教学

   班级： 课程  学期   学员列表   转学   上课记录  考试

   课程： 名称  价格  大纲


4 定义类与类的关系
总部----分校

学员----班级

班级----下区

老师----员工

学员----老师

员工-----校区



5 画UML模型


6写代码


'''


#日期模块
import datetime

class Shool(object):
    '''总部'''
    def __init__(self,name,addr,website):
        self.name = name
        self.abbr = addr
        self.website = website
        self.balance = 0
        #列表存分校
        self.branches = []
        #列表存储班级
        self.class_list = []
        #员工列表
        self.staff_list = []
        print("创建校区%s,地址%s"%(name,addr))



    def count_stu_num(self):
        print(self.class_list)

        pass
    #统计员工数
    def count_staff_num(self):
        pass
    #员工
    def staff_enrollment(self,staff_obj):
        self.staff_list.append(staff_obj)
        print("%s入职新员工%s职位%s,部门%s"%(self.name,staff_obj.name,staff_obj.position,staff_obj.dept))


    def count_total_revenue(self):
        print("---总输入---")
        total_rev = self.balance
        print(self.name,self.balance)
        for val in self.branches:
            print(val.name,val.balance)
            total_rev += val.balance
        print("各校区总收入:%s"%total_rev)

    def count_class_list(self):
        print("---各校区班级---")
        print(self.name,self.class_list)
        for i in self.branches:
            print(i.name,i.class_list)

    def pay_salary(self):
        print("每月发工资啦....")
        for i in self.staff_list:
            i.balance += i.salary  #发工资
            self.balance -= i.salary  #总部相应账户扣钱
            print("给%s发了%s钱员工账户余额%s"%(i.name,i.salary,i.balance))
        print("公司余额:",self.balance)

    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name


class BrancjhSchool(Shool):
    '''分校'''
    def __init__(self,name,addr,website,headquarter_obj):
        super().__init__(name,addr,website)
        self.headquarter = headquarter_obj
        self.headquarter.branches.append(self)



class Course(object):
    '''课程'''
    def __init__(self,name,price,outline):
        self.name = name
        self.price = price
        self.outline = outline
        print("创建了课程:%s学费:%s"%(name,price))

class Class(object):
    '''班级'''
    def __init__(self,course_obj,semester,school_obj):
        self.course_obj = course_obj
        self.semester = semester
        self.school_obj = school_obj
        self.stu_list = []      #存班级列表
        school_obj.class_list.append(self)      #把自己加到总校的班级列表
        print("校区%s创建了班级%s学期%s"%(school_obj.name,course_obj.name,semester))

    def stu_transter(self,stu_obj,nem_class,_obj):
        '''转学'''
        pass
    def __str__(self):
        '''字符串打印方法'''
        return "%s--%s--%s 学期"%(self.school_obj.name,self.course_obj,self.semester)



class Staff(object):
    '''员工'''
    def __init__(self,name,age,balance,salary,position,dept,school_obj):
        self.name = name
        self.age = age
        self.balance = balance
        self.salary = salary
        self.position = position   #职位
        self.dept = dept    #部门
        self.school_obj = school_obj
        school_obj.staff_enrollment(self)

    def punch_card(self):   #打卡
        print("%s打卡在%s上班"%(self.name,self.school_obj.name))

class Teacher(Staff):
    '''老师'''
    def __init__(self,name,age,balance,salary,position,dept,school_obj,course_obj):
        super().__init__(name,age,balance,salary,position,dept,school_obj)
        self.course_obj = course_obj

    def teach_class(self,class_obj,day):
        print("老师%s在班级%s上第%s天可"%(self.name,class_obj,day))


class Student(object):
    '''学生'''
    def __init__(self,name,age,balance,class_obj):
        self.name = name
        self.age = age
        self.balance = balance
        self.class_obj = class_obj
        #加入班级
        class_obj.stu_list.append(self)
        #交学费
        class_obj.school_obj.balance += class_obj.course_obj.price
        self.balance -= class_obj.course_obj.price
        print("班级%s加入了新学员%s,交学费%d"%(class_obj,name,class_obj.course_obj.price))

    def punch_card(self):
        print("%s:%s打卡上%s的课:"%(datetime.datetime.now(),self.name,self.class_obj.name))


# 创建校区
headquarter = Shool("It教育","北京","www.jy.com")
sh1_school = BrancjhSchool("张江校区","上海","ww.con",headquarter)
sh2_school = BrancjhSchool("红去校区","山西","ww.con",headquarter)
luffy = BrancjhSchool("路飞学成","北京","www.jjj.com",headquarter)
sz1 = BrancjhSchool("学成","深圳","www.cvr.com",headquarter)
# 创建 课程
py_course = Course("Python",21000,None)
Linux_course = Course("Linux",19800,None)
test_course = Course("Testing",19800,None)
Jv_course = Course("Java",11000,None)
# 创建 班级
py_24 = Class(py_course,24,headquarter)
go_24 = Class(Linux_course,12,headquarter)
py_5 = Class(Jv_course,24,sh1_school)
Linux_23 = Class(Linux_course,24,sz1)
py_21 = Class(Jv_course,23,sh2_school)
jv_32 = Class(Jv_course,23,luffy)

# 创建 员工 老师 学员
s1 = Staff("Alix",26,0,4000,"CEO","总经理",luffy)
s2 = Staff("lixi",35,0,60000,"CEO","总经理",sh2_school)
s3 = Staff("Yliix",28,0,30000,"Hr","Hr",sh1_school)

#老师
t1 = Teacher("hslk",25,0,25000,"讲师","教育部",sz1,py_24)
t2 = Teacher("kli",23,0,2354,"讲师","教育部",sh2_school,go_24)
t3 = Teacher("kpi",25,0,2384,"学科带头人","教育部",headquarter,py_5)

#学生
stu1 = Student("llk",22,50000,Linux_23)
stu2 = Student("kkh",21,72220,py_5)
stu3 = Student("jki",23,52000,go_24)
stu4 = Student("hju",21,26314,py_24)
stu5 = Student("fdg",22,2354,py_21)
stu6 = Student("ddf",21,22545,jv_32)
#-------------------------------------------------
print(headquarter.balance)

print(headquarter.branches)
print(sz1.balance)

headquarter.count_total_revenue()

headquarter.count_class_list()

headquarter.staff_enrollment(t1)

headquarter.pay_salary()

