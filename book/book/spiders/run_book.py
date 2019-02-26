import scrapy,os
from book.items import BookItem

class Blues(scrapy.Spider):
    name='book'

    allowed_domains=['www.lwxslwxs.com']
    start_urls=['https://www.lwxslwxs.com/51/51339/']
    def parse(self, response):
        item = BookItem()
        item["book_text_next"] = ''

        item['book_name']=response.xpath('//div[@class="info2"]/h1[@class=" text-center"]/text()').extract_first()
        datas=response.xpath('//div[@class="row"][3]/div[@class="col-sm-12 col-md-12"]/div[@class="panel panel-default"]/div[@class="panel-body"]/ul/li')
        print(item['book_name'])
        for data in datas:
            item["data_url"]=data.xpath('a/@href').extract_first()
            yield scrapy.Request(url='https://www.lwxslwxs.com'+item["data_url"],callback=self.content,meta={'data':item})

    def content(self,response):
        print(response)
        item = response.meta['data']
        item['book_title'] = response.xpath('//div[@class="panel-heading"][1]/text()').extract_first()
        item['book_text'] = ','.join(response.xpath('//div[@class="panel-body content-body content-ext"]/text()').extract())
        for i in range(2,7):
            page=os.path.split(response.url)[-1][:-5]+'-{}.html'.format(i)
            url=os.path.split(response.url)[0]+'/'+page
            yield scrapy.Request(url=url,callback=self.next,meta={'data':item})


    def next(self,response):
        print(response)
        item = response.meta['data']
        text = ','.join(response.xpath('//div[@class="panel-body content-body content-ext"]/text()').extract())
        item["book_text{}".format(response.url.split('-')[-1][0])]=text
        # print(item["book_text{}".format(response.url.split('-')[-1][0])])
        if len(item["book_text6"])>6 and len(item["book_text2"])>6 and len(item["book_text3"])>6 and len(item["book_text4"])>6 and len(item["book_text5"])>6:
            print('插入')
            yield item










