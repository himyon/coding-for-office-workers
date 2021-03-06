# 사람 클래스를 하나 만듭니다. 사람의 기본 요소는 이름, 나이, 성별로 합시다.
# 직장 동료 클래스를 사람 클래스를 이용해서 만듭시다.
# 사람 기본 요소 외 별도의 추가 사항은 직급입니다.
# 힌트
#
# 클래스와 상속을 활용합니다.
# 사람의 기본 요소인 이름, 나이, 성별은 각각 새로운 사람을 만들 때,
# 입력을 받을 수 있도록 합시다.
# 직장 동료의 기본 직급은 "대리"로 지정합니다.
# (고급) 사람 클래스에서 새로운 사람을 만들 때 입력은 그대로 유지하면서,
# 직급도 처음 만들어질 때 입력하도록 변경을 도전해봅시다.

class Human:

    def __init__(self, name, age, sex,):
        self.name = name
        self.age = age
        self.sex = sex

Human1 = Human("홍길동", "20", "남성")
Human2 = Human("김말숙", "20", "여성")

print(Human1.name)
print(Human1.age)
print(Human1.sex)

class worker(Human):
    positon = "대리"

worker_human = worker("김개똥", "20", "남성")
print(worker_human.positon)
