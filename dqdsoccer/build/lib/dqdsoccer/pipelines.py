# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from dqdsoccer.SoccerSQL import SoccerSql
from dqdsoccer.items import DqdsoccerItem

'''
item['appearance'] = response.meta['appearance']
item['starts'] = response.meta['starts']
item['goals'] = response.meta['goals']
item['assists'] = response.meta['assists']
item['success_pass_rate'] = response.meta['success_pass_rate']
item['avg_tackles'] = response.meta['avg_tackles']
item['avg_interceptions'] = response.meta['avg_interceptions']
item['avg_clearances'] = response.meta['avg_clearances']
'''
class DqdsoccerPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, DqdsoccerItem):
            name = item['name'].encode('utf-8')
            team = item['team'].encode('utf-8')
            country = item['country'].encode('utf-8')
            role = item['role'].encode('utf-8')
            shirtnumber = item['shirtnumber'].encode('utf-8')
            rank = item['rank'].encode('utf-8')
            appearance = item['appearance']
            starts = item['starts']
            goals = item['goals']
            assists = item['assists']
            success_pass_rate = item['success_pass_rate']
            avg_tackles = item['avg_tackles']
            avg_interceptions = item['avg_interceptions']
            avg_clearances = item['avg_clearances']
            rest = SoccerSql.player_exist(name)
            if rest==1:
                print '已经存在'
            else:
                SoccerSql.insert_db(name, team, country, role, shirtnumber, rank, appearance,
                                    starts, goals, assists, success_pass_rate, avg_tackles, avg_interceptions, avg_clearances)
