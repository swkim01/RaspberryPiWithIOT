import MySQLdb

def displayResult(cur, condition):
    cur.execute("select * from student where %s" % condition)
    print("The students where %s are as follow." % condition)
    rows = cur.fetchall()
    for row in rows:    
        print("%2d %20s, %10s %c" % row)

db = MySQLdb.connect("localhost", "pi", "raspberry", "test")
cur = db.cursor()
displayResult(cur, "gender='M'")
#cur.execute("select * from student where birth<%s", 19800101)
displayResult(cur, "birth < '19800101'")

cur.close()
db.close()
