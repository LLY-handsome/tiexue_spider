# -*- coding: utf-8 -*-
'''
from flask import Flask
#from test import keyword
from scrapy import cmdline
import os

start = Flask(__name__)

searchkey = input("请输入爬取关键字：")
# searchkey = keyword[0] #杀伤燃烧弹
# print(keyword[0])
# @start.route("/" + str(searchkey))
@start.route("/")
def index():
    # os.system(r"cd C:\Users\77926\Desktop\【铁血社区】scrapyDemo-master\Weapon")
    # os.system('scrapy crawl Weapon_spider')
    cmdline.execute('scrapy crawl Weapon_spider'.split())
    #pass
if __name__ == '__main__':
    #start.add_resource()
    start.run(host="127.0.0.1",port=5100)
'''