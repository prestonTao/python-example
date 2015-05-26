# -*- coding: utf-8 -*-

'''
Created on 2015年5月21日

@author: Administrator
'''
# 测试版本   0.9.8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_CONNECT_STRING = 'mysql://root:root@127.0.0.1:3306/test?charset=utf8&use_unicode=1'
params = {'pool_recycle': 60, 'echo_pool': True, 'pool_size': 500, 'echo': True}

engine = create_engine(DB_CONNECT_STRING, *(), **params)
# engine = create_engine(DB_CONNECT_STRING)
DB_Session = sessionmaker(bind=engine)
session = DB_Session()

session.execute('create database abc')
print session.execute('show databases').fetchall()
session.execute('use abc')
session.execute('create table user(id int)')
# 建 user 表的过程略
print session.execute('select * from user where id = 1').first()
print session.execute('select * from user where id = :id', {'id': 1}).first()

