#!/usr/bin/env python3
# coding=utf-8
# title          :dns_sample1.py
# description    :monitor dns example
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/12/21 15:31
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import dns.resolver
import http.client


iplist = []
appdomain = "www.baidu.com"


def get_iplist(domain=""):
    try:
        A = dns.resolver.query(domain, 'A')
    except Exception as e:
        print('resolve error:' + str(e))
        return
    for a in A.response.answer:
        for i in a.items:
            iplist.append(i.address)
    return True


def checkip(ip):
    checkurl = ip + ":80"
    getcontent = ""
    conn = http.client.HTTPConnection(checkurl)

    try:
        conn.request("GET", "/", headers={"Host": appdomain})
        r = conn.getresponse()
        getcontent = r.read(15)
    finally:
        if "<!doctype html>" in str(getcontent.lower()):
            print(ip+": ok")
        else:
            print(ip+": ERROR!!!")


if __name__ == "__main__":
    if get_iplist(appdomain) and len(iplist) > 0:
        for ip in iplist:
            checkip(ip)
    else:
        print("resolve error.")
