# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.

import json
import csv
path = 'C:/IT/GB/2PythonDeep/sem8/'
file_name = 'file4_access.json'
with open(f'{path}{file_name}', 'r+', encoding='utf-8') as f:

    json_data = json.load(f)

    while True:

        print(json_data)
        name, ID, access_level, *_ = input('name, ID, access_level-  ').split(' ')
        if name == 'exit':
            break
        json_data[access_level][ID] = name

    f.seek(0)
    json.dump(json_data, f, indent=2, sort_keys=True)
    with open(f'{path}file1.csv', 'w+',  encoding='utf-8') as f:

        csv.writer(f).writerow('ACCESSLEVEL,ID,NAME')
        for key in json_data:
            print(key)
