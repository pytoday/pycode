#!/usr/bin/env python3
# coding=utf-8
# title          : mtsleepClass.py
# description    : use call able instance create thread
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/7/22 5:20
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import threading
from time import sleep, ctime


class ThreadFunc:
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        self.func(*self.args)


def loop(nloop, nsec):
    print("start loop", nloop, "at: ", ctime())
    sleep(nsec)
    print("end loop of [%d] at : %s." % (nloop, ctime()))


def main(loops):
    print("START AT: %s" % ctime())
    threads = []
    nloops = range(len(loops))

    # create all thread
    for i in nloops:
        t = threading.Thread(target=ThreadFunc(loop, (i, loops[i]), loop.__name__))
        threads.append(t)

    # start thread
    for i in nloops:
        threads[i].start()

    # wait thread finish
    for i in nloops:
        threads[i].join()
    print("ALL DONE AT: %s" % ctime())


if __name__ == '__main__':
    loops = [2, 6]
    main(loops)
