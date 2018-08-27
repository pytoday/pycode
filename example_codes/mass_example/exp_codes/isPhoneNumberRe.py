#!/usr/bin/env python3
# coding=utf-8

import re
messg = input("Pls input something, I'll tell you contain phone number or not.")

def containNumber(msg):
    phoneNumberRe = re.compile(r'\d{3}-\d{3}-\d{4}')
    mo = phoneNumberRe.search(msg)
    if mo is None:
        return None
    return mo.group()

print(containNumber(messg))     #匹配内容并打印，未匹配内容输出None.