#!/usr/bin/python
#-*- coding:utf-8 -*-
########################################
# File Name: netease_spider.py
# Author: F.L.K
# Mail: nkuflk@gmail.com
# Created Time: 2015-06-14 23:42:45
########################################

import scrapy
from juvnews.items import JuvnewsItem

class JuvnewsSpider(scrapy.spider.Spider):
	name = 'netease'
	allowed_domains = ['163.com']
	start_urls = [
		'http://sports.163.com/special/00051NSJ/morejuv.html'
	]

	def parse(self, response):
		for sel in response.xpath('//div[@class="col2"]/ul/li'):
			item = JuvnewsItem()
			item['title'] = sel.xpath('span/a/text()').extract()
			item['url'] = sel.xpath('span/a/@href').extract()
			item['date'] = sel.xpath('span[@class="postTime"]/text()').extract()
			item['source'] = '163'
			yield item
