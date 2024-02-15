import note

def create_note(notes_dict):
    id = 0 if len(notes_dict) == 0 else int(max(notes_dict.keys()))
    id += 1
    new_note = note.Note(id)
    notes_dict[id] = [new_note.title, new_note.text, new_note.data]