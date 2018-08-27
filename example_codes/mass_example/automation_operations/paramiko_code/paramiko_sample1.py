#!/usr/bin/env python3
# coding=utf-8
# title          :paramiko_sample1.py
# description    :
# author         :JackieTsui
# organization   :pytoday.org
# date           :1/16/18 8:36 PM
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import paramiko
import getpass


hostname = '127.0.0.1'
username = 'jackie'
password = getpass.getpass()
# password = ''

paramiko.util.log_to_file('paramiko_ssh.log')

ssh = paramiko.SSHClient()  # create ssh connection object
ssh.load_system_host_keys()     # load known keys
ssh.connect(hostname=hostname, username=username, password=password)    # login to server
stdin, stdout, stderr = ssh.exec_command('ls -lh')
print(stdout.read())
ssh.close()
