import gameInit
import graphics.menu as graphic
import display
import variables as var

# Function that changes menu status
def chosing(event):
    if event == 'up' and var.menuStatus not in [1, 4, 5] and (var.menuStatus != 2 or len(var.playersStatus) != 0):
        var.menuStatus -= 1
    elif event == 'down' and var.menuStatus not in [3, 4, 10]:
        var.menuStatus += 1
    elif event == 'enter' or event == 'space':
        if var.menuStatus == 1:
            var.play = True
            gameInit.continuing()
        elif var.menuStatus == 2:
            var.menuStatus = 5
        elif var.menuStatus == 3:
            var.menuStatus = 4
        elif var.menuStatus == 4:
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
            gameInit.initing()
    if not var.play:
        display.displaying(graphic.displaying())



