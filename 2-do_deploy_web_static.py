""" Deploy """
# fab -f 2-do_deploy_web_static.py do_deploy:archive_path=versions/web_static_20210415190906.tgz -i ~/.ssh/id_rsa -u ubuntu
# ~/.ssh/id_rsa

from datetime import datetime
from fabric.api import local, run, put, sudo, env
from os import path
import os
env.hosts = ['35.231.210.244', '54.209.19.247']

def do_deploy(archive_path):
    """ distributes an archive to web servers"""
    print("start")
    if not path.isfile(archive_path):
        return False
    try:
        archive_ext = archive_path.split("/")
        res = put(archive_path, "/tmp/{}".format(archive_ext[1]))
        archive = archive_ext[1].split(".")
        res = run("mkdir -p /data/web_static/releases/{}/".format(archive[0]))
        res = run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
                .format(archive_ext[1], archive[0]))
        res = run("rm /tmp/{}".format(archive_ext[1]))
        res = run("mv /data/web_static/releases/{}/web_static/* \
        /data/web_static/releases/{}/".format(archive[0], archive[0]))
        res = run("rm -rf /data/web_static/releases/{}/web_static"
                .format(archive[0]))
        res = run("rm -rf /data/web_static/current")
        res = run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
                .format(archive[0]))
        print('New version deployed!')
        return True
    except Exception:
        return False