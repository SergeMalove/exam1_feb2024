import Note

def change_note(notes_dict):
    key_list = notes_dict.keys()
    id = 0
    while (True):
        id = input('Введите id заметки для изменения: ')
        if id in key_list:
            break
        print('Записи с введенным id не существует.\n')

    print('Введите новые данные замены\n')
    new_note = Note.Note(id)
    notes_dict[id] = [new_note.title, new_note.text, new_note.data]

