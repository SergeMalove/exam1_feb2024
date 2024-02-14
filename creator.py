import Note
import os

def create_note(notes_dict):
    id = 0 if len(notes_dict) == 0 else int(max(notes_dict.keys()))
    id += 1
    note = Note.Note(id)
    notes_dict[id] = [note.title, note.text, note.data]

    # with open('notes.csv', 'a', encoding = 'UTF-8') as file:
    #     if os.stat('notes.csv').st_size == 0:
    #         file.write(f'{1};{note.title};{note.text};{note.data}\n')
    #     else:
    #         id += 1
    #         file.write(f'{id};{note.title};{note.text};{note.data}\n')