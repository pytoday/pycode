#!/usr/bin/env python3
# coding=utf-8
# title          :curl_monitor_web.py
# description    :monitor web using libcurl
# author         :JackieTsui
# organization   :pytoday.org
# date           :12/22/17 5:29 PM
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import os
import sys
import pycurl


URL = "www.pytoday.org"

c = pycurl.Curl()
c.setopt(pycurl.URL, URL)   # define request url
c.setopt(pycurl.CONNECTTIMEOUT, 5)  # time out waiting to request connection
c.setopt(pycurl.TIMEOUT, 5)     # request time out
c.setopt(pycurl.NOPROGRESS, 1)  # download progress bar
c.setopt(pycurl.FORBID_REUSE, 1)    # forbid reuse
c.setopt(pycurl.MAXREDIRS, 5)   # max redirection
c.setopt(pycurl.DNS_CACHE_TIMEOUT, 60)  # dns cache timeout

# create content obj
indexfile = open(os.path.dirname(os.path.realpath(__file__))+"/content.txt", "wb")
c.setopt(pycurl.WRITEHEADER, indexfile)
c.setopt(pycurl.WRITEDATA, indexfile)

try:
    c.perform()
except Exception as e:
    print("connection error: " + str(e))
    indexfile.close()
    sys.exit()

NAMELOOKUP_TIME = c.getinfo(c.NAMELOOKUP_TIME)
CONNECT_TIME = c.getinfo(c.CONNECT_TIME)
PRETRANSFER_TIME = c.getinfo(c.PRETRANSFER_TIME)
STARTTRANSFER_TIME = c.getinfo(c.STARTTRANSFER_TIME)
TOTAL_TIME = c.getinfo(c.TOTAL_TIME)
HTTP_CODE = c.getinfo(c.HTTP_CODE)
SIZE_DOWNLOAD = c.getinfo(c.SIZE_DOWNLOAD)
HEADER_SIZE = c.getinfo(c.HEADER_SIZE)
SPEED_DOWNLOAD = c.getinfo(c.SPEED_DOWNLOAD)


# output result
print("HTTP CODE: %s" % HTTP_CODE)
print("DNS RESOLVE TIME: %.3f ms" % (NAMELOOKUP_TIME*1000))
print("CONNECT TIME: %.3f ms" % (CONNECT_TIME*1000))
print("PRETRANSFER TIME: %.3f ms" % (PRETRANSFER_TIME*1000))
print("STARTTRANSFER TIME: %.3f ms" % (STARTTRANSFER_TIME*1000))
print("TOTAL TIME: %.3f ms" % (TOTAL_TIME*1000))
print("DOWNLOAD SIZE: %d byte" % SIZE_DOWNLOAD)
print("HTTP HEADER SIZE: %d byte" % HEADER_SIZE)
print("DOWNLOAD SPEED: %d bytes/s" % SPEED_DOWNLOAD)
indexfile.close()
c.close()
