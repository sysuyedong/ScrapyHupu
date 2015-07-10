# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	pass

class DmozItem(scrapy.Item):
	title = scrapy.Field()
	link = scrapy.Field()
	desc = scrapy.Field()

class DoubanMoiveItem(scrapy.Item):
	name = scrapy.Field()
	year = scrapy.Field()
	director = scrapy.Field()
	score = scrapy.Field()
	picture = scrapy.Field()
	actor = scrapy.Field()
	classification = scrapy.Field()
	url = scrapy.Field()

class HupuPostItem(scrapy.Item):
	title = scrapy.Field()
	lighten_num = scrapy.Field()
	comment_num = scrapy.Field()
	author = scrapy.Field()
	publish_time = scrapy.Field()
	url = scrapy.Field()

class HupuUserItem(scrapy.Item):
	username = scrapy.Field()
	sex = scrapy.Field()
	place = scrapy.Field()
	level = scrapy.Field()
	calorie = scrapy.Field()
	online_time = scrapy.Field()
	register_time = scrapy.Field()
	visit_num = scrapy.Field()
	fans_num = scrapy.Field()
	follow_num = scrapy.Field()
	posts_num = scrapy.Field()
	avatar = scrapy.Field()
	url = scrapy.Field()