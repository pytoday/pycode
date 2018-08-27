#!/usr/bin/env python3
# coding=utf-8
# title          : tsUserv.py
# description    :
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/7/14 11:34
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
from socket import *
from time import ctime


HOST = ''
PORT = 12345
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpServer = socket(AF_INET, SOCK_DGRAM)
udpServer.bind(ADDR)

while True:
    print("waiting for messages:")
    data, addr = udpServer.recvfrom(BUFSIZE)
    if not data:
        break
    else:
        print("recv message is %s:" % data.decode('utf-8'))
        udpServer.sendto(('['+ctime()+']: ').encode('utf-8'), addr)
        print("message send.")
udpServer.close()

