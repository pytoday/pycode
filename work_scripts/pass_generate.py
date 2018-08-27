#!/usr/bin/env python3
# coding=utf-8
# title          :pass_generate.py
# description    :generate random password
# author         :JackieTsui
# organization   :pytoday.org
# date           :2018/1/24 17:15
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import string
import random
import sys
import pyperclip


punctuation = "!@#$%^&*"
letters = string.ascii_letters
digits = string.digits


def prompt():
    print("""
    ==Please select which on you want to use.==
    1. Use letters, digits and punctuation to generate password.
    2. Use letters and digits to generate password.
    """)
    choice = input("Please make a choice[1/2]: ")
    length = input("Please input character length[6-40]:")

    if not choice.isdigit() or not length.isdigit():
        print("Input type error. Abort.")
        sys.exit()
    elif 1 <= int(choice) <= 2 and 6 <= int(length) <= 40:
        result = [int(choice), int(length)]
        return result
    else:
        print("Input out of range.")


def genpass(result):
    flag_letter = random.choice(letters)
    flag_digit = random.choice(digits)
    flag_punc = random.choice(punctuation)
    password = ""

    if result[0] == 2:
        while result[1] != 0:
            tmp = random.choice(letters+digits)
            password += tmp
            result[1] -= 1
        # make sure password has letters and digits
        t1 = random.choice(password)
        t2 = random.choice(password)
        while t1 == t2:
            t2 = random.choice(password)
        p1 = password.replace(t1, flag_letter)
        p2 = p1.replace(t2, flag_digit)
        return p2
    elif result[0] == 1:
        while result[1] != 0:
            tmp = random.choice(letters+digits+punctuation)
            password += tmp
            result[1] -= 1
        # make sure password has letters and digits
        t1 = random.choice(password)
        t2 = random.choice(password)
        t3 = random.choice(password)
        while t1 == t2:
            t2 = random.choice(password)
        while t2 == t3 or t1 == t3:
            t3 = random.choice(password)
        p1 = password.replace(t1, flag_letter)
        p2 = p1.replace(t2, flag_digit)
        p3 = p2.replace(t3, flag_punc)
        return p3


result = prompt()
password = genpass(result)

pyperclip.copy(password)
print("Password: %s copied to clipboard." % password)
