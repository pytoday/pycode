#!/usr/bin/env python3
# coding=utf-8
# title          : mtsleepFun.py
# description    : use function create thread
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/7/22 5:02
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
from time import ctime, sleep
import threading


def loop(nloop, nsec):
    print("start loop", nloop, "at: ", ctime())
    sleep(nsec)
    print("end loop of [%d] at : %s." % (nloop, ctime()))


def main(loops):
    print("START AT:%s" % ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    # start thread.
    for i in nloops:
        threads[i].start()

    # waiting for all thread to finish or timeout. thread.join(timeout)
    for i in nloops:
        threads[i].join()

    print("ALL DONE AT: %s" % ctime())


if __name__ == "__main__":
    loops = [4, 8]
    main(loops)
