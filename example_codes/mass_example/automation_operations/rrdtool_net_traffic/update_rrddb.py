#!/usr/bin/env python3
# coding=utf-8
# title          :update_rrddb.py
# description    :update database of rrdtool
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/12/29 1:37
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import rrdtool
import time
import psutil


total_in_traffic = psutil.net_io_counters()[1]      # traffic input
total_out_traffic = psutil.net_io_counters()[0]     # traffic output
starttime = int(time.time())    # get current unix timestamp

update = rrdtool.updatev('Flow.rd', '%s:%s:%s' % (str(starttime), str(total_in_traffic), str(total_out_traffic)))
print(update)
