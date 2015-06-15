# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TiebaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    reply_cnt = scrapy.Field()
    t_url = scrapy.Field()
    t_title = scrapy.Field()
    t_id = scrapy.Field()
    title_content = scrapy.Field()
    author_id = scrapy.Field()
    author_name = scrapy.Field()
    author_days = scrapy.Field()
    author_url = scrapy.Field()
