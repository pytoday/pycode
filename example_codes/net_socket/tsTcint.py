#!/usr/bin/env python3
# coding=utf-8
# title          : tsTcint.py
# description    :
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/7/13 23:06
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
from socket import *


HOST = '127.0.0.1'
PORT = 12345
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpcli = socket(AF_INET, SOCK_STREAM)
tcpcli.connect(ADDR)

while True:
    data = input('>')
    if not data:
        break
    tcpcli.send(data.encode('utf-8'))
    recdata = tcpcli.recv(BUFSIZE)
    if not recdata:
        break
    print(recdata.decode('utf-8'))

tcpcli.close()
