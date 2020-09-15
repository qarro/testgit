#-*- coding:utf-8-*-
from urllib import request
import urllib
from bs4 import BeautifulSoup
import re
import xlwt



def main():
    baseurl = 'https://movie.douban.com/top250?start='
    datalist = getData(baseurl)
    savepath = '豆瓣电影Top250.xls'
    savedata(datalist,savepath)

#创建正则表达式对象。表示规则
#影片链接
findLink = re.compile(r'<a href="(.*?)">')
#影片图片
findImgSrc = re.compile(r'<img.*src=(.*?)"') #re.S让换行符包含在字符中
#影片片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
#评论
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
#概识
findInq = re.compile(r'<span class="inq">(.*)</span>')
#影片的相关内容
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)
#爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0,10):   #调用获取页面信息函数，10次
        url = baseurl + str(i*25)
        html = askURL(url)    #保存获取到的网页源码
    #逐步解析
        soup = BeautifulSoup(html,'html.parser')    #使用html解析器解析获得的html
        for item in soup.find_all('div',class_="item"): #查找符合要求（包含电影信息）的字符串
            data = []
            item = str(item)
            link = re.findall(findLink,item)[0] #用正则表达式查询指定字符串
            data.append(link)    #添加链接
            imgsrc = re.findall(findImgSrc,item)[0]
            data.append(imgsrc)        #添加图片
            title = re.findall(findTitle,item)
            if len(title) == 2:
                ctitle = title[0]       #添加中文名
                data.append(ctitle)
                etitle = title[1].replace('/','')
                data.append(etitle)     #添加英文名
            else:
                data.append(title[0])
                data.append(' ')
            rating = re.findall(findRating,item)[0]
            data.append(rating)         #添加评分
            judge = re.findall(findJudge,item)[0]
            data.append(judge)          #添加评论人数
            inq = re.findall(findInq,item)
            if len(inq) != 0:
                inq = inq[0].replace('。','')
                data.append(inq)
            else:
                data.append(' ')
            bd = re.findall(findBd,item)[0]
            bd = re.sub('<br(\s+)?>(\s+)?',"",bd)  #去掉<br/>
            bd = re.sub('/', '', bd)
            data.append(bd.strip())  #去掉前后空格
            datalist.append(data)
    return datalist


#获取单独一页的信息
def askURL(url):
    head = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }

    request = urllib.request.Request(url,headers=head)
    try:
        respose = urllib.request.urlopen(request)
        html =respose.read().decode('utf-8')
    except urllib.error.URLError as e:
        if hasattr(e,'code'):
            print(e.code)
        if hasattr(e,'reason'):
            print(e.reason)
    return html

def savedata(datalist,savepath):
    work = xlwt.Workbook(encoding='utf-8')
    sheet = work.add_sheet('豆瓣电影Top250')
    col = ('电影链接','图片链接','影片中文名','影片英文名','评分','评论人数','概识','相关信息')
    for i in range(0,8):
        sheet.write(0,i,col[i])
    for i in range(0,250):
        print('第%d条' %i)
        data = datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])  #数据
    work.save(savepath)




if __name__ == '__main__':
    main()
