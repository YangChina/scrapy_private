# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class SpiderMeizituItem(scrapy.Item):
    # define the fields for your item here like:
    images = scrapy.Field()
    image_urls = scrapy.Field()
    index = scrapy.Field()

class DoubanMovieItem(scrapy.Item):
    # 排名
    ranking = scrapy.Field()
    # 电影名称
    movie_name = scrapy.Field()
    # 评分
    score = scrapy.Field()
    # 评论人数
    score_num = scrapy.Field()

class Exam_Gongwuyuan_shenlun_Item(scrapy.Item):
    # 标题
    title = scrapy.Field() 
    # 内容 
    content = scrapy.Field()

class NationalStandardItem(scrapy.Item):
    StandardCategory = scrapy.Field()
    StandardNum = scrapy.Field()
    StandardTitle = scrapy.Field()
    StandardUrl = scrapy.Field()
    StandardID = scrapy.Field()