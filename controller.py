import menu
#import operation as operation
import sys

def button_click():
    menuList=["Добавить запись -->","Посмотреть записи -->","Выход -->"]
    menuChoice = menu.DrawMenu(menuList)
    match menuChoice[0]:
        case '1':
            print("TBD")
            # operation.AddRecord()
        case '2':
            print("TBD")
            # operation.ViewRecord()
        case '3':
            sys.exit