# coding:utf-8
from main.run_common import RunCommon

class HomeApi:
    def __init__(self):
        self.excel_file = "/Users/mac/Desktop/测试资料/蜗牛家产品线/woniujia_cc_jiekou/woniujia_cc_jiekou_git/woniujia_cc_project/dataconfig/home.xls"
        self.json_file = "/Users/mac/Desktop/测试资料/蜗牛家产品线/woniujia_cc_jiekou/woniujia_cc_jiekou_git/woniujia_cc_project/dataconfig/home.json"

    def go_run_home(self):
        run_comm = RunCommon(self.excel_file, self.json_file)
        run_comm.go_run_case()

if __name__ == '__main__':
    home = HomeApi()
    home.go_run_home()