#!/usr/bin/python3
""" Deploy """
from datetime import datetime
import time
from fabric.api import local, run, put, sudo, env
from os import path
import os
env.hosts = ['35.231.210.244', '54.209.19.247']


def do_pack():
    """ pack my static"""
    timestamp = time.strftime("%Y%m%d%H%M%S")
    path1 = "versions/web_static_{}.tgz".format(timestamp)
    try:
        if not path.exists('versions'):
            local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(path1))
        return path1
    except Exception:
        return None


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


def deploy():
    """creates deploy"""
    path = do_pack()
    if path is None:
        return False
    print(path)
    res = do_deploy(path)
    return res
