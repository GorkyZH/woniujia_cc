# coding=utf-8
from case.distribution_case import DistributionCase

"""新房分销模块接口测试"""
class DistributionApi:
    def __init__(self):
        distribution = DistributionCase()
        distribution.go_to_distribution()

if __name__ == '__main__':
    distribution_api = DistributionApi()