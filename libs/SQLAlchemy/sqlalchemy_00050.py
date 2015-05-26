# -*- coding: utf-8 -*-

'''
Created on 2015年5月21日

@author: Administrator
'''
# 测试版本   0.9.8

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

# 如何让执行的 SQL 语句增加前缀？
session.query(User.name).prefix_with('HIGH_PRIORITY').all()
session.execute(User.__table__.insert().prefix_with('IGNORE'), {'id': 1, 'name': '1'})


# 如何替换一个已有主键的记录？
user = User(id=1, name='ooxx')
session.merge(user)
session.commit()


# 如何使用无符号整数？
# 可以使用 MySQL 的方言：
# from sqlalchemy.dialects.mysql import INTEGER
# id = Column(INTEGER(unsigned=True), primary_key=True)

# 如何获取字段的长度？
print(User.name.property.columns[0].type.length)

# 如何指定使用 InnoDB，以及使用 UTF-8 编码？
class User_utf8(BaseModel):
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }




