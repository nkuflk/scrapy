#!/usr/bin/env python
# encoding: utf-8

import scrapy
import hashlib
from matchtime.items import MatchtimeItem
from matchtime.db import DB

# filter by label
label = {u'足球': 1}


class MatchtimeSpider(scrapy.spider.Spider):
    name = 'matchtime'
    allowed_domains = ['zhibo8.cc']
    start_urls = [
        'http://www.zhibo8.cc'
    ]

    def __init__(self):
        self.initDB()

    def parse(self, response):
        for sel in response.xpath('//div[@id="left"]/div[@class="box"]'):
            date = sel.xpath('div[@class="titlebar"]/h2/@title').extract()
            for subsel in sel.xpath('div[@class="content"]/ul/li'):
                item = MatchtimeItem()
                item['date'] = date
                item['label'] = subsel.xpath('@label').extract()
                time_name = subsel.xpath('text()').extract()[0]
                item['time'] = time_name[0:5]
                item['name'] = time_name[6:-1]
                if item['name']=='':
                    item['name'] = subsel.xpath('b/text()').extract()[0]
                item['md5'] = hashlib.md5(item['name'].encode('utf-8')).hexdigest()
                self.handle(item)
                #  if filter(lambda x: x in item['label'][0].split(','), label.keys()):
                #    print hashlib.md5(item['label'][0].encode('utf-8')).hexdigest()

    def initDB(self):
        self.db = DB()

    def handle(self, item):
        if len(self.db.selectMatchtime(item['md5']))==0:
            self.db.insertMatchtime(item)
        else:
            self.db.updateMatchtime(item)
