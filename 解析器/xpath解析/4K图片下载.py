#需求：解析下载图片 http://pic.netbian.com/4kdongman/
import requests
from lxml import etree
import os
if __name__ == '__main__':
    url = 'http://pic.netbian.com/4kdongman/'
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36 Edg/85.0.564.51'
    }
    response = requests.get(url=url,headers=head)
    #手动设置响应数据编码格式
    #response.encoding='utf-8'
    page_text = response.text
    #数据解析 ：src的属性值
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//div[@class="slist"]//li')

    if not os.path.exists('piclibs'):
        os.mkdir('piclibs')
    for li in li_list:
        image_src ='http://pic.netbian.com' + li.xpath('./a/img/@src')[0]
        image_name = li.xpath('./a/img/@alt')[0] + '.jpg'
        #通用处理中文乱码问题
        image_name = image_name.encode('iso-8859-1').decode('gbk')
        img_data = requests.get(url=image_src,headers=head).content
        img_path = 'piclibs/' + image_name
        with open(img_path,'wb',) as fp:
            fp.write(img_data)
            print(image_name + '下载成功！')
