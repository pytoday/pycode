#!/usr/bin/env python
# coding=utf-8
# title          : bandwidth_usage.py
# description    : Calculate interface bandwidth usage
# ==================================================

# Import the module needed to run the script

import subprocess, time
import sys, os, signal
from subprocess import Popen, PIPE
from time import sleep
from multiprocessing import Pool
# compatible with python2
from contextlib import closing


def listmavg(int_list):
    ll = []
    for i in range(len(int_list)-1):
        if i < len(int_list)-1:
            ll.append(int_list[i+1] - int_list[i])
    ll_avg = sum(ll)/len(ll)
    return ll_avg


def gettraffic(nic_name):
    with open('/sys/class/net/'+nic_name+'/statistics/rx_bytes', 'r') as f:
        rx = int(f.read())
    with open('/sys/class/net/'+nic_name+'/statistics/tx_bytes', 'r') as f:
        tx = int(f.read())
    # convert unit to Kb
    return rx, tx


def getspeed(nic_name):
    try:
        with open('/sys/class/net/'+nic_name+'/speed', 'r') as f:
            speed = int(f.read())
    except IOError:
        base_speed = 1000
        bond_path = '/sys/class/net/'+nic_name+'/bonding/slaves'
        # handle no speed net interface
        if os.path.exists(bond_path):
            with open(bond_path, 'r') as f:
                slave_count = len(f.read().split())
            # 处理部分无用的异常绑定口实际没绑定物理口导致slave网卡数为0产生除零错误
            if slave_count == 0:
                slave_count = 1
            speed = base_speed*slave_count
        else:
            speed = base_speed
    return speed


def getnic():
    nic_list = []
    nic_names = ['bond0', 'eth0', 'eth1', 'eth2', 'eth3', 'eth4', 'eth5', 'eth6',
                 'em0', 'em1', 'em2', 'em3', 'em4', 'em5', 'em6', 'wlan', 'lan']
    with open(nic_file, 'r') as f:
        nic_lines = f.readlines()
    for line in nic_lines:
        if ':' in line and 'lo:' not in line and ('em' in line or 'eth' in line or 'bond' in line or 'lan' in line):
            nic_name = line.split(':')[0].strip()
            if nic_name in nic_names:
                nic_list.append(nic_name)
    return nic_list


def getnicid(nic_name):
    nic_names = ['bond0', 'eth0', 'eth1', 'eth2', 'eth3', 'eth4', 'eth5', 'eth6',
                 'em0', 'em1', 'em2', 'em3', 'em4', 'em5', 'em6', 'wlan', 'lan']
    nic_inids = [3227, 3228, 3229, 3230, 3231, 3232, 3233, 3234, 3235, 3236, 3237, 3238, 3239, 3240, 3241, 3546, 3547]
    zipped = list(zip(nic_names, nic_inids))
    return zipped[nic_names.index(nic_name)]


def bandwidth_usage(nic_name):
    count = 0
    rx_list = []
    tx_list = []

    while count < 30:
        traffic_in = gettraffic(nic_name)[0]
        traffic_out = gettraffic(nic_name)[1]
        rx_list.append(traffic_in)
        tx_list.append(traffic_out)
        count += 1
        sleep(1)

    nicid = getnicid(nic_name)[1]
    percent = max(listmavg(rx_list), listmavg(tx_list))/1024.00/1024*8/getspeed(nic_name)*100   # fix for py2
    return nicid, percent


def makeurl(bd_usage=(0, 0)):
    nic_para = 'fid='+str(bd_usage[0])+'&value='+format(bd_usage[1], '.3f')+'|'
    return nic_para


def pcheck(pids):
    # using /proc/pid/cmdline,not ps cmd
    for pid in pids:
        if pid:
            with open('/proc/'+pid+'/cmdline') as cmd:
                cmd_content = cmd.read()
            if __file__ in cmd_content:
                # print(pid, cmd_content)
                os.kill(int(pid), signal.SIGKILL)


if __name__ == '__main__':
    nic_file = '/proc/net/dev'
    lock_file = '/tmp/bandwidth_usage.lock'
    # exec_file used to send monitor value
    exec_file = '/data/services/op_agent_d/tools/send_value '
    agents = 6
    interval = 300

    # process hang check
    if os.path.exists(lock_file):
        file_time = os.path.getmtime(lock_file)
        now_time = time.time()
        time_diff = now_time - file_time
        with open(lock_file) as f:
            pid = int(f.read())

        if not os.path.exists('/proc/'+str(pid)):
            os.remove(lock_file)
            sys.exit()
        elif time_diff > interval:
            os.kill(pid, signal.SIGKILL)
            os.remove(lock_file)
            sys.exit()
        else:
            sys.exit()

    elif not os.path.exists(lock_file):
        # get pid of script and kill it
        proc = subprocess.Popen(['pidof', 'python'], stdout=subprocess.PIPE, shell=False)
        allpid = proc.stdout.read()
        if isinstance(allpid, bytes):
            pids = allpid.decode().split()
        else:
            pids = allpid.split()
        pids.remove(str(os.getpid()))
        pcheck(pids)

        pid = os.getpid()
        fd = open(lock_file, 'w')
        fd.write(str(pid))
        fd.close()

        try:
            with closing(Pool(processes=agents)) as pool:
                result = pool.map(bandwidth_usage, getnic())
                pool.close()
                pool.join()

            all_para = ''
            for para in result:
                all_para += makeurl(para)
            params = all_para.rstrip('|')

            p = Popen(exec_file+'"'+params+'"', shell=True, stdin=PIPE, stdout=PIPE, close_fds=True)
            output = p.stdout.read()
            print(output)
        finally:
            os.remove(lock_file)
