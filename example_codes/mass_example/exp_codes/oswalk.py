#!/usr/bin/env python3
# coding=utf-8
# title          :oswalk.py
# description    :
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/5/13 11:33:17
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import os
import shutil
import send2trash

for folderName, subfolders, fileNames in os.walk(os.getcwd()):
    print('Current folder is ' + folderName)
    for subfolder in subfolders:
        print('Subfolder of '+ folderName + ' is: ' + subfolder)
    for filename in fileNames:
        print('Subfolder of ' + folderName + ' is: ' + filename)
    print(' ')