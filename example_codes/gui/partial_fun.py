#!/usr/bin/env python3
# coding=utf-8
# title          : partial_fun.py
# description    :
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/8/5 20:31
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script


from functools import partial as pto
from tkinter import Tk, Button, X
from tkinter.messagebox import showinfo, showerror, showwarning


WARN = 'warn'
CRIT = 'crit'
REGU = 'regu'

SIGNS = {
    'do not enter': CRIT,
    'railroad crossing': WARN,
    '55\nspeed limit': REGU,
    'wrong way': CRIT,
    'merging traffic': WARN,
    'on way': REGU
}

critCB = lambda: showerror('Error', 'Error Button Pressed!')
warnCB = lambda: showwarning('Warning', 'Waring Button Pressed.')
infoCB = lambda: showinfo('Info', 'Info Button Pressed.')

top = Tk()
top.title('Road Signs')
Button(top, text='QUIT', command=top.quit, bg='red', fg='white').pack()

MyButton = pto(Button, top)
CritButton = pto(MyButton, command=critCB, bg='white', fg='red')
WarnButton = pto(MyButton, command=warnCB, bg='goldenrod1')
ReguButton = pto(MyButton, command=infoCB, bg='white')

for each in SIGNS:
    signType = SIGNS[each]
    cmd = '%sButton(text=%r%s).pack(fill=X, expand=True)' % (signType.title(), each, '.upper()' if signType == CRIT else '.title()')
    eval(cmd)

top.mainloop()
