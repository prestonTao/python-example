# -*- coding: utf-8 -*-
'''
Created on 2015年5月21日

@author: Administrator
'''
# 测试版本   0.9.8

# from south.tests.fakeapp.models import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, CHAR


DB_CONNECT_STRING = 'mysql://root:root@127.0.0.1:3306/test?charset=utf8&use_unicode=1'
params = {'pool_recycle': 60, 'echo_pool': True, 'pool_size': 500, 'echo': True}

engine = create_engine(DB_CONNECT_STRING, *(), **params)
# engine = create_engine(DB_CONNECT_STRING)
DB_Session = sessionmaker(bind=engine)
session = DB_Session()

# declarative_base() 创建了一个 BaseModel 类，这个类的子类可以自动与一个表关联。
BaseModel = declarative_base()

class User(BaseModel):
    __tablename__ = 'user'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', CHAR(30)) # or Column(String(30))



def init_db():
    # BaseModel.metadata.create_all(engine) 会找到 BaseModel 的所有子类，并在数据库中建立这些表;
    BaseModel.metadata.create_all(engine)
def drop_db():
    BaseModel.metadata.drop_all(engine)

init_db()




