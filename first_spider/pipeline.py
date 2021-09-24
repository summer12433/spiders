"""
@encoding: utf-8
@author: summer
@contact: 43499756@qq.com
@file: pipeline.py
@time: 2021/9/23 14:36
"""
from feapder.pipelines import BasePipeline
from typing import Dict, List, Tuple
import csv


class Pipeline(BasePipeline):
    """
    pipeline 是单线程的，批量保存数据的操作，不建议在这里写网络请求代码，如下载图片等
    """
    def __init__(self):
        self.file = open('data.csv', 'w', newline='', encoding='utf-8-sig')
        self.csvwriter = csv.writer(self.file)
        self.csvwriter.writerow(['TITLE', 'CONTENT'])

    def save_items(self, table, items: List[Dict]) -> bool:
        """
        保存数据
        Args:
            table: 表名
            items: 数据，[{},{},...]

        Returns: 是否保存成功 True / False
                 若False，不会将本批数据入到去重库，以便再次入库

        """
        for i in items:
            print(i)
            self.csvwriter.writerow([i['title'], i['content']])

        # print("自定义pipeline， 保存数据 >>>>", table, items)
        return True




