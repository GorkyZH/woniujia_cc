# coding:utf-8
from main.run_common import RunCommon

class LoginCase:
    def __init__(self):
        # self.excel_file = "/Users/mac/Desktop/测试资料/蜗牛家产品线/woniujia_cc_jiekou/woniujia_cc_jiekou_git/woniujia_cc_project/dataconfig/login.xls"
        self.json_file = "/Users/mac/Desktop/测试资料/蜗牛家产品线/woniujia_cc_jiekou/woniujia_cc_jiekou_git/woniujia_cc_project/dataconfig/request_pram.json"
        self.sheet_name = "登录模块"
        self.sheet_id = 0
    def go_run_login(self):
        run_comm = RunCommon(self.json_file, self.sheet_name, self.sheet_id)
        run_comm.go_run_case()

if __name__ == '__main__':
    logincase = LoginCase()
    logincase.go_run_login()