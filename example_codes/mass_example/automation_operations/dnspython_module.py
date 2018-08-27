#!/usr/bin/env python3
# coding=utf-8
# title          :dnspython_module.py
# description    :
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/12/18 21:40
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import dns.resolver


domain = 'f1g1ns1.dnspod.net'
A = dns.resolver.query(domain, 'A')
for a in A.response.answer:
    for i in a.items:
        print(i.address)

mx_domain = '163.com'
MX = dns.resolver.query(mx_domain, 'MX')
for mx in MX:
    print('preference: %s' % mx.preference)
    print('exchange: %s' % mx.exchange)

# CNAME same as NS
ns_domain = 'pytoday.org'
NS = dns.resolver.query(ns_domain, 'NS')
for ns in NS.response.answer:
    for n in ns.items:
        print(n.to_text())
