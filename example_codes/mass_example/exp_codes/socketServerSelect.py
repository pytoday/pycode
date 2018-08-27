#!/usr/bin/env python3
# coding=utf-8
# title          :socketServerSelect.py
# description    :socket server using select
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/10/25 17:17
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
s.listen(5)
inputs = [s]

while True:
    rs, ws, es = select.select(inputs, [], [])
    for r in rs:
        if r is s:
            c, addr = s.accept()
            print("Got connection from: ", addr)
            inputs.append(c)
        else:
            try:
                data = r.recv(1024)
                disconnected = not data
            except socket.error:
                disconnected = True
            if disconnected:
                print(r.getpeername(), "disconnected")
                inputs.remove(r)
            else:
                print(data)
