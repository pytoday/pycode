#!/usr/bin/env python3
# coding=utf-8
# title          : cookies_cgi.py
# description    : cookies example for cgi
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/9/18 4:58
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
from cgi import FieldStorage
from os import environ
from urllib.request import quote, unquote
from io import StringIO


class AdvCgi:
    header = 'Content-Type: text/html\n\n'
    url = '/cgi-bin/cookies_cgi.py'

    formhtml = '''
    <html>
    <head><title>Cookies CGI Demo</title></head>
    <body><h2>Cookies CGI Demo Form</h2>
    <form method=post action="%s" enctype="multipart/form-data">
    <h3>My cookie setting</h3>
    <li><code><b>CPPuser = %s </b></code>
    <h3>Enter cookie value<br><input name=cookie value="%s">(<i>optional</i>)</h3>
    <h3>Enter your name<br><input name=person value="%s">(<i>optional</i>)</h3>
    <h3>What languages can you program in?(<i>at lease one required</i>)</h3>
    %s
    <h3>Enter file to upload <small>(max size 4k)</small></h3>
    <input type=file name=upfile value="%s" size=45>
    <p><input type=submit>
    </form>
    </body>
    </html>
    '''

    langset = ('Python', 'Ruby', 'Java', 'C++', 'PHP')
    langitem = '<input type=checkbox name=lang value="%s"%s> %s\n'

    def getcppcookies(self):
        if 'HTTP_COOKIE' in environ:
            cookies = [x.xtrip for x in environ['HTTP_COOKIE'].split(';')]
            for eachecookie in cookies:
                if len(eachecookie) > 6 and eachecookie[:3] == 'CPP':
                    tag = eachecookie[3:7]
                    try:
                        self.cookies[tag] = eval(unquote(eachecookie[8:]))
                    except (NameError, SyntaxError):
                        self.cookies[tag] = unquote(eachecookie[8:])
                if 'info' not in self.cookies:
                    self.cookies['info'] = ''
                if 'user' not in self.cookies:
                    self.cookies['user'] = ''
        else:
            self.cookies['info'] = self.cookies['user'] = ''
        if self.cookies['info'] != '':
            self.who, langstr, self.fn = self.cookies['info'].split(';')
            self.langs = langstr.split(',')
        else:
            self.who = self.fn = ''
            self.langs = ['Python']

    def showform(self):
        self.getcppcookies()

        langstr = []
        for eachlang in AdvCgi.langitem:
            langstr.append(AdvCgi.langitem % (eachlang, ' CHECKED' if eachlang in self.langs else '', eachlang))

        if not ('user' in self.cookies and self.cookies['user']):
            cookstatus = '<i>(cookie has not been set yet)</i>'
            usercook = ''
        else:
            usercook = cookstatus = self.cookies['user']
        print('%s%s' % (AdvCgi.header, AdvCgi.formhtml % (AdvCgi.url, cookstatus, usercook, self.who, ''.join(langstr), self.fn)))

        errhtml = '''
        <html><head><title>Cookies CGI Demo</title></head>
        <body>
        <h3>ERROR</h>
        <b>%s</b><p>
        <form><input type=button value=back onclick="window.history.back()></form>
        </body>
        </html>
        '''

    def go(self):
        pass


if __name__ == '__main__':
    page = AdvCgi()
    page.go()
