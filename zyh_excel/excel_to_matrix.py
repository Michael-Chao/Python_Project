import numpy as np
import pandas as pd
import xlrd
from sklearn import preprocessing

def excel_to_matrix(path):
    table = xlrd.open_workbook(path).sheets()[0]#获取第一个sheet表
    row = table.nrows#行数
    col = table.ncols#列数
    datamatrix = np.zeros((row, col))#生成一个nrows行ncols列，且元素均为0的初始矩阵
    for x in range(col):
        cols = np.matrix(table.col_values(x))
        datamatrix[:, x] = cols#按列把数据存进矩阵中
    print(datamatrix)
    #数据归一化


datafile = "D:\\python_project\\zyh_excel\\excelFile.xlsx"
excel_to_matrix(datafile)