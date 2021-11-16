# Написать скрипт, создающий стартер (заготовку) для проекта
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
# как лучше хранить конфигурацию этого стартера,
# чтобы в будущем можно было менять имена папок под конкретный проект;
# можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?

import os

root_dir = 'my_project'
dir_list = ['settings', 'mainapp', 'adminapp', 'authapp']
if not os.path.exists(root_dir):
    os.mkdir(root_dir)
for dir in dir_list:
    dir_path = os.path.join(root_dir, dir)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
