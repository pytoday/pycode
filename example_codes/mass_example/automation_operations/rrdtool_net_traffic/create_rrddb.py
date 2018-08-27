#!/usr/bin/env python3
# coding=utf-8
# title          :create_rrddb.py
# description    :create a rrd database
# author         :JackieTsui
# organization   :pytoday.org
# date           :12/28/17 8:34 PM
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import rrdtool
import time


cur_time = str(int(time.time()))     # get current timestamp
# step: 300 second
rrd = rrdtool.create('Flow.rd', '--step', '300', '--start', cur_time,
                     # define data source eth0_in and eth0_out, data type counter, timeout 600s ,min:max = 0:U
                     'DS:eth0_in:COUNTER:600:0:U',
                     'DS:eth0_out:COUNTER:600:0:U',
                     # RRA format: [RRA:CF:xff:steps:rows]
                     # CF: consolidation function, xff: xff The xfiles factor
                     # defines what part of a consolidation interval may be made up from *UNKNOWN* data
                     # while the consolidated value is still regarded as known.
                     'RRA:AVERAGE:0.5:1:600',
                     'RRA:AVERAGE:0.5:6:700',
                     'RRA:AVERAGE:0.5:24:775',
                     'RRA:AVERAGE:0.5:288:797',
                     'RRA:MAX:0.5:1:600',
                     'RRA:MAX:0.5:6:700',
                     'RRA:MAX:0.5:24:775',
                     'RRA:MAX:0.5:444:797',
                     'RRA:MIN:0.5:1:600',
                     'RRA:MIN:0.5:6:700',
                     'RRA:MIN:0.5:24:775',
                     'RRA:MIN:0.5:444:797')
