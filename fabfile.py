from fabric.api import local
from distutils.util import strtobool

def deploy(skip_tests):
    if skip_tests:
        skip_tests = bool(strtobool(skip_tests))
    if not skip_tests:
        local("python server/test_app.py")
    local("git add -p && git commit --allow-empty")
    local("git push heroku master:master")