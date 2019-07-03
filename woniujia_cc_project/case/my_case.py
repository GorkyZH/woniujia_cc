# coding:utf-8
from main.run_common import RunCommon

class MyCase:
    def __init__(self):
        self.json_file = "/Users/mac/Desktop/测试资料/蜗牛家产品线/woniujia_cc_jiekou/woniujia_cc_jiekou_git/" \
                         "woniujia_cc_project/dataconfig/my.json"
        self.sheet_name = "我的模块"
        self.sheet_id = 3

    def go_to_my(self):
        run_common = RunCommon(self.json_file, self.sheet_name, self.sheet_id)
        run_common.go_run_case()

if __name__ == '__main__':
    mycase = MyCase()
    mycase.go_to_my()
