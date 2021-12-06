# 2. Создайте собственный класс-исключение,
# обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class ZeroDiv(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_data1 = int(input("Введите делимое: "))
inp_data2 = int(input("Введите делитель: "))

try:
    if inp_data2 == 0:
        raise ZeroDiv('Ошибка деления на ноль')
    else:
        div = inp_data1 / inp_data2
        print(div)

except ZeroDiv as err:
    print(err)
finally:
    print('Вычисление завершено')
