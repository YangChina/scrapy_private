from scrapy.spiders import Spider

class NationalStandard(Spider):
    name = 'nationStandard'
    start_urls = {
        'http://www.gb688.cn/bzgk/gb/std_list_type?pageSize=50&p.p6=01',
    }
    custom_settings = {
        'ITEM_PIPELINES':{},
        'DOWNLOAD_DELAY' :'2',
    }
    basePath = './spider_data/shenlunfanwen/'

    def parse(self, response):
        print('response:',response)
        standards_list = response.xpath('//table[@class="table result_list table-striped table-hover"]/tbody[2]//tr')
        #print('standards_list:',standards_list)
        for i, standard in enumerate(standards_list):
            standardNum = standard.xpath('.//td[2]/a/text()').extract()[0]
            print(standardNum)
            standardCai = standard.xpath('.//td[3]').extract()[0]
            if(standardCai.find('采')>=0):
                standardCai = standard.xpath('.//td[3]/span/text()').extract()[0]
                print(standardCai)
                continue
            standardTitle = standard.xpath('.//td[4]/a/text()').extract()[0]
            print(standardTitle)