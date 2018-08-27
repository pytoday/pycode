#!/usr/bin/env python3
# coding=utf-8
# title          : mime_example.py
# description    :
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/7/17 2:09
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import message_from_string
from smtplib import SMTP


# multipart: alternative, related, mixed
# SMTP_SSL, POP3_SSL more security
def make_mpa_msg():
    email = MIMEMultipart('alternative')
    text = MIMEText("hello world!\r\n", 'plain')
    email.attach(text)
    html = MIMEText(
        '<html><body><h4>hello world!</h4></body></html>',
        'html')
    email.attach(html)
    return email


def make_img_msg(fn):
    f = open(fn, 'rb')
    data = f.read()
    f.close()
    email = MIMEImage(data, name=fn)
    email.add_header('Content-Dispostion', 'attachemnt', filename=fn)
    return email


def sendMsg(fr, to, host, msg):
    s = SMTP(host)
    errs = s.sendmail(fr, to, msg)
    s.quit()


def processMsg(entire_msg):
    body = ""
    msg = message_from_string(entire_msg)
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == 'text/palin':    # get mime type
                body = part.get_payload()
                break
            else:
                body = msg.get_payload(decode=True)
    else:
        body = msg.get_payload(decode=True)
    return body


if __name__ == '__main__':
    print("Sending multipart alternative msg...")
    msg = make_mpa_msg()
    msg['From'] = 'admin@pytoday.org'
    msg['To'] = ['1@pytoday.org', '2@pytoday.org']
    msg['Subject'] = 'multipart alternative test'
    sendMsg(msg['From'], msg['To'], 'localhost', msg.as_string())

    print("Sending img msg...")
    msg = make_img_msg('/path/to/filename.jgp')
    sendMsg(msg['From'], msg['To'], 'localhost', msg.as_string())
