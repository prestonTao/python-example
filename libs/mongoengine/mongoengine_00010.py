# -*- coding: utf-8 -*-

from mongoengine import connect
# connect('test', host='127.0.0.1', port=27017)
# connect('test', host='mongodb://localhost/test')
connect('test')   # 连接本地blog数据库

