# -*- coding: utf-8 -*-
'''
Created on 2015年5月25日

@author: Administrator
'''

from mongoengine.document import Document
from mongoengine import fields
from mongoengine import connect

# ；链接数据库
connect('test')

# 定义数据结构
class User(Document):
    name = fields.StringField()
    age = fields.IntField()


#------------------------------------------
def save():
    # 创建一个对象
    u = User(name='taohongfei', age=18)
    # 保存一条记录
    u.save()
# save()

#------------------------------------------
def update():
#     u = User.objects.get(name='taohongfei')
#     print(u.age)
#     u.age = 20
#     u.update(age=20)

#     u = User.objects.all()
#     u = User.objects(name='taohongfei')
#     u = u[0]
#     u.update(set__age=18)
#     u.update_one(set__age=22)
    # 批量修改
    User.objects(name='taohongfei').update(set__age=19)
# update()


#------------------------------------------
def select():
    # 查询所有
    users = User.objects.all()
    print(users)
    # 按条件查找
    users = User.objects(name='taohongfei')
    print(users)
select()

