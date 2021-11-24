# Написать функцию email_parse(<email_address>),
# которая при помощи регулярного выражения извлекает имя пользователя и почтовый домен из email адреса
# и возвращает их в виде словаря.
# Если адрес не валиден, выбросить исключение ValueError.
# Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
#
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
# имеет ли смысл в данном случае использовать функцию re.compile()?

import re


def email_parse(e_address):
    if not re.match(r'\w+@\w+\.\w+', e_address):
        raise ValueError(f'wrong email: {e_address}')
    e_address_dict = {}
    e_address_dict['username'] = re.findall(r'[^@]+', e_address)[0]
    e_address_dict['domain'] = re.findall(r'[^@]+', e_address)[1]
    return e_address_dict


print(email_parse('someone@geekbrains.ru'))
