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
    book_text=scrapy.Field()
    book_title_url=scrapy.Field()
    data_url=scrapy.Field()


    pass