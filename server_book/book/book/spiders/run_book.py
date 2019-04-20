import scrapy
from book.items import BookItem
from scrapy.linkextractor import LinkExtractor

import pymysql

import smtplib
from email.mime.text import MIMEText
from email.header import Header
def send_smtp():
    '''

    :return:
    '''
    #设置邮件发送者（查看smtp协议是否启动）
    from_addr = '835240908@qq.com'
    password = 'jqsyftttuofwbcgj'
    # 输入SMTP服务器地址:
    smtp_server = 'smtp.qq.com'
    to_addr = ['wang_junling@yeah.net']
    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText('爬虫即将停止，请尽快启动下一个...', 'plain', 'utf-8')
    message['From'] = Header("wangjunling", 'utf-8')  # 发送者
    message['To'] = Header("shouji", 'utf-8')  # 接收者
    subject = '数据抽取'#标题
    message['Subject'] = Header(subject, 'utf-8')
    try:
        server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], message.as_string())
        server.quit()
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")

num=0

class Blues(scrapy.Spider):
    name='book'

    allowed_domains=['www.lwxslwxs.com']
    start_urls = []
    mysql="""
    select section_url from datas_book limit 0,100000 
    """
    db = pymysql.connect('47.93.37.167', 'root', 'root', 'book',cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    cursor.execute(mysql)

    # for data in run.Get_data(mysql):
    for data in cursor.fetchall():
        start_urls.append(data['section_url'])

    # print(start_urls)

    def parse(self, response):
        global num

        num+=1
        if num>100000 :
            send_smtp()
        item = BookItem()

        item['book_title_url'] =response.url

        # item['book_name']=response.xpath('//ol[@class="breadcrumb"]/li[2]/a/text()').extract_first()extract_first
        # print(item['book_name'])

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

        item['book_title'] = response.xpath('//div[@class="panel-heading"][1]'
                                            '/text()').extract_first()
        item['book_text'] = ','.join(
            response.xpath('//div[@class="panel-body content-body content-ext"]/text()').extract())
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

        if response.status ==200:

            item['book_text2'] = ','.join(
                response.xpath('//div[@class="panel-body content-body content-ext"]/text()').extract())
            next_link = LinkExtractor(restrict_xpaths='//li[@class="next"]/a')
            next_links = next_link.extract_links(response)
            print(next_links[0].url)
            print(response.url.split('-')[0])
            if response.url.split('-')[0] in next_links[0].url:
                yield scrapy.Request(url=next_links[0].url, callback=self.next3, meta={'data': item})
            else:
                yield item
        else:
            yield scrapy.Request(url=response.url, callback=self.next2, meta={'data': item})
    def next3(self,response):
        item = response.meta['data']

        if response.status == 200:
            item['book_text3'] = ','.join(
                response.xpath('//div[@class="panel-body content-body content-ext"]/text()').extract())
            next_link = LinkExtractor(restrict_xpaths='//li[@class="next"]/a')
            next_links = next_link.extract_links(response)
            print(next_links[0].url)
            print(response.url.split('-')[0])
            if response.url.split('-')[0] in next_links[0].url:
                yield scrapy.Request(url=next_links[0].url, callback=self.next4, meta={'data': item})
            else:
                yield item
        else:
            yield scrapy.Request(url=response.url, callback=self.next3, meta={'data': item})

    def next4(self,response):

        item = response.meta['data']
        if response.status == 200:
            item['book_text4'] = ','.join(
                response.xpath('//div[@class="panel-body content-body content-ext"]/text()').extract())
            next_link = LinkExtractor(restrict_xpaths='//li[@class="next"]/a')
            next_links = next_link.extract_links(response)
            print(next_links[0].url)
            print(response.url.split('-')[0])
            if response.url.split('-')[0] in next_links[0].url:
                yield scrapy.Request(url=next_links[0].url, callback=self.next5, meta={'data': item})
            else:
                yield item
        else:
            yield scrapy.Request(url=response.url, callback=self.next4, meta={'data': item})
    def next5(self,response):
        item = response.meta['data']
        if response.status == 200:
            item['book_text5'] = ','.join(
                response.xpath('//div[@class="panel-body content-body content-ext"]/text()').extract())
            next_link = LinkExtractor(restrict_xpaths='//li[@class="next"]/a')
            next_links = next_link.extract_links(response)
            print(next_links[0].url)
            print(response.url.split('-')[0])
            if response.url.split('-')[0] in next_links[0].url:
                yield scrapy.Request(url=next_links[0].url, callback=self.next6, meta={'data': item})
            else:
                yield item
        else:
            yield scrapy.Request(url=response.url, callback=self.next5, meta={'data': item})

    def next6(self,response):
        item = response.meta['data']
        if response.status == 200:

            item['book_text6'] = ','.join(
                response.xpath('//div[@class="panel-body content-body content-ext"]/text()').extract())
            next_link = LinkExtractor(restrict_xpaths='//li[@class="next"]/a')
            next_links = next_link.extract_links(response)
            print(next_links[0].url)
            print(response.url.split('-')[0])
            if response.url.split('-')[0] in next_links[0].url:
                yield scrapy.Request(url=next_links[0].url, callback=self.next7, meta={'data': item})
            else:
                yield item
        else:
            yield scrapy.Request(url=response.url, callback=self.next6, meta={'data': item})

    def next7(self,response):
        item = response.meta['data']
        if response.status == 200:

            item['book_text7'] = ','.join(
                response.xpath('//div[@class="panel-body content-body content-ext"]/text()').extract())
            next_link = LinkExtractor(restrict_xpaths='//li[@class="next"]/a')
            next_links = next_link.extract_links(response)
            print(next_links[0].url)
            print(response.url.split('-')[0])
            if response.url.split('-')[0] in next_links[0].url:
                yield scrapy.Request(url=next_links[0].url, callback=self.next8, meta={'data': item})
            else:
                yield item
        else:
            yield scrapy.Request(url=response.url, callback=self.next7, meta={'data': item})

    def next8(self,response):
        item = response.meta['data']
        if response.status == 200:

            item['book_text8'] = ','.join(
                response.xpath('//div[@class="panel-body content-body content-ext"]/text()').extract())
            next_link = LinkExtractor(restrict_xpaths='//li[@class="next"]/a')
            next_links = next_link.extract_links(response)
            print(next_links[0].url)
            print(response.url.split('-')[0])
            if response.url.split('-')[0] in next_links[0].url:
                yield scrapy.Request(url=next_links[0].url, callback=self.next9, meta={'data': item})
            else:
                yield item
        else:
            yield scrapy.Request(url=response.url, callback=self.next8, meta={'data': item})
    def next9(self,response):
        item = response.meta['data']
        if response.status == 200:

            item['book_text9'] = ','.join(
                response.xpath('//div[@class="panel-body content-body content-ext"]/text()').extract())
            next_link = LinkExtractor(restrict_xpaths='//li[@class="next"]/a')
            next_links = next_link.extract_links(response)
            print(next_links[0].url)
            print(response.url.split('-')[0])
            if response.url.split('-')[0] in next_links[0].url:
                yield scrapy.Request(url=next_links[0].url, callback=self.next10, meta={'data': item})
            else:
                yield item
        else:
            yield scrapy.Request(url=response.url, callback=self.next9, meta={'data': item})

    def next10(self,response):

        item = response.meta['data']
        if response.status == 200:
            item['book_text10'] = ','.join(
                response.xpath('//div[@class="panel-body content-body content-ext"]/text()').extract())
            next_link = LinkExtractor(restrict_xpaths='//li[@class="next"]/a')
            next_links = next_link.extract_links(response)
            print(next_links[0].url)
            print(response.url.split('-')[0])
            yield item
        else:
            yield scrapy.Request(url=response.url, callback=self.next9, meta={'data': item})