import datetime

class Note:
    def __init__(self, id):
        self.id = id
        self.title = input('Введите заголовок заметки:\n')
        self.text = input('\nВведите заметку:\n')
        self.data = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
