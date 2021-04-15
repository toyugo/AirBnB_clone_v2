#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
from the contents of the web_static folder of your AirBnB Clone repo:

- Prototype: def do_pack():
- All files in the folder web_static must be added to the final archive
- All archives must be stored in the folder versions
  (your function should create this folder if it doesnt exist)
- The name of the archive created must be :
  web_static_<year><month><day><hour><minute><second>.tgz
- Function do_pack must RETURN the archive path if the archive
  has been correctly generated; otherwise, return None
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates a .tgz archive"""
    t = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    result = local(
            "tar -cvzf versions/web_static_{:s}.tgz web_static".format(t))

    if result.succeeded:
        return "versions/web_static_{:s}.tgz".format(t)
    else:
        return None
