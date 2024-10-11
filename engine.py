# Main game file - loop that makes ticks every keyboard event. Picks in which state program should be

import keyboard
import play
import menu
import variables as var
import variables as playvar
import gameInit as init

useableEvents = ['up', 'down', 'left', 'right', 'space', 'enter', 'q', 'v']


menu.chosing(None)


while var.engine:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        if event.name == 'esc':
            var.engine = False
        elif event.name in useableEvents:
            if playvar.play:
                play.tick(event.name)
            elif playvar.endScreen:
                if event.name == 'enter':
                    playvar.endScreen = False
            else:
                menu.chosing(event.name)
print("Program shutting down...")
