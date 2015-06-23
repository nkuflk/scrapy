#!/usr/bin/env python
# encoding: utf-8

import sqlite3

matchtime = """create table if not exists matchtime (
                id integer primary key autoincrement not null,
                md5 char(40) not null,
                date char(20),
                time char(20),
                name varchar(100))"""

matchtime_tag = """create table if not exists matchtime_tag (
                    id integer primary key autoincrement not null,
                    md5 char(40) not null,
                    tag varchar(50))"""

matchtime_index = "create index if not exists matchtime_index on matchtime(md5);"

matchtime_tag_index = "create index if not exists matchtime_tag_index on matchtime_tag(md5);"

insert_matchtime = 'insert into matchtime(md5,date,time,name) values("%s","%s","%s","%s");'

select_match_by_md5 = 'select * from matchtime where md5="%s";'

update_match_by_md5 = 'update matchtime set date="%s", time="%s", name="%s" where md5="%s";'


class DB():

    def __init__(self):
        self.db = sqlite3.connect('matchtime.db')
        self.cur = self.db.cursor()
        self.createTables()

    def __del__(self):
        self.cur.close()
        self.db.close()

    def createTables(self):
        self.cur.execute(matchtime)
        self.cur.execute(matchtime_tag)
        self.cur.execute(matchtime_index)
        self.cur.execute(matchtime_tag_index)
        self.db.commit()

    def insertMatchtime(self, item):
        sql = insert_matchtime % (item['md5'], item['date'], item['time'], item['name'])
        self.cur.execute(sql)
        self.db.commit()

    def selectMatchtime(self, md5):
        sql = select_match_by_md5 % (md5)
        self.cur.execute(sql)
        return self.cur.fetchall()

    def updateMatchtime(self, item):
        sql = update_match_by_md5 % (item['date'], item['time'], item['name'], item['md5'])
        self.cur.execute(sql)
        self.db.commit()
