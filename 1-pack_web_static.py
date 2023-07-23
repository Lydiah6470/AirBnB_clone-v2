#!/usr/bin/python3
# Fabfile to generates a .tgz archive from the contents of web_static.
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    dt = datetime.utcnow()
    archive_name = "web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                       dt.month,
                                                       dt.day,
                                                       dt.hour,
                                                       dt.minute,
                                                       dt.second)
    archive_path = "versions/{}".format(archive_name)

    if not os.path.exists("versions"):
        os.makedirs("versions")

    command = "tar -czvf {} web_static".format(archive_path)
    result = local(command)

    if result.failed:
        return None

    return archive_path
