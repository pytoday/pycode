#!/usr/bin/env python3
# coding=utf-8
# title          :paramiko_sftp.py
# description    :
# author         :JackieTsui
# organization   :pytoday.org
# date           :1/16/18 9:22 PM
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import paramiko
import os,sys,time


jumpip = "192.168.10.1"
jumpuser = "jackie"
jumppass = "123456"
hostname = "192.168.10.2"
user = "root"
password = "654321"

tmpdir = "/tmp"
remotedir = "/data"
localpath = "/home/nginx_access.tar.gz"
tmppath = tmpdir + "/nginx_access.tar.gz"
remotepath = remotedir + "/nginx_access_hd.tar.gz"
port = 22
passinfo = "'s password: "
paramiko.util.log_to_file('syslogin.log')

t = paramiko.Transport((jumpip, port))
t.connect(username=jumpuser, password=jumppass)
sftp = paramiko.SFTPClient.from_transport(t)
sftp.put(localpath, remotepath)
sftp.close()

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

channel = ssh.invoke_shell()
channel.settimeout(10)

buff = ""
resp = ""
channel.send("scp " + tmppath + " " + user + "@" + hostname + ":" + remotepath + "\n")
while not buff.endswith(passinfo):
    try:
        resp = channel.recv(9999)
    except Exception as e:
        print("Error info: " + str(e))
        channel.close()
        ssh.close()
        sys.exit()
    buff += resp
    if not buff.find("yes/no") == -1:
        channel.send("yes\n")
        buff = ""

channel.send(password + "\n")

buff = ""
while not buff.endswith("# "):
    resp = channel.recv(9999)
    if not resp.find(passinfo) == -1:
        print("Error info: Auth failed.")
        channel.close()
        ssh.close()
        sys.exit()
    buff += resp

print(buff)
channel.close()
ssh.close()

