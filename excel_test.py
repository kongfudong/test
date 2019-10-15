# -*- coding: utf-8 -*-
import xlrd  # 导入xlrd模块
import xlwt
import openpyxl
import pandas as pd

class ExcelData():
    def __init__(self, data_path, sheetname):
        self.data_path = data_path  # excle表格路径，需传入绝对路径
        self.sheetname = sheetname  # excle表格内sheet名
        self.data = xlrd.open_workbook(self.data_path)  # 打开excel表格
        self.table = self.data.sheet_by_name(self.sheetname)  # 切换到相应sheet
        self.keys = self.table.row_values(0)  # 第一行作为key值
        self.rowNum = self.table.nrows  # 获取表格行数
        self.colNum = self.table.ncols  # 获取表格列数
        # print(self.rowNum)
        # print(self.colNum)

    def readExcel(self):
        if self.rowNum < 2:
            print("excle内数据行数小于2")
        else:
            L = []  # 列表L存放取出的数据
            for i in range(1, self.rowNum):  # 从第二行（数据行）开始取数据
                sheet_data = {}  # 定义一个字典用来存放对应数据
                for j in range(self.colNum):  # j对应列值
                    sheet_data[self.keys[j]] = self.table.row_values(i)[j]  # 把第i行第j列的值取出赋给第j列的键值，构成字典
                L.append(sheet_data)  # 一行值取完之后（一个字典），追加到L列表中
            # print(type(L))
            return L

    def getRow(self, objectkey):
        result = []
        get_data = self.readExcel()
        for item in get_data:
            for k, v in item.items():
                if k == objectkey:
                    #print(v)
                    result.append(v)
        return result
    def writeExcel(self,result_path):
        result = self.getRow(data_key)
        ret = pd.value_counts(result)
        #print(ret)
        ret.to_excel(result_path,sheet_name="result")



if __name__ == '__main__':
    data_path = r"C:\Users\ezhawud\Desktop\2019北京积分落户公示名单.xlsx"  # 文件的绝对路径
    sheetname = "Sheet1"
    get_data = ExcelData(data_path, sheetname)  # 定义get_data对象
    # print(get_data.readExcel())
    data_key = "单位名称"
    result_path =  r"C:\Users\ezhawud\Desktop\2019北京积分落户公示名单_1.xlsx"
    get_data.writeExcel(result_path)
