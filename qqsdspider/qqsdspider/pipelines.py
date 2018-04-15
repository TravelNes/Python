# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from qqsdspider.QqsdSql import QqsdSQL
from qqsdspider.items import QqsdspiderItem


class QqsdspiderPipeline(object):

    def process_item(self, item, spider):
        item = QqsdspiderItem
        price = item['price']
        shirtnumber = item['shirtnumber']
        playtotal = item['playtotal']
        maintotal = item['maintotal']
        teamname = item['teamname']
        data1 = item['data1']
        data2 = item['data2']
        data3 = item['data3']
        data4 = item['data4']
        if QqsdSQL.if_team(teamname) == 1:
            aname = QqsdSQL.change_name(shirtnumber, teamname)
            QqsdSQL.insert_db(data1=data1, data2=data2, data3=data3, data4=data4, aname=aname, playtotal=playtotal,
                              price=price, maintotal=maintotal, shirtnumber=shirtnumber, teamname=teamname)
            print 'name:%s shirtnumber:%s teamname:%s' % (aname, shirtnumber, teamname)
