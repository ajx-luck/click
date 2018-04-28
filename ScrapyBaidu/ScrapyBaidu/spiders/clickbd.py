# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider
from scrapy import Request

from ScrapyBaidu.items import baiduItemtj
import os
from scrapy.conf import settings
from urllib import parse
import linecache
import random



class ClickbdSpider(scrapy.Spider):
    name = "clickbd"
    allowed_domains = ['m.baidu.com']
    def start_requests(self):
        for i in range(1,40005):
            a = random.randrange(1, 40005) #1-9中生成随机数
            theline = linecache.getline('D:\\bd\\456.txt', a)
            # mucifile = open("D:\\bd\\234.csv", "r", encoding="utf_16")
            # for line in mucifile.readlines():
            rows = theline.split('\t')
            keyword = rows[2];
            if keyword != "":
                for i in range(0,50,10):
                    yield Request('https://m.baidu.com/s?word=' + parse.quote(keyword)+'&pn='+str(i), self.parse)

    def parse(self, response):
        if(response.text is not None):
            word = response.url.split('word=')[1]
            divList=response.xpath('//div[@class="ec_urlline"]')
            # with open('E:/url/' + parse.unquote(word) + '.html','w',encoding='utf-8') as f:
            #     f.close()
            for li in divList:
                name= li.css('a::attr(href)').extract()

                for url in name:
                        # with open('E:/url/' + parse.unquote(word) + '.html','a+',encoding='utf-8') as f:
                        #     f.write(url+"\n")
                        #     f.close()
                    yield Request(url,self.parse)

        # related = response.css('#reword .rw-list a::text').extract()
        # if related:
        #     for rw in related:
        #         item = baiduItemtj()
        #         item['keyword'],item['description'] = [rw,'']
        #         yield item
        # rwlink = response.css('#reword .rw-list a::attr(href)').extract()
        # if rwlink:
        #     for link in rwlink:
        #         yield Request(link,self.parse)
        # tj = response.css('.wa-sigma-celebrity-rela-entity.c-scroll-element-gap a')
        # if tj:
        #     for i in tj:
        #         item = baiduItemtj()
        #         item['keyword'],item['description'] = i.css('p::text').extract()
        #         yield item
        #     tjlink = response.css('.wa-sigma-celebrity-rela-entity.c-scroll-element-gap a::attr(href)').extract()
        #     if tjlink:
        #         for link in tjlink:
        #             yield Request(link,self.parse)
        #

