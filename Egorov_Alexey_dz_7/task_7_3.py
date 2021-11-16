# 3. Создать структуру файлов и папок:
# |--my_project
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
# Примечание: исходные файлы необходимо оставить;
# обратите внимание, что html-файлы расположены в родительских папках (они играют роль пространств имён);
# предусмотреть возможные исключительные ситуации;
# это реальная задача, которая решена, например, во фреймворке django.

# создание первоначальной структуры

import os

root_dir = 'my_project'
dir_list = ['settings', 'mainapp', 'authapp']
set_files = ['dev.py', 'prod.py']
app_files = ['models.py', 'views.py']
templ_files = ['base.html', 'index.html']

if not os.path.exists(root_dir):
    os.mkdir(root_dir)
for dir in dir_list:
    dir_path = os.path.join(root_dir, dir)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    with open(os.path.join(dir_path, '__init__.py'), 'a') as f:
        f.write('')
    if dir == dir_list[0]:
        for file in set_files:
            with open(os.path.join(dir_path, file), 'a') as f:
                f.write('')
    else:
        dir_templ_path = os.path.join(dir_path, 'templates', dir)
        if not os.path.exists(dir_templ_path):
            os.makedirs(dir_templ_path)
        for file in templ_files:
            with open(os.path.join(dir_templ_path, file), 'a') as f:
                f.write('')
        for file in app_files:
            with open(os.path.join(dir_path, file), 'a') as f:
                f.write('')

# сбор шаблонов

import os
import shutil
root_dir ='my_project'
root_templ_dir = os.path.join('my_project', 'templates')
templ_dir = ['mainapp', 'authapp']
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file == 'index.html':
            try:
                shutil.copytree(root, os.path.join(root_templ_dir, os.path.basename(root)))
            except FileExistsError:
                print('Шаблоны уже скопированы. Удалите папку templates с шаблонами, чтобы повторить операцию')













