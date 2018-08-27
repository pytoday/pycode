#!/usr/bin/env python3
# coding=utf-8
# title          : tkhello.py
# description    :
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/8/5 17:07
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import tkinter


top = tkinter.Tk()
label = tkinter.Label(top, text="Hello World.")
label.pack()

qu = tkinter.Button(top, text='QUIT', command=top.quit, bg='red', fg='white')
qu.pack(fill=tkinter.X, expand=1)
tkinter.mainloop()
