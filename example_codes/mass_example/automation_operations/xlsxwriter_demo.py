#!/usr/bin/env python3
# coding=utf-8
# title          :xlsxwriter_demo.py
# description    :demo of xlsxwriter
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/12/23 15:24
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import xlsxwriter


workbook = xlsxwriter.Workbook('demon1.xlsx')   # create a excel workbook
worksheet = workbook.add_worksheet('SheetName')     # add work sheet to workbook
worksheet.set_column("A:B", 15)     # set A:B length 15
bold = workbook.add_format({'bold': True})  # set format bold
worksheet.write('A1', 'hello world')    # write string to A1
worksheet.write('B1', 'asdfasdf', bold)
worksheet.write('B2', u'中文输入测试', bold)
worksheet.write(2, 0, 32)   # set value use col and row
worksheet.write(3, 0, 35)
worksheet.write(4, 0, '=SUM(A3:A4)')
worksheet.insert_image('B5', 'img/ship.bmp')   # add img
workbook.close()
