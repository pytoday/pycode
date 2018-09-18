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

    def showerror(self):
        print(AdvCgi.header + AdvCgi.errhtml % self.error)

    reshtml = '''
    <html>
    <head><title>Cookie CGI Demo</title></head>
    <body>
   <h2>Your upload data</h2>
   <h3>your name is <b>%s</b></h3> 
   <h3>your can program in the follow lang:</h3>
   <ul>%s</ul>
   <h3>you uploaded file...<br> Name: <i>%s</i><br>Contents:</h3>
   <pre>%s</pre>
   Click<a href="%s"><b>here</b></a>
    </body>
    </html>
    '''

    def setcppcookies(self):
        for eachcook in self.cookies.keys():
            print('Set-Cookie: CPP%s=%s; path=/' % (eachcook, quote(self.cookies[eachcook])))

    def doresult(self):
        maxbyte = 4096
        langlist = ''.join('<li>%s<br>' % eachlang for eachlang in self.langs)
        filedata = self.fp.read(maxbyte)
        if len(filedata) == maxbyte:
            filedata = '%s%s' % (filedata, '...<b><i>(file truncated due to size)</i></b>')
            self.fp.close()
        if filedata == '':
            filedata = '<b><i>(file not given or upload error)</i></b>'
        filename = self.fn

        if not ('user' in self.cookies and self.cookies['user']):
            cookstatus = '<i>(cookie has not been set yet)</i>'
            usercook = ''
        else:
            usercook = cookstatus = self.cookies['user']

        self.cookies['info'] = ':'.join((self.who, ','.join(self.langs, ','), filename))
        self.setcppcookies()
        print('%s%s' % (AdvCgi.header, AdvCgi.reshtml % (cookstatus, self.who, langlist, filename, filedata, AdvCgi.url)))

    def go(self):
        self.cookies = {}
        self.error = []
        form = FieldStorage()
        if not form.keys():
            self.showform()
            return

        if 'person' in form:
            self.who = form['person'].value.strip().title()
            if self.who == '':
                self.error = 'your name is required.(blank)'
            else:
                self.error = 'your name is required.(missing)'
        self.cookies['user'] = unquote(form['cookies'].value.strip()) if 'cookie' in form else ''
        if 'lang' in form:
            langdata = form['lang']
            if isinstance(langdata, list):
                self.langs = [eachlang.value for eachlang in langdata]
            else:
                self.langs = [langdata.value]
        else:
            self.error = 'At lease one language required.'
        if 'upfile' in form:
            upfile = form['upfile']
            self.fn = upfile.filename or ''
            if upfile.file:
                self.fp = upfile.file
            else:
                self.fp = StringIO('(no data)')
        else:
            self.fp = StringIO('(no data)')
            self.fn = ''
        if not self.error:
            self.doresult()
        else:
            self.showerror()


if __name__ == '__main__':
    page = AdvCgi()
    page.go()
