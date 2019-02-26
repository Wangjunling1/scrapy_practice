import scrapy
from scrapy.linkextractor import LinkExtractor

class WeidsSpider(scrapy.Spider):
    name = "weids"
    allowed_domains = ["www.lwxslwxs.com"]
    start_urls = ['https://www.lwxslwxs.com/51/51339/']

    def parse(self, response):
        link = LinkExtractor(restrict_xpaths='//div[@class="row"][3]/div[@class="col-sm-12 col-md-12"]/div[@class="panel panel-default"]/div[@class="panel-body"]/ul[@class="list-group list-charts"]/li/a')
        links = link.extract_links(response)
        print(link)
        print(response)
        for i in links:
            print(i.url)