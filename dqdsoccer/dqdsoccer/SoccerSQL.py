# coding=utf-8
from dqdsoccer import settings
import MySQLdb

MYSQL_HOST = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_DB = settings.MYSQL_DB

db = MySQLdb.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB, charset="utf8")
cursor = db.cursor()

class SoccerSql():
   @classmethod
   def insert_db(cls, name, team, country, role, shirtnumber, rank):
       sql = 'insert into player_info(name, team, country, role, shirtnumber, rank) VALUES (%s, %s, %s, %s, %s, %s)'
       param = (name, team, country, role, shirtnumber, rank)
       try:
           cursor.execute(sql, param)
           db.commit()
       except MySQLdb.Warning, warning:
           print 'Warning:%s' %str(warning)
           db.rollback()

   @classmethod
   def player_exist(self, name):
        sql = "select EXISTS (SELECT 1 from player_info where name='%s')" %(name)
        try:
            cursor.execute(sql)
            return cursor.fetchone()[0]
        except MySQLdb.Warning, warning:
            print 'Warning:%s' %str(warning)
            db.rollback()

if SoccerSql.player_exist('w')==1:
    print '已经存在'
else:
    SoccerSql.insert_db('w', 'w', '', '', '9', '9')