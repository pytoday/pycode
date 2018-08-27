#!/usr/bin/env python3
# coding=utf-8
# title          : tsTserverSS.py
# description    :
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/7/14 13:25
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
from socketserver import TCPServer, StreamRequestHandler
from time import ctime


HOST = ''
PORT = 12345
ADDR = (HOST, PORT)


class MyRequstHandle(StreamRequestHandler):
    def handle(self):
        print('...connected from:', self.client_address)
        self.wfile.write(ctime().encode('utf-8') + self.rfile.readline())


tcpServ = TCPServer(ADDR, MyRequstHandle)
print("waiting for connection...")
tcpServ.serve_forever()
