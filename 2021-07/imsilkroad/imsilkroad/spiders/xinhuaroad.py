import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from imsilkroad.items import ImsilkroadItem


class XinhuaroadSpider(CrawlSpider):
    name = 'xinhuaroad'
    allowed_domains = ['www.imsilkroad.com']
    start_urls = ['https://www.imsilkroad.com/news/category/redianguanzhu']
    rules = (
        Rule(LinkExtractor(allow=r'page=\d+',
             restrict_xpaths='//nav[@class="relative z-0 inline-flex rounded-md shadow-sm -space-x-px"]'), follow=True),
        Rule(LinkExtractor(allow=r'https://www.imsilkroad.com/news/p/', restrict_xpaths='//h5[@class="text-xl"]/a'),
             callback='parse_detail', follow=False),
    )

    # def parse_item(self, response):
    #     node_list = response.xpath('//h5[@class="text-xl"]')
    #     for node in node_list:
    #         item = ImsilkroadItem()
    #         item['URL'] = node.xpath('./a/@href').extract_first()
    #         item['TITLE'] = node.xpath('./a/text()').extract_first().strip()
            # item['ORGANIZATION'] = '新华丝路网'
        # yield item

    def parse_detail(self, response):
        item = ImsilkroadItem()
        item['url'] = response.url
        item['title'] = response.xpath('//h1[@class="text-2xl md:text-4xl mb-4 font-song"]/text()').\
            extract_first().strip()
        item['content'] = response.xpath('//div[@class="essayDetails text-gray-700 prose lg:prose-xl mx-auto"]').\
            extract_first()
        item['section'] = '丝路资讯'
        item['organization'] = '新华丝路网'
        item['time'] = response.xpath('//p[@class="text-sm text-gray-600"]/span[last()]/text()').extract_first().strip()
        yield item




