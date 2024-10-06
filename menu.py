import graphics.menu as graphic
import display
import variables as var


def chosing(event):
    if var.menuStatus == 1:
        if event == 'enter' or event == 'space':
            var.play = True
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
    display.displaying(graphic.mainMenu[var.menuStatus])
