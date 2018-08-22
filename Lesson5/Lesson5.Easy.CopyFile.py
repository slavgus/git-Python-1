import sys
import Lesson5.MySafeLib as msl

original_file_path = sys.argv[0]
script_path_params = msl.split_path_into_params(original_file_path)

copy_suffix='copy'

original_file_directory = script_path_params['Directory']
original_file_name = script_path_params['FileName']
original_file_extension = script_path_params['FileExtension']
copy_file_name = '{0}_{1}.{2}'.format(original_file_name,copy_suffix,original_file_extension)
copy_file_path = original_file_directory + '/' + copy_file_name

# print (original_file_directory)
# print (original_file_extension)
# print (copy_file_name)
#
# print (original_file_path)
# print (copy_file_path)

file_copy_result = msl.safe_copy_file(original_file_path, original_file_directory + '/' + copy_file_name)

if file_copy_result[0] == 0:
    print('Файл успешно скопирован\n{0}\n>>>{1}'.format(original_file_path, copy_file_path))
else:
    print('Невозможно скопировать файл\n{0}\nОшибка #{1}: {2}'.format(original_file_path, file_copy_result[1], file_copy_result[2]))
