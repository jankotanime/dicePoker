import dices
import playVariables as var
import display
import graphics.play as graphic


def movement(event):
    if var.playersStatus[var.currPlayer]["playerType"] == "player":
        if event == 'space':
            var.throwDices[var.currDice-1] = not var.throwDices[var.currDice-1]
        elif event == 'enter':
            dices.throwing(var.throwDices)
            if var.players[var.currPlayer] and var.players[var.currPlayer] != 0:
                var.currPlayer = var.currPlayer + 1
            else:
                var.currPlayer = 1
        elif event == 'left' and var.currDice != 1:
            var.currDice -= 1
        elif event == 'right' and var.currDice != 5:
            var.currDice += 1
        elif event == 'q':
            if passing():
                passConf()


def twoPlayers(event):
    movement(event)
    display.displaying(graphic.displaying())


def passing():
    return True


def passConf():
    return True


def tick(event):
    movement(event)
    display.displaying(graphic.displaying())
    print(var.currPlayer)
    print(var.playersStatus)