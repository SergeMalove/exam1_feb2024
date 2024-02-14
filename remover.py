def remove_note(notes_dict):
    key_list = notes_dict.keys()
    id = 0
    while (True):
        id = input('Введите id заметки для удаления: ')
        if id in key_list:
            break
        print('Записи с введенным id не существует.\n')
    
    notes_dict.pop(id)