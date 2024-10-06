import keyboard
import os
import menu
import variables as var

useableEvents = ['up', 'down', 'left', 'right', 'space', 'enter']


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def tick(event):
    print(event.name)


while var.engine:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        if event.name == 'esc':
            var.engine = False
        elif event.name in useableEvents:
            if var.play:
                tick(event)
            else:
                menu.chosing(event.name)
print("Program shutting down...")

