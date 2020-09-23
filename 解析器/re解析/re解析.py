import requests
import re

if __name__ == '__main__':
    url = 'https://www.qiushibaike.com/article/123570111'
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
    }
    page_text = requests.get(url=url,headers=head).text
    ex = '<div class="thumb">.*?<img '