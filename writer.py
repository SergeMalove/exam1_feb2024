def write_notes(notes_dict):
    with open('notes.csv', 'w', encoding = 'UTF-8') as file:
        for id in notes_dict:
            file.write(f'{id};{notes_dict[id][0]};{notes_dict[id][1]};{notes_dict[id][2]}\n')