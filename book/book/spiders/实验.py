import scrapy
from scrapy.linkextractor import LinkExtractor

class WeidsSpider(scrapy.Spider):
    name = "weids"
    allowed_domains = ["www.wln100.com"]
    start_urls = ['https://www.wln100.com/Doc/Doc/show/grade/0/area/0/tid/0/times/0/year/0/sid/12']

    def parse(self, response):
        link = LinkExtractor(restrict_xpaths='//td[@class="sjtit"]/a')
        links = link.extract_links(response)
        print(link)
        print(response)
        for i in links:
            print(i.url)