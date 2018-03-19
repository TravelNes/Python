import MySQLdb

db = MySQLdb.connect('localhost', 'root', 'yzh199302', 'test')
cursor = db.cursor()
cursor.execute('select * from user')
data = cursor.fetchall()
print len(data)
cursor.close()
