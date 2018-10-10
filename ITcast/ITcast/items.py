# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ItcastItem(scrapy.Item):
    # define the fields for your item here like:
    #其实就是定义实体类的字段

    #老师的姓名
    name = scrapy.Field()
    #老师的职称
    title = scrapy.Field()
    #老师描述信息
    info = scrapy.Field()
