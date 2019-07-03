#coding:utf-8
from case.login_case import LoginCase

class LoginApi:
    def __init__(self):
        login = LoginCase()
        login.go_run_login()

if __name__ == '__main__':
    login_api = LoginApi()