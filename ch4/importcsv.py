from sys import argv
import csv
import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()

if len(argv) < 2:
    print "Please provide a name of a csv file. ex: python importcsv.py myfile.csv"
    exit(1)
else:
    csvfile = argv[1]

c.execute("CREATE TABLE student ( id INT PRIMARY KEY, name TEXT, birth DATE, gender CHAR )")
student = csv.reader(open(csvfile, 'rb'), delimiter=',', quotechar='"')
index = 0
for row in student:
    index = index + 1
    print "%s %s" % (index, row)
    c.execute("INSERT INTO student VALUES (?, ?, ?, ?)", (index, row[0], row[1], row[2]))

conn.commit()
conn.close()
