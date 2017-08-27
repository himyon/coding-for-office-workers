# 학교 클래스

class School:
    # name = "성보중학교"
    # year = "1999년"
    # adress = "서울시_관악구_신림동"

    def __init__(self, name, year, adress):
        self.name = name
        self.year = year
        self.adress = adress

School1 = School("성보중학교", "1999년", "서울시_관악구_신림동")
