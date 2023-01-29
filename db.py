from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

import os

DB_USER = os.getenv('GENERATOR_DB_USER') or 'root'
DB_PASS = os.getenv('GENERATOR_DB_PASS') or 'change-me'
DB_HOST = os.getenv('DB_HOST') or '127.0.0.1'
DB_NAME = 'micro'

Base = declarative_base()
db_path = 'mysql+pymysql://' + str(DB_USER) + ':' \
                             + str(DB_PASS) + '@' \
                             + str(DB_HOST) + '/' \
                             + DB_NAME 
print(db_path)
engine = create_engine(db_path, echo=False)


class Generator(Base):
    __tablename__ = 'generator'
    id = Column(Integer, primary_key=True)
    msg = Column(String(16), index=True)
    date = Column(DateTime)

    def __init__(self, msg, date, id=0):
        self.id = id
        self.msg = msg
        self.date = date

    def __len__(self):
        # need set some integer like count of all active gens
        return 1

    def __repr__(self):
        return str(self.id) + ' ' + str(self.msg) + ' ' + str(self.date)

    def __getitem__(self, id):
        print(id)
        return bytes(f'item: {id}', encoding='utf8')


class Worker(Base):
    __tablename__ = 'worker'
    id = Column(Integer, primary_key=True)
    count = Column(Integer, index=True)
    last_id = (Integer)


class front(Base):
    __tablename__ = 'front'
    id = Column(Integer, primary_key=True)
    count = Column(Integer, index=True)
    last_id = (Integer)

