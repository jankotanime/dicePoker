import keyboard
import play
import menu
import variables as var

useableEvents = ['up', 'down', 'left', 'right', 'space', 'enter']


menu.chosing(None)


while var.engine:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        if event.name == 'esc':
            var.engine = False
        elif event.name in useableEvents:
            if var.play:
                play.tick(event.name)
            else:
                menu.chosing(event.name)
print("Program shutting down...")

