# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
#
# Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.
import time
import random


src = [random.randint(1, 100) for num in range(1, 100)]

# решение «в лоб» (эффективно, когда список менее 35 элементов)
start = time.perf_counter_ns()
result = [num for num in src if src.count(num) == 1]
print(time.perf_counter_ns()-start, result)

# оптимизация (эффективно, когда список более 35 элементов)
start = time.perf_counter_ns()
non_unique_num = set()
tmp = set()
for el in src:
   if el in tmp:
       non_unique_num.add(el)
   else:
       non_unique_num.discard(el)
   tmp.add(el)
result = list(filter(lambda el: not el in non_unique_num, src))

print(time.perf_counter_ns()-start, result)
