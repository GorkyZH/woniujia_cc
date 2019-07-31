from case.article_case import ArticleCase

"""资讯页接口测试"""
class ArticleApi:
    def __init__(self):
        article = ArticleCase()
        article.go_to_article()

if __name__ == '__main__':
    article_api = ArticleCase()