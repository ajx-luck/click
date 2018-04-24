# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class baiduItemtj(scrapy.Item):
    # 右侧推荐有description 底部相关搜索没有 为空
    keyword = scrapy.Field()
    description = scrapy.Field()
