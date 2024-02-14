import Note

def create_note(notes_dict):
    id = 0 if len(notes_dict) == 0 else int(max(notes_dict.keys()))
    id += 1
    note = Note.Note(id)
    notes_dict[id] = [note.title, note.text, note.data]