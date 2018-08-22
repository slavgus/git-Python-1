# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import Lesson5.MySafeLib as msl

folder_list_result = msl.safe_view_folder('.')

if folder_list_result[0] == 0:
    print('Содержимое текущей директории:\n----------------------------')
    for item in folder_list_result[3]:
        print(item)
else:
    print('Невозможно вывести содержимое текущей директории\nОшибка #{0}: {1}'.format(folder_list_result[1],folder_list_result[2]))
