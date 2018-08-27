#!/usr/bin/env python3
# coding=utf-8
# title          : prodconsQueue.py
# description    :
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/7/30 15:44
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script


from random import randint
from time import sleep
from queue import Queue
from atexit import register
from myThread import MyThread


def writeq(queue):
    print("producing object for q...")
    queue.put('xxxx', 1)
    print("queue size now", queue.qsize())


def readq(queue):
    val = queue.get(1)
    print("consumed object from q... queue size now", queue.qsize())


def writer(queue, nloops):
    for i in range(nloops):
        writeq(queue)
        sleep(randint(1, 3))


def reader(queue, nloops):
    for i in range(nloops):
        readq(queue)
        sleep(randint(2, 5))


funcs = [writer, reader]
nfuncs = range(len(funcs))


def main():
    nloops = randint(2, 5)
    q = Queue(32)
    threads = []

    for i in nfuncs:
        t = MyThread(funcs[i], (q, nloops), funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()


@register
def _atexit():
    print("ALL DONE.")


if __name__ == '__main__':
    main()
