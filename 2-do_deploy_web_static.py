""" Deploy """
from datetime import datetime
from fabric.api import local, run, put, sudo, env
from os import path
import os
env.hosts = ['35.231.210.244', '54.209.19.247']


def do_deploy(archive_path):
    """ distributes"""
    if not path.isfile(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        dirpath = archive_path.split("/")[1].split(".")[0]
        sudo("mkdir -p /data/web_static/releases/{}/".format(dirpath))
        filepath = archive_path.split("/")[1]
        datapath = "/data/web_static/releases/{}".format(dirpath)
        sudo("tar -xvzf /tmp/{} -C {}".format(filepath, datapath))
        sudo("rm -rf /tmp/{}".format(filepath))
        sudo("mv {}/web_static/* {}".format(datapath, datapath))
        sudo("rm -rf {}/web_static".format(datapath))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s {} /data/web_static/current".format(datapath))
        return True
    except Exception:
        return False
