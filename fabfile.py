from fabric.api import local

def deploy():
    # local("python server/test_app.py")
    local("git add -p && git commit --allow-empty")
    local("git push heroku master:master")