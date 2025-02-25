#!/usr/bin/python3
""" Fabric script that generates a .tgz archive
 from the contents of the web_static folder of
 my AirBnB Clone repo, using the function do_pack"""
from datetime import datetime
from fabric.api import local
import os.path


def do_pack():
    """ main function"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        file = "version/web_static_{}.tgz".format(date)
        if os.path.isdir("versions") is False:
            local("mkdir versions")
        local("tar -cvzf {} web_static_".format(file))
        return file
    except:
        return None
