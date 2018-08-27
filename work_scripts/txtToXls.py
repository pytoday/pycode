#!/usr/bin/env python3
# coding=utf-8
# title          :txtToXls.py
# description    :convert txt file to xls
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/7/2 16:48
# email          :jackietsui72@gmail.com
# notes          :txtToXls.py /path/to/file.txt /path/to/save.xls
# ==================================================

# Import the module needed to run the script
import sys
import xlwt

if len(sys.argv) < 3:
    print('parameter less than 2.')
    print('usage: txtToXls.py /path/to/file.txt /path/to/save.xls')
    exit(1)

txtFile = sys.argv[1]
xlsFile = sys.argv[2]
sepStr = '\t'
# tf = open(txtFile, mode='r', encoding='gbk')  # for python2
tf = open(txtFile, mode='r')
lines = tf.readlines()
xf = xlwt.Workbook(encoding='utf-8')  # 创建工作簿
sheet1 = xf.add_sheet(u'sheet1', cell_overwrite_ok=True)  # 创建sheet

row_num = 0
for line in lines:

    tmp_line = line.strip('\n').split(sepStr)
    cols = len(tmp_line)

    for col_num in range(cols):
        first_col = sheet1.col(col_num)  # 设置宽度
        first_col.width = 256*20
        sheet1.write(row_num, col_num, tmp_line[col_num])
    row_num += 1

# sheet1.write(0,0,start_date,set_style('Times New Roman',220,True))
xf.save(xlsFile)  # 保存文件
tf.close()  # 关闭文本文件
