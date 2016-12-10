from fabric.api import *
from distutils.util import strtobool

env.use_ssh_config = True


def deploy(skip_tests=False):
    if skip_tests:
        skip_tests = bool(strtobool(skip_tests))

    if not skip_tests:
        local("pwd")
        local("python server/test_app.py")
        local("pwd")
        local("python scraper/test_events_scraper.py")
        local("python scraper/test_data_importer.py")
        local("python scraper/test_data_cleaner.py")

    local("git add -p && git commit --allow-empty")
    local("git push heroku master:master")

