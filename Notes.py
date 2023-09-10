import json
import os
import datetime

notes_file = "notes.json"

def load_notes():
    if os.path.exists(notes_file):
        with open(notes_file, "r") as file:
            return json.load(file)
    else:
        return []

def save_notes(notes):
    with open(notes_file, "w") as file:
        json.dump(notes, file, indent=4)

def add_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    note = {
        "id": len(notes) + 1,
        "title": title,
        "body": body,
        "timestamp": str(datetime.datetime.now())
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка добавлена.")

def list_notes():
    if not notes:
        print("Список заметок пуст.")
    else:
        for note in notes:
            print(f"{note['id']}. {note['title']} ({note['timestamp']})")

def edit_note():
    note_id = int(input("Введите ID заметки, которую вы хотите отредактировать: "))
    for note in notes:
        if note["id"] == note_id:
            new_title = input("Введите новый заголовок заметки: ")
            new_body = input("Введите новый текст заметки: ")
            note["title"] = new_title
            note["body"] = new_body
            note["timestamp"] = str(datetime.datetime.now())
            save_notes(notes)
            print("Заметка отредактирована.")
            return
    print(f"Заметка с ID {note_id} не найдена.")

def delete_note():
    note_id = int(input("Введите ID заметки, которую вы хотите удалить: "))
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка удалена.")
            return
    print(f"Заметка с ID {note_id} не найдена.")

if __name__ == "__main__":
    notes = load_notes()

    while True:
        print("\nВыберите действие:")
        print("1. Добавить заметку")
        print("2. Просмотреть список заметок")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")
        choice = input("Введите номер действия: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            list_notes()
        elif choice == "3":
            edit_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")