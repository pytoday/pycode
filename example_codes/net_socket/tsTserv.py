#!/usr/bin/env python3
# coding=utf-8
# title          : tsTserv.py
# description    :
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/7/13 22:33
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
from socket import *
from time import ctime


HOST = ''
PORT = 12345
BUFFSIZE = 1024
ADDR = (HOST, PORT)

tcpsock = socket(AF_INET, SOCK_STREAM)
tcpsock.bind(ADDR)
tcpsock.listen(5)

while True:
    print("waiting for connecting...")
    tcpcli, addr = tcpsock.accept()
    print("connected from: ", addr)

    while True:
        data = tcpcli.recv(BUFFSIZE)
        if not data:
            break
        tcpcli.send(('Current time: '+ctime()+'\n').encode('utf-8') + data)
    tcpcli.close()

