#coding=utf-8
from util.operation_excel import OperationExcel
from base.run_method import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
from jsonpath_rw import jsonpath,parse
import json

"""
数据依赖类
"""
class DependentData:
    def __init__(self, case_id, sheet_name, json_file):
        self.oper_excel = OperationExcel(sheet_name)
        self.util = CommonUtil()
        self.case_id = case_id
        self.data = GetData(json_file, sheet_name)

    # 通过case_id获取case_id的整行数据
    def get_case_line_data(self):
        rows_data = self.oper_excel.get_rows_data(self.case_id)
        return rows_data

    # 执行依赖测试，获取返回结果
    def run_dependent(self):
        run_method = RunMethod()
        row_num = self.oper_excel.get_row_num(self.case_id)
        print("row_num:", row_num)
        row_data = self.get_case_line_data()
        print("row_data:", row_data)
        request_data = self.data.get_data_for_json(row_num)
        print("request_data:", request_data)
        url = self.data.get_url(row_num)
        print("url:", url)
        method = self.data.get_request_type(row_num)
        print("method:", method)
        token_header = self.data.get_token_header(row_num, self.util.getToken(0))
        print("依赖的token_header:", token_header)
        res = run_method.run_main(method, url, request_data, token_header)
        print("res:", res)
        return json.loads(res)

    # 根据依赖的key去获取执行依赖测试case的响应，然后返回对应的返回值
    def get_data_for_key(self, row, index):
        dependent_data = self.data.get_dependent_data(row, index)
        print("dependent_data:", type(dependent_data))
        print("dependent_data:", dependent_data)
        response_data = self.run_dependent()
        print("response_data:", type(response_data))
        print("response_data:", response_data)
        json_exe = parse(dependent_data)
        madle = json_exe.find(response_data)
        return [math.value for math in madle][0]


if __name__ == '__main__':
    dependent = DependentData("case001")
    dependent.run_dependent()
    print(dependent.get_data_for_key(4, 1))

