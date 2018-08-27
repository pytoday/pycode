#!/usr/bin/env python3
# coding=utf-8
# title          : mtfacfib.py
# description    :
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/7/22 6:23
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
from time import sleep, ctime, time
from myThread import MyThread


def fib(x):
    sleep(0.005)
    if x < 2:
        return 1
    return (fib(x-2) + fib(x-1))


def fac(x):
    sleep(0.1)
    if x < 2:
        return 1
    return (x * fac(x-1))


def sum(x):
    sleep(0.1)
    if x < 2:
        return 1
    return (x + sum(x-1))


funcs = [fib, fac, sum]
n = 12


def main():
    nfuncs = range(len(funcs))
    print("*** SIGNLE THREAD")
    start_time = time()
    for i in nfuncs:
        print("starting", funcs[i].__name__, "at: ", ctime())
        print(funcs[i](n))
        print(funcs[i].__name__, "finished at: ", ctime())
    end_time = time()
    print("<<<<<*** SIG TOTAL COST: ", end_time-start_time)

    print("*** MULTIPLE THREADS")
    threads = []
    start_time = time()
    for i in nfuncs:
        t = MyThread(funcs[i], (n,), funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()
        print(threads[i].getResult())
    end_time = time()
    print("<<<<<*** MUL TOTAL COST: ", end_time-start_time)

    print("ALL DONE.")


if __name__ == '__main__':
    main()
