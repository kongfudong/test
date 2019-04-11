# -*- coding: utf-8 -*-
import urllib.request
import json


def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html


if __name__ == '__main__':
    key = '545854650f2740e58f2ae39d179875c0'
    api = 'http://www.tuling123.com/openapi/api?key=' + key + '&info='
    while True:
        info = input('我: ')
        request = api + info
        response = getHtml(request)
        dic_json = json.loads(response)
        print('机器人:'.encode('utf-8') + dic_json['text'])
