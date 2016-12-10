from apscheduler.schedulers.blocking import BlockingScheduler

from scraper.events_scraper import EventsScraper
from scraper.data_importer import DataImporter
from scraper.data_cleaner import DataCleaner

sched = BlockingScheduler()


# Note on times: Our Heroku instance in five hours ahead of us

@sched.scheduled_job('cron', hour=6, minute=30)
def scheduled_job():
    print('Job: Fetching events')
    EventsScraper(None).get_events()

@sched.scheduled_job('cron', hour=7, minute=30)
def scheduled_job():
    print('Job: Importing events')
    DataImporter(None).import_events()

@sched.scheduled_job('cron', hour=8, minute=30)
def scheduled_job():
    print('Job: Cleaning up old events')
    DataCleaner(None).do_clean()


sched.start()
