#!/usr/bin/env python3
# coding=utf-8
# title          : excel_com.pyw.py
# description    :
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/8/14 16:39
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
from tkinter import Tk
from time import sleep
from tkinter.messagebox import showwarning
import win32com.client as win32


warn = lambda app: showwarning(app, 'Exit')
RANGE = range(3, 8)


def excel():
    app = 'Excel'
    x1 = win32.gencache.EnsureDisaptch('%s.Application' % app)
    ss = x1.Workbooks.Add()
    sh = ss.ActiveSheet
    x1.Visible = True

    sleep(1)
    sh.Cells(1, 1).Value = 'Python to %s Demon' % app
    warn(app)
    ss.Close(False)
    x1.Application.Quit()


if __name__ == '__main__':
    Tk().withdraw()
    excel()
