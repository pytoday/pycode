#!/usr/bin/env python3
# coding=utf-8
# title          :util.py
# description    :
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/11/30 下午5:38
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script


def lines(file):
    # for line in xxx读取文本时line不带换行，使用yield line; yield '\n'为每行文本添加换行,否则文本块中多行当一行处理
    for line in file:
        yield line
        yield '\n'


def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            # 生成去除两边空格，带换行的文本块
            yield ''.join(block).strip()
            block = []
