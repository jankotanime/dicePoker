import dices
import playVariables as var
import display
import graphics.play as graphic
import bot
import time


def movement(event):
    if var.playersStatus[var.currPlayer]["playerType"] == "player":
        if event == 'space':
            var.throwDices[var.currDice-1] = not var.throwDices[var.currDice-1]
        elif event == 'enter':
            dices.throwing(var.throwDices)
            dices.moved()
        elif event == 'left' and var.currDice != 1:
            var.currDice -= 1
        elif event == 'right' and var.currDice != 5:
            var.currDice += 1
        elif event == 'q':
            if passing():
                passConf()
    else:
        bot.move()


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
    if var.playersStatus[var.currPlayer]["playerType"] == "bot":
        time.sleep(0.5)
        tick(None)