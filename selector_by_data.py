import re, note_printer

def select_by_data(notes_dict):
    data = -1
    while (True):
        data = input('Введите дату в формате ДД.ММ.ГГГГ: ')
        if re.match(r'\d\d.\d\d.\d\d', data) != None:
            break
        print('\nНеправильный ввод даты\n')

    isFouned = False
    for id in notes_dict:
        if data in notes_dict[id][2]:
            if isFouned == False:
                print(f'Заметки на дату {data}:\n')
                note_printer.print_note(id, notes_dict[id])
                isFouned = True

    if isFouned == False:
        print(f'\nЗаметок на дату {data} не найдено.\n')