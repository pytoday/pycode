#!/usr/bin/env python3
# coding=utf-8
# title          :dynamicHtml.py
# description    :
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/11/14 15:52
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import dryscrape
from bs4 import BeautifulSoup


url = "http://www.ziyoubaba.com/2016/05/29/python_catch_js"


def get_text_line(html):
    soup = BeautifulSoup(html)
    text_line = soup.find('span', id='text_line')  # 找到id='text_line'的span标签
    print(text_line.text)   # 打印出来该span标签的文本


def get_url_dynamic(url):
    session_req = dryscrape.Session()
    session_req.visit(url)  # 请求页面
    response = session_req.body()  # 网页的文本
    # print(response)
    return response


get_text_line(get_url_dynamic(url))  # 将输出一条文本
