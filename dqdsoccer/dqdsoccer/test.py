import MySQLdb
from dqdsoccer import settings

MYSQL_HOST = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_DB = settings.MYSQL_DB
agents = settings.AGENTS

db = MySQLdb.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB)
cursor = db.cursor()
for item in agents:
    print item
    sql = "insert into agents(agent) VALUES (%s)"
    param = (item)
    cursor.execute(sql, param)
    db.commit()
