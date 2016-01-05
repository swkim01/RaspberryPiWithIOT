import MySQLdb

db = MySQLdb.connect("localhost", "pi", "raspberry", "test")
cur = db.cursor()
cur.execute("select * from student")
while True:
    student = cur.fetchone()
    if not student: break
    print student

cur.close()
db.close()
