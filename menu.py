import gameInit
import graphics.menu as graphic
import display
import variables as var


# TODO: Improve the code, god look at that...


def chosing(event):
    if event == 'up':
        var.menuStatus -= 1
        if var.menuStatus == 0:
            var.menuStatus = 1
        elif var.menuStatus == 1 and len(var.playersStatus) == 0:
            var.menuStatus = 2
        elif var.menuStatus == 4:
            var.menuStatus = 5
    elif event == 'down':
        var.menuStatus += 1
        if var.menuStatus == 4:
            var.menuStatus = 3
        elif var.menuStatus == 11:
            var.menuStatus = 10
    elif event == 'enter' or event == 'space':
        if var.menuStatus == 1:
            var.menuStatus = 1
        elif var.menuStatus == 2:
            var.menuStatus = 5
        elif var.menuStatus == 3:
            var.menuStatus = 3
        elif var.menuStatus == 5:
            if var.difficulty in [1, 2, 3]:
                var.difficulty += 1
            else:
                var.difficulty = 1
        elif var.menuStatus in [6, 7, 8, 9]:
            if var.players[var.menuStatus-6] == 0:
                var.players[var.menuStatus-6] = 1
            elif var.players[var.menuStatus-6] == 1:
                var.players[var.menuStatus-6] = 2
            else:
                var.players[var.menuStatus-6] = 0
        elif var.menuStatus == 10:
            var.play = True
    if var.play:
        gameInit.initing()
    else:
        display.displaying(graphic.displaying())



