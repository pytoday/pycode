#!/usr/bin/env python3
# coding=utf-8
# title          :fabric_deploy.py
# description    :
# author         :JackieTsui
# organization   :pytoday.org
# date           :1/23/18 10:03 PM
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
from fabric.api import *
from fabric.colors import *
from fabric.context_managers import *
from fabric.contrib.console import confirm
import time


env.user = "root"
env.hosts = ['192.168.10.1', '192.168.10.11']
env.password = "123456"

env.project_dev_source = "/data/dev/webadmin"   # env used to define global var
env.project_tar_source = "/data/dev/release"
env.project_pack_name = "release"

env.deploy_project_root = "/data/www/webadmin"
env.deploy_release_dir = "releases"
env.deploy_current_dir = "current"
env.deploy_version = time.strftime("%Y%m%d") + "v2"


@runs_once
def input_versionid():
    return prompt("please input project roll back version ID: ", default="")


@task
@runs_once
def tar_source():   # package local dir
    print(yellow("Creating source package..."))
    with lcd(env.project_dev_source):
        local("tar -czf %s.tar.gz ." % (env.project_tar_source + env.project_pack_name))
    print(green("Creating package success!"))


@task
def put_package():
    print(yellow("Start put package..."))
    with settings(warn_only=True):
        with cd(env.deploy_project_root + env.deploy_release_dir):
            run("mkdir %s" % env.deploy_version)
    env.deploy_full_path = env.deploy_project_root + env.deploy_release_dir + "/" + env.deploy_version

    with settings(warn_only=True):
        result = put(env.project_tar_source + env.project_pack_name + ".tar.gz", env.deploy_full_path)
    if result.failed and not confirm("put file failed, Continue[Y/N]?"):
        abort("Aborting file put task")

    with cd(env.deploy_full_path):      # depress tar file
        run("tar -zxvf %s.tar.gz" % env.project_pack_name)
        run("rm -rf %s.tar.gz" % env.project_pack_name)
    print(green("Put & untar package success."))


@task
def make_symlink():
    print(yellow("update current symlink."))
    env.deploy_full_path = env.deploy_project_root + env.deploy_release_dir + "/" + env.deploy_version
    with settings(warn_only=True):
        run("rm -rf %s" % (env.deploy_project_root + env.deploy_current_dir))
        run("ln -s %s %s" % (env.deploy_full_path, env.deploy_project_root + env.deploy_current_dir))
        print(green("make symlink success!"))


@task
def rollback():
    print(yellow("rollback package version."))
    versionid = input_versionid()
    if versionid == "":
        abort("project version id error. abort.")
    env.deploy_full_path = env.deploy_project_root + env.deploy_release_dir + "/" + versionid
    run("rm -f %s" % (env.deploy_project_root + env.deploy_release_dir + "/" + versionid))
    run("ln -s %s %s" % (env.deploy_full_path, env.deploy_project_root + env.deploy_current_dir))
    print(green("rollback success!"))


@task
def go():
    tar_source()
    put_package()
    make_symlink()
