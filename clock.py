from apscheduler.schedulers.blocking import BlockingScheduler

from scraper import events_scraper
from scraper import data_importer

sched = BlockingScheduler()


@sched.scheduled_job('cron', day_of_week='mon-sun', hour=1)
def scheduled_job():
    events_scraper.get_events()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=2)
def scheduled_job():
    data_importer.do_import()




# test
# @sched.scheduled_job('interval', id='get_events', minutes=2)
# def scheduled_job():
#     events_scraper.get_events()
#
# @sched.scheduled_job('interval', id='import', minutes=2)
# def scheduled_job():
#     data_importer.do_import()




sched.start()
