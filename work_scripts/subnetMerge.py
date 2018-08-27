#!/usr/bin/env python3
# coding=utf-8
# title          :subnetMerge.py
# description    :merge and combine subnet
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/11/28 18:25
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import sys
import ipcalc
import netaddr
from netaddr import IPNetwork

if len(sys.argv) < 3:
    print("Usage:subnetMerge.py inputFile outputFile")
    exit(0)

in_txt = sys.argv[1]
out_txt = sys.argv[2]
template = '1024\t6\t128\t1\t新加坡\t1000\t1024\t0\t128\t1\n'


def ip_list(file):
    for line in file:
        yield IPNetwork(line.strip())


with open(in_txt, 'r') as in_file:
    sum_list = netaddr.cidr_merge(ip_list(in_file))

with open(out_txt, 'w') as out_file:
    for net in sum_list:
        IP = ipcalc.Network(str(net))
        network = str(IP.network())
        broadcast = str(IP.broadcast())
        out_file.write(network+'\t'+broadcast+'\t'+template)
