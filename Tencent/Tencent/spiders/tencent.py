# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    baseURL = "https://hr.tencent.com/position.php?&start="
    offset = 0
    start_urls = [baseURL + str(offset)]
    def parse(self, response):
        # 表示在下面两个节点的数据都可以拿到
        node_list =  response.xpath("//tr[@class = 'even'] | //tr[@class = 'odd']")
        for node in node_list:
            item = TencentItem()
            # extract()把xpath对象转换为unicode字符串。注意返回的是一个列表.
            # 把unicode转换为utf-8
            positionName = node.xpath("./td[1]/a/text()").extract()[0].encode("utf-8")
            positionLink = node.xpath("./td[1]/a/@href").extract()[0].encode("utf-8")
            # 如果有值表示len大于0,,条件成立.
            positionType = ""
            if len(node.xpath("./td[2]/text()")):
                positionType = node.xpath("./td[2]/text()").extract()[0].encode("utf-8")
            peopleNumber = node.xpath("./td[3]/text()").extract()[0].encode("utf-8")
            workLocation = node.xpath("./td[4]/text()").extract()[0].encode("utf-8")
            publishTime = node.xpath("./td[5]/text()").extract()[0].encode("utf-8")
            item['positionName'] = positionName
            item['positionLink'] = positionLink
            item['positionType'] = positionType
            item['peopleNumber'] = peopleNumber
            item['workLocation'] = workLocation
            item['publishTime'] = publishTime
            # 这个yield的作用每取到一个节点数据就返回给管道，然后程序继续执行for循环
            yield item

        # 实现翻页的功能--拼接url地址,重新发送请求.
        if self.offset < 3010:  # 注意：这里把数据写死了。不好 
            self.offset += 10
            url = self.baseURL + str(self.offset)
            # 重新构造请求，并且发送数据
            yield scrapy.Request(url, callback=self.parse)
    

    # 当然也可以自定义回调函数,进行处理解析数据










