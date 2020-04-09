#!/usr/bin/python3
# Generates .tgz archive from web_static folder of AirBnB Clone repo, using do_pack().
from fabric.api import *
from datetime import datetime
import os.path


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    DateTime = datetime.utcnow()
    File = "versions/web_static_{}{}{}{}{}{}.tgz".format(DateTime.year,
                                                         DateTime.month,
                                                         DateTime.day,
                                                         DateTime.hour,
                                                         DateTime.minute,
                                                         DateTime.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(File)).failed is True:
        return None
    return File
