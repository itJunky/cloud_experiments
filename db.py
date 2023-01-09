from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

import os

DB_USER = os.getenv('GENERATOR_DB_USER')
DB_PASS = os.getenv('GENERATOR_DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = 'micro'

if DB_USER:
    print(f'Have credentials for DB_USER: {DB_USER}')
else:
    print('Use default credentials for DB')
    DB_USER = 'micro'
    DB_PASS = 'ciew1Igh'
    DB_HOST = 'localhost'


Base = declarative_base()
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = 'mysql+pymysql://' + DB_USER + ':' + DB_PASS + '@' + DB_HOST + '/' + DB_NAME 
engine = create_engine(db_path, echo=False)


class Generator(Base):
    __tablename__ = 'generator'
    id = Column(Integer, primary_key=True)
    msg = Column(String(16), index=True)
    date = Column(DateTime)


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

