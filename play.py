import dicesManage as dices
import playVariables as var
import display
import graphics.play as graphic
import bot
import time


def movement(event):
    if var.playersStatus[var.currPlayer]["playerType"] == "player":
        if not var.passing:
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
                var.passing = True
        else:
            dices.passing(event)
    else:
        bot.move()


def twoPlayers(event):
    movement(event)
    display.displaying(graphic.displaying())


def actPlayer():
    return var.playersStatus[var.currPlayer]


def endGame():
    var.endScreen = True
    var.play = False


def tick(event):
    isAnyPlayer = any(var.playersStatus[x]["moves"] > 0 for x in var.playersStatus)
    if not isAnyPlayer:
        endGame()
    if actPlayer()["moves"] > 0:
        movement(event)
        display.displaying(graphic.displaying())
        if actPlayer()["playerType"] == "bot":
            tick(None)
    else:
        dices.moved()
    display.displaying(graphic.displaying())
    print(var.currPlayer)
    print(var.playersStatus)