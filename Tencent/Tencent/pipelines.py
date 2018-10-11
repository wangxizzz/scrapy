# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
class TencentPipeline(object):
    # 用写的方式打开文件，而不是a(追加)，是因为此文件只需要打开一次.
    def __init__(self):
        self.f = open("tencent.json", "w")
    # 所有的item都只经过这一个管道process_item
    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii = False) + ",\n"
        self.f.write(content)
        return item
    def close_spider(self, spider):
        self.f.close()
