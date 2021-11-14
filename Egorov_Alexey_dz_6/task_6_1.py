# 1. Не используя библиотеки для парсинга,
# распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
# получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>).

file_logs = 'nginx_logs.txt'
list_logs = []
with open(file_logs, 'r', encoding='utf-8') as f:
    for line in f:
        split_line = line.split(' ')
        tuple_line = split_line[0], split_line[5].replace('"', ''), split_line[6]
        list_logs.append(tuple_line)
print(list_logs[:3])
