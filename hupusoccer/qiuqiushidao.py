# coding=utf-8
import requests
import json
# 球球是道数据
# 获取所有联赛url
mainurl = 'https://i.qqshidao.com/api/index.php?c_id=50000&c_type=1&c_cpid=1&suid=d0db383909cebf7eccba9d09a17' \
          '7ed61&quid=383612&idfa=C385BEFB-6CF5-440F-A38F-0A3896FD2F4B'
# 联赛url
leagueurl = "https://i.qqshidao.com/api/index.php?c_id=50017&c_type=1&c_cpid=1&suid=d0db383909cebf7eccba9d0" \
            "9a177ed61&quid=383612&idfa=C385BEFB-6CF5-440F-A38F-0A3896FD2F4B"
# 积分url
rankurl = 'https://i.qqshidao.com/api/index.php?c_id=50002&c_type=1&c_cpid=1&suid=d0db383909cebf7eccba9d09a1' \
          '77ed61&quid=383612&idfa=C385BEFB-6CF5-440F-A38F-0A3896FD2F4B'
cookies = {
    'Hm_lvt_1cc6125513403f855d2a2484ef79b3b3': '1519715220,1521205969'
}


class Soccer:
    def __init__(self):
        self.session = requests.session()
        self.session.headers = {
            'Host': 'i.qqshidao.com',
            'Come-From': 'qiuqiushidao',
            'AppVersion': '3.4.1',
            'AppRegfrom': 'bocai',
            'Content-Type':	'application/x-www-form-urlencoded',
            'Connection': 'keep-alive',
            'User-Agent': 'qiuqiushidao_bocai/3.4.1 (iPhone; iOS 11.2.6; Scale/3.00)'
             }
        self.session.cookies.update(cookies)
        self.post_data = {
            'c_ck':	'MzgzNjEyZTk2YmU2NjZmM2MxNDkzNzg2NjQ1YjAxN2VmZGMyNDA='
        }

    # 获取所有的联赛列表
    def get_all_league_match(self):
        self.post_data['c_key'] = '9f36999cd47c95ebb9d30c940cfe0ee7'
        page = self.session.post(url=mainurl, data=self.post_data, verify=False).text
        jl = json.loads(page)
        seasonid = jl['data']['hot'][1][0]['SEASONID']
        self.get_league_match(seasonid)

    # 获取各联赛信息
    def get_league_match(self, seasonid):
        self.post_data['sid'] = seasonid
        self.post_data['c_key'] = '4a0f52738cc6515e1758a8011a1354c8'
        page = self.session.post(url=leagueurl, data=self.post_data, verify=False).text
        jl = json.loads(page)
        stid = jl['data']['stid']
        sid = jl['data']['sid']
        self.get_rank(sid, stid)

    # 获取联赛积分
    def get_rank(self, sid, stid):
        self.post_data['sid'] = sid
        self.post_data['stid'] = stid
        self.post_data['c_key'] = 'b4bacbcdfd89d8f541c513d02239d66f'
        self.post_data['t'] = 'all'
        page = self.session.post(url=rankurl, data=self.post_data, verify=False).text
        jl = json.loads(page)
        items = jl['data']
        for item in items:
            print item['order'], item['teamname']


Soccer().get_all_league_match()
