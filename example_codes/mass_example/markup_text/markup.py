#!/usr/bin/env python3
# coding=utf-8
# title          :markup.py
# description    :
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/11/30 下午9:23
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import sys
import re
from handlers import *
from util import *
from rules import *


class Parser:
    """
    读取文本，应用规则且控制handlers
    """
    def __init__(self, handler):
        self.handler = handler
        self.rules = []
        self.filters = []

    def addRule(self, rule):
        self.rules.append(rule)

    def addFilter(self, pattern, name):
        def filter(block, handler):
            return re.sub(pattern, handler.sub(name), block)
        self.filters.append(filter)

    def parse(self, file):
        self.handler.start('document')
        for block in blocks(file):
            for filter in self.filters:
                block = filter(block, self.handler)
            for rule in self.rules:
                if rule.condition(block):
                    last = rule.action(block, self.handler)
                    if last:
                        break
        self.handler.end('document')


class BasicTextParser(Parser):
    """
    在构造函数中增加规则和过滤器的具体语法分析器
    """
    def __init__(self, handler):
        Parser.__init__(self, handler)
        self.addRule(ListRule())
        self.addRule(ListItemRule())
        self.addRule(TitleRule())
        self.addRule(HeadingRule())
        self.addRule(ParagraphRule())

        self.addFilter(r'\*(.+?)\*', 'emphasis')
        self.addFilter(r'(https://[\.a-zA-Z]+)', 'url')
        self.addFilter(r'(http://[\.a-zA-Z]+)', 'url')
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z])', 'email')


handler = HTMLRenderer()
parser = BasicTextParser(handler)

parser.parse(sys.stdin)
