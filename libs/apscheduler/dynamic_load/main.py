# -*- coding: utf-8 -*-
'''
Created on 2015年5月26日

@author: Administrator
'''

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
import threading


def p():
    print "123"

jobstores = {
    'mongo': MongoDBJobStore(),
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}
executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 3
}
scheduler = BlockingScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults)

scheduler.remove_all_jobs()

scheduler.add_job(p, 'cron', second='*/5', minute='*', hour='*', day='*', month='*', day_of_week='0-6', year='*')

# scheduler.reschedule_job('my_job_id', trigger='cron', minute='*/5')
# scheduler.reschedule_job('my_job_id', trigger='cron', minute='*/5')
print("befor")
t = threading.Thread(target=scheduler.start)
t.start()
print("after")

def load(packname):
    exec("from libs.apscheduler.dynamic_load import "+packname)
    p = eval(packname+".run")
#     p()
    scheduler.add_job(p, 'cron', second='*/5', minute='*', hour='*', day='*', month='*', day_of_week='0-6', year='*')

# from libs.apscheduler.dynamic_load import job1

load('job1')
print("start")

# if __name__ == '__main__':
#     file = open('job1.py')
#     content = file.read()
#     exec content
#     run()

#     job1.run()
    