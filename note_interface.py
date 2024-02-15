import note_printer, note_reader, note_creator
import note_changer, note_writer, note_remover, selector_by_data

def run():
    command = 0
    notes_dict = note_reader.read_notes()
    isChanged = False

    while command != '7':
        print('Меню пользователя\n'
            '1. Вывод списка заметок на экран\n'
            '2. Вывести заметку по id\n'
            '3. Найти заметки по дате создания/изменения\n'
            '4. Добавить новую заметку\n'
            '5. Изменить существующую заметку\n'
            '6. Удалить заметку\n'
            '7. Выход из программы\n')
        
        command = input('Введите номер пункта меню: ')
        print()
        while command not in ('1', '2', '3', '4', '5', '6', '7'):
            print('Некорректный ввод пункта меню. Повторите ввод.\n')
            command = input('Выберете пункт меню: ')

        match command:
            case '1':
                note_printer.print_all(notes_dict)
            case '2':
                note_printer.print_one(notes_dict)
            case '3':
                selector_by_data.select_by_data(notes_dict)
            case '4':
                note_creator.create_note(notes_dict)
                isChanged = True
                print('\nНовая заметка успешно добавлена.\n')
            case '5':
                note_changer.change_note(notes_dict)
                isChanged = True
                print('\nЗаметка успешно изменена\n')
            case '6':
                note_remover.remove_note(notes_dict)
                isChanged = True
                print('\nЗаметка успешно удалена\n')
            case '7':
                if isChanged: note_writer.write_notes(notes_dict)
                print('\nЗавершение работы программы.')