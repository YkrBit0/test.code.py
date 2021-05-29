# -*- codeing =utf-8 -*-
# @Time : 2020/12/8 20:47
# @Author : 小洛
# @File : t2.py
# @Software: PyCharm
'''
from test1 import t1

#引入自定义

print(t1.add(1,2))


import sys
import os
'''

import requests

import urllib.request
import urllib
'''
response = urllib.request.urlopen("https://www.baidu.com/")

html = response.read().decode("utf-8")

print(html)

'''

#获取一个post请求
import urllib.parse   #解析器
'''
data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")

response = urllib.request.urlopen("http://httpbin.org/post",data=data)
html = response.read().decode("utf-8")
print(html)

'''
'''
try:
    response = urllib.request.urlopen("http://httpbin.org/get",timeout=1)
    html = response.read().decode("utf-8")
    print(html)
except urllib.error.URLError as e:
    print("time out")
'''

# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.getheaders())

#print(response.read().decode("utf-8"))

url = "https://www.douban.com/"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60"
}
data = bytes(urllib.parse.urlencode({"name":"xsa"}),encoding="utf-8")
request = urllib.request.Request(url=url,data=data,headers=header)
response = urllib.request.urlopen(request)
html = response.read().decode("utf-8")
print(html)






