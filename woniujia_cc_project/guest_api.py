# coding:utf-8
from data.get_data import GetData
from util.common_util import CommonUtil
from base.run_method import RunMethod
from data.dependent_data import DependentData
import json

class GuestApi:
    def __init__(self):
        self.excel_file = "/Users/mac/Desktop/测试资料/蜗牛家产品线/woniujia_cc_jiekou/woniujia_cc_jiekou_git/woniujia_cc_project/dataconfig/guest.xls"
        self.json_file = "/Users/mac/Desktop/测试资料/蜗牛家产品线/woniujia_cc_jiekou/woniujia_cc_jiekou_git/woniujia_cc_project/dataconfig/guest.json"
        self.data = GetData(self.excel_file, self.json_file)
        self.run_method = RunMethod()
        self.util = CommonUtil()

    def go_to_guest(self):
        # self.run_comm = RunCommon(self.excel_file, self.json_file)
        # self.run_comm.go_run_case()
        # 获取用例行数
        row_count = self.data.get_case_line()
        for i in range(1, row_count):
            is_run = self.data.get_is_run(i)
            if is_run:
                url = self.data.get_url(i)
                request_type = self.data.get_request_type(i)
                data = self.data.get_data_for_json(i)
                if i == 1:
                    header = self.data.get_header(i)
                    response = self.run_method.run_main(request_type, url, data, header)
                    res = json.loads(response)
                    # 获取token、operid并写入文件中
                    with open(self.util.base_dir(), 'w') as f:
                        f.write(res["data"]["token"] + "," + res["data"]["id"])
                else:
                    token = self.util.getToken(0)
                    token_header = self.data.get_token_header(i, token)
                    depend_morecase = self.data.is_more_depend(i, 0)
                    # 判断是否存在依赖
                    if depend_morecase != None:
                        self.depend_data = DependentData(depend_morecase, self.excel_file, self.json_file)
                        dependent_response_data = self.depend_data.get_data_for_key(i, 0)
                        depend_key = self.data.get_dependent_key(i, 0)
                        print("depend_key", depend_key)
                        if url == "http://182.61.33.241:8089/app/api/private/1.0/client/":
                            request_url = url + dependent_response_data
                            response = self.run_method.run_main(request_type, request_url, data, token_header)
                        if url == "http://182.61.33.241:8089/app/api/private/1.0/reporting/addorupdate":
                            depend_param2 = self.data.is_more_depend(i, 1)
                            self.depend_data2 = DependentData(depend_param2, self.excel_file, self.json_file)
                            dependent_response_data2 = self.depend_data2.get_data_for_key(i, 1)
                            depend_key2 = self.data.get_dependent_key(i, 1)
                            jsonData = json.loads(data)
                            jsonData[depend_key] = dependent_response_data
                            jsonData[depend_key2] = dependent_response_data2
                            requestData = json.dumps(jsonData)
                            response = self.run_method.run_main(request_type, url, requestData, token_header)
                        else:
                            jsonData = json.loads(data)
                            print("data:", data)
                            jsonData[depend_key] = dependent_response_data
                            requestData = json.dumps(jsonData)
                            response = self.run_method.run_main(request_type, url, requestData, token_header)
                    else:
                        if url == "http://182.61.33.241:8089/app/api/private/1.0/follow/clientpage":
                            oper_id = self.util.getToken(1)
                            json_data = json.loads(data)
                            json_data["operId"] = oper_id
                            request_data = json.dumps(json_data)
                            response = self.run_method.run_main(request_type, url, request_data, token_header)
                        else:
                            response = self.run_method.run_main(request_type, url, data, token_header)

                expect_res = self.data.get_except(i)
                print("期望结果：", expect_res)
                if self.util.is_contain(expect_res, response):
                    self.data.write_result(i, "测试通过")
                    print("测试通过")
                else:
                    self.data.write_result(i, "测试失败")
                    print("测试失败")
                self.data.write_response(i, response)
        return response

if __name__ == '__main__':
    guest = GuestApi()
    guest.go_to_guest()
