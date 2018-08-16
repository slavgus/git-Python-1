# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.


# функция записи в файл словаря по колонкам
def write_dict_in_columns (write_dict, write_path):
    max_len_key = len((max (write_dict.keys(), key=len)))

    with open('salaries.txt', 'w', encoding='UTF-8') as f:
        for dict_key in write_dict:
            spaces_to_add_in_column = (max_len_key - len(dict_key)) * ' '
            f.write('{0}{2} - {1}\n'.format(dict_key, write_dict[dict_key], spaces_to_add_in_column))
        f.close()


# функция чтения из файла словаря по колонкам
def read_dict_in_columns (read_path):

    result_dict = {}
    with open('salaries.txt', 'r', encoding='UTF-8') as f:
        for line in f:
            line.strip('\n')
            dict_key = (line.split('-')[0]).strip(' ')
            dict_value = line.split('-')[1].strip(' ')
            if int(dict_value) <= 50000:
                result_dict.update({dict_key: dict_value})

 #           print('{1}{0}'.format(dict_key,dict_value))

        f.close()
    return result_dict

#Заданные значения
employees = ['Иванов', 'Петров', 'Сидоров', 'Кузнецов']
salaries = [20000, 55000, 45000, 80000]

#Собираем из них словарь
gross_salary_dict = dict(zip(employees, salaries))
# Указываем в какой фал писать
salary_file_path = 'salaries.txt'

#Записываем файл
write_dict_in_columns(gross_salary_dict,salary_file_path)
#Читаем файл
net_salary_dict = read_dict_in_columns(salary_file_path)
#Выводим результат
for net_salary_dict_key in net_salary_dict:
    print ('{0} - {1}'.format(net_salary_dict_key.upper(), net_salary_dict[net_salary_dict_key]))



