def print_notes(notes_dict):
    for id in notes_dict:
        print(f'Номер заметки: {id}\n'
              f'{notes_dict[id][0]}\n'
              f'{notes_dict[id][1]}\n'
              f'Дата время последнего изменения: {notes_dict[id][2]}\n')