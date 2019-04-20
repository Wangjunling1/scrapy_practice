# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_name=scrapy.Field()
    book_title=scrapy.Field()

    book_title_url=scrapy.Field()
    data_url=scrapy.Field()

    book_text=scrapy.Field()
    book_text2=scrapy.Field()
    book_text3=scrapy.Field()
    book_text4=scrapy.Field()
    book_text5=scrapy.Field()
    book_text6=scrapy.Field()
    book_text7=scrapy.Field()
    book_text8=scrapy.Field()
    book_text9=scrapy.Field()
    book_text10=scrapy.Field()

    book_text_next=scrapy.Field()

    """目录连接获取"""
    mu_book_name=scrapy.Field()
    mu_book_author=scrapy.Field()
    mu_jianjie=scrapy.Field()
    mu_mulu_url=scrapy.Field()
    mu_img_url=scrapy.Field()
    mu_book_type=scrapy.Field()
    mu_book_url=scrapy.Field()



    pass
