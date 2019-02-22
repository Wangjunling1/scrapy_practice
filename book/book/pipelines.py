# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql,json
class BookPipeline(object):
    def process_item(self, item, spider):
        db=pymysql.connect('127.0.0.1','root','root','book')
        cursor=db.cursor()
        creata_sql="create table if not exists {}(id int primary key auto_increment,book_title text,book_text text)".format(item['book_name'])
        cursor.execute(creata_sql)
        book_name=item['book_name']

        book_title=(item['book_title']).lstrip().replace("'",'"')

        book_text=','.join((','.join((item['book_text']).split())).split("', '"))

        #
        with open('{}.txt'.format(book_name),'a+',encoding='utf-8') as f:
            f.write(book_text.replace(",,,",""))
        insert_sql="insert into {} values(0,'{}','{}')".format(book_name,book_title,book_text.replace(",,,",""))
        try:
            cursor.execute(insert_sql)
            db.commit()
        except BaseException as a:
            print(a)
            db.rollback()


        return item
