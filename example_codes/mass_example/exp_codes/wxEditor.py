#!/usr/bin/env python3
# coding=utf-8
# title          :wxEditor.py
# description    :wxPython example.
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/10/13 18:19
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import wx


def load(event):
    file = open(filename.GetValue())
    contents.SetValue(file.read())
    file.close()


def save(event):
    file = open(filename.GetValue(), 'w')
    file.write(contents.GetValue())
    file.close()


app = wx.App()
win = wx.Frame(None, title="Simple Editor", size=(410, 335))
bkg = wx.Panel(win)

"""
loadButton = wx.Button(win, label='Open', pos=(225, 5), size=(75, 25))
saveButton = wx.Button(win, label='save', pos=(315, 5), size=(75, 25))
filename = wx.TextCtrl(win, pos=(5, 5), size=(210, 25))
contents = wx.TextCtrl(win, pos=(5, 35), size=(390, 260), style=wx.TE_MULTILINE|wx.HSCROLL)
"""

loadButton = wx.Button(bkg, label='open')
loadButton.Bind(wx.EVT_BUTTON, load)

saveButton = wx.Button(bkg, label='save')
saveButton.Bind(wx.EVT_BUTTON, save)

filename = wx.TextCtrl(bkg)
contents = wx.TextCtrl(bkg, style=wx.TE_MULTILINE | wx.HSCROLL)

hbox = wx.BoxSizer()
hbox.Add(filename, proportion=1, flag=wx.EXPAND)    # proportion=1 允许扩展
hbox.Add(loadButton, proportion=0, flag=wx.LEFT, border=5)  # 左边框为准间隔5处放置
hbox.Add(saveButton, proportion=0, flag=wx.LEFT, border=5)

vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
vbox.Add(contents, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=5)

bkg.SetSizer(vbox)
win.Show()
app.MainLoop()
