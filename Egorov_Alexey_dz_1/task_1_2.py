# создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб x - третья степень числа x):
# вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# внимание: использовать только арифметические операции!
# к каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7


cube_list = [i ** 3 for i in range(1, 1001, 2)]
sum_task = 0
for value in cube_list:
    sum_digits = 0
    digit = value
    while digit != 0:
        sum_digits += digit % 10
        digit = digit // 10
    if sum_digits % 7 == 0:
        sum_task += sum_digits
        # print(value, sum_digits, sum_task)
print(sum_task)

for ind in range(len(cube_list)):
    cube_list[ind] += 17
sum_task = 0
for value in cube_list:
    sum_digits = 0
    digit = value
    while digit != 0:
        sum_digits += digit % 10
        digit = digit // 10
    if sum_digits % 7 == 0:
        sum_task += sum_digits
        # print(value, sum_digits, sum_task)
print(sum_task)



