# -*- codeing =utf-8 -*-
# @Time : 2020/12/8 21:36
# @Author : 小洛
# @File : test.2urllib.py
# @Software: PyCharm


# import urllib
# import urllib.request


#获取一个get请求
#response = urllib.request.urlopen("http://www.baidu.com")
#print(response.read().decode("utf-8"))

'''
#获取一个post请求
import urllib.parse
data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")    #bytes 字节
response = urllib.request.urlopen("http://httpbin.org/post",data=data)
print(response.read().decode("utf-8"))

'''

'''
try:
    response = urllib.request.urlopen("http://httpbin.org/get",timeout=1)
    print(response.read().decode("utf-8"))
except urllib.error.URLError as e:
    print("time out")

'''
'''
response = urllib.request.urlopen("http://www.baidu.com")
#print(response.status)

print(response.getheaders())

'''



# import urllib.parse
# import urllib.request
# from lxml import etree
# import requests

# url = "https://www.baidu.com/"
# reqs = requests.get(url=url)
#
# response = etree.HTML(reqs.text)
# print(response)


'''
url = "https://www.baidu.com/"
head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.55"
            }
data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
rq = urllib.request.Request(url=url,headers=head,data=data)

resqonse = urllib.request.urlopen(url)
print(resqonse.getheader("script"))         #   getheader 获取属性

html = resqonse.read().decode("utf-8")
print(html)
'''
'''
#url = "https://re.1688.com/?cosite=360daohang&location=mingzhan"
url = 'https://www.yuque.com/books/share/ee8e20bf-f275-4b45-97e6-bcd9180ca5c9/gyzx1n'
#url="http://httpbin.org/post"
data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 
(KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.55"}
rep = urllib.request.Request(url = url,data=data,headers=headers,method="POST")
response = urllib.request.urlopen(rep,timeout=60)             #接受服务器的回应
html = response.read().decode("utf-8")
print(html)
'''

'''
class Url(object):
    def __init__(self,url,html):
        self.url = url
        self.html = html

        heade = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.55"}
        data = bytes(urllib.parse.urlencode({"mane":"limi"}),encoding="utf-8")

        req = urllib.request.Request(url,headers=heade,data=data,method="POST")

        resqonses = urllib.request.urlopen(req)

        html = resqonses.read().decode("utf-8")

    def print_me(self):
        print(html)
html = Url("https://re.1688.com/?cosite=360daohang&location=mingzhan")
html.print_me()
'''

from bs4 import BeautifulSoup
import urllib.parse
import urllib.request
import re
import xlwt
import sqlite3

#写正则表达式

#影片详情链接
findlink = re.compile(r'<a href="(.*?)">')
#影片图片链接
findimg = re.compile(r'<img.*src="(.*?)"',re.S)
#影片的片名
findtitle = re.compile(r'<span class="title">(.*)</span>')
#影片的评分
findrating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#评价人数
findjudge = re.compile(r'<span>(\d*)人评价</span>')
#影片的概况
finding = re.compile(r'<span class="inq">(.*)</span>')
#影片的相关内容
findbd = re.compile(r'<p class="">(.*?)</p>',re.S)

#爬取网页数据
url = "https://movie.douban.com/top250?start=0"
heade = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.55"}
data = bytes(urllib.parse.urlencode({"mane":"limi"}),encoding="utf-8")
req = urllib.request.Request(url,headers=heade,data=data)
response = urllib.request.urlopen(req)
html = response.read().decode("utf-8")
datalist = []

#解析网页数据
bs = BeautifulSoup(html,'html.parser')
for item in bs.find_all('div',class_="item"):
    item = str(item)
    data = []
    link = re.findall(findlink,item)[0]
    data.append(link)

    img = re.findall(findimg,item)[0]
    data.append(img)

    title = re.findall(findtitle,item)
    if (len(title)==2):
        etitle = title[0]
        data.append(etitle)
        ctitle = title[1].replace("/","")
        data.append(ctitle)
    else:
        data.append(title[0])
        data.append(" ")

    rating = re.findall(findrating,item)[0]
    data.append(rating)

    judge = re.findall(findjudge,item)[0]
    data.append(judge)

    ing = re.findall(finding,item)
    if len(ing)!=0:
        ing = ing[0].replace('。',"")
        data.append(ing)
    else:
        data.append(" ")

    bd = re.findall(findbd,item)[0]
    bd = re.sub('<br(\s+)?/>(\s+)?',"",bd)
    bd = re.sub("/","",bd)
    #去掉前后的空格
    data.append(bd.strip())

    datalist.append(data)
#保存数据
# book = xlwt.Workbook(encoding="utf-8")
# sheet = book.add_sheet("movietest.01",cell_overwrite_ok=True)
# col = ("电影连接","电影图片","电影中片名","电影外片名","评分","概况","相关信息")
# for i in range(0,7):
#     sheet.write(0,i,col[i])
# for i in range(0,25):
#     print("第%d条"%i)
#     data = datalist[i]
#     for j in range(0,7):
#         sheet.write(i+1,j,data[j])
#book.save("./doubanmoves1.xls")

#print(datalist)

#创建数据库
conn = sqlite3.connect("movieTop.db")
#获取游标,指针
c = conn.cursor()
#创建数据表
sql = '''
        create table movieTop
        (
        id integer primary key autoincrement,
        info_link text,
        pic_link text,
        cname varchar ,
        ename varchar ,
        score numeric ,
        rated numeric ,
        instroduction text,
        info text
        )
'''
c.execute(sql)
conn.commit()
conn.close()

conn = sqlite3.connect("movieTop.db")
cur = conn.cursor()
for data in datalist:
    #print(data)
    for index in range(len(data)):
        if index == 4 or index == 5:
            continue
        data[index] = '"'+data[index]+'"'
    sql1 = '''
        insert into movieTop(
        info_link,pic_link,cname,ename,score,rated,instroduction,info
        )
        values(%s)'''%",".join(data)
    print(sql1)
    cur.execute(sql1)
    #提交操作
    conn.commit()
    conn.close()

#查询数据
conn = sqlite3.connect("movieTop.db")
sor = conn.cursor()
sql2 = "select id,info_link,pic_link,cname,ename,score,rated,instroduction,info from movieTop"

t_list = sor.execute(sql2)

for item in t_list:
    print("id = ",item[0])
    print("info_link = ",item[1])






# t_list = bs.find_all(class_='item')
#
# t_list1 = bs.find_all("title")
# print(t_list1)
# for item in t_list:
#     print(item)


















