# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

#Логика программы следующая. Переходить можно в произвольную директорию на диске, но создавать и удалять каталоги
#а также просматривать содержимое можно ТОЛЬКО В ТЕКУЩЕМ КАТАЛОГЕ (безопасность). Для этого введена проверка ввода на выход
#за пределы каталога - проверяется наличие в пути символов '..', ':' и '/'

#Для выполнения действий в программе используются "безопасные" версии функций по работе с каталогами из модуля
#MySafeLib, которые в свою очередь представляют из себя обертки для функций из модуля os с обработкой исключений

import Lesson5.MySafeLib as msl

def input_check(directory_full_path):
    if not msl.path_traversal_check(directory_full_path):
        return 0
    else:
        print('Невозможно создать директорию\n{0}\nВыход за пределы текущей директории запрещен'.format(directory_full_path))
        return 1

def create_local_dir(directory_full_path):

    directory_create_result = msl.safe_create_folder(directory_full_path)
    if directory_create_result[0] == 0:
        print('Директория успешно создана\n{0}'.format(directory_full_path))
        return 0
    else:
        print('Невозможно создать директорию\n{0}\nОшибка #{1}: {2}\n'.format(directory_full_path, directory_create_result[1], directory_create_result[2]))
        return 1

def delete_local_dir(directory_full_path):

    directory_delete_result = msl.safe_delete_folder(directory_full_path)
    if directory_delete_result[0] == 0:
        print('Директория успешно удалена\n{0}\n'.format(directory_full_path))
        return 0
    else:
        print('Невозможно удалить директорию\n{0}\nОшибка #{1}: {2}\n'.format(directory_full_path, directory_delete_result[1], directory_delete_result[2]))
        return 1

def change_dir(directory_full_path):

    change_directory_result = msl.safe_change_folder(directory_full_path)
    if change_directory_result[0] == 0:
        print('Переходим в директорию\n{0}\n'.format(directory_full_path))
        return 0
    else:
        print('Невозможно перейти в директорию\n{0}\nОшибка #{1}: {2}'.format(directory_full_path, change_directory_result[1], change_directory_result[2]))
        return 1

def show_dir_content():
    folder_list_result = msl.safe_view_folder('.')
    if folder_list_result[0] == 0:
        print('Содержимое текущей директории:\n----------------------------')
        for item in folder_list_result[3]:
            print(item)
        print ('\n')
    else:
        print('Невозможно вывести содержимое текущей директории\nОшибка #{0}: {1}'.format(folder_list_result[1],
                                                                                          folder_list_result[2]))

print('Доступны следующие действия:')
print('1. Перейти в папку')
print('2. Посмотреть содержимое папки')
print('3. Удалить папку')
print('4. Создать папку')
print('5. Выход\n')

option_choice = '0'

while not option_choice == '5':
    option_choice = input ('Выберите следующее действие: ')

    if option_choice == '1':
        change_directory_name = input('Введите имя директории: ')
        change_dir(change_directory_name)
    elif option_choice == '2':
        show_dir_content()
    elif option_choice == '3':
        delete_directory_name = input('Введите имя директории: ')
        if not input_check(delete_directory_name):
            delete_local_dir(delete_directory_name)
    elif option_choice == '4':
        create_directory_name = input('Введите имя директории: ')
        if not input_check(create_directory_name):
            create_local_dir(create_directory_name)
    else:
        print ('Такой опции не существует!')

