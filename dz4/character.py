import datetime
datetime.date.today().year # 2022
class Character:
    name = 'Adam'
    Year = 2008
    group = 785
    avarage = 9

    def __init__(self, name = 'Adam', Year = 2008, group = 785, avarage = 9):
        self.name = name
        self.Year = Year
        self.group = group
        self.avarage = avarage

    def __str__(self):
        return f' == {self.name} ==\n' \
            f' Год рождения : {self.Year}\n' \
            f' Грyппа : {self.group}\n ' \
            f' Средний балл : {self.avarage}\n'

    def age(self):
            return f' вам {datetime.date.today().year - self.Year} лет'

