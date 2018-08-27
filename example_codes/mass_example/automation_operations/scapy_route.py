#!/usr/bin/env python3
# coding=utf-8
# title          :scapy_route.py
# description    :get traceroute graph by scrapy
# author         :JackieTsui
# organization   :pytoday.org
# date           :12/29/17 5:38 PM
# email          :jackietsui72@gmail.com
# notes          :only support on unix-like
# ==================================================
# Import the module needed to run the script
# refer to :https://phaethon.github.io/scapy/api/usage.html
import time, subprocess
import warnings,logging
warnings.filterwarnings('ignore', category=DeprecationWarning)  # ignore scapy useless error
logging.getLogger('scapy.runtime').setLevel(logging.ERROR)      # ignore scapy ipv6 error
from scapy.all import *


domains = input('Please input one or more IP/domain(separated by blank space): ')
target = domains.split(' ')
dport = [80, 443]

if len(target) >= 1 and target[0]:
    res, unans = traceroute(target, dport=dport, maxttl=25, retry=-2)
    res.graph(target="getroute.svg")
    time.sleep(1)
    subprocess.Popen("/usr/bin/convert getroute.svg getroute.png", shell=True)
else:
    print('IP/domain error, exit.')
