from apscheduler.schedulers.blocking import BlockingScheduler

from scraper import events_scraper
from scraper import data_importer
from scraper import data_cleaner

sched = BlockingScheduler()


@sched.scheduled_job('cron', hour=6, minute=30)
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


sched.start()
