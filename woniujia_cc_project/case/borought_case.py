# coding=utf-8
from data.get_data import GetData
from base.run_method import RunMethod
from util.common_util import CommonUtil
from util.send_email import SendEmail
from data.dependent_data import DependentData
import json

class BoroughtCase:
    def __init__(self):
        self.json_file = "/Users/mac/Desktop/测试资料/蜗牛家产品线/woniujia_cc_jiekou/woniujia_cc_jiekou_git/woniujia_cc_project/dataconfig/borought.json"
        self.sheet_name = "楼盘模块"
        self.sheet_id = 2
        self.data = GetData(self.json_file, self.sheet_name)
        self.run_method = RunMethod()
        self.util = CommonUtil()
        self.email = SendEmail()

    def go_to_borought(self):
        # 获取用例行数
        row_count = self.data.get_case_line()
        pass_count = []
        fail_count = []
        result = True
        # 循环用例
        for i in range(1, row_count):
            # 获取isrun，是否运行该用例
            is_run = self.data.get_is_run(i)
            if is_run:
                url = self.data.get_url(i)
                request_type = self.data.get_request_type(i)
                is_connect = self.data.get_is_conn_db(i)   # 获取是否连接数据库，若是则执行sql，若不是直接获取期望结果
                if is_connect:
                    token = self.util.getToken(0)
                    operid = self.util.getToken(1)
                    token_header = self.data.get_token_header(i, token)
                    depend_morecase = self.data.is_more_depend(i, 0)
                    expect_res = self.data.get_except_data_for_sql(i)  # 获取数据库返回的所有楼盘记录（返回类型：数组型）
                    expect_borough_name_list = []
                    for expect_index in range(0, len(expect_res)):
                        expect_borough_name = expect_res[expect_index]['borough_name']  # 循环获取数据库返回的楼盘名称
                        expect_borough_name_list.append(expect_borough_name)  # 将数据库中所有的楼盘名称存入该数组中
                    count = len(expect_borough_name_list)
                    if count == 0 or (count/15 < 1):
                        new_count = 1
                    elif (count/15) >=1 and (count % 15) >= 1:
                        new_count = int(count/15) + 1
                    else:
                        new_count = int(count/15)
                    for n in range(1, new_count + 1):
                        data = self.data.get_data_for_newjson(i, '"' + str(n) + '"')
                        # 判断是否存在依赖
                        if depend_morecase != None:
                            self.depend_data = DependentData(depend_morecase, self.sheet_name, self.json_file)
                            dependent_response_data = self.depend_data.get_data_for_key(i, 0)
                            depend_key = self.data.get_dependent_key(i, 0)
                            print("depend_key", depend_key)
                            jsonData = json.loads(data)
                            print("data:", data)
                            jsonData[depend_key] = dependent_response_data
                            requestData = json.dumps(jsonData)
                            response = self.run_method.run_main(request_type, url, requestData, token_header)  # 获取接口返回数据（返回类型：string型）
                        else:
                            response = self.run_method.run_main(request_type, url, data, token_header)  # 获取接口返回数据（返回类型：string型）
                        response_dict = json.loads(response)  # 将response字符串型转换成字典型
                        response_list = response_dict['data']['list']
                        if count == 0 and len(response_list) == 0:
                            result = True
                        else:
                            for response_index in range(len(response_list)):
                                response_borough_name = response_list[response_index]['boroughName']  # 循环获取接口返回的楼盘名称
                                if self.util.is_contain(response_borough_name, expect_borough_name_list):  # 判断如果接口返回的楼盘名称存在数据库楼盘名数组中，则测试通过
                                    result = True
                                else:
                                    result = False
                    if result:
                        self.data.write_result(i, "测试通过", self.sheet_id)
                        pass_count.append(i)
                        print("测试通过")
                    else:
                        self.data.write_result(i, "测试失败", self.sheet_id)
                        fail_count.append(i)
                        print("测试失败")
                else:
                    data = self.data.get_data_for_json(i)
                    expect_res = self.data.get_except(i)
                    print("期望结果：", expect_res)
                    if i == 1:
                        header = self.data.get_header(i)
                        response = self.run_method.run_main(request_type, url, data, header)
                        res = json.loads(response)
                        # 获取token、operid并写入文件中
                        with open(self.util.base_dir(), 'w') as f:
                            f.write(res["data"]["token"] + "," + res["data"]["id"])
                        print("获取token：", res["data"]["token"])
                    else:
                        token = self.util.getToken(0)
                        operid = self.util.getToken(1)
                        token_header = self.data.get_token_header(i, token)
                        response = self.run_method.run_main(request_type, url, data, token_header)
                    print("返回结果：", response)
                    if self.util.is_contain(expect_res, response):
                        self.data.write_result(i, "测试通过", self.sheet_id)
                        pass_count.append(i)
                        print("测试通过")
                    else:
                        self.data.write_result(i, "测试失败", self.sheet_id)
                        fail_count.append(i)
                        print("测试失败")

                # if i == 1:
                #     data = self.data.get_data_for_json(i)
                #     header = self.data.get_header(i)
                #     # request_data = self.data.get_data_for_json(i)
                #     response = self.run_method.run_main(request_type, url, data, header)
                #     print("返回结果：", response)
                #     res = json.loads(response)
                #     # 获取token、operid并写入文件中
                #     with open(self.util.base_dir(), 'w') as f:
                #         f.write(res["data"]["token"] + "," + res["data"]["id"])
                #     print("获取token：", res["data"]["token"])
                #     expect_res = self.data.get_except(i)
                #     print("期望结果：", expect_res)
                #     if self.util.is_contain(expect_res, response):
                #         self.data.write_result(i, "测试通过", self.sheet_id)
                #         pass_count.append(i)
                #         print("测试通过")
                #     else:
                #         self.data.write_result(i, "测试失败", self.sheet_id)
                #         fail_count.append(i)
                #         print("测试失败")
                # else:
                #     # data = self.data.get_data_for_newjson(i, no, newno, size, newsize)
                #     token = self.util.getToken(0)
                #     operid = self.util.getToken(1)
                #     token_header = self.data.get_token_header(i, token)
                #     depend_morecase = self.data.is_more_depend(i, 0)
                #     expect_res = self.data.get_except_data_for_sql(i)  # 获取数据库返回的所有楼盘记录（返回类型：数组型）
                #     expect_borough_name_list = []
                #     for expect_index in range(0, len(expect_res)):
                #         expect_borough_name = expect_res[expect_index]['borough_name']  # 循环获取数据库返回的楼盘名称
                #         expect_borough_name_list.append(expect_borough_name)  # 将数据库中所有的楼盘名称存入该数组中
                #     count = len(expect_borough_name_list)
                #     if (count % 15) >= 1:
                #         new_count = int(count / 15) + 1
                #     else:
                #         new_count = int(count / 15)
                #     for n in range(1, new_count+1):
                #         data = self.data.get_data_for_newjson(i, '"'+ str(n) +'"')
                #         # 判断是否存在依赖
                #         if depend_morecase != None:
                #             self.depend_data = DependentData(depend_morecase, self.sheet_name, self.json_file)
                #             dependent_response_data = self.depend_data.get_data_for_key(i, 0)
                #             depend_key = self.data.get_dependent_key(i, 0)
                #             print("depend_key", depend_key)
                #             jsonData = json.loads(data)
                #             print("data:", data)
                #             jsonData[depend_key] = dependent_response_data
                #             requestData = json.dumps(jsonData)
                #             response = self.run_method.run_main(request_type, url, requestData, token_header)  # 获取接口返回数据（返回类型：string型）
                #         else:
                #             response = self.run_method.run_main(request_type, url, data, token_header)  # 获取接口返回数据（返回类型：string型）
                #         response_dict = json.loads(response)  # 将response字符串型转换成字典型
                #         response_list = response_dict['data']['list']
                #         for response_index in range(len(response_list)):
                #             response_borough_name = response_list[response_index]['boroughName']  # 循环获取接口返回的楼盘名称
                #             if self.util.is_contain(response_borough_name, expect_borough_name_list):  # 判断如果接口返回的楼盘名称存在数据库楼盘名数组中，则测试通过
                #                 result = True
                #             else:
                #                 result = False
                #     if  result:
                #         self.data.write_result(i, "测试通过", self.sheet_id)
                #         pass_count.append(i)
                #         print("测试通过")
                #     else:
                #         self.data.write_result(i, "测试失败", self.sheet_id)
                #         fail_count.append(i)
                #         print("测试失败")

                    # expect_borough_name_list = []
                    # for j in range(len(expect_res)):
                    #     expect_borough_name = expect_res[j]['borough_name']
                    #     expect_borough_name_list.append(expect_borough_name)
                    # print("期望结果：", expect_res)
                    # if self.util.is_contain(response_borough_name, expect_borough_name_list):
                    #     self.data.write_result(i, "测试通过", self.sheet_id)
                    #     pass_count.append(i)
                    #     print("测试通过")
                    # else:
                    #     self.data.write_result(i, "测试失败", self.sheet_id)
                    #     fail_count.append(i)
                    #     print("测试失败")

                self.data.write_response(i, response, self.sheet_id)
        # self.email.send_main(pass_count, fail_count)
        return response


if __name__ == '__main__':
    borought_case = BoroughtCase()
    borought_case.go_to_borought()