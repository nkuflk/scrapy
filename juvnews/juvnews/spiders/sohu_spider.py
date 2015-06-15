#!/usr/bin/python
#-*- coding:utf-8 -*-
########################################
# File Name: sohu_spider.py
# Author: F.L.K
# Mail: nkuflk@gmail.com
# Created Time: 2015-06-14 23:42:45
########################################

import scrapy
from juvnews.items import JuvnewsItem

class JuvnewsSpider(scrapy.spider.Spider):
	name = 'sohu'
	allowed_domains = ['sohu.com']
	start_urls = [
		'http://sports.sohu.com/youwendongtai.shtml'
	]

	def parse(self, response):
		for sel in response.xpath('//div[@class="f14list"]/ul/li'):
			item = JuvnewsItem()
			item['title'] = sel.xpath('a/text()').extract()
			item['url'] = sel.xpath('a/@href').extract()
			item['date'] = sel.xpath('span/text()').extract()
			if item['date']:
				item['date'] = item['date'][0]
			item['source'] = 'sohu'
			yield item
