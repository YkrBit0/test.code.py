# -*- codeing =utf-8 -*-
# @Time : 2021/4/27 18:49
# @Author : 小洛
# @File : spider_001.py
# @Software: PyCharm

#引入模块
from urllib import request
import urllib
from urllib import parse
from bs4 import BeautifulSoup
import requests

from lxml import etree
import bs4
import re
#新闻网页连接

baseurl = 'https://kankan.eastday.com/?qid=01365'

''''
url = 'https://mini.eastday.com/assets/images/moudle_bg.png'
#head = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Mobile Safari/537.36 Edg/90.0.818.46'}
#data = bytes(urllib.parse.urlencode({"name":"liming"}),encoding="utf-8")
req = urllib.request.Request(url=url,method="GET")
response = urllib.request.urlopen(req)
html = response.read()
print(html)
soup = BeautifulSoup(html,'parser.html')
t_list = soup.find_all('a',class_="hove lists-item")
for item in t_list:
    item = str(item)
    print(item)

'''

response = requests.request("GET",baseurl)

html = response.text

f = open("./index1.html","rb")

data = etree.HTML(response.text)
t_list = data.xpath("//a[@href]")
for item in t_list:
   print(item)


hr = f.read().decode("utf-8")

soup = BeautifulSoup(hr,"hr.parser")

for x in soup.find_all('a',class_="hove lists-item"):
    x = str(x)
    print(x)














class Journalism(object):
    baseurl = 'https://kankan.eastday.com/?qid=01365'
    def __init__(self,url):
        self.url = url




