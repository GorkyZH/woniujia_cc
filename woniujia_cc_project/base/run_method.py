#coding:utf-8
import requests
import json

"""
post、get基类的封装
"""

class RunMethod:
    def post_main(self,url,data,header=None):
        result = None
        if header != None:
            result = requests.post(url=url,data=data,headers=header)
        else:
            result = requests.post(url=url, data=data)
        print(result.status_code)
        return result.json()

    def get_main(self,url,data=None,header=None):
        result = None
        if header != None:
            result = requests.get(url=url,data=data,headers=header)
        else:
            result = requests.get(url=url, data=data)
        return result.json()

    def run_main(self,method,url,data=None,header=None):
        result = None
        if method == 'post':
            result = self.post_main(url,data,header)
        else:
            result = self.get_main(url,data,header)
        # 返回数据格式调整
        # return json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return json.dumps(result, ensure_ascii=False)
        #return result

