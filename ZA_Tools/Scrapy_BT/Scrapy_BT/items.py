# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyBtItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class QuoteItem(scrapy.Item):
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()

class dmhyItem(scrapy.Item):
    rdName = scrapy.Field()#资源名称
    rdUpTime = scrapy.Field()#资源发布时间
    rdSize = scrapy.Field()#资源大小
    rdUpNum = scrapy.Field()#资源上传数
    rdDownloadNum = scrapy.Field()#资源下载数
    rdInfo = scrapy.Field()#资源介绍
    rdOK = scrapy.Field()#资源完成数
    rdMagnet = scrapy.Field()#资源下载链接
    rdMagnet2 = scrapy.Field()#资源下载链接
    rdTracker = scrapy.Field()#资源下tracker服务器
    rdType =scrapy.Field()#资源种类
    rdView = scrapy.Field()#资源详细页地址