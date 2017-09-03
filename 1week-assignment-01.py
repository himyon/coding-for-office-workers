# 처음 파이썬 파일을 실행 시키면
# 한식, 중식, 일식 중 한 가지를 고르라는 내용이 나옵니다.
# 그 중에서 한 가지를 고르면 식당 이름을 하나 임의로 추천해 줍니다.

name = input("한식, 중식, 일식 중 고르세요. ")

import random

k = ("참마루", "감자탕", "남산옥", "놀부부대찌개")
c = ("치찌", "중화반점", "티원", "홍콩반점")
j = ("태풍참치", "청수사", "기꾸스시", "우리수산")

if name == "한식":
    print(random.choice(k))
if name =="중식":
    print(random.choice(c))
if name =="일식":
    print(random.choice(j))
