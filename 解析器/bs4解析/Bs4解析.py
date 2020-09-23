#-*- coding=utf-8 -*-
from bs4 import BeautifulSoup
import lxml
import re
if __name__ == '__main__':
    #将本地html文档中的数据加载到该对象中
    fp = open('test.html', 'r', encoding='utf-8')
    soup = BeautifulSoup(fp,'lxml')
    #print(soup)
    #print(soup.findAll('div',class_='song')) #soup.tagName 返回第一次出现的tagName对应标签
    print(soup.select('.song> ul > li')[0].text)
