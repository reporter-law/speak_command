"""程序说明"""
# -*-  coding: utf-8 -*-
# Author: cao wang
# Datetime : 2020
# software: PyCharm
# 收获:
import re
import requests
from lxml import etree

import random
def baidu_spider(keyword):
    url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd={}".format(keyword)
    data = {'wd':keyword}
    #headers = {'User-Agent':  getagent_str()}
    #print(headers)

    r = requests.get(url, params=data)
    message = []
    content_list = etree.HTML(r.text)
    number = content_list.xpath('//*[@id="content_left"]/*')
    #print(len(number))
    for i in range(len(number)-1):
        title = "".join(content_list.xpath('//*[@id="%d"]/h3//text()' % i))
        title = re.findall(r'\w+[\u4e00-\u9fa5]+\w+', title)

        text = "".join(content_list.xpath('//*[@id="%d"]/div[1]//text()' % i))
        text = re.findall(r'\w+[\u4e00-\u9fa5]+\w+', text)

        source = "".join(content_list.xpath('//*[@id="%d"]/div[2]//text()' % i))
        source= re.findall(r'\w+[\u4e00-\u9fa5]+\w+', source)

        if title == "" or text == "":
            pass
        else:
            message.append(["标题: "+"".join(title),"内容:   "+"".join(text),"来源:    "+"".join(source)])

    return "".join(random.choice(message))

#print(baidu_spider("陈科宇"))