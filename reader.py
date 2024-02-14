import csv
import os

def read_notes():
    notes_dict = {}
    if os.path.exists('notes.csv'):
        with open('notes.csv', 'r', encoding = 'UTF-8') as file:
            file_reader = csv.reader(file, delimiter=";")
            for row in file_reader:
                notes_dict[row[0]] = [row[1], row[2], row[3]]
    return notes_dict