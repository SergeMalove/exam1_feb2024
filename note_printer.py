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
    
def print_note(id, data):
    print(f'Номер заметки: {id}\n{data[0]}\n{data[1]}\nДата время последнего изменения: {data[2]}\n')    