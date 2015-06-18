#!/usr/bin/env python
# encoding: utf-8

import scrapy
from matchtime.items import MatchtimeItem


class MatchtimeSpider(scrapy.spider.Spider):
    name = 'matchtime'
    allowed_domains = ['zhibo8.cc']
    start_urls = [
        'http://www.zhibo8.cc'
    ]

    def parse(self, response):
        for sel in response.xpath('//div[@id="left"]/div[@class="box"]'):
            date = sel.xpath('div[@class="titlebar"]/h2/@title').extract()
            for subsel in sel.xpath('div[@class="content"]/ul/li'):
                item = MatchtimeItem()
                item['date'] = date
                item['label'] = subsel.xpath('@label').extract()
                item['time'] = subsel.xpath('text()').extract()[0]
                item['name'] = subsel.xpath('text()').extract()[0]
                print item