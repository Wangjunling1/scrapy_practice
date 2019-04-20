# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql,hashlib
# from mysql_comment import Mysql_connect

class BookPipeline(object):

    def md5_key(self, arg):
        hash = hashlib.md5()
        hash.update(arg.encode("utf-8"))
        return hash.hexdigest()

    def process_item(self, item, spider):
        # run=Mysql_connect()
        db=pymysql.connect(
            '47.93.37.167',
            ''
            ,''
            ,'book')
        cursor=db.cursor()
        book_title=(item['book_title']).lstrip().replace("'",'"')

        book_text=','.join((','.join((item['book_text']).split())).split("', '"))
        for i in range(2,10):
            if len(item['book_text{}'.format(i+1)]) >3:
                if  ','.join((','.join((item['book_text{}'.format(i)]).split())).split("', '")) !=\
                        ','.join((','.join((item['book_text{}'.format(i+1)]).split())).split("', '")):


                    book_text=book_text+','.join(
                        (','.join((item['book_text{}'.format(i+1)]).split())).split("', '"))

        # book_text=book_text.replace(",,,","")
        # with open('{}.txt'.format(book_name),'a+',encoding='utf-8') as f:
        #     f.write(book_text+'\n')
        insert_sql="update `datas_book2` set `section_name`='{}',section_text=" \
                   "'{}' where srction_md5='{}'".format(book_title
                    ,book_text.replace(",,,","").replace(',,',',')
                    .replace('    一秒记住域名:"lwxslwxs.com"乐*文书屋','')
                    .replace('乐文书屋','').replace('lwxslwxs.com','')
                    ,self.md5_key(item['book_title_url']))
        try:
            cursor.execute(insert_sql)
            db.commit()
        except BaseException as a:
            print(a)
            db.rollback()


        return item
