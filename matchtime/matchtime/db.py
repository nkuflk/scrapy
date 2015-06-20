#!/usr/bin/env python
# encoding: utf-8

import MySQLdb

matchtime = """create table if not exists matchtime (
                id int auto_increment not null primary key,
                md5 char(40),
                date char(20),
                time char(20),
                name varchar(100))"""

matchtime_tag = """create table if not exists matchtime_tag (
                    id int auto_increment not null primary key,
                    md5 char(40),
                    tag varchar(50))"""


class DB():

    def __init__(self):
        self.db = MySQLdb.connect('localhost', 'root', 'love', 'matchtime')
        cur = self.getCur()
        cur.execute(matchtime)
        cur.execute(matchtime_tag)

    def getCur(self):
        return self.db.cursor()
