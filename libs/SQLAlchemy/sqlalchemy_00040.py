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


# 如何批量插入大批数据？
# 上面我批量插入了 10000 条记录，半秒内就执行完了；而 ORM 方式会花掉很长时间。
session.execute(
    User.__table__.insert(),
    [{'name': `randint(1, 100)`,'age': randint(1, 100)} for i in xrange(10000)]
)
session.commit()


session.query(User.name).prefix_with('HIGH_PRIORITY').all()
session.execute(User.__table__.insert().prefix_with('IGNORE'), {'id': 1, 'name': '1'})
