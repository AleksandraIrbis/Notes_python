import json
import datetime


def load_notes():
    try:
        with open('notes.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_notes(notes):
    with open('notes.json', 'w') as file:
        json.dump(notes, file, indent=4)


def create_note():
    note = {}
    note['id'] = len(notes) + 1
    note['title'] = input('Введите заголовок заметки: ')
    note['body'] = input('Введите текст заметки: ')
    note['timestamp'] = str(datetime.datetime.now())
    notes.append(note)
    save_notes(notes)
    print('Заметка успешно создана!')


def read_notes():
    if not notes:
        print('Список заметок пуст.')
    else:
        for note in notes:
            print(f"ID: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Текст: {note['body']}")
            print(f"Дата/Время: {note['timestamp']}")
            print()


def edit_note():
    note_id = int(input('Введите ID заметки, которую хотите отредактировать: '))
    for note in notes:
        if note['id'] == note_id:
            note['title'] = input('Введите новый заголовок заметки: ')
            note['body'] = input('Введите новый текст заметки: ')
            note['timestamp'] = str(datetime.datetime.now())
            save_notes(notes)
            print('Заметка успешно отредактирована!')
            return
    print('Заметка с указанным ID не найдена.')


def delete_note():
    note_id = int(input('Введите ID заметки, которую хотите удалить: '))
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print('Заметка успешно удалена!')
            return
    print('Заметка с указанным ID не найдена.')


notes = load_notes()

while True:
    print('Выберите действие:')
    print('1. Просмотреть список заметок')
    print('2. Создать новую заметку')
    print('3. Редактировать заметку')
    print('4. Удалить заметку')
    print('5. Выйти из программы')

    choice = input('Введите номер действия: ')

    if choice == '1':
        read_notes()
    elif choice == '2':
        create_note()
    elif choice == '3':
        edit_note()
    elif choice == '4':
        delete_note()
    elif choice == '5':
        break
    else:
        print('Неверный выбор. Попробуйте ещё раз.')

print('Программа завершена.')
