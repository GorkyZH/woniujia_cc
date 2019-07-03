#coding:utf-8

from util.operation_excel import OperationExcel
from data import data_config
from util.operation_json import OperationJson

"""封装获取接口数据"""
class GetData:
    def __init__(self, json_file, sheet_name):
        self.operation_excel = OperationExcel(sheet_name)
        self.json_file = json_file

    #获取excel行数
    def get_case_line(self):
        return self.operation_excel.get_lines()

    #获取模块
    def get_model(self, row):
        col = int(data_config.get_module())
        return self.operation_excel.get_cell_value(row, col)

    #获取是否执行
    def get_is_run(self, row):
        flag = None
        col = int(data_config.get_run())
        run_model = self.operation_excel.get_cell_value(row, col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    #获取是否携带header
    def get_header(self, row):
        col = int(data_config.get_header())
        header = self.operation_excel.get_cell_value(row, col)
        if header == 'yes':
            return data_config.get_header_value()
        else:
            return None

    #获取携带token的header
    def get_token_header(self, row, token_value):
        col = int(data_config.get_header())
        header = self.operation_excel.get_cell_value(row, col)
        if header == 'yes':
            return data_config.get_token_header_value(token_value)
        else:
            return None

    #获取请求类型
    def get_request_type(self, row):
        col = int(data_config.get_request_type())
        return self.operation_excel.get_cell_value(row, col)

    #获取url
    def get_url(self, row):
        col = int(data_config.get_url())
        return self.operation_excel.get_cell_value(row, col)

    #获取请求参数
    def get_parameter(self, row):
        col = int(data_config.get_parameter())
        data = self.operation_excel.get_cell_value(row, col)
        if data == '':
            return None
        return data

    #通过关键字拿到data数据
    def get_data_for_json(self, row):
        oper_json = OperationJson(self.json_file)
        data_json = oper_json.get_data(self.get_parameter(row))
        return data_json

    #获取预期结果
    def get_except(self, row):
        col = int(data_config.get_except())
        except_data = self.operation_excel.get_cell_value(row, col)
        if except_data == '':
            return None
        return except_data

    #写入实际结果
    def write_result(self, row, value, sheet_id):
        col = int(data_config.get_result())
        self.operation_excel.write_value(row, col, value, sheet_id)

    #写入实际返回结果
    def write_response(self, row, value, sheet_id):
        col = int(data_config.get_response())
        self.operation_excel.write_value(row, col, value, sheet_id)

    #获取依赖的返回数据
    def get_dependent_data(self, row, index):
        col = int(data_config.get_data_dependent())
        #dependent_data = self.operation_excel.get_cell_value(row, col)
        dependent_data = self.operation_excel.get_cell_value_more(row, col, index)
        if dependent_data == '':
            return None
        return dependent_data

    #判断是否存在依赖case
    def is_depend(self, row):
        col = int(data_config.get_case_dependent())
        dependent_case_id = self.operation_excel.get_cell_value(row, col)
        if dependent_case_id == '':
            return None
        return dependent_case_id

    # 判断是否存在2个依赖case
    def is_more_depend(self, row, index=None):
        col = int(data_config.get_case_dependent())
        dependent_case_value = self.operation_excel.get_cell_value_more(row, col, index)
        if dependent_case_value == '':
            return None
        if ',' in dependent_case_value:
            dependent_case_id = dependent_case_value.split(',', 1)[index]
            return dependent_case_id
        else:
            return dependent_case_value

    # 获取依赖的字段
    def get_dependent_key(self, row, index=None):
        col = int(data_config.get_key_dependent())
        dependent_key = self.operation_excel.get_cell_value(row, col)
        if dependent_key == '':
            return None
        if ',' in dependent_key:
            dependent_key_id = dependent_key.split(',')[index]
            return dependent_key_id
        else:
            return dependent_key








