# encoding: utf-8
'''
@author: Jeremiah
@file: Utils.py
@time: 2018/6/28 13:57
@desc:
'''

import datetime
from re import sub
from html.parser import unescape
from urllib.parse import quote, unquote
from re import split
def htmlParser(string):
    return unescape(string)

def urlEncode(string):
    return quote(string).encode('utf-8')

def urlDecode(string):
    return unquote(string)

def getCurrentTime():
    currentTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return currentTime

def codeUnFormat(string):
    if string:
        return sub('\s+', ' ', string.strip(), count=0)
    return None

def getUpdateLog():
    try:
        with open('updateLog.txt', encoding='utf-8') as f:
            result = f.read()
            if result:
                return result
    except:
        return None


def formatHeaders(string):
    result = ''
    try:
        list = split('\n', string)
        for str in list:
            result = result + '\'' + str.replace(': ', '\': \'') + '\',\n'
        return result
    except:
        return None

