# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DqdsoccerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    team = scrapy.Field()
    rank = scrapy.Field()
    country = scrapy.Field()
    role = scrapy.Field()
    shirtnumber = scrapy.Field()

    appearance = scrapy.Field()
    starts = scrapy.Field()
    goals = scrapy.Field()
    assists = scrapy.Field()
    success_pass_rate = scrapy.Field()
    avg_tackles = scrapy.Field()
    avg_interceptions = scrapy.Field()
    avg_clearances = scrapy.Field()
