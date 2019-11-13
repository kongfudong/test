# _*_ coding:utf-8 _*_
__author__ = 'wudong'
__date__ = '2019-11-13 21:27'

import difflib

filename1 = '/tmp/passwd'
filename2 = '/tmp/passwd1'

with open(filename1) as f1,open(filename2) as f2:
    content1 = f1.read().splitlines(keepends=True)
    content2 = f2.read().splitlines(keepends=True)

d = difflib.HtmlDiff()
htmlContent = d.make_file(content1,content2)

with open('passwdDiff.html','w') as f:
    f.write(htmlContent)
