# -*- coding: utf-8 -*-
import scrapy
'''
从项目名字Itcast下的items.py文件导入ItcastItem类。
可以用ITcast.items这样导，是因为有__init__.py文件存在。
'''
from ITcast.items import ItcastItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    # 域名允许的范围，作为过滤的作用。也可以不要这个条件
    allowed_domains = ['http://www.itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        node_list = response.xpath("//div[@class='li_txt']")
        # 存放老师信息的列表
        # items = []
        for node in node_list:
            # 创建一个Item对象，用来存储信息
            item = ItcastItem()

            #extract()方法是将node.xpath()返回的对象转换为unicode字符串
            names = node.xpath("./h3/text()").extract()
            titles = node.xpath("./h4/text()").extract()
            infos = node.xpath("./p/text()").extract()
            #xpath() 返回的是一个列表，需要通过索引[0]访问。
           
            #print("name:%s"%names)
            #print("title:%s:"%titles)

            item['name'] = names[0]
            item['title'] = titles[0]
            item['info'] = infos[0]

            #items.append(item)
            
            #将获取的数据交给管道pipeline，实时的处理数据，不用在内存堆积。
            yield item
        # 返回数据不经过管道，返回给引擎。会存在当数据很多时，占用内存过大问题。
        #return items
