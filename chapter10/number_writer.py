import json

number = [2, 3, 5, 7, 8, 11]

file_name = 'number.json'
with open(file_name, 'w') as f_obj:
    json.dump(number, f_obj)