from apscheduler.schedulers.blocking import BlockingScheduler

from scraper import events_scraper
from scraper import data_importer
from scraper import data_cleaner

sched = BlockingScheduler()


# Note on times: Our Heroku instance in five hours ahead of us

@sched.scheduled_job('cron', hour=1, minute=30)
def scheduled_job():
    print('Job: Fetching events')
    events_scraper.get_events()

@sched.scheduled_job('cron', hour=7, minute=30)
def scheduled_job():
    print('Job: Importing events')
    data_importer.import_events()

@sched.scheduled_job('cron', hour=8, minute=30)
def scheduled_job():
    print('Job: Cleaning up old events')
    data_cleaner.do_clean()


# Test jobs:
#
# @sched.scheduled_job('cron', hour=18, minute=18)
# def scheduled_job():
#     print('Job: Fetching events')
#     events_scraper.get_events()
#
# @sched.scheduled_job('cron', hour=18, minute=19)
# def scheduled_job():
#     print('Job: Importing events')
#     data_importer.import_events()
#
# @sched.scheduled_job('cron', hour=18, minute=20)
# def scheduled_job():
#     print('Job: Cleaning up old events')
#     data_cleaner.do_clean()


sched.start()
