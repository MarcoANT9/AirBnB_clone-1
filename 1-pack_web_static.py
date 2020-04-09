#!/usr/bin/python3
# Generates .tgz archive from web_static folder of AirBnB Clone repo, using do_pack().
from fabric.api import *
from datetime import datetime
import os.path


def do_pack():
    """Create a .tgz file with web_static's content."""
    DateTime = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    File = local('tar -czvf versions/web_static_{}.tgz web_static'
                   .format(now))
    if File.failed:
        return None
    else:
        return File
