#-*-conding:utf-8 -*-
import scrapy,pymysql,hashlib
from scrapy.linkextractor import LinkExtractor

from book.items import BookItem
def md5_key(arg):
    hash = hashlib.md5()
    hash.update(arg.encode("utf-8"))
    return hash.hexdigest()

class WeidsSpider(scrapy.Spider):
    name = "mulu_url"
    allowed_domains = ["www.lwxslwxs.com"]
    start_urls=[]
    for i in range(1,1662):
        start_urls.append('https://www.lwxslwxs.com/list/1-{}.html'.format(i))

    def parse(self, response):
        if response.status==200:
            link=LinkExtractor(
                restrict_xpaths='//div[@class="col-lg-6 col-sm-6  col-md-6 col-sm-index"]'
                                '/div[@class="media"]/div[@class="media-body"]'
                                '/h4[@class="media-heading book-title"]/a')
            links = link.extract_links(response)
            # print(links)
            for link_url in links:
                yield scrapy.Request(url=link_url.url,callback=self.mul_url)
        else:
            yield scrapy.Request(url=response.url, callback=self.parse)


    def mul_url(self,response):
        item = BookItem()

        if response.status==200:
            link = LinkExtractor(restrict_xpaths='//div[@class="row"][3]'
                                                 '/div[@class="col-sm-12 col-md-12"]'
                                                 '/div[@class="panel panel-default"]'
                                                 '/div[@class="panel-body"]'
                                                 '/ul[@class="list-group list-charts"]'
                                                 '/li/a')
            links = link.extract_links(response)

            item['mu_book_name']= response.xpath('//div[@class="info2"]'
                                      '/h1[@class=" text-center"]/text()').extract_first()
            item['mu_book_author']=response.xpath('//div[@class="info2"]'
                                       '/h3[@class="text-center"]/a/text()').extract_first()

            item['mu_jianjie']=response.xpath('//div[@class="info2"]'
                                   '/div/p/text()').extract_first()

            item['mu_book_url']=response.url

            item['mu_mulu_url']=''
            for i in links:
                item['mu_mulu_url']+=str(i.url+':::')
            
            try:
                img=response.xpath('//div[@class="info1"]/img/@src').extract_first()
                item['mu_img_url']='http://www.lwxslwxs.com'+img
            except Exception as a :
                print(a) 
            '''
            类型
            ''' 
            item['mu_book_type']='玄幻'
            yield item

        else:
            yield scrapy.Request(url=response.url, callback=self.mul_url)
