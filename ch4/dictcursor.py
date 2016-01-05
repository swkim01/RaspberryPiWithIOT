import MySQLdb

db = MySQLdb.connect("localhost", "pi", "raspberry", "test")
cur = db.cursor(MySQLdb.cursors.DictCursor)
cur.execute("insert into student values(%s,%s,%s,%s)",(4,"Jang GilSan","771028",'M'))
db.commit()
cur.execute("select * from student")
desc = cur.description
print desc[0][0], desc[3][0], desc[1][0]

while True:
    student = cur.fetchone()
    if not student: break
    print student["id"],student["gender"],student["name"]
    #print student[0],student[3],student[1]

cur.close()
db.close()
