#coding:utf-8
import os, json, operator

"""
其他公共工具类
"""
class CommonUtil:

    def is_contain(self, except_res, actrual_res):
        """
        判断一个字符串是否存在另一个字符串中
        :param except_res:查找的字符串
        :param actrual_res:被查找的字符串
        """
        flag = None
        if except_res in actrual_res:
            flag = True
        else:
            flag = False
        return flag

    def is_equal_dict(self, dict1, dict2):
        """
        判断两个字典是否相等
        :param dict1:
        :param dict2:
        :return:
        """
        if isinstance(dict1, str):
            dict1 = json.loads(dict1)
        if isinstance(dict2, str):
            dict2 = json.loads(dict2)
        return operator.eq(dict1, dict2)

    def is_equal(self, expect_res, actrual_res):
        flag = None
        if expect_res == actrual_res:
            flag = True
        else:
            flag = False
        return flag

    def base_dir(self):
        '''返回token文件的目录文件保存绝对地址'''
        return os.path.join(os.path.dirname(__file__), 'token.md')

    def getToken(self, index):
        '''读取存储在文件中的token'''
        with open(self.base_dir(), 'r') as f:
            token = f.read()
            return token.split(',')[index]

