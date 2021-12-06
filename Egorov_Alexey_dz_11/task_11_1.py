# 1. Реализовать класс «Дата»,
# функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def date_to_int(cls, date):
        date = list(map(int, date.split('-')))
        return date

    @staticmethod
    def valid_date(date):
        date = list(map(int, date.split('-')))
        if not 0 < date[0] <= 31 or not 0 < date[1] <= 12:
            raise ValueError('Неверные значения в дате')
        else:
            return date


print(Date.date_to_int('22-03-2021'))
d = Date('23-04-2018')
print(d.date_to_int(d.date))

print(Date.valid_date('31-1-2021'))