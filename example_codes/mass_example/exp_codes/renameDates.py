#!/usr/bin/env python3
# coding=utf-8
# title          :renameDates.py
# description    :
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/5/13 14:32:06
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import os
import re
import shutil

# Create regex for date format.
dateRe = re.compile('''
^(.*?)              #all text before date 
((0|1)?\d)-         #one or two digit for month
((0|1|2|3)?\d)-     #one or two digit for day
((19|20)\d\d)       #four digit for year
(.*?)$              #all text after date
''', re.VERBOSE)
# TODO: Loop over the files in wording directory
for filename in os.listdir('.'):
    m = dateRe.search(filename)
    
    # TODO: Skip files without a date
    if m == None:
        continue

    # TODO: Get the different parts of the filename
    beforePart = m.group(1)
    monPart = m.group(2)
    dayPart = m.group(4)
    yearPart = m.group(6)
    afterPart = m.group(8)

    new_filename = beforePart + dayPart + '-' + monPart + '-' + yearPart + afterPart

    # TODO: Get full path and file name
    absPath = os.path.abspath('.')
    filename = os.path.join(absPath, filename)
    new_filename = os.path.join(absPath, new_filename)

    # TODO: Rename file
    shutil.move(filename, new_filename)
    print('Rename filename from %s to %s.' % (filename, new_filename))