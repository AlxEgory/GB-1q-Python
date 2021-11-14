# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип:
# одна строка — один пользователь, разделитель между значениями — запятая.
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
# ключи — ФИО, значения — данные о хобби.
# Сохранить словарь в файл. Проверить сохранённые данные.
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.
# Если наоборот — выходим из скрипта с кодом «1». 
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.

with open('users.csv', 'r', encoding='utf-8') as f:
    content_u = f.read()
with open('hobby.csv', 'r', encoding='utf-8') as f:
    content_h = f.read()
content_u = content_u.splitlines()
content_h = content_h.splitlines()
if len(content_u) > len(content_h):
    content_h.extend([None]*(len(content_u) - len(content_h)))
elif len(content_u) < len(content_h):
    print('Пользователей сайта меньше чем хобби' )
    exit(1)
user_dict = {}
for key, val in zip(content_u, content_h):
    user_dict[key] = val
print(user_dict)

