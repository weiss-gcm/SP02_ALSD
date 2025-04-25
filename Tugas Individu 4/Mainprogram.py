from menu_class_stack import menu_stack
from menu_class_queue import menu_queue
from sys import exit

def menu_utama():
    pengulangan = True
    while pengulangan:
        print("Menu Utama")
        print("1. Stack")
        print("2. Queue")
        print("3. Keluar")
        menu = input("Pilih Menu: ")
        if menu == "1":
            menu_stack()
        elif menu == "2":
            menu_queue()
        elif menu == "3":
            pengulangan = False
        else:
            print("Menu diluar jangkauan, tidak ada di daftar")
            exit
    
menu_utama()
