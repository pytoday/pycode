#!/usr/bin/env python3
# coding=utf-8
# title          :remove_duplicate_ip.py
# description    :
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/12/25 13:29
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import sys

if len(sys.argv) < 3:
    print("arg too short.\nUsage: remove_duplicate_ip.py /path/to/infile.txt /path/to/outfile.txt")
    sys.exit()

input_file = sys.argv[1]
output_file = sys.argv[2]

ips = []
with open(input_file, 'r') as f:
    lines = f.readlines()
    for line in lines:
        tmp_line = line.strip('\n').split(' ')
        if len(tmp_line) > 1:
            for i in tmp_line:
                ips.append(i)
        else:
            ips.append(line.strip('\n'))

out = list(set(ips))

with open(output_file, 'w') as f1:
    for j in out:
        f1.write(j+'\n')
