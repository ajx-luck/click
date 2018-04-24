# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.contrib.downloadermiddleware.httpproxy import HttpProxyMiddleware
import random

class IPPOOlS(HttpProxyMiddleware):

    # 初始化
    def __init__(self, ip=''):
        self.ip = ip
        self.IPPool = []
        with open("D:\\proxy\\ip_proxy.txt", "r", encoding="utf_8") as file:
            for line in file:
                self.IPPool.append(line)


    # 请求处理
    def process_request(self, request, spider):
        thisproxy = eval(random.choice(self.IPPool))
        for key in thisproxy:
            proxy = key+'://'+thisproxy[key]
            # 先随机选择一个IP
            print("当前使用proxy是："+ proxy)
            request.meta["proxy"] = proxy

