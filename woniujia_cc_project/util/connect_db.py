# coding:utf-8

import pymysql.cursors
import json

"""封装连接数据库操作"""
class OperationMysql:
    def __init__(self, sql_base):
        self.sql_base = sql_base
        self.conn = pymysql.connect(
            host='182.61.33.241',
            port=3306,
            user='admin',
            passwd='vvopdb',
            db=sql_base,
            charset='utf8'
        )
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

    # 查询一条数据
    def search_one(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        # result = json.dumps(result)
        return result

    # 查询多条数据
    def search_many(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchmany(3)
        # result = json.dumps(result)
        return result

    # 查询所有数据
    def search_all(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        # result = json.dumps(result)
        return result

if __name__ == '__main__':
    oper_mysql = OperationMysql("testwoniujia")
    sql = "select * from ymm_borough where city_id='62' AND is_checked = '1' AND borough_name like '%万科%'"
    # sql = "SELECT * FROM ymm_article WHERE `status`='1' AND title LIKE '%海珠巨无霸城中村%' OR digest LIKE '%从预告净利润变动幅度来看%' OR content LIKE '%sfds%'"
    # keyword = "%广州%"
    # sql = "SELECT * FROM ymm_article WHERE `status`='1' AND title LIKE '%s' or digest like '%s' or content like '%s'" % (keyword, keyword, keyword)
    res = oper_mysql.search_all(sql)
    print("查询数据：", res)
    print(type(res))