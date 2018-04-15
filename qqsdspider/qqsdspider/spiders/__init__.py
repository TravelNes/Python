# coding=utf-8
# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
from scrapy.spiders import Spider
from scrapy.http import FormRequest
import json
from qqsdspider.items import QqsdspiderItem


class QqsdSpider(Spider):
    name = 'qqsdspider'

    def start_requests(self):
        url = 'https://i.qqshidao.com/api/index.php?c_id=50000&c_type=1&c_cpid=1&suid=d0db383909cebf7ecc' \
              'ba9d09a177ed61&quid=383612&idfa=C385BEFB-6CF5-440F-A38F-0A3896FD2F4B'
        post_data = {
            'c_ck': 'MzgzNjEyZTk2YmU2NjZmM2MxNDkzNzg2NjQ1YjAxN2VmZGMyNDA=',
            'c_key': '9f36999cd47c95ebb9d30c940cfe0ee7'
        }
        return [FormRequest(url=url, formdata=post_data, callback=self.parse)]

    def parse(self, response):
        jsonpage = json.loads(response.text)
        for itemall in jsonpage['data']['all']:
            for items in jsonpage['data']['all'][itemall]['seasonlist'][17:]:
                for item in items['DATA']:
                    for iid in item:
                        season_url = 'https://i.qqshidao.com/api/index.php?c_id=50017&c_type=1&c_cpid=1&' \
                                     'suid=d0db383909cebf7eccba9d09a177ed61&quid=383612&idfa=C385BEFB-6CF5' \
                                     '-440F-A38F-0A3896FD2F4B'
                        post_data = {
                            'c_ck': 'MzgzNjEyZTk2YmU2NjZmM2MxNDkzNzg2NjQ1YjAxN2VmZGMyNDA=',
                            'c_key': '4a0f52738cc6515e1758a8011a1354c8',
                            'sid': iid['SEASONID']
                        }
                        yield FormRequest(url=season_url, formdata=post_data, callback=self.get_leagues)

    def get_leagues(self, response):
        jsonpage = json.loads(response.text)
        sid = jsonpage['data']['sid']
        stid = jsonpage['data']['stid']
        rank_url = 'https://i.qqshidao.com/api/index.php?c_id=50002&c_type=1&c_cpid=1&suid=d0db3839' \
                   '09cebf7eccba9d09a177ed61&quid=383612&idfa=C385BEFB-6CF5-440F-A38F-0A3896FD2F4B'
        post_data = {
            'c_ck': 'MzgzNjEyZTk2YmU2NjZmM2MxNDkzNzg2NjQ1YjAxN2VmZGMyNDA=',
            'c_key': 'b4bacbcdfd89d8f541c513d02239d66f',
            'sid': sid,
            't': 'all',
            'stid': stid
        }
        yield FormRequest(url=rank_url, formdata=post_data, dont_filter=True, callback=self.get_teams)

    def get_teams(self, response):
        jsonpage = json.loads(response.text)
        for teams in jsonpage['data']:
            teamid = teams['teamid']
            teamname = teams['teamname']
            team_url = 'https://i.qqshidao.com/api/index.php?c_id=50021&c_type=1&c_cpid=1&suid=d0db38390' \
                       '9cebf7eccba9d09a177ed61&quid=383612&idfa=C385BEFB-6CF5-440F-A38F-0A3896FD2F4B'
            post_data = {
                'c_ck': 'MzgzNjEyZTk2YmU2NjZmM2MxNDkzNzg2NjQ1YjAxN2VmZGMyNDA=',
                'c_key': '24159dbfe1a107e42a3bd650f87824eb',
                'teamid': teamid
            }
            yield FormRequest(url=team_url, formdata=post_data, dont_filter=True,
                              callback=self.get_members, meta={'teamname': teamname})

    def get_members(self, response):
        jsonpage = json.loads(response.text)
        for key in jsonpage['data']['players']:
            for playersm in jsonpage['data']['players'][key]:
                name = playersm['name']
                worth = playersm['worth']
                playerid = playersm['playerid']
                shirtnumber = playersm['teamnum']
                param = {
                    'teamname': response.meta['teamname'],
                    'name': name,
                    'shirtnumber': shirtnumber,
                    'worth': worth
                }
                ability_url = 'https://i.qqshidao.com/api/index.php?c_id=50024&c_type=1&c_cpid=1&suid=d0db383' \
                              '909cebf7eccba9d09a177ed61&quid=383612&idfa=C385BEFB-6CF5-440F-A38F-0A3896FD2F4B'
                post_data = {
                    'c_ck': 'MzgzNjEyZTk2YmU2NjZmM2MxNDkzNzg2NjQ1YjAxN2VmZGMyNDA=',
                    'c_key': '40a4c091ff680960800c801dac96c733',
                    'id': playerid,
                    'sid': ''
                }
                yield FormRequest(url=ability_url, formdata=post_data, meta=param, callback=self.get_ability)

    def get_ability(self, response):
        jsonpage = json.loads(response.text)
        item = QqsdspiderItem()
        if 'parr' or 'stats' in jsonpage['data']:
            item['aname'] = response.meta['name']
            item['shirtnumber'] = response.meta['shirtnumber']
            item['price'] = response.meta['worth']
            item['teamname'] = response.meta['teamname']
            item['playtotal'] = jsonpage['data']['stats']['playtotal']
            item['maintotal'] = jsonpage['data']['stats']['main_total']
            item['data1'] = jsonpage['data']['parr'][0][0]
            item['data2'] = jsonpage['data']['parr'][1][0]
            item['data3'] = jsonpage['data']['parr'][2][0]
            item['data4'] = jsonpage['data']['parr'][3][0]
            return item
        else:
            print 'Data Empty'
