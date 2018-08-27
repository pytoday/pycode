#!/usr/bin/env python3
# coding=utf-8
# title          :handlers.py
# description    :
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/11/30 下午6:50
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script


class Handler:
    """
    处理从Parser调用的对象的方法

    解释器会在每个块开始部分调用start()和end()方法，使用合适的块名作为参数。sub()方法用于正则表达式替换，返回合适的替换函数。
    """
    def callback(self, prefix, name, *args):
        method = getattr(self, prefix+name, None)
        if callable(method):
            return method(*args)

    def start(self, name):
        self.callback('start_', name)

    def end(self, name):
        self.callback('end_', name)

    def sub(self, name):
        def substitution(match):
            result = self.callback('sub_', name, match)
            if result is None:
                return match.group(0)
            return result
        return substitution


class HTMLRenderer(Handler):
    """
    用于生成html的具体处理程序

    HTMLRenderer内的方法都可以通过超类的start(), end(), sub()方法来访问。它们实现了用于html文档的基本标签。
    """
    def start_document(self):
        print('<html><head><title>...</title></head><body>')

    def end_document(self):
        print('</body></html>')

    def start_paragraph(self):
        print('<p>')

    def end_paragraph(self):
        print('</p>')

    def start_heading(self):
        print('<h2>')

    def end_heading(self):
        print('</h2>')

    def start_list(self):
        print('<ul>')

    def end_list(self):
        print('</ul>')

    def start_listitem(self):
        print('<li>')

    def end_listitem(self):
        print('</li>')

    def start_title(self):
        print('<h1>')

    def end_title(self):
        print('</h1>')

    def sub_emphasis(self, match):
        return '<em>%s</em>' % match.group(1)

    def sub_url(self, match):
        return '<a href="%s">%s</a>' % (match.group(1), match.group(1))

    def sub_email(self, match):
        return '<a href="mail to:%s">%s</a>' % (match.group(1), match.group(1))

    def feed(self, data):
        print(data)
