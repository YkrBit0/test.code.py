# -*- codeing =utf-8 -*-
# @Time : 2020/12/24 20:35
# @Author : 小洛
# @File : music.py
# @Software: PyCharm

import urllib.request
import urllib
import requests
import json
'''
def get_music():
    name = input("输入歌手名：")
    yeshu = int(input("输入页数："))
    for x in range(1,yeshu+1):
        url = "https://s.music.so.com/s/song?page="
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66"
                 }
        request = requests.get(url,headers=header)
        html = request.text
        # print(html)
        result = json.loads(html)
        data = result['data']['list']
        for i in data:
            rid = i['rid']
            name = i['name']
            url = 'https://s.music.so.com/s/song?page='
            request = requests.get(url, headers=header)
            music_url = result['url']
            with open('音乐/{}.mp3'.format(name),'wb') as f:
                music = requests.get(music_url)
                f.write(music.content)


get_music()

'''

'''
from urllib import request
from bs4 import BeautifulSoup
import re
import requests
import time


class Music(object):
    def __init__(self, baseurl, path):
        head = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
            }
        self.baseurl = baseurl
        self.headers = head
        self.path = path


    def main(self):
        html = self.askurl()
        bs4 = self.analysis(html)
        name1 = self.matching(bs4)
        self.save(name1)


    def askurl(self):
        req = request.Request(url=self.baseurl, headers=self.headers)
        response = request.urlopen(req)
        html = response.read().decode("utf-8")
        return html


    def analysis(self, html):
        soup = BeautifulSoup(html, "html.parser")
        bs4 = soup.find_all("textarea")
        bs4 = str(bs4)
        return bs4


    def matching(self, bs4):
        rule0 = re.compile(r'"name":"(.*?)","tns":[],"alias":[]')
        name0 = re.findall(rule0,bs4)
        str = ""
        for i in name0:
            str  = str + "," + i
        str = str.replace("\xa0", " ")
        rule1 = re.compile(r'jpg,(.*?),(.*?)","id":(\d*)')
        name1 = re.findall(rule1, str)
        return name1


    def save(self, name1):
        for j in name1:
            print("正在下载：" + j[1] + " - " + j[0] + "...")
            url = "http://music.163.com/song/media/outer/url?id=" + j[2]
            content = requests.get(url=url, headers=self.headers).content
            with open(self.path + j[1] + " - " + j[0] + ".mp3", "wb") as f:
                f.write(content)
            print(j[1] + " - " + j[0] + "下载完毕。\n")
            time.sleep(0.5)
        return


if __name__ == "__main__":
    baseurl = "https://music.163.com/discover/toplist?id=3778678"  # 要爬取的热歌榜链接
    path = "E:/360下载/网易云热歌榜/"  # 保存的文件目录
    demo0 = Music(baseurl, path)
    demo0.main()
    print("下载完毕")
'''
# def getmusic():
#     name = input("输入歌手名：")
#     yeshu = int(input("输入页数："))
#     for i in range(0,yeshu+1):
#         url = ''
'''


from lxml import etree
url = 'https://music.163.com/discover/toplist?id=3778678'
respose = requests.get(url = url)
html = etree.HTML(respose.text)
id_list = html.xpath('//a[contains(@href,"song?")]')

url_base = "http://music.163.com/song/media/outer/url?id="
for data in id_list:
    href = data.xpath('./@href')[0]
    music_id = href.split("=")[1]          #裁剪数据split
    music_name = data.xpath('./text()')[0]
    music_url = url_base + music_id
    music = requests.get(url = music_url)
    with open('./music/%s.mp3' % music_name,'wb') as file:
        file.write(music.content)
        print('<%s>下载成功----' %music_name)
          
'''
from lxml import etree

import urllib.error

from urllib import parse

from bs4 import BeautifulSoup

import re

import xlwt

