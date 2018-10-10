# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
class ItcastPipeline(object):
    #初始化类方法，此方法只会被初始化一次。
    def __init__(self):
        #把数据输出到自定义文件。
        self.f = open("itcast.pipeline.json", "w")


    def process_item(self, item, spider):
        content =  json.dumps(dict(item),ensure_ascii=False) + "\n"
        self.f.write(content.encode("utf-8"))
        return item


    def close_spider(self, spider):
        self.f.close()
# above function is to handle json data.
# You could write many of pipe function to handle different data type.
# such as to handle database data
