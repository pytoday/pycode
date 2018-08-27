#!/usr/bin/env python3
# coding=utf-8


def isphnumber(msg):
    if len(msg) != 12:
        return False
    for i in range(0, 3):
        if not msg[i].isdecimal():
            return False
    if msg[3] != '-':
        return False
    for i in range(4, 7):
        if not msg[i].isdecimal():
            return False
    if msg[7] != '-':
        return False
    for i in range(8, 12):
        if not msg[i].isdecimal():
            return False
    return True

message = input("Pls input something, I'll tell text contain phone number or not.")
for i in range(len(message)):
    chunck = message[i:i+12]
    if isphnumber(chunck):
        print("Find phone number:" + chunck)

print("All DONE.")