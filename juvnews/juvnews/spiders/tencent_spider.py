#!/usr/bin/python
#-*- coding:utf-8 -*-
########################################
# File Name: tencent_spider.py
# Author: F.L.K
# Mail: nkuflk@gmail.com
# Created Time: 2015-06-14 23:42:45
########################################

import scrapy
from juvnews.items import JuvnewsItem

class JuvnewsSpider(scrapy.spider.Spider):
	name = 'tencent'
	allowed_domains = ['qq.com']
	start_urls = [
		'http://sports.qq.com/l/isocce/yijia/juven/more.htm'
	]

	def parse(self, response):
		for sel in response.xpath('//div[@class="mod newslist"]/ul/li'):
			item = JuvnewsItem()
			item['title'] = sel.xpath('a/text()').extract()
			item['url'] = sel.xpath('a/@href').extract()
			item['date'] = sel.xpath('span[@class="pub_time"]/text()').extract()
			item['source'] = 'tencent'
			yield item
