#!/usr/bin/env python3
# coding=utf-8
# title          : approval_host.py
# description    :
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/7/27 8:02
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
from selenium import webdriver
import time


options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(chrome_options=options)
driver.get('http://aaa.bbb.ccc/flow/privileges/')
driver.find_element_by_xpath("//*[@id='username']").send_keys('')
driver.find_element_by_xpath("//*[@id='password']").send_keys('')
# driver.find_element_by_xpath("//*[@id='login']").click()
driver.find_element_by_name("submit").click()
driver.find_element_by_link_text("流程管理").click()
i = 0
x = 0
begin = time.time()
while True:
    end = time.time()
    i = end - begin
    if i < 28800:
        driver.find_element_by_link_text("我的审批单").click()
        # driver.find_element_by_name("btSelectAll").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='approval_table']/thead/tr/th[1]/div[1]/input").click()
        # driver.find_elements_by_class_name('selected')[0].click()
        driver.find_element_by_xpath("//button[@class='btn btn-success' and text()='通过' ] ").click()
        driver.refresh()
        driver.find_element_by_link_text("我的审批单").click()
        time.sleep(20)
        x = x+1
        print("已经循环了%d次，执行时长%d秒" % (x, i))
    else:
        print("已经自动审批了%d次，请重新运行程序!" % x)
        break
driver.close()
