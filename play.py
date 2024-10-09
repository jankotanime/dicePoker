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
            passing(event)
    else:
        bot.move()


def twoPlayers(event):
    movement(event)
    display.displaying(graphic.displaying())


def passing(event):
    var.passing = False
    if event == 'enter':
        var.playersStatus[var.currPlayer]["moves"] = 0


def tick(event):
    actPlayer = var.playersStatus[var.currPlayer]
    if actPlayer["moves"] > 0:
        movement(event)
    else:
        dices.moved()
    display.displaying(graphic.displaying())
    print(var.currPlayer)
    print(var.playersStatus)
    endGame = any(var.playersStatus[x]["moves"] > 0 for x in var.playersStatus)
    if ((actPlayer["playerType"] == "bot" and actPlayer["moves"] > 0) or actPlayer["moves"] <= 0) and endGame:
        time.sleep(0.5)
        tick(None)