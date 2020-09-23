#-*- coding=utf-8 -*-
import requests
import re
import os

def main():
    if not os.path.exists('qiutuLibs2'):
        os.mkdir('qiutuLibs2')
    url = 'https://www.qiushibaike.com/imgrank/page/%d/'
    for pageNum in range(1,3):
        new_url = format(url%pageNum)
        data(new_url)



def data(url):
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
    }
    # 爬取整张页面的内容
    response = requests.get(url=url, headers=head).text
    ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
    page_data = re.findall(ex,response,re.S)
    for item in page_data:
        item = 'https:' + item
        img_data = requests.get(url=item,headers=head).content
        img_name = item.split('/')[-1]
        name_path = './qiutuLibs2/' + img_name
        with open(name_path, 'wb') as fp:
            fp.write(img_data)
            print('爬取成功！')


if __name__ == '__main__':
    main()