#!/usr/bin/env python3
# coding=utf-8
# title          :IPy_module.py
# description    :example usage of module "IPy"
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/12/18 21:16
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
from IPy import IP


ip_s = '192.168.0.0/24'
ips = IP(ip_s)

if len(ips) > 1:
    print('net: %s' % ips.net())
    print('netmask: %s' % ips.netmask())
    print('broadcast: %s' % ips.broadcast())
    print('reverse address: %s' % ips.reverseNames()[0])
    print('subnet: %s' % len(ips))
else:
    print('reverse address: %s' % ips.reverseName())
print('hexadecimal: %s' % ips.strHex())
print('binary ip: %s' % ips.strBin())
print('iptype: %s' % ips.iptype())