# findlink = re.compile(r'<a href="/(.*?)">',re.S)
#
# url = "https://music.163.com/#/discover/toplist?id=3779629"
# #异常处理
# try:
#     head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
#         "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63"}
#     data = bytes(urllib.parse.urlencode({"name":"limi"}),encoding="utf-8")
#     #发送请求
#     ret = urllib.request.Request(url,headers=head,data=data)
#     #接受返回
#     response = urllib.request.urlopen(ret)
#     #读出返回内容
#     html = response.read().decode("utf-8")
#     soup = BeautifulSoup(html, "html.parser")
#     for txt in soup.find_all('span',class_="txt"):
#         datamusic = []
#         txt = str(txt)
#         link = re.findall(findlink,txt)
#         print(link)
#
#     print(html)
# except urllib.error.URLError as e:
#     if hasattr(e,"code"):
#         print(e.code)
#     if hasattr(e,"reason"):
#         print(e.reason)


'''
response = requests.get(url)

html = etree.HTML(response.text)

print(html)

#music = html.xpath('./')
music_name = html.xpath('./text()')[0]
with open('./music/%s.mp3'%music_name,'wb') as file:
    file.write(response.content)
    
'''
import sqlite3
#主函数
def main():
    baseurl = 'https://y.music.163.com/m/discover/toplist?id='
    datalist = getdata(baseurl)
    dbpath = "music.db"
    dpath = "音乐文件.xls"
    #savedata(datalist,dbpath)
    savepath(datalist,dpath)


#url = 'https://y.music.163.com/m/discover/toplist?id=2884035'
#歌曲名称
findtitle = re.compile(r'<li><a.*>(.*?)</a></li>')
#歌曲详情链接
findlimk = re.compile(r'<li><a href="(.*?)">.*</a></li>')
#抓取网页
def askurl(url):
    head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63"}
    #data = bytes(urllib.parse.urlencode({"name":"limi"}),encoding="utf-8")
    #发送请求
    ret = urllib.request.Request(url,headers=head)
    #接受返回
    response = urllib.request.urlopen(ret)
    #读出返回内容
    html = response.read().decode("utf-8")
    return html
#获取数据
def getdata(baseurl):
    datalist = []
    col = (19723756,3779629,2884035,3778678)
    for i in range(len(col)):
        url = baseurl + str(i)
        html = askurl(url)
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('ul',class_="f-hide"):
            for row in item:
                row = str(row)
                title = re.findall(findtitle,row)
                #extend---- 以元素的形式追加到列表中
                link = re.findall(findlimk,row)
                link.extend(title)
                datalist.append(link)
    return datalist
#保存数据
def savedata(baselist,bdpath):
    init(bdpath)
    conn = sqlite3.connect(bdpath)
    cur = conn.cursor()
    for data in baselist:
        if len(data) == 2:
            for index in range(len(data)):
                data[index] = '"'+ data[index] + '"'
            sql = '''
                insert into contmusic
                (info_link,nametitle)
                values (%s)'''%",".join(data)
            cur.execute(sql)
            conn.commit()
        else:
            continue
def init(dbpath):
    sql = '''
        create table contmusic
        (id integer primary key autoincrement,
        nametitle text,
        info_link char(50)
        ) 
    '''
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    c.execute(sql)
    conn.commit()
    print("创建数据库成功")
    conn.close()

#保存方法2
def savepath(baset,dpath):
    work = xlwt.Workbook(encoding = "utf-8",style_compression="0")
    sheet1 = work.add_sheet("音乐LISt",cell_overwrite_ok=True)
    col1 = ("详情链接","音乐名")
    basedata = []
    data = []
    for data in baset:
        if len(data) == 2:
            basedata.append(data)

    for i in range(0,2):
        sheet1.write(0,i,col1[i])

    for i in range(0,len(basedata)):
        print("第%s条"%(1+i))
        data = basedata[i]
        for j in range(0,2):
            sheet1.write(1+i,j,data[j])
        work.save(dpath)




if __name__ == "__main__":
    main()
    print("爬取完毕")
















