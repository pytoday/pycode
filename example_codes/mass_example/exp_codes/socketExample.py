#!/usr/bin/env python3
# coding=utf-8
# title          :socketExample.py
# description    :socket example code for server side
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/10/24 11:46
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import socket


host = '127.0.0.1'
port = 1234
bufsize = 1024
input_data = "Thanks for connecting..."

s = socket.socket()
s.bind((host, port))
s.listen(3)
while True:
    c, addr = s.accept()
    print("Got connecting from ", addr)
    c.send(input_data.encode('utf-8'))
    data = c.recv(bufsize)
    print("Recv things on server side: ", data.decode('utf-8'))

