#coding:utf-8
from login_api import LoginApi
from borough_api import BoroughApi
from article_api import ArticleApi
from guest_api import GuestApi
from home_api import HomeApi
from my_api import MyApi

"""
主流程运行的主方法类
"""
class RunTest:
    def __init__(self):
        login = LoginApi()
        borough = BoroughApi()
        article = ArticleApi()

if __name__ == '__main__':
    run = RunTest()
