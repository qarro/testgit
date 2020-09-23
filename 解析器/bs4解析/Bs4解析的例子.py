#-*- coding=utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
if __name__ == '__main__':
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
    }
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    page_text = requests.get(url=url,headers=head).text
    soup = BeautifulSoup(page_text,'lxml')
    li_list = soup.select('.book-mulu > ul >li')
    fp = open('三国演义.txt', 'w', encoding='utf-8')
    for li in li_list:
        name = li.a.string
        data_url = 'https://www.shicimingju.com' + li.a['href']
        data_page_text = requests.get(headers=head,url=data_url).text
        text_soup = BeautifulSoup(data_page_text,'lxml')
        div_tag = text_soup.find('div',class_="chapter_content")
        content = div_tag.text
        content = content.replace(' ',' ')
        fp.write(name+':'+content)
        print(name+'爬取完成！')