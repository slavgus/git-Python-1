# Файл включает в себя решение задач уровня Easy для урока №2

# Задача №1 (решал для списка произвольных фруктов)

print('Задача №1\n')
fruit_list = ['яблоко', 'абрикос', 'ананас', 'киви', 'топинамбур']  # список произвольных фруктов
len_set = set()  # объявляем множество длин названий фруктов

for item in fruit_list:  # для каждого фрукта в списке
    len_set.add(len(item))  # определяем множество длин названий фруктов (можно и список, но это сэкономит память)

for i, item in enumerate(fruit_list):  # перебираем индексы и значения элементов списка фруктов (enumerate возвращает соответствующие кортежи)
    # Выводим нужную информацию, в том числе необходимое число пробелов перед названием фрукта,
    # равное разнице между длиной названия текущего фрукта и максимальной длиной в множестве длин
    print('{0}. {1}{2}'.format(i + 1, " " * (max(len_set) - len(item)), item))

print('\n')

# Задача №2 Т.к. списки произвольные, считаем, что и в первом и во втором могут быть повторяющиеся значения, а также сложные типы объектов (например, словари)
print('Задача №2\n')
list_delete_from = ['blabla', 15, ['a', 'defg'], 27, 'Text1', 'Text2', 15, 47]  # список из которого удаляются значения
list_delete_what = ['Text1', ['a', 'defg'], 'Text1', 15]  # список удаляемых значений
list_result_buffer = []  # промежуточный буфер, в который мы будем складывать значения, которые не надо удалять

for item in list_delete_from:  # для каждого элемента списка из которого удаляются значения
    if not list_delete_what.count(item):  # если этот элемент НЕ присутствует в списке удаляемых значений
        list_result_buffer.append(item)  # то добавляем его в буфер

list_delete_from = list_result_buffer.copy()  # присваиваем первоначальному списку значение буфера, таким образом, в нем остается только то, что не подлежит удалению
# Интересный вопрос. Если не сделать копию и обнулить буфер, то вместе с ним обнулится и первоначальный список. Означает ли это,
# что списки при присвоении не копируются, в отличие от простых типов, а создаются ссылки на одну и ту же область памяти?
# Или они разделяются, в процессе исполнения, как только один из списков меняется?

list_result_buffer.clear()  # обнуляем буфер, чтобы не занимал память

print(list_delete_from)
print('\n')

# Задача №3
print('Задача №3\n')
source_number_list = [10, 52, 14, 33, 48, 44, 101, 12]  # исходный список целых чисел
result_number_list = []  # результирующий список

for number in source_number_list:  # для каждого элемента исходного списка
    if number / 2 == number // 2:  # если результаты обычного и целочисленного деления на 2 равны, значит кратно 2)
        result_number_list.append(
            number / 4)  # делим на 4 по условиям задачи (получается не всегда целое) и добавляем в результирующий список
    else:  # в другом случае (если не кратно двум)
        result_number_list.append(number * 2)  # умножаем на 2 по условиям задачи и добавляем в результирующий список

print(result_number_list)

# интересно, почему результат умножения целого числа на целое - это целое число, а деления - с плавающей точкой? :))
