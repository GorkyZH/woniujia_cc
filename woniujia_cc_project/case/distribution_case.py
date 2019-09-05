# coding=utf-8
from main.run import Run

class DistributionCase:
    def __init__(self):
        self.json_file = "/Users/mac/Desktop/测试资料/蜗牛家产品线/woniujia_cc_jiekou/woniujia_cc_jiekou_git/" \
                         "woniujia_cc_project/dataconfig/request_pram.json"
        self.sheet_name = "分销模块"
        self.sheet_id = 7
        self.sql_base = "effect20190628"

    def go_to_distribution(self):
        run = Run(self.json_file, self.sheet_name, self.sheet_id, self.sql_base)
        run.go_to_run()

if __name__ == '__main__':
    distribution = DistributionCase()
    distribution.go_to_distribution()