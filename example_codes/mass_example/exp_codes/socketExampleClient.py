#!/usr/bin/env python3
# coding=utf-8
# title          :socketExampleClient.py
# description    :
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/10/24 12:00
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import socket


host = '127.0.0.1'
port = 1234
bufsize = 1024
input_data = "some things."

s = socket.socket()
s.connect((host, port))
data = s.recv(bufsize)
print("Recv things on client side: ", data.decode('utf-8'))
s.send(input_data.encode('utf-8'))
