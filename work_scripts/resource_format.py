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
<TABLE DEFINE>
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
    sql = "select ip,mod1,mod1,jifang,loads,cpu,mem,io,disk from tb1"
    cur.execute(sql)
    data = cur.fetchall()
    return data


# save detail to excel
def save_detail(ws, data):
    detail_title = ['IP', '一级模块', '二级模块', '机房', '1分钟负载', 'CPU使用率', '内存使用率', '磁盘io', '磁盘使用率']
    ws.append(detail_title)
    for row in data:
        ws.append(row)


# get idc summary
def get_sum(idc, mods, cur):
    sql_idc_mod = "select '%s', count(1), round(sum(loads)/count(1), 3), round(sum(cpu)/count(1), 3), round(sum(mem)/count(1),3),round(sum(io)/count(1), 3), round(sum(disk)/count(1), 3) from db1.resource where jifang='%s' and mod1 like '%s'"
    sql_idc = "select '汇总', count(1), round(sum(loads)/count(1), 3), round(sum(cpu)/count(1), 3), round(sum(mem)/count(1),3),round(sum(io)/count(1), 3), round(sum(disk)/count(1), 3) from db1.resource where jifang='%s'"
    mod_data = []
    for mod in mods:
        mod_data += cur.execute(sql_idc_mod, (idc, mod))
    idc_data = cur.execute(sql_idc, (idc,))
    return mod_data, idc_data


# get all summary
def get_allsum(mods, cur):
    sql_idc_mod = "select '%s', count(1), round(sum(loads)/count(1), 3), round(sum(cpu)/count(1), 3), round(sum(mem)/count(1),3),round(sum(io)/count(1), 3), round(sum(disk)/count(1), 3) from db1.resource where mod1 like '%s'"
    sql_idc = "select '汇总', count(1), round(sum(loads)/count(1), 3), round(sum(cpu)/count(1), 3), round(sum(mem)/count(1),3),round(sum(io)/count(1), 3), round(sum(disk)/count(1), 3) from db1.resource"
    mod_data = []
    for mod in mods:
        mod_data += cur.execute(sql_idc_mod, (mod, mod))
    idc_data = cur.execute(sql_idc)
    return mod_data, idc_data


# save summary to excel
def save_allsum(ws, idcs, mods, cur):
    # set summary title
    sum_title = ['业务', '服务器数量', '负载平均值', 'CPU使用率%', '内存使用率%', '磁盘IO平均率%', 'DATA磁盘使用率%']
    empty_line = ['']*7

    # save all idc summary
    ws['A1'] = "全部机房"
    ws.merge_cells('A1:A7')
    ws.append(sum_title)
    allsum_data = get_allsum(mods, cur)
    for row in allsum_data[0]:
        ws.append(row)
    ws.append(allsum_data[1])
    ws.append(empty_line)

    # save single idc summary
    for idc in idcs:
        ws.append(idc)
        sum_data = get_sum(idc, mods, cur)
        for row in sum_data[0]:
            ws.append(row)
        ws.append(sum_data[1])
        ws.append(empty_line)


if __name__ == '__main__':
    # db config
    connect = pymysql.connect(
        host='192.168.31.134',
        user='user',
        password='password',
        charset='utf8',
        db='db1'
    )
    cursor = connect.cursor()

    # create workbook
    wb = Workbook()
    dst_file = "20XX年X份自建机房服务器资源使用情况-V1.0.xlsx"
    ws1 = wb.active
    ws1.title = "汇总信息"
    ws2 = wb.create_sheet(title="汇总详情")

    # add data to work sheet
    save_detail(ws2, get_detail(cursor))
    save_allsum(ws1, get_idc(cursor), get_mod(cursor), cursor)

    # save workbook
    wb.save(filename=dst_file)
