# -*- codeing =utf-8 -*-
# @Time : 2021/9/29 22:31
# @Author : 小洛
# @File : file.py
# @Software: PyCharm

import urllib.request
import urllib.parse
import re
import xlwt
from bs4 import BeautifulSoup
import sqlite3

def main():
    url = "https://movie.douban.com/top250?start=0"
    datalist = PaseUrl(url)
    path = "./豆瓣电影Top250.xls"
    name = "豆瓣电影"
    Savedata(name,datalist,path)

    savepath = "moviedata.db"


#创建正则类
class Re_list(object):
    #影片链接
    find_link = re.compile(r'<a href="(.*?)">')
    #图片链接
    imgsrc_link = re.compile(r'<img.*src="(.*?)"class="">',re.S)
    #片名
    find_text = re.compile(r'<span class="title">(.* ?)</span >',re.S)
    #影片评分
    find_rating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
    #评价人数据
    find_judge = re.compile(r'<span>(\d*)人评价</span>')
    #评价
    find_ing = re.compile(r'<span class="inq">(.*)</span>')
    #
    find_bd = re.compile(r'<p class="">(.*?)</p>',re.S)

    def __init__(self):

        pass

#获取网页
def askurl(url):
    try:
        head = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}
        data = bytes(urllib.parse.urlencode({"equest Method": "GET","Status Code": "200","Remote Address": "116.211.202.164:443","Referrer Policy":"unsafe-url"}),encoding="utf-8")
        #封装请求
        ret = urllib.request.Request(url,headers=head,data=data,method="POST")
        #接收请求
        res = urllib.request.urlopen(ret)
        #读取
        html = res.read().decode("utf-8")
        return html

    except UnicodeError as e:
        if hasattr(e,"code"):
            print(e.code)
        elif hasattr(e,"reson"):
            print(e.reson)

#解析网页
def PaseUrl(baseurl):
    datalist = []
    for i in range(1):
        baseurl = baseurl + str(i)
        html = askurl(baseurl)
        soup = BeautifulSoup(html,"html.parser")

        for data in soup.find_all('div', class_="item"):

            data = str(data)
            data_t = []

            link = re.findall(Re_list.find_link,data)[0]
            data_t.append(link)

            text = re.findall(Re_list.find_text,data)
            if len(text) == 2:
                ctext = text[0]
                data_t.append(ctext)
                wtext = text[1].replace("/","")
                data_t.append(wtext)
            else:
                data_t.append(text[0])
                data_t.append(" ")


            imgsrc = re.findall(Re_list.imgsrc_link,data)[0]
            data_t.append(imgsrc)


            rating = re.findall(Re_list.find_rating,data)[0]
            data_t.append(rating)

            jugnum = re.findall(Re_list.find_judge,data)[0]
            data_t.append(jugnum)

            ing = re.findall(Re_list.find_ing,data)
            if len(ing) !=0:
                ing = ing[0].replace('。','')
                data_t.append(ing)
            else:
                data_t.append("")


            bd = re.findall(Re_list.find_bd,data)[0]
            bd = re.sub('<br(\s+)?>(\s+)',"",bd)  #去掉<br>
            bd = re.sub("/"," ",bd)
            data_t.append(bd.strip())         #去掉 空格
            datalist.append(data_t)
    return datalist

#创建表格

def sheets(workname):
    Work = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheets = Work.add_sheet(workname, cell_overwrite_ok=True)
    return sheets,Work

#----表格保存信息---1
def Savedata(name,datalist,savepath):
    sheet = sheets(name)

    coll = ['电影详情链接','中文片名','外文片名','图片链接','评分','评价人数','概况','相关信息']

    for i in range(0,8):
        sheet[0].write(0,1,coll[i])

    for i in range(0,250):
        print("第%d条"%i)

        data = datalist[i]

        for j in range(0,8):
            sheet[0].write(i+1,j,data[j])

    sheet[1].save(savepath)

#---数据库保存信息---1

def Savedata_Sql(dbpath,datalist):
    Sqlat(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    for data in datalist:
        for index in range(len(data)):
            if index == 4 or index == 5:
                continue
            data[index] = '"'+data[index]+'"'

            sql = '''
            insert into movieTop250
            (info_link,cname,ic_link,scor,rated,instroduction,info
            )values(%s)'''%','.join(data)

            cur.execute(sql)
            conn.commit()

    conn.close()

def Sqlat(savepath):

    #获取数据库游标
    conn = sqlite3.connect(savepath)
    c = conn.cursor()
    print("打开数据库")
    #写数据库操作语句
    sql = '''
    create table movieTop250
        (id int primary key authorization,
        info_link text,
        cname varchar ,
        wname varchar ,
        pic_link text,
        score numeric ,
        rated numeric ,
        instroduction text,
        info text,
         );
    
    '''
    c.execute(sql)  #执行sql语句
    conn.commit()  #提交操作
    conn.close()   #关闭数据库
    print('成功建表')

if __name__ == '__main__':
    pass







