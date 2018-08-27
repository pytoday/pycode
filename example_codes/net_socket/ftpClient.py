#!/usr/bin/env python3
# coding=utf-8
# title          : ftpClient.py
# description    :
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/7/17 0:59
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import os, socket
import ftplib


HOST = 'ftp.mozillia.org'
DIRN = 'pub/mozilla.org/webtools'
FILE = 'bugzilla-last.tar.gz'


def main():
    try:
        f = ftplib.FTP(HOST)
    except (socket.error, socket.gaierror) as e:
        print('Can\'t connected to host %s' % HOST)
        return
    print("Connected to host %s:" % HOST)

    try:
        f.login()
    except ftplib.error_perm:
        print("Login failed. may be wrong user or password.")
        f.quit()
    print("***Logged in as 'anonymous'")

    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print("Cannot cd to %s" % DIRN)
        f.quit()
        return
    print("***Changed to %s folder" % DIRN)

    try:
        f.retrbinary('RETR %s' % FILE, open(FILE, 'wb'.write))
    except ftplib.error_perm:
        print("cannot read file %s" % FILE)
        os.unlink(FILE)
    else:
        print("***Download %s to CWD" % FILE)
    finally:
        f.quit()


if __name__ == "__main__":
    main()
