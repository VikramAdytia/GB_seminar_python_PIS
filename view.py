#!/usr/bin/env python3


def main_menu():
    return input('Выберите действие: \n1 - посмотреть справочник\n2 - найти\n3 - добавить\n4 - выход\n')

def get_search_text(): 
    return input('Введите текст для поиска: ').title()

def get_data():
    person = {}
    person['first_name'] = input('Введите имя: \n').title()
    person['last_name'] = input('Введите фамилию: \n').title()  
    person['number_phone'] = input('Введите номер телефона: \n')
    person['description'] = input('Введите описание: \n').title()
    return person


def print_person(person):
    print("-" * 20)
    print(f"Имя: {person['first_name']}")
    print(f"Фамилия: {person['last_name']}") 
    print(f"Телефон: {person['number_phone']}") 
    print(f"Описание: {person['description']}") 


def print_phonebook(phone_book):
    if not phone_book: 
        print('Справочник пустой')
        return
    for person in phone_book:
        print_person(person)
    print('\n')    


def print_searh_result(result):
    if not result: 
        print('Ничего не найдено')
        print('')
        return
    print('')
    print('Результаты поиска: \n')
    for person in result:
        print_person(person)