# Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]

# Подсказка: использовать возможности python, изученные на уроке.
# Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def num_gen():
    num_pred = src[0]
    for num in src:
        if num > num_pred:
            yield num
        num_pred = num


result = list(num_gen())
print(result)