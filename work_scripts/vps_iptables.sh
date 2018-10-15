#!/usr/bin/env bash
#coding=utf-8
#description    :
#author         :JackieTsui
#organization   :pytoday.org
#date           :2018/1/2 0:38
#email          :jackietsui72@gmail.com
#notes          :iptables example
#==================================================
#backup original iptables-rule
#/sbin/iptables-save >/etc/iptables-rule_ori_$(date +%Y-%m-%d)
#Clear rules and set default policy
iptables -F
iptables -X
iptables -Z
iptables -P INPUT ACCEPT
iptables -P FORWARD ACCEPT
iptables -P OUTPUT ACCEPT
iptables -A INPUT -i lo -j ACCEPT
iptables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT

#Enable icmp protocol
iptables -A INPUT -p icmp --icmp-type 8 -j ACCEPT

#Allow ssh port
iptables -N LIMIT_ACCESS_SSH
iptables -A INPUT  -p tcp -m multiport --dports 2222 -g LIMIT_ACCESS_SSH
iptables -A LIMIT_ACCESS_SSH -s 0.0.0.0/0 -j ACCEPT

#Allow web access
iptables -N LIMIT_ACCESS_WEB
iptables -A INPUT  -p tcp -m multiport --dports 80,443 -g LIMIT_ACCESS_WEB
iptables -A LIMIT_ACCESS_WEB -s 0.0.0.0/0 -j ACCEPT

#Allow shadowsocks access
iptables -N LIMIT_ACCESS_SS
iptables -A INPUT  -p tcp -m multiport --dports 4430 -g LIMIT_ACCESS_SS
iptables -A LIMIT_ACCESS_SS -s 0.0.0.0/0 -j ACCEPT

#Allow test port
iptables -N LIMIT_ACCESS_DJ
iptables -A INPUT  -p tcp -m multiport --dports 8000 -g LIMIT_ACCESS_DJ
iptables -A LIMIT_ACCESS_DJ -s 0.0.0.0/0 -j ACCEPT

#Log and denied
iptables -A INPUT ! -d 255.255.255.255 -j LOG --log-prefix="iptables-reject "
iptables -A INPUT ! -d 255.255.255.255 -j DROP
