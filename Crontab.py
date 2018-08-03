# encoding: utf-8
'''
@author: Jeremiah
@file: Crontab.py
@time: 2018/6/29 9:04
@desc:
'''
import json
import re
import requests


HEADERS = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'www.atool.org',
    'Referer': 'http://www.atool.org/crontab.php',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}

def getCrontab(string):

    if string and re.match(r'^(?:[\d\-/*,]+\s+){4}[\d\-/*,]+$', string):
        datas = {
            'c': string,
            't': '20'
        }
        try:
            r = requests.post('http://www.atool.org/include/crontab.inc.php', data=datas, headers=HEADERS)
            j = json.loads(r.content)
            list = j['c']

            i = 1
            result = ''
            for str in list:
                result = result + '第{}次执行：\t{}\n\n'.format(i, str)
                i = i + 1
            return result
        except:
            return None














