# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv
import json
from imsilkroad.items import ImsilkroadItem


class ImsilkroadPipeline:
    def __init__(self):
        self.file = open('xinhuaroad.csv', 'w', newline='', encoding='utf-8-sig')
        self.csvwriter = csv.writer(self.file)
        self.csvwriter.writerow(['TITLE', 'ORGANIZATION', 'TIME', 'URL', 'CONTENT', 'SECTION'])

    def process_item(self, item, spider):
        self.csvwriter.writerow([item["title"], item["organization"], item["time"], item["url"], item["content"],
                                 item["section"]])
        return item

    def close_spider(self, spider):
        self.file.close()
# class ImsilkroadPipeline:
#     def open_spider(self, spider):
#         self.file = open(r"xinhuaroad.json", "w", encoding="utf-8")
#
#     def process_item(self, item, spider):
#         content = json.dumps(dict(item), ensure_ascii=False) + '\n'
#         self.file.write(content)
#         return item
#
#     def close_spider(self, spider):
#         self.file.close()