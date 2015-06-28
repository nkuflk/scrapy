#!/usr/bin/env python
# encoding: utf-8

import sqlite3
import os
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2

salt = b'saltysalt'
iv = b' ' * 16
length = 16

my_pass = 'love'
my_pass = my_pass.encode('utf8')

iterations = 1003


def clean(x):
    return x[:-x[-1]].decode('utf8')

def getValue(value):
    encrypted_value = value[3:]
    key = PBKDF2(my_pass, salt, length, iterations)
    cipher = AES.new(key, AES.MODE_CBC, IV=iv)
    decrypted = cipher.decrypt(encrypted_value)
    print(clean(decrypted))


def get_chrome_cookies():
    os.system('cp ~/Library/Application\ Support/Google/Chrome/Default/Cookies .')
    conn = sqlite3.connect('Cookies')
    cookies_list = []
    for row in conn.execute('select name, encrypted_value from cookies where host_key like ".alibaba-inc.com"'):
        cookies_list.append(row)
        getValue(row[1])
    # cookies.update(cookies_list)

get_chrome_cookies()
