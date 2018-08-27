#!/usr/bin/env python3
# coding=utf-8
# title          :paramiko_sshclient.py
# description    :
# author         :JackieTsui
# organization   :pytoday.org
# date           :1/16/18 9:07 PM
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import paramiko
import os


hostname = 'localhost'
username = 'jackie'
paramiko.util.log_to_file('sshclient.log')

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.WarningPolicy())
ssh.load_system_host_keys()
privatekey = os.path.expanduser('~jackie/.ssh/id_rsa')      # convert ~ to path
key = paramiko.RSAKey.from_private_key_file(privatekey)

ssh.connect(hostname=hostname, username=username, pkey=key)
stdin, stdout, stderr = ssh.exec_command('free -m')
print(stdout.read(), end='\n')
ssh.close()
