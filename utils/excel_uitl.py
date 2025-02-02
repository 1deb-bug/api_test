import  openpyxl

from conf.config import *


def  read_excel(file_name=EXCEL_FILE,sheet=SHEET):


    #打开excel的工作簿
    workbook=openpyxl.load_workbook(file_name)

    #打开工作簿的sheet页
    sheet=workbook[sheet]

    data=[]
    #提取用例数据的key
    keys=[cell.value for cell in  sheet[2]]

    #提取excel每一条测试用例的数据值
    for values  in  sheet.iter_rows(min_row=3,values_only=True):
        case=dict(zip(keys,values))

        #如果is_true为空，则不执行用例(实现分组执行测试用例)
        if case['is_true']:
            data.append(case)

    return   data


