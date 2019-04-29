#!/usr/bin/env python3
# coding=utf-8
# title          : zentao_user_sync.py
# description    : create zentao user, add to permission group
# date           : 2019/4/12 20:54
# notes          :
# ==================================================

# Import the module needed to run the script
import pymysql
import time
from ldap3 import Server, Connection, ALL

# database config
DB_NAME = "db1"
DB_HOST = ""
DB_PORT = 3306
DB_USER = ""
DB_PASS = ""

# ldap server config
LDAP_HOST = "192.168.0.1"
LDAP_PORT = 389
LDAP_BASE = "dc=example,dc=com"
LDAP_DN = "cn=admin,"+LDAP_BASE
LDAP_PASS = "password"


class SyncUser:
    def __init__(self):
        self.connection = pymysql.connect(host=DB_HOST,
                                          port=DB_PORT,
                                          user=DB_USER,
                                          password=DB_PASS,
                                          db=DB_NAME,
                                          charset='utf8mb4',)

    def getuser(self):
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT `account` FROM `zt_user`"
                cursor.execute(sql)
                result = cursor.fetchall()
                all_user = []
                for each in result:
                    all_user.append(each[0])
            return set(all_user)
        except Exception as e:
            print(e)
            return 0

    def getldapuser(self):
        try:
            server = Server(host=LDAP_HOST, port=LDAP_PORT, get_info=ALL)
            conn = Connection(server, LDAP_DN, LDAP_PASS, auto_bind=True)
            conn.search(search_base=LDAP_BASE, search_filter='(&(objectclass=*)(cn=*))', attributes=['cn', 'email'])
            all_entries = conn.entries
            all_user = []
            for entry in all_entries:
                all_user.append(str(entry['cn']))
            return set(all_user)
        except Exception as e:
            print(e)
            return 0

    def createuser(self, username):
        try:
            with self.connection.cursor() as cursor:
                # Create a new record
                user_sql = "INSERT INTO `zt_user` (`dept`, `account`, `password`, `role`, `realname`, `nickname`,\
                           `commiter`, `avatar`, `email`, `skype`, `qq`, `yahoo`, `gtalk`, `wangwang`, `mobile`, \
                           `phone`, `address`, `zipcode`,`ip`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
                           %s, %s, %s, %s, %s, %s, %s)"
                group_sql = "INSERT INTO `zt_usergroup` (`account`, `group`) VALUES (%s, %s)"
                cursor.execute(user_sql, (0, username, 'somepassword', 'guest', username, '', '', '',
                                          username+'@example.com', '', '', '', '', '', '', '', '', '', '1.2.3.4'))
                cursor.execute(group_sql, (username, 11))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            self.connection.commit()
            print("user %s synced at %s." % (username, time.asctime()))
        except Exception as e:
            print(e)

    def batchuser(self):
        users = self.getldapuser() - self.getuser()
        for username in users:
            self.createuser(username)

    def close(self):
        self.connection.close()


if __name__ == '__main__':
    create_user = SyncUser()
    create_user.batchuser()
    create_user.close()
