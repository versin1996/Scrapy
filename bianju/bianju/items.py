# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PlayItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    writer = scrapy.Field()
    submit_data = scrapy.Field()
    read_count = scrapy.Field()
    review_count = scrapy.Field()
    douban_score = scrapy.Field()

    subclass = scrapy.Field()
    word_count = scrapy.Field()
    simple_brief = scrapy.Field()
    detail_brief = scrapy.Field()
    features = scrapy.Field()
    characters = scrapy.Field()
    like_count = scrapy.Field()
    dislike_count = scrapy.Field()
    star_count = scrapy.Field()
    editor = scrapy.Field()

    page = scrapy.Field()
    content = scrapy.Field()
    

    



