print('Задача №1\n')
source_number_list = [10, 4, 14, -33, 36, 0, 101, 12, 25, 16]  # исходный список чисел
result_number_list = []  # результирующий список

for number in source_number_list:  # для каждого элемента исходного списка
    result = number ** (1 / 2) #оператор ** в случае извлечения корня из отрицательного числа возвращает отрицательное значение, а не вылетает с ошибкой :)) Хм...
    if number >=0 and not (result - int(result)): # eсли исходное число больше нуля и отсутствует разница между результатом извлечения корня и его целой частью:
        result_number_list.append(result) # добавляем результат извлечения корня в результирующий список

print (result_number_list)
print ('\n')


print('Задача №2\n')

source_date = '28.04.2008' #исходная дата


#списки возможных текстовых значений
month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
day_list = ['первое', 'второе', 'третье', 'четвертое', 'пятое', 'шестое', 'седьмое', 'восьмое', 'девятое', 'десятое','одиннадцатое',
            'двенадцатое','тринадцатое','четырнадцатое','пятнадцатое','шестнадцатое','семнадцатое','восемнадцатое','девятнадцатое','двадцатое',
            'двадцать ', 'тридцать ']

source_day = int(source_date[:2])  # извлекаем номер дня как целое число
source_day_dig1 = int(source_date[0]) # извлекаем первую цифру дня, как целое число
source_day_dig2 = int(source_date[1]) # извлекаем вторую цифру дня, как целое число

source_month = int(source_date[3:5]) # извлекаем номер месяца, как целое число
source_year = int(source_date[6:]) # извлекаем год как целое число (не обязательно)

if source_day <= 20: # если номер дня меньше или равен 20
    res_day = day_list[source_day - 1] # выбираем подходящее текстовое значение из списка
else:  # иначе (номер дня больше 20)
    res_day = day_list[18 + source_day_dig1] + day_list[source_day_dig2 -1] # составляем текстовое значение на основе первой цифры номера дня и второй цифры


res_month = month_list[source_month-1] #подбираем текстовое значение из списка для месяца

print ('Исходная дата: {0}'.format(source_date)) #в
print ('Результирующая дата: {0} {1} {2} года'.format(res_day,res_month,source_year))