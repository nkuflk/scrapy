#!/usr/bin/env python
# encoding: utf-8

import MySQLdb

matchtime = """create table if not exists matchtime (
                id int auto_increment not null primary key,
                md5 char(40),
                date char(20),
                time char(20),
                name varchar(100)) character set = utf8"""

matchtime_tag = """create table if not exists matchtime_tag (
                    id int auto_increment not null primary key,
                    md5 char(40),
                    tag varchar(50)) character set = utf8"""


class DB():
    insert_matchtime = 'insert into matchtime(md5,date,time,name) values("%s","%s","%s","%s");'
    select_match_by_md5 = 'select * from matchtime where md5="%s";'

    def __init__(self):
        self.db = MySQLdb.connect('localhost', 'root', 'love', 'matchtime')
        self.cur = self.getCur()
        self.createTables()

    def __del__(self):
        self.cur.close()
        self.db.close()

    def createTables(self):
        self.cur.execute(matchtime)
        self.cur.execute(matchtime_tag)

    def getCur(self):
        return self.db.cursor()
