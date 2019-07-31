# coding=utf-8
from case.borough_case import BoroughCase

"""楼盘页接口测试"""
class BoroughApi:
    def __init__(self):
        borough = BoroughCase()
        borough.go_to_borough()

if __name__ == '__main__':
    borough_api = BoroughApi()