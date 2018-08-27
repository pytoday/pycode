#!/usr/bin/env python3
# coding=utf-8
# title          : mtsleepA.py
# description    :
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/7/17 21:51
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import _thread
from time import ctime, sleep


def loop0(num):
    print("start loop0 at %d: %s" % (num, ctime()))
    sleep(4)
    print("loop0 done at: ", ctime())


def loop1():
    print("start loop1 at: ", ctime())
    sleep(2)
    print("loop1 done at: ", ctime())


def main():
    print("START: ", ctime())
    _thread.start_new_thread(loop0, (111,))
    _thread.start_new_thread(loop1, ())
    sleep(6)    # 必须等待thread运行完，否则运行完不等待线程运行完会退出,此情况下未完成线程也退出
    print("DONE: ", ctime())


if __name__ == '__main__':
    main()
