#!/usr/bin/env python3
# coding=utf-8
# title          :highs_lows.py
# description    :
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/8/22 下午9:10
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script

import csv
from matplotlib import pyplot as plt
from datetime import datetime


filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # for index, column_header in enumerate(header_row):
    #   print(index, column_header)

    dates, highs, lows = [], [], []
    for row in reader:
        # datetime.strptime() convert str to datetime obj. strftime convert datetime obj to str
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        try:
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            highs.append(high)
            lows.append(low)
    # print(highs)

fig = plt.figure(dpi=128, figsize=(12, 6))
plt.plot(dates, highs, c='red', alpha=0.7)
plt.plot(dates, lows, c='blue', alpha=0.7)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.3)
plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperatures (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
