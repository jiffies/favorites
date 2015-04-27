#-*-coding:utf-8-*-
import os,re
from datetime import datetime
from fabric.api import *

env.user = 'jiffies'
env.sudo_user = 'root'
env.hosts = ['121.40.194.92']

_TAR_FILE = 'dist-favorites.tar.gz'

def build():
    includes = ['favorites/*','requirements.txt','manager.py','wsgi.py','populate.py']
    excludes = ['*.pyc','*.swp']
    local('rm -f dist/%s' % _TAR_FILE)
    with lcd(os.path.abspath('.')):
        cmd = ['tar','-czvf','dist/%s' % _TAR_FILE]
        cmd.extend(['--exclude=\'%s\'' % ex for ex in excludes])
        cmd.extend(includes)
        local(' '.join(cmd))


_REMOTE_TMP_TAR = '/tmp/%s' % _TAR_FILE
_REMOTE_BASE_DIR = '/home/jiffies/python'

def deploy():
    newdir = 'www-%s' % datetime.now().strftime('%y-%m-%d_%H.%M.%S')
    run('rm -f %s' % _REMOTE_TMP_TAR)
    put('dist/%s' % _TAR_FILE, _REMOTE_TMP_TAR)

    with cd(_REMOTE_BASE_DIR):
        run('mkdir %s' % newdir)

    with cd('%s/%s' % (_REMOTE_BASE_DIR, newdir)):
        sudo('tar -xzvf %s' % _REMOTE_TMP_TAR)
    with cd(_REMOTE_BASE_DIR):
            sudo('rm -f www')
            sudo('ln -s %s www' % newdir)
            sudo('chown jiffies:jiffies www')
            sudo('chown -R jiffies:jiffies %s' % newdir)
    # 重启Python服务和nginx服务器:
    run('export FAVORITES_ENV=prod')
    with settings(warn_only=True):
        sudo('supervisorctl stop favorites')
        sudo('supervisorctl start favorites')
        sudo('/etc/init.d/nginx reload')



