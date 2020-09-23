import requests
from bs4 import BeautifulSoup
import re
if __name__ == '__main__':
    fp = open('test.html', 'r', encoding='utf-8')
    soup = BeautifulSoup(fp,'lxml').text
    soup = soup.replace('a','王安   石')
    print(soup)