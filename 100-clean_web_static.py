#!/usr/bin/python3
# Distributes archives to web servers with do_deploy().
from fabric.api import *
from datetime import datetime
import os.path
import os

env.hosts = ["54.145.28.120", "35.229.33.79"]


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


def deploy():
    """Executes do_deploy & do_pack."""
    NewPath = do_pack()
    if not NewPath:
        return False
    else:
        return (do_deploy(NewPath))


def do_clean(number=0):
    """Deletes out-of-date archives."""
    number = 1 if int(number) == 0 else int(number)

    FileToClean = sorted(os.listdir("versions"))
    [FileToClean.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in FileToClean]

    with cd("/data/web_static/releases"):
        FileToClean = run("ls -tr").split()
        FileToClean = [a for a in FileToClean if "web_static_" in a]
        [FileToClean.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in FileToClean]
