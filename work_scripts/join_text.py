#!/usr/bin/env python3
# coding=utf-8
# title          : join_text.py
# description    :
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/8/1 11:37
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import sys


f1 = sys.argv[1]
f2 = sys.argv[2]


with open(f1) as fd1:
    fd1_list = fd1.readlines()

with open(f2) as fd2:
    fd2_list = fd2.readlines()

with open('allinfo.txt', 'w') as f:
    for i in range(len(fd1_list)):
        ip = fd1_list[i].split('\t')[0]
        for j in range(len(fd2_list)):
            ip2 = fd2_list[j].split('\t')[0]
            if ip2 == ip:
                f.write(fd1_list[i].rstrip('\n')+'\t'+fd2_list[j])

