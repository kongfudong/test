#_*_coding:UTF-8 _*_
#开发人员 : sdau_
#编写时间:  2019/3/30 15:44
#文件名称:  111.py



import chardet

for i in ['abc123', '中国']:
   print(i, chardet.detect(i))