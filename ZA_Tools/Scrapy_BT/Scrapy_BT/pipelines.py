# -*- coding: utf-8 -*-
import codecs,json,pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class ScrapyBtPipeline(object):
#     def process_item(self, item, spider):
#         # return item
#         # 如果爬虫名是movie
#         if spider.name == 'dmhy':
#             print('老子是dmhy的管道，我感受到了力量')
#             dmhyPipeline(object)
#         elif spider.name == 'book':
#             print('老子是book的管道，我感受到了力量')
#         else:
#             print("我是谁，我在哪，我在做什么")


# class dmhyPipeline(object):
class ScrapyBtPipeline(object):
    def __init__(self,host,database,user,password,port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host = crawler.settings.get('MYSQL_HOST'),
            database = crawler.settings.get('MYSQL_DATABASE'),
            user = crawler.settings.get('MYSQL_USER'),
            password = crawler.settings.get('MYSQL_PASSWORD'),
            port = crawler.settings.get('MYSQL_PORT'),
        )
    def open_spider(self,spider):
        self.db = pymysql.connect(self.host,self.user,self.password,self.database,self.port,charset='utf8',)
        self.cursor = self.db.cursor()

    def close_spider(self,spider):
        self.db.close()

    def process_item(self,item,spider):
        data = dict(item)
        # print(type(data))
        keys = ','.join(data.keys())
        values = ','.join(['%s']*len(data))
        # sql = 'insert into %s (%s) values (%s)'%(item.table,keys,values)
        sql = "INSERT INTO {table}({keys}) VALUES ({values})".format(table='ZA_BT_items', keys=keys, values=values)
        self.cursor.execute(sql,tuple(data.values()))
        self.db.commit()
        return item
