# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

'''
shotin:前锋(中锋)进球数
shotrate:前锋(中锋)射门命中率
weixie:前锋威胁球
guoren:前锋过人数
chuanqiu:中锋传球成功率
chuqiu:中锋触球次数
qiangduan:后卫场均抢断
lanjie:后卫场均拦截
jiewei:后卫场均解围
shiqiu:门卫场均失球
pujiu:门卫场均扑救
price:球员身价

'''


class QqsdspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    aname = scrapy.Field()
    data1 = scrapy.Field()
    data2 = scrapy.Field()
    data3 = scrapy.Field()
    data4 = scrapy.Field()

    playtotal = scrapy.Field()
    maintotal = scrapy.Field()
    price = scrapy.Field()
    shirtnumber = scrapy.Field()
    teamname = scrapy.Field()
