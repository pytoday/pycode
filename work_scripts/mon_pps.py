#!/usr/bin/env python
# Monitor packets per second
# coding=utf-8
# Import the module needed to run the script

import sys, os, time
import subprocess, signal
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


def packets(nic_name):
    with open('/sys/class/net/'+nic_name+'/statistics/rx_packets', 'r') as f:
        rx = int(f.read())
    with open('/sys/class/net/'+nic_name+'/statistics/tx_packets', 'r') as f:
        tx = int(f.read())
    # convert unit to Kb
    return rx, tx


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
    # better to use dict not list
    nic_names = ['bond0', 'eth0', 'eth1', 'eth2', 'eth3', 'eth4', 'eth5', 'eth6',
                 'em0', 'em1', 'em2', 'em3', 'em4', 'em5', 'em6', 'wlan', 'lan']
    nic_inids = [3549, 3551, 3553, 3555, 3557, 3559, 3561, 3563, 3565, 3567, 3569, 3571, 3573, 3575, 3577, 3579, 3581]
    nic_outids = [3550, 3552, 3554, 3556, 3558, 3560, 3562, 3564, 3566, 3568, 3570, 3572, 3574, 3576, 3578, 3580, 3582]
    zipped = list(zip(nic_names, nic_inids, nic_outids))
    return zipped[nic_names.index(nic_name)]


def pps_sum(nic_name):
    count = 0
    rx_list = []
    tx_list = []

    while count < 30:
        packet_in = packets(nic_name)[0]
        packet_out = packets(nic_name)[1]
        rx_list.append(packet_in)
        tx_list.append(packet_out)
        count += 1
        sleep(1)

    return getnicid(nic_name)[1], listmavg(rx_list), getnicid(nic_name)[2], listmavg(tx_list)


def makeurl(pps=(0, 0, 0, 0)):
    nic_para = 'fid='+str(pps[0])+'&value='+str(pps[1])+'|'+'fid='+str(pps[2])+'&value='\
               + str(pps[3])+'|'
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
    lock_file = '/tmp/mon_pps.lock'
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
                result = pool.map(pps_sum, getnic())
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
