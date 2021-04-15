""" Deploy """
""" fab -f 2-do_deploy_web_static.py do_deploy:archive_path=versions/web_static_20210415190906.tgz -i my_ssh_private_key -u ubuntu"""
# curl 35.231.210.244/hbnb_static/0-index.html
from datetime import datetime
from fabric.api import local, run, put, sudo, env
from os import path
env.hosts = ['35.231.210.244', '54.209.19.247']


def do_deploy(archive_path):
    """ distributes an archive to web servers"""
    print("start")
    if not path.isfile(archive_path):
        print("FAUX")
        return False
    #try:
        """put(archive_path, "/tmp/")
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
        print("OK")
        return True"""
    #except Exception:
    #    print("false")
    #    return False
    