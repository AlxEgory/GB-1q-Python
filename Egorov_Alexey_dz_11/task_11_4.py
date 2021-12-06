# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

class Stock:
    def __init__(self):
        pass


class Equipment:
    def __init__(self, price, manufact):
        self.price = price
        self.manufact = manufact


class Printer(Equipment):
    def __init__(self, price, manufact, colour_print):
        super.__init__(price, manufact)
        self.colour_print =colour_print


class Computer(Equipment):
    def __init__(self, price, manufact, os):
        super.__init__(price, manufact)
        self.os = os
