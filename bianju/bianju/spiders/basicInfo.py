# -*- coding: utf-8 -*-
import scrapy
from tqdm import tqdm
from bianju.items import PlayItem


class BasicinfoSpider(scrapy.Spider):
    name = 'basicInfo'

    def __init__(self, category=None):
        self.play_type = category
        if self.play_type == 'recommend':
            self.start_urls = 'https://www.1bianju.com/Display_Best.asp'
        else:
            self.start_urls = 'https://www.1bianju.com/{}/'.format(self.play_type)

    def start_requests(self):
        yield scrapy.Request(self.start_urls, self.parse_catalog)

    def parse_catalog(self, response):
        catalog_pages = int(response.xpath('//span[@style="font-size:9pt"]/font[3]/text()').get())
        for page in tqdm(range(1, catalog_pages+1)):
            if self.play_type == 'recommend':
                url = 'https://www.1bianju.com/Display_Best.asp?Page={}'.format(page)
            else:
                url = 'https://www.1bianju.com/{}/?Page={}'.format(self.play_type, page)
            
            yield scrapy.Request(url, self.parse_catalog_core)
    
    def parse_catalog_core(self, response):
        td = response.xpath('//td[@align="center" and @valign="top"]')
        trs = td.xpath('.//tr')[2::2][:-1]
        if self.play_type == 'free' or self.play_type == 'recommend':
            for tr in trs:
                id = tr.xpath('./td[@width="277"]/a/@href').get().split('=')[1].strip()
                title = tr.xpath('./td[@width="277"]/a/@title').get().strip()
                writer = tr.xpath('./td[@width="103"]/a/text()').get().strip()
                submit_data = tr.xpath('./td[@width="68"]/font/text()').get().strip()
                read_count = tr.xpath('./td[@width="45"][1]/text()').get().strip()
                review_count = tr.xpath('./td[@width="45"][2]/text()').get().strip()
                if review_count == "":
                    review_count = tr.xpath('./td[@width="45"][2]/a/text()').get().strip()
                item = PlayItem(id=id, title=title, writer=writer, submit_data=submit_data, read_count=int(read_count), review_count=int(review_count))       
                yield item
        elif self.play_type == 'famous':
            for tr in trs:
                id = tr.xpath('./td[@height="28"][1]/a/@href').get().split('=')[1].strip()
                title = tr.xpath('./td[@height="28"][1]/a/@title').get().strip()
                writer = tr.xpath('./td[@height="28"][2]/font/text()').get().strip()
                submit_data = tr.xpath('./td[@width="80"]/text()').get().strip()
                read_count = tr.xpath('./td[@width="64"]/text()').get().strip()
                review_count = tr.xpath('./td[@width="35"]/text()').get().strip()
                if review_count == "":
                    review_count = tr.xpath('./td[@width="35"]/text()').get().strip()
                douban_score = tr.xpath('./td[@width="62"]/font/text()').get().strip()
                if douban_score != '-':
                    douban_score = float(douban_score)
                item = PlayItem(id=id, title=title, writer=writer, submit_data=submit_data, read_count=int(read_count), review_count=int(review_count), douban_score=douban_score)       
                yield item
        else:
            for tr in trs:
                id = tr.xpath('./td[@height="28"]/a/@href').get().split('=')[1].strip()
                title = tr.xpath('./td[@height="28"]/a/@title').get().strip()
                writer = tr.xpath('./td[@width="112"]/a/text()').get().strip()
                submit_data = tr.xpath('./td[@width="103"]/font/text()').get().strip()
                read_count = tr.xpath('./td[@width="62"]/text()').get().strip()
                review_count = tr.xpath('./td[@width="68"]/text()').get().strip()
                if review_count == "":
                    review_count = tr.xpath('./td[@width="68"]/a/text()').get().strip()
                item = PlayItem(id=id, title=title, writer=writer, submit_data=submit_data, read_count=int(read_count), review_count=int(review_count))
                yield item