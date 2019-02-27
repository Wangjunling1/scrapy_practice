import scrapy,os
from book.items import BookItem
from scrapy.linkextractor import LinkExtractor

class Blues(scrapy.Spider):
    name='book'

    allowed_domains=['www.lwxslwxs.com']

    with open(r'D:\python项目\爬虫\one\book\book\spiders\mulu_url.txt','r',encoding='utf-8') as f:
        f=f.read()
    start_urls = []
    for url in f.split('::::::'):
        start_urls.append(str(url))
    def parse(self, response):
        item = BookItem()

        item['book_text']=''
        item['book_text2']=''
        item['book_text3']=''
        item['book_text4']=''
        item['book_text5']=''
        item['book_text6']=''
        item['book_text7']=''
        item['book_text8']=''
        item['book_text9']=''
        item['book_text10']=''

        item['book_title'] = response.xpath('//div[@class="panel-heading"][1]/text()').extract_first()
        item['book_text'] = ','.join(response.xpath('//div[@class="panel-body content-body content-ext"]/text()').extract())
        next_link = LinkExtractor(restrict_xpaths='//li[@class="next"]/a')
        next_links = next_link.extract_links(response)
        print(next_links[0].url)
        print(response.url.split('.html')[0])
        if response.url.split('.html')[0] in next_links[0].url:
            yield scrapy.Request(url=next_links[0].url,callback=self.next2,meta={'data':item})
        else:
            yield item


    def next2(self,response):


        item = response.meta['data']

        item['book_text2'] = ','.join(response.xpath('//div[@class="panel-body content-body content-ext"]/text()').extract())
        next_link = LinkExtractor(restrict_xpaths='//li[@class="next"]/a')
        next_links = next_link.extract_links(response)
        print(next_links[0].url)
        print(response.url.split('-')[0])
        if response.url.split('-')[0] in next_links[0].url:
            yield scrapy.Request(url=next_links[0].url, callback=self.next3, meta={'data': item})
        else:
            yield item

    def next3(self,response):
        item = response.meta['data']
        item['book_text3'] = ','.join(response.xpath('//div[@class="panel-body content-body content-ext"]/text()').extract())
        next_link = LinkExtractor(restrict_xpaths='//li[@class="next"]/a')
        next_links = next_link.extract_links(response)
        print(next_links[0].url)
        print(response.url.split('-')[0])
        if response.url.split('-')[0] in next_links[0].url:
            yield scrapy.Request(url=next_links[0].url, callback=self.next4, meta={'data': item})
        else:
            yield item

    def next4(self,response):
        item = response.meta['data']
        item['book_text4'] = ','.join(response.xpath('//div[@class="panel-body content-body content-ext"]/text()').extract())
        next_link = LinkExtractor(restrict_xpaths='//li[@class="next"]/a')
        next_links = next_link.extract_links(response)
        print(next_links[0].url)
        print(response.url.split('-')[0])
        if response.url.split('-')[0] in next_links[0].url:
            yield scrapy.Request(url=next_links[0].url, callback=self.next5, meta={'data': item})
        else:
            yield item

    def next5(self,response):
        item = response.meta['data']
        item['book_text5'] = ','.join(response.xpath('//div[@class="panel-body content-body content-ext"]/text()').extract())
        next_link = LinkExtractor(restrict_xpaths='//li[@class="next"]/a')
        next_links = next_link.extract_links(response)
        print(next_links[0].url)
        print(response.url.split('-')[0])
        if response.url.split('-')[0] in next_links[0].url:
            yield scrapy.Request(url=next_links[0].url, callback=self.next6, meta={'data': item})
        else:
            yield item

    def next6(self,response):
        item = response.meta['data']
        item['book_text6'] = ','.join(response.xpath('//div[@class="panel-body content-body content-ext"]/text()').extract())
        next_link = LinkExtractor(restrict_xpaths='//li[@class="next"]/a')
        next_links = next_link.extract_links(response)
        print(next_links[0].url)
        print(response.url.split('-')[0])
        if response.url.split('-')[0] in next_links[0].url:
            yield scrapy.Request(url=next_links[0].url, callback=self.next7, meta={'data': item})
        else:
            yield item

    def next7(self,response):
        item = response.meta['data']
        item['book_text7'] = ','.join(response.xpath('//div[@class="panel-body content-body content-ext"]/text()').extract())
        next_link = LinkExtractor(restrict_xpaths='//li[@class="next"]/a')
        next_links = next_link.extract_links(response)
        print(next_links[0].url)
        print(response.url.split('-')[0])
        if response.url.split('-')[0] in next_links[0].url:
            yield scrapy.Request(url=next_links[0].url, callback=self.next8, meta={'data': item})
        else:
            yield item

    def next8(self,response):
        item = response.meta['data']
        item['book_text8'] = ','.join(response.xpath('//div[@class="panel-body content-body content-ext"]/text()').extract())
        next_link = LinkExtractor(restrict_xpaths='//li[@class="next"]/a')
        next_links = next_link.extract_links(response)
        print(next_links[0].url)
        print(response.url.split('-')[0])
        if response.url.split('-')[0] in next_links[0].url:
            yield scrapy.Request(url=next_links[0].url, callback=self.next9, meta={'data': item})
        else:
            yield item

    def next9(self,response):
        item = response.meta['data']
        item['book_text9'] = ','.join(response.xpath('//div[@class="panel-body content-body content-ext"]/text()').extract())
        next_link = LinkExtractor(restrict_xpaths='//li[@class="next"]/a')
        next_links = next_link.extract_links(response)
        print(next_links[0].url)
        print(response.url.split('-')[0])
        if response.url.split('-')[0] in next_links[0].url:
            yield scrapy.Request(url=next_links[0].url, callback=self.next10, meta={'data': item})
        else:
            yield item

    def next10(self,response):
        item = response.meta['data']
        item['book_text10'] = ','.join(response.xpath('//div[@class="panel-body content-body content-ext"]/text()').extract())
        next_link = LinkExtractor(restrict_xpaths='//li[@class="next"]/a')
        next_links = next_link.extract_links(response)
        print(next_links[0].url)
        print(response.url.split('-')[0])
        yield item