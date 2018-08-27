#!/usr/bin/env python3
# coding=utf-8
# title				:sendMail.py
# description		:
# date				:2017-08-04 02:34:23
# notes				:
# =====================================================

import smtplib
import time
from email.mime.text import MIMEText
from email.header import Header

host = 'mail.xxx.com'
port = 587
mail_from = 'xxx@xxx.com'
mail_pass = '123456'
mail_to = 'aa@163.com, bb@163.com'
# mail_cc = ('aa@163.com',)

with open('/tmp/alarm.tmp') as fileObj:
    content = fileObj.read()
message = MIMEText(content, 'plain', 'utf-8')
subject = host + ':mail server error'
message['Subject'] = Header(subject)
message['From'] = mail_from
message['To'] = mail_to
# message['Cc'] = mail_cc

try:
    server = smtplib.SMTP(host, port)
    server.ehlo()
    server.starttls()
    server.login(mail_from, mail_pass)
    server.sendmail(mail_from, mail_to.split(','), message.as_string())
    server.quit()
    time_str = time.strftime('%Y-%m-%d %H:%M:%S')
    print(time_str + ' mail sent.')
except smtplib.SMTPException:
    time_str = time.strftime('%Y-%m-%d %H:%M:%S')
    print(time_str + " Can't send mail.")
