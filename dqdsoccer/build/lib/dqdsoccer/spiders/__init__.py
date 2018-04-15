# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
# coding=utf-8
from scrapy.spiders import CrawlSpider
from scrapy.http import Request
import json
import requests
from dqdsoccer.items import DqdsoccerItem

class DqdSpider(CrawlSpider):
    name = 'dqdspider'
    start_urls = ['https://api.dongqiudi.com/data/fifa/club_rank?version=595']

    def parse(self, response):
        jsonpage = json.loads(response.text)
        for team in jsonpage['content']['data'][1:]:
            team_id = team['team_id']
            rank = team['rank']
            members_url = 'https://api.dongqiudi.com/data/v1/team/members/'+team_id
            yield Request(url=members_url, callback=self.get_members, dont_filter=True, meta={'rank': rank})

    def get_members(self, response):
        jsonpage = json.loads(response.text)
        for item in jsonpage['data']['list'][1:]:
            for mems in item['data']:
                person_id = mems['person_id']
                rank = response.meta['rank']
                param = {
                    'rank': rank,
                    'person_id': person_id
                }
                person_url = 'https://api.dongqiudi.com/data/v1/person/statistic_new/'+person_id
                yield Request(url=person_url, callback=self.get_ability, dont_filter=True, meta=param)

    def get_ability(self, response):
        # get player ability

        jsonpage_ability = json.loads(response.text)
        if 'base_info' in jsonpage_ability['league'][0]:
            appearance = jsonpage_ability['league'][0]['base_info']['appearances']
            starts = jsonpage_ability['league'][0]['base_info']['starts']
            goals = jsonpage_ability['league'][0]['base_info']['goals']
            assists = jsonpage_ability['league'][0]['base_info']['assists']
            success_pass_rate = jsonpage_ability['league'][0]['pass']['success_pass_rate']
            avg_tackles = jsonpage_ability['league'][0]['defense']['avg_tackles']
            avg_interceptions = jsonpage_ability['league'][0]['defense']['avg_interceptions']
            avg_clearances = jsonpage_ability['league'][0]['defense']['avg_clearances']
            param = {
                'appearance': appearance,
                'starts': starts,
                'goals': goals,
                'assists': assists,
                'success_pass_rate': success_pass_rate,
                'avg_tackles': avg_tackles,
                'avg_interceptions': avg_interceptions,
                'avg_clearances': avg_clearances,
                'rank': response.meta['rank']
            }
            person_id = response.meta['person_id']
            person_info_url = 'https://api.dongqiudi.com/data/v1/sample/person/'+person_id
            yield Request(url=person_info_url, callback=self.get_info, meta=param)

    def get_info(self, response):
        jsonpage = json.loads(response.text)
        item = DqdsoccerItem()
        item['name'] = jsonpage['person_name']
        item['country'] = jsonpage['nationality']
        item['team'] = jsonpage['team_info']['team_name']
        item['shirtnumber'] = jsonpage['team_info']['shirtnumber']
        item['role'] = jsonpage['team_info']['role']
        item['rank'] = response.meta['rank']
        item['appearance'] = response.meta['appearance']
        item['starts'] = response.meta['starts']
        item['goals'] = response.meta['goals']
        item['assists'] = response.meta['assists']
        item['success_pass_rate'] = response.meta['success_pass_rate']
        item['avg_tackles'] = response.meta['avg_tackles']
        item['avg_interceptions'] = response.meta['avg_interceptions']
        item['avg_clearances'] = response.meta['avg_clearances']
        return item
