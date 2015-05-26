# -*- coding: utf-8 -*-

'''
Created on 2015年5月21日

@author: Administrator
'''
# 测试版本   0.9.8

from random import randint

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer


DB_CONNECT_STRING = 'mysql://root:root@127.0.0.1:3306/test?charset=utf8&use_unicode=1'
params = {'pool_recycle': 60, 'echo_pool': True, 'pool_size': 500, 'echo': True}

engine = create_engine(DB_CONNECT_STRING, *(), **params)
# engine = create_engine(DB_CONNECT_STRING)
DB_Session = sessionmaker(bind=engine)
session = DB_Session()

BaseModel = declarative_base()

class User(BaseModel):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    age = Column(Integer)

class Friendship(BaseModel):
    __tablename__ = 'friendship'
    id = Column(Integer, primary_key=True)
    user_id1 = Column(Integer, ForeignKey('user.id'))
    user_id2 = Column(Integer, ForeignKey('user.id'))

BaseModel.metadata.drop_all(engine)
BaseModel.metadata.create_all(engine)

for i in xrange(100):
    session.add(User(age=randint(1, 100)))
session.flush() # 或 session.commit()，执行完后，user 对象的 id 属性才可以访问（因为 id 是自增的）
for i in xrange(100):
    session.add(Friendship(user_id1=randint(1, 100), user_id2=randint(1, 100)))
session.commit()
# 删除这句代码会报错，因为这条记录有其他表关联
session.query(User).filter(User.age < 50).delete()


