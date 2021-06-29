from bottle import *
from bottle_sqlite import SQLitePlugin

sqlite = SQLitePlugin(dbfile='test.db')
install(sqlite)

@route('/show')
def showall(db):
    row = db.execute("SELECT * from student")
    if row:
        return template('showitem', items=row)
    return HTTPError(404, "Page not found")

@route('/show/<item>')
def show(item, db):
    row = db.execute("SELECT * from student where name like ?", ('%'+item+'%',))
    if row:
        return template('showitem', items=row)
    return HTTPError(404, "Page not found")

run(host='192.168.0.31', port=8008)
