import os


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def displaying(element):
    clear_terminal()
    print(element)