#!/usr/bin/env python3

import json
import os.path


file_name = 'data.json'
phone_book = []

def load_data():
    global phone_book
    if not os.path.exists(file_name): return
    with open(file_name) as json_file:
        phone_book = json.load(json_file) 


def save_data():
    global phone_book
    with open(file_name, 'w') as outfile:
        json.dump(phone_book, outfile)


def get_all_data():
    global phone_book
    return phone_book


def search(search_text):
    result = [] 
    global phone_book
    for person in phone_book: 
        if search_text in person.values(): 
            result.append(person)
    return result


def add_data(data):
    global phone_book
    phone_book.append(data)