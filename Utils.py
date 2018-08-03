# encoding: utf-8
'''
@author: Jeremiah
@contact: wuyiting@myhexin.com
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

def congratulations():
    week = str(datetime.datetime.now().weekday())
    switch = {
        '0': '\t\t\t恭喜吴一艇写日报！！！',
        '1': '\t\t\t恭喜廖义权写日报！！！',
        '2': '\t\t\t恭喜沈成写日报！！！',
        '3': '\t\t\t恭喜郑小兰写日报！！！',
        '4': '\t\t\t恭喜乌东宇写日报！！！',
        '5': '\t\t\t再次恭喜乌东宇写日报！！！',
        '6': '\t\t\t今天老子不上班！！！',
    }
    return switch[week]

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

