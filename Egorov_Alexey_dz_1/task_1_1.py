# 1. Реализовать вывод информации о промежутке времени в зависимости
# от его продолжительности duration в секундах:
# до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: # <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

#ввод значения
duration = int(input('Введите период в секундах: '))
if duration < 60:
    print(duration,'сек')
elif 60 < duration < 3600:
    print(duration // 60, 'мин', duration % 60, 'сек')
elif 3600 <= duration < 86400:
    print(duration // 3600, 'час', duration % 3600 // 60, 'мин', duration % 60, 'сек')
else:
    print(duration // 86400, 'дн', duration % 86400 // 3600, 'час', duration % 3600 // 60, 'мин', duration % 60, 'сек')