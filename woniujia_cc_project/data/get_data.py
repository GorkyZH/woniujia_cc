#coding:utf-8

from util.operation_excel import OperationExcel
from data import data_config
from util.operation_json import OperationJson
from util.connect_db import OperationMysql

"""封装获取excel中的数据"""
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

    # 获取是否连接数据库
    def get_is_conn_db(self, row):
        flag = None
        col = int(data_config.get_conn_db())
        conn_data_value = self.operation_excel.get_cell_value(row, col)
        if conn_data_value == 'yes':
            flag = True
            # self.get_data_for_json()
        else:
            flag = False
            # self.get_data_for_newjson()
        return flag

    #通过关键字拿到data数据
    def get_data_for_json(self, row):
        oper_json = OperationJson(self.json_file)
        data_json = oper_json.get_data(self.get_parameter(row))
        return data_json

    #通过关键字和修改请求参数值重新获取json中的请求数据
    def get_data_for_newjson(self, row, value):
        oper_json = OperationJson(self.json_file)
        data_json = oper_json.get_new_json(self.get_parameter(row), value)
        return data_json

    #获取预期结果
    def get_except(self, row):
        col = int(data_config.get_except())
        except_data = self.operation_excel.get_cell_value(row, col)
        # sql_value = "%万科%"
        # except_data = "select * from ymm_borough where city_id='62' AND is_checked = '1' AND borough_name LIKE '%s'" % sql_value
        if except_data == '':
            return None
        return except_data

    #通过sql获取预期结果
    def get_except_data_for_sql(self, row, sql_base):
        oper_mysql = OperationMysql(sql_base)
        except_data = self.get_except(row)
        result = oper_mysql.search_all(except_data)
        # if sql_value == '':
        #     result = oper_mysql.search_all(except_data)
        # else:
        #     result = oper_mysql.search_all(except_data % sql_value)
        return result

    # 写入实际结果
    def write_result(self, row, value, sheet_id):
        col = int(data_config.get_result())
        self.operation_excel.write_value(row, col, value, sheet_id)

    # 写入实际返回结果
    def write_response(self, row, value, sheet_id):
        col = int(data_config.get_response())
        self.operation_excel.write_value(row, col, value, sheet_id)

    # 获取依赖的返回数据
    def get_dependent_data(self, row, index):
        col = int(data_config.get_data_dependent())
        #dependent_data = self.operation_excel.get_cell_value(row, col)
        dependent_data = self.operation_excel.get_cell_value_more(row, col, index)
        if dependent_data == '':
            return None
        return dependent_data

    # 判断是否存在依赖case
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

    # 获取接口返回的字段
    def get_response_key(self, row, index=None):
        col = int(data_config.get_response_key())
        response_key = self.operation_excel.get_cell_value(row, col)
        if response_key == '':
            return None
        else:
            return response_key

    # 获取数据库中查询出的字段
    def get_sql_key(self, row, index=None):
        col = int(data_config.get_sql_key())
        sql_key = self.operation_excel.get_cell_value(row, col)
        if sql_key == '':
            return None
        # if ',' in sql_key:
        #     sql_key_id = sql_key.split(',')[index]
        #     return sql_key_id
        else:
            return sql_key

    # 获取对比类型
    def get_sql_type(self, row):
        col = int(data_config.get_sql_type())
        sql_type = self.operation_excel.get_cell_value(row, col)
        if sql_type == '':
            return None
        else:
            return sql_type







