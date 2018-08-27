#!/usr/bin/env python3
# coding=utf-8
# title          : tkhello1.py
# description    :
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/8/5 17:20
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import tkinter


def resize(ev=None):
    lable.config(font='Helvetica -%d bold' % scale.get())


top = tkinter.Tk()
top.geometry('250x150')

lable = tkinter.Label(top, text='Hello World.', font='Helvetica -12 bold')
lable.pack(fill=tkinter.Y, expand=1)

scale = tkinter.Scale(top, from_=10, to=40, orient=tkinter.HORIZONTAL, command=resize)
scale.set(12)
scale.pack(fill=tkinter.X, expand=1)

qu = tkinter.Button(top, text='QUIT', command=top.quit, activeforeground='white', activebackground='red')
qu.pack()

tkinter.mainloop()
