from lxml import etree
if __name__ == '__main__':
    tree = etree.parse('baidu.html')
    #r = tree.xpath('//div[@id="u1"]/a/text()')
    r = tree.xpath('//a/@href')[3]
    print(r)