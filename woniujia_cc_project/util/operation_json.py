# _*_ coding:utf-8 _*_
import json

"""
读取json文件工具类
"""
class OperationJson:
    def __init__(self, json_file):
        self.json_file = json_file
        self.data = self.read_data()
        #"/Users/mac/Desktop/practise/Demo/dataconfig/logincom.json"

    #读取json文件
    def read_data(self):
        #with open("../dataconfig/logincom.json") as fp:
         with open(self.json_file) as fp:
            data = json.load(fp)
            return data

    #根据关键字获取数据
    def get_data(self, id):
        #return self.data[id]
        return json.dumps(self.data[id])

if __name__ == '__main__':
    operJson = OperationJson("/Users/mac/Desktop/测试资料/蜗牛家产品线/woniujia_cc_jiekou/woniujia_cc_jiekou_git/woniujia_cc_project/dataconfig/login.json")
    print(operJson.get_data('login'))
