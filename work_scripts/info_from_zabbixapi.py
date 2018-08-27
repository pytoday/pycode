#!/usr/bin/env python3
# coding=utf-8
# title          :zabbixapi.py
# description    :get host info from zabbix api
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/9/22 16:26
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
from pyzabbix import ZabbixAPI


url = "http://192.168.31.128/zabbix"
user = "Admin"
password = "zabbix"
key_ = "net.if.out[eth0]"
start_time = "1506060000"
end_time = "1506069000"
file = "ip_value.txt"

zapi = ZabbixAPI(url=url, user=user, password=password)


def get_group():
    group_request = zapi.do_request('hostgroup.get', {"output": ["groupid", "name"]})
    return group_request['result']


def get_host(gid):
    host_request = zapi.do_request("host.get",
                                   {"output": ["hostid", "host", "available", "status", "name",
                                               "description"], "groupids": gid})
    return host_request['result']


def get_interface(hid):
    interface_request = zapi.do_request("hostinterface.get", {"output": "extend", "hostids": hid})
    return interface_request['result']


def get_item(hid, key):
    item_request = zapi.do_request("item.get",
                                   {"output": ["itemid", "name", "type", "value_type", "description", "status"],
                                    "hostids": hid, "search": {"key_": key},
                                    "sortfield": "name"})
    return item_request['result']


def get_hist_value(itid, stime, etime):
    hist_request = zapi.do_request("history.get", {"output": "extend", "itemids": itid,
                                                   "time_from": stime, "time_till": etime})
    return hist_request['result']


def get_result(history):
    vv = []
    for i in history:
        vv.append(i['value'])
    v = list(map(int, vv))
    ma = max(v)
    mi = min(v)
    avg = sum(v)/len(v)
    result = [mi, avg, ma]
    return result


groups = get_group()
print("groupname and groupid is:")
for group in groups:
    print(group['name']+":"+group['groupid'])
gid = input("which group you want to count, type groupid:")

hosts = get_host(gid)
hostsid = []
for host in hosts:
    hostsid.append(host['hostid'])

all_result = []
for hid in hostsid:
    interface = get_interface(hid)
    ip = interface[0]['ip']
    item = get_item(hid, key_)
    item_id = item[0]['itemid']
    hist = get_hist_value(item_id, start_time, end_time)
    value = get_result(hist)

    all_result.append([ip, value])

# print(all_result)

with open(file, 'w') as f:
    f.write("IP\tmin\tavg\tmax\n")
    for result in all_result:
        f.write(result[0]+"\t")
        f.write(str(result[1][0])+"\t")
        f.write(str(result[1][1])+"\t")
        f.write(str(result[1][2])+"\n")
    f.close()
