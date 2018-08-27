#!/usr/bin/env python3
# coding=utf-8
# title          :socketServerFork.py
# description    :socket server can forking
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/10/25 11:15
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
from socketserver import TCPServer, StreamRequestHandler, ForkingMixIn


host = '127.0.0.1'
port = 1234


class Server(ForkingMixIn, TCPServer):
    pass


class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print("Got connection from: ", addr)
        self.wfile.write("Thank you for connecting...".encode('utf-8'))


server = Server((host, port), Handler)
server.serve_forever()
