# -*- coding: utf-8 -*-
import scrapy
from tqdm import tqdm
from pymongo import MongoClient
from bianju.items import PlayItem
from bianju.settings import COOKIE


class ContentSpider(scrapy.Spider):
    name = 'content'

    def __init__(self, category=None):
        self.play_type = category
        self.cookie = COOKIE
        client = MongoClient()
        database = 'bianju'
        collection = 'basicInfo_' + category
        db = client[database][collection]
        ret = list(db.find({}, {'_id': 0, 'id': 1}))
        ret.reverse()
        client_content = MongoClient()
        db_content = client_content[database]['content_' + category]
        self.ret_content = list(db_content.find({}, {'_id': 0, 'id': 1, 'page': 1}))
        self.start_urls = []
        for i in ret:
            self.start_urls.append('https://www.1bianju.com/Art_list.asp?id={}&CType=content'.format(i['id']))
        self.total = len(self.start_urls)

    def start_requests(self):
        for url in tqdm(self.start_urls):
            yield scrapy.Request(url, self.parse, cookies=self.cookie)

    def parse(self, response):
        pages = response.xpath('//td[@background="images/bg_art.gif"]//div[@align="center"]/a[last()]/text()').get()
        if pages:
            pages = int(pages)
        else:
            pages = 1
        
        if pages > 25:
            print('tolong')
            return
        for page in range(1, pages+1):  
            id = response.url.split('?id=')[1].split('&')[0]
            print(id, page, 'start')
            if {'id': id, 'page': page} in self.ret_content:
                print(id, page, 'end')
                continue
            url = 'https://www.1bianju.com/Art_list.asp?id={}&page={}&CType=content'.format(id, page)
            
            yield scrapy.Request(url, self.parse_core, cookies=self.cookie, meta={'id': id, 'page': page})

    def parse_core(self, response):
        id = response.meta['id']
        page = response.meta['page']
        content = response.xpath('//td[@background="images/bg_art.gif"]/text()').getall()
        content = [c.strip() for c in content]
        content = [c for c in content if c != '' and c != '【' and c != '】']
        if '【本作品已在' in content:
            content = content[3:]
        item = PlayItem(id=id, page=int(page), content=content)
        print(id, page, 'end')
        yield item