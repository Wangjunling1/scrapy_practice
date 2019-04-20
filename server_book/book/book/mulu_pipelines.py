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

        db = pymysql.connect(
            '',
            '',
            '',
            '',
            charset='utf8mb4',
        use_unicode=True,)
        cursor = db.cursor()

        insert_sql = "insert into `book_name_url` values(0,'{0}','{1}','{2}','{3}" \
                     "','{4}','{5}','{6}','{7}',0)".format(
                           item['mu_book_name'], item['mu_jianjie'],
                           item['mu_mulu_url'], item['mu_img_url']
                           , self.md5_key(item['mu_img_url']),
                           item['mu_book_url'],
                           item['mu_book_author'],
                           item['mu_book_type'])
        try:
            if len(item['mu_mulu_url']) > 20:
                cursor.execute(insert_sql)
                db.commit()
                print('ok')
            # import requests
            # response_img = requests.get(img_url)
            # with open("imsget//{}.jpg".format(md5_key(img_url)), 'wb')as img_wb:
            #     img_wb.write(response_img.content)
            else:
                print('没有获取到目录')

        except BaseException as a:
            print(a)
            db.rollback()


        return item
