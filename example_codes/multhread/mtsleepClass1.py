#!/usr/bin/env python3
# coding=utf-8
# title          : mtsleepClass1.py
# description    : another class
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/7/22 5:35
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import threading
from time import sleep, ctime


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        self.func(*self.args)


def loop(nloop, nsec):
    print("start loop", nloop, "at: ", ctime())
    sleep(nsec)
    print("end loop of [%d] at : %s." % (nloop, ctime()))


def main(loops):
    print("START AT: %s" % ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print("ALL DONE AT: %s" % ctime())


if __name__ == '__main__':
    loops = [3, 6]
    main(loops)
