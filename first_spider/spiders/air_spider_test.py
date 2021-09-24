# -*- coding: utf-8 -*-
"""
Created on 2021-09-23 13:25:29
---------
@summary:
---------
@author: muller
"""

import feapder
from feapder import Item


class AirSpiderTest(feapder.AirSpider):
    def start_requests(self):
        for i in range(1, 10):
            yield feapder.Request("https://www.qiushibaike.com/text/page/{}/".format(i))

    def download_midware(self, request):
        request.headers = {
            'Connection': 'close',
        }
        return request

    def parse(self, request, response):
        print(response)
        url_list = response.xpath('//a[@class="contentHerf"]/@href').extract()
        for i in url_list:
            yield feapder.Request(url=str(i), callback=self.parse_detail, verify=False, download_midware=self.download_midware)
            print(i)

    def parse_detail(self, request, response):
        item = Item()
        item.table_name = 'spider_data'
        title = response.xpath('//h1[@class="article-title"]/text()').extract_first().strip()
        content = response.xpath('//div[@class="content"]/text()').extract_first().strip()
        item.title = title
        item.content = content
        print(title)
        print(content)
        print(item)
        yield item


if __name__ == "__main__":
    AirSpiderTest().start()