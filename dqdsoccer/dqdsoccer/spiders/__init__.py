# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
# coding=utf-8
from scrapy.spiders import CrawlSpider
import scrapy
import json
from dqdsoccer.items import DqdsoccerItem
from twisted.internet import reactor
from scrapy.utils.log import configure_logging
from scrapy.crawler import CrawlerRunner


class DqdSpider(CrawlSpider):
    name = 'dqdspider'
    start_urls = ['https://api.dongqiudi.com/data/fifa/club_rank?version=595']

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 NewsApp/5.9.5 NetType/NA Technology/Wifi (iPhone; iOS 11.2.6; Scale/3.00) (modelIdentifier/iPhone10,2 )',
            'Referer': 'dongqiudi://v1/main/data/league/755',
            'action': 'click',
            'UUID': '@KZ6tDX4s8cur5gQehtB+qpJ5paxr5MVvd0wtz4Z8wNzimWWbw4G8iWMCUibCVqcV0DjDK/9R/eg=',
            'positon': '13',
            'sign': 'Ry/X+h+Q/EInFr05q4JTjKu1ZsQd1vqphVbuvtO0K8s=',
            'Connection': 'keep-alive',
            'IDFV': '8D36C49E-DEAA-4DAA-8B6A-CEEF0C1598FD',
            'page': '/rankdata/755',
            'api-key': 'dongqiudi.com',
            'IDFA': 'C385BEFB-6CF5-440F-A38F-0A3896FD2F4B'
}
        self.cookies = {
            'laravel_session': 'eyJpdiI6Ikk4U3NGbjZJMWVCa3VxSkhQaHI1elRvdGpiM3JtNkJobzdGcEFOaXRyajg9IiwidmFsdWUiOiJlQ3ZvVXlHRThKVndXM3RHSW9SQ0ZOOEd4MWkzY1VqXC9cL256TVQrNmNVZERsa1A5VW5yS2RmRHA1TGkrR05NNFBrZEJ6R1JETlFjU1ZUMkVhWFg1WTRBPT0iLCJtYWMiOiJlNTA5OWEyNTFmY2E2ZGIzM2E2MWEyZDVhOWFjNjJhZGRhNjYyYmViZjI1MDk0Nzg3Y2VhNTAyN2RhN2Y2MzUwIn0%3D',
            'dqduid': 'ChN8ElqzfmrA22sCAyiZAg=='
}

    def parse(self, response):
        jsonpage = json.loads(response.text)
        for team in jsonpage['content']['data'][1:]:
            team_id = team['team_id']
            rank = team['rank']
            members_url = 'https://api.dongqiudi.com/data/v1/team/members/'+team_id
            yield scrapy.Request(url=members_url, callback=self.get_members, dont_filter=True, meta={'rank': rank})

    def get_members(self, response):
        jsonpage = json.loads(response.text)
        for item in jsonpage['data']['list'][1:]:
            for mems in item['data']:
                person_id = mems['person_id']
                rank = response.meta['rank']
                person_url = 'https://api.dongqiudi.com/data/v1/sample/person/'+person_id
                yield scrapy.Request(url=person_url, callback=self.get_person, dont_filter=True, meta={'rank': rank})

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

class QQSDSpider(CrawlSpider):
    name = 'qqsdspider'
    pass

configure_logging()
runner = CrawlerRunner()
runner.crawl(DqdSpider)
d = runner.join()
d.addBoth(lambda _: reactor.stop())
reactor.run()