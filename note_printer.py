def print_note(id, data):
    print(f'Номер заметки: {id}\n{data[0]}\n{data[1]}\nДата время последнего изменения: {data[2]}\n')

def print_all(notes_dict):
    print('Список всех заметок:\n')
    for id in notes_dict:
        print_note(id, notes_dict[id])
        
def print_one(notes_dict):
    key_list = notes_dict.keys()
    id = 0
    while (True):
        id = input('Введите id заметки для отображения на экране: ')
        if id in key_list:
            break
        print('Записи с введенным id не существует.\n')

    print_note(id, notes_dict[id])

def print_by_date(notes_dict):
    notes_list = []
    
    for n in notes_dict:
        notes_list.append(f'{notes_dict[n][2]} {n}')

    notes_list.sort()

    for i in range(len(notes_list)):
        id = notes_list[i].split()[2]
        print_note(id, notes_dict[id])