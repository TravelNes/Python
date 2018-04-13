# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
# coding=utf-8
from scrapy.spiders import CrawlSpider
from scrapy.http import Request
import json
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
                person_url = 'https://api.dongqiudi.com/data/v1/sample/person/'+person_id
                yield Request(url=person_url, callback=self.get_person, dont_filter=True, meta={'rank': rank})

    def get_person(self, response):
        jsonpage = json.loads(response.text)
        item = DqdsoccerItem()
        item['name'] = jsonpage['person_name']
        item['country'] = jsonpage['nationality']
        item['team'] = jsonpage['team_info']['team_name']
        item['shirtnumber'] = jsonpage['team_info']['shirtnumber']
        item['role'] = jsonpage['team_info']['role']
        item['rank'] = response.meta['rank']
        return item
