import requests
import re
import os

if __name__ == '__main__':
    #创建一个文件夹，保存所有图片
    if not os.path.exists('qiutuLibs'):
        os.mkdir('qiutuLibs')

    url = 'https://www.qiushibaike.com/imgrank/'
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
    }
    #爬取整张页面的内容
    response = requests.get(url=url,headers=head).text
    #正则表达式寻找图片链接
    ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'

    img_src_list = re.findall(ex,response,re.S)
    for item in img_src_list:
        item = 'https:'+ item
        img_data = requests.get(url=item,headers=head).content
        #生成图片名称
        img_name = item.split('/')[-1]
        #图片存储位置
        imgPath = './qiutulibs/' + img_name
        with open(imgPath,'wb') as fp:
            fp.write(img_data)
            print(img_name,'下载成功！')