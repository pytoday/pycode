#!/usr/bin/env python3
# coding=utf-8
# title          :phantomjs.py
# description    :example of phantomjs
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/11/23 14:40
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


url = "http://quote.eastmoney.com/center/"


dcap = dict(DesiredCapabilities.PHANTOMJS)
UA = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
dcap["phantomjs.page.setttings.userAgent"] = UA

driver = webdriver.PhantomJS(executable_path=r'C:\Program Files (x86)\phantomjs\bin\phantomjs.exe',
                             desired_capabilities=dcap)
driver.get(url)
tables = driver.find_element_by_class_name("data-table")
print(tables.text)
