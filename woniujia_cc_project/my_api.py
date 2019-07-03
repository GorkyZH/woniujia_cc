#coding:utf-8
from case.my_case import MyCase

class MyApi:
    def __init__(self):
        my = MyCase()
        my.go_to_my()

if __name__ == '__main__':
    my_api = MyApi()