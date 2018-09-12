#!/usr/bin/env python3
# coding=utf-8
# title          : cgi_http.py
# description    : simple http server
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/9/12 16:31
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
# python -m CGIHTTPServer   # python2
from http.server import CGIHTTPRequestHandler, test


test(CGIHTTPRequestHandler)
