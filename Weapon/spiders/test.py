# -*- coding: utf-8 -*-
import scrapy
import re
from Weapon.items import WeaponItem
from scrapy import cmdline
#from Weapon.start import searchkey
import time

f = open("category1.txt", "r", encoding="gb18030")
keyword = []
findkeyword = re.compile(r".*【(.*)】.*")

for line in f.readlines():
    line =str(line)
    word = re.findall(findkeyword,line)
    keyword.append(word)


urllist = []
item = WeaponItem()
count = 10

class TestSpider(scrapy.Spider):
    name = 'Weapon_spider'
    allowed_domains = ['bbs.tiexue.net','www.baidu.com']
    start_urls = []

    # searchword = searchkey
    #
    # item['Keyword'] = searchword

    # url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=bds&wd=" + searchword + "&rsv_pq=e1437a360007bd6a&rsv_t=f7d9%2B33o0%2BLdoX%2BZ9uCTCOpRZmEokYTbzUCQR%2FdpgKh4qLZV7%2B6t%2FAnf&rqlang=cn&rsv_enter=1&rsv_dl=tb&si=tiexue.net&ct=2097152&gpc=stf%3D1588771080%2C1620307080%7Cstftype%3D1"
    # start_urls.append(url)

    for i in range(len(keyword)):
        searchwordlist = keyword[i]
        searchword = searchwordlist[0]

        item['Keyword'] = searchword

        # url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=bds&wd=" + searchword + "&rsv_pq=e1437a360007bd6a&rsv_t=f7d9%2B33o0%2BLdoX%2BZ9uCTCOpRZmEokYTbzUCQR%2FdpgKh4qLZV7%2B6t%2FAnf&rqlang=cn&rsv_enter=1&rsv_dl=tb&si=tiexue.net&ct=2097152&gpc=stf%3D1588771080%2C1620307080%7Cstftype%3D1"
        # start_urls.append(url)

    #######多页爬取
    for j in range(0,count*10,10):
        url = "https://www.baidu.com/baidu?word=" + searchword + "&pn" + str(j) + "&tn=bds&cl=3&ct=2097152&si=tiexue.net&s=on"
        start_urls.append(url)

    def parse(self, response):
        hreflist = []
        time.sleep(3)
        #只爬一条
        # web_node_list = response.xpath('//div[@id="content_left"]//div [@class="result c-container new-pmd"][1]//h3/a/@href').extract()
        # hreflist.append(web_node_list[0])

        #一页全爬
        web_node_list = response.xpath('//div[@id="content_left"]//h3/a/@href').extract()
        for i in range(len(web_node_list)):
            hreflist.append(web_node_list[i])

            for href in hreflist:
                #//div [@class="s_form"]//span [@class="bg s_ipt_wr quickdelete-wrap"]//input/@value
                searchworditem = response.xpath('//title/text()').get()
                findsearchword = re.compile(r"(.*)_百度搜索")
                searchworditem = str(searchworditem)
                searchkeyword = re.findall(findsearchword,searchworditem)
                searchword = searchkeyword[0]

                yield scrapy.Request(url=href, meta={'Keyword':searchword},callback=self.new_parse)

    def new_parse(self,response):
        Source = '铁血社区'
        #Title = response.xpath('//div [@class="postContent border"]//div [@class="contents"]//div [@class="contRow_2"]//div [@class="bbsPosTit"]/h1/text()').get().strip()
        Title = response.xpath('//div [@class="postContent border"]//div [@class="contents"]//div [@class="contRow_2"]//div [@class="bbsPosTit"]/h1/text()').extract_first().strip()
        Website = response.request.url

        Date = response.xpath('//div [@class="postContent border"]//div [@class="date"]/text()').extract_first().strip()
        #Date = "".join(Date).strip()
        Date = str(Date).replace(":","").replace("/","").replace(" ","")
        #Date = int(Date)

        Content = response.xpath('//div [@class="postContent border"]//div [@class="contents"]//div [@class="contRow_2"]//div [@id="postContent"]//text()').getall()
        Content = "".join(Content).strip()

        #Name = response.xpath('//div [@class="postContent border"]//div [@class="postStart"]//ul//li [@class= "userName"]//div [@class="user_01"]//strong//a/text()').get()

        Keyword = response.meta['Keyword']

        item = {"Keyword": Keyword, "Source": Source, "Title": Title, "Website": Website, "Date": Date, "Content": Content}
        yield item

cmdline.execute('scrapy crawl Weapon_spider'.split())