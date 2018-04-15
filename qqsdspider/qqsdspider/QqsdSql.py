# coding=utf-8
import MySQLdb
from qqsdspider import settings

MYSQL_HOST = settings.MYSQL_HOST
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_DB = settings.MYSQL_DB

db = MySQLdb.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB, charset='utf8')
cursor = db.cursor()


class QqsdSQL:

    @staticmethod
    def insert_db(data1, data2, data3, data4, aname, price, shirtnumber, playtotal, maintotal, teamname):
        insert_sql = 'insert into player_ability(data1, data2, data3, data4, aname, price, shirtnumber,' \
              'playtotal, maintotal, teamname) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

        param = (data1, data2, data3, data4, aname, price, shirtnumber, playtotal, maintotal, teamname)
        try:
            cursor.execute(insert_sql, param)
            db.commit()
        except MySQLdb.Warning, warning:
            print 'Warning:%s' % str(warning)
            db.rollback()

    @staticmethod
    def change_name(shirtnumber, team):
        query_sql = "select name, shirtnumber, team from player_info WHERE shirtnumber='%s' and team='%s'" % (shirtnumber, team)
        cursor.execute(query_sql)
        results = cursor.fetchone()
        return results[0]

    @staticmethod
    def if_team(team):
        query_sql = "select DISTINCT team from player_info WHERE team='%s'" % (team)
        cursor.execute(query_sql)
        result = cursor.fetchone()
        if result is not None:
            return 1
        else:
            return 0

    @staticmethod
    def updata_data(shirtnumber, team):
        query_sql = "select name, shirtnumber, team from player_info WHERE shirtnumber='%s' and team='%s'" % (shirtnumber, team)
        cursor.execute(query_sql)
        results = cursor.fetchone()

# print QqsdSQL.if_team('曼')
print QqsdSQL.change_name('8', '曼城')