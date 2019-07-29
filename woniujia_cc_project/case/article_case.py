# coding=utf-8
from main.run import Run

# 资讯接口用例模块
class ArticleCase:
    def __init__(self):
        self.json_file = "/Users/mac/Desktop/测试资料/蜗牛家产品线/woniujia_cc_jiekou/woniujia_cc_jiekou_git/" \
                         "woniujia_cc_project/dataconfig/article.json"
        self.sheet_name = "资讯模块"
        self.sheet_id = 3
        self.db = "testwoniujia"

    def go_to_article(self):
        run = Run(self.json_file, self.sheet_name, self.sheet_id, self.db)
        run.go_to_run("title", "title")

if __name__ == '__main__':
    article = ArticleCase()
    article.go_to_article()