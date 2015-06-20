#!/usr/bin/env python
# encoding: utf-8

import scrapy
import hashlib
from matchtime.items import MatchtimeItem
from matchtime.db import DB

# config
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
                item['time'] = subsel.xpath('text()').extract()[0]
                item['name'] = subsel.xpath('text()').extract()[0]
                if filter(lambda x: x in item['label'][0].split(','), label.keys()):
                    print hashlib.md5(item['label'][0].encode('utf-8')).hexdigest()

    def initDB(self):
        db = DB()
