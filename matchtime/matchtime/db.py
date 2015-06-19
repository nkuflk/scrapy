#!/usr/bin/env python
# encoding: utf-8

import MySQLdb


class DB():

    def __init__(self):
        self.db = MySQLdb.connect('localhost', 'root', 'love', 'matchtime')

    def getCur(self):
        return self.db.cursor()
