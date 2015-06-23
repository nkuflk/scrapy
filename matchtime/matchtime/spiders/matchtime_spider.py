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
                time_name = subsel.xpath('text()').extract()[0]
                item['time'] = time_name[0:5]
                item['name'] = time_name[6:-1]
                self.handle(item)
                #  if filter(lambda x: x in item['label'][0].split(','), label.keys()):
                #    print hashlib.md5(item['label'][0].encode('utf-8')).hexdigest()

    def initDB(self):
        self.db = DB()
        self.cur = self.db.getCur()

    def handle(self, item):
        md5 = hashlib.md5(item['name'].encode('utf-8')).hexdigest()
        #sql = self.db.select_match_by_md5 % (md5)
        #cnt = self.cur.execute(sql)
        #if cnt == 0:
        #    sql = self.db.insert_matchtime % (md5, item['date'], item['time'], item['name'])
        #    self.cur.execute(sql)
        #    self.db.commit()
