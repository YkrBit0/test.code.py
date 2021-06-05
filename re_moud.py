# -*- codeing =utf-8 -*-
# @Time : 2021/5/28 20:46
# @Author : 小洛
# @File : re_moud.py
# @Software: PyCharm

import re

import bs4

from bs4 import BeautifulSoup



f = open("..//index/index1.html","rb")

html = f.read().decode("utf-8")

soup = BeautifulSoup(html,"html.parser")

findlink = re.compile(r'<a class="hove lists-item".*?>(.*)</a>')

link = re.findall(findlink,html)

t_list = soup.select("a[class='hove lists-item']")

#全局匹配---找到一个就行
t_list1 = re.search(r'<a class="hove lists-item".*?>(.*)</a>',html)

print(t_list)

print(t_list1)

# print(soup.title)

print(link)

print("------------------")

# '.'表示任意字符

r = re.search(".","setgr")

print(r)

# '^'匹配字符开头
a = re.search("^asd","asdfdg")
print(a)

# '$'匹配结尾
c = re.search("f$","setfsertf")

print(c)
k = re.search("^ah$","ahdsrgtfsah")

print(k)

#'*'匹配*前的字符0次或多次
g = re.search("a*","aasdasf")
print(g)

d = re.search("d*","afsdgdsfg")
print(d)


# '+'匹配前一个字符1次或多次

x = re.search("a+","aasdsaf")
print(x)
x1 = re.search("a+","sfdafsaf")

print(x1)

# '?'匹配前一个字符1次或0次
s = re.search("a?","asdfafg")
print(s)

# '{m}'匹配前一个字符m次---字符出现n次
# '{n,m}'匹配前一个字符n到m次---字符出现n---m次
n = re.search("a{3}","aaasdager")
print(n)
n1 = re.search("a{3,5}","aaaddddd")
print(n1)

# '|'匹配|左或|右的字符
l = re.search("abc|ABC","abcAbcasdfABC")

print(l)


# '(...)'分组匹配
i = re.search("(abc){1}a(123|45)","abcabca1234568")

print(i)


# '\A' 只从字符开头匹配
g = re.search("\Aabc","abccsdd")   #'\A'开头是abc

p = re.search("\Aabc\Z","abc")    #'\Z'开头是abc结尾是abc


print(g)
print(p)

w = re.search("[a-zA-Z0-9]{5}","abcABC1021")
print(w)

# '\d'表示数字
b = re.search("\d{3}","1234")
print(b)
b1 = re.search(".*\d+.*","sedfgse123446aef")
print(b1)


# ''






def cop():
    import shutil
    shutil.copyfile("re_moud.py","re_moud2.py")









