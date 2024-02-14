import printer, reader, creator, changer, writer

command = 0

while command != '5':
    print('Меню пользователя\n'
          '1. Вывод списка заметок на экран\n'
          '2. Добавить новую заметку\n'
          '3. Изменить существующую заметку\n'
          '4. Удалить заметку\n'
          '5. Выход из программы\n')
    
    command = input('Введите номер пункта меню: ')
    print()
    while command not in ('1', '2', '3', '4', '5'):
        print('Некорректный ввод пункта меню. Повторите ввод.')
        command = input('Выберете пункт меню: ')

    notes_list = reader.read_notes()
    max_id = 0 if len(notes_list) == 0 else int(max(notes_list.keys()))

    match command:
        case '1':
            printer.print_notes(notes_list)
        case '2':
            creator.create_note(max_id)
            max_id += 1
            print('Новая заметка успешно добавлена.\n')
        case '3':
            changer.change_note(notes_list)
            writer.write_notes(notes_list)
            print('Заметка успешно изменена\n')
        case '4':
            print('4. Удалить заметку\n')
        case '5':
            print('Завершение работы программы.')