#from sqlalchemy.dialects.sqlite import DATE
#from sqlalchemy.ext.compiler import compiles
#
#@compiles(DATE, 'sqlite')
#def compile_date(element, compiler, **kw):
#  return "CHAR_%s" % element.__class__.__name__

from sqlalchemy import create_engine, Column, Integer, String, Date, DateTime
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import text

engine = create_engine('sqlite:////home/pi/flask/test.db', echo=True, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
#Base.query = db_session.query_property()

def init_db():
    Base.metadata.create_all(bind=engine)

class Student(Base):
    __tablename__ = 'Student'
    __table_args__ = {'sqlite_autoincrement': True}

    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    birth = Column(String)
    #birth = Column(DateTime)
    #birth = Column(Date)
    #birth = Column(DATE)
    #birth = Column(DATE(
    #    storage_format="%(year)04d%(month)02d%(day)02d",
    #    regexp=r"(\d{4})(\d{2})(\d{2})",))
    gender = Column(String)

    def __init__(self, id=1, name=None, birth=None, gender=None):
        self.id = id
        self.name = name
        self.birth = birth
        self.gender = gender

    def __repr__(self):
        #return '<Student %r>' % (self.name,)
        return '<%r, %r, %r>' % (self.name,self.birth,self.gender)

def show():
    row = db_session.execute("SELECT * from student").fetchall()
    print(row)

def showall():
    #row = Student.query.all()
    row = db_session.query(Student).all()
    print(row)

def showitem(item):
    row = db_session.execute("SELECT * from student where name like "+"'%"+item+"%'").fetchall()
    print(row)
