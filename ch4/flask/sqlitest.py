import sqlite3, sys

db = sqlite3.connect("sqlitest/test.db")
db.row_factory = sqlite3.Row
cur = db.cursor()
query = cur.execute("select * from student")
#for row in query.fetchall():
#    print row["id"],row["name"],row["gender"]
while True:
    student = cur.fetchone()
    if not student: break
    if sys.version_info < (3,0):
        print(student)
    else:
        print([col for col in student])

cur.close()
db.close()
