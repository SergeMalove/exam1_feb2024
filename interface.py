import printer, reader, creator, changer, writer, remover

command = 0
notes_dict = reader.read_notes()
#max_id = 0 if len(notes_dict) == 0 else int(max(notes_dict.keys()))

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

    match command:
        case '1':
            printer.print_notes(notes_dict)
        case '2':
            creator.create_note(notes_dict)
            #max_id += 1
            print('\nНовая заметка успешно добавлена.\n')
        case '3':
            changer.change_note(notes_dict)
            #writer.write_notes(notes_dict)
            print('Заметка успешно изменена\n')
        case '4':
            remover.remove_note(notes_dict)
            #writer.write_notes(notes_dict)
            print('Заметка успешно удалена\n')
        case '5':
            writer.write_notes(notes_dict)
            print('Завершение работы программы.')

# Для оптимизации и ускорения работы код "writer.write_notes(notes_dict)" в case 3 и 4 можно вынести в case 5