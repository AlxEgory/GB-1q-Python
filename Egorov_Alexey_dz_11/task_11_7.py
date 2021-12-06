# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа),
# выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


class Complex_Number:
    def __init__(self, number):
        self.number = number

    def __repr__(self):
        return str(self.number)

    def __add__(self, other):
        return Complex_Number(self.number + other.number)

    def __mul__(self, other):
        return Complex_Number(self.number * other.number)


number1 = Complex_Number(5)
number2 = Complex_Number(7)

print(number1 + number2)
print(number1 * number2)