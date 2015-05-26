# -*- coding: utf-8 -*-
'''
Created on 2015年5月22日

@author: Administrator
'''
#测试版本  2.10.3

import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

r.set('name','taohongfei')

#看是否存在这个键值
print(r.exists('name'))

# 列出所有键值。（这时候已经存了4个了）
print(r.keys())

# 库里有多少key，多少条数据
print(r.dbsize())

print(r.get('name'))
print(r.delete('name'))

print(r.dbsize())

# 强行把数据库保存到硬盘。保存时阻塞
r.save()

# 删除当前数据库的所有数据
r.flushdb()