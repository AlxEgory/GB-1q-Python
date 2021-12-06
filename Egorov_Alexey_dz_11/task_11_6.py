# 6. Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад,
# нельзя использовать строковый тип данных.

class Stock:
    def __init__(self):
        self.units = {}

    def __repr__(self):
        return str(*self.units)

    def take_to(self, unit, quantity):
        if type(quantity) != int:
            raise StockErr('Принимаемое количество должно быть числом')
        elif quantity < 0:
            raise StockErr('Принимаемое количество не может быть отрицательным')
        else:
            if self.units.get(unit) is None:
                self.units[unit] = quantity
            else:
                self.units[unit] += quantity


    def out_of(self, unit, quantity):
        if type(quantity) != int:
            raise StockErr('Принимаемое количество должно быть числом')
        elif quantity < 0:
            raise StockErr('Принимаемое количество не может быть отрицательным')
        else:
            self.units[unit] -= quantity



class Equipment:
    def __init__(self, price, manufact):
        self.price = price
        self.manufact = manufact


class Printer(Equipment):
    def __init__(self, price,  manufact, colour_print):
        super().__init__(price,  manufact)
        self.colour_print = colour_print

    def __repr__(self):
        return f'{self.__class__.__name__} {self.manufact} {self.colour_print} ({self.price}$)'


class Computer(Equipment):
    def __init__(self, price,  manufact, os):
        super.__init__(price,  manufact)
        self.os = os

    def __repr__(self):
        return f'{self.__class__.__name__} {self.manufact} {self.os} ({self.price}$)'


class StockErr(Exception):
    pass


stock = Stock()
printer_hp = Printer(100, 'HP', 'bw')
print(printer_hp)
stock.take_to(printer_hp, 10)
stock.take_to(printer_hp, 5)
print(stock.units)
stock.out_of(printer_hp, 3)
print(stock.units)

