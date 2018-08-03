# encoding: utf-8
'''
@author: Jeremiah
@file: TransByJere.py
@time: 2018/6/26 13:43
@desc:
'''

import requests
import json
from ParseJS import Py4js

MAIN_URL = 'https://translate.google.cn/translate_a/single?' + \
      'client=t&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md' + \
      '&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&otf=1&kc='

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'Host': 'translate.google.cn'
}

def checkLanguage(str):
    # 全英文
    if all(ord(c) < 128 for c in str):
        return True
    # 全中文
    if all('\u4e00' <= c <= '\u9fa5' for c in str):
        return False

    # 也可以用lambda：
    # if all(map(lambda c:'\u4e00' <= c <= '\u9fa5',str)):
    #    return False

def getData(url, param):
    try:
        r = requests.get(url, params=param, headers=HEADERS, timeout=2)
        return r.text
    except Exception:
        # print('连接失败~')
        return None

def parseJson(data):
    try:
        jsonData = json.loads(data)
    except:
        return 0
    result = []
    result.append(jsonData[0][0][0])  # 主翻译
    # 其他翻译
    if jsonData[1] is not None:
        for i in jsonData[1]:
            result.append(i)
    return result


def show(result):
    if result == 0:
        exit(0)
    print()
    print(result[0])
    print()
    length = len(result)
    if length > 1:
        for i in range(1, length):
            r = result[i]
            print('{}:'.format(r[0]))
            for j in r[2]:
                print('\t{}:{}'.format(j[0], j[1]))

def main(word):
    js = Py4js()
    tk = js.getTK(word)

    if checkLanguage(word):
        param = {'tk': tk, 'q': word, 'sl': 'en', 'tl': 'zh-CN', 'ssel': '0', 'tsel': '0'}
    else:
        param = {'tk': tk, 'q': word, 'sl': 'zh-CN', 'tl': 'en', 'ssel': '3', 'tsel': '3'}

    show(parseJson(getData(MAIN_URL, param)))





