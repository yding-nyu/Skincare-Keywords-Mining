# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #文章url
    url = scrapy.Field()
    #文章标题
    title = scrapy.Field()
    #作者
    author = scrapy.Field()
    #正文
    content = scrapy.Field()
