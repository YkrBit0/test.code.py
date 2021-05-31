# -*- codeing =utf-8 -*-
# @Time : 2020/12/21 19:57
# @Author : 小洛
# @File : spider.tp.py
# @Software: PyCharm
'''
import urllib
import bs4
from bs4 import BeautifulSoup
import urllib.request
import urllib.request,urllib.error




def main():
    baseurl = " "
    datalist = getData(baseurl)
    savapath = "英雄图片"

def getData(baseurl):
    datalist = []


def askURl(url):
    heade = {}
    request = urllib.request.Request(url,headers=heade)
    html = " "
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)


def saveData(savepath):
    print("save---")




if __name__ == '__main__':
    main()
'''


import urllib.request
import urllib.parse
import jsonpath         #筛选数据
import requests
import urllib.error
import xlwt
# url = "  "
# response = requests.get(url).json()
# heroids = jsonpath.__all__(response,'$..heroId')
#
# for heroid in heroids:
#     hero_info_url = " "
#     skin_info_list = jsonpath.parse()


url = 'https://music.163.com/discover/toplist?id=3778678'
head = {
    "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.122  Safari / 537.36 "
}
data = bytes(urllib.parse.urlencode({"name":"xsif"}),encoding="utf-8")
re = urllib.request.Request(url = url,data=data,headers=head)
html = ""
try:
    response = urllib.request.urlopen(re)
    html = response.read().decode("utf-8")
    print(html)
except urllib.error.URLError as e:
    if hasattr(e,"code"):
        print(e.code)
    if hasattr(e,"reason"):
        print(e.reason)






























