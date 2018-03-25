from scrapy import Request
from scrapy.spiders import Spider
from scrapy_private.items import NationalStandardItem
from lxml import etree
import re
class NationalStandard(Spider):
    name = 'nationStandard'
    start_urls = {
        'http://www.gb688.cn/bzgk/gb/std_list_type?pageSize=50&p.p6=01',
    }
    custom_settings = {
        'ITEM_PIPELINES':{},
        'DOWNLOAD_DELAY' :'1',
    }
    basePath = './spider_data/shenlunfanwen/'

    def parse(self, response):
        #print('response:',response)
        standards_list = response.xpath('//table[@class="table result_list table-striped table-hover"]/tbody[2]//tr')
        #print('standards_list:',standards_list)
        for i, standard in enumerate(standards_list):
            standardNum = standard.xpath('.//td[2]/a/text()').extract()[0]
            #print('standardNum:',standardNum)

            standardCai = standard.xpath('.//td[3]').extract()[0]
            if(standardCai.find('采')>=0):
                standardCai = standard.xpath('.//td[3]/span/text()').extract()[0]
                #print(standardCai)
                continue

            standardID = standard.xpath('.//td[2]/a/@onclick').extract()[0]
            standardID = re.findall(r'showInfo\(\'(.*)\'\)', standardID)[0]
            #print('standardID:',standardID)

            standardTitle = standard.xpath('.//td[4]/a/text()').extract()[0]
            #print('standardTitle:',standardTitle)

            standardUrl = 'http://www.gb688.cn/bzgk/gb/newGbInfo?hcno='+standardID
            #print('standardUrl:',standardUrl)

            yield Request(standardUrl,callback=self.parse_download)

    def parse_download(self, response):
        #print(response.body)
        res = etree.HTML(response.body.decode('utf8'))
        print(res)
        item = NationalStandardItem()
        print('response.url::',response.url)

        item['StandardNum'] = res.xpath('//div[@class="bor2"]/table[1]//h1/text()')[0]
        item['StandardNum'] = re.findall(r'标准号：(.*)', item['StandardNum'])[0]
        print('StandardNum::', item['StandardNum'])

        item['StandardTitle'] = res.xpath('//div[@class="bor2"]/table[2]//b/text()')[0]
        print('StandardTitle::', item['StandardTitle'])
        
        item['StandardCategory'] = res.xpath('/html/body/div[2]/div/div/div/div/div[2]/div[2]/text()')[0]
        item['StandardCategory'] = ''.join(re.findall(r'(\w*)', item['StandardCategory']))
        print('StandardCategory::', item['StandardCategory'])
        
        item['StandardID'] = response.url
        item['StandardID'] = re.findall(r'\.*hcno=(.*)', item['StandardID'])[0]
        print('StandardID::', item['StandardID'])

        item['StandardUrl'] = 'http://c.gb688.cn/bzgk/gb/viewGb?hcno='+item['StandardID']

