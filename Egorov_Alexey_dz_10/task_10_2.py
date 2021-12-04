# Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма(2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани.
# Проверить на практике полученные на этом уроке знания.
# Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def cloth_spend(self):
        pass


class Coat(Clothes):
    def __init__(self, name, v):
        self.name = name
        self.size = v

    @property
    def cloth_spend(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name, h):
        self.name = name
        self.height = h

    @property
    def cloth_spend(self):
        return 2 * self.height + 0.3


coat = Coat('зимнее', 50)
print(coat.cloth_spend)

suit = Suit('парадный', 1.76)
print(suit.cloth_spend)
