import note_printer, note_reader, note_creator, note_changer, note_writer, note_remover

def run():
    command = 0
    notes_dict = note_reader.read_notes()

    while command != '6':
        print('Меню пользователя\n'
            '1. Вывод списка заметок на экран\n'
            '2. Вывести заметку по id\n'
            '3. Добавить новую заметку\n'
            '4. Изменить существующую заметку\n'
            '5. Удалить заметку\n'
            '6. Выход из программы\n')
        
        command = input('Введите номер пункта меню: ')
        print()
        while command not in ('1', '2', '3', '4', '5', '6'):
            print('Некорректный ввод пункта меню. Повторите ввод.')
            command = input('Выберете пункт меню: ')

        match command:
            case '1':
                note_printer.print_all(notes_dict)
            case '2':
                note_printer.print_note(notes_dict)
            case '3':
                note_creator.create_note(notes_dict)
                print('\nНовая заметка успешно добавлена.\n')
            case '4':
                note_changer.change_note(notes_dict)
                print('Заметка успешно изменена\n')
            case '5':
                note_remover.remove_note(notes_dict)
                print('Заметка успешно удалена\n')
            case '6':
                note_writer.write_notes(notes_dict)
                print('Завершение работы программы.')