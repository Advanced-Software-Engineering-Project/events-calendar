from apscheduler.schedulers.blocking import BlockingScheduler
import logging

from scraper.events_scraper import EventsScraper
from scraper.data_importer import DataImporter
from scraper.data_cleaner import DataCleaner

sched = BlockingScheduler()
logging.basicConfig()


# Note on times: Our Heroku instance in five hours ahead of us

@sched.scheduled_job('cron', hour=6, minute=30)
def scheduled_job():
    print('Job: Fetching events')
    EventsScraper(None).get_events()


@sched.scheduled_job('cron', hour=7, minute=30)
def scheduled_job():
    print('Job: Importing events')
    data_importer = DataImporter(None)
    data_importer.import_groups('scraper/data/pages_data_3.json')
    data_importer.import_events('scraper/data/events_data.json')


@sched.scheduled_job('cron', hour=8, minute=30)
def scheduled_job():
    print('Job: Cleaning up old events')
    DataCleaner(None).do_clean()


sched.start()
