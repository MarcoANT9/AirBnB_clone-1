#!/usr/bin/python3
# Distributes archives to web servers with do_deploy().
from fabric.api import *
from datetime import datetime
import os.path

env.hosts = ["54.145.28.120", "35.229.33.79"]


def do_deploy(archive_path):
    """Deploys static archive to web servers."""
    if os.path.isfile(archive_path) is False:
        return False
    Path = archive_path.split("/")[-1]
    Name = Path.split(".")[0]

    if put(archive_path, "/tmp/{}".format(Path)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(Name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(Name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(Path, Name)).failed is True:
        return False
    if run("rm /tmp/{}".format(Path)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(Name, Name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(Name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(Name)).failed is True:
        return False
    print("\nNew Version Successfuly Deployed!\n")
    return True
