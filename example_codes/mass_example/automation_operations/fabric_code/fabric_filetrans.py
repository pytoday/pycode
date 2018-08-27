#!/usr/bin/env python3
# coding=utf-8
# title          :fabric_filetrans.py
# description    :fabric file transfer
# author         :JackieTsui
# organization   :pytoday.org
# date           :1/22/18 3:21 PM
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
from fabric.api import *
from fabric.context_managers import *
from fabric.contrib.console import confirm


env.user = "jackie"
env.hosts = "192.168.10.10"
# env.password = "123456"
env.key_filename = "~/.ssh/id_rsa"


@task
@runs_once
def tar_task():
    with lcd("/data/logs"):
        local("tar -czf access.tar.gz access.log")


@task
def put_task():
    run("mkdir -p /data/logs")
    with cd("/data/logs"):
        with settings(warn_only=True):
            result = put("/data/logs/access.tar.gz", "/data/logs/access.tar.gz")
        if result.failed and not confirm("put file failed, Continue[Y/N]?"):
            abort("Aborting file put task!")


@task
def check_task():
    with settings(warn_only=True):
        lmd5 = local("md5sum /data/logs/access.tar.gz", capture=True).split(" ")[0]
        rmd5 = run("md5sum /data/logs/access.tar.gz").split(" ")[0]
    if lmd5 == rmd5:
        print("OK")
    else:
        print("Error.")

