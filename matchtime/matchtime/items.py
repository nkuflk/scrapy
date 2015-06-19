# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MatchtimeItem(scrapy.Item):
    # match type
    label = scrapy.Field()
    # match date
    date = scrapy.Field()
    # match time
    time = scrapy.Field()
    # match name
    name = scrapy.Field()
