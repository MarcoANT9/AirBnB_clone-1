#!/usr/bin/python3
""" This function generates a compressed file. """
from fabric.api import local
from datetime import datetime


def do_pack():
    """ This function creates a .tgz file. """
    local("mkdir -p versions")
    time = datetime.now()
    compresed_file = "versions/web_static_"
    compresed_file += "{}{}{}".format(time.year, time.month, time.day)
    compresed_file += "{}{}{}".format(time.hour, time.minute, time.second)
    compresed_file += ".tgz"
    compresed = "tar -cvzf "
    compresed += compresed_file
    compresed += " web_static"
    if local(compresed) == 1:
        return None
    return compresed_file
