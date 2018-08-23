import os
import shutil
import re

#Функция сигнатурного анализа для выявления атак/ошибок класса Path Travesal (выход за пределы каталога)
def path_traversal_check (path):
    path_traversal_pattern = '(\.\.)|(\:)|(\/)'
    path_string = str(path)

    if re.search(path_traversal_pattern, path_string):
        return 1
    else:
        return 0

#Разбирает полный путь к файлу на параметры - путь к директории, в которой находится файл и, собственно, имя файла
def split_path_into_params (full_path):

    full_path_string = str(full_path)

    file_name_separator_position = full_path_string.rfind('/')
    file_extension_separator_position = full_path_string.rfind('.')

    path_element_dict = {}

    path_element_dict['Directory'] = full_path_string[:file_name_separator_position]
    path_element_dict['CompleteFileName'] = full_path_string[file_name_separator_position + 1:]
    path_element_dict['FileName']= full_path_string[file_name_separator_position + 1:file_extension_separator_position]
    path_element_dict['FileExtension'] = full_path_string[file_extension_separator_position + 1:]

    return path_element_dict

#Фyнкция безопасного создания папки с обработкой исключений. Возвращает тройку - результат (0-успешно, 1 - неуспешно),
#Номер ошибки (если была, в противном случае - 0) и текстовое описание результата (успешного или неуспешного)
def safe_create_folder (folder_path):
    folder_path_string = str(folder_path)
    try:
        os.mkdir(folder_path_string)
        return (0,0,"Директория создана успешно")
    except OSError as e:
        return (1,e.errno, e.strerror)

#Фyнкция безопасного удаления папки с обработкой исключений. Возвращает тройку - результат (0-успешно, 1 - неуспешно),
#Номер ошибки (если была, в противном случае - 0) и текстовое описание результата (успешного или неуспешного)
def safe_delete_folder (folder_path):
    folder_path_string = str(folder_path)
    try:
        os.rmdir(folder_path_string)
        return (0, 0, "Директория удалена успешно")
    except OSError as e:
        return (1, e.errno, e.strerror)

#Фyнкция безопасного вывода содержимого каталога. Возвращает тройку - результат (0-успешно, 1 - неуспешно),
#Номер ошибки (если была, в противном случае - 0) и текстовое описание результата (успешного или неуспешного)
def safe_view_folder (folder_path):
    folder_path_string = str(folder_path)
    try:
        folder_item_list = os.listdir(folder_path_string)
        return (0, 0, "Директория просмотрена успешно",folder_item_list)
    except OSError as e:
        return (1, e.errno, e.strerror)

#Фyнкция безопасного перехода в другой каталог. Возвращает тройку - результат (0-успешно, 1 - неуспешно),
#Номер ошибки (если была, в противном случае - 0) и текстовое описание результата (успешного или неуспешного)
def safe_change_folder (folder_path):
    folder_path_string = str(folder_path)
    try:
        os.chdir(folder_path_string)
        return (0, 0, "Переход в директорию выполнен успешно")
    except OSError as e:
        return (1, e.errno, e.strerror)

#Фyнкция безопасного копирования файла. Возвращает тройку - результат (0-успешно, 1 - неуспешно),
#Номер ошибки (если была, в противном случае - 0) и текстовое описание результата (успешного или неуспешного)

def safe_copy_file (original_file_path, copy_file_path):
    original_file_path_string = str(original_file_path)
    copy_file_path_string = str(copy_file_path)

    try:
        shutil.copyfile(original_file_path_string,copy_file_path_string)
        return (0, 0, "Файл скопирован успешно")
    except OSError as e:
        return (1, e.errno, e.strerror)
