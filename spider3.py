# -*- codeing =utf-8 -*-
# @Time : 2021/3/17 19:44
# @Author : 小洛
# @File : spider3.py
# @Software: PyCharm

#引入工具bao

from bs4 import BeautifulSoup
import urllib.error
import urllib.request
import urllib.parse
import re
import xlwt
import bs4
import sqlite3

#1 爬取网页
#2 保存网页
#3 数据保存

def main():
    baseurl = "https://movie.douban.com/top250?start="

    datalist = getData(baseurl)
    dbpath = "move.db"
    #savapath = "doubanmoves.xls"
    #saveData(datalist,savapath)
    saveData2DB(datalist,dbpath)

#------compile ----创建正则表达式规则
#---影片连接
findlink = re.compile(r'<a href="(.*?)">')
#----re.S---忽略换行符---s---大写
#---影片图片连接
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S)
#影片片名
findTitel = re.compile(r'<span class="title"(.*)</span>')
#影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#评价人数----\d--表示数字
findJudge = re.compile(r'<span(\d*)人评价</span>')
#影片的概况
findIng = re.compile(r'<span class="inq">(.*)</span>')
#影片的相关内容
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)
#1----------爬取网页

def getData(baseurl):
    datalist = []
    #抓取所有的网页
    for i in range(0,10):
        url = baseurl + str(25*i)
        html = askURL(url)
        #解析网页
        soup = BeautifulSoup(html,"html.parser")
        #遍历soup中的所有内容-----形成列表
        for item in soup.find_all('div',class_="item"):
            item = str(item)
            data = []

            link = re.findall(findlink,item)[0]
            #添加图片
            data.append(link)

            imgSrc = re.findall(findImgSrc,item)[0]
            #添加连接
            data.append(imgSrc)

            titles = re.findall(findTitel,item)
            if(len(titles)==2):
                ctitle = titles[0]
                data.append(ctitle)
                #-----replace----去掉无关的符号
                otitle = titles[1].replace("/","")
                data.append(otitle)
            else:
                data.append(titles[0])
                #----外文名留空---
                data.append('')

            rating = re.findall(findRating,item)[0]
            data.append(rating)

            judgeNum = re.findall(findJudge,item)[0]
            data.append(judgeNum)

            inq = re.findall(findIng,item)
            if len(inq) != 0:
                inq = inq[0].replace("。","")
                data.append(inq)
            else:
                #留空
                data.append("")
            bd = re.findall(findBd,item)[0]
            #---bd---表示对bd进行操作
            bd = re.sub('<br(\s+)?/>(\s+)?',"",bd)
            bd = re.sub("/","",bd)
            #---strip---去掉空格
            data.append(bd.strip())

            datalist.append(data)
    return datalist

def askURL(url):
    head = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)"
    " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Mobile Safari/537.36 Edg/89.0.774.54"
            }
    data = bytes(urllib.parse.urlencode({"name":"liming"}),encoding="utf-8")
    html = ''
    #异常处理
    try:
        # 数据封装
        reaquests = urllib.request.Request(url,headers=head,data=data,method="POST")
        # 接收请求
        resqones = urllib.request.urlopen(reaquests)
        #读取网页内容
        html =resqones.read().decode("utf-8")

    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html

#2保存数据
def saveData(datalist,savapath):
    book = xlwt.Workbook(encoding="utf-8")
    sheet = book.add_sheet('豆瓣电影top',cell_overwrite_ok=True)
    col = ("电影连接","电影图片","电影中片名","电影外片名","评分","概况","相关信息")
    for i in range(0,7):
        sheet.write(0,i,col[i])
    for i in range(0,250):
        print("第%d条"%i)
        data = datalist[i]
        for j in range(0,7):
            sheet.write(i+1,j,data[j])
    book.save(savapath)


def saveData2DB(datalist,dbpath):

    init_db(dbpath)
    #连接数据库
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    for data in datalist:
        for index in range(len(data)):
            data[index] = '"'+data[index]+'"'

        sql = '''
                insert into movie250(
                info_link,pic_link,cname,ename,score,rated,instroducion,info
                )
                values(%s)'''%",".join(data)   #join方法将列表中的数据用”,“相分隔
        print(sql)
        #cur.execute(sql)
        #conn.commit()
    cur.close()
    conn.close()

def init_db(dbpath):
    #创建数据表
    sql = '''
        create table movie250(
        id integer primary key autoincrement,
        info_link text,
        pic_link text,
        cname varchar ,
        ename varchar ,
        score numeric ,
        rated numeric ,
        instroduction tevt,
        info text
        )
        
    
    '''
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    #提交操作
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()


