#!/usr/bin/env python3
# coding=utf-8
# title          :pxssh_use.py
# description    :
# author         :JackieTsui
# organization   :pytoday.org
# date           :1/15/18 10:40 PM
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
from pexpect import pxssh
import getpass


try:
    s = pxssh.pxssh()       # create a pxssh object
    hostname = input("Please input hostname: ")
    username = input("Please input username: ")
    password = getpass.getpass("please input password: ")
    s.login(hostname, username, password)       # connect to server
    s.sendline('uptime')    # run uptime
    s.prompt()
    print(s.before, s.after)
    s.logout()
except pxssh.ExceptionPxssh as e:
    print("pxssh failed on login with error: " + str(e))
