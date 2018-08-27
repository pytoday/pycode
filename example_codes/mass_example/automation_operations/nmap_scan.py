#!/usr/bin/env python3
# coding=utf-8
# title          :nmap_scan.py
# description    :python-nmap scan example
# author         :JackieTsui
# organization   :pytoday.org
# date           :2018/1/12 5:32
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import sys
import nmap


input_data = input("Please input hosts and ports: ")
scan_row = input_data.split(" ")
if len(scan_row) != 2:
    print("Input errors, example \"192.168.0/24 80,443,22\"")
    sys.exit()

hosts = scan_row[0]
port = scan_row[1]

try:
    nm = nmap.PortScanner()     # create a port scanner instance
except nmap.nmap.PortScannerError:
    print("Nmap not foud", sys.exc_info()[0])
    sys.exit()
except Exception:
    print("Unexpected error: ", sys.exc_info()[0])
    sys.exit()

try:
    nm.scan(hosts=hosts, arguments='-v -sS -p'+port)
except Exception as e:
    print("Scan error: " + str(e))

for host in nm.all_hosts():     # scan all hosts
    print("---------------------------")
    print("Host: %s (%s)" % (host, nm[host].hostname()))        # show hostname and port
    print("State: %s" % nm[host].state())

    for proto in nm[host].all_protocols():
        print("-----------------------------")
        print("Protocol: %s" % proto)
        lport = nm[host][proto].keys()
        ports = list(lport)
        ports.sort()
        for port in ports:
            print("Port: %s\tState: %s" % (port, nm[host][proto][port]['state']))
