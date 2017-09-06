

# 클래스 class

##### Article variables
title1 = "개발"
author1 = "빅토르"
content1 = "개발은 쉬워욜"
view_count1 = 0

title2 = "코칭"
author2 = "마르코"
content3 = "코칭은 쉬워요"
view_count1 = 0

title3 = "창업"
author3 = "빅토르"
content3 = "창업은 쉬워요"
view_count1 = 0

#### Article class
# class Article:
#     title = "개발"
#     author = "빅토르"
#     content = "개발은 쉬워욜"
#     view_count = 0

# article1 = Article()
# print(article1.title)
# article2 = Article()
# article2.title = "코칭"
# print(article1.title)
# print(article2.title)


#### Article class with _init_
class Article:
    author = "빅토르"
    view_count = 0

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def read(self):
        self.view_count = self.view_count + 1

article1 = Article("개발", "개발은 쉬워요")
article2 = Article("코칭", "코칭은 쉬워요")
article3 = Article("창업", "창업은 쉬워요")

# print(article1.view_count)
# article1.read()
# print(article1.view_count)

#### Ariticle class inheritance 상속
# 클래스도 부모 클래스로부터 자식 클래스가 물려받을 수 있다.
class BrunchArticle(Article):
    source = "브런치"

    def read(self):
        self.view_count = self.view_count + 2

brunch_article = BrunchArticle("개발", "개발은 쉬워요")
print(brunch_article.title)
print(brunch_article.source)
print(brunch_article.view_count)
brunch_article.read()
print(brunch_article.view_count)