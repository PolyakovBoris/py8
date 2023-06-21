import json

path = 'C:/IT/GB/2PythonDeep/sem8/'
file_name = 'file3.txt'

with open(f'{path}{file_name}', 'r', encoding='utf-8') as f:
    dict_from_txt = {}
    for line in f:
        key, value = line.replace('\n', '').split(' ')
        dict_from_txt.setdefault(key.capitalize(), value)

with open(f'{path}new_JSON_file.json', 'w', encoding='utf-8') as f:
    json.dump(dict_from_txt, f, sort_keys='True', indent=2)
