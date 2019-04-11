# _*_coding:UTF-8 _*_
# 开发人员 : sdau_
# 编写时间:  2019/4/11 19:50
# 文件名称:  read_txt.py

import sys
result = []
with open(r'C:\Users\sdau_\Desktop\ne_list_NBI_CI-NBM-64_20190411161159.txt', 'r') as f:
    temp_result = f.readlines()
    for line in temp_result:
        result.append(line.strip("\n").split()[0])
    #print(result)

    res = '|'.join(result)
    print(res)
    open('cdays-4-result.txt', 'w').write(res)




