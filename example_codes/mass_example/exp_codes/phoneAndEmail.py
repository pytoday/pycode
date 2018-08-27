#!/usr/bin/env python3
# coding=utf-8
# phoneAndEmail.py - find phone number and email address in clipboard.

import re
import pyperclip

# create phone regex.
phoneRe = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  #area code
    (\s|-|\.)?          #separator
    (\d{3})             #first 3 digit
    (\s|-|\.)           #separator
    (\d{4})             #last 4 digit
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  #extension
    )''', re.VERBOSE)

# create email regex
emailRe = re.compile(r'''(
    [a-zA-Z0-9-.+]+     #username
    @                   #separator
    [a-zA-Z0-9.-]+      #domain name
    (\.[a-zA-Z]{2,4})   #root dns domain
    )''', re.VERBOSE)

# find match in clipboard.
text = str(pyperclip.paste())
matches = []

for group in phoneRe.findall(text):
    phoneNum = '-'.join([group[1], group[3], group[5]])
    if group[8] != '':
        phoneNum += ' x' + group[8]
    matches.append(phoneNum)
for group in emailRe.findall(text):
    matches.append(group[0])

# copy result to clipboard and print in console.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    print('\n'.join(matches))
else:
    print('Nothing found')

# vs enviroment test env test +1