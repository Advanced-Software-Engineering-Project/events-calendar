from fabric.api import *
from fabric.context_managers import cd
from distutils.util import strtobool

env.use_ssh_config = True


def deploy(skip_tests=False):
    if skip_tests:
        skip_tests = bool(strtobool(skip_tests))
    if not skip_tests:
        with cd('/Users/ianjohnson/Desktop/Columbia/Advanced Software Engineering/events-calendar/server'):
            local("pwd")
            local("python test_app.py")
    local("git add -p && git commit --allow-empty")
    local("git push heroku master:master")


# from fabric.api import local, run
# from fabric.context_managers import cd
# from distutils.util import strtobool
#
# def deploy(skip_tests=False):
#     if skip_tests:
#         skip_tests = bool(strtobool(skip_tests))
#     if not skip_tests:
#         with cd('/tmp'):
#             run("python test_app.py")
#     local("git add -p && git commit --allow-empty")
#     local("git push heroku master:master")