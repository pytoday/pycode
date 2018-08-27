#!/usr/bin/env python3
# coding=utf-8
# title          : mtsleepB.py
# description    :
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/7/17 22:11
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
from time import ctime, sleep
import _thread


def loop(nloop, nsec, nlock):
    print("loop[%d] started at: %s." % (nloop, ctime()))
    sleep(nsec)
    print("loop[%d] done at: %s." % (nloop, ctime()))
    nlock.release()


def main(loops):
    print("STARTED AT: ", ctime())
    locks = []
    nloops = range(len(loops))

    # generate lock for each loop/thread and save it to list.
    for i in nloops:
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    # start loop/thread
    for i in nloops:
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))

    # check if each loop/thread release lock.
    for i in nloops:
        while locks[i].locked():
            pass

    # control thread wait each loop release lock.
    print("DONE AT: ", ctime())


if __name__ == '__main__':
    loops = [6, 4]
    main(loops)
