#!/usr/bin/env python3
# coding=utf-8
# title          :socketServerPoll.py
# description    :
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/10/25 17:41
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import socket
import select


s = socket.socket()
host = ''
port = 1234
s.bind((host, port))

fdmap = {s.fileno(): s}

s.listen(5)
p = select.poll()
p.register(s)
while True:
    events = p.poll()
    for fd, event in events:
        if fd == s.fileno():
            c, addr = s.accept()
            print("Got connection from: ", addr)
            p.register(c)
            fdmap[c.fileno()] = c
        elif event & select.POLLIN:
            data = fdmap[fd].recv(1024)
            if not data:
                print(fdmap[fd].getpeername(), "disconnected")
                p.unregister(fd)
                del fdmap[fd]
            else:
                print(data)
