import json


def add_contact(phone_book, name, phone_numbers):
    phone_book[name] = phone_numbers


def remove_contact(phone_book, name):
    if name in phone_book:
        del phone_book[name]


def view_contacts(phone_book):
    if phone_book:
        for name, phone_numbers in phone_book.items():
            print(f"Имя: {name}")
            print("Номера телефонов:")
            for phone_number in phone_numbers:
                print(phone_number)
            print()
    else:
        print("Телефонная книга пуста.\n")

def search_contact(phone_book, name):
    if name in phone_book:
        print(f"Имя: {name}")
        print("Номера телефонов:")
        for phone_number in phone_book[name]:
            print(phone_number)
        print()
    else:
        print("Контакт не найден.\n")


def update_contact(phone_book, name):
    if name in phone_book:
        new_phone_numbers = input("Введите новые номера телефонов через запятую: ").split(',')
        phone_book[name] = new_phone_numbers
        print("Контакт обновлен\n")
    else:
        print("Контакт не найден.\n")


def load_phone_book(file_name):
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


phone_book = load_phone_book('phone_book.txt')

while True:
    print("1. Добавить контакт")
    print("2. Удалить контакт")
    print("3. Просмотреть все контакты")
    print("4. Поиск контакта")
    print("5. Изменить контакт")
    print("6. Выход")

    choice = input("Выберите действие (1-6): ")

    if choice == '1':
        name = input("Введите имя контакта: ")
        phone_numbers = input("Введите номера телефонов через запятую : ").split(',')
        add_contact(phone_book, name, phone_numbers)
        print("Контакт добавлен\n")
        with open('phone_book.txt', 'w') as file:
            json.dump(phone_book, file)
    elif choice == '2':
        name = input("Введите имя контакта для удаления: ")
        remove_contact(phone_book, name)
        print("Контакт удален\n")
        with open('phone_book.txt', 'w') as file:
            json.dump(phone_book, file)
    elif choice == '3':
        view_contacts(phone_book)
    elif choice == '4':
        name = input("Введите имя контакта для поиска: ")
        search_contact(phone_book, name)
    elif choice == '5':
        name = input("Введите имя контакта для изменения: ")
        update_contact(phone_book, name)
        with open('phone_book.txt', 'w') as file:
            json.dump(phone_book, file)
    elif choice == '6':
        print("Довай До свидания!")
        break
    else:
        print("Ощибка ЕПТА\n")


