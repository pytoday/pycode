#!/usr/bin/env python3
# coding=utf-8
# title          :clamav_scan.py
# description    :scan hosts with clamd
# author         :JackieTsui
# organization   :pytoday.org
# date           :2018/1/12 3:55
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import time
import pyclamd
from threading import Thread


class Scan(Thread):
    def __init__(self, ip, scan_type, file):
        """param init"""
        Thread.__init__(self)
        self.ip = ip
        self.scan_type = scan_type
        self.connstr = ""
        self.scanresult = ""

    def run(self):
        """multiple process run"""
        try:
            cd = pyclamd.ClamdNetworkSocket(self.ip, 3310)      # create a socket object
            if cd.ping():   # ping check
                self.connstr = self.ip + " connection [OK]"
                cd .reload()
            if self.scan_type == "contscan_file":   # chose scan mode
                self.scanresult = "{0}\n".format(cd.contscan_file(self.file))
            elif self.scan_type == "multiscan_file":
                self.scanresult = "{0}\n".format(cd.multiscan_file(self.file))
            elif self.scan_type == "scan_file":
                self.scanresult = "{0}\n".format(cd.scan_file(self.file))
                time.sleep(1)   # wait thread
            else:
                self.connstr = self.ip + " ping error, exit"
                return
        except Exception as e:
            self.connstr = self.ip + " " + str(e)


IPs = ['192.168.10.1', '192.168.10.2']
scantype = "multiscan_file"
scanfile = "/data/www"
scanlist = []
i = 1
threadnum = 2
for ip in IPs:
    currp = Scan(ip, scantype, scanfile)
    scanlist.append(currp)
    if i % threadnum == 0 or i == len(IPs):
        for task in scanlist:
            task.start()
        for task in scanlist:
            task.join()
            print(task.connstr, task.scanresult)
        scanlist = []
    i += 1
