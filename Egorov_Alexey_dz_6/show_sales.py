import sys

# 1 вариант: без чтения всего файла при указании аргументов
args = [*map(int, sys.argv[1:3])]
if len(args) == 0:
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        content = f.read().splitlines()
        for line in content:
            print(line)
elif len(args) == 1:
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        n = 1
        for line in f:
            if n >= args[0]:
                print(line.strip())
            n += 1
else:
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        n = 1
        for line in f:
            if args[0] <= n <= args[1]:
                print(line.strip())
            n += 1


# 2 вариант: с чтением всего файла при указании аргументов
with open('bakery.csv', 'r', encoding='utf-8') as f:
    content = f.read()
content = content.splitlines()
args = [*map(int, sys.argv[1:3])]
if len(args) == 0:
    for i in range(len(content)):
        print(content[i])
elif len(args) == 1:
    for i in range(args[0]-1, len(content)):
        print(content[i])
else:
    for i in range(args[0]-1, args[1]):
        print(content[i])