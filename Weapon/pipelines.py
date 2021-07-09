# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import time
import json
import codecs

class WeaponPipeline(object):
    start = 1
    num = 0
    def __init__(self):
        self.filename = 'C:/Users/77926/Desktop/【铁血社区】scrapyDemo-master/Weapon/spiders/' + '铁血' + time.strftime("%Y%m%d%H%M%S") + '.json'
        # self.f = codecs.open(f_name, 'a', encoding='utf-8')
        # self.content_dict = []
        # #self.content_dict['datalist'] = []

    def process_item(self, item, spider):
        self.num = self.num + 1
        if self.num == 51:
            self.start = 1
            self.num = 0
            self.filename = 'C:/Users/77926/Desktop/【铁血社区】scrapyDemo-master/Weapon/spiders/' + '铁血' + time.strftime("%Y%m%d%H%M%S") + '.json'
        with open(self.filename, "a+", encoding='utf-8') as f:

            item = '{\n' + item['Keyword'] + item['Source'] + item['Title'] + item['Website'] + item['Date'] + item['Content'] + '}'

            if self.start == 0:
                item = ',\n' + item
            if self.start == 1:
                item = '[\n' + item
                self.start = 0
            if self.num == 50:
                item = item + '\n]'
            f.write(item)
        return item

    # def process_item(self, items, spider):
    #     # #content = json.dumps(dict(item), indent=4, ensure_ascii=False) + ",\n"
    #     # self.content_dict.append(dict(item))
    #     # #self.content_dict['datalist'].append(dict(item))
    #     # # self.f.write(content)
    #     # # self.datalist.append(content)
    #     self.num = self.num + 1
    #     if self.num == 51:
    #         self.start = 1
    #         self.num = 0
    #     with open(self.filename, "a+", encoding='utf-8') as f:
    #         items = '{\n' + items['time'] + items['label'] + items['origin'] + items['title'] \
    #                + items['pageUrl'] + items['poster'] + items['content'] + '}'
    #         if self.start == 0:
    #             items = ',\n' + items
    #         if self.start == 1:
    #             items = '[\n' + items
    #             self.start = 0
    #         if self.num == 50:
    #             items = items + '\n]'
    #         f.write(items)
    #     return items

    def close_spider(self, spider):
        # # self.f.write(str(self.datalist))
        # self.f.write(json.dumps(self.content_dict, indent=4, ensure_ascii=False) + ',\n')
        # self.f.close()

        with open(self.filename, "a+", encoding='utf-8') as f:
            #print('爬虫关闭')
            item = '\n]'
            f.write(item)

class myWeaponPipeline:
    def process_item(self, item, spider):
        return {
            'Keyword': '"标签": ' + '"' + item['Keyword'] + '"' + ',' + '\n',
            'Source': '"来源": ' + '"' + '铁血社区' + '"' + ',' + '\n',
            'Title': '"标题": ' + '"' + item['Title'] + '"' + ',' + '\n',
            'Website': '"网址": ' + '"' + item['Website'] + '"' + ',' + '\n',
            'Date': '"时间": ' + item['Date'] + ' ,' + '\n',
            'Content': '"内容": ' + '"' + item['Content'] + '"' + '\n',
        }