#-*- coding=utf-8 -*-
import requests
from lxml import etree
import re
if __name__ == '__main__':
    url = 'https://sh.58.com/ershoufang/'
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36 Edg/85.0.564.51'
    }
    resepon = requests.get(url=url,headers=head).text
    tree = etree.HTML(resepon)
    li_list = tree.xpath('//ul[@class="house-list-wrap"]/li/text()')

    print(li_list[1])
   #  fp = open('./二手房.txt','w',encoding='utf-8')
   #  i = 0
   # for li in li_list:
   #      标签下继续查找
   #      title = li.xpath('./div[2]/h2/a/text()')[0]
   #     i = i+1
   #      title = title.replace(' ','')
   #     fp.write(title + '\n')
   #      print('第%d条爬取完成！'%i)

