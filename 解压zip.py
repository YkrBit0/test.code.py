# -*- codeing =utf-8 -*-
# @Time : 2021/10/2 10:19
# @Author : 小洛
# @File : 解压zip.py
# @Software: PyCharm


import zipfile
import itertools
filename = input("解压文件名>>>")
a = "abcdefghijklmnopqrstuvwxyz"
b= "0123456789"
c = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chars = ""
print("----选择密码组成数---")
print("a----a~z")
print("b-----0~9")
print("c-----A~Z")
while 1:
    char = input("密码组成>>>")
    if char == "a":
        chars += a
    elif char == "b":
        chars += b
    elif char == "c":
        chars += c
    elif char == "q":
        break
n = int(input("所组密码的字符个数>>>"))
password = '1234'

def uncompress(filename,password):
    try:
        with zipfile.ZipFile(filename) as zfile:
            zfile.extractall("./",pwd=password.encode("utf-8"))
            return True
    except:
        return False

def way1():
    for c in itertools.permutations(chars,n):  #全排列生成密码字典
        password = "".join(c)
        print(password)
        result = uncompress(filename,password)
        if not result:
            print("解压失败",password)
        else:
            print("解压成功",password)
            break



def way2():
    for i in range(0,n):
        for c in itertools.permutations(chars, n):  # 全排列生成密码字典
            password = "".join(c)
            print(password)
            result = uncompress(filename, password)
            if not result:
                print("解压失败", password)
            else:
                print("解压成功", password)
                break





