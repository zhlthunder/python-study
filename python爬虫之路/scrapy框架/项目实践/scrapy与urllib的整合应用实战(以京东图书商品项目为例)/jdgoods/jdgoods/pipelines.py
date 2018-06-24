# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class JdgoodsPipeline(object):
    def process_item(self, item, spider):
        print(item['pd1'])
        print(item['pd2'])
        print(item['name'])
        print(item['price'])
        print(item['pnum'])
        print(item['author'])
        print(item['pub'])
        print(item['seller'])

        # return item
