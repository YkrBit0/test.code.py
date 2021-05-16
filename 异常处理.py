# -*- codeing =utf-8 -*-
# @Time : 2021/5/15 14:23
# @Author : 小洛
# @File : 异常处理.py
# @Software: PyCharm

'''
while True:
    try:
        print("请输入：")
        num1 = int(input("n1>>"))
        num2 = int(input("n2>>"))
        res = num1 + num2
        print("result",res)
    except Exception as e:
        print('输入错误')
'''

'''
name = "lik"
d = [1,2,3]
while True:
    try:
        print("请输入：")
        num1 = int(input("n1>>"))
        num2 = int(input("n2>>"))
        res = num1 + num2
        print("result",res,name)
        #d[3]
        raise IndexError  #主动触发异常

        # print("请输入：")
        # n = int(input("n>>"))
        # if n == 0:
        #     break



    # except Exception as e:
    #     print('输入错误')
    except ValueError as v: #输入值错误
        print(v)

    except AttributeError as a: #访问一个对象没有的属性
        print(a)

    except IOError as i:   # 输入/输出异常，基本上是文件无法打开
        print(i)

    except IndentationError as d: #语法错误，代码没有正确对齐
        print(d)

    except IndexError as e:  #下标索引超出序列边界，
        print(e)

    except KeyError as k:   #访问字典里不存在的键
        print(k)

    except NameError as n:  #使用一个未赋予对象的变量
        print(n)

    except SyntaxError as s: #代码非法，代码不能编译
        print(s)

    except TypeError as t:  #传入的对象类型与要求不符合
        print(t)

    except KeyboardInterrupt as ke: #Ctrl+c 被按下
        print(ke)

    # except UnboundLocalError as u:  #访问还未设置的局部变量
    #     print(u)

    except Exception as e:
        print(e)
        print('发生错误')

    else:
        print("无异常")

    finally:
        print("不管有没有错都可执行")

'''

#自定义异常
class YoutubeConnectionError(BaseException):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return self.msg

while True:
    try:
        print("请输入：")
        num1 = int(input("n1>>"))
        num2 = int(input("n2>>"))
        res = num1 + num2
        print("result",res)
        print("请输入：")
        n = int(input("n>>"))
        if n == 0:
            break
       # raise YoutubeConnectionError("在中国无法翻墙")

    except IOError as i:
        print(i)
    except YoutubeConnectionError as y:
        print("error",y)

    except IndexError as a:
        print("error",a)


    except Exception as e:
        print('输入错误')



