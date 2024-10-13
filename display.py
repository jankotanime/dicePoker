import os


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def displaying(element):
    clear_terminal()
    print(element)


# Wielkosc ekranu 61 x 
