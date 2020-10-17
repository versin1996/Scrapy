# -*- coding: utf-8 -*-
import scrapy
from tqdm import tqdm
from pymongo import MongoClient
from bianju.items import PlayItem
from bianju.settings import COOKIE


class BriefSpider(scrapy.Spider):
    name = 'brief'

    def __init__(self, category=None):
        self.play_type = category
        self.cookie = COOKIE
        client = MongoClient()
        database = 'bianju'
        collection = 'basicInfo_' + category
        db = client[database][collection]
        ret = db.find({}, {'_id': 0, 'id': 1})
        self.start_urls = []
        for i in ret:
            self.start_urls.append('https://www.1bianju.com/Art_list.asp?id={}&CType=brief'.format(i['id']))

    def start_requests(self):
        for url in tqdm(self.start_urls):
            yield scrapy.Request(url, self.parse, cookies=self.cookie)

    def parse(self, response):
        id = response.url.split('?id=')[1].split('&')[0]

        subclass, word_count = [i.strip() for i in response.xpath('//td[@bgcolor="#F0FAEF"]/font/text()').getall()][:2]

        simple_brief = response.xpath('//b[contains(text(),"简短梗概")]/following-sibling::node()[position()>2 and position()<4]').getall()
        simple_brief = [sb.strip() for sb in simple_brief]

        detail_brief = response.xpath('//b[contains(text(),"详细梗概")]/following-sibling::node()[position()>2 and position()<last()-11]').getall()
        detail_brief = [db.strip() for db in detail_brief]
        detail_brief = [db for db in detail_brief if db != '' and db != '<br>']

        features = response.xpath('//td[@background="images/bg_art.gif"]/a[@target="_blank"]/text()').getall()

        characters = response.xpath('//div[@id="brief_role"]/text()').getall()
        characters = [character.strip() for character in characters]

        like_count = response.xpath('//span[@id="goodNo"]/text()').get()

        dislike_count = response.xpath('//span[@id="badNo"]/text()').get()

        star_count = response.xpath('//span[@id="favoriteNo"]/text()').get()
        if self.play_type == 'famous':
            editor = None
        else:
            editor = response.xpath('//font[@color="gray" and 1]/text()').get().strip().split('：')[1][:-1]
        
        item = PlayItem(
            id=id,
            subclass=subclass, 
            word_count=int(word_count),
            simple_brief=simple_brief,
            detail_brief=detail_brief,
            features=features,
            characters=characters,
            like_count=int(like_count),
            dislike_count=int(dislike_count),
            star_count=int(star_count),
            editor=editor
        )

        yield item