import gameInit
import graphics.menu as graphic
import display
import variables as var


# TODO: Improve the code, god look at that...
def chosing(event):
    if var.menuStatus == 1:
        if event == 'enter' or event == 'space':
            var.menuStatus = 5
        elif event == 'down':
            var.menuStatus += 1
    elif var.menuStatus == 2:
        if event == 'enter' or event == 'space':
            var.menuStatus = 3
        elif event == 'up':
            var.menuStatus -= 1
    elif var.menuStatus == 3:
        if event == 'enter' or event == 'space':
            var.menuStatus = 2
    elif var.menuStatus == 5:
        if event == 'enter' or event == 'space':
            if var.difficulty == 1:
                var.difficulty = 2
            elif var.difficulty == 2:
                var.difficulty = 3
            elif var.difficulty == 3:
                var.difficulty = 4
            else:
                var.difficulty = 1
        elif event == 'down':
            var.menuStatus += 1
    elif var.menuStatus in [6, 7, 8, 9]:
        if event == 'enter' or event == 'space':
            if var.players[var.menuStatus-6] == 0:
                var.players[var.menuStatus-6] = 1
            elif var.players[var.menuStatus-6] == 1:
                var.players[var.menuStatus-6] = 2
            else:
                var.players[var.menuStatus-6] = 0
        elif event == 'down':
            var.menuStatus += 1
        elif event == 'up':
            var.menuStatus -= 1
    elif var.menuStatus == 10:
        if event == 'enter' or event == 'space':
            var.menuStatus = 1
            var.play = True
        elif event == 'up':
            var.menuStatus -= 1
    if var.play:
        gameInit.initing()
    else:
        display.displaying(graphic.displaying_new())

