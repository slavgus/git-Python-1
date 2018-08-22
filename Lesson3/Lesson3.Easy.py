# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

def pers_data_to_sring(name, surname, age):
    result = '{0}, {1} год(а), проживает в городе {2}'.format(name, surname, age)
    return result

input_name = input('Введите имя: ')
input_surname = input('Введите возраст: ')
input_age = input('Введите город проживания: ')

print (pers_data_to_sring(input_name, input_surname, input_age))

# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

def max_number(num1, num2, num3):
    result = max(num1, num2, num3)
    return result

numbers = [22, 7, 3]

result_string = 'Максимальное число: {0}'.format(max_number(numbers[0], numbers[1], numbers[2]))
print(result_string)

# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

def longest_string(*args):
    max_string=max(args, key=len)
    return max_string

print('Самая длинная строка: {0}'.format(longest_string('aa', 'yiuyd', 'zzz', 'qewq')))
