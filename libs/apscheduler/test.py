
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
scheduler.add_job(p, 'interval', seconds=2)
scheduler.start()
# scheduler.add_job(func = p, trigger = 'interval', minutes=2)
# scheduler.add_job(func, trigger, args, kwargs, id, name, misfire_grace_time, coalesce, max_instances, next_run_time, jobstore, executor, replace_existing)

# time.sleep(10)