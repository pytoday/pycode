#!/usr/bin/env python3
# coding=utf-8
# title          : unshuffle_db.py
# description    :
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/8/8 13:38
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import os
from random import randrange as rand


COLSIZE = 10
FIELEDS = ('login', 'userid', 'projid')
DBMSs = {'m': 'mysql', 's': 'sqlite', 'g': 'gadfly'}
DBNAME = 'test'
DBUSER = 'root'
NAMELEN = 16
DB_EXC = None
NAMES = (
    ('asdfasdf', 2134123), ('2qersadf', 123452), ('dfsg2adf', 12345),
    ('asdg', 123456), ('qwetsdg', 2345324), ('2q3adsg', 2345),
)


tformat = lambda s: str(s).title().ljust(COLSIZE)
cformat = lambda s: str(s).upper().ljust(COLSIZE)


def setup():
    return DBMSs[input('''
    Choose a db system:
    (M)ySql
    (G)adfly
    (S)QLite
    Enter choice:''').strip().lower()[0]]


def connector(db, dbname):
    global DB_EXC
    dbdir = '%s_%s' % (db, dbname)

    if db == 'sqlite':
        try:
            import sqlite3
        except ImportError:
            return None

        DB_EXC = sqlite3
        if not os.path.isdir(dbdir):
            os.mkdir(dbdir)
        cxn = sqlite3.connect(os.path.join(dbdir, dbname))
    elif db == 'mysql':
        try:
            import pymysql
            import pymysql.err as DB_EXC
            try:
                cxn = pymysql.connect(user=DBUSER, db=DBNAME)
            except DB_EXC.InterfaceError:
                return None
        except ImportError:
            return None
    elif db == 'gadfly':
        try:
            from gadfly import gadfly
            DB_EXC = gadfly
        except ImportError:
            return None
        try:
            cxn = gadfly(dbname, dbdir)
        except IOError:
            cxn = gadfly()
            if not os.path.isdir(dbdir):
                os.mkdir(dbdir)
            cxn.startup(dbname, dbdir)
    else:
            return None
    return cxn


def create(cur):
    try:
        cur.execute('''
            create table users (
            login varchar(%d),
            userid integer, 
            projid integer)''' % NAMELEN)
    except DB_EXC.OpertionalError as e:
        drop(cur)
        create(cur)


def drop(cur):
    cur.execute('drop table users')
    return cur


def randname():
    pick = set(NAMES)
    while pick:
        yield pick.pop()


def insert(cur,db):
    if db == 'sqlite' or db == 'gadfly':
        cur.executemany("insert into users values(?, ?, ?)", [(who, uid, rand(1, 5)) for who, uid in randname()])
    elif db == 'mysql':
        cur.executemany("insert into users values(%s, %s, %s)", [(who, uid, rand(1, 5)) for who, uid in randname()])


getrc = lambda cur: cur.rowcount if hasattr(cur, 'rowcount') else -1


def update(cur):
    fr = rand(1, 5)
    to = rand(1, 5)
    cur.execute("update users set projid=%d where projid=%d" % (to, fr))
    return fr, to, getrc(cur)


def delete(cur):
    rm = rand(1, 5)
    cur.execute("delete from users where projid=%d" % rm)
    return rm, getrc(cur)


def dbdump(cur):
    cur.execute("select * from users")
    print('\n%s' % ' '.join(map(cformat, FIELEDS)))
    for data in cur.fetchall():
        print(' '.join(map(tformat, data)))


def main():
    db = setup()
    print('*** Connect to %r database' % db)
    cxn = connector(db, DBNAME)
    if not cxn:
        print("Error: %r not supported or unreachable, exit" % db)
        return
    cur = cxn.cursor()

    print('\n Creating users table')
    create(cur)

    print('\n Insert data')
    insert(cur, db)
    dbdump(cur)

    print('\n Randomly update')
    fr, to, num = update(cur)
    print('\t(%d users moved) from (%d) to (%d)' % (num, fr, to))
    dbdump(cur)

    print('\n Randomly delete')
    rm, num = delete(cur)
    print('\t(group #%d; %d users removed.' % (rm, num))
    dbdump(cur)

    print('\n*** Droping users table')
    drop(cur)
    print('\n Close cxn')
    cur.close()
    cxn.commit()
    cxn.close()


if __name__ == '__main__':
    main()

