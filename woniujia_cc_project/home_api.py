# coding:utf-8
from case.home_case import HomeCase

class HomeApi:
    def __init__(self):
        home = HomeCase()
        home.go_run_home()

if __name__ == '__main__':
    home_api = HomeApi()