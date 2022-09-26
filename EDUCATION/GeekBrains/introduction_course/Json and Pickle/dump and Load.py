import json
import pickle

some_data = {'name': 'Rammstein',
             'tracks': ['Angel', 'Sonne', 'My heart brent'],
             'P.S': ['Fuck you!', 'All what you do is right!',
                     'Не сдавайся.', 'I Hate you!']}
# Запись.
with open('music_serialize_in.json', 'w', encoding='utf-8') as work_file:
    json.dump(some_data, work_file)

with open('music_serialize_in.pickle', 'wb') as work_file:
    pickle.dump(some_data, work_file)

# Чтение.
with open('music_serialize_in.json', 'r', encoding='utf-8') as work_file:
    load_data = json.load(work_file)

with open('music_serialize_in.pickle', 'rb') as work_file:
    load_data_2 = pickle.load(work_file)


print(load_data, ' Json')
print(load_data_2, ' Pickle')
