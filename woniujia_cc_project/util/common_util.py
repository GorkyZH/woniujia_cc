#coding:utf-8
import os

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

    def base_dir(self):
        '''返回token文件的目录文件保存绝对地址'''
        return os.path.join(os.path.dirname(__file__), 'token.md')

    def getToken(self, index):
        '''读取存储在文件中的token'''
        with open(self.base_dir(), 'r') as f:
            token = f.read()
            return token.split(',')[index]

