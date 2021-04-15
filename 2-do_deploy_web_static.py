#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to your web servers :

- Prototype: def deploy():
- Call the do_pack() function and store the path of the created archive
- Return False if no archive has been created
- Call the do_deploy(archive_path) function, using
  the new path of the new archive
- Return the return value of do_deploy
- All remote commands must be executed on both of web your servers
  using env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script
- Deploy the script on your servers: xx-web-01 and xx-web-02
"""

from fabric.api import *
from fabric.api import env
import os.path
from os.path import exists
env.hosts = ['35.190.132.204', '34.75.103.223']


def do_deploy(archive_path):
    """Creates and distributes an archive to my web servers"""
#   if not os.path.isfile(archive_path):
#       return False
#    if exists(archive_path) is False:
#        return False

    try:
        path = '/data/web_static/releases/'
        filename = archive_path.split('/')[-1]
        filename_no_ext = filename.split('.')[0]

        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, filename_no_ext))
        run('tar -xzf /tmp/{} -C {}{}'.format(
                    filename, path, filename_no_ext))
        run('rm /tmp/{}'.format(filename))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, filename_no_ext))
        run('rm -rf {}{}/web_static'.format(path, filename_no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{} /data/web_static/current'.format(
                    path, filename_no_ext))
        return True
    except:
        return False
