#!/usr/bin/env python3
# coding=utf-8
# title          :sendEmail.py
# description    :example of sending email.
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/12/21 17:06
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


HOST = "smtp.163.com"
SUBJECT = u'业务服务质量周报'
TO = ['testemail.qq.com', ]
FROM = "myeamil@163.com"
PASSWD = "123456"


def addimg(src, imgid):
    fp = open(src, 'rb')
    msgimage = MIMEImage(fp.read())
    fp.close()
    msgimage.add_header('Content-ID', imgid)    # 指定图片对象id
    return msgimage


msg = MIMEMultipart('related')  # mixed带附件的邮件体，默认选项； related构建内嵌资源邮件体；alternative超文本与文本并在

msgtext = MIMEText("<font color=red>业务图表:<br><img src=\"cid:weekly\"border=\"1\"<br>详细见附件</font>",
                   "html", "utf-8") # 邮件超文本内容
msg.attach(msgtext)
msg.attach(addimg("img/weekly.png", "weekly"))

attach = MIMEText(open("doc/week_report.xlsx", "rb").read(), "base64", "utf-8")
attach["Content-Type"] = "application/octet-stream" # 指定附件类型
attach["Content-Disposition"] = "attachment; filename=\"业务周报.xlsx\"".encode("gb18303")  # 保存附件时名称

msg.attach(attach)
msg["Subject"] = SUBJECT
msg["From"] = FROM
msg["TO"] = TO

try:
    server = smtplib.SMTP()
    server.connect(HOST, 25)
    server.starttls()
    server.login(FROM, PASSWD)
    server.sendmail(FROM, TO, msg.as_string())
    server.quit()
    print("Mail send.")
except Exception as e:
    print("Send error with error: " + str(e))
