from apscheduler.schedulers.blocking import BlockingScheduler

from scraper import events_scraper
from scraper import data_importer

sched = BlockingScheduler()


@sched.scheduled_job('cron', hour=13, minute=34)
def scheduled_job():
    events_scraper.get_events()

@sched.scheduled_job('cron', hour=2)
def scheduled_job():
    data_importer.do_import()


@sched.scheduled_job('interval', seconds=10)
def scheduled_job():
    print('dummy job')


sched.start()
