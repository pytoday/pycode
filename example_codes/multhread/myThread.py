#!/usr/bin/env python3
# coding=utf-8
# title          : myThread
# description    : another class
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/7/22 5:35
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import threading
from time import ctime


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        print("starting", self.name, "at: ", ctime())
        self.res = self.func(*self.args)
        print(self.name, "finished at: ", ctime())

    def getResult(self):
        return self.res

