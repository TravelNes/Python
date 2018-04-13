# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from dqdsoccer.SoccerSQL import SoccerSql
from dqdsoccer.items import DqdsoccerItem


class DqdsoccerPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, DqdsoccerItem):
            name = item['name'].encode('utf-8')
            team = item['team'].encode('utf-8')
            country = item['country'].encode('utf-8')
            role = item['role'].encode('utf-8')
            shirtnumber = item['shirtnumber'].encode('utf-8')
            rank = item['rank'].encode('utf-8')
            rest = SoccerSql.player_exist(name)
            if rest==1:
                print '已经存在'
            else:
                SoccerSql.insert_db(name, team, country, role, shirtnumber, rank)
