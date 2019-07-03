# coding:utf-8
from data.get_data import GetData
from util.common_util import CommonUtil
from base.run_method import RunMethod
from data.dependent_data import DependentData
from util.send_email import SendEmail
import json

class RunCommon:
    def __init__(self, json_file, sheet_name, sheet_id):
        # self.excel_file = excel_file
        self.json_file = json_file
        self.sheet_name = sheet_name
        self.sheet_id = sheet_id
        self.data = GetData(self.json_file, self.sheet_name)
        self.run_method = RunMethod()
        self.util = CommonUtil()
        self.email = SendEmail()

    def go_run_case(self):
        # 获取用例行数
        row_count = self.data.get_case_line()
        pass_count = []
        fail_count = []
        # 循环用例
        for i in range(1, row_count):
            # 获取isrun，是否运行该用例
            is_run = self.data.get_is_run(i)
            if is_run:
                #model = self.data.get_model(i)
                url = self.data.get_url(i)
                data = self.data.get_data_for_json(i)
                request_type = self.data.get_request_type(i)
                if i == 1:
                    header = self.data.get_header(i)
                    #request_data = self.data.get_data_for_json(i)
                    response = self.run_method.run_main(request_type, url, data, header)
                    print("返回结果：", response)
                    res = json.loads(response)
                    # 获取token、operid并写入文件中
                    with open(self.util.base_dir(), 'w') as f:
                        f.write(res["data"]["token"] + "," + res["data"]["id"])
                    print("获取token：", res["data"]["token"])
                else:
                    token = self.util.getToken(0)
                    operid = self.util.getToken(1)
                    token_header = self.data.get_token_header(i, token)
                    depend_morecase = self.data.is_more_depend(i, 0)
                    #判断是否存在依赖
                    if depend_morecase != None:
                        self.depend_data = DependentData(depend_morecase, self.sheet_name, self.json_file)
                        dependent_response_data = self.depend_data.get_data_for_key(i, 0)
                        depend_key = self.data.get_dependent_key(i, 0)
                        print("depend_key", depend_key)
                        jsonData = json.loads(data)
                        print("data:", data)
                        jsonData[depend_key] = dependent_response_data
                        requestData = json.dumps(jsonData)
                        response = self.run_method.run_main(request_type, url, requestData, token_header)
                    else:
                        if self.data.get_model(i) == "用户更新":
                            jsonData = json.loads(data)
                            jsonData['id'] = operid
                            requestData = json.dumps(jsonData)
                            response = self.run_method.run_main(request_type, url, requestData, token_header)
                        else:
                            response = self.run_method.run_main(request_type, url, data, token_header)
                expect_res = self.data.get_except(i)
                print("期望结果：", expect_res)
                if self.util.is_contain(expect_res, response):
                    self.data.write_result(i, "测试通过", self.sheet_id)
                    pass_count.append(i)
                    print("测试通过")
                else:
                    self.data.write_result(i, "测试失败", self.sheet_id)
                    fail_count.append(i)
                    print("测试失败")
                self.data.write_response(i, response, self.sheet_id)
        #self.email.send_main(pass_count, fail_count)
        return response

if __name__ == '__main__':
    run = RunCommon()
    run.go_run_case()
