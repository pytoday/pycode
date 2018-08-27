#!/usr/bin/env python3
# coding=utf-8
# title          : ushuffle_orm.py
# description    :
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/8/14 14:57
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
from os.path import dirname
from random import randrange as rand
from sqlalchemy import Column, Integer, String, create_engine, exc, orm
from sqlalchemy.ext.declarative import declarative_base
from unshuffle_db import DBNAME, NAMELEN, randname, FIELEDS, tformat, cformat, setup


DSNs = {
    'mysql': 'mysql://root@localhost/%s' % DBNAME,
    'sqlite': 'sqlite:///:memory:',
}

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    login = Column(String(NAMELEN))
    userid = Column(Integer, primary_key=True)
    projid = Column(Integer)

    def __str__(self):
        return ''.join(map(tformat, (self.login, self.userid, self.projid)))


class SQLAlchemyTest:
    def __init__(self, dsn):
        try:
            eng = create_engine(dsn)
        except ImportError:
            raise RuntimeError()
        try:
            eng.connect()
        except exc.OperationalError:
            eng = create_engine(dirname(dsn))
            eng.execute('creater database %s' % DBNAME).close()
            eng = create_engine(dsn)

        session = orm.sessionmaker(bind=eng)
        self.ses = session()
        self.users = Users.__table__
        self.eng = self.users.metadata.bind = eng

    def insert(self):
        self.ses.add_all(Users(login=who, userid=userid, projid=rand(1, 5)) for who, userid in randname())
        self.ses.commit()

    def update(self):
        fr = rand(1, 5)
        to = rand(1, 5)
        i = -1
        users = self.ses.query(Users).filter_by(projid=fr).all()
        for i, user in enumerate(users):
            user.projid = to
        self.ses.commit()
        return fr, to, i+1

    def delete(self):
        rm = rand(1, 5)
        i = -1
        users = self.ses.query(Users).filter_by(projid=rm).all()
        for i, user in enumerate(users):
            self.ses.delete(user)
        self.ses.commit()
        return rm, i+1

    def dbdump(self):
        print('\n%s' % ''.join(map(cformat, FIELEDS)))
        users = self.ses.query(Users).all()
        for user in users:
            print(user)
        self.ses.commit()

    def __getattr__(self, attr):
        return getattr(self.users, attr)

    def finish(self):
        self.ses.connection().close()


def main():
    print("*** Connect to %r database." % DBNAME)
    db = setup()
    if db not in DSNs:
        print("%r not supported" % db)
        return

    try:
        orm = SQLAlchemyTest(DSNs[db])
    except RuntimeError:
        print("%r not supported" % db)
        return

    print("create table")
    orm.drop(checkfirst=True)
    orm.create()
    print("insert.")
    orm.insert()
    orm.dbdump()
    print("move and update")
    fr, to, num = orm.update()
    orm.dbdump()
    print("delete")
    rm, num = orm.delete()
    orm.dbdump()
    print("drop table")
    orm.drop()
    orm.finish()


if __name__ == '__main__':
    main()
