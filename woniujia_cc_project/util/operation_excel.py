# coding=utf-8

import xlrd
from xlutils.copy import copy

"""
读取excel文件工具类
"""
class OperationExcel:
    def __init__(self, sheet_name=None, file_name=None):
        if file_name:
            self.file_name = file_name
            self.sheet_name = sheet_name
        else:
            # self.file_name = '../dataconfig/case02.xls'
            self.file_name = '/Users/mac/Desktop/测试资料/蜗牛家产品线/woniujia_cc_jiekou/woniujia_cc_jiekou_git/woniujia_cc_project/dataconfig/testcase.xls'
            self.sheet_name = sheet_name
        self.data = self.get_data()

    # 获取sheet的内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        #tables = data.sheets()[self.sheet_id]
        tables = data.sheet_by_name(self.sheet_name)
        return tables

    # 获取单元格的行数
    def get_lines(self):
        tables = self.data
        return tables.nrows

    # 获取某一个单元格的内容
    def get_cell_value(self, row, col):
        tables = self.data
        return tables.cell_value(row, col)

    # 获取某一个单元格的2个内容
    def get_cell_value_more(self, row, col, index=None):
        tables = self.data
        cell_data = tables.cell_value(row, col)
        if ',' in cell_data:
            cell_value = cell_data.split(',', 1)[index]
            return cell_value
        else:
            return cell_data

    # 往单元格中写入数据
    def write_value(self, row, col, value, sheet_id):
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(sheet_id)
        sheet_data.write(row, col, value)
        write_data.save(self.file_name)

    # 根据对应的case_id找到对应行的内容
    def get_rows_data(self, case_id):
        row_num = self.get_row_num(case_id)
        rows_data = self.get_row_values(row_num)
        return rows_data

    # 根据对应的case_id找到对应的行号
    def get_row_num(self, case_id):
        num = 0
        cols_data = self.get_cols_data()
        for col_data in cols_data:
            if case_id in col_data:
                return num
            num = num + 1

    # 根据行号找到该行内容
    def get_row_values(self, row):
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

    # 根据列号获取某一列的内容
    def get_cols_data(self, col_id=None):
        if col_id != None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(1)
        return cols


if __name__ == '__main__':
    opers = OperationExcel("login")
    print(opers.get_lines())
    print(opers.get_cell_value(4, 7))
    print(opers.get_cell_value_more(3, 7))
