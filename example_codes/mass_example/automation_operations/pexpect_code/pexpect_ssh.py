#!/usr/bin/env python3
# coding=utf-8
# title          :pexpect_ssh.py
# description    :
# author         :JackieTsui
# organization   :pytoday.org
# date           :1/15/18 10:59 PM
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import pexpect
import getpass


ip = "127.0.0.1"
user = "jackie"
password = getpass.getpass("Password: ")
# password = "123456"
target_file = "scp.log"

child = pexpect.spawn('/usr/bin/ssh', [user+'@'+ip])
fout = open(target_file, 'wb')
child.logfile = fout

try:
    child.expect('(?i)password')    # ignore case
    child.sendline(password)
    child.expect("$")
    child.sendline('ls -lhd /home')
    child.sendline('exit')
    fout.close()
except EOFError:
    print("expect EOF")
except TimeoutError:
    print("expect TIMEOUT")
