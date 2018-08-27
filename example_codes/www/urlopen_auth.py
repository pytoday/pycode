#!/usr/bin/env python3
# coding=utf-8
# title          : urlopen_auth.py
# description    :
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/8/17 14:07
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import urllib.request, urllib.error, urllib.parse


LOGIN = 'wesley'
PASSWD = "you'llNeverGuess"
URL = 'http://localhost'
REALM = 'Secure Archive'


def handler_version(url):
    hdlr = urllib.request.HTTPBasicAuthHandler()
    hdlr.add_password(REALM, urllib.parse.urlparse(url)[1], LOGIN, PASSWD)
    opener = urllib.request.build_opener(hdlr)
    urllib.request.install_opener(opener)
    return url


def request_version(url):
    from base64 import encodebytes
    req = urllib.request.Request(url)
    b64str = encodebytes(bytes('%s:%s' % (LOGIN, PASSWD), 'utf-8'))[:-1]    # remove \n
    req.add_header("Authorization", "Basic %s" % b64str)
    return req


for func in ('handler', 'request'):
    print("*** Using %s:" % func.upper())
    url = eval('%s_version' % func)(URL)
    f = urllib.request.urlopen(url)
    print(str(f.readline(), 'utf-8'))
    f.close()
