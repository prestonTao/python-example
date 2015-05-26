# -*- coding: utf-8 -*-


from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor


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
scheduler.add_job(p, 'cron', second='0', minute='44', hour='9', day='21', month='5', day_of_week='', year='')
# scheduler.reschedule_job('my_job_id', trigger='cron', minute='*/5')
# scheduler.reschedule_job('my_job_id', trigger='cron', minute='*/5')
scheduler.start()