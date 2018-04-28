# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.contrib.downloadermiddleware.httpproxy import HttpProxyMiddleware
import random
# 导入settings文件中的UPPOOL
from .settings import UPPOOL
# 导入官方文档对应的HttpProxyMiddleware
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware

class IPPOOlS(HttpProxyMiddleware):

    # 初始化
    def __init__(self, ip=''):
        self.ip = ip
        self.IPPool = []
        with open("D:\\proxy\\ip_proxy_enable.txt", "r", encoding="utf_8") as file:
            for line in file:
                self.IPPool.append(line)


    # 请求处理
    def process_request(self, request, spider):
        thisua = random.choice(UPPOOL)
        # print("当前使用User-Agent是："+thisua)
        request.headers.setdefault('User-Agent',thisua)
        # thisproxy = eval(random.choice(self.IPPool))
        # for key in thisproxy:
        #     proxy = key+'://'+thisproxy[key]
        #     # 先随机选择一个IP
        #     print("当前使用proxy是："+ proxy)
        #     request.meta["proxy"] = proxy

class Uamid(UserAgentMiddleware):
    # 初始化 注意一定要user_agent，不然容易报错
    def __init__(self, user_agent=''):
        self.user_agent = user_agent

        # 请求处理
        def process_request(self, request, spider):
            # 先随机选择一个用户代理
            thisua = random.choice(UPPOOL)
            print("当前使用User-Agent是："+thisua)
            request.headers.setdefault('User-Agent',thisua)

