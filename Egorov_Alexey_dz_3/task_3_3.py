# 3. Написать функцию thesaurus(),
# принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена,
# начинающиеся с соответствующей буквы.
# Например:
# >>>  thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки?
# Как поступить, если потребуется сортировка по ключам?
# Можно ли использовать словарь в этом случае?


def thesaurus(*args, sort=''):
    """
    The function returns the dictionary with names
    :param  args: names
    :param  sort: 'asc' - ascending sort, 'desc' - descending sort
    :return: dictionary, where the keys are the first letters of the names,
    and the values are lists, containing names starting with the corresponding letter.
    """
    names_dict = {}
    if sort == 'asc':
        args = sorted(args)
        print(args)
    elif sort == 'desc':
        args = sorted(args, reverse=True)
    else:
        print(f'Wrong argument "{sort}" for sorting -> "asc" for ascending sort, "desc" for descending sort')
    for name in args:
        names_dict[name[0]] = []
    for name in args:
        names_dict[name[0]].append(name)
    return names_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья", sort='desc'))
# {'П': ['Петр'], 'М': ['Мария'], 'И': ['Илья', 'Иван']}


