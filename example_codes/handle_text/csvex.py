#!/usr/bin/env python3
# coding=utf-8
# title          : csvex.py
# description    :
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/9/29 18:56
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import csv


data = (
    (9, 'web client', 'base64', 'urllib'),
    (10, 'django', 'text', 'file'),
)

print('***Handle csv file***')
with open('csvdata.csv', 'w') as f:
    writer = csv.writer(f)
    for i in data:
        writer.writerow(i)

print('***data saved***')
with open('csvdata.csv', 'r') as f:
    reader = csv.reader(f)
    for num, desc, type, type1 in reader:
        print('%s\t%s\t%s\t%s' % (num, desc, type, type1))
