# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class ShopPipeline(object):
    def __init__(self):
        self.conn=pymysql.connect(host="127.0.0.1",user='root',passwd='123456',db='tb')

    def process_item(self, item, spider):
        try:
            title=item["title"][0]
            link=item["link"]
            price=item["price"]
            comment=item["comment"]
            print(title)
            print(link)
            print(price)
            print(comment)
            sql="insert into ttb(title,link,price,comment)  values('"+title+"','"+link+"','"+price+"','"+comment+"')"
            self.conn.query(sql)

            return item
        except Exception as err:
            pass

    def close_spider(self):
        self.conn.close()