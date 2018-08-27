#!/usr/bin/env python3
# coding=utf-8
# title          : myMail.py
# description    :
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/7/17 1:38
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
from smtplib import SMTP
from poplib import POP3
from time import sleep


SServer = 'smtp.pytoday.org'
PServer = 'pop.pytoday.org'
who = 'admin@pytoday.org'
body = '''
From: %(who)s
To: %(who)s
Subject: test msg
Hello World!
''' % {'who': who}

sendSvr = SMTP(SServer)
errs = sendSvr.sendmail(who, [who], body)
sendSvr.quit()
assert len(errs) == 0, errs
sleep(10)

recvSvr = POP3(PServer)
recvSvr.user('admin')
recvSvr.pass_('password')
# stat(), return mail stat(msg_count, mbox_size); retr(msgnum), return server response, msglines, msgsize
rsp, msg, size = recvSvr.retr(recvSvr.stat()[0])
sep = msg.index('')
recvBody = msg[sep+1:]
assert body == recvBody
