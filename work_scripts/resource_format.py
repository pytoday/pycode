#!/usr/bin/env python3
# coding=utf-8
# title          : resource_format.py
# description    :
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/12/20 15:26
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import pymysql
from openpyxl import Workbook


"""
<table define>
| tb1 | CREATE TABLE `tb1` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '无意义',
  `ip` varchar(20) COLLATE utf8mb4_bin NOT NULL DEFAULT '0' COMMENT '机器IP',
  `mod1` varchar(45) COLLATE utf8mb4_bin NOT NULL DEFAULT '运维' COMMENT '一级模块',
  `mod2` varchar(200) COLLATE utf8mb4_bin NOT NULL DEFAULT '0' COMMENT '二级模块',
  `jifang` varchar(200) COLLATE utf8mb4_bin NOT NULL DEFAULT '运维' COMMENT '机房',
  `loads` decimal(6,2) NOT NULL DEFAULT '0.00' COMMENT '负载',
  `cpu` decimal(6,2) NOT NULL DEFAULT '0.00' COMMENT 'CPU使用',
  `mem` decimal(6,2) NOT NULL DEFAULT '0.00' COMMENT '内存',
  `io` decimal(6,2) NOT NULL DEFAULT '0.00' COMMENT 'IO使用率',
  `disk` decimal(6,2) NOT NULL DEFAULT '0.00' COMMENT '磁盘空间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5411 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin                                 |
"""

# db config
connect = pymysql.connect(
    host='192.168.31.134',
    user='user',
    password='password',
    charset='utf8',
    db='db1'
)
cursor = connect.cursor()


# get mod
def get_mod(cur):
    # sql = "SELECT name,saving FROM trade WHERE account = '%s' "
    # data = ('13512345678',)
    sql = "select distinct mod1 from tb1"
    cur.execute(sql)
    for row in cur.fetchall():
        yield row[0]


# get idc name
def get_idc(cur):
    sql = "select distinct jifang from tb1"
    cur.execute(sql)
    for row in cur.fetchall():
        yield row[0]


# get detail
def get_detail(cur):
    sql = "select * from tb1"
    cur.execute(sql)
    data = cur.fetchall()
    return data


# create workbook
wb = Workbook()
dst_file = "20XX年X份自建机房服务器资源使用情况-V1.0.xlsx"
ws1 = wb.active
ws1.title = "汇总信息"
ws2 = wb.create_sheet(title="汇总详情")
# ws1.append(range(600))
# ws2.cell(column=col, row=row, value="{0}".format(get_column_letter(col)))
wb.save(filename=dst_file)


# save detail to excel
detail_title = ['IP', '一级模块', '二级模块', '机房', '1分钟负载', 'CPU使用率', '内存使用率', '磁盘io', '磁盘使用率']
# get summary


# save summary to excel
sum_title = ['业务', '服务器数量', '负载平均值', 'CPU使用率%', '内存使用率%', '磁盘IO平均率%', 'DATA磁盘使用率%']


if __name__ == '__main__':
    print(list(get_mod(cursor)))
    print(list(get_idc(cursor)))
    print(get_detail(cursor)[0])
