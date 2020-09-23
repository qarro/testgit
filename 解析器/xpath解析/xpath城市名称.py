import requests
from lxml import etree

#-*- coding=utf-8 -*-
if __name__ == '__main__':
    # url = 'https://www.aqistudy.cn/historydata/'
    # head = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36 Edg/85.0.564.51'
    # }
    # page_text = requests.get(url=url, headers=head).text
    # tree = etree.HTML(page_text)
    # li_list = tree.xpath('//div[@class="bottom"]/ul/li')
    # # 解析热门城市名称
    # all_city_name = []
    # for li in li_list:
    #     hot_page_name = li.xpath('./a/text()')[0]
    #     all_city_name.append(hot_page_name)
    # # 解析全部城市
    # all_name = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
    # for li in all_name:
    #     all_names = li.xpath('./a/text()')[0]
    #     all_city_name.append(all_names)
    # print(all_city_name)

    url = 'https://www.aqistudy.cn/historydata/'
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36 Edg/85.0.564.51'
    }
    page_text = requests.get(url=url, headers=head).text
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a')
    city_names = []
    for li in li_list:
        city_name = li.xpath('./text()')[0]
        city_names.append(city_name)
    print(city_names,len(city_names))