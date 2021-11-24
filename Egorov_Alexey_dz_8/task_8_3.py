# Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
# @type_logger
# def calc_cube(x):
#    return x ** 3
# >>> a = calc_cube(5)
# 5: <class 'int'>


def type_logger(fun):
    def log_fun(*args, **kwargs):
        args_list = [str(arg) + ': ' + str(type(arg)) for arg in args]
        args_str = ', '.join(args_list)
        print(args_str)
        result = fun(*args)
        print(f'type of function result {type(result)}')
        print(kwargs)
        print(f'{fun.__name__}({args_str})')

    return log_fun


@type_logger
def calc_cube(*args):
    f_value = []
    for arg in args:
        f_value.append(arg ** 3)
    return f_value


calc_cube(5, 6, lang='ru')
