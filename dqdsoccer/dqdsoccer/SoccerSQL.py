# coding=utf-8
from dqdsoccer import settings
import MySQLdb

MYSQL_HOST = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_DB = settings.MYSQL_DB

db = MySQLdb.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB, charset="utf8")
cursor = db.cursor()
'''
    appearance = scrapy.Field()
    starts = scrapy.Field()
    goals = scrapy.Field()
    assists = scrapy.Field()
    success_pass_rate = scrapy.Field()
    avg_tackles = scrapy.Field()
    avg_interceptions = scrapy.Field()
    avg_clearances = scrapy.Field()
'''
class SoccerSql():
   @staticmethod
   def insert_db(name, team, country, role, shirtnumber, rank, appearance,
                 starts, goals, assists, success_pass_rate, avg_tackles, avg_interceptions, avg_clearances):
       sql = 'insert into player_info(name, team, country, role, shirtnumber, rank, appearance, starts, goals,' \
             ' assists, success_pass_rate, avg_tackles, avg_interceptions, avg_clearances) VALUES' \
             ' (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
       param = (name, team, country, role, shirtnumber, rank, appearance,
                 starts, goals, assists, success_pass_rate, avg_tackles, avg_interceptions, avg_clearances)
       try:
           cursor.execute(sql, param)
           db.commit()
       except MySQLdb.Warning, warning:
           print 'Warning:%s' %str(warning)
           db.rollback()

   @staticmethod
   def player_exist(name):
        sql = "select EXISTS (SELECT 1 from player_info where name='%s')" %(name)
        try:
            cursor.execute(sql)
            return cursor.fetchone()[0]
        except MySQLdb.Warning, warning:
            print 'Warning:%s' %str(warning)
            db.rollback()
