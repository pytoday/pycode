#!/usr/bin/env python3
# coding=utf-8
# title          : tsUcint.py
# description    :
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/7/14 11:55
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
from socket import *

HOST = '127.0.0.1'
PORT = 12345
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpCli = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input(">")
    if not data:
        break
    udpCli.sendto(data.encode('utf-8'), ADDR)
    recdata, addr = udpCli.recvfrom(BUFSIZE)
    if not recdata:
        break
    print('rec message from server is: %s' % recdata.decode('utf-8'))

udpCli.close()
