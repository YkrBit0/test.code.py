# -*- codeing =utf-8 -*-
# @Time : 2020/12/15 16:45
# @Author : 小洛
# @File : 爬虫练习1.py
# @Software: PyCharm

import urllib
import urllib.request
import urllib.request,urllib.error
from bs4 import BeautifulSoup
import re


'''
def main():
    baseurl = bas
    datalist = getData(baseurl)
    savepath = ".\\豆瓣电影TOP.xls"
    #askURL("https://movie.douban.com/top250?start=")
    
findlink = re.compile(r'<a href="(.*?)">')
bas = input("请输入一个网址：")

def getData(baseurl):
    datalist = []
    for i in range(0,1):
        url = baseurl + str(i*25)
        html = askURL(url)
        
    soup = BeautifulSoup(html,"html.parser")
    for item in soup.find_all('div',class_="item"):
        data = []
        item = str(item)
        link = re.findall(findlink,item)[0]
        print(link)

def askURL(url):
    head = { 
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.122  Safari / 537.36 "
    }
    repust = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(repust)
        html = response.read().decode("utf-8")
        #print(html)                             #----------------------打印网页
    except urllib.request.Request as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

    return html


def savedata(savepath):
    print("----save----")



if __name__ == "__main__":
    main()
    
'''
import urllib
import urllib.request
import bs4
from bs4 import BeautifulSoup
import urllib.error
import xlwt


def main():
    baseurl = "https://movie.douban.com/top250?start="
    datalist = getData(baseurl)
    savepath = "doubanTOP.xls"
    saveData(datalist,savepath)
    #askURL("https://movie.douban.com/top250?start=")
#影片详情链接
findlink = re.compile(r'<a href="(.*?)">')
#影片图片链接
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S)   #re.S---让换行符包含在其中
#影片片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
#影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#影片评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')         #\d表示数字
#影片概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
#影片相关内容
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)
def getData(baseurl):
    datalist = []
    for i in range(0,1):
        url = baseurl + str(i*25)
        html = askURL(url)
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_="item"):
            data = []
            item = str(item)

            link = re.findall(findlink,item)[0]
            data.append(link)

            ImgSrc = re.findall(findImgSrc,item)
            data.append(ImgSrc)

            titles = re.findall(findTitle,item)
            if(len(titles)==2):
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/","")
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append(" ")

            Rating = re.findall(findRating,item)
            data.append(Rating)

            Judge = re.findall(findJudge,item)
            data.append(Judge)

            ing = re.findall(findInq,item)
            if len(ing) != 0:
                ing = ing[0].replace("。"," ")
                data.append(ing)
            else:
                data.append(" ")

            bd = re.findall(findBd,item)
            bd = re.sub('<br(\s+)?/>(\s+)?'," ",bd)
            bd = re.sub('/'," ",bd)
            data.append(bd.strip())

            datalist.append(data)
    return datalist
def askURL(url):
    head = {
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.122  Safari / 537.36 "
    }
    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html


def saveData(datalist,savepath):
    print("save---")
    netbook = xlwt.Workbook(encoding="utf-8",style_compression=0)
    sheet1 = netbook.add_sheet("doubanTOP.xls",cell_overwrite_ok=True)
    col = ("电影详情链接","图片链接","影片中文名","影片外文名","评分","评价数","概况","相关信息")
    for i in range(0,8):
        sheet1.write(0,i,col[i])

    for i in range(0,250):
        print("第%d条" %i)
        data = datalist[i]
        for j in range(0,8):

            sheet1.write(i+1,j,data[j])
    netbook.save(savepath)




if __name__ == "__main__":
    main()
