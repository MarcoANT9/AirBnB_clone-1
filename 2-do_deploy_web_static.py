#!/usr/bin/python3
""" This function generates a compressed file. """
from fabric.api import *
from os import path
from datetime import datetime
from shlex import split


env.host = ["35.243.187.246", "54.234.253.58"]


def do_deploy(archive_path):
    if not path.exists(archive_path) or (path.exists(archive_path) and
                                         path.isdir(archive_path)):
        return False
    try:
        put(archive_path, "/tmp/")
        file_name = archive_path.split("/")[1]
        file_name2 = file_name.split(".")[0]
        mk_dir = "mkdir -p /data/web_static/releases/{}".format(file_name2)
        sudo(mk_dir)
        uncompres = "tar -xzf /tmp/{}".format(file_name)
        uncompres += " -C data/web_static/releases/{}".format(file_name2)
        sudo(uncompres)
        rm_var = "rm /tmp/{}".format(file_name)
        sudo(rm_var)
        mv_var = "mv /data/web_static/releases/"
        mv_var += "{}/web_static/*".format(file_name2)
        mv_var += " /data/web_static/releases/{}/".format(file_name2)
        sudo(mv_var)
        rm_dir = "rm -rf /data/web_static/releases/{}".format(file_name2)
        rm_dir += "/web_static"
        sudo(rm_dir)
        sudo("rm -rf /data/web_static/current")
        sym_link = "ln -s /data/web_static/releases/{}/".format(file_name2)
        sym_link += " /data/web_static/current"
        sudo(sym_link)
        print("New version deployed!")
        return True
    except Exception:
        return False
