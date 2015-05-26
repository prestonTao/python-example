# -*- coding: utf-8 -*-

from mongoengine.document import Document
from mongoengine import fields
from mongoengine import connect

# ；链接数据库
connect('test')

# 定义数据结构
class User(Document):
    name = fields.StringField()

# 创建一个对象
u = User(name='taohongfei')

# 保存一条记录
u.save()

# 聚合查找
count = User.objects(name='taohongfei').count()
print(count)
num_users = len(User.objects)
print(num_users)
num_users = User.objects.count()
print(num_users)

# 两种限制查询结果个数的方法
# users = User.objects[10:15]
# users = User.objects.skip(10).limit(5)
users = User.objects.limit(1)
print(users[0].name)

