# Задача-1:
# Напишите скрипт, удаляющий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.

import sys
import Lesson5.MySafeLib as msl

def delete_local_dir(directory_full_path):
    directory_delete_result = msl.safe_delete_folder(directory_full_path)
    if directory_delete_result[0] == 0:
        print('Директория успешно удалена\n{0}'.format(directory_full_path))
        return 0
    else:
        print('Невозможно удалить директорию\n{0}\nОшибка #{1}: {2}'.format(directory_full_path, directory_delete_result[1], directory_delete_result[2]))
        return 1

script_path = sys.argv[0]
script_path_params = msl.split_path_into_params(script_path)

for i in range(1,10):
    delete_local_dir('{0}/Dir_{1}'.format(script_path_params['Directory'],i))

