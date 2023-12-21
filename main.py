import os
import pprint


class Note():
    # Получение списка заметок
    def get_note_list(self):
        note_list = os.listdir('notes')
        if len(note_list) == 0:
            print('Список заметок пуст!')
        else:
            for note in note_list:
                print(note)
            return note_list

    # Создание заметки
    def new_note(self):
        name = input('Введи название заметки:\n')
        note = input('Введи текст заметки:\n')
        file = open(f'notes/{name}.txt', 'a+')
        file.write(note)
        file.close()
        print(f'Заметка "{name}" создана')

    # Удаление заметки
    def remove_note(self):
        note_list = os.listdir('notes')
        if len(note_list) > 0:
            note_dict = {}
            for i in range(len(note_list)):
                note_dict[i + 1] = note_list[i]
            for i in range(len(note_dict)):
                print(f'{i + 1} - {note_dict.get(i + 1)}')
            index = input('Выбери номер заметки, которую хочешь удалить:\n')
            try:
                os.remove(f'notes/{note_dict.get(int(index))}')
                print(f"Заметка {note_dict.get(int(index))} удалена!")
            except:
                print("Не существует заметки с таким номером!")
        else:
            print("Список заметок пуст!")

    def edit_note(self):
        note_list = os.listdir('notes')
        if len(note_list) > 0:
            note_dict = {}
            for i in range(len(note_list)):
                note_dict[i + 1] = note_list[i]
            for i in range(len(note_dict)):
                print(f'{i + 1} - {note_dict.get(i + 1)}')
            index = input('Выбери номер заметки, которую хочешь изменить:\n')
            print(f'Название заметки:\n{note_dict.get(int(index))}')
            with open(f'notes/{note_dict.get(int(index))}', 'r') as f:
                print(f'\nТекст заметки:\n{f.read()}')
            position = input('\nЧто ты хочешь изменить?\n1 - название\n2 - текст\n')
            try:
                if position == str(1):
                    new_name = input('Введи новое название для заметки!\n')
                    os.rename(f'notes/{note_dict.get(int(index))}', f'notes/{new_name}.txt')
                    print(f"Заметка {note_dict.get(int(index))} изменена!")
                if position == str(2):
                    new_text = input('Введи новый текст заметки!\n')
                    flag_response = ''
                    flag = ''
                    while True:
                        flag_response = input(
                            'Как ты хочешь сохранить заметку?\n1-переписать(прежний текст будет удален!!!)\n2-'
                            'дописать\n')
                        if flag_response == str(1):
                            flag = 'w'
                            break
                        elif flag_response == str(2):
                            flag = 'a'
                            break
                        else:
                            print("Введи корректный ответ!")
                    with open(f'notes/{note_dict.get(int(index))}', flag) as file:
                        file.write(f'\n{new_text}')
                    print(f"Заметка {note_dict.get(int(index))} изменена!")
            except:
                print("Не существует заметки с таким номером!")
        else:
            print("Список заметок пуст!")

    def get_note(self):
        note_list = os.listdir('notes')
        if len(note_list) > 0:
            note_dict = {}
            for i in range(len(note_list)):
                note_dict[i + 1] = note_list[i]
            for i in range(len(note_dict)):
                print(f'{i + 1} - {note_dict.get(i + 1)}')
            index = input('Выбери номер заметки, которую хочешь посмотреть:\n')
            print(f'Название заметки:\n{note_dict.get(int(index))}')
            with open(f'notes/{note_dict.get(int(index))}', 'r') as f:
                print(f'\nТекст заметки:\n{f.read()}')
        else:
            print("Список заметок пуст!")


my_note = Note()
while True:
    answer = input(
        '\nВыбери пункт меню:\n1-Посмотреть список заметок\n2-Создать заметку\n3-Удалить заметку\n4-Редактировать заметку\n5-Посмотреть заметку\n0-Выход\n')
    if answer == str(1):
        my_note.get_note_list()
    elif answer == str(3):
        my_note.remove_note()
    elif answer == str(2):
        my_note.new_note()
    elif answer == str(4):
        my_note.edit_note()
    elif answer == str(5):
        my_note.get_note()
    elif answer == str(0):
        print('До новых встреч!))')
        break
    else:
        print('Такого пункта не существует!')
