from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

env.hosts = ['jasonrhaas.com']

def commit():
    local("git add -p && git commit")

def push():
    local("git push")

def prep():
    commit()
    push()

def deploy():
	code_dir = '~/repos/jhaas-web'
	with cd(code_dir):
		run("git pull")