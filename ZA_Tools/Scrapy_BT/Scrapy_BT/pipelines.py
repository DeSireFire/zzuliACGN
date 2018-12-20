# -*- coding: utf-8 -*-
import codecs,json
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapyBtPipeline(object):
    def process_item(self, item, spider):
        return item

class dmhyPipeline(object):
    # def __init__(self):
    #     self.file = codecs.open('data_cn.json', 'wb', encoding='utf-8')
    #
    # def process_item(self, item, spider):
    #     line = json.dumps(dict(item)) + '\n'
    #     self.file.write(line.decode("unicode_escape"))
    #     return item

    # 如果爬虫名是movie
    # if spider.name == 'movie':
    #     try:
    #         self.cursor.execute("insert into Movie (name,movieInfo,star,number,quote) \
    #         VALUES (%s,%s,%s,%s,%s)", (item['movie_name'], item['movie_message'], item['movie_star'],
    #                                    item['number'], item['movie_quote']))
    #         self.conn.commit()
    #     except pymysql.Error:
    #         print("Error%s,%s,%s,%s,%s" % (item['movie_name'], item['movie_message'], item['movie_star'],
    #                                        item['number'], item['movie_quote']))
    #     return item
    # # 如果爬虫名是book
    # elif spider.name == 'book':
    #     try:
    #         self.cursor.execute("insert into Book (book_name,author,book_type,book_state,book_update,book_time,new_href,book_intro) \
    #                 VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", (item['book_name'], item['author'], item['book_type'],
    #                                                     item['book_state'], item['book_update'], item['book_time'],
    #                                                     item['new_href'], item['book_intro']))
    #         self.conn.commit()
    #     except pymysql.Error:
    #         print("Error%s,%s,%s,%s,%s,%s,%s,%s" % (item['book_name'], item['author'], item['book_type'],
    #                                                 item['book_state'], item['book_update'], item['book_time'],
    #                                                 item['new_href'], item['book_intro']))
    #     return item
    pass