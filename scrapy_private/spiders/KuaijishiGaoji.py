from scrapy import Request
from scrapy.spiders import Spider
from lxml import etree
import re

class GaojiKuaijishi(Spider):
    name = 'gjkjs'
    start_urls = {
        'http://www.wangxiao.cn/gaoji/57321018829.html',
    }
    custom_settings = {
        'ITEM_PIPELINES':{},
        'DOWNLOAD_DELAY' :'0',
    }
    '''
    headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding":"gzip, deflate, sdch",
        "Accept-Language":"zh-CN,zh;q=0.8",
        "Cache-Control":"max-age=0",
        "Connection":"keep-alive",
        "Cookie":"agentmembers=wx; gr_user_id=c00bdbdc-7de5-4f4e-867e-27814ce99baf; gr_session_id_882ce7449fa11cc8=d893dc20-5852-4c2b-87d2-52a63e1e1357; Hm_lvt_fd91d2ffbfa83c234c1cee672a69326c=1522065499; Hm_lpvt_fd91d2ffbfa83c234c1cee672a69326c=1522065853",
        "Host":"www.exam8.com",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
    }
    '''
    def parse(self, response):
        print('response:::',response.body)
        title = response.xpath('//div[@class="newsMain"]/h1/text()').extract()[0]
        print('title:::',title)