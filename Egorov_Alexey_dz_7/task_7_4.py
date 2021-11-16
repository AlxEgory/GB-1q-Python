# 4. Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
# а значения — общее количество файлов (в том числе и в подпапках),
# размер которых не превышает этой границы, но больше предыдущей (начинаем с 0),
# например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.

import os

dir_path = 'my_project'
size_dict = {}
for root, dirs, files in os.walk(dir_path):
    for file in files:
        file_size = os.stat(os.path.join(root, file)).st_size
        key = 1
        while file_size != 0:
            key *= 10
            file_size //= 10
        if size_dict.get(key) is not None:
            val = size_dict.get(key) + 1
        else:
            val = 1
        size_dict[key] = val
list_keys = list(size_dict.keys())
list_keys.sort()
size_dict_sort = {}
for key in list_keys:
    size_dict_sort[key] = size_dict[key]
print(size_dict_sort)




