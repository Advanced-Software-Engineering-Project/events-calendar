from apscheduler.schedulers.blocking import BlockingScheduler

from scraper import events_scraper
from scraper import data_importer

sched = BlockingScheduler()


@sched.scheduled_job('cron', hour=18, minute=41)
def scheduled_job():
    print('Job: Fetching events')
    events_scraper.get_events()

@sched.scheduled_job('cron', hour=2)
def scheduled_job():
    print('Job: Importing events')
    data_importer.do_import()


@sched.scheduled_job('interval', seconds=10)
def scheduled_job():
    print('dummy job')


sched.start()
