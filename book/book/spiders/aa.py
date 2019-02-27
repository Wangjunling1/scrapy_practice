import scrapy
from scrapy.linkextractor import LinkExtractor

class WeidsSpider(scrapy.Spider):
    name = "mulu_url"
    allowed_domains = ["www.lwxslwxs.com"]
    start_urls = ['https://www.lwxslwxs.com/51/51339/']

    def parse(self, response):
        link = LinkExtractor(restrict_xpaths='//div[@class="row"][3]/div[@class="col-sm-12 col-md-12"]/div[@class="panel panel-default"]/div[@class="panel-body"]/ul[@class="list-group list-charts"]/li/a')
        links = link.extract_links(response)
        print(link)
        print(response.status)
        book_name= response.xpath('//div[@class="info2"]/h1[@class=" text-center"]/text()').extract_first()
        # for i in links:
        #     print(i.url)
        #     with open('{}_url.txt'.format(book_name),'a+',encoding='utf-8') as f:
        #         f.write(i.url+'::::::')


        img=response.xpath('//div[@class="info1"]/img/@src').extract_first()

        img_url='www.lwxslwxs.com'+img
        import requests
        response_img=requests.get(img_url)
        with open("images/{}.jpg".format(book_name),'wb')as img_wb:
            img_wb.write(response_img.content)
