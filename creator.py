import Note
import os

def create_note(id):
    note = Note.Note(id)
    with open('notes.csv', 'a', encoding = 'UTF-8') as file:
        if os.stat('notes.csv').st_size == 0:
            file.write(f'{1};{note.title};{note.text};{note.data}\n')
        else:
            id += 1
            file.write(f'{id};{note.title};{note.text};{note.data}\n')