#!/usr/bin/env python3

import view
import model


def button_click():
    model.load_data()
    while True:
        action = view.main_menu() 
          
        match action:
            case '1': view.print_phonebook(model.get_all_data())
            case '2': view.print_searh_result(model.search(view.get_search_text()))
            case '3': 
                model.add_data(view.get_data()) 
                model.save_data()
            case '4': return 
            case _: print('Некорректный ввод. Повторите команду')        
