#!/usr/bin/env python3
# coding=utf-8
# title          :fabric_lnmp.py
# description    :deploy lnmp using fabric
# author         :JackieTsui
# organization   :pytoday.org
# date           :1/23/18 9:04 PM
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
from fabric.colors import *
from fabric.api import *


env.user = "root"
env.roledefs = {
    "webserver": ['192.168.10.100', '192.168.100.1'],
    "dbserver": ["192.168.1.23", "192.168.10.101"]
}
env.passwords = {
    "root@192.168.10.100": "123456",
    "root@192.168.10.101": "123456"
}


@roles("dbserver")
def dbtask():
    print(yellow("Install mysql...."))
    with settings(warn_only=True):
        run("yum install -y mysql-server mysql")
        run("checkconfig mysqld on")


@roles("webserver")
def webtask():
    print(yellow("Iinstall nginx php php-fpm..."))
    with settings(warn_only=True):
        run("yum install -y nginx")
        run("yum install -y php php-fpm php-xml php-gd")
        run("checkconfig nginx on; checkconfig php-fpm on")


@roles("dbserver", "webserver")
def publictask():
    print(yellow("Install epel ntp.."))
    with settings(warn_only=True):
        run("rpm -Uvh http://xxx/path/to/epel.rpm")
        run("yum install -y ntp")


def deploy():
    execute(publictask)
    execute(dbtask)
    execute(webtask)
