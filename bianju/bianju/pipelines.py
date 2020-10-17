# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from bianju.db import DB
import json

class BianjuPipeline(object):
	def open_spider(self, spider):
		database = 'bianju'
		collection = spider.name + '_' + spider.play_type
		self.db = DB(database, collection)
		
	def process_item(self, item, spider):
		self.db.insert(dict(item))
		# try:
		# 	print(item.get('id'), item.get('page'))# print(item.get('id'), item.get('detail_brief')[-3:])
		# 	pass
		# except:
		# 	pass
		# print('*' * 177)	
		return item