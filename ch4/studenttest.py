import MySQLdb

db = MySQLdb.connect("localhost", "pi", "raspberry", "test")
cur = db.cursor()
cur.execute("update student set gender='M' where id<=2")
cur.execute("select * from student")
desc = cur.description
print desc[0][0], desc[3][0], desc[1][0]

while True:
    student = cur.fetchone()
    if not student: break
    #print student[desc[0][0]],student[desc[3][0]],student[desc[1][0]]
    print student[0],student[3],student[1]

cur.close()
db.close()
