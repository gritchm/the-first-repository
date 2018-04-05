#Q1- init 함수의 용도가 무엇인가 ?
#Q2- 상속의 개념과 용도?
#Q3- 이걸 왜쓰는지 클래스를 ? 직접 클래스를 구현할 기회는 잘 없지만
# 멀리보는 개발자라면 이부분을 충분히 이해하는것도 좋다


# 클래스 class

#### Article variables
title1="개발"
author1="마르코"
content1="개발을 쉬워요"
view_count1=0

title2="코칭"
author2="마르코"
content2="코칭은 쉬워요"
view_count2=0

title3="창업"
author3="마르코"
content3="창업은 쉬워요"
view_count3=0
#
# #### Article class
# class Article:
#         title="개발"
#         author="마르코"
#         content="개발을 쉬워요"
#         view_count=0
#
# #Class 내 변수 접근하기위해서, Class 의 정보를 담고있는 접근가능한 변수를 만든다
# article1=Article()
# print(article1.title)
# article2=Article()
# article2.title="코칭"
# print(article2.title)

####Article class with_init_
#init 클래스의 내장함수, self 는 변수
#self 는 class 안의 변수에 접근하겠다는 약속
#init 함수를 쓰고싶으면 해당하는 requirement를 모두 채워줘야 Class 활성화 가능
#클래스와 Def__init__ 을 통해서 수정해야할 부분만 간단히 수정가능
class Article:
    author="마르코"
    view_count=0

    def __init__(self, title, content):
        self.title=title
        self.content = content
    def read(self):
        self.view_count=self.view_count+1

article1=Article("개발", "개발은 쉬워요")
article2=Article("코칭", "코칭은 쉬워요")
article3=Article("창업", "창업은 쉬워요")
#
# print(article1.view_count)
# article1.read()
# # 클래스내장함수없다면 다음 코드 다짜야함 article1.view_count1=article1.view_count1+1
# print(article1.view_count)


#### Article class inheritance 상속
class BrunchArticle(Article):
    source="브런치"
#Overide 같은 함수를 변경해서 사용하는것
    def read(self):
        self.view_count=self.view_count+2
#Instance 만듬, Brunch Article 활성화 시키는것
brunch_article=BrunchArticle("글쓰기","글쓰기는 쉬워요")
print(brunch_article.title)
print(brunch_article.content)
print(brunch_article.source)
print(brunch_article.view_count)
brunch_article.read()
print(brunch_article.view_count)



title1="개발"
author1="마르코"
content1="개발을 쉬워요"
view_count1=0

title2="코칭"
author2="마르코"
content2="코칭은 쉬워요"
view_count2=0

title3="창업"
author3="마르코"
content3="창업은 쉬워요"
view_count3=0

#학교 클래스 과제
# #### Article class
# class Article:
#         title="개발"
#         author="마르코"
#         content="개발은 쉬워요"
#         view_count=0
#
# #Class 내 변수 접근하기위해서, Class 의 정보를 담고있는 접근가능한 변수를 만든다
# article1=Article()
# print(article1.title)
# article2=Article()
# article2.title="코칭"
# print(article2.title)

name1="영남대"

class School:
    name="영남대"
    year=1967
    address="경산"

schoo1=School()
print(school1.year)
