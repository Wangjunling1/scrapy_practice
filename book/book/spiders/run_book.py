import scrapy,os
from book.items import BookItem

class Blues(scrapy.Spider):
    name='book'

    allowed_domains=['www.lwxslwxs.com']
    start_urls=['https://www.lwxslwxs.com/51/51339/']
    def parse(self, response):
        item = BookItem()
        item['book_name']=response.xpath('//div[@class="info2"]/h1[@class=" text-center"]/text()').extract_first()
        datas=response.xpath('//div[@class="row"][3]/div[@class="col-sm-12 col-md-12"]/div[@class="panel panel-default"]/div[@class="panel-body"]/ul/li')
        item['book_text']=''
        print(item['book_name'])
        for data in datas:
            item["data_url"]=data.xpath('a/@href').extract_first()
            yield scrapy.Request(url='https://www.lwxslwxs.com'+item["data_url"],callback=self.content,meta={'data':item})

    def content(self,response):
        item = response.meta['data']
        item['book_title'] = response.xpath('//div[@class="panel-heading"][1]/text()').extract_first()
        text=','.join(response.xpath('//div[@class="panel-body content-body content-ext"]/text()').extract())
        item['book_text']=item['book_text']+text
        net=response.xpath('//li[@class="next"]/a[@class="btn btn-info"]/@href').extract_first()
        if len(net)>8:
            if net[:-7] in str(response):
                print(net)
                print('下一页')
                yield scrapy.Request(url='https://www.lwxslwxs.com'+net,callback=self.content,meta={'data':item})
            else:
                yield item
                print('True,存入',item['book_title'])
        else:
            yield item





