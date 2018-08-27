#!/usr/bin/env python3
# coding=utf-8
# title          :phantomjs.py
# description    :example of phantomjs
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/11/23 14:40
# email          :jackietsui72@gmail.com
# notes          :在开头的stock中加入要获取的股票代码，必须以英文引号引起来，区分大小写
# ==================================================

# Import the module needed to run the script
import os
import xlwt
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# example: stock = ['SZ000651', 'SZ999321', 'HD432']
stock = ['SZ000651', 'SZ000001']
# waiting for page load complete
times = 2


def format_line(li):
    """序号异常格式化"""
    for_line = []
    for_line.append(li[0])
    for i in range((len(li)//2)):
        if i < len(li)//2-1:
            for_line.append(li[2*i+1]+' '+li[2*(i+1)])
    for_line.append(li[-1])
    return for_line


def format_text(text, num):
    """按年份生成文本块"""
    all_lines = len(text.split('\n'))
    sep_num = all_lines/num
    line_number = 0
    block = []
    for li in text.split('\n'):
        line_number += 1
        block.append(li)
        if not line_number % sep_num:
            yield block
            block = []


def save_list(work_book, text_list, sheet_name):
    sheet1 = work_book.add_sheet(sheet_name, cell_overwrite_ok=True)  # 创建sheet
    row_num = 0
    for line in text_list:
        line_list = []
        if '合计' in line and '股东' not in line:
            line = 'N ' + line
        for li in line.split(' '):
            if li.strip('AG'):
                line_list.append(li)
        for col_num in range(len(line_list)):
            first_col = sheet1.col(col_num)  # 设置宽度
            first_col.width = 256 * 20
            sheet1.write(row_num, col_num, line_list[col_num])
        row_num += 1


def save_file(work_book, sto_name, file_name):
    xls_file = os.path.join(sto_name, file_name)
    work_book.save(xls_file)


def save_text(text, sto_name):
    if not os.path.exists(sto_name):
        os.makedirs(sto_name)
    text_list = []
    for line in text.split('\n'):
        text_list.append(line)
    xf = xlwt.Workbook(encoding='utf-8')  # 创建工作簿
    save_list(xf, text_list, u'sheet1')
    save_file(xf, sto_name, u'股东人数.xls')


def handle(stock, times):
    """处理主函数"""
    # set UA for driver
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    UA = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/\
    62.0.3202.94 Safari/537.36"
    dcap["phantomjs.page.setttings.userAgent"] = UA
    dcap["phantomjs.page.settings.loadImages"] = False
    driver = webdriver.PhantomJS(executable_path=r'C:\Program Files (x86)\phantomjs\bin\phantomjs.exe',
                             desired_capabilities=dcap)

    # page and script timeout
    driver.set_page_load_timeout(10)
    driver.set_script_timeout(10)

    # url set
    url_tmp = "http://emweb.securities.eastmoney.com/f10_v2/ShareholderResearch.aspx?type=web&code="
    url = url_tmp + stock

    # load page
    driver.get(url)
    sleep(times)

    # find all tag
    tables = driver.find_elements_by_tag_name('table')
    for t in tables:
        driver.execute_script("arguments[0].setAttribute('style', 'visibility:visible')", t)

    # get date from class name tab
    date = driver.find_elements_by_class_name('tab')
    date_list = date[0].text.split('\n')
    # print(date_list[0])

    gdrs = driver.find_elements_by_id('Table0')
    # print(gdrs[0].text)
    save_text(gdrs[0].text, stock)

    ltgd = driver.find_elements_by_id('TTCS_Table_Div')
    ltxf = xlwt.Workbook(encoding='utf-8')  # 创建工作簿
    n = 0
    for line in format_text(ltgd[0].text, len(date_list)):
        save_list(ltxf, format_line(line), date_list[n])
        n += 1
    save_file(ltxf, stock, u'十大流通股东.xls')

    sdgd = driver.find_elements_by_id('TTS_Table_Div')
    sdxf = xlwt.Workbook(encoding='utf-8')  # 创建工作簿
    n = 0
    for line in format_text(sdgd[0].text, len(date_list)):
        save_list(sdxf, line, date_list[n])
        n += 1
    save_file(sdxf, stock, u'十大股东.xls')

    jjcg = driver.find_elements_by_id('FHS_Table_Div')
    jjxf = xlwt.Workbook(encoding='utf-8')  # 创建工作簿
    n = 0
    for line in format_text(jjcg[0].text, len(date_list)):
        save_list(jjxf, line, date_list[n])
        n += 1
    save_file(jjxf, stock, u'基金持股.xls')

    driver.quit()


for st in stock:
    handle(st, times)
