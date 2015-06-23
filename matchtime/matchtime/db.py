#!/usr/bin/env python
# encoding: utf-8

import sqlite3

matchtime = """create table if not exists matchtime (
                id int auto_increment primary key not null,
                md5 char(40) not null,
                date char(20),
                time char(20),
                name varchar(100))"""

matchtime_tag = """create table if not exists matchtime_tag (
                    id int auto_increment primary key not null,
                    md5 char(40) not null,
                    tag varchar(50))"""

matchtime_index = "create index if not exists matchtime_index on matchtime(md5);"

matchtime_tag_index = "create index if not exists matchtime_tag_index on matchtime_tag(md5);"


class DB():
    insert_matchtime = 'insert into matchtime(md5,date,time,name) values("%s","%s","%s","%s");'
    select_match_by_md5 = 'select * from matchtime where md5="%s";'

    def __init__(self):
        self.db = sqlite3.connect('matchtime.db')
        self.cur = self.db.cursor()
        self.createTables()
        print 'success'

    def __del__(self):
        self.cur.close()
        self.db.close()

    def createTables(self):
        self.cur.execute(matchtime)
        self.cur.execute(matchtime_tag)
        self.cur.execute(matchtime_index)
        self.cur.execute(matchtime_tag_index)
        self.db.commit()

    def getCur(self):
        return self.db.cursor()
