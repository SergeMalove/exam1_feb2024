def print_all(notes_dict):
    for id in notes_dict:
        print(f'Номер заметки: {id}\n'
              f'{notes_dict[id][0]}\n'
              f'{notes_dict[id][1]}\n'
              f'Дата время последнего изменения: {notes_dict[id][2]}\n')
        
def print_note(notes_dict):
    key_list = notes_dict.keys()
    id = 0
    while (True):
        id = input('Введите id заметки для отображения на экране: ')
        if id in key_list:
            break
        print('Записи с введенным id не существует.\n')

    print(f'Номер заметки: {id}\n'
            f'{notes_dict[id][0]}\n'
            f'{notes_dict[id][1]}\n'
            f'Дата время последнего изменения: {notes_dict[id][2]}\n')