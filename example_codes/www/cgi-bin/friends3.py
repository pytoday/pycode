#!/usr/bin/env python3
# coding=utf-8
# title          : friends3.py
# description    :
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/9/14 20:01
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import cgi
from urllib.parse import quote_plus


header = 'Content-Type: text/html\n\n'
url = '/cgi-bin/friends3.py'

errhtml = '''
<html>
<head><title>Friends list</title></head>
<body>
<h3>ERROR</h3>
<b>%s</b><p>
<form><input type=button value=back onclick="window.history.back()"></form>
</body>
</html>
'''

formhtml = '''
<html>
<head><title>Friend list</title></head>
<body>
<h3>Friends list for: <i>%s</i></h3>
<form action="%s">
<b>Enter you name:</b>
<input type=hidden name=action value=edit>
<input type=text name=person value="%s" size=15><p>
<b>How many friends do you have? </b> %s <p>
<input type=submit>
</form>
</body>
</html>
'''

fradio = '<input type=radio name=howmany value="%s" %s> %s\n'

reshtml = '''
<html>
<head><title>Friend list</title></head>
<body>
<h3>Friend list for: <i>%s</i></h3>
your name is <b>%s</b><p>
you have <b>%s</b> friends<p>
Click <a href="%s">here</a> to edit your data agin.
</body>
</html>
'''


def show_error(error_str):
    print(header + errhtml % error_str)


def show_form(who, howmany):
    friends = []
    for i in (0, 10, 25, 50, 100):
        checked = ''
        if str(i) == howmany:
            checked = 'CHECKED'
        friends.append(fradio % (str(i), checked, str(i)))
    print('%s%s' % (header, formhtml % (who, url, who, ''.join(friends))))


def do_results(who, howmany):
    newurl = url + '?action=reedit&person=%s&howmany=%s' % (quote_plus(who), howmany)
    print(header + reshtml % (who, who, howmany, newurl))


def process():
    error = ''
    form = cgi.FieldStorage()
    if 'person' in form:
        who = form['person'].value.title()
    else:
        who = 'New user'
    if 'howmany' in form:
        howmany = form['howmany'].value
    else:
        if 'action' in form and form['action'].value == 'edit':
            error = "Please select number of friends."
        else:
            howmany = 0
    if not error:
        if 'action' in form and form['action'].value != 'reedit':
            do_results(who, howmany)
        else:
            show_form(who, howmany)
    else:
        show_error(error)


if __name__ == '__main__':
    process()
