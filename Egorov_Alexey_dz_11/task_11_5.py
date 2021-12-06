# 5. Продолжить работу над первым заданием.
# Разработайте методы,
# которые отвечают за приём оргтехники на склад
# и передачу в определённое подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных,
# можно использовать любую подходящую структуру (например, словарь).


class Stock:
    def __init__(self):
        self.units = {}

    def take_to(self, unit, quantity):
        if self.units.get(unit) is None:
            self.units[unit] = quantity
        else:
            self.units[unit] += quantity

    def out_of(self, unit, quantity):
        self.units[unit] -= quantity



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
